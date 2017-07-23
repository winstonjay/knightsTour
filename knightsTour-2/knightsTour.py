#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Knights Tour 

Info about the Knights Tour problem as described by wikipedia:

A knight's tour is a sequence of moves of a knight on a chessboard such that 
the knight visits every square only once. If the knight ends on a square that 
is one knight's move from the beginning square (so that it could tour the board 
again immediately, following the same path), the tour is closed, otherwise it 
is open.
"""
import cKnightsTour as cKT

def knightsTour(start, size=8):
    """Takes tuple and integer as input; returns a vaild knights tour or fails 
    from a give start position on a n x n chessboard.
    knightsTour((x,y), n) -> [(x,y), (x1,y1), (x2,y2), ...]"""
    knightsTour.size = size 
    try: # check function is called with valid start position
        sX, sY = start
        assert (0 <= sX < knightsTour.size)
        assert (0 <= sY < knightsTour.size)
    except AssertionError:
        raise AssertionError(
                "Start position must be within bounds of board size"
                "based on zero based indcies; range = 0 to n-1"
            )
    return cKT.KnightsTour(sX, sY) # Value returned from C function

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        start = (int(sys.argv[1]), int(sys.argv[2]))
    else:
        start = (0, 0)

    print(knightsTour(start))