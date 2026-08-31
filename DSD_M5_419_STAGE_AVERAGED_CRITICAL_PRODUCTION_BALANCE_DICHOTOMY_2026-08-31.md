# DSD M5-419 — Stage-averaged critical production balance dichotomy

Date: 2026-08-31

Status: **M5-418 GIVES A FIXED POSITIVE CRITICAL `dot H^{3/2}` TIME CHARGE ON EVERY LATE NATURAL DUAL-CLUSTER STAGE OUTSIDE THE ALREADY-TYPED STRAIN-THROUGHPUT EXIT / INSERTING THIS INTO THE EXACT `dot H^{1/2}` ENERGY IDENTITY SHOWS THAT AN INFINITE FIRST-HITTING TOWER MUST EITHER ACCUMULATE CRITICAL `dot H^{1/2}` MASS AT A NONNEGLIGIBLE RATE OR HAVE LONG-BLOCK NONLINEAR PRODUCTION ASYMPTOTICALLY BALANCE THE VISCOUS CRITICAL DISSIPATION / THIS REPLACES THE VAGUE `LARGE CRITICAL NORM` FRONTIER BY `CRITICAL MASS ACCUMULATION OR NEAR-BALANCED RECURRENT CRITICAL ELEMENT` / NEITHER BRANCH IS YET EXCLUDED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-415 shows that merely routing the proof tree to critical throughput does not beat the classical `dot H^{1/2}` barrier.

M5-418 adds genuinely dynamical information: outside a large local-strain exit, every natural main/companion source event persists for a fixed positive fraction of one natural time and therefore carries a fixed positive critical `dot H^{3/2}` time charge.

The present note inserts that charge into the exact critical Sobolev energy identity and derives a block-level dichotomy.

---

## 2. Critical quantities

For the smooth preterminal solution define

\[
\boxed{
X(t):=\|u(t)\|_{\dot H^{1/2}}^2
}
\]

and

\[
\boxed{
Y(t):=\|u(t)\|_{\dot H^{3/2}}^2.
}
\]

Let the exact critical nonlinear production be

\[
\boxed{
\mathcal N(t)
:=-\left\langle
\Lambda^{1/2}(u\cdot\nabla u),
\Lambda^{1/2}u
\right\rangle.
}
\]

For smooth times,

\[
\boxed{
\frac12X'(t)+\nu Y(t)=\mathcal N(t).
}
\]

No product-estimate upper bound is used in the present derivation.

---

## 3. Stage quantities

On the `j`-th first-hitting interval

\[
I_j=[t_j,t_{j+1}],
\]

define

\[
\boxed{
D_j:=\int_{I_j}Y(t)dt
}
\]

and

\[
\boxed{
P_j:=\int_{I_j}\mathcal N(t)dt.
}
\]

The exact stage identity is

\[
\boxed{
P_j
=
\nu D_j
+
\frac12\bigl(X_{j+1}-X_j\bigr),
}
\]

where

\[
X_j:=X(t_j).
\]

---

## 4. M5-418 supplies a positive stage charge

On the natural-source local corridor, M5-418 gives a main/companion packet persisting for a fixed normalized time and hence a critical dissipative lower bound

\[
\boxed{
D_j\ge d_*>0
}
\]

with `d_*` depending only on the retained first-hitting/analyticity/compact-cluster constants, after fixing the viscosity convention.

If the hypotheses needed for this persistence fail through large local strain/full-gradient action, the stage has already entered `H_throughput^crit` in the strong strain form and is not a quiet counterexample to the present reduction.

Thus an eventual local natural-cluster tower has a uniform positive `D_j` floor.

---

## 5. Block identity

For a block of stages `j=J,...,K-1`, set

\[
D_{J,K}:=\sum_{j=J}^{K-1}D_j,
\qquad
P_{J,K}:=\sum_{j=J}^{K-1}P_j.
\]

Telescoping gives

\[
\boxed{
P_{J,K}
=
\nu D_{J,K}
+
\frac12(X_K-X_J).
}
\]

Since

\[
D_{J,K}
\ge
d_*(K-J),
\]

the block contains a linearly growing amount of critical dissipative action.

---

## 6. Define the actual production efficiency

Whenever `D_{J,K}>0`, define

\[
\boxed{
\eta_{J,K}
:=
\frac{P_{J,K}}{\nu D_{J,K}}.
}
\]

The exact identity yields

\[
\boxed{
\eta_{J,K}
=
1+
\frac{X_K-X_J}{2\nu D_{J,K}}.
}
\]

This is an identity for the actual nonlinear production, not the constant in a Sobolev product estimate.

---

## 7. Sublinear critical-mass growth forces near balance

Suppose along arbitrarily long late blocks

\[
\frac{|X_K-X_J|}{K-J}\to0.
\]

Because

\[
D_{J,K}\ge d_*(K-J),
\]

we obtain

\[
\boxed{
\eta_{J,K}\to1.
}
\]

Thus if critical `dot H^{1/2}` mass does not accumulate at a positive rate per first-hitting generation, the actual nonlinear production must asymptotically balance the viscous critical dissipation on long blocks.

This is substantially sharper than saying only that the critical norm is large.

---

## 8. Complement: nonnegligible critical-mass accumulation

If the preceding sublinear alternative fails, then there exist late blocks on which

\[
\boxed{
X_K-X_J
\gtrsim
c_X(K-J)
}
\]

for some positive rate along a subsequence, or stronger superlinear accumulation occurs.

This defines the first survivor:

\[
\boxed{
C_{mass\,accum}:
\quad
\text{critical }\dot H^{1/2}\text{ mass grows at nonnegligible generation rate.}
}
\]

M5-408 interprets part of this growth as increasing phase-space carrier novelty when the mass separates into formed atoms.

If the growth instead remains concentrated in one bounded phase-space cluster, it is a critical-element concentration problem rather than a many-atom packing problem.

---

## 9. Second survivor: near-balanced recurrent critical dynamics

The complementary survivor is

\[
\boxed{
C_{bal}:
\quad
\eta_{J,K}\to1
}
\]

on long late blocks while the tower continues to hit geometrically increasing vorticity levels.

This means

\[
\boxed{
\int\mathcal N
\sim
\nu\int Y
}
\]

at the block level: nonlinear critical production replenishes almost exactly the critical dissipation required by the persistent natural source geometry.

This is the natural candidate for a recurrent/minimal critical element.

---

## 10. A one-sided efficiency deficit cannot persist

Suppose for some fixed `epsilon>0` one had on every sufficiently late stage

\[
P_j
\le
(1-\epsilon)\nu D_j.
\]

Then

\[
X_{j+1}-X_j
\le
-2\epsilon\nu D_j
\le
-2\epsilon\nu d_*.
\]

Summing would force `X_j` negative after finitely many stages, impossible.

Therefore

\[
\boxed{
\text{an infinite natural-cluster tower cannot have a uniform actual production deficit below viscosity.}
}
\]

This is an exact consequence of M5-418 plus the critical energy identity.

It does not prove that a deficit exists; M5-417 explicitly warns that one-snapshot geometry alone does not give it.

---

## 11. A uniform supercritical excess produces mass accumulation

Conversely, if

\[
P_j
\ge
(1+\epsilon)\nu D_j
\]

on a positive lower density of late stages, then

\[
X_{j+1}-X_j
\ge
2\epsilon\nu d_*
\]

on those stages.

Thus persistent supercritical production efficiency automatically enters `C_mass_accum`.

Hence the only way to avoid explicit linear critical-mass growth is for the weighted long-block efficiency to approach the threshold `1`.

---

## 12. Relation to bounded critical norm regularity

A truly bounded `X(t)` corridor would have

\[
X_K-X_J=O(1)
\]

on arbitrarily long blocks and therefore

\[
\eta_{J,K}\to1.
\]

But bounded `dot H^{1/2}` implies bounded `L^3` by Sobolev embedding and therefore lies in the standard critical regularity corridor.

Thus a hypothetical singular tower cannot remain in a bounded critical-mass recurrent state.

The near-balanced branch must still have `X(t)` unbounded, but its growth is slow relative to cumulative critical dissipation along the selected blocks.

---

## 13. Updated hard-core split

The single M5-415 throughput frontier can now be refined dynamically as

\[
\boxed{
H_{throughput}^{crit}
\Longrightarrow
C_{mass\,accum}
\lor
C_{bal}
\lor
H_{strong\,strain/interface},
}
\]

where the last term collects stages that leave the M5-418 persistent local-cluster corridor through already typed strong strain/remote/interface action.

After M5-416, near-efficient formed source geometry itself localizes to the natural main/companion phase-space window.

Thus `C_bal` is a compact natural-cluster recurrent-element problem, not a generic remote-source problem.

---

## 14. What must be proved next

### Against `C_mass_accum`

Distinguish:

1. many Bessel-separated critical atoms;
2. growth of one/few interacting critical clusters;
3. diffuse phase-space critical mass.

The first is quantified by M5-408, the third by the shell/frequency ledgers, and the second is the likely critical-element lane.

### Against `C_bal`

Classify near-equality/recurrent solutions satisfying simultaneously:

- first-hitting normalization;
- persistent main/companion natural carriers;
- angular source necessity;
- material genealogy;
- actual critical production/dissipation balance.

This is more specific than trying to classify all ancient Navier--Stokes solutions.

---

## 15. Firewall

The block balance identity is not a regularity proof.

`C_mass_accum` is compatible with a singular critical norm.

`C_bal` is also not impossible by algebra alone; it is a nonlinear recurrent-element condition that still requires rigidity.

No sharp product-estimate constant or unproved sign assumption is used.

---

## 16. Audit verdict

### DERIVED

\[
\boxed{
\eta_{J,K}
=
1+
\frac{X_K-X_J}{2\nu D_{J,K}},
\qquad
D_{J,K}\ge d_*(K-J).
}
\]

Hence an infinite tower requires

\[
\boxed{
\text{nonnegligible critical-mass accumulation}
\quad\lor\quad
\text{asymptotic production/dissipation balance}.
}
\]

### TRUE NEXT TARGET

A rigidity theorem for the near-balanced natural main/companion critical element, together with a concentration classification for critical-mass accumulation.

### CURRENT STATUS

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
