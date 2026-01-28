import numpy as np
from scipy.linalg import svd

def compute_pod(X):
    X_mean = X.mean(axis=1, keepdims=True)
    Xc = X - X_mean
    U, S, Vt = svd(Xc, full_matrices=False)
    energy = np.cumsum(S**2) / np.sum(S**2)
    return U, S, energy
