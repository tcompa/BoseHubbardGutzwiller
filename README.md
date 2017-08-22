# BoseHubbardGutzwiller
Gutzwiller ansatz for Bose-Hubbard model, with simulated-annealing optimization

## What is this

## How to use it
This code is tested on python 2.7, and it requires the
[numpy](http://www.numpy.org/) and [cython](http://cython.org/) libraries.

Before using it, the cython library needs to be compiled, through the command:

    $ python setup_cython.py build_ext --inplace

After this step, have a look of the two example files:
+ In `example_1.py`, a single simulated-annealing run is performed, and the energy and density are computed (using the optimized Gutzwiller coefficients).
+ In `example_2.py`, a scan of different J values is performed, showing the transition from a Mott insulator (integer density) to a superfluid.

## Notes
1. The user 
2. 
If necessary, the code can be optimized further.
A simple change would be to use the gsl random-number generator (see <a href="http://pyinsci.blogspot.it/2010/12/efficcient-mcmc-in-python.html">here</a>), which is not implemented in this version to avoid an additional dependency.
