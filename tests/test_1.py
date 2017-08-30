import sys
sys.path.append('..')

from lib_gutzwiller_simulated_annealing import Gutzwiller
from lib_gutzwiller_simulated_annealing import SA_for_gutzwiller


def test_on_a_simple_run():
    # Physical parameters
    z = 6        # number of neighbors
    nmax = 4     # cutoff on the occupation number per site
    U = 1.0      # on-site interaction coefficient
    J = 0.03     # hopping coefficient
    mu = 0.1     # chemical potential
    V = 0.015    # nearest-neighbor interaction coefficient
    P = 0.003    # induced-tunneling coefficient

    # Simulated-annealing parameters
    beta_min = 0.01
    beta_max = 1e5
    cooling_rate = 0.05
    n_steps_per_T = 1000
    quench_to_T_equal_to_0 = True
    n_steps_at_T_equal_to_0 = 1e5

    G = Gutzwiller(nmax=nmax, U=U, zJ=z*J, mu=mu, zV=z*V, zP=z*P)
    G = SA_for_gutzwiller(G, beta_min=beta_min, beta_max=beta_max,
                          cooling_rate=cooling_rate, n_steps_per_T=n_steps_per_T,
                          quench_to_T_equal_to_0=quench_to_T_equal_to_0,
                          n_steps_at_T_equal_to_0=n_steps_at_T_equal_to_0)
    assert abs(G.energy + 0.16327963) < 1e-3
    assert abs(G.compute_density() - 0.87358150) < 1e-2


if __name__ == '__main__':
    test_on_a_simple_run()
