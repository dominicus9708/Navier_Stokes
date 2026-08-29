# DSD M5-264 — Momentum-Stress Absolute-Action Gate

Date: 2026-08-30

Parent: `DSD_M5_263_RECURRENT_MEAN_MOMENTUM_TO_BOUNDARY_STRESS_OR_RELATIVE_TRACE_2026-08-30.md`

Status: **NEW FORMED TURNOVER ACTION / THE VECTOR MOMENTUM-STRESS CORRELATION FORCED BY THE STATIONARY-TAIL MEAN-DRIFT BRANCH IS NOT IDENTICAL TO THE EXISTING SCALAR ABSOLUTE RELATIVE-ENERGY BOUNDARY ACTION / COMPACTNESS OF THE FIXED-BALL W1 HULL CONVERTS THE SIGNED CORRELATION FLOOR INTO A STRICT ABSOLUTE MOMENTUM-STRESS ACTION FLOOR; COMPONENTWISE TRIANGLE INEQUALITY THEN FORCES CONVECTIVE, PRESSURE-FORCE, OR VISCOUS-FORCE ACTION / THIS IS A FINITE NEW `T_mom` SUBTYPE UNLESS A LATER COMPARISON ABSORBS IT INTO THE OLD SCALAR T GATE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input correlation

M5-263 gives, on the momentum-stress branch,

\[
\boxed{
\left|\left\langle m_R\cdot b_{phys}\right\rangle\right|
\ge
\frac14\langle|m_R|^2\rangle.
}
\]

With the M5-262 current-induced mean floor,

\[
\boxed{
\langle|m_R|^2\rangle
\ge m_*^2
:=\frac{3j_R}{\pi R^3}.
}
\]

Therefore

\[
\boxed{
\left|\left\langle m_R\cdot b_{phys}\right\rangle\right|
\ge\frac14m_*^2>0.
}
\]

---

## 2. Compact mean upper bound

On the fixed-ball compact W1 hull, the local mean is a continuous state observable. Hence

\[
\boxed{
|m_R(s)|\le m_+<\infty.
}
\]

Then

\[
\left|\left\langle m_R\cdot b_{phys}\right\rangle\right|
\le
m_+\langle|b_{phys}|\rangle.
\]

Thus

\[
\boxed{
\langle|b_{phys}|\rangle
\ge
b_*
:=
\frac{m_*^2}{4m_+}
>0.
}
\]

This is an absolute momentum-stress action floor.

---

## 3. Three physical force components

Recall

\[
 b_{phys}
=
\frac1{M_R}
\int_{\partial B_R}
\left[
\nu\partial_nV
-(V\otimes V)n
-Pn
\right]dS.
\]

Define

\[
\boxed{
 b_{vis}
:=
\frac\nu{M_R}
\int_{\partial B_R}\partial_nVdS,
}
\]

\[
\boxed{
 b_{conv}
:=-\frac1{M_R}
\int_{\partial B_R}(V\otimes V)n\,dS,
}
\]

and

\[
\boxed{
 b_{pres}
:=-\frac1{M_R}
\int_{\partial B_R}Pn\,dS.
}
\]

The pressure term is gauge invariant because

\[
\int_{\partial B_R}n\,dS=0.
\]

Then

\[
\boxed{b_{phys}=b_{vis}+b_{conv}+b_{pres}.}
\]

---

## 4. Finite component fork

By triangle inequality,

\[
|b_{phys}|
\le
|b_{vis}|+|b_{conv}|+|b_{pres}|.
\]

Averaging and using the action floor gives

\[
\boxed{
\langle|b_{vis}|\rangle
+\langle|b_{conv}|\rangle
+\langle|b_{pres}|\rangle
\ge b_*.
}
\]

Hence at least one component satisfies

\[
\boxed{
\langle|b_{vis}|\rangle\ge b_*/3
}
\]

or

\[
\boxed{
\langle|b_{conv}|\rangle\ge b_*/3
}
\]

or

\[
\boxed{
\langle|b_{pres}|\rangle\ge b_*/3.
}
\]

Thus the mean-drift branch has been reduced to three explicit physical boundary-force mechanisms.

---

## 5. Viscous-force branch

Cauchy--Schwarz on the sphere gives

\[
|b_{vis}|
\le
\frac\nu{M_R}
|\partial B_R|^{1/2}
\|\partial_nV\|_{L^2(\partial B_R)}.
\]

Therefore a positive `b_vis` action requires a positive normal-derivative trace action.

By a standard local trace estimate on a slightly enlarged annulus, this routes to

\[
\boxed{
H2\text{-type derivative action}
\quad\lor\quad
\text{large annular }H1\text{ reservoir}.
}
\]

No claim is made that a mere positive value crosses the repository's H ceiling.

---

## 6. Convective-force branch

Similarly,

\[
|b_{conv}|
\le
\frac1{M_R}
\int_{\partial B_R}|V|^2dS.
\]

Thus large convective momentum action requires a persistent boundary velocity-amplitude/trace reservoir.

After subtracting the local mean,

\[
V=m_R+w_R,
\]

this becomes a finite combination of

- mean-drift amplitude;
- relative boundary trace;
- their cross term.

The relative trace is already routed to gradient/variance in M5-263. The pure mean part is constrained by the recurrent momentum equation itself.

---

## 7. Pressure-force branch

The pressure force is

\[
 b_{pres}
=-M_R^{-1}\int_{\partial B_R}Pn\,dS.
\]

By divergence theorem,

\[
\int_{\partial B_R}Pn\,dS
=\int_{B_R}\nabla P\,dY.
\]

Thus positive pressure-force action is a genuine local pressure-gradient action.

On the spatial-Type-I corridor, pressure is determined by velocity through the Poisson/Riesz representation, but the vector integral has no universal sign. It therefore routes to

\[
\boxed{
\text{pressure-gradient / nonlocal tail coupling}
}
\]

rather than disappearing by gauge choice.

---

## 8. Why the old scalar absolute-action gate does not automatically absorb this

The existing compensated-variance absolute boundary action uses the scalar relative-energy work

\[
F_w
\]

constructed from

- `|v|^2` material crossing;
- pressure work `(p-c)v·grad phi`;
- viscous cutoff leakage.

The present momentum action uses instead

\[
\nu\partial_nV,
\qquad
(V\otimes V)n,
\qquad
Pn
\]

paired at vector level with the local mean.

Neither family pointwise dominates the other without extra amplitude/trace assumptions.

Therefore

\[
\boxed{
T_{mom}\not\equiv T_{abs}
}

at the present level of the audit.

This is a firewall against hiding a new vector force channel inside an old scalar-energy label.

---

## 9. Scale-normalized interpretation

At a first-hitting physical scale `r_j`, velocity scales like `r_j^-1`, pressure like `r_j^-2`, and momentum stress like `r_j^-2`.

After integrating over a sphere of area `r_j^2` and normalizing by the ball volume `r_j^3`, the physical mean acceleration scales like `r_j^-3` in physical time, which becomes order one in the natural similarity-time/velocity normalization.

Thus `b_*` is a genuine scale-normalized finite-stage action and does not vanish merely because `r_j->0`.

Its unweighted physical energy cost may still be summable across generations; no global contradiction is claimed from scaling alone.

---

## 10. Updated stationary endpoint

Combining M5-260--264,

\[
\boxed{
S_{crit}^{stationary}
\Longrightarrow
T_{var/bdry}
\lor
T_{rel-trace}
\lor
T_{mom},
}

where

\[
\boxed{
T_{mom}
=
T_{vis-force}
\lor
T_{conv-force}
\lor
T_{pres-force}.
}

This is now a finite and physically typed boundary-action family.

---

## 11. Next target

The pressure-force and viscous-force components naturally require one derivative more than the scalar variance ledger. The convective-force component is lower order.

The next efficient audit is therefore:

1. absorb `T_vis-force` and `T_pres-force` into the already defined H2/pressure-gradient ceiling **if and only if** their normalized thresholds exceed the pure corridor;
2. analyze `T_conv-force` using the mean + relative-trace decomposition and the M5-262 mean floor.

If all three remain below their pure ceilings, the momentum equation itself may give an upper bound contradicting `b_*`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
