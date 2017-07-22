"""
Knights Tour 

Info about the Knights Tour problem as described by wikipedia:

A knight's tour is a sequence of moves of a knight on a chessboard such that 
the knight visits every square only once. If the knight ends on a square that 
is one knight's move from the beginning square (so that it could tour the board 
again immediately, following the same path), the tour is closed, otherwise it 
is open.
"""

def knightsTour(start, size=8):
    """Takes tuple and integer as input; returns a vaild knights tour or fails 
    from a give start position on a n x n chessboard.
    knightsTour((x,y), n) -> [(x,y), (x1,y1), (x2,y2), ...]"""
    knightsTour.size = size 
    goalState = size**2
    try: # check function is called with valid start position
        sX, sY = start
        assert (0 <= sX < knightsTour.size)
        assert (0 <= sY < knightsTour.size)
    except AssertionError:
        raise AssertionError(
                "Start position must be within bounds of board size",
                "based on zero based indcies; range = 0 to n-1"
            ) 
    TOUR = DFSearch(nodeSuccessors, sortedNodes, start)
    return TOUR

def DFSearch(graph, heuristic, node):
    """Takes Tuple and list of tuples; variation of a depth-first-search
    optimised by Warnsdoffs rule. If program meets a dead end, it will back
    track into alternative good branches.""" 
    DFSearch.path = [] 
    DFSearch.branches = []
    backtracks = set()
    while node not in DFSearch.path:
        DFSearch.path.append(node)
        if len(DFSearch.path) == knightsTour.size **2:
            return DFSearch.path
        successors = graph(node)
        if successors: 
            node = heuristic(successors)
        elif DFSearch.branches:
            node, backtracks = backtrack(backtracks)

    return Fail 

Fail = []

def backtrack(backtracks):
    """Checks for alternative branches and checks to see if they have not
    already been backtracked to. then returns the new backtracks and
    a new choice to choose from. Some problems are none in this function
    and the backtacking method but haven't been fully specified."""
    oldChoice, newChoice = DFSearch.branches.pop()
    while newChoice not in backtracks and DFSearch.branches:
        oldChoice, newChoice = DFSearch.branches.pop()
    backtracks.add(newChoice)
    DFSearch.path = DFSearch.path[:DFSearch.path.index(oldChoice)]
    return newChoice, backtracks

def nodeSuccessors(node):
    """Takes tuple as input; returns list of valid moves from the current 
    position. A valid move is defined as a delta increment that is within
    the bounds of the board and not already in our explored path.
    nodeSuccessors( (x, y) ) -> [(x1, y1), (x2, y2), ...]"""
    X, Y = node
    return ([(X + x, Y + y) for x, y in deltas      
              if  (0 <= X + x < knightsTour.size)                  
              and (0 <= Y + y < knightsTour.size)                  
              and not (X + x, Y + y) in DFSearch.path]) 

deltas = [(-2, 1), (-2,-1), (-1,-2), ( 1,-2), # possible moves by increment
          ( 2,-1), ( 2, 1), ( 1, 2), (-1, 2)] # that a knight peice can make.

def sortedNodes(nodes):
    """Sorts nodes in acordance with Warnsdoffs Rule. In case of a tie eucledian
    distance from the center of the board is used to break the tie. if this also 
    returns more than one equal value the first generated is selected and the rest
    are added to the DFSearch.branches for possible backtracking if the first path 
    were to fail."""
    sortedN = sorted([(len(nodeSuccessors(n)), n) for n in nodes])
    sortedN = [n for rank, n in sortedN if rank == sortedN[0][0]]
    if len(sortedN) != 1:
        sortedN.sort(key=euclideanDistance, reverse=True)
        choices = [(sortedN[0], node) for node in sortedN[1:]]
        DFSearch.branches += choices
    return sortedN[0]


def euclideanDistance(node):
    """returns Euclidean distance squared from center of board
    sqrt has been omited as unessary computation"""
    p1, p2 = node
    center = (knightsTour.size - 1.0) / 2
    return ((p1 - center)**2 + (p2 - center)**2) 


def closedTour(start, size):
    """Finds the first solution in possible start positions
    where a closed tour exists. Since a closed tour is a loop
    it then takes this tour and shifts the start positon to a user
    set start position."""
    if size % 2: return Fail # no closed tour can be found in odd number squares
    i = range(size)
    posStarts = shiftStart(start, [(x, y) for x in i for y in i])
    for pstart in posStarts:
        Tour = knightsTour(pstart, size)
        end = Tour[-1]
        if subtract(pstart, end) in deltas:
            closedTour = Tour
            break # we have found a closed tour
    return (shiftStart(start, closedTour) 
            if start is not closedTour[0] else
            closedTour)


def shiftStart(start, listItem):
    "Returns a closed tour shifted to meet the rquested start position"
    index = listItem.index(start)
    return (listItem[index:] + listItem[:index])

def subtract(tuple1, tuple2):
    "Subtracts tuples and returns a tuple"
    t1a, t1b = tuple1
    t2a, t2b = tuple2
    return (t1a - t2a, t1b - t2b)


if __name__ == '__main__':
    import sys
    size = int(sys.argv[1]) if len(sys.argv) == 2 else 8
    start = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) == 4 else (0, 0)
    tour = knightsTour(start, size)
    print(tour)



