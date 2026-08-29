# DSD M5-248 — Uniform Small-`rho` Tail Certificate to Fixed-W1-Window Inheritance

Date: 2026-08-30

Parent: `DSD_M5_247_ENERGY_VISIBLE_RESIDUAL_FLUX_DERIVATIVE_LARGE_STRUCTURE_ROUTING_2026-08-30.md`

Status: **MAJOR INTERFACE BRIDGE / A ROBUST POSITIVE LOCAL CERTIFICATE ON THE CANONICAL TAIL DOES NOT REQUIRE FULL EXPANDING-WINDOW CONVERGENCE TO REACH THE W1 OR FINITE-STAGE SOLUTION / EXACT RG RECONSTRUCTION IS UNIFORMLY CONTINUOUS AT `rho=0` ON THE COMPACT REALIZED TAIL HULL, SO ONE FIXED SMALL POSITIVE `rho_*` PRESERVES A FIXED FRACTION OF THE TAIL CERTIFICATE / BY DESCENDANT COVARIANCE THIS BECOMES A CERTIFICATE ON ONE FIXED FINITE NORMALIZED ANNULUS OF A W1 STATE, WHICH DOES PASS TO LARGE FINITE FIRST-HITTING STAGES BY ORDINARY FIXED-WINDOW COMPACTNESS / GLOBAL REGULARITY UNPROVED.**

---

## 1. The interface problem

The W1 canonical tail is a scale-infinity object.  Earlier audits correctly isolated the Expanding-Window Gate because local convergence of finite-stage rescalings to a W1 state does not imply convergence on radii

\[
R_j\to\infty.
\]

However M5-237--240 now provide additional structure: every **realized** tail has a unique backward-RG reconstruction

\[
\mathscr R_\rho(T),
\qquad 0\le\rho\le1,
\]

with

\[
\mathscr R_0(T)=T,
\qquad
\mathscr R_1(T)=\mathfrak T^{-1}(T).
\]

This lets a robust tail certificate be moved a fixed positive distance away from scale infinity before returning to finite-stage compactness.

---

## 2. Exact integral reconstruction

M5-237 gives

\[
\boxed{
\partial_\rho\mathscr R_\rho(T)
=-\mathcal F(\mathscr R_\rho(T)),
}
\]

so

\[
\boxed{
\mathscr R_\rho(T)-T
=-\int_0^\rho
\mathcal F(\mathscr R_\sigma(T))d\sigma.
}
\]

Fix one punctured normalized cell `K` and a topology `X(K)` strong enough for the certificate under consideration, for example:

- `L2/H1` for strain/gradient energy;
- `H1/H2` for derivative certificates;
- local `C^1` or stronger for a robust coefficient-amplitude certificate.

On the retained smooth punctured W1 corridor, the set

\[
\{\mathscr R_\sigma(T):T\in\mathcal T,\ 0\le\sigma\le\rho_0\}
\]

is compact in the corresponding local regularity class for sufficiently small fixed `rho0`.

Hence

\[
\boxed{
M_{F,K}
:=
\sup_{T\in\mathcal T,\ 0\le\sigma\le\rho_0}
\|\mathcal F(\mathscr R_\sigma(T))\|_{X(K)}
<\infty.
}
\]

Therefore

\[
\boxed{
\|\mathscr R_\rho(T)-T\|_{X(K)}
\le M_{F,K}\rho
}
\]

uniformly over the entire compact tail hull.

---

## 3. Abstract robust-certificate lemma

Let

\[
\mathcal C:X(K)\to[0,\infty)
\]

be a continuous local certificate.

Assume the surviving tail branch supplies a uniform floor

\[
\boxed{
\mathcal C(T)\ge c_*>0
\qquad\forall T\in E
}
\]

on a compact recurrent subset `E` of tail phases (or on a positive-measure compact sublevel selected from the invariant hull).

Uniform continuity of `C` on the compact local class gives a radius `delta_C>0` such that

\[
\|U-T\|_{X(K)}<\delta_C
\Longrightarrow
|\mathcal C(U)-\mathcal C(T)|<c_*/2.
\]

Choose

\[
\boxed{
0<\rho_*
<
\min\left\{
\rho_0,
\frac{\delta_C}{M_{F,K}}
\right\}.
}
\]

Then for every `T in E`,

\[
\boxed{
\mathcal C(\mathscr R_{\rho_*}(T))
\ge\frac{c_*}{2}.
}
\]

This is a **uniform fixed-positive-RG-depth inheritance theorem**.

---

## 4. Convert fixed `rho_*` to finite descendant time

Write

\[
\rho_*=e^{-h_*},
\qquad
R_*=e^{h_*/2}=\rho_*^{-1/2}.
\]

Both `h_*` and `R_*` are finite constants independent of the first-hitting stage index.

By definition of the descendant,

\[
\boxed{
\mathscr R_{\rho_*}(T_V)(Y)
=
\mathcal D_{h_*}[V](Y)
=
R_*\,(S(h_*)V)(R_*Y).
}
\]

Thus a certificate on a unit cell for `R_{rho_*}(T)` is exactly a scale-normalized certificate of the actual W1 state

\[
S(h_*)V
\]

on the finite annulus

\[
R_*K.
\]

Crucially,

\[
\boxed{R_*<\infty\text{ is fixed}.}
\]

No expanding normalized window occurs.

---

## 5. Return to finite first-hitting stages

The W1 state `S(h_*)V` is obtained as a fixed-time limit of the finite first-hitting rescalings on every fixed compact normalized cylinder.

Since `R_*K` is fixed, the standard local compactness package gives, after the chosen subsequence,

\[
U_j^{(h_*)}\to S(h_*)V
\]

strongly in the local topology needed by the certificate.

Therefore for all sufficiently large `j`,

\[
\boxed{
\mathcal C(U_j^{(h_*)})
\ge\frac{c_*}{4}
}
\]

on the same fixed normalized annulus/cell.

Thus a robust positive tail certificate becomes an actual finite-stage witness.

---

## 6. Application to the M5-247 common frontier

The residual-gap branch was reduced to

\[
R_{gap}
\Longrightarrow
S_{amp}\lor H_{tail}\lor L_{tail}.
\]

Each can be represented by a robust local certificate after the usual finite-threshold selection.

### Strain amplitude

For example

\[
\mathcal C_S(T)
=
\|\mathcal S_T\|_{L^2(K)}
\]

or a localized compressive/radial-strain version.

A positive tail floor therefore gives a finite-stage normalized strain witness on a fixed annulus.

### H derivative

Use a localized derivative norm such as

\[
\mathcal C_H(T)
=
\|\nabla T\|_{L^2(K)}
\]

or the retained H2 norm after choosing a branch with a fixed lower threshold.

This too passes to a finite-stage fixed-window derivative witness.

### Large coefficient

If the branch is stated as a robust local `C^k` amplitude threshold, strong local smooth convergence preserves half of the threshold at fixed positive `rho_*` and at finite stage.

Thus

\[
\boxed{
S_{amp},H_{tail},L_{tail}
\Longrightarrow
\text{finite-stage fixed-window witnesses}.
}

---

## 7. What this does not prove

M5-248 does **not** prove full expanding-window convergence of the original finite-stage sequence to the canonical tail.

It does not identify the physical solution on every fixed physical radius with the static tail trace.

The full EWG remains relevant for claims that require following the tail all the way to normalized radius

\[
R_j\asymp r_j^{-1}.
\]

The new point is narrower and stronger for the current endgame:

\[
\boxed{
\text{a robust local tail obstruction can be pulled back through one fixed RG depth, so full EWG is unnecessary for that obstruction.}
}
\]

---

## 8. DSD interface audit

The order of operations is essential:

1. form the canonical tail on the compact W1 hull;
2. use the **realized RG reconstruction** at one fixed `rho_*>0`;
3. convert by exact descendant scaling to one finite W1 annulus;
4. only then pass from W1 to finite stages on a fixed window.

The invalid order would be

\[
\text{finite stages}
\to
R_j\to\infty
\to
\text{tail}
\]

without an expanding-window theorem.

M5-248 does not use that invalid limit.

---

## 9. Updated frontier

The previous interface gap

\[
\text{tail }S/H/L
\stackrel{?}{\Longrightarrow}
\text{finite-stage H/T}
\]

is now partially closed:

\[
\boxed{
\text{robust tail }S/H/L
\Longrightarrow
\text{finite-stage fixed-normalized-window }S/H/L.
}
\]

The remaining obligation is no longer tail inheritance itself.  It is to show that these **finite-stage fixed-window witnesses** are incompatible with the already-defined pure no-H/no-T first-hitting corridor, or to identify exactly which witness was not previously included in `H/T`.

---

## 10. Next target

Match the three inherited finite-stage witness types against the existing definitions of:

- `H` derivative/roughness escape;
- `T` turnover/center/material escape;
- pure bounded-strain/variance corridor.

If `S_amp` and `H_tail` already fall inside the existing `H` complement at the same normalized thresholds, the residual-active tail branch closes on the pure corridor.  Any unmatched `L_tail` coefficient must then be isolated as the final genuinely new finite-stage branch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]