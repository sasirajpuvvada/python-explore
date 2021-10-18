import time
from functools import lru_cache

'''
 lru_cache decorator caches the computed result

 maxsize represents no. of results you can store

 LRU - least recently used
'''


@lru_cache(maxsize=3)
def fibonacci_cache(n) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)

def fibonacci(n) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("**** Using Cache ****")
start_time = time.time()
ans = fibonacci_cache(37)
print(ans)
print(time.time() - start_time)

print("**** Without Cache ****")
start_time = time.time()
ans = fibonacci(37)
print(ans)
print(time.time() - start_time)