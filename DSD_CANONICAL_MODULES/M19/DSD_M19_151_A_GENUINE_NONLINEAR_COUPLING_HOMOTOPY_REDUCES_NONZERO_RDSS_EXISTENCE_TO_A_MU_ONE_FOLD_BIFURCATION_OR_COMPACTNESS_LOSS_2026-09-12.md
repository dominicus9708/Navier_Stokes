# DSD M19-151 — A genuine nonlinear-coupling homotopy reduces nonzero RDSS existence to a mu=1 fold/bifurcation or compactness loss

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / PERIODIC-ORBIT EXISTENCE REDUCTION / INTRODUCING A TRUE EXTERNAL HOMOTOPY PARAMETER TAU IN FRONT OF THE NAVIER--STOKES QUADRATIC TERM CONNECTS THE LINEAR OU/STOKES PROBLEM AT TAU=0 TO THE ORIGINAL EQUATION AT TAU=1 / AT FIXED INTRINSIC (S,Q_*) A NONZERO RELATIVE-PERIODIC SOLUTION CANNOT APPEAR ALONG A COMPACT SOLUTION COMPONENT WITHOUT A MU=1 FIXED-POINT DEGENERACY / ELLIPTIC UNIT MULTIPLIERS ALONE DO NOT CREATE A NEW FIXED-POINT BRANCH / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why a new homotopy parameter is legitimate

M19-113 correctly warned that

\[
S,
\quad Q_*,
\quad \alpha
\]

are intrinsic moduli of a relative-periodic orbit, not free external parameters of the Navier--Stokes equation.

That firewall remains in force.

Here introduce instead a genuine equation parameter

\[
\boxed{\tau\in[0,1]}
\]

multiplying the quadratic advection:

\[
\boxed{
\partial_sU
+\frac12U
+\frac12(y\cdot\nabla)U
+\tau(U\cdot\nabla)U
=-\nabla P+\nu\Delta U,
\qquad
\nabla\cdot U=0.
}
\]

At

\[
\tau=1
\]

this is the original similarity Navier--Stokes equation.
At

\[
\tau=0
\]

it is the linear similarity Stokes/OU equation.

This is an artificial homotopy for proof architecture, but it is a genuine external parameter of the homotopy family and therefore does not violate M19-113.

---

## 2. Fix relative-periodic moduli

For the continuation argument, fix an intrinsic candidate pair

\[
S>0,
\qquad
Q_*\in SO(3),
\]

and impose

\[
\boxed{U(s+S)=Q_*U(s).}
\]

After phase/rotation gauges, define the relative-periodic operator

\[
\mathcal F_\tau(U;S,Q_*)=0.
\]

The target original orbit, if it exists, is a zero of

\[
\mathcal F_1.
\]

---

## 3. Linear endpoint tau=0

At `tau=0`, the equation is linear.

The vorticity satisfies the bare quarter-gap evolution

\[
\frac12\frac d{ds}\|\Omega\|_2^2
+\nu\|\nabla\Omega\|_2^2
+\frac14\|\Omega\|_2^2
=0.
\]

If

\[
\Omega(s+S)=Q_*\Omega(s),
\]

then integrating one period gives

\[
\nu\int_s^{s+S}\|\nabla\Omega\|_2^2d\sigma
+\frac14\int_s^{s+S}\|\Omega\|_2^2d\sigma
=0.
\]

Hence

\[
\Omega\equiv0.
\]

Under the whole-space finite-energy/critical-tail class this implies the velocity is the trivial admissible state after excluding nondecaying harmonic/Galilean gauges.

Therefore

\[
\boxed{
\mathcal F_0(U;S,Q_*)=0
\Longrightarrow
U=0.
}
\]

There is no nonzero relative-periodic branch at the linear endpoint.

---

## 4. Suppose a nonzero tau=1 orbit exists

Assume there is a nonzero solution

\[
U_1
\]

of

\[
\mathcal F_1(U_1;S,Q_*)=0.
\]

Consider the zero set

\[
\mathcal Z
:=
\{(\tau,U):\mathcal F_\tau(U;S,Q_*)=0\}
\]

inside a controlled Banach/Fredholm corridor with phase/rotation gauges imposed.

Suppose the relevant solution component containing `(1,U1)` remains compact and does not leave the certified smooth hard class.

---

## 5. Local continuation at a nondegenerate point

If

\[
D_U\mathcal F_\tau
\]

is invertible on the symmetry-gauged space, the implicit-function theorem makes the solution set locally a unique graph

\[
U=U(\tau).
\]

Therefore the projection

\[
(\tau,U)\mapsto\tau
\]

has no interior endpoint or turning point at such a state.

A compact connected nonzero component cannot simply terminate in the interior of `0<tau<1` while the state derivative remains invertible.

---

## 6. Why a compact isola still needs degeneracy

A disconnected compact isola of nonzero solutions cannot evade this conclusion.

On a compact one-dimensional regular component, the projection to the interval `[0,1]` attains a maximum and minimum.
At an interior extremum the projection cannot be a local diffeomorphism.
Hence

\[
D_U\mathcal F_\tau
\]

must fail to be invertible there.

In fixed-point language, the corresponding twisted monodromy has

\[
\boxed{\mu=1}
\]

in the symmetry-quotiented spectrum.

Thus even an isolated saddle-node/isola requires a multiplier-one event.

---

## 7. Elliptic modes do not create a fixed-point branch by themselves

A multiplier

\[
\mu=e^{i\vartheta},
\qquad
\vartheta\ne0
\]

does not make

\[
I-\mathcal M_S^{tw}
\]

singular.

Therefore an elliptic unit multiplier alone does not destroy fixed-point invertibility and cannot by itself create or terminate a branch of relative-periodic fixed points under the scalar homotopy parameter `tau`.

This does not mean elliptic modes are irrelevant to recurrent dynamics; it means they are not the branch-creation obstruction for this continuation argument.

---

## 8. Continuation dichotomy

Under the fixed `(S,Q_*)` gauge and a priori compactness,

\[
\boxed{
\text{nonzero solution at }\tau=1
\Longrightarrow
\text{there exists }\tau_*\in(0,1]
\text{ with a nonsymmetry }\mu=1\text{ degeneracy}.
}
\]

If no such degeneracy exists, any attempted nonzero branch must instead leave the controlled corridor.

Hence the correct global alternative is

\[
\boxed{
\mathcal R_{RDSS/RSS}^{nonzero}
\Longrightarrow
\mathcal T_{kernel}^{homotopy}
\lor
\mathcal G_{homotopy\ compactness\ loss}.
}
\]

---

## 9. Relation to the zero state

M19-110 already gave a finite-amplitude floor near the zero profile for fixed positive period.
The present homotopy explains the topology behind that fact.

The zero branch persists for every `tau`, but a disconnected nonzero branch can appear only through a fold/bifurcation where fixed-point invertibility fails, or through loss of compactness from the controlled space.

Thus the moderate finite-amplitude RSS/RDSS hard core is not independent of the kernel problem once a uniform homotopy compactness theorem is available.

---

## 10. What must be proved for a full reduction

Two new uniform statements would suffice:

1. **homotopy kernel rigidity**
   \[
   \boxed{
   \ker D_U\mathcal F_\tau
   =E_{sym}^{\mu=1}
   \quad\forall\tau\in[0,1]
   }
   \]
   after gauge fixing;

2. **homotopy compactness**
   every relative-periodic solution with the retained Type-I/critical-tail bounds remains in a compact controlled corridor uniformly in `tau`.

If both hold, the linear endpoint `tau=0` has only zero and no nonzero relative-periodic orbit can exist at `tau=1`.

---

## 11. Firewall

This is a continuation reduction, not yet a proof of nonexistence.

In particular,

\[
\boxed{
\text{kernel-free at }\tau=1
\not\Rightarrow
\text{kernel-free for all }\tau\in[0,1].
}
\]

and

\[
\boxed{
\text{compactness of the original }\tau=1\text{ orbit}
\not\Rightarrow
\text{uniform compactness along the artificial homotopy}.
}
\]

---

## 12. Audit verdict

### Certified

- `tau` is a legitimate external homotopy parameter unlike intrinsic period/holonomy;
- the `tau=0` relative-periodic problem has only the trivial admissible solution;
- under fixed-moduli compact continuation, creation of a nonzero relative-periodic branch requires a `mu=1` fixed-point degeneracy;
- elliptic unit multipliers alone do not create a fixed-point branch in this homotopy.

### Not certified

- homotopy-uniform kernel rigidity;
- homotopy-uniform compactness;
- nonexistence at `tau=1`;
- global regularity.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
