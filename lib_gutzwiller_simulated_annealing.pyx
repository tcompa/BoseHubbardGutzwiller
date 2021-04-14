#cython: language_level=3

'''
Program: lib_gutzwiller_simulated_annealing.pyx
Created: Tue Aug 22 22:25:31 CEST 2017
Author: Tommaso Comparin

The notation is the same as in Eq. (11) of
    R. H. Chaviguri, T. Comparin, M. Di Liberto, M. A. Caracanhas,
    Density-dependent hopping for ultracold atoms immersed in a Bose-Einstein-condensate vortex lattice
    arXiv:1711.10234 [cond-mat.quant-gas]
    https://arxiv.org/abs/1711.10234
'''

import sys
import math
import random

import numpy
import cython


@cython.wraparound(False)
@cython.boundscheck(False)
@cython.initializedcheck(False)
cdef class Gutzwiller:
    '''
    Encodes the Gutzwiller-ansatz parameters, their evolution through
    the Metropolis Monte Carlo algorithm, and the measurement of
    relevant observables (energy, density, condensate density).

    See Eq. (11) in https://arxiv.org/abs/1711.10234.
    '''

    cdef public double beta
    cdef public double energy
    cdef int nmax
    cdef double zJ, U, mu, zV, zP
    cdef double df
    cdef double [:] f, f_new

    def __init__(self, int nmax=5, double mu=0.0, double zJ=0.0, double U=0.0,
                 double zV=0.0, double zP=0.0):
        self.nmax = nmax
        self.zJ = zJ
        self.mu = mu
        self.U = U
        self.zV = zV
        self.zP = zP
        self.f = numpy.zeros(self.nmax + 1)
        self.f_new = numpy.zeros(self.nmax + 1)
        # Initialize relevant variables
        for j in xrange(self.nmax + 1):
            self.f[j] = random.random()
        self.f = self.normalize_f(self.f)
        self.df = 0.01
        self.energy = self.compute_energy(self.f)
        # Check the sign of some parameters
        assert self.zJ >= 0.0
        assert self.U >= 0.0
        assert self.zV >= 0.0

    cdef double [:] normalize_f(self, double [:] _f):
        '''
        Returns a normalized copy of the Gutzwiller coefficients _f.
        Note that _f can be any array of coefficients, not only self.f.
        '''
        cdef double norm_sq = 0.0
        cdef int n
        for n in xrange(0, self.nmax + 1):
            norm_sq += _f[n] ** 2
        cdef double inv_norm = 1.0 / math.sqrt(norm_sq)
        for n in xrange(0, self.nmax + 1):
            _f[n] = _f[n] * inv_norm
        return _f[:]

    cdef double compute_energy(self, double [:] _f):
        '''
        Returns the expectation value of the Hamiltonian in the
        Gutzwiller state with coefficients _f.
        Note that _f can be any array of coefficients, not only self.f.
        '''
        cdef double xJ = 0.0, xU = 0.0, xmu = 0.0, xV = 0.0, xP = 0.0
        cdef int n, m
        for n in xrange(0, self.nmax + 1):
            # Diagonal terms
            xU += _f[n] ** 2 * n * (n - 1.0)
            xmu += _f[n] ** 2 * n
            xV += _f[n] ** 2 * n
            # Off-diagonal terms
            if n == self.nmax:
                continue
            xJ += _f[n] * _f[n + 1] * math.sqrt(n + 1.0)
            for m in xrange(0, self.nmax):
                xP += (_f[n + 1] * _f[m] * _f[n] * _f[m + 1] *
                       math.sqrt((n + 1.0) * (m + 1.0)) * (n + m + 1.0))
        cdef double E = 0.0
        E -= self.zJ * xJ ** 2
        E += 0.5 * self.U * xU
        E -= self.mu * xmu
        E -= 0.5 * self.zV * xV ** 2
        E -= self.zP * xP
        return E

    cpdef double compute_density(self):
        '''
        Returns the expectation value of the density in the Gutzwiller
        state with coefficients self.f.
        '''
        cdef double res = 0.0
        cdef int n
        for n in xrange(self.nmax + 1):
            res += self.f[n] ** 2 * n
        return res

    cpdef double compute_abs_of_average_b(self):
        '''
        Returns the absolute value of the annihilation-operator
        expectation value in the Gutzwiller state with coefficients
        self.f.
        '''
        cdef double res = 0.0
        cdef int n
        for n in xrange(self.nmax):
            res += self.f[n] * self.f[n + 1] * math.sqrt(n + 1.0)
        return abs(res)

    cdef void update_MC_parameters(self, double acc_ratio):
        '''
        Updates the parameters of the probability distribution used at
        each Monte Carlo step.
        '''
        if acc_ratio < 0.2 and self.df > 0.005:
            self.df *= 0.90909090909090909090
        elif acc_ratio > 0.8 and self.df < 1.1:
            self.df *= 1.1

    cdef int MC_move(self):
        '''
        Performs one step of the Metropolis Monte Carlo algorithm.
        '''
        cdef int n
        for n in xrange(self.nmax + 1):
            self.f_new[n] = self.f[n] + random.uniform(-self.df, self.df)
        self.f_new = self.normalize_f(self.f_new[:])
        cdef double E_new = self.compute_energy(self.f_new[:])
        cdef double dE = E_new - self.energy
        if dE < 0.0 or random.random() < math.exp(- self.beta * dE):
            for n in xrange(self.nmax + 1):
                self.f[n] = self.f_new[n]
            self.energy = E_new
            return 1
        else:
            return 0


@cython.wraparound(False)
@cython.boundscheck(False)
@cython.initializedcheck(False)
def SA_for_gutzwiller(Gutzwiller P, double beta_min=1e-2, double beta_max=1e2,
                      double cooling_rate=0.01, int n_steps_per_T=100,
                      int quench_to_T_equal_to_0=1,
                      int n_steps_at_T_equal_to_0=1000):
    '''
    Variables

    P: Gutzwiller-class instance
        Instance of the Gutzwiller class
    beta_min : float, optional
        Minimum inverse temperature (default: 1e-2)
    beta_max: float, optional
        Maximum inverse temperature (default: 1e2)
    cooling_rate : float, optional
        Cooling rate (default: 0.01)
    n_steps_per_T : int, optional
        Number of MC moves attempted at each temperature (default: 100)
    quench_to_T_equal_to_0: bool, optional
        If True, perform a T=0 quench at the end of the annealing
    n_steps_at_T_equal_to_0: int, optional
        Number of MC moves after the T=0 quench
    '''
    cdef double acc_ratio = 0.0
    cdef int acc, step
    P.beta = beta_min
    while P.beta < beta_max:
        # Perform n_steps_per_T Monte Carlo steps
        acc = 0
        for step in range(n_steps_per_T):
            acc += P.MC_move()
        acc_ratio = acc / float(n_steps_per_T)
        # Update beta and MC parameters
        P.beta *= (1.0 + cooling_rate)
        P.update_MC_parameters(acc_ratio)
    # T=0 quench
    if quench_to_T_equal_to_0:
        P.beta = 1e24
        for step in range(n_steps_at_T_equal_to_0):
            P.MC_move()
    return P
