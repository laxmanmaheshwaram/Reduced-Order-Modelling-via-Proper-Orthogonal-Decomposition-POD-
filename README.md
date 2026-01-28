# Reduced Order Modelling via Proper Orthogonal Decomposition (POD)

This project demonstrates the construction of a Reduced Order Model (ROM)
for a structural dynamical system using Proper Orthogonal Decomposition (POD).
The objective is to reduce computational complexity while retaining the
dominant dynamics of the system.

The project serves as an introductory study towards data-informed and
adaptive ROMs for structural and energy systems.

---

## 1. Problem Description

We consider a linear mass–spring–damper chain governed by:

M x¨ + C x˙ + K x = f(t)

The full-order system is simulated, and state snapshots are collected.
POD is then applied to extract dominant modes, and the governing equations
are projected onto a reduced subspace.

---

## 2. Methodology

1. Full-order model simulation
2. Snapshot collection
3. Proper Orthogonal Decomposition (SVD)
4. Galerkin projection
5. Accuracy vs efficiency analysis

---

## 3. Results

- Energy captured by POD modes
- Comparison of FOM and ROM responses
- Error reduction as a function of retained modes

---

## 4. Conclusions

The POD-based ROM captures the dominant structural dynamics while reducing
the system dimension by an order of magnitude. This highlights the trade-off
between computational efficiency and model accuracy.

---

## References
- Holmes et al., *Turbulence, Coherent Structures, Dynamical Systems*
- Benner et al., *Model Reduction for Dynamical Systems*
