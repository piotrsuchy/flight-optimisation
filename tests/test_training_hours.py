import unittest
from src.allowed_approach.classes.crew_member import FlightAttendant

class TestFlightAttendant(unittest.TestCase):

    def test_training_hours_within_range(self):
        """ Test if training_hours is within the expected range (0 to 744) """
        attendants = [FlightAttendant() for _ in range(10)]
        for attendant in attendants:
            self.assertGreaterEqual(attendant.training_hours[0], 0)
            self.assertLessEqual(attendant.training_hours[1], 744)

    def test_training_hours_duration(self):
        """ Test if the duration of training_hours is always 24 hours """
        attendant = FlightAttendant("SomeBase")
        duration = attendant.training_hours[1] - attendant.training_hours[0]
        self.assertEqual(duration, 24)

    def test_training_hours_not_the_same(self):
        """ Test if training_hours is within the expected range (0 to 744) """
        attendants = [FlightAttendant() for _ in range(2)]
        self.assertNotEqual(attendants[0].training_hours[0], attendants[1].training_hours[0])

if __name__ == '__main__':
    unittest.main()
