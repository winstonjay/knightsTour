#include <Python.h>

static PyObject* knightsTour(PyObject* self)
{
    return Py_BuildValue("s", "One day this will return a tour");
}

static char knightsTour_docs[] =
    "knightsTour( ): Any message you want to put here!!\n";

static PyMethodDef knightsTour_funcs[] = {
    {"knightsTour", (PyCFunction)knightsTour, 
     METH_NOARGS, knightsTour_docs},
    {NULL}
};

void initcTour(void)
{
    Py_InitModule3("cTour", knightsTour_funcs,
                   "Extension module example!");
}