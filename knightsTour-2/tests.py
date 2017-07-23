#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import knightsTour as KN

#   Limited tests as C function only takes a fixed board size atm
#   to change this you must edit the knightsTour.h file and re-install.

def c_tests():
    "Test the implimentation with C bindings"
    size = 8 # currently C implimentation is of this fixed size.
    S2 = size**2
    indicies = range(size)
    possibleStarts = ((x, y) for x in indicies for y in indicies)
    fails = set()
    for start in possibleStarts:
        tour = KN.knightsTour(start, size)
        try:
            assert len(tour) == S2
        except AssertionError:
            fails.add(start)
    print(fails)
    T = S2 - len(fails)
    return ("{}/{} tests pass ({}%)".format(T, S2, (T / S2 * 100)) )


if __name__ == '__main__':
    print(c_tests())

"""
Results so far:

8 x 8 board: 60/64 tests pass (93.75%)
    Fail Positions: set([(5, 6), (7, 6), (1, 3), (3, 4)])

    Time: 0.001 seconds

32 x 32 board: 1000/1024 tests pass (97.65625%)
    Fail Positions: set([(18, 26), (30, 31), (17, 16), (11, 10), (4, 9), (11, 12), 
                        (0, 11), (11, 22), (29, 22), (6, 25), (25, 22), (8, 15), 
                        (29, 26), (18, 2), (28, 10), (9, 3), (9, 16), (14, 2), 
                        (21, 18), (25, 28), (15, 17), (10, 16), (18, 7), (0, 31)])


64 x 64 Couldnt be bothered to wait the estimated 16 mins for all the tests.
    Time: 5 function calls in 0.235 seconds
        ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1       0.005    0.005    0.235    0.235 knightsTour.py:13(<module>)
        1       0.000    0.000    0.230    0.230 knightsTour.py:16(knightsTour)
        1       0.230    0.230    0.230    0.230 {cKnightsTour.KnightsTour}
        1       0.000    0.000    0.000    0.000 {len}


100 x 100 Just time test: 5 function calls in 1.339 seconds
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.011    0.011    1.339    1.339 knightsTour.py:13(<module>)
        1    0.000    0.000    1.328    1.328 knightsTour.py:16(knightsTour)
        1    1.328    1.328    1.328    1.328 {cKnightsTour.KnightsTour}
        1    0.000    0.000    0.000    0.000 {len}
"""