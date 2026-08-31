# DSD M5-415 — Critical-throughput / H^{1/2} energy firewall and the true next target

Date: 2026-08-31

Status: **THE SINGLE MASTER CLASS `H_throughput^crit` IS NOW COMPARED AGAINST THE STANDARD SCALE-CRITICAL `dot H^{1/2}` ENERGY STRUCTURE / THE M5-408 CARRIER NOVELTY DESCRIPTOR IS CONTROLLED BY THE SAME CRITICAL NORM, AND THE STANDARD `dot H^{1/2}` ENERGY ESTIMATE ONLY CLOSES THE SMALL-NORM REGIME / ON A HYPOTHETICAL SINGULAR CORRIDOR THE CRITICAL NORM MAY DIVERGE, SO REDUCING ALL GEOMETRIC BRANCHES TO CRITICAL THROUGHPUT DOES NOT BY ITSELF ADVANCE PAST THE CLASSICAL CRITICAL-NORM BARRIER / THE GENUINELY NEW NEXT TARGET MUST USE THE FIRST-HITTING MATERIAL/SOURCE GEOMETRY TO PROVE A STRICT EFFICIENCY, NONREUSE, OR CRITICAL-ELEMENT RIGIDITY STATEMENT NOT CONTAINED IN THE BARE H^{1/2} ESTIMATE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-414 reduced the audited master tree to

\[
\boxed{
\text{hypothetical singular tower}
\Longrightarrow
H_{throughput}^{crit}.
}
\]

This is structurally much cleaner than the former H/T/contact/remote/projective/export tree.

But one must now ask whether `H_throughput^crit` is genuinely stronger than the standard statement that a singular solution must lose control of a scale-critical norm.

The correct comparison space is

\[
\dot H^{1/2}(\mathbb R^3)
\]

for velocity, equivalently

\[
\dot H^{-1/2}
\]

for vorticity.

---

## 2. Critical norm and carrier novelty

Set

\[
\boxed{
X(t):=\|u(t)\|_{\dot H^{1/2}}^2
=
\|\omega(t)\|_{\dot H^{-1/2}}^2.
}
\]

M5-408 defines a maximal phase-space carrier count/novelty descriptor `mathfrak N_crit` satisfying

\[
\boxed{
\mathfrak N_{crit}(t)
\lesssim
\nu^{-2}X(t).
}
\]

Thus

\[
\boxed{
\mathfrak N_{crit}(t)\to\infty
\Longrightarrow
X(t)\to\infty.
}
\]

The distributed shell/frequency branch is not always literally a finite carrier count, but once point-picking extracts separated natural packets it enters the same critical norm.

Therefore `X` is a coarse scalar envelope for the newly unified throughput mechanism.

---

## 3. Standard critical Sobolev energy identity

Apply `Lambda^{1/2}` to Navier--Stokes and pair with `Lambda^{1/2}u`.

Define

\[
Y(t):=\|u(t)\|_{\dot H^{3/2}}^2.
\]

Then

\[
\boxed{
\frac12X'(t)
+\nu Y(t)
=
-\langle
\Lambda^{1/2}(u\cdot\nabla u),
\Lambda^{1/2}u
\rangle.
}
\]

The standard critical product estimate gives

\[
\boxed{
\left|
\langle
\Lambda^{1/2}(u\cdot\nabla u),
\Lambda^{1/2}u
\rangle
\right|
\le
C_{1/2}
X(t)^{1/2}Y(t).
}
\]

Therefore

\[
\boxed{
\frac12X'
+
\left(
\nu-C_{1/2}X^{1/2}
\right)Y
\le0.
}
\]

---

## 4. What the standard estimate closes

If

\[
X(t)^{1/2}
<
\frac\nu{C_{1/2}}
\]

throughout a time interval, then

\[
X'(t)\le0
\]

and the critical dissipation remains coercive.

This is the usual small-critical-data mechanism.

It is completely consistent with the M5-408 atom theorem: only finitely many order-one critical carrier atoms can fit below a sufficiently small critical norm.

---

## 5. What the standard estimate does not close

Once

\[
X^{1/2}
\ge
\frac\nu{C_{1/2}},
\]

the coefficient in front of `Y` loses sign.

The inequality then permits the nonlinear term to balance or exceed viscous critical dissipation.

Nothing in the bare estimate prevents

\[
X(t)\to\infty
\qquad(t\uparrow T_*).
\]

Therefore

\[
\boxed{
H_{throughput}^{crit}
\Longrightarrow
X\text{ large/divergent}
}
\]

is **not** a contradiction.

This is exactly the critical barrier expected in the 3D problem.

---

## 6. Relation to the L3 critical criterion

The Sobolev embedding gives

\[
\boxed{
\dot H^{1/2}
\hookrightarrow
L^3.
}
\]

Thus a uniform bound on `X(t)` up to the terminal time would place the solution in a standard scale-critical velocity class.

The repository's weak-L3/ancient Liouville work is consistent with the same principle: bounded critical velocity size is a rigid/regular corridor, while a hypothetical singular continuation must escape through critical-norm growth or loss of compactness.

M5-408--414 identify the **mechanisms** producing that escape, but they do not overturn the basic critical-norm dichotomy.

---

## 7. DSD audit: what has actually been gained

The reduction to `H_throughput^crit` is still meaningful.

Before the reduction, critical norm escalation could be attributed vaguely to many apparently independent mechanisms:

- local derivative H;
- material replacement;
- contact;
- remote satellites;
- ambient harmonic strain;
- projective rotation;
- export;
- detached affine limits;
- restart defects.

The later audits show that these are not independent ways around the critical barrier.

They all require repeated creation, redistribution, or loss of compactness of the same scale-critical source/carrier content.

Thus the novelty is **mechanistic classification and no-double-counting**, not a new a priori bound on `X`.

---

## 8. One natural event also has scale-critical H^{3/2} time cost

For orientation, consider a coherent natural packet of spatial scale `r` and velocity size `nu/r` persisting for a natural viscous time

\[
\Delta t\asymp\frac{r^2}{\nu}.
\]

Its `dot H^{3/2}` size scales as

\[
\|u\|_{\dot H^{3/2}}^2
\asymp
\frac{\nu^2}{r^2}.
\]

Hence

\[
\boxed{
\int_{I_{nat}}
\|u\|_{\dot H^{3/2}}^2dt
\asymp
\nu.
}
\]

Thus natural carrier formation has an order-one **critical Sobolev dissipation scale** as well as an order-one `dot H^{1/2}` atom scale.

But there is no Leray-level global bound on

\[
\int^{T_*}\|u\|_{\dot H^{3/2}}^2dt
\]

independent of the nonlinear critical production.

So this observation alone also does not close the tower.

---

## 9. Why another packing theorem alone is unlikely to be enough

M5-408 already provides phase-space Bessel packing without shrinking scale weight.

If infinitely many simultaneous separated carriers are formed, `X` must diverge.

But a singularity is allowed to have diverging `X`.

Therefore a further theorem of the form

\[
\text{more critical carriers}
\Longrightarrow
\text{larger critical norm}
\]

would improve quantification but would not by itself prove regularity.

A useful next theorem must compare **critical nonlinear production against critical dissipation or rigidity**, not merely count packets.

---

## 10. True target I — strict per-cluster nonlinear efficiency gap

The first-hitting analysis gives more structure than an arbitrary `dot H^{1/2}` field.

A coherent high-vorticity core cannot self-supply its required stretching if perfectly aligned; M5-362 forces a misaligned source network, and M5-394 forms a companion critical flux carrier on the natural-source branch.

Therefore a candidate theorem is a geometry-restricted sharpening of the standard critical product estimate:

\[
\boxed{
|\mathcal N_{1/2}|
\le
C_{eff}(\mathcal G)
X^{1/2}Y,
}
\]

where `mathcal G` records the first-hitting main/companion/source geometry.

A useful result would need a **strict efficiency loss** not available to arbitrary critical fields.

A fixed numerical improvement of `C_{1/2}` alone is not enough when `X->infinity`; the improvement must strengthen as throughput multiplicity/scale separation grows, or force another coercive channel.

---

## 11. True target II — critical-element rigidity

A second route is concentration compactness.

If global regularity fails, choose a sequence approaching minimal or recurrent critical-throughput behavior after quotienting by translations and scalings.

The desired rigidity statement would say that a critical element simultaneously satisfying

- first-hitting vorticity normalization;
- material-flux carrier formation;
- the angular source necessity;
- finite phase-memory exclusion;
- bounded-shell weak-critical compactness where applicable;

cannot remain nonzero for all backward times.

This would use substantially more information than the bare `dot H^{1/2}` norm.

---

## 12. True target III — novelty-to-dissipation nonreuse

A third route is to distinguish new carrier formation from persistence.

M5-408 counts simultaneous critical atoms, while M5-393--412 track material/flux ancestry.

A desired nonreuse theorem would have schematic form

\[
\boxed{
\text{fresh critical phase-space atom}
\Longrightarrow
\text{critical dissipative action not chargeable to old atoms}.
}
\]

If such actions were Bessel/Carleson orthogonal in space-time with a globally controlled source, repeated throughput could be excluded.

No such theorem is presently proved.

This is more precise than simply asking for another energy estimate.

---

## 13. Current master interpretation

The single frontier

\[
\boxed{H_{throughput}^{crit}}
\]

should now be read as

\[
\boxed{
\text{the solution must continually create or reorganize scale-critical source content fast enough to escape every bounded critical compactness corridor.}
}
\]

That is a strong structural statement.

But at the scalar norm level it is still compatible with

\[
\|u(t)\|_{\dot H^{1/2}}\to\infty,
\]

which is precisely what a hypothetical singularity is free to do.

---

## 14. Firewall against overclaim

Do not conclude

\[
\text{single remaining branch}
\Rightarrow
\text{proof nearly complete}.
\]

A single scale-critical branch can contain the full difficulty of the Clay problem.

Do not conclude

\[
\mathfrak N_{crit}\to\infty
\Rightarrow
\text{contradiction}.
\]

It currently implies only critical-norm escalation.

Do not use small-data `dot H^{1/2}` coercivity after the norm has crossed the critical threshold.

---

## 15. Audit verdict

### VERIFIED

- M5-408 critical carrier novelty is enveloped by the standard `dot H^{1/2}` velocity norm;
- the standard critical energy estimate closes only the small-critical-norm regime;
- the unified throughput branch is compatible with critical norm divergence;
- a natural packet has an order-one critical H3/2 time scale, but that spacetime norm is not a priori finite at blow-up.

### TRUE NEXT TARGET

One must exploit the extra first-hitting/source/material structure to obtain something **strictly stronger** than bare critical-norm escalation:

\[
\boxed{
\text{strict nonlinear efficiency gap}
\lor
\text{critical-element rigidity}
\lor
\text{novelty-to-dissipation nonreuse}.
}
\]

### CURRENT STATUS

\[
\boxed{
\text{GLOBAL REGULARITY REMAINS UNPROVED.}
}
\]