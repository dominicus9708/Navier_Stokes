# DSD M5-194I — Type-I Limit to Šverák Prerequisite Ledger

Date: 2026-08-29

Parent: `DSD_M5_194H_STATIONARY_MINUS_ONE_HOMOGENEOUS_TAIL_RIGIDITY_AUDIT_2026-08-29.md`

Status: **NEGATIVE SHORTCUT FIREWALL / THE CURRENT FIRST-HITTING TYPE-I ROUTE CAN PRODUCE A NONTRIVIAL ANCIENT SUITABLE LIMIT ON THE MORREY CORRIDOR, WITH FIXED-CENTER PRESSURE CONTROL AND CONTINUOUS BACKWARD VORTICITY TYPE-I DECAY, BUT THESE RESULTS DO NOT ESTABLISH PHYSICAL-TIME STATIONARITY OR EXACT SPATIAL `(-1)` HOMOGENEITY / THEREFORE ŠVERÁK'S STATIONARY HOMOGENEOUS CLASSIFICATION CANNOT YET BE APPLIED TO THE ACTUAL ANCIENT SURVIVOR / SUBSEQUENTIAL COMPACTNESS DOES NOT IMPLY DILATION INVARIANCE / A TIME SLICE IS NOT A STATIONARY NS SOLUTION UNLESS `partial_t U=0` / THE NEXT TARGET IS THE SCALING-DEFECT AND TIME-DEFECT EQUATIONS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-194H established a strong rigidity statement for an exact stationary smooth `(-1)`-homogeneous Navier--Stokes profile:

- the nonzero purely tangential branch is impossible;
- every nontrivial smooth stationary `(-1)`-homogeneous profile on `R^3\{0}` lies in the Landau class;
- an additional unforced distributional condition across the origin can eliminate the Landau point-force branch.

The present audit asks whether the Type-I compactness construction already available in this repository satisfies the hypotheses needed to invoke that classification.

The answer is **not yet**.

Several compactness and pressure prerequisites are now available, but the two decisive rigidity hypotheses -- stationarity and exact homogeneity -- are absent.

---

## 2. Repository inputs audited

The following earlier records are relevant.

### 2.1 First-hitting Type-I compactness bridge

`TYPEI_COMPACTNESS_BRIDGE_2026-08-20.md` introduced fixed-scale fields

\[
U_j(y,\tau)
=r_j u(X_j+r_jy,t_j+r_j^2\tau),
\qquad r_j=W_j^{-1/2},
\]

and the scale-invariant suitable-solution quantities `A,C,D,E`.

The original note correctly marked the bridge conditional on center nesting, local derivative compactness, pressure gauge control, and uniform local Type-I bounds.

### 2.2 Exact Type-I scaling of the tower

`TYPEI_TOWER_SCALING_2026-08-20.md` showed that the geometric first-hitting hierarchy has the exact **size scaling**

\[
|U|\sim R^{-1},
\qquad
|\Omega|,|\Sigma|\sim R^{-2},
\qquad
|P|\sim R^{-2}
\]

across the corresponding backward stages.

This is a scale ledger for amplitudes and local quantities. It is not the functional identity

\[
U(\lambda x)=\lambda^{-1}U(x).
\]

The distinction is central to the present audit.

### 2.3 Fixed-center pressure

`TYPEI_PRESSURE_FROM_VELOCITY_TOWER_2026-08-20.md` removed the accelerated-frame affine-pressure issue by working in the fixed limiting-center frame and using the canonical whole-space pressure

\[
P=\mathcal R_i\mathcal R_j(U_iU_j)
\]

modulo a function of time.

Thus pressure compactness is not an independent obstruction once the local Type-I velocity quantities are controlled.

### 2.4 Ancient extraction on the Morrey corridor

`ANCIENT_LOCAL_COMPACTNESS_FROM_MORREY_WITHOUT_GLOBAL_Z_2026-08-24.md` derived, on every fixed cylinder, uniform local `A/E/C/D` bounds from the centered Morrey energy corridor and the first-hitting vorticity cap.

It then obtained, after a diagonal subsequence, an ancient suitable solution

\[
U_\infty
\quad\text{on}\quad
\mathbb R^3\times(-\infty,0],
\]

with nontrivial terminal vorticity

\[
|\Omega_\infty(y_*,0)|=1.
\]

This is a genuine compactness gain, but the output is a time-dependent ancient solution class.

### 2.5 Continuous backward Type-I vorticity decay

`ANCIENT_CONTINUOUS_BACKWARD_VORTICITY_TYPEI_2026-08-24.md` strengthened the first-hitting inheritance to

\[
\boxed{
\|\Omega_\infty(\tau)\|_\infty
\le
\min\left\{1,\frac{K_I}{|\tau|}\right\},
\qquad \tau<0.
}
\]

Hence

\[
\|\Omega_\infty(\tau)\|_\infty\to0
\qquad(\tau\to-\infty).
\]

Again, this is a dynamic Type-I statement. It does not imply stationarity.

---

## 3. Šverák prerequisite ledger

The exact stationary `(-1)`-homogeneous classification requires a much more rigid object than an arbitrary ancient Type-I solution.

| Requirement | Current status | Audit reason |
|---|---|---|
| Ancient/local compact limit | **YES on the established Morrey corridor** | fixed-cylinder `A/E/C/D` bounds and diagonal suitable-solution extraction are already recorded |
| Nontriviality | **YES on that corridor** | first-hitting normalization passes as `|Omega(y_*,0)|=1` under the recorded local derivative compactness |
| Fixed-center pressure control | **YES locally** | canonical Riesz pressure and dyadic remote-pressure control are already recorded |
| Local smoothness away from any possible singular concentration | **AVAILABLE conditionally from the no-H/local-regularity corridor** | sufficient for local operator calculations, but not a homogeneity statement |
| Physical-time stationarity `partial_tau U=0` | **NO** | no repository result forces the ancient limit to be independent of `tau` |
| Exact spatial `(-1)` homogeneity `U(lambda y,tau)=lambda^{-1}U(y,tau)` | **NO** | Type-I size bounds and geometric stage scaling do not imply this identity |
| Unique tangent under every dilation | **NO** | only subsequential compactness is established; uniqueness of the blow-up/tangent profile is not |
| Smooth stationary profile on the full sphere | **NO AS A ŠVERÁK INPUT** | local smoothness of a dynamic ancient solution is not a stationary sphere profile |
| Unforced stationary distributional equation across the origin for a homogeneous limit | **NO SUCH LIMIT HAS BEEN PRODUCED** | the Landau point-force issue becomes relevant only after a stationary homogeneous limiting passage |

The decisive blockers are therefore

\[
\boxed{
\partial_\tau U=0
}
\]

and

\[
\boxed{
U+y\cdot\nabla U=0.
}
\]

Neither follows from the existing Type-I bounds.

---

## 4. Type-I scaling is not exact homogeneity

The repository's first-hitting scaling gives estimates of the form

\[
|U(y,\tau)|\lesssim |y|^{-1}
\]

in the appropriate critical-tail regime, together with matching scale-invariant `A,C,D,E` behavior.

Exact `(-1)` homogeneity is instead the group identity

\[
\boxed{
U(\lambda y)=\lambda^{-1}U(y)
\quad\text{for every }\lambda>0.
}
\]

Differentiating in `lambda` at `lambda=1` gives the infinitesimal condition

\[
\boxed{
\mathcal H U
:=U+y\cdot\nabla U
=0.
}
\]

A bound

\[
|U|\le C|y|^{-1}
\]

places `U` in the same scaling **class**, but it gives no control of `mathcal H U`.

For example, a log-radially modulated critical field

\[
U(y)=\frac1{|y|}\Phi(-\log|y|,\hat y)
\]

has the exact critical amplitude while

\[
\mathcal H U
=-\frac1{|y|}\partial_s\Phi(s,\hat y),
\qquad s=-\log|y|,
\]

which need not vanish.

Thus

\[
\boxed{
\text{critical size}\not\Rightarrow\text{homogeneity}.
}
\]

---

## 5. Subsequence compactness is not dilation invariance

Let the Navier--Stokes scaling be

\[
U^{(\lambda)}(y,\tau)
=\lambda U(\lambda y,\lambda^2\tau).
\]

Suppose a sequence of rescalings has a subsequence converging to `U_infty`.

Compactness alone says only that scaled sequences admit limit points. It does **not** imply

\[
U_\infty^{(\lambda)}=U_\infty
\]

for every `lambda`.

To deduce exact scale invariance one needs an additional mechanism such as

1. uniqueness of the tangent/blow-up limit under all dilation subsequences;
2. a monotonicity formula whose equality case forces self-similarity;
3. direct vanishing of the scaling defect;
4. an equivalent rigidity theorem.

No such mechanism has yet been established in the present branch.

Therefore the implication

\[
\boxed{
\text{Type-I compactness}
\Longrightarrow
\text{exact homogeneous limit}
}
\]

is closed as an unjustified shortcut.

---

## 6. An ancient time slice is not a stationary Navier--Stokes solution

The ancient limit satisfies

\[
\partial_\tau U
-\Delta U
+(U\cdot\nabla)U
+\nabla P=0.
\]

Fixing one time `tau_0` gives

\[
-\Delta U(\tau_0)
+(U(\tau_0)\cdot\nabla)U(\tau_0)
+\nabla P(\tau_0)
=
-\partial_\tau U(\tau_0).
\]

Hence the time slice is a stationary solution only if

\[
\boxed{
\partial_\tau U(\tau_0)=0.
}
\]

The continuous backward decay

\[
\|\Omega(\tau)\|_\infty\lesssim|\tau|^{-1}
\]

does not imply this derivative vanishes at any finite time.

Consequently one cannot apply the stationary Landau/Šverák classification independently to each ancient time slice.

---

## 7. The origin-defect issue must be postponed, not assumed away

The extracted ancient solution itself is obtained as a local whole-space suitable solution on `R^3 x (-infinity,0]` in the recorded Morrey compactness branch.

But the Šverák route would require an **additional** limiting operation that produces a stationary exactly homogeneous profile.

Convergence only on annuli

\[
\mathbb R^3\setminus\{0\}
\]

does not by itself determine the distributional equation at the origin.

A concentration defect can survive there. The Landau family is the canonical warning: it is smooth on `R^3\{0}` but carries a point-force distribution at the origin.

Therefore, if a future stationary homogeneous tangent is produced, the audit must separately verify the momentum-flux limit around shrinking spheres or an equivalent distributional no-defect condition before using the stronger `only zero` corollary.

---

## 8. DSD verdict

### ESTABLISHED

On the current no-H/no-turnover/Morrey corridor, the proof tree has enough local control for a nontrivial ancient Type-I compact limit, including fixed-center pressure and continuous backward vorticity decay.

This significantly narrows the endgame.

### CLOSED AS INVALID SHORTCUTS

The following implications are not justified and are now explicitly closed:

\[
\boxed{
\text{Type-I size scaling}
\Rightarrow
\text{exact `(-1)` homogeneity}
}
\]

and

\[
\boxed{
\text{ancient compact limit}
\Rightarrow
\text{stationary limit}
}
\]

and

\[
\boxed{
\text{subsequential blow-up convergence}
\Rightarrow
\text{unique dilation-invariant tangent}.
}
\]

Therefore M5-194H cannot yet be used to eliminate the actual Type-I ancient survivor.

### SURVIVING ROUTES

1. prove vanishing of the time defect `partial_tau U`;
2. prove vanishing of the spatial homogeneity defect `U+y·nabla U`;
3. prove uniqueness of dilation tangents and infer scale invariance;
4. obtain a parabolic/self-similar rigidity theorem suited to the actual ancient Type-I class rather than forcing a stationary theorem onto it;
5. if those fail, return to the generic critical-drift backward-uniqueness/matrix-symmetrizer route.

---

## 9. Next audit target

Introduce two distinct defects and do not conflate them:

\[
\boxed{
\mathcal T[U]:=\partial_\tau U
}
\]

and

\[
\boxed{
\mathcal H[U]:=U+y\cdot\nabla U.
}
\]

Stationary exact `(-1)` homogeneity requires

\[
\mathcal T[U]=0,
\qquad
\mathcal H[U]=0.
\]

The Navier--Stokes scaling symmetry naturally combines them into the parabolic scaling defect

\[
\boxed{
\mathcal Z[U]
:=U+y\cdot\nabla U+2\tau\partial_\tau U.
}
\]

The next calculation should derive the exact PDE solved by `mathcal Z[U]` and by `partial_tau U`, then test whether the inherited ancient Type-I/Morrey bounds place either defect in a Liouville or backward-uniqueness class.
