'''
Program: setup_cython.py
Created: Tue Aug 22 22:06:12 CEST 2017
Author: Tommaso Comparin
description:   Compiles  cython module
notes:         to be executed through
               $ python setup_cython.py build_ext --inplace
'''

import glob
from distutils.extension import Extension
from distutils.core import setup
from Cython.Distutils import build_ext

# Loop over all pyx files
for lib in glob.glob('*.pyx'):
    basename = lib[:-4]
    ext_modules = [Extension(basename, [basename + '.pyx'])]
    setup(cmdclass={'build_ext': build_ext}, ext_modules=ext_modules)
