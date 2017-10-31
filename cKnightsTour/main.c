//
//  main.c
//  knightsTour
//
//  Created by Karl Sims on 12/07/2017.
//  Copyright © 2017 Karl Sims. All rights reserved.
//
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#include "knightsTour.h"


int main() {
    
    int BoardN = 6;
    int BoardNxN = BoardN * BoardN;
    Vector start = {0,0};

    Path tour = { /* struct: *path, BoardN, pathLength, success; */
        (Vector*) malloc(BoardNxN * sizeof(Vector)), BoardN, 0, false }; 

    if (tour.path == NULL) {
        printf("Error! memory not allocated.\n");
        return 0;
    }

    clock_t t0 = clock(), t1;
    tour = KnightsTour(start, BoardN, tour);
    t1 = clock() - t0;
    if (tour.success) {
        printf("Success!\n");
        for (int i = 0; i < tour.pathLength; i++) {
            printf("[%d, %d], ", tour.path[i].x,  tour.path[i].y);
        }
    } else {
        printf("Failed!");
    }
    printf("\n%d \n", tour.pathLength);
    float msec = t1 * 1000 / CLOCKS_PER_SEC;
    printf("Completed in %f seconds.\n", msec/1000);
    free(tour.path);
    tour.path = NULL;
}

