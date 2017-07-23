from distutils.core import setup, Extension
setup(name='cKnightsTour', version='1.0',  \
      ext_modules=[Extension('cKnightsTour', ['knightstour.c'])])


