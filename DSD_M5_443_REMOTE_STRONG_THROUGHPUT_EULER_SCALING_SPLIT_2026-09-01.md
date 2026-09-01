# DSD M5-443 — Strong remote throughput as an Euler-scaling Type-II compactness split

Date: 2026-09-01

Status: **THE STRONG REMOTE PAYER OF M5-440--442 HAS A CANONICAL SOURCE-SCALE EULER NORMALIZATION / WITH LENGTH `R=Kr` AND VELOCITY `U_E=nu K^2/R=nu R/r^2`, THE NAVIER--STOKES VISCOSITY BECOMES EXACTLY `K^-2`, THE FIRST-HITTING VORTICITY CAP BECOMES ORDER ONE, AND THE SOURCE OSCILLATION HAS A FIXED NONZERO NORMALIZED L2 LOWER BOUND / HENCE `K->infinity` SPLITS INTO AN EULER-COMPACT TYPE-II BRANCH OR A STRONGER SOURCE-SCALE NONCOMPACT DERIVATIVE/PRESSURE/AMPLITUDE BRANCH / THIS IS STRUCTURALLY PARALLEL TO SEREGIN'S 2026 EULER-SCALING TYPE-II PROGRAM, BUT THE REPOSITORY DOES NOT YET DERIVE SEREGIN'S FULL SCALE-WEIGHTED COMPACTNESS ASSUMPTIONS AND NO EXTERNAL LIOUVILLE THEOREM IS APPLIED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Canonical remote source scale

Let the target first-hitting natural scale be

\[
r_j=\sqrt{\frac{\nu}{W_j}},
\]

and suppose a fixed-fraction remote strain payer lies at

\[
R_j=K_jr_j,
\qquad K_j\to\infty.
\]

M5-437 shows that the source must have local velocity oscillation at least

\[
U_R\gtrsim\frac{\nu K_j^2}{R_j}.
\]

Define the canonical Euler velocity scale by the lower-bound value

\[
\boxed{
U_j^E
:=
\frac{\nu K_j^2}{R_j}
=
\frac{\nu R_j}{r_j^2}.
}
\]

The associated nonlinear time is

\[
\boxed{
T_j^E
:=
\frac{R_j}{U_j^E}
=
\frac{r_j^2}{\nu}.
}
\]

Thus the source-scale Euler clock is exactly the current first-hitting clock.

---

## 2. Euler normalization

Choose a source center `x_j^s` and a Galilean constant `c_j` realizing the local velocity oscillation quotient up to fixed constants.

Set

\[
y=\frac{x-x_j^s}{R_j},
\qquad
\tau=\frac{t-t_j}{T_j^E},
\]

and

\[
\boxed{
V_j(y,\tau)
=
\frac{u(x,t)-c_j}{U_j^E}.
}
\]

Scale pressure by `(U_j^E)^2`.

Then the Navier--Stokes equation becomes

\[
\boxed{
\partial_\tau V_j
+(V_j\cdot\nabla_y)V_j
=-\nabla_yP_j
+\varepsilon_j\Delta_yV_j,
\qquad
\nabla_y\cdot V_j=0,
}
\]

with

\[
\boxed{
\varepsilon_j
=
\frac{\nu}{U_j^ER_j}
=
K_j^{-2}
\to0.
}
\]

Thus the remote strong-throughput branch is canonically a vanishing-viscosity / Euler-scaling branch.

---

## 3. First-hitting vorticity cap becomes order one

The Euler-scaled vorticity is

\[
\Omega_j^E
=
\nabla_y\times V_j
=
\frac{R_j}{U_j^E}\omega.
\]

Since

\[
\frac{R_j}{U_j^E}
=
\frac{r_j^2}{\nu}
\]

and the first-hitting stage has

\[
|\omega|\le qW_j
=q\frac{\nu}{r_j^2},
\]

we obtain

\[
\boxed{
\|\Omega_j^E\|_\infty
\le q.
}
\]

This is an important normalization fact: although the source velocity amplitude is Type-II large relative to parabolic scaling at `R_j`, the corresponding Euler-scaled vorticity amplitude remains uniformly bounded.

---

## 4. Source nontriviality survives the normalization

M5-437 gives

\[
\inf_c\|u-c\|_{L^2(D_{R_j})}
\ge
c\nu K_j^2R_j^{1/2}.
\]

But

\[
U_j^ER_j^{3/2}
=
\frac{\nu K_j^2}{R_j}R_j^{3/2}
=
\nu K_j^2R_j^{1/2}.
\]

Therefore on a fixed normalized source annulus `D_1`,

\[
\boxed{
\inf_c
\|V_j-c\|_{L^2(D_1)}
\ge c_0>0.
}
\]

The Euler normalization does not collapse to the zero field.

If the normalized local oscillation instead diverges above this lower scale, that is an even stronger amplitude noncompactness branch.

---

## 5. Natural microstructure becomes subscale 1/K

The original first-hitting natural scale is `r_j`. In source-scale Euler variables this becomes

\[
\boxed{
\frac{r_j}{R_j}=K_j^{-1}\to0.
}
\]

Thus the remote source can contain increasingly fine vorticity microstructure inside an order-one Euler-scale region.

This explains why the uniform vorticity amplitude bound alone does not automatically give strong compactness in source variables.

Indeed the parent analyticity estimate gives schematically

\[
|\nabla_y\Omega_j^E|
\lesssim K_j
\]

rather than a uniform source-scale derivative bound.

Therefore an Euler limit requires an additional compactness condition; it is not automatic from M5-392.

---

## 6. Exact compactness split

The strong remote branch now splits naturally.

### A. Euler-compact source branch

Suppose, on every fixed source-scale cylinder, the normalized family additionally satisfies uniform bounds sufficient for local compactness, for example bounded scale-weighted energy/gradient/pressure quantities of the standard suitable-solution type.

Then after extracting a subsequence,

\[
V_j\to V
\]

locally in a topology strong enough to pass the nonlinear term, while

\[
\varepsilon_j\to0.
\]

The limit solves the incompressible Euler equations

\[
\boxed{
\partial_\tau V+(V\cdot\nabla)V=-\nabla P,
\qquad
\nabla\cdot V=0,
}
\]

and is nontrivial because of the fixed local oscillation lower bound.

Since `T_j^E=r_j^2/nu ->0`, the fixed pre-singular physical time interval expands to an arbitrarily long backward interval in `tau`; under uniform local bounds this is the natural route to an ancient Euler profile.

### B. Euler-noncompact source branch

If the required local source-scale compactness fails, then at least one normalized amplitude, derivative/frequency, pressure, spatial-tail, or time-compactness quantity diverges.

This is not a new quiet branch. It is a stricter form of

\[
\boxed{H_{strong\ critical/noncompact}.}
\]

Thus

\[
\boxed{
H_{remote}^{strong}
\Longrightarrow
E_{ancient}^{Euler,compact}
\lor
H_{Euler\text{-}scale\ noncompact}^{strong}.
}
\]

---

## 7. Comparison with Seregin 2026

Gregory Seregin, *On potential Type II blowups for the Navier-Stokes equations* (arXiv:2606.29468, 2026), studies particular Type-II scenarios by an Euler scaling and obtains nontrivial ancient Euler limits under explicit scale-weighted local energy, gradient, pressure, and mixed-norm assumptions.

The structural parallel is direct:

\[
\boxed{
\text{Type-II amplification}
\to
\text{Euler scaling}
\to
\text{ancient Euler profile}
\to
\text{scenario-dependent Liouville/rigidity}.
}
\]

However the present repository has **not** yet proved that the M5-440 remote source satisfies Seregin's precise conditions `(1.3)`, `(1.7)`, `(2.4)`, or their Section 3 replacements.

Therefore no theorem from that paper is imported as a closure here.

The correct claim is only that M5-443 independently reaches the same Euler-scaling junction from the first-hitting remote-source geometry.

---

## 8. Highest-value next target

The next useful calculation is no longer another remote distance estimate.

It is to derive, from the first-hitting cap plus the source-action ledgers, enough source-scale Morrey/energy/pressure control to decide between:

1. a compact nontrivial ancient Euler profile in a known Liouville class;
2. explicit source-scale noncompactness, which can be priced by a stronger critical throughput ledger.

In particular, the quantities closest to Seregin's framework should be translated into the repository's source variables rather than assumed.

---

## 9. Firewall

Bounded Euler-scaled vorticity does not imply a Liouville theorem. Nontrivial bounded-vorticity ancient or steady Euler flows exist in broad classes.

Likewise vanishing viscosity does not by itself imply strong convergence to Euler without compactness.

Therefore M5-443 is a reduction to an Euler rigidity problem, not a closure.

---

## 10. Audit verdict

### Derived

\[
\boxed{
\varepsilon_j=K_j^{-2}\to0,
\qquad
\|\Omega_j^E\|_\infty\le q,
\qquad
\inf_c\|V_j-c\|_{L^2(D_1)}\ge c_0.
}
\]

### Frontier split

\[
\boxed{
H_{remote}^{strong}
\Longrightarrow
E_{ancient}^{Euler,compact}
\lor
H_{Euler\text{-}scale\ noncompact}^{strong}.
}
\]

### External comparison

This independently reaches the Euler-scaling junction used in recent Type-II work, but the external theorem hypotheses have not yet been derived.

### Still open

- Euler-scale compactness/pressure control;
- Liouville rigidity for the resulting nontrivial Euler profile;
- source-scale noncompactness pricing;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
