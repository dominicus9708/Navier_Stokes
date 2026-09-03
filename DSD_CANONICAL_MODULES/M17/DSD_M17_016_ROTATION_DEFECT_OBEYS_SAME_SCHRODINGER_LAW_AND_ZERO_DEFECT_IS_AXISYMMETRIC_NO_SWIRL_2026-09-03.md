# DSD M17-016 — The horizontal rotation defect obeys the same Schrödinger law; zero defect is the axisymmetric no-swirl firewall

Date: 2026-09-03
Canonical ID: **M17-016**

Status: **INTERNAL HIGHER-JET AXISYMMETRY CLASSIFIER / FOR A VERTICAL GREAT-CIRCLE FILAMENT CENTERED ON THE `x_3` AXIS, DEFINE THE HORIZONTAL ROTATION GENERATOR `L=x_1 partial_2-x_2 partial_1` AND THE ANGULAR DEFECT `chi=Lq`. BECAUSE `L` COMMUTES WITH THE FULL LAPLACIAN AND `Delta q=F(q,x_3,theta)`, THE DEFECT SATISFIES THE SAME REAL-POTENTIAL EQUATION `Delta chi=kappa chi`. IF `chi` VANISHES IDENTICALLY, THEN `q` AND `U_3=G(q,x_3,theta)` ARE AXISYMMETRIC; THE RECONSTRUCTION LAW MAKES `L phi` INDEPENDENT OF `x_3`, WHILE INCOMPRESSIBILITY MAKES IT HORIZONTALLY HARMONIC. FINITE THREE-DIMENSIONAL ENERGY/DECAY THEN ELIMINATES A NONZERO `x_3`-INDEPENDENT SWIRL COMPONENT, SO `L phi=0` AND THE VELOCITY IS AXISYMMETRIC WITHOUT SWIRL. THUS `chi=0` IS EXACTLY THE LOCAL/GLOBAL FIREWALL CONDITION WITHIN THIS CENTERED VERTICAL BRANCH. A CONFORMAL POSITIVE NODAL CORE WITH `chi != 0` MUST HAVE A FINITE HIGHER-ORDER ANGULAR JET; UNDER COMPACTNESS AND UNIFORM SEPARATION FROM THE FIREWALL, ITS ORDER AND JET SIZE ARE UNIFORMLY CONTROLLED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Candidate symmetry axis and rotation generator

Work on a vertical regular winding filament and center the horizontal coordinates so that the filament is

\[
\Gamma=\{x_1=x_2=0\}.
\]

Define the generator of rotations about the `x_3` axis:

\[
\boxed{
\mathcal L
:=
x_1\partial_2-x_2\partial_1.
}
\]

For any scalar `f`,

\[
\mathcal Lf=0
\]

means that `f` is invariant under horizontal rotations, hence depends only on

\[
r=\sqrt{x_1^2+x_2^2}
\]

and `x_3` locally/globally on connected regions.

Define the streamfunction angular defect

\[
\boxed{
\chi:=\mathcal Lq.
}
\]

---

## 2. Rotation commutes with the semilinear operator

The Euclidean Laplacian is rotation invariant, so

\[
[\Delta,\mathcal L]=0.
\]

M17-004 gives

\[
\Delta q=F(q,x_3,\theta).
\]

Apply `mathcal L`:

\[
\Delta(\mathcal Lq)
=
\mathcal L(F(q,x_3,\theta)).
\]

Since `mathcal L x_3=0` and `mathcal L theta=0`,

\[
\mathcal L F
=F_q\mathcal Lq.
\]

Using

\[
\kappa=F_q,
\]

we obtain the exact defect equation

\[
\boxed{
\Delta\chi
=\kappa\chi.
}
\]

Thus higher-order horizontal non-axisymmetry is itself governed by the same real-potential Schrödinger operator as the great-circle vorticity components.

---

## 3. If chi = 0, q is axisymmetric

Suppose

\[
\boxed{\chi\equiv0.}
\]

Then

\[
q=q(r,x_3,\theta).
\]

Because

\[
U_3=G(q,x_3,\theta),
\]

we immediately get

\[
\boxed{
\mathcal LU_3
=G_q\chi
=0.
}
\]

Hence the vertical velocity component is also axisymmetric.

---

## 4. Angular defect of the horizontal velocity potential

Recall

\[
U_h=\nabla_h\phi
\]

and

\[
\partial_3\phi
=G(q,x_3,\theta)-q.
\]

Define

\[
\boxed{
\psi:=\mathcal L\phi.
}
\]

Apply `mathcal L` to the reconstruction law:

\[
\partial_3\psi
=
(G_q-1)\chi.
\]

Therefore if

\[
\chi=0,
\]

then

\[
\boxed{
\partial_3\psi=0.
}
\]

So the angular potential defect is independent of `x_3`.

---

## 5. Incompressibility makes psi horizontally harmonic

Incompressibility in the M17-004 representation is

\[
\Delta_h\phi+\partial_3U_3=0.
\]

Apply `mathcal L` and use commutation with the horizontal Laplacian:

\[
\Delta_h\psi
+\partial_3(\mathcal LU_3)=0.
\]

When `chi=0`,

\[
\mathcal LU_3=0,
\]

so

\[
\boxed{
\Delta_h\psi=0.
}
\]

Thus `psi` is simultaneously

1. independent of `x_3`;
2. harmonic in `(x_1,x_2)`.

---

## 6. Finite three-dimensional energy eliminates the residual angular mode

In polar coordinates,

\[
\psi=\partial_\theta\phi.
\]

The horizontal azimuthal velocity is

\[
U_\theta
=\frac1r\partial_\theta\phi
=\frac{\psi(r,\theta,\theta_{sim})}{r}.
\]

But `psi` is independent of the physical axial coordinate `x_3`.
If `psi/r` were nonzero on any horizontal set of positive measure, then the corresponding azimuthal kinetic-energy contribution would repeat unchanged for every `x_3`, giving infinite three-dimensional energy.

The retained finite-energy/decay class therefore forces

\[
\boxed{
\psi=0.
}
\]

Hence

\[
\boxed{
\mathcal L\phi=0.
}
\]

So `phi` is axisymmetric and

\[
U_h=\nabla_h\phi
\]

is purely radial in the horizontal plane.

Together with axisymmetric `U_3`, this gives

\[
\boxed{
U
=
u_r(r,x_3,\theta)e_r
+
u_3(r,x_3,\theta)e_3,
\qquad
U_\theta=0.
}
\]

This is exactly the axisymmetric no-swirl form of the M17-008 firewall.

---

## 7. Exact firewall statement

Within the centered vertical great-circle branch and retained finite-energy/decay class,

\[
\boxed{
\chi=\mathcal Lq\equiv0
\Longrightarrow
\text{axisymmetric no-swirl velocity}.
}
\]

The converse is immediate for an axisymmetric no-swirl field:

\[
q=q(r,x_3,\theta)
\Longrightarrow
\chi=0.
\]

Thus, within this branch,

\[
\boxed{
\chi\equiv0
\iff
G_{axis/no\text{-}swirl}.
}
\]

The axisymmetric firewall is no longer only a qualitative comparison class; it is the exact zero set of a scalar angular-defect field.

---

## 8. Conformal positive core and higher-order non-axisymmetry

Suppose the first-order nodal shape is conformal positive as in M17-014.
Then

\[
Q=\nabla_h^2q|_\Gamma=cI_2,
\qquad c\neq0.
\]

At the axis,

\[
\nabla_hq=0.
\]

The constant, linear, and isotropic quadratic Taylor parts of `q` are rotationally invariant, so `mathcal L` annihilates them.
Therefore

\[
\boxed{
\operatorname{ord}_\Gamma\chi\ge3
}
\]

whenever `chi` is nonzero.

Hence a conformal first-order core that is nevertheless non-axisymmetric must reveal that non-axisymmetry at a finite higher angular jet.

---

## 9. Infinite-order angular flatness implies the firewall

Because `chi` is analytic and satisfies

\[
\Delta\chi=\kappa\chi,
\]

if every spatial jet of `chi` vanishes at one point of the connected analytic domain, then

\[
\boxed{
\chi\equiv0.
}
\]

By Section 7 this means the state lies in the axisymmetric no-swirl firewall.

Therefore a genuinely non-axisymmetric analytic state cannot hide its angular defect to infinite order at the regular axis.

---

## 10. Compact-hull finite angular-jet dichotomy

Consider a compact recurrent hard subhull of centered vertical conformal-core states.
There are two possibilities.

### A. Axisymmetric accumulation
There exists a sequence whose angular defect tends to zero in every fixed `C^m` norm on the core.
Any compact limit then satisfies

\[
\chi=0
\]

and lies in the axisymmetric no-swirl firewall.

### B. Uniformly separated non-axisymmetric branch
Assume instead the branch is uniformly separated from the firewall in some fixed core norm:

\[
\|\chi\|_{X(core)}\ge\varepsilon_A>0.
\]

If the vanishing order of `chi` on the filament were unbounded, compactness would produce a limit with all jets of `chi` zero at the axis.
Analyticity would force

\[
\chi\equiv0,
\]

contradicting the uniform separation.

Hence there exist

\[
\boxed{
m_A<\infty,
\qquad
c_A>0
}
\]

such that on the uniformly non-axisymmetric separated branch, some angular-defect jet of order at most `m_A` obeys

\[
\boxed{
\max_{1\le m\le m_A}
|\nabla^m\chi|_\Gamma
\ge c_A.
}
\]

For a conformal core the first possible nonzero order is at least three.

---

## 11. DSD analysis

The axisymmetry question is converted from a global verbal classification into a scalar descriptor:

\[
\boxed{
\chi=\mathcal Lq.
}
\]

Its meanings are:

- `chi=0`: axisymmetric no-swirl firewall;
- `chi!=0`: genuine angular defect;
- finite `ord chi`: first resolved higher-jet non-axisymmetric channel;
- unbounded `ord chi` under compactness: accumulation onto the regular firewall.

This creates a clean describability hierarchy from first-order nodal shape to higher angular jets.

---

## 12. DSD audit

### Audit A — assuming conformal Hessian means axisymmetry
Rejected.
A conformal quadratic core may have cubic or higher angular defects.

### Audit B — using only local chi=0 at one order
Rejected.
Axisymmetry requires the full analytic defect to vanish, not merely its first few jets.

### Audit C — declaring approach to axisymmetry contradictory
Rejected.
Axisymmetric no-swirl is a known regular firewall; accumulation onto it is an allowed regularization channel.

### Audit D — energy step
The elimination of `psi=Lphi` uses the retained whole-space finite-energy/decay class. Without such a global condition, an `x_3`-independent harmonic angular potential mode would require a separate treatment.

### Audit E — proof status
The nonzero angular-defect branch remains open.

---

## 13. Updated conformal-core branch

The positive-index conformal class now splits as

\[
\boxed{
G_{conf+}^{core}
\Longrightarrow
G_{axis/no\text{-}swirl}
\ \lor\ 
A_{high\text{-}jet}^{nonaxis}.
}
\]

On a compact branch uniformly separated from the firewall,

\[
\boxed{
A_{high\text{-}jet}^{nonaxis}
\Longrightarrow
\text{finite-order angular defect with a uniform jet floor}.
}
\]

Thus the old vague "higher-jet axisymmetry test" is reduced to a finite-order analytic defect problem.

---

## 14. Next target

The rank-one genuinely non-axisymmetric problem now consists of three explicit regular classes:

\[
\boxed{
G_{index-}^{core},
\qquad
G_{aniso+}^{core},
\qquad
A_{high\text{-}jet}^{nonaxis}.
}
\]

Each must be combined with the M17-013 label-area hysteresis and M17-012 positive-sheath/negative-payer requirement.

The most promising next calculation is to derive the material/elliptic evolution of the angular defect `chi` and determine whether a recurrent finite-order `chi` jet can remain uniformly nonzero while the `kappa` label flow repeatedly executes the required expansion/contraction hysteresis.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
