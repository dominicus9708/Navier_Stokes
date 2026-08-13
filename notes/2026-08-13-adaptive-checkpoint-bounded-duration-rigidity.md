# Adaptive first-hitting bounded-duration rigidity

Date: 2026-08-13

Status: **COMPACT-BRANCH RIGIDITY LEMMA / ANCIENT-DURATION BRANCH REMAINS**.

The adaptive checkpoint construction uses amplitude ratios `q_j -> infinity`.  In terminal normalization the previous checkpoint therefore has vorticity amplitude tending uniformly to zero.

If the normalized duration between the two checkpoints stayed bounded and the normalized solutions were locally compact, the limiting vorticity would be zero at a finite past time and nonzero at the terminal time.  This is incompatible with the homogeneous vorticity evolution from zero data.

---

## 1. Adaptive first-hitting data

Let

\[
W_j=\|\omega(t_j)\|_\infty
\]

be an adaptive increasing first-hitting sequence with

\[
q_j=\frac{W_j}{W_{j-1}}\to\infty.
\]

Normalize at the terminal level `W_j`:

\[
r_j=W_j^{-1/2},
\]

\[
U_j(y,s)
=r_j u(x_j+r_jy,t_j+r_j^2s),
\]

\[
\Omega_j(y,s)
=r_j^2\omega(x_j+r_jy,t_j+r_j^2s).
\]

Then first hitting gives

\[
\|\Omega_j(s)\|_\infty\le1
\]

throughout the normalized past interval and

\[
|\Omega_j(0,0)|=1.
\]

Let

\[
\sigma_j=W_j(t_j-t_{j-1}).
\]

At the previous checkpoint,

\[
\boxed{
\|\Omega_j(-\sigma_j)\|_\infty
\le\frac1{q_j}
\to0.
}
\]

---

## 2. Bounded-duration contradiction under compactness

Assume a subsequence with

\[
\sigma_j\le S<\infty.
\]

After passing to a further subsequence,

\[
\sigma_j\to\sigma_*\in[0,S].
\]

Assume the bounded-affine/local-regularity branch supplies enough compactness that, after the standard moving/affine frame normalization,

\[
\Omega_j\to\Omega_\infty
\]

locally strongly enough on a fixed cylinder containing `[-S,0]` to pass the vorticity equation and the endpoint values.

Then

\[
\boxed{
\Omega_\infty(\cdot,-\sigma_*)=0.
}
\]

The limiting vorticity solves the homogeneous incompressible Navier--Stokes vorticity equation

\[
\partial_s\Omega
+(U\cdot\nabla)\Omega
=(\Omega\cdot\nabla)U
+\nu\Delta\Omega.
\]

Zero vorticity at one finite time is preserved forward: the equation contains no source independent of `Omega`.

Hence

\[
\Omega_\infty\equiv0
\qquad\text{for }s\ge-\sigma_*.
\]

But terminal normalization requires

\[
|\Omega_\infty(0,0)|=1.
\]

Contradiction.

Therefore

\[
\boxed{
\sigma_j\to\infty
}
\]

on every nontrivial adaptive first-hitting branch for which the required local compactness remains controlled.

---

## 3. Meaning of compactness failure

The conclusion is conditional on extracting the local limit in a class where the vorticity equation and zero-data uniqueness are valid.

If this compactness fails, the failure is not left untyped.  It returns to previously identified channels such as

- affine condition-number degeneration;
- V2/high-derivative concentration;
- pressure-Hessian/eigenframe concentration;
- non-affine Gaussian residual concentration;
- shell/local-energy loss of compactness.

Thus bounded normalized duration is not an independent residual route.

---

## 4. Relation to the adaptive one-step memory scale

For the checkpoint choice

\[
q_j=W_j^{1/3+2\varepsilon},
\]

the previous natural normalized time is `q_j`, while the present lemma only forces

\[
\sigma_j\to\infty.
\]

It does **not** yet prove

\[
\sigma_j\gtrsim q_j.
\]

Therefore an intermediate regime remains possible:

\[
1\ll\sigma_j\ll q_j.
\]

This is the next fast-relative-to-previous-scale branch to analyze.

---

## 5. DSD interpretation

A terminal dangerous state cannot be generated from an asymptotically zero previous resolved state inside a uniformly bounded amount of normalized evolution while all structural channels remain compact.

Hence the adaptive state graph has a temporal persistence requirement:

\[
\boxed{
q_j\to\infty
+\text{compact channels}
\Longrightarrow
\text{checkpoint separation in terminal time }\to\infty.
}
\]

Status: **BOUNDED-DURATION ADAPTIVE LANE PRUNED / INTERMEDIATE `1 << sigma_j << q_j` LANE REMAINS OPEN**.
