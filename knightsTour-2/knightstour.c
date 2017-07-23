#include <Python.h>
#include <stdbool.h> // required here and in "knightstour.h"
#include "knightstour.h"
/*
    Module for interfacing python with C implementation of a Knights tour 
    algorthm.

    Python Module Name:         cKnightsTour
    Python Accessible calls:    KnightsTour(x, y)

    Example python usage:

        import cKnightsTour
        tour = cKnightsTour.KnightsTour(4, 4)
        print(tour)
*/

static PyObject * Py_KnightsTour(const Path *C_Tour);
static PyObject * CtoPy_KnightsTour(PyObject *self, PyObject *args);

/*
    Below Required setup for intergrating with python.

    initcKnightsTour(void) is called by the module name in python 
    on import (i think...). 
*/
static char CtoPy_KnightsTour_docs[] =
    "KnightsTour(int x, int y): Returns a valid tour eg... ([(0,0), (2,1), ...]) or an empty list";
// python docstring for reading in python

static PyMethodDef CtoPy_KnightsTour_funcs[] = {
    {"KnightsTour", (PyCFunction)CtoPy_KnightsTour, METH_NOARGS, CtoPy_KnightsTour_docs},
    {"KnightsTour", CtoPy_KnightsTour, METH_VARARGS, CtoPy_KnightsTour_docs},
    { NULL, NULL, 0, NULL }
};
// list the functions accessible, CtoPy_KnightsTour with and without args

void initcKnightsTour(void)
{
    Py_InitModule3("cKnightsTour", CtoPy_KnightsTour_funcs,
                   "Module for computing knights tours faster than in python");
}


/*
    Functions to return a tour from the C function.
*/
static PyObject * 
CtoPy_KnightsTour(PyObject* self, PyObject *args)
{   
    /* CtoPy_KnightsTour(PyObject* self, PyObject *args): return a valid tour 
    or empty list to python; Parses input from python function runs the C 
    KnightsTour from "knightstour.h" with the given args. If the pathLength 
    of the tour is not a goal state, generate an empty python list. Else return 
    value from Py_KnightsTour */
    int x, y;
    PyObject *Fail = Py_BuildValue("[]");
    if (!PyArg_ParseTuple(args, "ii", &x, &y)) 
    {
      return NULL;
    }
    Vector start_positon = { x, y };
    Path C_Tour = KnightsTour(start_positon);
    if (C_Tour.success) 
    {
        return Py_KnightsTour(&C_Tour);
    }
    return Fail;
}

static PyObject * 
Py_KnightsTour(const Path * C_Tour)
{
    /* Py_KnightsTour(const Path * C_Tour): Return a valid tour;
    Generate a python list of tuples from the (path.x, path.y) 
    values returned from the Path (C_tour) C struct data type.
    The `Path` C struct is made up of a struct Array of Vectors (x, y)
    a Int pathLength and a boolean valid tour. */
    PyObject *PyTour = PyList_New(C_Tour->pathLength);
    if (!PyTour) return NULL;
    for (int i = 0; i < C_Tour->pathLength; i++)
    {
        PyObject *move_tuple = Py_BuildValue("ii", 
                                    C_Tour->path[i].x, 
                                    C_Tour->path[i].y);
        if (!move_tuple) 
        {
            Py_DECREF(PyTour); 
            return NULL;
        }
        PyList_SET_ITEM(PyTour, i, move_tuple);
    }
    return PyTour;
}




