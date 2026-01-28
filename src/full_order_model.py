import numpy as np
from scipy.integrate import solve_ivp

def build_matrices(n, damping=0.01):
    M = np.eye(n)
    K = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    C = damping * K
    return M, C, K

def simulate_fom(M, C, K, t_span, t_eval):
    n = M.shape[0]

    def dynamics(t, z):
        x = z[:n]
        v = z[n:]
        a = np.linalg.solve(M, -C @ v - K @ x)
        return np.hstack([v, a])

    z0 = np.zeros(2*n)
    sol = solve_ivp(dynamics, t_span, z0, t_eval=t_eval)
    return sol.y[:n, :], sol.t
