# DSD M17-183 — M5 high-amplitude flux labels and vertical nodal cores are disjoint material strata; the direct same-label bridge is retracted

Date: 2026-09-06  
Canonical ID: **M17-183**

Status: **STRONG CORRECTIVE AUDIT / M5-681'S DIRECTED `kappa`-SPACE CURRENT IS DEFINED ON A RETAINED HIGH-AMPLITUDE, POSITIVE-VORTICITY MATERIAL VORTEX-LINE ENSEMBLE. THE VERTICAL M17-090 OCTUPOLE LIVES ON A NODAL FILAMENT WITH `rho=|W|=0`. CE-H GIVES THE HOMOGENEOUS MATERIAL LAW `D_B rho=(sigma+kappa-1)rho`, SO `rho>0` AND `rho=0` ARE DISJOINT MATERIAL-INVARIANT STRATA ON EVERY FINITE REGULAR INTERVAL. THEREFORE NO M5 HIGH-AMPLITUDE MATERIAL LABEL CAN EVOLVE INTO, OR BE IDENTIFIED AS, THE VERTICAL NODAL CORE. M17-095'S LABEL-BY-LABEL SUBSTITUTION CANNOT BE REPAIRED BY A SAME-MATERIAL GENEALOGY THEOREM; IT MUST BE RETRACTED IN THAT INTERPRETATION. ANY VALID M5-TO-NODAL BRIDGE MUST INSTEAD BE AN EULERIAN/SPATIAL ASSOCIATION BETWEEN REGULAR POSITIVE-VORTICITY LABELS AND A NEIGHBORING NODAL CORE, WITH AN EXPLICIT LOCALIZATION/TRACE/COVARIANCE THEOREM. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. M5 current support

M5-681 works on one finite retained material vortex-line flux ensemble.

Its labels satisfy

\[
\boxed{\rho=|W|>0}
\]

and, on the retained high-amplitude/finite-core part used to obtain compact `kappa` support, the amplitude is bounded below away from zero after restriction.

The current

\[
G(k,\theta)
=\int h_\lambda\delta(k-\kappa_\lambda)d\mu_\theta
\]

is therefore a current of **regular positive-vorticity material labels**.

---

## 2. Vertical nodal support

M17-090 is evaluated on a vertical nodal filament where

\[
\boxed{W=0}
\]

and hence

\[
\boxed{\rho=0.}
\]

Its local octupole

\[
O_V=-\frac15|Q|_F^2\kappa_3
\]

at a regular nodal `kappa=0` crossing is a descriptor of this zero-vorticity material stratum.

---

## 3. CE-H preserves the amplitude strata

The CE-H material amplitude law is

\[
\boxed{
D_B\rho
=(\sigma+\kappa-1)\rho.
}
\]

Along a regular material trajectory,

\[
\boxed{
\rho(\theta)
=\rho(\theta_0)
\exp\int_{\theta_0}^{\theta}
(\sigma+\kappa-1)d\tau.
}
\]

Therefore, for every finite regular time interval,

\[
\boxed{
\rho(\theta_0)>0
\Longrightarrow
\rho(\theta)>0,
}
\]

and

\[
\boxed{
\rho(\theta_0)=0
\Longrightarrow
\rho(\theta)=0.
}
\]

Thus

\[
\boxed{
\{\rho>0\}
\quad\text{and}\quad
\{\rho=0\}
}
\]

are disjoint material-invariant strata.

---

## 4. Consequence for M17-095

M17-095 used the M5 material-label integral and substituted the nodal identity

\[
h=-\frac{5r_V}{|Q|_F^2}O_V.
\]

But the `h` on the left of the M5 integral belongs to a regular positive-vorticity material label, whereas the `h`, `r_V`, and `O_V` on the right belong to a nodal zero-vorticity material trajectory.

Because Sections 1--3 show that these strata do not convert materially, there is no same-label interpretation under which this substitution is valid.

Therefore the direct material statement

\[
\boxed{
G_\Phi(0)
=-5\int
 a\frac{r_VO_V}{|Q|_F^2}
\delta(\kappa)d\mu_0
}
\]

is **retracted as an unconditional M5 identity**.

---

## 5. What kind of bridge is still possible

A regular positive-vorticity label may be spatially close to a nodal filament at the same time.

Thus one may still seek an Eulerian association

\[
\boxed{
\text{regular vortex-line packet}
\longleftrightarrow
\text{neighboring nodal core geometry}
}
\]

through, for example,

1. nested winding level sets around the nodal core;
2. a nearest/associated nodal critical point map inside a controlled Morse neighborhood;
3. localization of the regular `kappa=0` current to shrinking `q`-flux annuli around the nodal critical level;
4. an Eulerian covariance theorem relating regular crossing data to nodal pressure/octet data.

But such a map is not material and must explicitly control its Jacobian, multiplicity, and sign transfer.

---

## 6. Valid results retained

This correction does **not** affect:

- the vertical nodal geometry itself;
- the local octupole formula M17-090;
- the global pressure lock M17-082;
- the local-to-global pressure-production localization M17-164;
- the radial scale current and palinstrophy identities M17-166--171;
- the adapted regular M5 flux chart M17-179;
- the regular crossing octupole firewall M17-181.

It affects only claims that identify the M5 high-amplitude material current directly with nodal-core quantities.

---

## 7. Updated vertical Rank-1 split

The correct split is now

\[
\boxed{
R_{1,V}
\Longrightarrow
R_{V}^{regular\ M5\ conveyor}
\quad\oplus\quad
R_{V}^{nodal\ pressure/octet}
}
\]

with no material conversion between the two strata.

A proof must either

\[
\boxed{
\text{close the regular M5 conveyor directly}
}
\]

or establish a new **Eulerian spatial coupling theorem** between the two blocks.

---

## 8. DSD audit

### Audit A — same-material nodal conversion
Impossible on a finite regular interval by the homogeneous amplitude law.

### Audit B — high-amplitude versus nodal support
They are disjoint by construction.

### Audit C — deleting all nodal pressure work
Rejected. Those results remain valid and may still couple spatially/nonlocally to the regular population.

### Audit D — proof status
The correction removes an invalid bridge but leaves two sharply defined Rank-1 blocks.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
