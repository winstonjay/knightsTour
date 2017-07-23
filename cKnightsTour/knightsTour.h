//
//  knightsTour.h
//  knightsTour
//
//  Created by Karl Sims on 12/07/2017.
//  Copyright © 2017 Karl Sims. All rights reserved.
//
#ifndef knights_tour_h
#define knights_tour_h

typedef struct { signed char x; signed char y; } Vector;

const signed char DeltaN = 8; /* Max amount of succesor moves 
                                 of a single square from any postion
                                 on any size board. */
const Vector Deltas[DeltaN] = {
    {-2, 1}, {-2,-1}, {-1,-2}, { 1,-2}, 
    { 2,-1}, { 2, 1}, { 1, 2}, {-1, 2}
}; /* Possible moves a knight can make in vector space.*/

typedef struct { Vector nodes[DeltaN]; short length; } NodeList;

// const int BoardN = 8;
// const int BoardNxN = BoardN * BoardN;

typedef struct {
    Vector *path;
    int BoardN;
    int pathLength;
    bool success;
} Path;
/* Functions */

Path KnightsTour(Vector start, int boardN, Path tour); /* The daddy function */
Vector SelectedNode(NodeList nodelist, const Path *tour);
NodeList NodeSuccessors(Vector node, const Path *Path);
bool NodeInPath(Vector node, const Path *Path);
int EuclideanDistance(Vector node, int BoardN);


Path KnightsTour(Vector start, int BoardN, Path tour)
{
    /* Takes start co-ordinates and trys to find a valid
     tour and return it else fails*/
    int BoardNxN = BoardN * BoardN; // Set number of square in the board.
    Vector node = start;
    while (!tour.success)
    {
        tour.path[tour.pathLength] = node;
        tour.pathLength++;
        if (tour.pathLength >= BoardNxN)
        {
            tour.success = true; /* found a tour; set exit condition */
            break;
        }
        NodeList successors = NodeSuccessors(node, &tour);
        if (successors.length > 0)
        {
            node = SelectedNode(successors, &tour);
        }
        else
        {
            break; /* failed to find a tour; no valid successors */
        }
    }
    return tour;
}

Vector SelectedNode(NodeList nodelist, const Path *tour)
{
    /* Following Warnsdoffs rule this function searches for the 
     node that has the least number of successor nodes then incase of a
     draw tries to tiebreak on distance from the center of the board
     if this tiebreaks also the first added is selected. 
     */
    short bestNode = DeltaN; // max amount of possible succesor nodes.
    Vector selectedNode = {-1, -1}; // init incase of fail.
    int currentFurthest = 0;
    for (int n = 0; n < nodelist.length; n++)
    {
        short len = NodeSuccessors(nodelist.nodes[n], tour).length;
        if (len <= bestNode)
        {
            if (len == bestNode){
                int eucDist = EuclideanDistance(nodelist.nodes[n], tour->BoardN);
                if (eucDist > currentFurthest)
                {
                    bestNode = len;
                    currentFurthest = eucDist;
                    selectedNode = nodelist.nodes[n];
                }
            }
            else
            {
                bestNode = len;
                selectedNode = nodelist.nodes[n];
            }
        }
    }
    return selectedNode;
}

NodeList NodeSuccessors(Vector node, const Path *Path)
{
    /* Returns availible move nodes from the current possition. */
    NodeList successors;
    unsigned short count = 0;
    for (int i = 0; i < DeltaN; i++)
    {
        Vector N = {node.x + Deltas[i].x, node.y + Deltas[i].y};
        if ((N.x <  Path->BoardN) && (N.y <  Path->BoardN) &&
            (N.x >= 0) && (N.y >= 0) && !NodeInPath(N, Path))
        {
            successors.nodes[count] = N;
            count++;
        }
    }
    successors.length = count;
    return successors;
}

bool NodeInPath(Vector node, const Path *Path)
{
    /* Searches for a node a given Path and returns true if found else false */
    for (int i = 0; i < Path->pathLength; i++)
    {
        if ((Path->path[i].x == node.x) && (Path->path[i].y == node.y))
        {
            return true;
        }
    }
    return false;
}

int EuclideanDistance(Vector node, int BoardN)
{
    /* returns approx eucledian distance^2 from the center of the board
     basically the hypotenuse of a triangle */
    int center = BoardN - 1;
    int nX = node.x * 2 - center;
    int nY = node.y * 2 - center;
    return (nX * nX) + (nY * nY);
}

#endif