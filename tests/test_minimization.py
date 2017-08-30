from __future__ import print_function
import sys
sys.path.append('..')

from lib_gutzwiller_simulated_annealing import Gutzwiller
from lib_gutzwiller_simulated_annealing import SA_for_gutzwiller


def test_in_the_superfluid_phase():
    z = 6
    nmax = 4
    U = 1.0
    J = 0.03
    mu = 0.1
    V = 0.015
    P = 0.003

    beta_min = 0.01
    beta_max = 1e5
    cooling_rate = 0.05
    n_steps_per_T = 1000
    quench_to_T_equal_to_0 = True
    n_steps_at_T_equal_to_0 = 1e5

    G = Gutzwiller(nmax=nmax, U=U, zJ=z*J, mu=mu, zV=z*V, zP=z*P)
    G = SA_for_gutzwiller(G, beta_min=beta_min, beta_max=beta_max,
                          cooling_rate=cooling_rate,
                          n_steps_per_T=n_steps_per_T,
                          quench_to_T_equal_to_0=quench_to_T_equal_to_0,
                          n_steps_at_T_equal_to_0=n_steps_at_T_equal_to_0)
    print()
    print('[begin stdout]')
    print('>> G.energy:', G.energy)
    print('>> G.compute_density():', G.compute_density())
    print('>> G.compute_abs_of_average_b():', G.compute_abs_of_average_b())
    print('[end stdout]')
    print()
    assert abs(G.energy + 0.1632796) < 1e-3
    assert abs(G.compute_density() - 0.87358) < 1e-3
    assert abs(G.compute_abs_of_average_b() - 0.61206) < 1e-3


def test_in_the_mott_phase():
    z = 6
    nmax = 3
    U = 1.0
    J = 0.01
    mu = 0.1
    V = 0.005
    P = 0.003

    beta_min = 0.01
    beta_max = 1e5
    cooling_rate = 0.05
    n_steps_per_T = 1000
    quench_to_T_equal_to_0 = True
    n_steps_at_T_equal_to_0 = 1e5

    G = Gutzwiller(nmax=nmax, U=U, zJ=z*J, mu=mu, zV=z*V, zP=z*P)
    G = SA_for_gutzwiller(G, beta_min=beta_min, beta_max=beta_max,
                          cooling_rate=cooling_rate,
                          n_steps_per_T=n_steps_per_T,
                          quench_to_T_equal_to_0=quench_to_T_equal_to_0,
                          n_steps_at_T_equal_to_0=n_steps_at_T_equal_to_0)
    print()
    print('[begin stdout]')
    print('>> G.energy:', G.energy)
    print('>> G.compute_density():', G.compute_density())
    print('>> G.compute_abs_of_average_b():', G.compute_abs_of_average_b())
    print('[end stdout]')
    print()
    
    assert abs(G.energy + 0.1149999) < 1e-3
    assert abs(G.compute_density() - 1.0) < 1e-3
    assert abs(G.compute_abs_of_average_b() - 0.0) < 1e-3


if __name__ == '__main__':
    test_in_the_superfluid_phase()
    test_in_the_mott_phase()
