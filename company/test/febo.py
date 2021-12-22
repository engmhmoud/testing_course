from functools import lru_cache

cache = {}


def feb(n: int):
    if n == 0:
        return 0
    if n < 2:
        return 1
    else:
        return feb(n - 1) + feb(n - 2)


def cached_feb(n: int):
    if cache.get(n):
        return cache[n]

    if n == 0:
        return 0
    if n < 2:
        return 1

    else:
        res = feb(n - 1) + feb(n - 2)
        cache[n] = res
        return res


@lru_cache(maxsize=255)
def cached_lru_feb(n: int):
    if n == 0:
        return 0
    if n < 2:
        return 1
    else:
        return feb(n - 1) + feb(n - 2)

    pass
