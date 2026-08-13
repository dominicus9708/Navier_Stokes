# Bounded V2 channel implies strong local `L2_t H1_x` vorticity compactness

Date: 2026-08-13

Status: **DERIVED CONDITIONAL-ON-BOUNDED-BLOCK COMPACTNESS LEMMA / STANDARD ELLIPTIC + AUBIN-LIONS MECHANISM**.

The compactness-interpolation rigidity gap previously assumed strong local `H1` compactness of normalized vorticity.  On the branch where the buffered normalized V2 channel is uniformly bounded, that compactness follows from the vorticity equation and standard compactness machinery.

The lemma is local and requires bounds on a fixed **buffered normalized cylinder**, not merely on the final dangerous set.

---

## 1. Buffered normalized block

Let

\[
Q_R=B_R\times(-T,0)
\]

and choose

\[
1<R_0<R.
\]

Assume uniformly in `j`

\[
\boxed{
\|U_j\|_{L_s^\infty L_y^2(Q_R)}
\le M_U,
}
\]

\[
\boxed{
\|\Omega_j\|_{L_s^\infty L_y^2(Q_R)}
\le M_\Omega,
}
\]

and the buffered V2 bound

\[
\boxed{
\|\Delta\Omega_j\|_{L^2(Q_R)}
\le M_2.
}
\]

The fields satisfy the normalized vorticity equation

\[
\partial_s\Omega_j
=\nu\Delta\Omega_j
-\nabla\cdot
(U_j\otimes\Omega_j-\Omega_j\otimes U_j).
\]

---

## 2. Interior `H2` reserve

A standard interior elliptic estimate on `B_R` gives, for each time,

\[
\|\Omega_j(s)\|_{H^2(B_{R_0})}
\le
C_{R_0,R}
\left[
\|\Delta\Omega_j(s)\|_{L^2(B_R)}
+\|\Omega_j(s)\|_{L^2(B_R)}
\right].
\]

Integrating in time,

\[
\boxed{
\Omega_j
\text{ is uniformly bounded in }
L_s^2H_y^2(Q_{R_0}).
}
\]

In three dimensions,

\[
H^2(B_{R_0})\hookrightarrow L^\infty(B_{R_0}),
\]

so

\[
\boxed{
\Omega_j
\text{ is uniformly bounded in }
L_s^2L_y^\infty(Q_{R_0}).
}
\]

---

## 3. Time derivative in `L2 H^-1`

On a still smaller ball `B_{R_1}` with `R_1<R_0`, use a fixed cutoff to avoid boundary issues.

The viscous part obeys

\[
\nu\Delta\Omega_j
\in L_s^2L_y^2
\hookrightarrow L_s^2H_y^{-1}.
\]

For the nonlinear tensor,

\[
\|U_j\otimes\Omega_j\|_{L_y^2}
\le
\|U_j\|_{L_y^2}
\|\Omega_j\|_{L_y^\infty}.
\]

Thus

\[
U_j\otimes\Omega_j,
\quad
\Omega_j\otimes U_j
\]

are uniformly bounded in

\[
L_s^2L_y^2(Q_{R_0}).
\]

Taking one divergence,

\[
\boxed{
\partial_s\Omega_j
\text{ is uniformly bounded in }
L_s^2H_y^{-1}(Q_{R_1}).
}
\]

Cutoff commutators are lower order and are controlled by the same buffered `U_j`, `Omega_j`, and `H2` bounds.

---

## 4. Strong `L2 H1` compactness

On the bounded interior domain,

\[
H^2(B_{R_1})
\Subset
H^1(B_{R_1})
\hookrightarrow
H^{-1}(B_{R_1}).
\]

Therefore the standard Aubin--Lions--Simon compactness mechanism gives a subsequence such that

\[
\boxed{
\Omega_j
\to
\Omega_\infty
\quad\text{strongly in }
L_s^2H_y^1(Q_{R_1}).
}
\]

After another subsequence, strong `H1` convergence holds for almost every normalized time.

---

## 5. Consequence for the magnitude-rigidity gap

Let

\[
f_j(s)=\chi|\Omega_j(s)|
\]

for a cutoff supported inside `B_{R_1}`.

The Lipschitz property of the modulus and the strong `H1` convergence above give the required compactness reserve for the scalar magnitude profile, after selecting almost-everywhere times and using the cutoff.

Therefore, on the V2-bounded branch, the previous compactness-rigidity statement can be used without separately postulating strong spatial `H1` compactness:

\[
\boxed{
\text{nontrivial persistent cutoff core}
+\text{bounded buffered V2}
\Longrightarrow
\liminf\chi_{\rm mag}>0
}
\]

along any source-saturation subsequence for which the relevant time slices are selected.

The time-selection/persistence step is supplied separately by the localized enstrophy temporal-concentration gate on the bounded source/shell branch.

---

## 6. Complementary branch

If the buffered V2 channel is not uniformly bounded,

\[
\boxed{
\|\Delta\Omega_j\|_{L^2(Q_R)}\to\infty
}
\]

along every candidate subsequence, then the compactness branch is abandoned and the route records an explicit normalized second-vorticity-derivative concentration.

Hence

\[
\boxed{
\text{V2 concentration}
\quad\text{or}\quad
\text{strong local }L^2H^1\text{ vorticity compactness}.
}
\]

This is exactly the compactness-or-concentration structure needed by the current proof map.

---

## 7. Claim boundary

This lemma does not assert that the V2 bound is automatic for arbitrary Navier--Stokes amplification windows.  It states that **if** the normalized buffered V2 channel stays bounded, the strong vorticity compactness needed by the magnitude-interpolation rigidity argument follows from standard PDE compactness.

Status: **V2-BOUNDED COMPACTNESS BRANCH CLOSED / V2-UNBOUNDED BRANCH EXPLICIT**.
