# DSD M5-513 — Audit signed cycle observables: circulation, helicity, and dual-frame winding

Date: 2026-09-01

Status: **SIGNED-OBSERVABLE AUDIT / MATERIAL CIRCULATION IN SIMILARITY VARIABLES IS SCALE INVARIANT AND, BY STOKES, IS THE SAME MATERIAL VORTICITY-FLUX OBSERVABLE ALREADY AUDITED IN M5-489; ITS VISCOUS INCREMENT IS SIGN-INDEFINITE AND HAS ZERO MEAN ON A RECURRENT PERSISTENT LINEAGE / GLOBAL HELICITY IS ALSO SCALE INVARIANT, BUT IT IS NOT AUTOMATICALLY FINITE IN THE CURRENT `W IN L2`, `U IN L6` CLASS, AND EVEN WHEN FINITE ITS VISCOUS DERIVATIVE `-2 int W·curl W` HAS NO DEFINITE SIGN / A PERSISTENT NONCOLLINEAR DUAL PAIR CAN LOCALLY DEFINE AN `SO(3)` FRAME AND HENCE A PATH-HOMOTOPY/WINDING MARK, BUT THE PRESENT GENEALOGY DOES NOT KEEP A UNIFORM NONCOLLINEAR GAP FOR THE ENTIRE RETURN CYCLE, NOR DOES POSITIVE RATCHET ACTION FORCE NONTRIVIAL WINDING / THE OBVIOUS SIGNED STATE OBSERVABLES THEREFORE DO NOT YET CLOSE THE RECURRENT HARD CORE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Target from M5-512

M5-512 showed that every marked generation in the globally smooth compact branch pays a fixed positive local phase-space arclength.

That action is unsigned and therefore compatible with closed recurrent cycles.

To close a finite lineage cycle, one needs a quantity whose increment is genuinely signed and cannot cancel around the loop.

M5-513 audits three natural candidates:

1. material circulation;
2. global helicity;
3. topological winding of a persistent noncollinear dual pair.

---

## 2. Material circulation is scale invariant

Let `C(s)` be a physical material loop transported by the ancient velocity `mathcal U`, and define

\[
\Gamma(s)
:=
\oint_{C(s)}
\mathcal U(x,s)\cdot dx.
\]

Under backward similarity variables

\[
x=\sqrt a\,y,
\qquad
a=-s,
\qquad
U(y,\theta)=\sqrt a\,\mathcal U(\sqrt a y,-a),
\]

we have

\[
\mathcal U=a^{-1/2}U,
\qquad
dx=\sqrt a\,dy.
\]

Hence

\[
\boxed{
\Gamma(s)
=
\oint_{\gamma(\theta)}U(y,\theta)\cdot dy.
}
\]

There is no scaling prefactor.

Thus circulation is Navier--Stokes scale critical, just like material vorticity flux.

---

## 3. Exact viscous circulation law

For viscosity one, Kelvin's circulation identity for a material loop is

\[
\frac{d\Gamma}{ds}
=
\oint_{C(s)}
\Delta_x\mathcal U\cdot dx.
\]

Since

\[
\Delta_x\mathcal U
=a^{-3/2}\Delta_yU,
\qquad
dx=\sqrt a\,dy,
\qquad
\frac{ds}{d\theta}=a,
\]

we obtain

\[
\boxed{
\frac{d\Gamma}{d\theta}
=
\oint_{\gamma(\theta)}
\Delta U\cdot dy.
}
\]

The right side has no definite sign.

---

## 4. Circulation is not independent of M5-489 flux

If `Sigma(theta)` is any oriented material surface spanning `gamma(theta)`, Stokes gives

\[
\Gamma(\theta)
=
\int_{\Sigma(\theta)}W\cdot n\,dA
=\Phi(\theta).
\]

Likewise,

\[
\oint_{\gamma}\Delta U\cdot dy
=
\int_{\Sigma}
\nabla\times\Delta U\cdot n\,dA
=
\int_{\Sigma}\Delta W\cdot n\,dA.
\]

Therefore the circulation law is exactly the M5-489 material-flux law:

\[
\boxed{
\Gamma'=\Phi'
=
\int_{\Sigma}\Delta W\cdot n\,dA.
}
\]

It does not provide a second signed channel.

On a recurrent persistent lineage,

\[
\langle\Gamma'\rangle
=
\langle\Phi'\rangle
=0,
\]

while absolute variation may remain positive.

Thus circulation fails as a strict cycle potential for the same reason as flux.

---

## 5. Helicity is also scale invariant

Formally define physical helicity

\[
\mathcal H(s)
:=
\int_{\mathbb R^3}
\mathcal U(x,s)\cdot\mathcal\Omega(x,s)dx.
\]

Under similarity scaling,

\[
\mathcal U=a^{-1/2}U,
\qquad
\mathcal\Omega=a^{-1}W,
\qquad
dx=a^{3/2}dy.
\]

All powers cancel:

\[
\boxed{
\mathcal H(s)
=
\int_{\mathbb R^3}U(y,\theta)\cdot W(y,\theta)dy.
}
\]

Thus helicity is another scale-critical candidate.

---

## 6. First helicity firewall: finiteness is not automatic

The current compact vorticity class gives

\[
W\in L^2,
\qquad
U\in L^6.
\]

Holder would require

\[
W\in L^{6/5}
\]

to guarantee

\[
U\cdot W\in L^1.
\]

But on the whole space,

\[
W\in L^2\cap L^\infty
\]

does not imply membership in an exponent below `2`.

Equivalently, in Fourier variables helicity contains a low-frequency factor schematically comparable to

\[
\int
\frac{|\widehat W(\xi)|^2}{|\xi|}d\xi,
\]

which is not controlled by the unweighted `L2` vorticity norm alone.

Therefore

\[
\boxed{
\mathcal H
\text{ need not be a finite continuous observable on the entire M5-508 hull.}
}
\]

A global helicity cocycle cannot be used without an additional low-frequency/integrability hypothesis.

---

## 7. Second helicity firewall: the viscous derivative has no sign

Assume temporarily that all decay/integrability conditions needed for the standard helicity identity hold.

For physical Navier--Stokes,

\[
\frac{d\mathcal H}{ds}
=-2
\int
\mathcal\Omega\cdot
(\nabla_x\times\mathcal\Omega)dx.
\]

Transforming to similarity time gives

\[
\boxed{
\frac{d}{d\theta}
\int U\cdot W\,dy
=
-2
\int
W\cdot(\nabla\times W)dy.
}
\]

Again there is no similarity damping term because helicity is scale invariant.

The integrand

\[
W\cdot\nabla\times W
\]

has no fixed sign.

Therefore even on a subbranch where helicity is finite,

\[
\boxed{
\text{viscosity does not make helicity a monotone Lyapunov quantity.}
}
\]

A recurrent orbit may have zero mean signed helicity dissipation and positive absolute helicity variation.

---

## 8. Localized helicity does not repair the sign problem automatically

One may introduce a cutoff

\[
\mathcal H_R
:=
\int\chi_R U\cdot W\,dy.
\]

This is finite and continuous on the globally smooth compact hull.

However differentiating `H_R` generates

1. the sign-indefinite bulk term `W·curl W`;
2. transport through the cutoff boundary;
3. viscous boundary commutators;
4. similarity-dilation cutoff terms.

None has a known one-sided sign on the recurrent lineage cycle.

Thus localization repairs finiteness but not strictness.

---

## 9. Persistent dual pair as a local frame

Suppose two persistent oriented vorticity directions satisfy

\[
\xi_a\times\xi_b\ne0.
\]

Then define

\[
e_1=\xi_a,
\]

\[
e_2
=
\frac{\xi_b-(\xi_a\cdot\xi_b)\xi_a}
{|\xi_b-(\xi_a\cdot\xi_b)\xi_a|},
\]

and

\[
e_3=e_1\times e_2.
\]

The matrix

\[
R_{ab}
=(e_1,e_2,e_3)
\]

lies in

\[
SO(3).
\]

Thus a continuously noncollinear dual pair can define a path in `SO(3)`.

For a closed pair cycle, the loop has a homotopy class in

\[
\pi_1(SO(3))\cong\mathbb Z_2.
\]

This is a genuine path-memory quantity rather than an instantaneous scalar potential.

---

## 10. Why the frame winding is not yet available as a proof obstruction

M5-490 guarantees recurrent positive-frequency noncollinear dual events.

It does **not** prove a uniform angle gap

\[
|\xi_a\times\xi_b|
\ge s_*>0
\]

for every time along an entire return cycle.

If the pair becomes collinear, the frame `R_ab` degenerates and its loop class cannot be continued without an additional convention or replacement rule.

Even if a continuous frame loop exists, positive ratchet action only implies nonzero path length. It does not imply that the loop represents the nontrivial element of `Z2`.

A contractible loop can have arbitrarily large path length and repeated projective action.

Therefore

\[
\boxed{
\text{positive ratchet action}
\not\Longrightarrow
\text{nontrivial }SO(3)\text{ winding}.
}
\]

---

## 11. Signed-observable verdict

The three natural candidates give:

### Circulation

\[
\boxed{
\text{exactly the same coboundary as vorticity flux; zero mean signed viscous increment.}
}
\]

### Helicity

\[
\boxed{
\text{not automatically finite; when finite, derivative is sign-indefinite.}
}
\]

### Dual-frame winding

\[
\boxed{
\text{genuinely path-topological, but continuous frame persistence and nontrivial winding are not forced.}
}
\]

Hence no currently justified candidate produces the strict bounded cocycle required by M5-485.

---

## 12. New exact subtargets

The audit turns the vague search for a `strict cocycle` into three concrete possible routes.

### S1 — low-frequency helicity closure

Prove enough spatial/low-frequency control to make helicity finite and then find an additional structural condition forcing one sign of

\[
\int W\cdot\nabla\times W.
\]

No such sign is presently known.

### S2 — persistent frame-gap theorem

Show that one recurrent dual pair satisfies

\[
|\xi_a\times\xi_b|
\ge s_*>0
\]

through an entire recurrent cycle, not merely on a positive-frequency event set.

Then an `SO(3)` path invariant is well defined.

### S3 — collinearity-crossing cost

If a recurrent pair must repeatedly lose the angle gap, quantify the cost of crossing the near-collinear set and determine whether that cost forces replacement, separator palinstrophy, or a signed viscous flux event.

This is the most direct internal DSD route after the present audit.

---

## 13. Updated hard core

The finite recurrent critical network is now known to support

\[
\boxed{
\text{positive unsigned state action}
+
\text{zero-mean signed material circulation/flux}
+
\text{sign-indefinite helicity channel}
}
\]

with possible pair-frame topology not yet globally defined.

Thus the remaining obstruction is specifically **cycle topology or irreversible signed transfer**, not ordinary norm growth.

---

## 14. Highest-value next target

Proceed with S3 first.

Track one persistent dual pair from an event with

\[
\sin\angle(\xi_a,\xi_b)\ge s_0
\]

toward any subsequent near-collinear state.

Use the exact relative-angle equation from M5-491,

\[
\frac d{d\theta}(\xi_a\cdot\xi_b)
=R_{strain}+R_{diff},
\]

together with the M5-492 active-bridge/separator dichotomy and the M5-512 time-thickening mechanism.

The goal is a quantitative dichotomy:

\[
\boxed{
\text{uniform frame gap}
\lor
\text{fixed crossing cost per angle collapse}.
}
\]

This is sharper than searching for an unspecified scalar Lyapunov function.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
