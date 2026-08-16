# Local critical-L3 vacuum forces a full parabolic-time separation before a coherent crossing

Date: 2026-08-16

Status: **DERIVED CONDITIONAL ON THE STANDARD QUANTITATIVE INTERIOR DERIVATIVE CONSEQUENCE OF BARKER--PRANGE LOCALIZED SMOOTHING. THE CLEAN PRECURSOR SATISFIES THEIR INITIAL LOCAL `L3` AND GLOBAL `L2_uloc` HYPOTHESES AFTER `R`-RESCALING. A COHERENT CROSSING CANNOT OCCUR INSIDE A FIXED FRACTION OF ONE `R^2` PARABOLIC TIME. GLOBAL REGULARITY NOT PROVED.**

External primary reference:

- Tobias Barker and Christophe Prange, *Localized smoothing for the Navier--Stokes equations and concentration of critical norms near singularities*, arXiv:1812.09115, Theorem 1 and the bootstrap in Theorem 4.

## 1. Clean precursor data

At the enstrophy-minimum checkpoint `s_m`,

\[
E_m=\|\Omega(s_m)\|_2^2
\lesssim
\frac{R^\beta}{W^{1/2}},
\qquad 0<\beta<4.
\]

The coherent-crossing energy relation gives

\[
W^{1/2}
\gtrsim
R^5(\log R)^{5/2}.
\]

Therefore

\[
\boxed{
E_m
\lesssim
R^{\beta-5}(\log R)^{-5/2}.
}
\]

For divergence-free whole-space velocity,

\[
\|U(s_m)\|_6
\lesssim
\|\nabla U(s_m)\|_2
=E_m^{1/2}.
\]

---

## 2. Vanishing local critical L3 norm on the future core scale

For every spatial center `x0`, Holder gives

\[
\|U(s_m)\|_{L^3(B_{2R}(x_0))}
\lesssim
R^{1/2}E_m^{1/2}.
\]

Hence

\[
\boxed{
\sup_{x_0}
\|U(s_m)\|_{L^3(B_{2R}(x_0))}
\lesssim
R^{(\beta-4)/2}(\log R)^{-5/4}
\to0.
}
\]

This is a uniform local critical-velocity vacuum at radius `R`, not merely smallness at the eventual crossing center.

---

## 3. Rescale radius R to unit size

For any center `x0`, define

\[
v(z,\tau)
=R\,U(x_0+Rz,s_m+R^2\tau).
\]

Then `v` solves the same Navier--Stokes equation, with viscosity unchanged after the harmless fixed-`nu` normalization convention.

The critical norm is invariant:

\[
\boxed{
\|v_0\|_{L^3(B_2)}
=
\|U(s_m)\|_{L^3(B_{2R}(x_0))}
\to0.
}
\]

For the uniformly local L2 norm,

\[
\begin{aligned}
\|v_0\|_{L^2(B_1(z_0))}^2
&=
R^{-1}
\int_{B_R(x_0+Rz_0)}|U(s_m,y)|^2dy\\
&\lesssim
R^{-1}R^2\|U(s_m)\|_6^2\\
&\lesssim
R E_m.
\end{aligned}
\]

Therefore

\[
\boxed{
\|v_0\|_{L^2_{uloc}}^2
\lesssim
R E_m
\lesssim
R^{\beta-4}(\log R)^{-5/2}
\to0.
}
\]

Because the original smooth finite-energy velocity is in `L2(R3)`, the spatial-decay-at-infinity hypothesis in the local-energy framework is also available for each rescaled datum.

Thus, for all sufficiently large `R`, the rescaled initial data satisfy the Barker--Prange Theorem 1 assumptions with one fixed upper bound `M0` and with local `L3` smaller than their universal smallness constant.

---

## 4. Fixed positive rescaled smoothing time

Barker--Prange Theorem 1 gives, for fixed `M0`, a time

\[
S_0=S^*(M_0)>0
\]

independent of the late index, such that `v` is locally bounded and smooth inside a fixed fractional ball for

\[
0<\tau<S_0.
\]

Their Theorem 4 gives the near-initial local bounded/Hölder bootstrap for the perturbation after splitting off the small mild `L3` solution.

Combining that with standard interior parabolic regularity for the smooth solution yields the scale-compatible derivative estimate

\[
\boxed{
\|\nabla v(\tau)\|_{L^\infty(B_{1/4})}
\le
\frac{C_0}{\tau}
}
\]

for `0<tau<S1`, after possibly reducing to one fixed `S1<=S0`; `C0` is independent of the late sequence because the theorem's input norms are uniformly bounded and the local critical datum tends to zero.

The precise power `tau^-1` is the standard critical heat-scale bound; any estimate no worse than this suffices below.

---

## 5. Return to terminal normalization

Vorticity scales as

\[
\omega_v(z,\tau)
=R^2\Omega(x_0+Rz,s_m+R^2\tau).
\]

Hence, inside the corresponding fractional physical/normalized ball,

\[
\boxed{
\|\Omega(s_m+t)\|_\infty
\le
\frac{C_0}{t}
}
\]

whenever

\[
0<t<S_1R^2.
\]

Notice that the radius `R` cancels exactly: this is the scale-critical derivative consequence of localized smoothing.

---

## 6. Intersect with the logarithmic time lower bound

The clean-precursor growth lemma already gives

\[
\boxed{
s_c-s_m\gtrsim c\log R.}
\]

Suppose, for contradiction, that the coherent crossing occurs while

\[
0<s_c-s_m<S_1R^2.
\]

Apply the preceding localized derivative bound with the center chosen to be the future crossing center. Since the precursor smallness was uniform in `x0`, no center-tracking assumption is needed.

Then

\[
\|\Omega(s_c)\|_{L^\infty(B_{cR})}
\lesssim
\frac{1}{s_c-s_m}
\lesssim
\frac{1}{\log R}
\to0.
\]

But the coherent crossing has

\[
|\bar\Omega|\ge c_0>0
\]

and thus order-one vorticity on a fixed fraction of `B_R`. Contradiction.

Therefore every surviving coherent crossing must satisfy

\[
\boxed{
s_c-s_m\ge S_1R^2}
\]

for all sufficiently late members of the sequence.

---

## 7. Meaning

The previous clean-precursor argument only forced a logarithmically long terminal-normalized amplification interval.

Localized critical smoothing upgrades this to a full coherent-radius parabolic time:

\[
\boxed{
\text{clean low-enstrophy precursor}
\longrightarrow
\text{coherent }R\text{-core}
\quad\text{requires at least }cR^2\text{ normalized time.}
}
\]

In physical variables,

\[
\boxed{
\Delta t_{m\to c}
\gtrsim
\frac{R^2}{W}.
}
\]

This matches the parabolic-time scale that previously emerged from material-flux reset, but it is now obtained from a completely different critical-local-smoothing route.

---

## 8. What this does and does not close

This does not yet contradict a Zeno cascade because

\[
\sum_j R_j^2/W_j
\]

may converge.

It does remove any survivor that tries to reconstruct the coherent crossing in a sub-parabolic normalized time after the clean precursor.

Hence the active final branch must preserve/rebuild critical local velocity mass for at least one full `R^2` scale-time block before each coherent crossing, or else enter the already typed V2/higher-derivative branch at the precursor checkpoint.

The next target is to combine this `R^2` persistence with the global enstrophy dissipation budget, the fixed-time scale packing, and the stochastic deformation-weighted derivative ledger.

Overall status: **SUB-PARABOLIC RECONSTRUCTION CLOSED / SURVIVING COHERENT CROSSING REQUIRES A FULL `R^2` NORMALIZED PRECURSOR-TO-CROSSING INTERVAL.**
