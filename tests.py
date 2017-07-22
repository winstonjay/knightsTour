#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import json


import knightsTour as KT
import numpy as np

"""
Knights Tour Test Suite.

For testing multiple size boards at once the tests shell program should 
be used as the tests function fails to produce accurate results in large loops 
spanning accross significanlty sized boards.

Current tests will check possible tours from any start position on a given board
size, check for interval errors in each tour, log all the start positions that 
make a closed tour and log time and failed tours.

A report is created in json format.
"""

def tests(size):
    """For a given size check if all the start positions
    return valid solutions"""
    TITLE = KT.knightsTour.__name__.upper()
    REPORT = {
        TITLE            : "{}X{}".format(size, size),
        "_N"             : size,
        "_PASS"          : True,
        "_FAIL COUNT"    : 0,
        "_TEST COUNT"    : size**2,
        "_FALSE STARTS"  : [],
        "_AVG TIME"      : 0,
        "_INTERVAL ERRS" : 0,
        "_CLOSED TOURS"  : [],
        "_CLOSED COUNT"  : 0
    }
    TIMES = []

    indicies = range(size)
    possibleStarts = ((x, y) for x in indicies for y in indicies)

    for start in possibleStarts:
        t0 = time.clock()
        TOUR = KT.knightsTour(start, size)
        t1 = time.clock()
        TIMES.append((t1 - t0))
        try:
            assert len(TOUR) == size**2

            end = TOUR[-1]
            if tuple(np.subtract(start, end)) in KT.deltas:
                REPORT["_CLOSED TOURS"].append(start)
                REPORT["_CLOSED COUNT"] += 1
                

        except AssertionError:
            REPORT["_PASS"] = False
            REPORT["_FAIL COUNT"] += 1
            REPORT["_FALSE STARTS"].append(start)


        d1, d2, d3, d4, d5, d6, d7, d8 = KT.deltas
        INTERVALS = (tuple(np.subtract(a, b)) for a, b in zip(TOUR[0::2], TOUR[1::2]))
        for I in INTERVALS:
            try:
                assert (I == d1 or I == d2 or I == d3 or I == d4 or 
                        I == d5 or I == d6 or I == d7 or I == d8)
            except AssertionError:
                REPORT["_PASS"] = False
                REPORT["_INTERVAL ERRS"] += 1

    REPORT["_AVG TIME"] = round((sum(TIMES) / size**2), 6)
    return json.dumps(REPORT)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2: 
        print tests(int(sys.argv[1]))


