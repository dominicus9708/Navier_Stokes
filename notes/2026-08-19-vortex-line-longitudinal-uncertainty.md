# Vortex-line longitudinal uncertainty from div omega = 0

Date: 2026-08-19

Status: **DERIVED EXACT DIVERGENCE-FREE COUPLING + LONGITUDINAL TIGHTNESS GATE / GLOBAL REGULARITY NOT PROVED**.

This note treats the coherent-direction / magnitude-interface survivor left by the palinstrophy covariance decomposition.

---

## 1. Exact magnitude-direction coupling

Where

\[
\omega=\rho\xi,
\qquad
\rho=|\omega|>0,
\qquad
|\xi|=1,
\]

the vorticity is divergence free:

\[
\nabla\cdot\omega=0.
\]

Therefore

\[
\boxed{
\xi\cdot\nabla\rho
=-\rho\,\nabla\cdot\xi.
}
\]

Hence longitudinal variation of vorticity magnitude along a vortex direction is not independent of direction-field variation.

Since

\[
|\nabla\cdot\xi|^2
\le3|\nabla\xi|^2,
\]

one has

\[
\boxed{
\int|\xi\cdot\nabla\rho|^2dx
\le
3\int\rho^2|\nabla\xi|^2dx
=3P_\xi.
}
\]

Thus a direction-coherent state makes the magnitude nearly constant along its own vortex lines unless another geometric escape is activated.

---

## 2. Longitudinal Heisenberg bound along a fixed axis

Fix a constant unit vector `n` and a center `X`. Let

\[
E_\rho=\int\rho^2dx
=\|\omega\|_2^2,
\]

and define the longitudinal second moment

\[
M_n(X)
=
\int
\left|(x-X)\cdot n\right|^2
\rho^2(x)dx.
\]

Define

\[
R_n^2(X)=M_n(X)/E_\rho.
\]

One-dimensional integration by parts gives

\[
E_\rho
\le
2M_n(X)^{1/2}
\|\partial_n\rho\|_2.
\]

Hence

\[
\boxed{
\|\partial_n\rho\|_2^2
\ge
\frac{E_\rho}{4R_n^2(X)}.
}
\]

A vorticity-magnitude distribution that is tight along `n` must therefore have a definite longitudinal magnitude derivative.

---

## 3. Split the longitudinal derivative relative to the vortex direction

Decompose

\[
n
=(n\cdot\xi)\xi
+P_{\xi^\perp}n.
\]

Then

\[
\partial_n\rho
=(n\cdot\xi)(\xi\cdot\nabla\rho)
+(P_{\xi^\perp}n)\cdot\nabla\rho.
\]

Using the divergence-free identity,

\[
\partial_n\rho
=-(n\cdot\xi)\rho\,\nabla\cdot\xi
+(P_{\xi^\perp}n)\cdot\nabla\rho.
\]

Define the cross-axis magnitude-gradient cost

\[
\boxed{
Q_n
=
\int
|P_{\xi^\perp}n|^2
|\nabla\rho|^2dx.
}
\]

Then

\[
\|\partial_n\rho\|_2^2
\le
6P_\xi+2Q_n.
\]

Combining with the longitudinal uncertainty bound gives

\[
\boxed{
6P_\xi+2Q_n
\ge
\frac{E_\rho}{4R_n^2(X)}.
}
\]

Equivalently,

\[
\boxed{
3P_\xi+Q_n
\ge
\frac{E_\rho}{8R_n^2(X)}.
}
\]

This is the principal tightness gate of this note.

---

## 4. Interpretation

A vorticity core that is simultaneously

1. nontrivial in enstrophy `E_rho`;
2. spatially tight along an axis `n`, so `R_n=O(1)` in normalized variables;
3. projectively aligned with `n`, so `P_{xi^perp} n` is small on the magnitude-gradient region;
4. small in magnitude-weighted direction variation `P_xi`;

cannot persist.

Indeed the inequality forces at least one of

\[
\boxed{
P_\xi\ \text{non-small}
}
\]

or

\[
\boxed{
Q_n\ \text{non-small}
}
\]

or

\[
\boxed{
R_n\ \text{large}.
}
\]

These are respectively:

- direction-variation / coherence cost (`H`);
- cross-axis magnitude-interface complexity (`H` / interior angular channel);
- longitudinal spatial non-tightness / long vortex-line geometry (`T`).

---

## 5. Straight constant-direction rigidity

If `xi=n` is exactly constant, then

\[
Q_n=0,
\qquad
P_\xi=0.
\]

The tightness gate forces

\[
R_n=\infty
\]

for every nonzero finite-enstrophy configuration.

Equivalently, `div( rho n )=0` gives

\[
\partial_n\rho=0.
\]

A nonzero state with exactly constant direction therefore extends indefinitely along `n`; it cannot be a spatially tight finite-energy vortex core.

This is a kinematic finite-energy rigidity statement, not a regularity theorem.

---

## 6. Consequence for the reduced first-hitting route

The near-saturated `M` branch already tends toward strong vorticity alignment with the principal extensional strain axis. The present inequality shows that a bounded-radius coherent core cannot use this alignment to avoid derivative costs indefinitely.

A tight aligned survivor must pay through

\[
\boxed{
P_\xi
\quad\text{or}\quad
Q_n,
}

while suppressing both forces longitudinal extension and hence the `T` branch.

Thus the coherent-direction magnitude-interface survivor is further reduced to

\[
\boxed{
\text{direction variation}
\ \lor\ 
\text{cross-axis magnitude gradients}
\ \lor\ 
\text{longitudinal non-tightness}.
}
\]

The remaining hard case is a repeatedly regenerated, bounded-radius vortex core in which the direction field and magnitude-interface normals co-reorganize so that `P_xi` and `Q_n` stay critical but globally repeatable.

Status: **STRAIGHT/TIGHT COHERENT VORTEX CORE EXCLUDED KINEMATICALLY; FINAL CO-REORGANIZING DIRECTION/INTERFACE PACKING STEP OPEN**.
