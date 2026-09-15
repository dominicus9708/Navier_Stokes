# DSD M19-278 — Critical radial source pairing collapses to the pre-existing infinite diffuse spectator-tail defect

**Date:** 2026-09-16  
**Canonical ID:** **M19-278**  
**Status:** **ACTIVE RADIAL-DEFECT AUDIT / CRITICAL POSITIVE WEIGHT IDENTIFIED / FINITE NON-COBOUNDARY BUDGET FAILS / REMOTE DEFECT RECLASSIFIED AS DIFFUSE SPECTATOR TAIL / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-276--277

On the CE-H material-population branch, with \(W=\rho\xi\), the population exchange/source density satisfies

\[
\boxed{
S_p
:=
\rho^p\kappa
+\rho^p|\nabla\xi|^2
+(p-1)\rho^{p-2}|\nabla\rho|^2
=
\frac1p\Delta(\rho^p).
}
\]

Hence every compactly supported spatial test \(\psi\) gives

\[
\boxed{
\int \psi S_p
=
\frac1p\int \rho^p\Delta\psi,
}
\]

so compact localization does not create a new one-sign non-coboundary resource.

For \(p=2\) and radial power \(\psi(r)=r^\alpha\),

\[
\Delta r^\alpha
=
\alpha(\alpha+1)r^{\alpha-2},
\]

therefore

\[
\boxed{
\int r^\alpha S_2
=
\frac{\alpha(\alpha+1)}2
\int r^{\alpha-2}|W|^2.
}
\]

## 2. Unique scale-critical radial weight

Under Navier--Stokes scaling, the weighted enstrophy quantity

\[
\int r^{\alpha-2}|W|^2dy
\]

has scaling degree \(3-\alpha\). Thus the unique scale-critical power is

\[
\boxed{\alpha=3.}
\]

At this exponent,

\[
\boxed{
\int r^3 S_2\,dy
=
6\int r|W|^2dy.
}
\]

Thus the only positive scale-critical radial source pairing is exactly the first radial enstrophy moment.

## 3. M5-531 already classifies the critical quantity

M5-531 proves on every nontrivial invariant recurrent hard component that

\[
\boxed{
\mathcal M_1(Y)
:=
\int_{\mathbb R^3}|y|\,|W_Y(y)|^2dy
=
\infty
}
\]

for invariant-almost every state.

Therefore the critical radial pairing is not a finite signed budget that can be exhausted by repeated positive events. It is already infinite on the surviving recurrent component.

Hence

\[
\boxed{
\text{critical positive radial pairing}
\not\Rightarrow
\text{finite non-coboundary contradiction}.
}
\]

## 4. M5-532 converts the divergence to a radial defect equation

Define

\[
\mathfrak T(\varrho,Y)
=
R\int_{|y|>R}|W_Y|^2dy,
\qquad R=e^{\varrho}.
\]

M5-532 gives the invariant mean balance

\[
\boxed{
\frac12\frac d{d\varrho}\overline{\mathfrak T}(\varrho)
=
\overline{\mathcal S}(\varrho),
}
\]

while

\[
\boxed{
\int^\infty\overline{\mathfrak T}(\varrho)d\varrho
=
\infty.
}
\]

If \(\overline{\mathfrak T}\) is bounded at large radius, then

\[
\boxed{
\sup_{\varrho>\varrho_0}
\left|
\int_{\varrho_0}^{\varrho}
\overline{\mathcal S}(s)ds
\right|<\infty.
}
\]

Thus the surviving bounded branch is a conservative/oscillatory radial defect with infinite occupation but bounded signed source primitive, not a one-way monotone drain.

## 5. M5-533 fixes the tail morphology

The globally compact high-Sobolev hull has uniform remote derivative decay. In particular,

\[
\boxed{
\sup_Y\sup_{|y|>R}|\nabla^jW_Y(y)|\to0
\qquad(R\to\infty)
}
\]

for every fixed \(j\).

Therefore the infinite first radial moment is carried by a vanishing-amplitude diffuse/spreading tail, not by fixed-strength coherent packets.

The persistent fixed-flux lineage network remains a bounded/intermediate-scale core object.

## 6. M5-534 decouples the remote defect from the active core

For any fixed core ball \(B_L\), the remote Biot--Savart contribution obeys

\[
\boxed{
\|U_{far,R}\|_{L^\infty(B_L)}
\lesssim
R^{-1/2}E_{tail}(R)^{1/2},
}
\]

and

\[
\boxed{
\|\Sigma_{far,R}\|_{L^\infty(B_L)}
\lesssim
R^{-3/2}E_{tail}(R)^{1/2}.
}
\]

Since the unweighted enstrophy tail is uniformly tight, both quantities vanish as \(R\to\infty\).

Hence the infinite weighted tail cannot directly pay the fixed positive recurrent stretching/projective action in the bounded core.

## 7. Consequence for M19-271 lag-defect search

M19-271 requires a non-coboundary remainder/resource with positive mean whose payment is independently impossible or finite-budgeted.

The radial source candidate fails this standard in the only scale-critical positive power:

\[
\boxed{
\psi=r^3
\Longrightarrow
\text{positive pairing}
=
6\mathcal M_1
=
\infty.
}
\]

Moreover M5-532 shows that its radial source primitive can remain bounded by signed cancellation, while M5-533--534 separate it dynamically from the active core.

Therefore

\[
\boxed{
\mathcal T_{lag}^{radial-source}
\text{ does not close the hard branch.}
}
\]

It must be reclassified as

\[
\boxed{
\mathcal E_{remote}^{diffuse}
:=
\text{infinite first radial moment + vanishing-amplitude spectator tail}.
}
\]

## 8. Updated separation of active mechanisms

The retained hard architecture now has a sharper decomposition:

\[
\boxed{
\text{active bounded/intermediate core}
\quad\oplus\quad
\text{diffuse remote weighted spectator defect}.
}
\]

The active core carries

- positive production;
- persistent fixed-flux populations/lineages;
- projective or anchored CE-H events;
- finite-depth signed energy-transport events.

The remote tail carries

- infinite critical first radial moment;
- vanishing pointwise vorticity amplitude;
- bounded/oscillatory signed radial-source primitive on the bounded-tail branch;
- asymptotically negligible direct strain influence on the active core.

These two structures must not be merged into one payer ledger.

## 9. Updated closure targets

The terminal hard branch is therefore reduced to the following genuinely distinct gates.

### Stationary/terminal-defect route

\[
\boxed{
\mathcal T_{stress}^{tight}
\lor
\mathcal T_{tail}^{zero-force-rigidity}.
}
\]

The stationary point-force coefficient can disappear only through uniform far-field stress tightness or a critical weak-\(L^3\) zero-force rigidity theorem; finite energy, ordinary moment identities, helicity, and leading pressure do not supply this automatically.

### Dynamic recurrent-core route

\[
\boxed{
\mathcal T_{tail}^{lag-defect/core}
\lor
\mathcal T_{aper}^{signed/index}
\lor
\mathcal T_{critical}^{factor/observability}.
}
\]

Any successful non-coboundary object must be supported by the active core/intermediate scales or by a genuine global factor/observability obstruction. The diffuse radial reservoir cannot serve as the required finite critical payer.

### Independent physical-derivative route

\[
\boxed{
\mathcal T_{GMS}^{base-gain}
}
\]

and its representation/root gates remain open and are not altered by this radial-tail audit.

## 10. Permanent firewalls added by M19-278

\[
\boxed{
\text{positive radial source pairing}
\not\Rightarrow
\text{finite critical budget},
}
\]

\[
\boxed{
\text{scale-critical radial weight}
\Longrightarrow
\text{first radial moment defect},
}
\]

\[
\boxed{
\text{infinite first radial moment}
\not\Rightarrow
\text{order-one remote coherent packet},
}
\]

\[
\boxed{
\text{infinite weighted remote tail}
\not\Rightarrow
\text{order-one direct core strain payer},
}
\]

and

\[
\boxed{
\text{remote diffuse defect}
\neq
\text{active recurrent core mechanism}.
}
\]

## 11. Verdict

The M19-277 radial-weight candidate is now fully audited.

Its unique positive scale-critical realization is not a new closure mechanism; it is exactly the already certified infinite first radial enstrophy moment. Historical M5-532--534 further show that this defect is conservative/diffuse, vanishing-amplitude, and asymptotically decoupled from bounded-core stretching.

Therefore the radial-source route is closed as a **NO-GO for finite non-coboundary payment**, while the corresponding remote-tail defect remains a legitimate survivor.

The next active theorem must act on the bounded/intermediate recurrent core, terminal stress tightness/zero-force rigidity, the GMS base-gain gate, or a genuinely global dynamical-factor/observability obstruction.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
