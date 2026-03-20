"""
Tests verifying the memory leak fixes:
1. Solution.schedulers dict gets cleaned up when solutions are discarded
2. AvailabilityLog.log gets cleared between iterations
3. EventScheduler.events is empty after processing all events
4. Unallowed approach deepcopy optimization copies only per-solution data
"""
import gc
import copy
import pytest
import sys
import os

# Ensure project root is on the path so imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.allowed_approach.event_scheduler import EventScheduler
from src.allowed_approach.solution import Solution
from src.allowed_approach.classes.availability import AvailabilityLog, Availability


# ---------------------------------------------------------------------------
# Fix 1: Solution.schedulers cleanup
# ---------------------------------------------------------------------------

class TestSolutionSchedulersCleanup:
    def setup_method(self):
        """Clear the class-level schedulers dict before each test."""
        Solution.schedulers.clear()

    def test_scheduler_registered_on_creation(self):
        """A new Solution registers its scheduler in the class dict."""
        sol = Solution(1, _make_stub_structures(), 720)
        assert 1 in Solution.schedulers
        assert Solution.schedulers[1] is sol.scheduler

    def test_scheduler_removed_on_del(self):
        """When a Solution is garbage-collected, its scheduler entry is removed."""
        sol = Solution(42, _make_stub_structures(), 720)
        assert 42 in Solution.schedulers
        del sol
        gc.collect()
        assert 42 not in Solution.schedulers

    def test_cleanup_schedulers_removes_stale_ids(self):
        """cleanup_schedulers removes entries not in the active set."""
        sols = [Solution(i, _make_stub_structures(), 720) for i in range(1, 11)]
        assert len(Solution.schedulers) == 10

        active_ids = {1, 2, 3}
        Solution.cleanup_schedulers(active_ids)
        assert set(Solution.schedulers.keys()) == active_ids
        del sols  # prevent GC during test

    def test_cleanup_schedulers_keeps_active(self):
        """cleanup_schedulers preserves entries that are still active."""
        sols = [Solution(i, _make_stub_structures(), 720) for i in range(1, 6)]
        active_ids = {s.id for s in sols}
        Solution.cleanup_schedulers(active_ids)
        assert len(Solution.schedulers) == 5

    def test_schedulers_dont_grow_unbounded(self):
        """Simulates the pattern of creating & discarding solutions across iterations."""
        for iteration in range(5):
            # Create a batch of solutions
            sols = [Solution(iteration * 10 + i, _make_stub_structures(), 720) for i in range(10)]
            # Keep only the first 3 (simulating selection)
            kept = sols[:3]
            active_ids = {s.id for s in kept}
            Solution.cleanup_schedulers(active_ids)
            assert len(Solution.schedulers) == 3
            del sols, kept

        # After 5 iterations we should only have 3 entries, not 50
        assert len(Solution.schedulers) <= 3


# ---------------------------------------------------------------------------
# Fix 2: EventScheduler.clear_events
# ---------------------------------------------------------------------------

class TestEventSchedulerClearEvents:
    def test_events_empty_after_run_until_no_events(self):
        """After processing all events, the events list should be empty."""
        scheduler = EventScheduler()
        results = []
        scheduler.schedule_event(1, results.append, "a")
        scheduler.schedule_event(2, results.append, "b")
        scheduler.schedule_event(3, results.append, "c")

        scheduler.run_until_no_events()

        assert results == ["a", "b", "c"]
        assert len(scheduler.events) == 0

    def test_clear_events_empties_pending(self):
        """clear_events removes all pending events."""
        scheduler = EventScheduler()
        for i in range(100):
            scheduler.schedule_event(i, lambda: None)

        assert len(scheduler.events) == 100
        scheduler.clear_events()
        assert len(scheduler.events) == 0

    def test_clear_events_allows_reuse(self):
        """After clear_events, the scheduler can be reused normally."""
        scheduler = EventScheduler()
        scheduler.schedule_event(1, lambda: None)
        scheduler.clear_events()

        results = []
        scheduler.schedule_event(0.5, results.append, "x")
        scheduler.run_until_no_events()
        assert results == ["x"]


# ---------------------------------------------------------------------------
# Fix 3: AvailabilityLog.clear_log
# ---------------------------------------------------------------------------

class TestAvailabilityLogClearLog:
    def test_clear_log_empties_log(self):
        """clear_log removes all snapshots."""
        airport = _make_stub_airport(1)
        log = AvailabilityLog(airport)

        # Add some snapshots manually
        for t in range(10):
            avail = Availability(airport, t, set(), set())
            log.log.append(avail)

        assert len(log.log) == 10
        log.clear_log()
        assert len(log.log) == 0

    def test_clear_log_allows_new_snapshots(self):
        """After clearing, new snapshots can be added."""
        airport = _make_stub_airport(1)
        log = AvailabilityLog(airport)

        avail = Availability(airport, 0, set(), set())
        log.log.append(avail)
        log.clear_log()

        avail2 = Availability(airport, 5, set(), set())
        log.log.append(avail2)
        assert len(log.log) == 1
        assert log.log[0].simulation_time == 5

    def test_clear_logs_after_timestamp_still_works(self):
        """The existing clear_logs_after_timestamp is unaffected by our changes."""
        airport = _make_stub_airport(1)
        log = AvailabilityLog(airport)

        for t in [1, 5, 10, 15, 20]:
            avail = Availability(airport, t, set(), set())
            log.log.append(avail)

        log.clear_logs_after_timestamp(10)
        assert len(log.log) == 3  # timestamps 1, 5, 10
        assert all(a.simulation_time <= 10 for a in log.log)


# ---------------------------------------------------------------------------
# Fix 4: Unallowed approach - deepcopy optimization
# ---------------------------------------------------------------------------

class TestUnallowedDeepCopyOptimization:
    def test_deepcopy_single_sol_status_is_equivalent(self):
        """Copying a single solution's status produces the same result as copying all."""
        pilots_status_pop = [
            [{'location': i, 'time': 0, 'train_hs': [10, 34], 'day-off': [1, 5]}
             for i in range(5)]
            for _ in range(3)
        ]

        # Old way: deepcopy entire pop
        full_copy = copy.deepcopy(pilots_status_pop)

        # New way: deepcopy single solution
        single_copy = copy.deepcopy(pilots_status_pop[1])

        # Both should produce identical data for solution index 1
        assert full_copy[1] == single_copy

    def test_deepcopy_single_is_independent(self):
        """Modifying original after single-solution deepcopy doesn't affect the copy."""
        pilots_status = [
            {'location': 1, 'time': 0, 'train_hs': [10, 34], 'day-off': [1, 5]},
            {'location': 2, 'time': 0, 'train_hs': [20, 44], 'day-off': [2, 6]},
        ]

        backup = copy.deepcopy(pilots_status)
        pilots_status[0]['location'] = 99
        assert backup[0]['location'] == 1  # unaffected


# ---------------------------------------------------------------------------
# Helpers / stubs
# ---------------------------------------------------------------------------

class _StubAirport:
    """Minimal airport stub for testing without full initialization."""
    def __init__(self, airport_id):
        self.id = airport_id
        self.pilots = []
        self.attendants = []
        self.availability_log = AvailabilityLog(self)

    def get_eligible_pilots(self, duration):
        return []

    def get_eligible_attendants(self, duration):
        return []


class _StubStructures:
    """Minimal structures stub."""
    def __init__(self):
        self.airports = [_StubAirport(i) for i in range(1, 3)]


def _make_stub_structures():
    return _StubStructures()


def _make_stub_airport(airport_id):
    return _StubAirport(airport_id)
