# DSD M5-423 — Global far-field critical visibility radius

Date: 2026-08-31

Status: **THE SINGLE-SHELL M5-421 DUALITY ESTIMATE EXTENDS TO THE ENTIRE FAR BIOT--SAVART STRAIN FIELD WITHOUT DYADIC DOUBLE COUNTING / THE STRAIN KERNEL CUT OFF OUTSIDE RADIUS `R` HAS `dot H^{1/2}` NORM `O(R^-2)`, SO `|S_far,R| <= C R^-2 ||omega||_{dot H^-1/2}` / FOR A FIRST-HITTING TARGET OF NATURAL SCALE `s`, ALL VORTICITY OUTSIDE NORMALIZED RADIUS `L` CONTRIBUTES AT MOST `C L^-2 X^(1/2)/nu` OF THE NATURAL STRAIN / THEREFORE AN EFFECTIVE SOURCE WINDOW OF RADIUS `L_eff ~ epsilon^-1/2 (X/nu^2)^(1/4)` CONTAINS ALL BUT AN `epsilon` FRACTION OF THE STRAIN / THIS GIVES A QUARTIC CRITICAL VISIBILITY LAW AND REMOVES THE MULTI-SHELL SUMMATION GAP FOR THE FAR STRAIN ITSELF / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-421 proves the critical duality estimate on one remote shell:

\[
|S_R|
\lesssim
R^{-2}\|\omega_R\|_{\dot H^{-1/2}}.
\]

Its explicit firewall notes that summing localized shell norms in `dot H^{-1/2}` is nontrivial because the space is nonlocal.

For the **total far strain**, no shell sum is needed. One may pair the full vorticity directly with the entire far kernel.

This yields a cleaner global source-visibility radius.

---

## 2. Far Biot--Savart strain kernel

Let `K(y)` be one tensor component of the whole-space strain kernel, homogeneous of degree `-3`.

Choose a fixed smooth radial cutoff `chi` with

\[
\chi(z)=1
\quad\text{for }|z|\le1,
\]

and

\[
\chi(z)=0
\quad\text{for }|z|\ge2.
\]

For target point `x_*`, define the full far test kernel

\[
\boxed{
\Psi_R(y)
:=
K(x_*-y)
\left[
1-\chi\left(\frac{y-x_*}{R}\right)
\right].
}
\]

Then the far strain is

\[
\boxed{
S_{>R}(x_*)
=
\langle\omega,\Psi_R\rangle.
}
\]

Because the singularity at the target is removed, no principal-value issue remains in this far pairing.

---

## 3. The unit far kernel belongs to `dot H^{1/2}`

At unit scale,

\[
\Psi_1(y)
=
K(-y)(1-\chi(y))
\]

is smooth near the origin and behaves like

\[
|y|^{-3}
\]

at infinity.

In particular it lies in `L2`, and its first derivatives decay one power faster and also lie in `L2`.

Thus

\[
\Psi_1\in H^1
\subset
\dot H^{1/2}
\]

for the retained tensor components after the harmless smooth cutoff.

Set

\[
C_K:=\|\Psi_1\|_{\dot H^{1/2}}<\infty.
\]

---

## 4. Exact scaling

By kernel homogeneity,

\[
\Psi_R(y)
=
R^{-3}
\Psi_1\left(\frac{y-x_*}{R}\right).
\]

Homogeneous Sobolev scaling gives

\[
\boxed{
\|\Psi_R\|_{\dot H^{1/2}}
=
C_KR^{-2}.
}
\]

This is the same critical exponent found shell-by-shell in M5-421.

---

## 5. Global far-field duality bound

By `dot H^{-1/2}`--`dot H^{1/2}` duality,

\[
\boxed{
|S_{>R}(x_*)|
\le
C_KR^{-2}
\|\omega\|_{\dot H^{-1/2}}.
}
\]

Using the divergence-free equivalence

\[
\|\omega\|_{\dot H^{-1/2}}
\asymp
\|u\|_{\dot H^{1/2}},
\]

and

\[
X(t)=\|u(t)\|_{\dot H^{1/2}}^2,
\]

we obtain

\[
\boxed{
|S_{>R}(x_*)|
\lesssim
R^{-2}X(t)^{1/2}.
}
\]

No shell orthogonality or localized-norm square sum is used.

---

## 6. Normalize at the first-hitting natural scale

Let the target natural scale be

\[
s=\sqrt{\nu/W}.
\]

The natural strain is

\[
S_{nat}\asymp\frac{\nu}{s^2}.
\]

Write

\[
R=Ls.
\]

Then

\[
\boxed{
\frac{|S_{>Ls}(x_*)|}{\nu/s^2}
\lesssim
L^{-2}
\frac{X(t)^{1/2}}{\nu}.
}
\]

This controls the entire exterior, not merely one annulus.

---

## 7. Effective critical visibility radius

Fix a desired far-strain tolerance `epsilon>0`.

Choose

\[
\boxed{
L_{eff}(t,\epsilon)
:=
C
\epsilon^{-1/2}
\left(
\frac{X(t)}{\nu^2}
\right)^{1/4}.
}
\]

Then

\[
\boxed{
\frac{|S_{>|L_{eff}s}(x_*)|}{\nu/s^2}
\le
\epsilon.
}
\]

Thus all but an `epsilon` fraction of the target natural strain is generated inside a normalized spatial radius growing only like the **fourth root of the global critical mass**.

This is the critical visibility law.

---

## 8. Consequence for a fixed remote fraction

Conversely, if the total field outside normalized radius `L` supplies a fixed fraction `epsilon_0` of the natural strain, then

\[
\boxed{
X(t)
\gtrsim
\epsilon_0^2\nu^2L^4.
}
\]

This reproduces the M5-421 quartic cost but now for the entire exterior field with no shell assignment.

---

## 9. Relation to M5-419 mass accumulation

The M5-419 near-balanced lane permits `X(t)` to diverge, but only slowly relative to cumulative critical dissipation on the selected long blocks.

The present theorem implies that the dynamically relevant source window grows only as

\[
\boxed{
L_{eff}\sim X^{1/4}.
}
\]

For example, if along selected blocks

\[
X_j=o(j),
\]

then for fixed `epsilon`

\[
L_{eff,j}=o(j^{1/4})
\]

up to the chosen tolerance factor.

This is not a contradiction, but it quantitatively constrains how quickly dynamically relevant source geometry can escape in normalized space.

---

## 10. Relation to M5-420 compact-cluster cap

M5-420 shows that every fixed normalized parent ball carries at most `O(nu^2)` critical mass.

The present note shows that critical mass far beyond `L_eff` is dynamically almost invisible to the current core's strain.

Thus the critical field splits naturally into

\[
\boxed{
\text{compact active/source window of radius }O(X^{1/4})
+
\text{far critical reservoir with small instantaneous strain coupling}.
}
\]

The exterior may carry large norm, but it cannot directly produce order-one target stretching from arbitrarily far away without enlarging `X` according to the quartic law.

---

## 11. Relation to source age dilution

For one old source whose physical scale does not co-shrink, the target normalized distance grows geometrically and M5-422 yields `q^-k` age dilution.

The present global theorem is the continuum analogue:

if all old/non-co-shrinking source material eventually lies beyond an increasing normalized radius `L_k`, then its **combined** direct strain influence is at most

\[
C L_k^{-2}X^{1/2}/\nu.
\]

Thus old exterior material cannot defeat source-age dilution merely by distributing itself across many far shells unless the total critical norm grows accordingly.

---

## 12. Why this is stronger than shell-by-shell packing

The M5-421 multi-shell ledger required care because localized `dot H^{-1/2}` shell norms cannot simply be square-summed.

The far-kernel pairing bypasses that issue entirely.

There is one test function `Psi_R`, and duality uses the global critical norm exactly once.

Therefore there is no nested-shell double counting in

\[
\boxed{
|S_{>R}|
\lesssim
R^{-2}X^{1/2}.
}
\]

This is the preferred estimate whenever only the total far strain matters.

---

## 13. Firewall

The effective radius `L_eff` may still diverge because `X(t)` may diverge at a singularity.

The theorem does not give velocity or pressure compactness on the full ball `B_{L_eff}`.

It controls only the **strain contribution from outside** that ball.

Nor does it prove that source structures inside the visibility window are compact or formed; distributed critical throughput may still occur there.

---

## 14. Next target

The natural next question is now localized:

> inside the critical visibility window `L <= C X^{1/4}`, can a near-balanced tower repeatedly hand off the required natural source while `X` grows only sublinearly relative to cumulative critical dissipation?

M5-422 says old non-co-shrinking sources have finite functional age.

Therefore a near-balanced tower must continually create fresh sources or maintain a co-shrinking material source lineage **inside this visibility window**.

This is a much narrower critical-element/nonreuse problem than unrestricted remote sourcing.

---

## 15. Audit verdict

### DERIVED

\[
\boxed{
|S_{>R}|
\lesssim
R^{-2}\|\omega\|_{\dot H^{-1/2}}.
}
\]

and

\[
\boxed{
L_{eff}(t,\epsilon)
\asymp
\epsilon^{-1/2}
\left(\frac{X(t)}{\nu^2}\right)^{1/4}.
}
\]

### GAIN

The full remote exterior is controlled with one critical duality pairing and no shell double counting.

### STILL OPEN

- source handoff/nonreuse inside the growing visibility window;
- co-shrinking recurrent critical element;
- critical-mass accumulation compatible with the quartic visibility law;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
