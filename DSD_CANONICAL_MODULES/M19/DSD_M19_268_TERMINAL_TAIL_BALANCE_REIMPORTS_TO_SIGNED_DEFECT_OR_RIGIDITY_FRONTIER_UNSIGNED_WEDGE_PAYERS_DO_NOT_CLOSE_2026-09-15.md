# DSD M19-268 — Terminal-tail balance reimports to a signed-defect or rigidity frontier; unsigned wedge payers do not close the proof

Date: 2026-09-15  
Canonical ID: **M19-268**  
Status: **ACTIVE MASTER REIMPORT / M5-582--598 SYNTHESIS / UNSIGNED TAIL-BALANCE CLOSURE RETIRED / SIGNED DEFECT OR RIGIDITY FRONTIER PROMOTED / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-266 reduced the surviving low-frequency hard branch to a positive-density terminal scattering process rather than a decaying tail.

M19-267 strengthened the terminal energy ledger to the quantitative dichotomy

\[
\boxed{
\langle\Phi_E\rangle
\ge \frac{c_3}{2M_A}
}
\]

or

\[
\boxed{
\left\langle\int_{S^2}A\cdot C\,d\omega\right\rangle
\ge \frac{c_3}{2M_A}.
}
\]

It is therefore natural to ask whether the exact PDE balance itself now closes the hard tail.

The historical M5-582--598 chain already developed precisely this question through the full scale-invariant parabolic wedge, finite-depth enstrophy production, and same-event charge accounting.

The present module reimports that chain under the corrected M19 physical-scale interpretation.

---

## 2. Exact wedge rather than terminal-only dynamics

Introduce

\[
q=\log r,
\qquad
z=\frac{-s}{r^2},
\qquad
u(x,s)=r^{-1}F(z,q,\omega),
\qquad
p(x,s)=r^{-2}H(z,q,\omega).
\]

The coordinate \(z\) is exactly invariant under Navier--Stokes scaling, while scaling acts by translation in \(q\).

The terminal boundary is

\[
\boxed{F(0,q,\omega)=A(q,\omega),}
\]

and

\[
\boxed{\partial_zF(0,q,\omega)=C(q,\omega).}
\]

Thus the terminal pair \((A,C)\) is only the boundary jet of a full wedge field.

The exact transformed Navier--Stokes equation is the degenerate mixed equation

\[
\boxed{
\partial_zF
=
-\mathfrak L_1F
+\mathfrak N(F,F)
+\mathfrak G_2H.
}
\]

Therefore any terminal payer must be audited against transport through positive wedge depth before it can be called contradictory.

---

## 3. Exact q-averaged wedge energy transport

Let

\[
\mathscr E(z)
:=
\left\langle
\int_{S^2}\frac12|F|^2d\omega
\right\rangle_q,
\]

\[
\mathscr J(z)
:=
\left\langle
\int_{S^2}\mathcal J_r\,d\omega
\right\rangle_q,
\]

and

\[
\mathscr D(z)
:=
\left\langle
\int_{S^2}\mathcal D_F\,d\omega
\right\rangle_q
\ge0.
\]

M5-583 gives the exact one-dimensional balance

\[
\boxed{
\mathscr E'(z)
+2z\mathscr J'(z)
+\mathscr J(z)
=
\mathscr D(z).
}
\]

At the terminal boundary,

\[
\boxed{
\mathscr E'(0)
=
\left\langle\int_{S^2}A\cdot C\,d\omega\right\rangle,
}
\]

\[
\boxed{
\mathscr J(0)=\langle\Phi_E\rangle,
}
\]

and

\[
\boxed{
\mathscr D(0)=\langle\mathcal D_A\rangle.
}
\]

Hence the M19-267 payer dichotomy is exactly the \(z=0\) boundary decomposition of the full wedge energy transport law.

It is not an independent terminal-only source law.

---

## 4. Terminal energy-flux branch is not scale contradictory

On the stationary terminal branch \(C=0\), M5-578 gives

\[
\Phi_E(q)>0
\qquad\forall q
\]

for every nontrivial recurrent stationary terminal profile.

M19-267 adds the quantitative mean lower bound

\[
\langle\Phi_E\rangle
\ge
\frac{c_3}{M_A}.
\]

However M5-579 audits this against the natural Type-I shrinking core.

At

\[
R(s)=L\sqrt{-s},
\]

the physical terminal energy current has order

\[
\frac{1}{R(s)}\Phi_E
\asymp
(-s)^{-1/2},
\]

which is exactly the same order as

- the core kinetic-energy change rate;
- the viscous dissipation in the shrinking core;
- the moving-boundary work term.

Therefore

\[
\boxed{
\text{positive terminal energy flux}
\not\Rightarrow
\text{Type-I scaling contradiction}.
}
\]

The flux branch can close only if one proves a true **terminal local-energy defect exclusion or structure theorem** inherited from the original unforced solution.

Define

\[
\boxed{
\mathcal T_{tail}^{energy-defect}:
\text{the original solution cannot generate the required nonzero terminal critical energy-current defect.}
}
\]

This theorem is not currently available in the DSD package.

---

## 5. Residual-correlation branch is transported into the wedge

On the M19-267 residual branch,

\[
\boxed{
\mathscr E'(0)
\ge
\frac{c_3}{2M_A}>0.
}
\]

Thus the q-averaged scale-normalized wedge energy initially increases as one moves away from the terminal boundary into \(z>0\).

But this is allowed by the exact wedge balance because

\[
\mathscr E'
=
\mathscr D-\mathscr J-2z\mathscr J'.
\]

There is no inherited sign for the radial flux field \(\mathscr J\) or its derivative at finite depth.

The positive boundary derivative therefore forces finite-depth transport, not a contradiction.

M5-580 further shows that on a genuinely dynamic ergodic terminal component

\[
\boxed{
\left\langle\int_{S^2}|C|^2d\omega\right\rangle
=c_C>0,
}
\]

while M5-574/M5-584 give zero mean for the net-force projection of \(C\).

Hence the dynamic payer is necessarily fluctuating/projective rather than a persistent one-sign force.

---

## 6. Enstrophy transport forces a finite-depth production shell

M5-585 derives the q-averaged wedge enstrophy law

\[
\boxed{
\mathscr K_\omega'
+2z\mathscr J_\omega'
+3\mathscr J_\omega
=
\mathscr P_\omega-\mathscr Q_\omega,
}
\]

where

\[
\mathscr P_\omega\ge0
\]

is vorticity-gradient dissipation and \(\mathscr Q_\omega\) is stretching production.

M5-586 shows that the positive terminal vorticity density does **not** create an extra \(z=0\) defect: the leading Hardy boundary terms cancel exactly.

M5-587 then uses the finite-depth boundary functional

\[
\mathscr Y_\omega(z)
=
\frac12z^{1/2}\mathscr K_\omega(z)
+z^{3/2}\mathscr J_\omega(z)
\]

to force an interior maximum at some

\[
\boxed{z_*\in(0,\infty).}
\]

At that depth,

\[
\boxed{
\mathscr Q_\omega(z_*)
-
\mathscr P_\omega(z_*)
=
\frac{\mathscr K_\omega(z_*)}{2z_*}
>0.
}
\]

Thus the positive terminal hard tail necessarily feeds a genuine finite-depth stretching surplus.

This is a strong structural theorem, but it is still an **unsigned positive production event**.

---

## 7. Finite-depth production splits into positive local charges

M5-588 decomposes

\[
W=\rho\xi
\]

and

\[
|\nabla W|^2
=
|\nabla\rho|^2
+
\rho^2|\nabla\xi|^2.
\]

At the forced finite-depth shell,

\[
\boxed{
\left\langle
\int
\rho^2\left(\sigma-\frac14\right)dS
\right\rangle
=
P_{mag,*}+P_{dir,*}.
}
\]

Hence, unless the full gradient charge vanishes, at least one of

\[
P_{mag,*}>0
\]

or

\[
P_{dir,*}>0
\]

is quantitatively active.

The later M5-589--597 chain further refines the surviving branches into explicit positive local payers and rigid CE-H-type alternatives.

However this refinement does not change the physical accumulation question.

---

## 8. M5-598 accumulation firewall remains decisive

M5-598 audits the complete same-event payer menu and returns it to physical variables.

A fixed positive normalized event charge at geometric similarity generations does not cost a fixed positive amount of physical energy.

For a Type-I event at physical scale parameter

\[
a_j=-s_j,
\]

a fixed normalized dissipation event costs physical kinetic energy of order

\[
\boxed{a_j^{1/2}.}
\]

On a geometric first-hitting tower,

\[
a_j\asymp q^{-j},
\]

so

\[
\boxed{
\sum_j a_j^{1/2}<\infty.
}
\]

Therefore infinitely many positive normalized tail/wedge production payments are compatible with the finite physical energy inequality.

The same conceptual firewall applies to the M19-267 quantitative payer floor: a fixed scale-invariant normalized payment does not by itself produce a nonsummable original-variable cost.

Hence

\[
\boxed{
\mathcal T_{tail}^{balance}
\text{ as a purely unsigned payer mechanism does not close.}
}
\]

---

## 9. Correct terminal-tail closure taxonomy

The tail route now has only three legitimate closure types.

### A. Signed defect exclusion

Prove that a bounded original-variable or scale-invariant state observable cannot support the required terminal defect/current.

Representative target:

\[
\boxed{
\mathcal T_{tail}^{energy-defect}.
}
\]

### B. Monotone or signed recurrent drift

Construct a bounded observable \(\mathcal O\) for which

\[
\boxed{
\langle D\mathcal O\rangle
\text{ has a strict one-way sign}
}
\]

on every nontrivial hard component, with no compensating channel of equal critical order.

This is the same structural requirement as the active

\[
\boxed{\mathcal T_{aper}^{signed}.}
\]

### C. Rigidity / exact incompatibility

Use the full wedge PDE, compactness, or the finite-depth production geometry to force

- a Liouville contradiction;
- an impossible exact PDE constraint;
- or a terminal defect forbidden by an independent theorem.

Call this

\[
\boxed{\mathcal T_{tail}^{rigidity}.}
\]

---

## 10. Merger with the current M19 hard core

The R-critical / low-frequency tail route is therefore **not** an independent fourth closure mechanism based on accumulating positive fluxes.

It reduces to

\[
\boxed{
\mathcal T_{tail}^{energy-defect}
\lor
\mathcal T_{aper}^{signed}
\lor
\mathcal T_{tail}^{rigidity}.
}
\]

This is consistent with the M5-598 master conclusion that a terminal proof must use at least one of:

1. scale-invariant signed drift of a bounded observable;
2. monotone critical quantity;
3. compactness/Liouville obstruction;
4. finite new-label/replacement count;
5. exact PDE incompatibility.

The current terminal-tail calculations have not yet supplied one of these in a closed form.

---

## 11. Consequence for the GMS/base-gain route

M19-261 showed that the ancestral raw-H2 resource lacks the physical fine-scale factor required for direct H3/GMS closure.

M19-266--268 now show that the alternative low-frequency terminal-tail route also does not bypass that gap by simple positive payer accumulation.

Thus the two apparently different hard mechanisms meet at the same structural frontier:

\[
\boxed{
\text{a true signed/monotone/rigidity theorem is still required.}
}
\]

This does not invalidate the GMS endpoint or the wedge identities. It identifies exactly why neither is currently a complete proof.

---

## 12. Permanent firewalls after M19-268

\[
\boxed{
\text{positive terminal cubic density}
\not\Rightarrow
\text{physical energy contradiction},
}
\]

\[
\boxed{
\text{positive terminal dissipation floor}
\not\Rightarrow
\text{nonsummable original-variable cost},
}
\]

\[
\boxed{
\text{positive radial energy flux}
\not\Rightarrow
\text{Type-I scaling contradiction},
}
\]

\[
\boxed{
\text{positive }\langle A\cdot C\rangle
\not\Rightarrow
\text{terminal contradiction without finite-depth transport control},
}
\]

\[
\boxed{
\text{finite-depth stretching surplus}
\not\Rightarrow
\text{global contradiction by unsigned accumulation},
}
\]

\[
\boxed{
\text{tail balance route}
\not\Rightarrow
\text{closure unless promoted to signed defect, monotonicity, or rigidity}.
}
\]

---

## 13. Immediate next target

The most informative next calculation is to use the **signed** boundary condition found in M19-267,

\[
\mathscr E'(0)>0
\]

on the residual payer branch, together with the deep-wedge decay

\[
\mathscr E(z)\to0
\qquad(z\to\infty),
\]

to force an interior extremum of \(\mathscr E\), and then audit the exact wedge energy ODE at that extremum.

The goal is not to produce another positive unsigned payer, but to test whether the extremum converts the residual branch into a signed flux constraint or a true finite-depth rigidity condition.

If it again reduces to a freely signed flux derivative, record that as a no-go and return the active frontier to \(\mathcal T_{aper}^{signed}\) / terminal-defect / rigidity.

Global 3D Navier--Stokes regularity remains unproved.
