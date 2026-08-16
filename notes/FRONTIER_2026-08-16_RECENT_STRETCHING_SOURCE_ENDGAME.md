# Frontier: clean precursor erased, old source erased, coherent vorticity must be freshly generated in the recent one-third layer

Date: 2026-08-16

Overall status: **THE STOCHASTIC-ANCESTRY ENDGAME HAS BEEN REDUCED FURTHER. A CLEAN LOW-ENSTROPHY PRECURSOR CANNOT CONTRIBUTE ORDER-ONE VORTICITY BY LINEAR ADVECTION--DIFFUSION, AND STRETCHING OLDER THAN `W^(1/3+)` IS POINTWISE NEGLIGIBLE. EVERY LATE COHERENT CROSSING MUST FRESHLY GENERATE ITS ORDER-ONE VORTICITY IN THE RECENT `W^(1/3+)` NORMALIZED LAYER, WHICH ALREADY CARRIES `R^3` ENSTROPHY OCCUPANCY. GLOBAL REGULARITY NOT PROVED.**

---

# 1. Corrected starting point

The previous bulk-stochastic-deformation frontier identified a deformation-weighted palinstrophy

\[
\mathcal Q_D
=\int E\int|D\nabla\Omega|^2
\]

as the apparent final wall.

This continuation produced two changes.

First, a scaling error in an attempted deep affine product estimate was found and corrected. The exact affine heat theorem is scale critical under terminal normalization:

\[
J_{\rm term}M_{\Pi,\rm term}^2
\gtrsim
\nu/q,
\]

not `nu q`. Therefore no superlarge ordinary-palinstrophy contradiction comes from choosing an arbitrarily deep checkpoint.

Second, a direct PDE/adjoint-kernel route now bypasses much of the long stochastic ancestry for the purpose of **pointwise vorticity generation**.

---

# 2. Clean minimum-enstrophy checkpoint

Choose a deep first-hitting checkpoint

\[
q_\beta=W/R^\beta,
\qquad
0<\beta<4,
\]

and then select

\[
s_m\in[s_-,s_c]
\]

at the minimum of global terminal-normalized enstrophy.

Then

\[
\boxed{
E_m
\le E_-
\lesssim
R^\beta/W^{1/2}
\to0.
}
\]

Since `s_m` is source-active in the Dini sense and the first-hitting cap is `||Omega||_infty<=1`,

\[
\boxed{
P_m\lesssim_\nu E_m.
}
\]

For every unit direction `e`,

\[
\boxed{
M_{\Pi,e}^2
\lesssim_\nu E_m.
}
\]

The precursor also satisfies

\[
\boxed{
\|\Omega_m\|_\infty
\lesssim
E_m^{1/8}\|D^2\Omega_m\|_2^{3/4}.
}
\]

Thus a non-small precursor maximum is already a V2 concentration event; otherwise the precursor maximum tends to zero.

---

# 3. Global H1 lifespan is much stronger than the logarithmic-time bound

The classical enstrophy estimate is

\[
|Q|
\lesssim
E^{3/4}P^{3/4}
\le
\frac\nu2P+C\nu^{-3}E^3.
\]

Hence

\[
\boxed{
E'\le C\nu^{-3}E^3.
}
\]

Integrating from the clean minimum to the coherent crossing gives

\[
\boxed{
s_c-s_m
\gtrsim
\nu^3E_m^{-2}.}
\]

Using the deep ceiling,

\[
\boxed{
s_c-s_m
\gtrsim
\nu^3W/R^{2\beta}.}
\]

In physical variables,

\[
\boxed{
t_c-t_m
\gtrsim
\nu^3R^{-2\beta}.}
\]

This dominates the earlier `log R` and local `R^2` separation estimates on the clean branch.

---

# 4. Clean precursor linear inheritance is erased

Let

\[
T=s_c-s_m.
\]

The divergence-free scalar adjoint kernel satisfies

\[
\|K_T\|_2
\lesssim
(\nu T)^{-3/4}.
\]

Therefore

\[
|P_{s_m,s_c}\Omega_m(x_c)|
\lesssim
(\nu T)^{-3/4}E_m^{1/2}.
\]

Using

\[
T\gtrsim\nu^3E_m^{-2},
\]

we obtain

\[
\boxed{
|P\Omega_m(x_c)|
\lesssim_\nu E_m^2
=o(1).
}
\]

Thus the future coherent vorticity cannot be inherited from the clean precursor by the homogeneous advection--diffusion part of the vorticity equation.

---

# 5. Stretching source older than W^(1/3+) is erased

The source satisfies

\[
\|S\Omega\|_1
\lesssim E.
\]

The adjoint kernel ceiling is

\[
\|K_\tau\|_\infty
\lesssim
(\nu\tau)^{-3/2}.
\]

The global normalized enstrophy-time budget is

\[
\int E(s)ds
\lesssim_\nu
W^{1/2}\|u_0\|_2^2.
\]

Hence source older than age `L` contributes at most

\[
C_{\nu,u_0}W^{1/2}L^{-3/2}.
\]

Take

\[
\boxed{L=W^{1/3+\delta}.}
\]

Then

\[
\boxed{
I_{\rm old}=O(W^{-3\delta/2})=o(1).
}
\]

The exponent `1/3` therefore reappears independently as the natural pointwise old-source cutoff.

---

# 6. Fresh-generation identity

Combining Sections 4 and 5,

\[
\boxed{
\Omega(s_c,x_c)
=
\int_0^{W^{1/3+\delta}}
P_{s_c-\tau,s_c}(S\Omega)(x_c)d\tau
+o(1).
}
\]

Since

\[
|\Omega(s_c,x_c)|\ge c_0,
\]

the recent stretching integral carries a fixed order-one amount.

This is now the direct source-active endgame.

---

# 7. The recent layer automatically carries R^3 ordinary enstrophy occupancy

The coherent crossing has

\[
\boxed{E_c\gtrsim R^3.}
\]

The first-hitting cap also gives

\[
E'\le C E.
\]

Therefore on a fixed terminal normalized time block

\[
[s_c-\tau_0,s_c],
\]

\[
E(s)
\gtrsim
R^3.
\]

Hence

\[
\boxed{
D_L
:=
\int_0^L E(s_c-\tau)d\tau
\gtrsim R^3.
}
\]

In physical variables this terminal block costs

\[
\boxed{
\nu\int\|\omega\|_2^2dt
\gtrsim
c\nu R^3/W^{1/2}.
}
\]

This may still be summable on a super-separated sequence.

---

# 8. Thin recent source is routed to V2

The recent pointwise source obeys

\[
\|K_\tau\|_{4/3}
\lesssim
(\nu\tau)^{-3/8},
\]

\[
\|S\Omega\|_4
\lesssim
M^{3/2}E^{1/4},
\qquad
M=\|\Omega\|_\infty.
\]

Thus, with

\[
A_L=\int_0^L\tau^{-1/2}M^2d\tau,
\]

an order-one recent source gives

\[
\boxed{D_LA_L^3\gtrsim\nu^{3/2}.}
\]

The Gagliardo--Nirenberg bound

\[
M^2
\lesssim
E^{1/4}Z^{3/4},
\qquad
Z=\|D^2\Omega\|_2^2,
\]

gives

\[
A_L
\lesssim
D_L^{1/4}
\left(
\int_0^L\tau^{-2/3}Z\,d\tau
\right)^{3/4}.
\]

Therefore

\[
\boxed{
D_L^7
\left(
\int_0^L\tau^{-2/3}Z\,d\tau
\right)^9
\gtrsim
\nu^6.
}
\]

This does not replace the automatic `R^3` occupancy. It says that attempts to make the actual source more singular/thin are routed into the already typed V2 / higher-derivative hierarchy.

---

# 9. Stochastic/Malliavin route remains as an independent structural cross-check

The stochastic Cauchy invariant still gives the exact condition-number / variance dichotomy:

\[
\mathcal Q_D/R^3=O(1)
\Longrightarrow
\text{positive product measure of histories with }
\kappa(D)\gtrsim q^{3/2}.
\]

Every path also has the pulled-back Gramian

\[
C_T=\int F^{-1}F^{-T}ds.
\]

Two exact pathwise bounds are now available:

\[
\boxed{
(\mu_2\mu_3)^{1/2}
\ge T
}
\]

from Minkowski determinant + `det F=1`, and

\[
\boxed{
(\mu_2\mu_3)^{1/2}
\gtrsim q_p/J_p
}
\]

from deformation--diffusion compensation.

Thus

\[
\boxed{
(\mu_2\mu_3)^{1/2}
\gtrsim
\max\{T,q_p/J_p\}.
}
\]

Malliavin randomness of `F` and `C` is generated only by `nabla^2 U`, hence by a deformation-weighted ordinary vorticity-gradient/Hessian channel.

This route is consistent with, but no longer required for, the direct conclusion that terminal vorticity must be freshly generated by recent stretching.

---

# 10. External localized-smoothing audit

Barker--Prange localized critical smoothing provides an independent check on the clean precursor geometry.

After rescaling `B_R` to the unit ball, the clean precursor satisfies

\[
\|v_0\|_{L^3(B_2)}\to0,
\qquad
\|v_0\|_{L^2_{uloc}}^2
\lesssim
R E_m
\to0
\]

for `beta<4`.

Their local smoothing therefore rules out reconstruction of the coherent crossing inside a fixed fraction of one `R^2` parabolic time. The stronger global cubic-enstrophy lifespan `E_m^-2` is the preferred internal estimate, but the external theorem independently validates the local critical-vacuum interpretation.

---

# 11. What is no longer the main final branch

The following are no longer kept as separate endgames:

- direct linear inheritance from a far clean precursor;
- stretching source from arbitrarily old normalized times;
- deterministic late flux creation detached from ancestry;
- one exceptional stochastic loop geometry;
- a purely spatial-affine-versus-non-affine matrix escape;
- a superlarge deep-affine product barrier (withdrawn after scaling correction).

---

# 12. Current single proof wall

The live critical mechanism is now:

\[
\boxed{
\begin{gathered}
\text{fresh stretching inside the recent }W^{1/3+}\text{ layer}\\
+\\
R^3\text{ normalized enstrophy occupancy}\\
+\\
\text{possible V2/high-curvature concentration when the source is thinned}.
\end{gathered}
}
\]

An infinite singular cascade can still evade the finite physical energy budget by making the corresponding physical costs shrink rapidly:

\[
R^3/W^{1/2},
\qquad
R^{-\beta},
\qquad
\text{and derivative costs}
\]

may remain summable on a super-separated sequence.

Therefore the missing theorem is now a **recent-source scale-time nonrepeatability theorem**:

> A finite-energy smooth 3D Navier--Stokes solution cannot execute infinitely many first-hitting episodes in which an order-one coherent `R_j^3` vorticity core is freshly regenerated inside the recent `W_j^(1/3+)` source horizon while the required ordinary enstrophy occupancy and any compensating V2/high-curvature concentration remain compatible with the finite global dissipation and derivative ledgers.

No proof of this theorem has yet been obtained.

Overall status: **CLEAN PRECURSOR ERASED / OLD SOURCE ERASED / ENDGAME TEMPORALLY LOCALIZED TO RECENT STRETCHING WITH `R^3` ENSTROPHY OCCUPANCY AND OPTIONAL V2 CONCENTRATION / GLOBAL REGULARITY NOT PROVED.**
