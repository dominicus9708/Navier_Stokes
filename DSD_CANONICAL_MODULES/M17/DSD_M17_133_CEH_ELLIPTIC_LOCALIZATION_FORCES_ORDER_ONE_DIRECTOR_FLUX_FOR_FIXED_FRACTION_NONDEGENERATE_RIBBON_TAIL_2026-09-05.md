# DSD M17-133 — CE-H elliptic localization forces an order-one director-flux floor for fixed-fraction nondegenerate ribbon tails

Date: 2026-09-05
Canonical ID: **M17-133**

Status: **NEW CE-H REALIZATION RIGIDITY / M17-129 IDENTIFIED `Phi_k~K_k^-1` AS THE SHARP SEQUENCE MODEL IF ONLY FLUX CAPTURE IS USED. THE FULL CE-H ELLIPTIC EQUATION `Delta W=kappa W` ADDS A LOCAL `L^2 -> L^infinity` RIGIDITY WHEN `kappa` IS UNIFORMLY BOUNDED ON FIXED-SIZE REMOTE CORES. IF A UNIFORMLY NONDEGENERATE COMPLETE RIBBON CARRIES A FIXED FRACTION OF THE AGE-k SHELL VORTICITY ENERGY, ITS MAXIMUM AMPLITUDE IS CONTROLLED BY THE TOTAL SHELL `L^2` MASS, WHILE ITS PER-FLUX ENSTROPHY IS CONTROLLED BY THAT MAXIMUM AMPLITUDE. CANCELLING THE SHELL ENERGY FORCES `Phi_k>=c>0`, INDEPENDENT OF k. THEREFORE THE `Phi_k~K_k^-1` MODEL CANNOT BE REALIZED BY A FIXED-FRACTION UNIFORMLY NONDEGENERATE COMPLETE-RIBBON FAMILY UNDER THE BOUNDED-POTENTIAL CE-H HYPOTHESIS. THE SURVIVING TAIL IS A LOW-AMPLITUDE BUT ORDER-ONE-DIRECTOR-FLUX SKELETON, OR IT MUST EXIT THROUGH DEGENERATION/BOUNDARY/SMALL MASS FRACTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Fixed-time CE-H elliptic equation

At each fixed similarity time,

\[
\boxed{
\Delta W=\kappa W.
}
\]

Assume on the relevant remote enlarged shells / fixed-size local ribbon cores

\[
\boxed{
\|\kappa\|_{L^\infty}\le K_0
}
\]

with `K_0` independent of the remote shell index.

For any unit ball `B_1(x)` contained in the enlarged shell, standard interior elliptic estimates for the bounded-potential Schrödinger equation give

\[
\boxed{
\|W\|_{L^\infty(B_{1/2}(x))}^2
\le
C_E(K_0)
\int_{B_1(x)}|W|^2dy.
}
\]

The same conclusion holds with any fixed local radius after adjusting the constant.

---

## 2. Shell amplitude controlled by shell enstrophy

Let

\[
E_k^\omega
:=
\int_{A_k^*}|W|^2dy
\]

on an enlarged remote annulus `A_k^*` containing the ribbon local cores with bounded overlap.
Define

\[
\boxed{
a_k:=\sup_{\mathcal T_k}\rho
=\sup_{\mathcal T_k}|W|.}
\]

Cover the fixed-size ribbon core by finitely many interior balls. Section 1 gives

\[
\boxed{
a_k^2\le C_EE_k^\omega.}
\]

In the M5 weighted notation,

\[
J_k^\omega=K_kE_k^\omega,
\]

so

\[
\boxed{
a_k^2\le C_E\frac{J_k^\omega}{K_k}.}
\]

Thus the remote tail amplitude must decay whenever the unweighted shell enstrophy decays.

---

## 3. Per-flux enstrophy upper bound

On a uniformly nondegenerate complete-ribbon class assume

\[
|J_\xi|\ge c_J>0
\]

and, by bounded-core containment M17-124,

\[
L_\lambda\le L_+<\infty.
\]

M17-122 gives

\[
\mathcal W_J(\lambda)
=\oint_{\Gamma_\lambda}
\frac{\rho^2}{|J_\xi|}ds.
\]

Therefore

\[
\boxed{
\mathcal W_J(\lambda)
\le
\frac{L_+}{c_J}a_k^2.
}
\]

For total ribbon flux `Phi_k`,

\[
\boxed{
E_{k,rib}^\omega
\le
\frac{L_+}{c_J}a_k^2\Phi_k.
}
\]

---

## 4. Fixed shell-mass fraction forces a flux floor

Assume the selected ribbon family carries a fixed fraction `theta>0` of the shell vorticity energy:

\[
\boxed{
E_{k,rib}^\omega
\ge
\vartheta E_k^\omega.
}
\]

Using Sections 2 and 3,

\[
\vartheta E_k^\omega
\le
\frac{L_+}{c_J}C_EE_k^\omega\Phi_k.
\]

For every shell with `E_k^omega>0`, cancel the common factor to obtain

\[
\boxed{
\Phi_k
\ge
\frac{\vartheta c_J}{C_EL_+}
=:c_\Phi>0.
}
\]

The lower bound is independent of `k`.

---

## 5. Consequence for the M17-129 K^-1 model

M17-129 showed that, absent additional PDE localization, the sequence

\[
\Phi_k\sim K_k^{-1}
\]

is the sharp flux scaling compatible with

\[
J_{k,rib}^\omega\sim1.
\]

M17-133 shows that this scaling cannot occur if all of the following hold uniformly:

1. bounded CE-H potential `|kappa|<=K_0` on fixed-size local cores;
2. complete ribbon geometry with `|J_xi|>=c_J` and bounded loop length;
3. the ribbon carries a fixed positive fraction of the shell enstrophy.

Under these hypotheses,

\[
\boxed{\Phi_k\ge c_\Phi>0}
\]

instead of `Phi_k~K_k^-1`.

---

## 6. The surviving low-amplitude skeleton

Since

\[
E_k^\omega=J_k^\omega/K_k
\]

and the ancient tail has finite unweighted enstrophy, remote shell energies tend to zero along the tail.
Section 2 forces

\[
\boxed{a_k\to0}
\]

on such fixed-size cores.

Therefore a nondegenerate fixed-fraction ribbon survivor has the asymptotic structure

\[
\boxed{
\rho_k\to0,
\qquad
|J_\xi|\ge c_J,
\qquad
\Phi_k\ge c_\Phi.
}
\]

The vorticity amplitude vanishes while the director-area geometry remains order one.

This is a **low-amplitude / strong-direction skeleton**. The weighted-harmonic director energy becomes cheap because its weight `rho^2` degenerates, even though the unweighted director Jacobian does not.

---

## 7. Alternative exits

If the order-one flux floor is not observed, at least one hypothesis of Section 5 must fail:

\[
\boxed{
\begin{aligned}
&|J_\xi|\to0
&&\text{(Rank-1/rank-deficient accumulation)},\\
&L_\lambda\to\infty
&&\text{(boundary/ribbon-cover exit)},\\
&\|\kappa\|_{L^\infty}\to\infty
&&\text{(loss of compact CE-H potential control)},\\
&\frac{E_{k,rib}^\omega}{E_k^\omega}\to0
&&\text{(ribbon carries vanishing shell fraction)}.
\end{aligned}
}
\]

Thus the realization problem is now a finite explicit branch split.

---

## 8. Relation to palinstrophy

The low-amplitude skeleton does not immediately contradict M17-131.
Indeed

\[
2\rho^2|J_\xi|
\le|\nabla W|^2
\]

and `rho^2` itself tends to zero.
An order-one director-area flux can therefore have a summably small weighted/palinstrophy cost if the vorticity amplitude decays at the critical rate.

Hence the new flux floor is a geometric complexity statement, not yet an energetic contradiction.

---

## 9. DSD audit

### Audit A — using a generic Sobolev pointwise estimate

The key estimate comes from the actual CE-H elliptic equation with bounded potential, not from `H^1 -> L^infinity`, which is false in three dimensions.

### Audit B — shell boundary effects

Use an enlarged annulus and fixed-size interior balls. Finite enlargement does not alter the M5 cubic-stack classification.

### Audit C — fixed ribbon fraction assumed silently

Not silent. The order-one flux floor applies only to a ribbon branch carrying a fixed positive fraction of the shell vorticity energy. Vanishing ribbon fraction remains an explicit exit.

### Audit D — order-one flux contradicts finite energy

Rejected. Director-area flux is unweighted geometry and can remain order one while `rho -> 0` makes all ordinary vorticity energy costs small.

### Audit E — proof status

The `K^-1` nondegenerate fixed-fraction realization is excluded, but the low-amplitude order-one-flux skeleton remains open.

---

## 10. Updated compact-ribbon realization frontier

For fixed-fraction remote ribbon tails under bounded CE-H potential and bounded complete-loop geometry,

\[
\boxed{
R_{ribbon}^{critical}
\Longrightarrow
S_{low\ amplitude}^{\Phi\ge c}
\ \lor\
A_{R1}
\ \lor\
T_{boundary}
\ \lor\
U_{\kappa\text{-unbounded}}
\ \lor\
V_{ribbon\ fraction\to0}.
}
\]

The highest-value next calculation is now the first branch:

\[
\boxed{
\rho_k\to0,
\qquad
|J_\xi|\gtrsim1,
\qquad
\Phi_k\gtrsim1.
}
\]

Test whether the exact CE-H identities permit order-one unweighted director geometry to survive indefinitely as the amplitude weight `rho^2` vanishes, or whether analyticity/Schrodinger unique continuation forces the director geometry to collapse with amplitude.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
