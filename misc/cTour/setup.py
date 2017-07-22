from distutils.core import setup, Extension
setup(name='cTour', version='1.0',  \
      ext_modules=[Extension('cTour', ['tour.c'])])


