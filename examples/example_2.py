import sys
sys.path.append('..')

import numpy

from lib_gutzwiller_simulated_annealing import Gutzwiller
from lib_gutzwiller_simulated_annealing import SA_for_gutzwiller

# Physical parameters
z = 6        # number of neighbors
nmax = 5     # cutoff on the occupation number per site
U = 1.0      # on-site interaction coefficient
mu = 0.5     # chemical potential
V = 0.015    # nearest-neighbor interaction coefficient
P = 0.003    # induced-tunneling coefficient


# Simulated-annealing parameters
beta_min = 0.1
beta_max = 1e4
cooling_rate = 0.05
n_steps_per_T = 1000
quench_to_T_equal_to_0 = True
n_steps_at_T_equal_to_0 = 10000

for J in numpy.arange(0.005, 0.041, 0.005):
    # Initialize Gutzwiller-class instance
    G = Gutzwiller(nmax=nmax, U=U, zJ=z*J, mu=mu, zV=z*V, zP=z*P)
    # Perform simulated-annealing optimization
    G = SA_for_gutzwiller(G, beta_min=beta_min, beta_max=beta_max,
                          cooling_rate=cooling_rate, n_steps_per_T=n_steps_per_T,
                          quench_to_T_equal_to_0=quench_to_T_equal_to_0,
                          n_steps_at_T_equal_to_0=n_steps_at_T_equal_to_0)
    print('J=%f energy=%.8f density=%.8f' % (J, G.energy, G.compute_density()))
