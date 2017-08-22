from lib_gutzwiller_simulated_annealing import Gutzwiller
from lib_gutzwiller_simulated_annealing import SA_for_gutzwiller

# Physical parameters
z = 6        # number of neighbors
nmax = 5     # cutoff on the occupation number per site
U = 1.0      # on-site interaction coefficient
J = 0.03     # hopping coefficient
mu = 0.5     # chemical potential
V = 0.015    # nearest-neighbor interaction coefficient
P = 0.003    # induced-tunneling coefficient

# Initialize Gutzwiller-class instance
G = Gutzwiller(nmax=nmax, U=U, zJ=z*J, mu=mu, zV=z*V, zP=z*P)

# Simulated-annealing parameters
beta_min = 0.1
beta_max = 1e4
cooling_rate = 0.05
n_steps_per_T = 1000
quench_to_T_equal_to_0 = True
n_steps_at_T_equal_to_0 = 10000

# Perform simulated-annealing optimization
G = SA_for_gutzwiller(G, beta_min=beta_min, beta_max=beta_max,
                      cooling_rate=cooling_rate, n_steps_per_T=n_steps_per_T,
                      quench_to_T_equal_to_0=quench_to_T_equal_to_0,
                      n_steps_at_T_equal_to_0=n_steps_at_T_equal_to_0)
print 'Simulated-annealing optimization completed'
print 'Average energy: %.8f' % G.energy
print 'Average density: %.8f' % G.compute_density()
