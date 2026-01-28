import numpy as np
from scipy.integrate import solve_ivp

def project_system(M, C, K, Phi):
    Mr = Phi.T @ M @ Phi
    Cr = Phi.T @ C @ Phi
    Kr = Phi.T @ K @ Phi
    return Mr, Cr, Kr

def simulate_rom(Mr, Cr, Kr, Phi, t_span, t_eval):
    r = Mr.shape[0]

    def dynamics(t, z):
        q = z[:r]
        qd = z[r:]
        qdd = np.linalg.solve(Mr, -Cr @ qd - Kr @ q)
        return np.hstack([qd, qdd])

    z0 = np.zeros(2*r)
    sol = solve_ivp(dynamics, t_span, z0, t_eval=t_eval)
    x_rec = Phi @ sol.y[:r, :]
    return x_rec
