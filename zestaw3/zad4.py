import functools
from secrets import randbelow

def pamiec(func):
    series = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args not in series:
            temp = func(*args, **kwargs)
            series[temp] = temp
            return temp
        return series[args]

    return wrapper

@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n-1) + fibonacci(n-2)

for i in range(100):
    print(str(i) + " -- " + str(fibonacci(i)))
