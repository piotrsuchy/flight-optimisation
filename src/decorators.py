import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Duration of {func.__name__} is {end_time - start_time}")
        return result
    return wrapper
