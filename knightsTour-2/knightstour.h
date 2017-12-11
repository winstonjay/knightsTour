#ifndef knights_tour_h
#define knights_tour_h
/*

Info about the Knights Tour problem as described by wikipedia:

A knight's tour is a sequence of moves of a knight on a chessboard such that
the knight visits every square only once. If the knight ends on a square that
is one knight's move from the beginning square (so that it could tour the board
again immediately, following the same path), the tour is closed, otherwise it
is open.

*/



typedef struct { signed char x; signed char y; } Vector;

const signed char DeltaN = 8; /* Max amount of succesor moves
                                 of a single square from any postion
                                 on any size board. */
const Vector Deltas[DeltaN] = {
    {-2, 1}, {-2,-1}, {-1,-2}, { 1,-2},
    { 2,-1}, { 2, 1}, { 1, 2}, {-1, 2}
}; /* Possible moves a knight can make in vector space.*/

typedef struct { Vector nodes[DeltaN]; short length; } NodeList;

const int BoardN = 8;
const int BoardNxN = BoardN * BoardN;

typedef struct {
    Vector path[BoardNxN];
    int pathLength;
    bool success;
} Path;


/* Functions */
Path KnightsTour(Vector start);
Vector SelectedNode(NodeList nodelist, const Path *tour);
NodeList NodeSuccessors(Vector node, const Path *Path);
bool NodeInPath(Vector node, const Path *Path);
int EuclideanDistance(Vector node);



/**
 * KnightsTour:
 * Takes start co-ordinates and trys to find a valid
 * tour and return it else fails.
*/
Path KnightsTour(Vector start) {
    Vector node = start;
    Path tour;
    tour.pathLength = 0;
    tour.success = false;
    while (!tour.success) {
        tour.path[tour.pathLength] = node;
        tour.pathLength++;
        if (tour.pathLength >= BoardNxN) {
            tour.success = true; /* found a tour; set exit condition */
            break;
        }
        NodeList successors = NodeSuccessors(node, &tour);
        if (successors.length > 0) {
            node = SelectedNode(successors, &tour);
        } else {
            break; /* failed to find a tour; no valid successors */
        }
    }
    return tour;
}

/**
 * Following Warnsdoffs rule this function searches for the
 * node that has the least number of successor nodes then incase of a
 * draw tries to tiebreak on distance from the center of the board
 * if this tiebreaks also the first added is selected.
*/
Vector SelectedNode(NodeList nodelist, const Path *tour) {

    short bestNode = DeltaN;        // max amount of possible succesor nodes.
    Vector selectedNode = {-1, -1}; // init incase of fail.
    int currentFurthest = 0;

    for (int n = 0; n < nodelist.length; n++) {

        short len = NodeSuccessors(nodelist.nodes[n], tour).length;

        if (len < bestNode) {
            bestNode = len;
            selectedNode = nodelist.nodes[n];

        } else if (len == bestNode) {
            int eucDist = EuclideanDistance(nodelist.nodes[n]);
            if (eucDist > currentFurthest) {
                bestNode = len;
                currentFurthest = eucDist;
                selectedNode = nodelist.nodes[n];
            }
        }
    }
    return selectedNode;
}

/**
 * NodeSuccessors:
 * Returns availible move nodes from the current possition.
*/
NodeList NodeSuccessors(Vector node, const Path *Path) {
    NodeList successors;
    unsigned short count = 0;
    for (int i = 0; i < DeltaN; i++) {
        Vector N = {node.x + Deltas[i].x, node.y + Deltas[i].y};
        if ((N.x <  BoardN) && (N.y <  BoardN) &&
            (N.x >= 0) && (N.y >= 0) && !NodeInPath(N, Path))
        {
            successors.nodes[count] = N;
            count++;
        }
    }
    successors.length = count;
    return successors;
}


/**
 * NodeInPath:
 * Searches for a node a given Path and returns true if found else false.
*/
bool NodeInPath(Vector node, const Path *Path) {
    for (int i = 0; i < Path->pathLength; i++) {
        if ((Path->path[i].x == node.x) && (Path->path[i].y == node.y)) {
            return true;
        }
    }
    return false;
}


/**
 * EuclideanDistance:
 * Returns approx eucledian distance^2 from the center of the board
 * as basically the hypotenuse of a triangle.
*/
int EuclideanDistance(Vector node) {
    int center = BoardN - 1;
    int nX = node.x * 2 - center;
    int nY = node.y * 2 - center;
    return (nX * nX) + (nY * nY);
}

#endif