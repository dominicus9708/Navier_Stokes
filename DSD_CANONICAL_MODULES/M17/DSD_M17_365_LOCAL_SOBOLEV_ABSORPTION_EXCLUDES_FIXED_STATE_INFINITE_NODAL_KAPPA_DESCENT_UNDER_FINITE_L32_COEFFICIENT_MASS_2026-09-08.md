# DSD M17-365 — Local Sobolev absorption excludes fixed-state infinite nodal kappa descent under finite L3/2 coefficient mass

Date: 2026-09-08  
Canonical ID: **M17-365**

Status: **ACTIVE LOCAL NODAL-RIGIDITY REDUCTION / NO CROSS-GENERATION CLAIM**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Local CE-H elliptic equation

At one fixed smooth CE-H time slice, on the regular active set,

\[
\boxed{\Delta W=\kappa W.}
\]

Let

\[
B_{2r}=B_{2r}(x_0)
\]

and choose a cutoff `eta` satisfying

\[
\eta\equiv1\text{ on }B_r,
\qquad
\operatorname{supp}\eta\subset B_{2r},
\qquad
|\nabla\eta|\le C/r.
\]

The argument is componentwise and sums over the vector components of `W`.

## 2. Exact cutoff identity

Integration by parts gives

\[
-\int \eta^2W\cdot\Delta W
=
\int\eta^2|\nabla W|^2
+2\int\eta W\cdot(\nabla\eta\cdot\nabla W).
\]

Using

\[
\Delta W=\kappa W
\]

and expanding `nabla(eta W)`, one obtains the exact identity

\[
\boxed{
\int|\nabla(\eta W)|^2
=
-\int\eta^2\kappa|W|^2
+
\int|\nabla\eta|^2|W|^2.
}
\]

Therefore

\[
\int|\nabla(\eta W)|^2
\le
\int\kappa_-|\eta W|^2
+
\frac{C}{r^2}\int_{B_{2r}}|W|^2.
\]

## 3. Critical L3/2 absorption

Let `S>0` be a Sobolev constant such that

\[
S\|f\|_6^2
\le
\|\nabla f\|_2^2.
\]

Hölder gives

\[
\int\kappa_-|\eta W|^2
\le
\|\kappa_-\|_{L^{3/2}(B_{2r})}
\|\eta W\|_6^2.
\]

Hence

\[
\int|\nabla(\eta W)|^2
\le
\frac{\|\kappa_-\|_{3/2}}{S}
\int|\nabla(\eta W)|^2
+
\frac{C}{r^2}\int_{B_{2r}}|W|^2.
\]

If

\[
\boxed{
\|\kappa_-\|_{L^{3/2}(B_{2r})}
\le
\theta S,
\qquad 0<\theta<1,
}
\]

then the potential term is absorbed and

\[
\boxed{
\int_{B_r}|\nabla W|^2
\le
\frac{C_\theta}{r^2}
\int_{B_{2r}}|W|^2.
}
\]

This is the local critical-potential Caccioppoli gate.

## 4. Contrapositive nodal carrier statement

Suppose a proposed nodal carrier at scale `r` has an interior gradient charge satisfying

\[
\int_{B_r}|\nabla W|^2
>
\frac{C_\theta}{r^2}
\int_{B_{2r}}|W|^2.
\]

Then the absorption hypothesis cannot hold. Therefore

\[
\boxed{
\|\kappa_-\|_{L^{3/2}(B_{2r})}
>\theta S.
}
\]

Thus a nodal microcarrier that is energetic relative to its surrounding amplitude must carry a fixed critical negative-coefficient mass on that scale.

Conversely, if the local critical coefficient mass is small, the interior nodal gradient energy is paid by surrounding `L2` amplitude rather than by an autonomous hidden nodal structure.

## 5. Fixed-state infinite descent is incompatible with local L3/2 integrability

Assume now

\[
\kappa_-\in L^{3/2}_{loc}
\]

for one fixed CE-H state near `x_0`.

Absolute continuity of the Lebesgue integral gives

\[
\boxed{
\|\kappa_-\|_{L^{3/2}(B_{2r}(x_0))}
\to0
\qquad(r\to0).
}
\]

Therefore there exists `r_0>0` such that for every

\[
0<r<r_0,
\]

the absorption condition of Section 3 holds.

Consequently an infinite nested sequence

\[
r_j\downarrow0
\]

cannot continue to satisfy the autonomous nodal-carrier inequality of Section 4 at every scale.

Hence

\[
\boxed{
\text{one fixed locally }L^{3/2}\text{ coefficient state cannot support an infinite autonomous critical nodal descent at one point.}
}
\]

## 6. Exact survivors

An apparent infinite nodal descent can survive only if at least one of the following occurs:

\[
\boxed{G_{\kappa_-\notin L^{3/2}_{loc}/coefficient\ singularity},}
\]

\[
\boxed{G_{surrounding\ amplitude\ payment},}
\]

\[
\boxed{G_{moving\ center/state/scale\ concentration},}
\]

or

\[
\boxed{G_{nodal/interface/genealogy\ migration}.}
\]

The first is genuine coefficient decompactification.

The second reconnects the nodal core to non-negligible surrounding amplitude.

The third is a concentration-compactness issue across a sequence of states or record generations, not a fixed-state nodal singularity.

## 7. Relation to M17-310

M17-310's global lower bound

\[
\|\kappa_-\|_{3/2}\ge S_3
\]

is consistent with the present local theorem.

The lower bound need not be concentrated at one nodal point. It may migrate in space, split among multiple centers, or recur at changing scales.

The present module only removes the shortcut in which one fixed smooth state hides the same autonomous critical coefficient charge at arbitrarily small nested radii around one nodal point.

## 8. Scale audit

The quantity

\[
\|\kappa_-\|_{L^{3/2}(B_r)}
\]

is exactly invariant under Navier--Stokes parabolic spatial scaling when the ball is scaled with the coefficient.

Thus the absorption threshold is critical rather than subcritical. No favorable scale power has been inserted.

## 9. DSD-theory role

The heuristic is to ask whether a purported nested structure is genuinely autonomous or is being paid from its surrounding shell. The proof is the standard cutoff identity, Sobolev inequality, Holder inequality, and absolute continuity of an `L^{3/2}` integral.

No DSD axiom is used as a PDE hypothesis.

## 10. Updated nodal frontier

Combining M17-362--365, the critical nodal branch is reduced to

\[
\boxed{
\begin{aligned}
G_{critical\ nodal\ \kappa_-}
\Longrightarrow{}&
G_{coefficient\ L^{3/2}\ singular/decompactified}\\
&\lor G_{surrounding\ amplitude\ payment}\\
&\lor G_{moving\ center/state/record\ concentration}\\
&\lor G_{nodal/interface/rank/domain\ exit}\\
&\lor H_{high\text{-}amplitude\ negative\ capture}.
\end{aligned}
}
\]

The next high-value target is the moving-center/state concentration branch: determine whether scale-critical negative coefficient mass can migrate indefinitely across record generations without producing a bounded-multiplicity concentration measure or returning to the M17-298 cross-scale allocation problem.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
