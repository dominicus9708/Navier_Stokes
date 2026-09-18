# M19-406 — Exact homogeneous zero-force stationary endpoint is externally rigid; hard survivor must be genuinely log-dilation dependent

Date: 2026-09-18

Status: **EXTERNAL CLASSIFICATION PRUNING / ŠVERÁK'S CLASSIFICATION OF SMOOTH (-1)-HOMOGENEOUS STATIONARY 3D NAVIER--STOKES FIELDS IDENTIFIES THE EXACT SELF-SIMILAR CLASS WITH THE LANDAU FAMILY. LANDAU FIELDS ARE THE SCALE-CRITICAL POINT-FORCE SOLUTIONS; THE ZERO-FORCE MEMBER IS THE TRIVIAL FIELD. THEREFORE, ON THE SMOOTH EXACTLY (-1)-HOMOGENEOUS TERMINAL BRANCH, \`kappa_force=0\` IMPLIES \`A=0\`. A NONTRIVIAL ZERO-FORCE HARD TERMINAL SURVIVOR MUST THUS ESCAPE EXACT HOMOGENEITY: IT MUST RETAIN GENUINE LOG-RADIUS/DILATION DEPENDENCE, LOSE THE SMOOTH-SPHERE CLASS, OR EXIT THROUGH AN ALREADY TYPED NONSTATIONARY/REPRESENTATION BRANCH. THIS DOES NOT CLASSIFY GENERAL DISCRETELY SELF-SIMILAR OR APERIODIC RECURRENT LOG-DILATION PROFILES. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Terminal critical ansatz

The stationary hard tail is written

\[
u(x)
=
\frac1r A(q,\omega),
\qquad
p(x)
=
\frac1{r^2}P(q,\omega),
\qquad
q=\log r.
\]

The exact homogeneous subbranch is

\[
\boxed{
\partial_qA=0,
\qquad
\partial_qP=0.
}
\]

Then

\[
u(\lambda x)
=
\lambda^{-1}u(x),
\]

so the field is exactly homogeneous of degree \(-1\).

---

## 2. External classification theorem

Šverák's Landau classification, as used explicitly in later stationary self-similar literature, states that every smooth exactly self-similar / degree-\(-1\) homogeneous stationary Navier--Stokes solution in

\[
\mathbb R^3\setminus\{0\}
\]

belongs to the Landau family.

The theorem concerns the smooth angular class on the sphere.

It does **not** classify arbitrary log-periodic, discretely self-similar, or aperiodic recurrent dependence in

\[
q=\log r.
\]

This scope distinction is permanent.

---

## 3. Landau family and point-force parameter

The Landau solutions solve the punctured stationary equation classically and, distributionally on all of \(\mathbb R^3\), carry a point-force vector:

\[
-\Delta u
+
u\cdot\nabla u
+
\nabla p
=
b\,\delta_0,
\qquad
\nabla\cdot u=0.
\]

The nontrivial Landau members correspond to

\[
b\ne0.
\]

The zero-force member

\[
b=0
\]

is the trivial field.

In the notation of M19-272--274, the terminal stress-flux coefficient is exactly this point-force vector:

\[
\boxed{
\kappa_{\rm force}
=
\int_{S_r}\mathbb Tn\,dS.
}
\]

Thus on the exactly homogeneous smooth branch,

\[
\boxed{
\kappa_{\rm force}=0
\Longrightarrow
u\equiv0.
}
\]

---

## 4. Exact homogeneous branch closure

Assume

1. stationary terminal profile;
2. smoothness on \(\mathbb R^3\setminus\{0\}\);
3. exact degree-\(-1\) homogeneity;
4. zero terminal point force.

Then Šverák's classification gives a Landau field, and zero force selects the trivial member.

Therefore

\[
\boxed{
G_{\rm stationary}^{hom}
+
G_{\rm force=0}
\Longrightarrow
A\equiv0.
}
\]

This closes the smooth exact-homogeneous zero-force terminal branch.

---

## 5. Nonzero-force homogeneous branch is not a contradiction

If

\[
\kappa_{\rm force}\ne0,
\]

the classification returns a nontrivial Landau solution.

This is fully compatible with the critical scaling

\[
u\sim r^{-1},
\qquad
p\sim r^{-2}.
\]

Hence exact homogeneity by itself does not close the stationary hard tail.

It reduces it to the explicit point-force branch already isolated by M19-272--274.

Therefore the homogeneous stationary split is

\[
\boxed{
\begin{aligned}
\kappa_{\rm force}=0
&\Rightarrow
u=0,\\
\kappa_{\rm force}\ne0
&\Rightarrow
\text{Landau point-force endpoint}.
\end{aligned}
}
\]

The second requires force cancellation / stress tightness upstream if it is to be eliminated.

---

## 6. Consequence for the zero-force hard survivor

Suppose the stationary hard terminal profile is nontrivial and

\[
\kappa_{\rm force}=0.
\]

Then it cannot be both smooth and exactly homogeneous.

Hence at least one of the following must hold:

\[
\boxed{
\partial_qA\not\equiv0
}
\]

(genuine dilation dependence),

or

\[
\boxed{
G_{\rm angular/sphere}^{singular}
}
\]

(loss of the smooth angular class),

or an already typed

\[
\boxed{
G_{\rm nonstationary/representation/tail}.
}
\]

On the retained smooth compact stationary branch, the surviving option is therefore genuine log-radius dynamics.

---

## 7. Relation to recurrent dilation hull

The M5-482--485 terminal construction produces a compact dilation hull.

M19-406 shows that a nontrivial **zero-force** invariant measure cannot collapse to a fixed point corresponding to an exactly homogeneous smooth state.

The surviving zero-force hull must instead carry nontrivial dilation dynamics:

\[
\boxed{
A(q+\tau,\omega)
\not\equiv
A(q,\omega)
}
\]

for some shifts \(\tau\).

This may be

1. periodic in \(q\) (DSS / log-periodic);
2. quasiperiodic;
3. aperiodic recurrent.

The external homogeneous classification does not distinguish or remove these.

---

## 8. DSS/log-periodic firewall

Later work on stationary discretely self-similar solutions, including Kwon--Tsai, investigates restricted axisymmetric bifurcation around Landau solutions and reports rigorous partial non-bifurcation results together with numerical evidence in that setting.

This is **not** a general theorem that every smooth stationary DSS solution is Landau.

Therefore one must not write

\[
\text{stationary DSS}
\Rightarrow
\text{Landau}
\]

as a certified theorem.

The general log-periodic / recurrent zero-force endpoint remains open in the present proof architecture.

---

## 9. Revised stationary zero-force target

The broad gate

\[
\mathcal T_{tail}^{zero-force-rigidity}
\]

can now be sharpened to

\[
\boxed{
\mathcal T_{dil}^{nonconstant}:
\text{exclude nontrivial smooth zero-force stationary recurrent dilation hulls with genuine }q\text{-dependence}.
}
\]

Equivalently,

\[
\boxed{
\text{zero force}
+
\text{smooth stationary hard tail}
+
\text{nontriviality}
\Longrightarrow
\text{nonconstant dilation dynamics}.
}
\]

The remaining problem is therefore dynamical/rigidity in log radius, not exact homogeneous classification.

---

## 10. Relation to M19-405

M19-405 identifies the same \(1/r\) corridor as the common obstruction to

- GMS subcritical palinstrophy transfer;
- terminal stress tightness;
- weak-\(L^3\) stationary rigidity.

M19-406 removes the easiest zero-force endpoint inside that corridor:

\[
\boxed{
\text{exactly homogeneous zero-force}
}
\]

is not a survivor.

Thus the common critical-tail obstruction becomes more specific:

\[
\boxed{
\text{nonzero Landau force}
\quad\lor\quad
\text{genuinely log-dependent zero-force recurrent tail}.
}
\]

---

## 11. External-dependency firewall

This module relies on the external classification only for the exact smooth degree-\(-1\) homogeneous stationary class.

It does not import a theorem for:

- arbitrary weak-\(L^3\) stationary fields;
- angularly singular homogeneous fields;
- general DSS stationary fields;
- arbitrary recurrent \(A(\log r,\omega)\);
- nonstationary ancient tails.

Those remain separate branches.

---

\[
\boxed{\text{M19-406 COMPLETE; THE SMOOTH EXACT-HOMOGENEOUS ZERO-FORCE ENDPOINT IS CLOSED, LEAVING NONZERO LANDAU FORCE OR GENUINE LOG-DILATION DYNAMICS.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
