# DSD M5-651 — Every vorticity-amplitude superlevel has a strictly negative flux-weighted kappa balance

Date: 2026-09-03

Status: **INTERNAL ELLIPTIC SUPERLEVEL IDENTITY / THE CE-H PARALLEL EIGENFIELD EQUATION `Delta rho=(kappa+|nabla xi|^2)rho` IMPLIES THAT FOR EVERY POSITIVE REGULAR AMPLITUDE LEVEL `a`, THE SUPERLEVEL `Omega_a={rho>a}` SATISFIES `int_{Omega_a} kappa rho = -int_{rho=a}|nabla rho| - int_{Omega_a}rho|nabla xi|^2 < 0` / IN VORTEX-TUBE COORDINATES THIS IS A STRICTLY NEGATIVE FLUX-WEIGHTED LINE-LENGTH BALANCE `int kappa_lambda L_a(lambda) dPhi_lambda<0` / THUS POSITIVE-KAPPA FLUX RECHARGE ON HIGH-AMPLITUDE VORTEX LINES MUST BE OVERPAID BY NEGATIVE-KAPPA HIGH-AMPLITUDE LINE LENGTH AND/OR MAGNITUDE/DIRECTION GEOMETRIC COST AT THE SAME THRESHOLD / THIS STRONGLY CONSTRAINS BUT DOES NOT YET ELIMINATE MULTI-SHEET/OSCILLATORY RECHARGE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Parallel CE-H amplitude equation

Write

\[
W=\rho\xi,
\qquad
\rho=|W|,
\qquad
|\xi|=1.
\]

The global CE-H eigenfield equation

\[
\Delta W=\kappa W
\]

splits into the parallel scalar equation

\[
\boxed{
\Delta\rho
=
(\kappa+|\nabla\xi|^2)\rho.
}
\]

Equivalently,

\[
\boxed{
\kappa\rho
=
\Delta\rho-\rho|\nabla\xi|^2.
}
\]

---

## 2. Positive amplitude superlevels are bounded

Fix a positive regular value `a>0` of `rho` and define

\[
\boxed{
\Omega_a:=\{y\in\mathbb R^3:\rho(y)>a\}.
}
\]

The terminal/similarity far-field decay gives

\[
\rho(y)\to0
\quad\text{as }|y|\to\infty,
\]

uniformly on the compact hard hull.

Hence `Omega_a` is bounded.

For a regular value its boundary is

\[
\partial\Omega_a=\{\rho=a\}
\]

up to the usual finite-component decomposition.

---

## 3. Exact superlevel identity

Integrate the parallel equation over `Omega_a`:

\[
\int_{\Omega_a}\kappa\rho\,dy
=
\int_{\Omega_a}\Delta\rho\,dy
-
\int_{\Omega_a}\rho|\nabla\xi|^2dy.
\]

On the boundary of a superlevel, the outward unit normal is

\[
n=-\frac{\nabla\rho}{|\nabla\rho|}.
\]

Therefore

\[
\int_{\Omega_a}\Delta\rho\,dy
=
\int_{\partial\Omega_a}\partial_n\rho\,dS
=
-\int_{\{\rho=a\}}|\nabla\rho|\,dS.
\]

Hence

\[
\boxed{
\int_{\Omega_a}\kappa\rho\,dy
=
-
\int_{\{\rho=a\}}|\nabla\rho|\,dS
-
\int_{\Omega_a}\rho|\nabla\xi|^2dy.
}
\]

Both terms on the right are nonnegative before the minus sign.

Thus

\[
\boxed{
\int_{\Omega_a}\kappa\rho\,dy\le0.
}
\]

For a nontrivial CE-H hard state the identity is strict for every regular level whose superlevel contains genuine vorticity structure; simultaneous vanishing would force `rho` constant on the bounded superlevel with zero direction gradient and is incompatible with the level boundary/nontrivial L2 field.

Thus on the retained levels of interest,

\[
\boxed{
\int_{\Omega_a}\kappa\rho\,dy<0.
}
\]

---

## 4. Relation to the previous power-weight identities

M5-634 gave, for `p>=2`,

\[
\int\kappa\rho^p
=
-(p-1)\int\rho^{p-2}|\nabla\rho|^2
-
\int\rho^p|\nabla\xi|^2.
\]

The present result is stronger in localization: it does not average all amplitudes with one power weight.

Instead it gives a signed inequality separately on **every amplitude superlevel**.

This is the natural layer-cake version of the M5-634 family.

---

## 5. Vortex-tube coordinate form

On CE-H,

\[
W\cdot\nabla\kappa=0,
\]

so `kappa` is constant along each instantaneous vortex line.

In a regular vortex flow box, let `dPhi` be the positive transverse vorticity-flux measure and `ds` arclength along a vortex line.

Since

\[
d\Phi=\rho\,dA,
\]

the volume element is

\[
\boxed{
dV=\frac{d\Phi\,ds}{\rho}.
}
\]

Therefore

\[
\kappa\rho\,dV
=
\kappa\,d\Phi\,ds.
\]

Let

\[
L_a(\lambda)
:=
\mathcal H^1
\left(
\{\text{points on vortex leaf }\lambda:\rho>a\}
\right)
\]

be the total high-amplitude arclength of one leaf.

Using the M5-644--647 transverse atlas and partitioning if needed,

\[
\boxed{
\int_{\Omega_a}\kappa\rho\,dy
=
\int_{\mathcal L}
\kappa_\lambda L_a(\lambda)\,d\Phi_\lambda.
}
\]

Hence

\[
\boxed{
\int_{\mathcal L}
\kappa_\lambda L_a(\lambda)\,d\Phi_\lambda
<0.
}
\]

---

## 6. Positive and negative line populations

Split the leaf space at one time into

\[
\mathcal L_+:=\{\kappa_\lambda>0\},
\qquad
\mathcal L_-:=\{\kappa_\lambda<0\}.
\]

Then

\[
\int_{\mathcal L_+}
\kappa_\lambda L_a\,d\Phi
<
\int_{\mathcal L_-}
|\kappa_\lambda|L_a\,d\Phi.
\]

More precisely the deficit is exactly

\[
\boxed{
D_a
:=
\int_{\{\rho=a\}}|\nabla\rho|dS
+
\int_{\Omega_a}\rho|\nabla\xi|^2dy
>0.
}
\]

Thus

\[
\boxed{
\int_{\mathcal L_-}
|\kappa|L_a\,d\Phi
-
\int_{\mathcal L_+}
\kappa L_a\,d\Phi
=D_a.
}
\]

Positive multiplier activity on high-amplitude leaves is therefore strictly inefficient: it is overpaid by negative activity plus geometric dissipation at the same amplitude threshold.

---

## 7. Why this is relevant to multi-sheet recharge

M5-648--649 close one connected common-law relabeling sheet because lower relative flux cannot recharge.

M5-650 retains the possibility that a packet transfers between different relabeling sheets or enters a genuinely cross-level forced branch, allowing its absolute/relative `kappa` sign to change.

Such a recharge can only occur through positive `kappa` phases.

If the recharging bundle simultaneously carries a coherent high-amplitude segment of length at least `ell_a>0`, then its positive material-flux growth rate is represented inside

\[
\int_{\mathcal L_+}\kappa L_a\,d\Phi.
\]

The superlevel identity says this positive recharge cannot be isolated; at the same threshold the system must carry an even larger negative flux-weighted line-length budget or pay the explicit `D_a` geometric deficit.

This converts multi-sheet recharge from an unpriced sign switch into a quantitatively compensated process.

---

## 8. Finite total high-amplitude line measure

The total flux-weighted high-amplitude arclength is

\[
\int_{\mathcal L}L_a\,d\Phi
=
\int_{\Omega_a}\rho\,dy.
\]

Since `rho>a` on `Omega_a`,

\[
\rho\le\frac{\rho^2}{a},
\]

so

\[
\boxed{
\int_{\mathcal L}L_a\,d\Phi
\le
\frac{E}{a}
\le
\frac{Z_*}{a}.
}
\]

Thus at every fixed amplitude threshold there is a finite instantaneous flux-weighted high-amplitude line-length resource.

This does not by itself give a time-integrated contradiction because the same line resource can change and recharge over time.

---

## 9. Firewall

The inequality

\[
\int\kappa L_a\,d\Phi<0
\]

does **not** imply `kappa<=0` on every vortex line.

Positive-`kappa` lines are allowed, provided they are overcompensated by negative lines/geometric deficit.

Nor does the instantaneous strict deficit alone prevent a recurrent oscillator in which flux is lost and later recharged.

A closure requires coupling this spatial inefficiency to a time-recurrent bounded resource or to the cross-level sheet-transfer dynamics.

---

## 10. Updated multi-sheet target

Any surviving multi-sheet/forced recharge mechanism must now satisfy, at every retained amplitude threshold,

\[
\boxed{
\text{positive high-amplitude flux recharge}
+
D_a
\le
\text{negative high-amplitude flux consumption}
}
\]

in the precise flux-weighted line-length sense above.

The next useful calculation is the time evolution of a truncated amplitude functional such as

\[
\int(\rho-a)_+dy,
\]

which imports this strict spatial deficit into a bounded/recurrent temporal ledger.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]