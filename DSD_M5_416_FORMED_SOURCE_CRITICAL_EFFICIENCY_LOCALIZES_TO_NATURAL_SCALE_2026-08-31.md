# DSD M5-416 — Formed-source critical efficiency localizes to the natural scale

Date: 2026-08-31

Status: **A FORMED NATURAL-STRENGTH VORTICITY CARRIER OF SCALE `r` AT DISTANCE `d` FROM A FIRST-HITTING TARGET OF NATURAL SCALE `s` HAS DIMENSIONLESS STRAIN EFFICIENCY AT MOST `C s^2 r/(d+r)^3` / AFTER `a=r/s`, `b=d/s`, THE EFFICIENCY IS `C a/(a+b)^3` / REMOTE SOURCING IS OPTIMALLY ONLY `O(b^-2)`, SUBNATURAL SOURCING IS `O(a)`, AND OVERCOARSE SOURCING IS `O(a^-2)` / THEREFORE ANY NEAR-EFFICIENT FORMED SOURCE MUST LIVE AT COMPARABLE SCALE AND COMPARABLE DISTANCE, EXACTLY THE M5-394 NATURAL COMPANION WINDOW / THIS IS A VARIATIONAL LOCALIZATION OF FORMED SOURCE EFFICIENCY, NOT YET A REGULARITY CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-415 identifies the true post-pruning target: obtain information stronger than bare critical-norm escalation by exploiting first-hitting source/material geometry.

M5-362 shows that first-hitting amplification needs a misaligned Biot--Savart source, and M5-394 shows that a fixed-fraction natural source forms an actual scale-invariant companion flux carrier.

M5-408 then identifies each formed natural carrier as an order-one atom in the critical vorticity space `dot H^{-1/2}` / velocity space `dot H^{1/2}`.

The present note asks a variational question:

> For one fixed critical carrier cost, how efficiently can a formed source at arbitrary scale and distance supply the natural strain required by a first-hitting target?

The answer is that the efficient window is necessarily natural-scale and local.

---

## 2. Target normalization

Let the target first-hitting carrier have natural length

\[
s=\sqrt{\frac{\nu}{W_A}},
\]

so its natural strain scale is

\[
\boxed{
S_A^{nat}\asymp W_A\asymp\frac{\nu}{s^2}.
}
\]

A first-hitting stage with bounded normalized length requires an order-one fraction of this strain at some stage time by M5-340/M5-362.

---

## 3. One formed source carrier

Let `B` be a coherent formed vorticity carrier with characteristic radius `r`, center distance `d` from the target center, and natural-strength amplitude bound

\[
|\omega_B|\lesssim\frac{\nu}{r^2}
\]

on a region of volume `O(r^3)`.

Then

\[
\boxed{
\|\omega_B\|_{L^1}\lesssim \nu r.
}
\]

This is the same natural scaling as the M5-394 companion and the later formed replacement carriers.

---

## 4. Unified Biot--Savart/CZ strain bound

If `d` is larger than a fixed multiple of `r`, the Biot--Savart strain kernel gives

\[
|S_{B\to A}|
\lesssim
\frac{\|\omega_B\|_1}{d^3}
\lesssim
\frac{\nu r}{d^3}.
\]

If the target lies at distance `O(r)` or inside the coherent source region, the pointwise singular integral is controlled by the carrier's normalized smoothness/analyticity and natural amplitude:

\[
|S_{B\to A}|
\lesssim
\frac{\nu}{r^2}.
\]

These two regimes are summarized, up to a fixed carrier-shape constant, by

\[
\boxed{
|S_{B\to A}|
\lesssim
\frac{\nu r}{(d+r)^3}.
}
\]

This interpolation has the correct dimensions and reproduces both limiting estimates.

The statement is for a coherent formed carrier. A diffuse multiscale field that cannot be decomposed into such carriers remains in the distributed-shell/capacity branch and is not silently included here.

---

## 5. Dimensionless source efficiency

Normalize by the target natural strain:

\[
\eta(B\to A)
:=
\frac{|S_{B\to A}|}{\nu/s^2}.
\]

Then

\[
\boxed{
\eta(B\to A)
\lesssim
\frac{s^2r}{(d+r)^3}.
}
\]

Set

\[
a=\frac rs,
\qquad
b=\frac ds.
\]

Then

\[
\boxed{
\eta(a,b)
\lesssim
\frac{a}{(a+b)^3}.
}
\]

This is scale- and translation-invariant and therefore is a natural phase-space efficiency descriptor.

---

## 6. Remote optimization

Fix a remote normalized distance `b>0` and optimize over the source scale `a>0`.

For

\[
f_b(a)=\frac{a}{(a+b)^3},
\]

\[
f_b'(a)
=\frac{b-2a}{(a+b)^4}.
\]

Thus the unique maximum occurs at

\[
\boxed{a=\frac b2.}
\]

At that point

\[
f_b(b/2)
=
\frac{b/2}{(3b/2)^3}
=
\frac{4}{27}b^{-2}.
\]

Therefore

\[
\boxed{
\sup_{r>0}
\eta(B\to A)
\lesssim
\frac{4}{27}
\left(\frac{s}{d}\right)^2.
}
\]

Hence a genuinely remote formed carrier cannot supply order-one target strain at fixed critical-carrier cost.

Even the optimal remote carrier chooses its own scale comparable to its distance from the target and still loses quadratically in `d/s`.

---

## 7. Subnatural inefficiency

Suppose the source remains at target distance `d\asymp s` but has

\[
r\ll s.
\]

Then `b\asymp1` and `a\ll1`, so

\[
\boxed{
\eta(a,b)\lesssim Ca
\asymp C\frac rs.
}
\]

Thus one subnatural formed source becomes linearly inefficient as its scale drops below the target natural scale.

To replace one order-one natural source by fixed-flux subnatural formed atoms, the required atom count must grow at least like `s/r`, modulo bounded-overlap and angular-sign efficiencies.

This agrees with the earlier high-frequency/capacity routing.

---

## 8. Overcoarse inefficiency

If

\[
r\gg s
\]

while `d=O(s)` or even `d=O(r)`, then

\[
\eta(a,b)
\lesssim
Ca^{-2}
\asymp
C\left(\frac sr\right)^2.
\]

Thus a broad coarse carrier is also inefficient at supplying the target natural strain.

This is the formed-carrier version of the affine/harmonic observation that a large-scale field must carry increasing global critical structure if it is to maintain a fixed small-scale strain.

---

## 9. The efficient window

Fix any efficiency threshold `epsilon_*>0` below the carrier-shape constant.

The condition

\[
\eta(a,b)\ge\epsilon_*
\]

forces `a` and `b` into a compact subset of `(0,infinity) x [0,infinity)`.

In particular there exist constants depending only on `epsilon_*` and the fixed carrier shape bounds such that

\[
\boxed{
c_*(\epsilon_*)
\le
\frac rs
\le
C_*(\epsilon_*),
}
\]

and

\[
\boxed{
\frac ds
\le
D_*(\epsilon_*).
}
\]

Thus any formed source carrying a fixed fraction of the required first-hitting strain with bounded critical atom cost must have

\[
\boxed{
r\asymp s,
\qquad
d\asymp s
}
\]

up to fixed constants.

This is precisely the natural companion geometry produced by M5-394.

---

## 10. Critical-atom interpretation

M5-408 shows that every fixed-flux natural carrier has a critical atom cost

\[
\|\omega_B\|_{\dot H^{-1/2}}^2
\gtrsim
c\nu^2
\]

in the Bessel-separated formed regime.

Therefore the efficiency law can be read as a cost-per-source statement:

\[
\boxed{
\text{one order-one critical atom at phase-space distance }(a,b)
\text{ contributes at most }C\frac{a}{(a+b)^3}
}
\]

to the target's normalized natural strain.

Remote or badly scale-mismatched formed atoms are therefore inefficient in the exact critical currency identified in M5-408.

---

## 11. Consequence for near-minimal critical throughput

Consider any formed-source configuration that supplies a fixed normalized stretching amount `c_gamma>0` to a first-hitting target.

If its total critical atom budget is near the minimum compatible with that target stretching, then it cannot spend most of that budget on atoms with arbitrarily small `eta`.

Hence every near-minimal formed-source sequence has a positive fraction of its effective source budget in a compact natural phase-space window:

\[
\boxed{
r/s\asymp1,
\qquad
d/s=O(1).
}
\]

This is a variational localization statement for a prospective critical element.

It does not yet prove that such a local critical element is impossible.

---

## 12. Relation to the remote recursion

M5-409--410 show that remote-of-remote recursion either creates new phase-space content or reuses a finite source family inefficiently.

The present law explains quantitatively why finite remote reuse fails:

\[
\eta_{remote}
\lesssim
C(d/s)^{-2}
\to0.
\]

Thus an iterated remote branch that continues to supply order-one first-hitting strain must continually increase its critical formed-source budget or return to a natural local companion at the newly selected target scale.

Remote relocation is therefore an inefficient representation of the same critical throughput, not a separate efficient mechanism.

---

## 13. Firewall

The estimate does **not** prove

\[
H_{throughput}^{crit}\Rightarrow\bot.
\]

A hypothetical singularity is allowed to pay an arbitrarily large critical atom budget.

The estimate also does not cover a completely diffuse source field by pretending it is a finite family of fixed-flux carriers. Such a field remains in the distributed shell/frequency/capacity branch and must be priced with the existing diffuse-packing machinery.

Finally, an order-one natural companion is not shown to have nonlinear efficiency below viscosity. The present result localizes the efficient source geometry; it does not close that geometry.

---

## 14. Next target

The critical problem is now sharper.

For a near-minimal formed throughput event, the source must reduce to the compact natural configuration

\[
\boxed{
\text{main first-hitting carrier}
+
\text{misaligned natural companion(s)}.
}
\]

The next question is whether this compact dual/multicarrier geometry has a strict nonlinear-production versus critical-dissipation inequality, or whether an explicit local anti-model shows that no such universal gap exists.

That is the correct M5-417 target.

---

## 15. Audit verdict

### DERIVED

- formed-source strain efficiency
  \[
  \eta\lesssim s^2r/(d+r)^3;
  \]
- remote optimum
  \[
  \eta_{max}(d/s)\lesssim (d/s)^{-2};
  \]
- subnatural inefficiency `O(r/s)`;
- overcoarse inefficiency `O((s/r)^2)`;
- near-efficient formed source localization to the natural phase-space window.

### STILL OPEN

- diffuse source efficiency outside the formed-atom model;
- strict production/dissipation gap for the natural dual-flux cluster;
- exclusion of unlimited critical throughput;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
