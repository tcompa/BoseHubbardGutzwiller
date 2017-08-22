# BoseHubbardGutzwiller
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.846905.svg)](https://doi.org/10.5281/zenodo.846905)

## What is this?
This is a simple python/cython code implementing the homogeneous Gutzwiller
variational wave function for the [Bose-Hubbard
model](https://en.wikipedia.org/wiki/Bose%E2%80%93Hubbard_model).  The search
for the optimal wave-function parameters is performed through [Simulated
Annealing](https://en.wikipedia.org/wiki/Simulated_annealing), a Monte Carlo
method for stochastic optimization.

## How to use it?
This code is tested on python 2.7, and it requires the
[numpy](http://www.numpy.org/) and [cython](http://cython.org/) libraries.
Before being imported in a python script, the module `lib_gutzwiller_simulated_annealing.pyx` has to be compiled through the command

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
