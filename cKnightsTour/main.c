//
//  main.c
//  knightsTour
//
//  Created by Karl Sims on 12/07/2017.
//  Copyright © 2017 Karl Sims. All rights reserved.
//
#include <stdio.h>
#include <stdbool.h>
#include <time.h>

#include "knightsTour.h"


int main()
{
    Vector start = {0,0};
    clock_t t0 = clock(), t1;
    Path tour = KnightsTour(start);
    t1 = clock() - t0;
    if (tour.success)
    {
        printf("Success!\n");
        for (int i = 0; i < tour.pathLength; i++)
        {
            printf("[%d, %d], ", tour.path[i].x,  tour.path[i].y);
        }
    }
    else
    {
        printf("Failed!");
    }
    printf("\n%d \n", tour.pathLength);
    float msec = t1 * 1000 / CLOCKS_PER_SEC;
    printf("Completed in %f seconds.\n", msec/1000);
}

