from typing import Callable

import pytest
from fixtures import time_tracker

from febo import cached_feb, cached_lru_feb, feb


def handle_parameters(argnames, argvalues):
    print(argnames, type(argnames))
    print(argvalues, type(argvalues))
    print("*" * 20)
    result = []

    for val in argvalues:

        print(val, type(val))
        print("*" * 20)
        _val = list(val)

        item = {}
        for i, v in zip(argnames, _val):
            print(i, type(i))
            print(v, type(v))
            print("*" * 20)
            item[i] = v

        result.append(item)

    return result


def my_parameterize(argnames, argvalues):
    args = handle_parameters(argnames=argnames, argvalues=argvalues)

    def decorator(function):
        def run_func():
            for arg in args:

                function(**arg)

        return run_func()

    return decorator


# @pytest.mark.parametrize(


@pytest.mark.parametrize(argnames=["n", "result"], argvalues=[(0, 0), (1, 1), (2, 1), (3, 2), (25, 75025)])
def test_feb(n: int, result: int):
    assert feb(n) == result


@pytest.mark.parametrize(argnames=["n", "result"], argvalues=[(0, 0), (1, 1), (2, 1), (3, 2), (25, 75025)])
def test_cached_feb(n: int, result: int):
    assert cached_feb(n) == result


@pytest.mark.parametrize(argnames=["n", "result"], argvalues=[(0, 0), (1, 1), (2, 1), (3, 2), (25, 75025)])
def test_cached_feb_lru(n: int, result: int):
    assert cached_lru_feb(n) == result


@pytest.mark.parametrize(argnames=["n", "result"], argvalues=[(0, 0), (1, 1), (2, 1), (3, 2), (25, 75025)])
@pytest.mark.parametrize("feb_fnc", [test_feb, test_cached_feb, test_cached_feb_lru])
def test_all_feb(time_tracker, feb_fnc: Callable[[int, int], int], n: int, result: int):
    # res = feb_fnc(n)
    # assert res == result
    feb_fnc(n, result)
