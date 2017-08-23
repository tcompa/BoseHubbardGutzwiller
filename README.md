# BoseHubbardGutzwiller
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.846905.svg)](https://doi.org/10.5281/zenodo.846905)
[![Build Status](https://travis-ci.org/tcompa/BoseHubbardGutzwiller.svg?branch=master)](https://travis-ci.org/tcompa/BoseHubbardGutzwiller)

## What is this?
This is a simple python/cython code implementing the homogeneous Gutzwiller
variational wave function for the [Bose-Hubbard
model](https://en.wikipedia.org/wiki/Bose%E2%80%93Hubbard_model).  The search
for the optimal wave-function parameters is performed through [Simulated
Annealing](https://en.wikipedia.org/wiki/Simulated_annealing), a Monte Carlo
method for stochastic optimization.

## How to use it?
This code requires the [numpy](http://www.numpy.org/) and
[cython](http://cython.org/) libraries, and it is tested on python 2.7, 3.4,
3.5 and 3.6.

Before being imported in a python script, the module
`lib_gutzwiller_simulated_annealing.pyx` has to be compiled through the command

    $ python setup_cython.py build_ext --inplace

After this step, it can be imported in ordinary python scripts.
Have a look at the two example files:
+ In `example_1.py`, a single simulated-annealing run is performed, and the energy and density are computed (using the optimized Gutzwiller coefficients).
+ In `example_2.py`, a scan of different J values is performed, showing the transition from a Mott insulator (integer density) to a superfluid.

## Notes
1. The user should play around with values of the simulated-annealing
parameters. For instance a large value of the cooling rate might increase the
chance of hitting local minima. An additional check consists in comparing the
outcome of several independent runs (each one starting with a different initial
condition for the Gutzwiller coefficients).
2. If necessary, the code can easily be optimized further.  An example of a
possible change is to use the gsl random-number generator (see <a
href="http://pyinsci.blogspot.it/2010/12/efficcient-mcmc-in-python.html">here</a>),
which is not implemented in this version to avoid an additional dependency.

## License

MIT License

Copyright (c) 2017 Tommaso Comparin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
