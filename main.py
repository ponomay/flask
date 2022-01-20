import time


def speed_calc_decorator(function_name):
    def wrapped():
        before_time = time.time()
        function_name()
        after_time = time.time()
        print(f'Time taken to run {function_name.__name__}: {after_time - before_time}s')
    return wrapped


@speed_calc_decorator
def fast_function():
    for i in range(100000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(1000000):
        i * i


f = fast_function()
slow_function()
