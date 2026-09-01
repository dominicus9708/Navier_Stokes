# DSD M5-483 — Lift terminal dilation genealogy to a parabolic ancient dilation hull

Date: 2026-09-01

Status: **SPACE-TIME TAIL LIFT / THE M5-478 RECORD-SCALE ANCIENT CELLS SATISFY AN EXACT PARABOLIC DILATION GENEALOGY, SO THE BOUNDED COMPACT TAIL LANE OF M5-482 LIFTS FROM TERMINAL TIME SLICES TO A COMPLETE TWO-SIDED FAMILY OF NONTRIVIAL TYPE-I ANCIENT NAVIER--STOKES CELLS / A PERIODIC RETURN IN THIS LIFT IS EXACTLY A BACKWARD DISCRETELY SELF-SIMILAR NAVIER--STOKES SOLUTION; THE GENERAL NONZERO BACKWARD DSS PROBLEM IS KNOWN TO REMAIN OPEN AT THE WEAK CRITICAL ENDPOINT / THE APERIODIC DILATION HULL IS EVEN MORE GENERAL / THUS THE PRESENT PROOF ROUTE HAS REACHED A RECOGNIZED OPEN HARD CORE RATHER THAN A CLOSED LIOUVILLE CLASS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Space-time record cells

For every backward record radius `R_m`, define

\[
\boxed{
\mathcal V_m(y,s)
:=R_mV(R_my,R_m^2s),
}
\]

\[
\boxed{
\mathcal P_m(y,s)
:=R_m^2P(R_my,R_m^2s).
}
\]

Each solves unit-viscosity 3D Navier--Stokes for

\[
s<L_*/R_m^2,
\]

so every fixed compact subset of `s<0` lies in the domain for late `m`.

M5-478 gives uniform Type-I vorticity/velocity bounds and a nontrivial old-carrier mark.

---

## 2. Exact parabolic dilation identity

Set

\[
\lambda_m:=R_{m+1}/R_m.
\]

Then

\[
\begin{aligned}
\mathcal V_{m+1}(y,s)
&=R_{m+1}V(R_{m+1}y,R_{m+1}^2s)\\
&=\lambda_mR_mV(R_m(\lambda_my),R_m^2(\lambda_m^2s))\\
&=\lambda_m
\mathcal V_m(\lambda_my,\lambda_m^2s).
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal V_{m+1}
=\mathscr D_{\lambda_m}\mathcal V_m,
}
\]

where

\[
\boxed{
(\mathscr D_\lambda U)(y,s)
:=\lambda U(\lambda y,\lambda^2s).
}
\]

Similarly

\[
\boxed{
\mathcal P_{m+1}(y,s)
=\lambda_m^2
\mathcal P_m(\lambda_my,\lambda_m^2s).
}
\]

This is exact Navier--Stokes parabolic scaling, not merely a terminal spatial relation.

---

## 3. Compactness of shifted cell families

On every compact cylinder

\[
K\Subset\mathbb R^3\times(-\infty,0),
\]

M5-478 gives uniform

\[
\|\Omega_m\|_\infty,
\qquad
\|\Omega_m\|_2,
\qquad
\|\mathcal V_m\|_\infty
\]

bounds depending only on the distance of `K` from `s=0`.

Interior parabolic regularity gives uniform higher derivative bounds on `K`.

Thus the family of ancient cells is precompact in the local smooth topology on `s<0`.

If compactness fails through spatial escape of the marked cell or through terminal/frequency defects, that failure is returned to the already typed strong/dynamic branches.

---

## 4. Complete two-sided parabolic genealogy

Choose `m_k -> infinity` and diagonalize over every fixed integer offset `n`.

After a subsequence,

\[
\mathcal V_{m_k+n}
\to
\mathcal U_n
\]

locally smoothly on `s<0`, and

\[
\lambda_{m_k+n}	o\lambda_n
\in[\lambda_-,\lambda_+].
\]

Passing to the exact dilation relation gives

\[
\boxed{
\mathcal U_{n+1}
=\mathscr D_{\lambda_n}\mathcal U_n,
\qquad n\in\mathbb Z.
}
\]

Every `mathcal U_n` is a Type-I ancient Navier--Stokes solution.

The old first-hitting carrier and no-defect compactness preserve a nontrivial marked member of the hull.

---

## 5. Periodic return gives exact backward DSS

Suppose for some `N>=1`

\[
\mathcal U_N=\mathcal U_0.
\]

Let

\[
\Lambda:=\prod_{n=0}^{N-1}\lambda_n>1.
\]

Iterating the genealogy gives

\[
\mathcal U_N
=\mathscr D_\Lambda\mathcal U_0.
\]

Hence

\[
\boxed{
\mathcal U_0(y,s)
=\Lambda
\mathcal U_0(\Lambda y,\Lambda^2s).
}
\]

This is precisely the definition of a backward `Lambda`-discretely self-similar Navier--Stokes solution.

Thus

\[
\boxed{
\text{periodic parabolic dilation hull}
\Longrightarrow
\text{backward DSS ancient NS}.
}
\]

---

## 6. Exact literature scope of the DSS endpoint

Classical backward continuously self-similar Leray profiles are excluded in broad integrability classes.

However the general existence/nonexistence problem for nonzero backward **discretely** self-similar Navier--Stokes solutions remains open at critical endpoints. Quantitative regularity literature explicitly records this as a long-standing open problem.

Known nonexistence results for asymptotically or locally DSS scenarios impose stronger assumptions such as strong `L3` profile integrability or specific decay.

The present surviving tail was derived precisely because global strong `L3` may fail through a critical `1/r`-type or dilation-hull tail.

Therefore those stronger DSS Liouville theorems cannot be imported silently.

---

## 7. Aperiodic return is a genuine broader endpoint

If the complete hull contains no periodic return, then the closure of

\[
\{\mathcal U_n:n\in\mathbb Z\}
\]

may support a compact aperiodic dilation dynamics.

Such an object is not excluded merely by compactness and Type-I bounds.

Hence the bounded compact tail endpoint has the space-time split

\[
\boxed{
E_{tail}^{compact}
\Longrightarrow
E_{DSS}^{backward}
\lor
E_{dil,aper}^{ancient}.
}

The second is more general than the classical backward DSS problem.

---

## 8. Relation to the original ratchet problem

The full chain is now

\[
\boxed{
\text{positive-density material ratchet}
\to
\text{marked finite-enstrophy ancient element}
\to
\text{backward record blow-down}
\to
\text{terminal critical Dirichlet tail}
\to
\text{parabolic dilation hull}.
}
\]

Thus the bounded ratchet corridor does not disappear; it is converted into a recognizable self-similar/dilation ancient-solution problem.

---

## 9. What is genuinely achieved

The proof attempt is no longer facing an undefined `critical H` label on this lane.

The compact bounded-amplitude survivor has been identified as a precise dynamical object:

\[
\boxed{
\text{nonzero Type-I ancient parabolic dilation hull with finite-enstrophy ancestry}.
}
\]

This is substantially narrower than an arbitrary singular Navier--Stokes scenario.

But because the periodic subcase already touches the unresolved backward-DSS problem, no honest proof can declare the entire hull impossible without a genuinely new rigidity theorem.

---

## 10. Highest-value next target

Any further progress must exploit structure stronger than generic DSS:

- the inherited material-axis ratchet mark;
- finite-enstrophy ancestry and backward Type-I enstrophy saturation;
- finite total ancient palinstrophy before the second blow-down;
- dual-source/flux genealogy;
- or a new monotone/rigid quantity on the dilation hull.

A theorem using one of these extra marks could exclude a subclass of backward DSS not covered by existing literature and would constitute a genuinely new closing mechanism.

---

## 11. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
