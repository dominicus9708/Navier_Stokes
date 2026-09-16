# DSD M19-344 — Near-perfect sign cancellation factors exactly into sign flux fraction, line residence, and residence-weighted coefficient scale

Date: 2026-09-16  
Canonical ID: **M19-344**

Status: **ACTIVE SIGN-BALANCE FACTORIZATION / FLUX-THINNING REFINEMENT / RESIDENCE-COEFFICIENT TRADEOFF**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-458 and M19-337

On the late mixed-sign exact CE-H branch, define

\[
K_+
:=\int_{\{\kappa>0\}}\kappa\rho^2dx,
\]

\[
K_-
:=\int_{\{\kappa<0\}}(-\kappa)\rho^2dx.
\]

The whole-space identity gives

\[
P=K_--K_+\ge0.
\]

M17-458 shows that on the retained good-time set of the diffuse survivor, the ancestry-imposed palinstrophy smallness yields near-perfect first-moment cancellation,

\[
\boxed{
\frac{K_--K_+}{K_++K_-}\to0
}
\]

along the selected late records, equivalently

\[
\boxed{
\frac{K_-}{K_+}\to1
}
\]

whenever the common sign moment stays nontrivial.

M19-337 supplies the line-residence representation needed to factor this balance.

## 2. Flux-line form of the sign moments

On a regular positive-orientation flux family let \(d\nu\) be the positive flux-label measure and

\[
L_1(\lambda)=\int_{\Gamma_\lambda}\rho\,ds.
\]

Exact CE-H gives \(D_\xi\kappa=0\), so \(\kappa=\kappa_\lambda\) on each connected regular line.

Using

\[
\rho^2dV=\rho\,d\nu\,ds,
\]

we obtain exactly

\[
\boxed{
K_+
=
\int_{S_+}\kappa_\lambda L_1(\lambda)d\nu,
}
\]

and

\[
\boxed{
K_-
=
\int_{S_-}(-\kappa_\lambda)L_1(\lambda)d\nu.
}
\]

Here

\[
S_+=\{\kappa_\lambda>0\},
\qquad
S_-=\{\kappa_\lambda<0\}.
\]

## 3. Sign-resolved flux, residence, and coefficient means

Define the sign fluxes

\[
\Phi_+:=\int_{S_+}d\nu,
\qquad
\Phi_-:=\int_{S_-}d\nu.
\]

When \(\Phi_\pm>0\), define the sign-resolved mean line residences

\[
\boxed{
\bar L_+
:=
\frac{1}{\Phi_+}
\int_{S_+}L_1d\nu,
\qquad
\bar L_-
:=
\frac{1}{\Phi_-}
\int_{S_-}L_1d\nu.
}
\]

Define the residence-weighted coefficient magnitudes

\[
\boxed{
\bar\kappa_{+,L}
:=
\frac{
\int_{S_+}\kappa_\lambda L_1d\nu
}{
\int_{S_+}L_1d\nu
},
}
\]

\[
\boxed{
\bar\kappa_{-,L}
:=
\frac{
\int_{S_-}(-\kappa_\lambda)L_1d\nu
}{
\int_{S_-}L_1d\nu
}.
}
\]

All factors are nonnegative.

## 4. Exact triple factorization

By construction,

\[
\boxed{
K_+
=
\Phi_+\bar L_+\bar\kappa_{+,L},
}
\]

and

\[
\boxed{
K_-
=
\Phi_-\bar L_-\bar\kappa_{-,L}.
}
\]

Let

\[
\Phi=\Phi_++\Phi_-+\Phi_0
\]

and define sign flux fractions

\[
\eta_\pm=\Phi_\pm/\Phi.
\]

Then, whenever both sign moments are nonzero,

\[
\boxed{
\frac{K_+}{K_-}
=
\frac{\eta_+}{\eta_-}
\frac{\bar L_+}{\bar L_-}
\frac{\bar\kappa_{+,L}}{\bar\kappa_{-,L}}.
}
\]

Therefore M17-458's near-perfect cancellation becomes

\[
\boxed{
\frac{\eta_+}{\eta_-}
\frac{\bar L_+}{\bar L_-}
\frac{\bar\kappa_{+,L}}{\bar\kappa_{-,L}}
\to1.
}
\]

This is the main M19-344 identity.

## 5. Flux thinning is not an independent escape

Suppose

\[
\eta_+\to0
\]

while

\[
\eta_-\ge c_->0.
\]

Near-perfect sign cancellation requires

\[
\frac{\bar L_+}{\bar L_-}
\frac{\bar\kappa_{+,L}}{\bar\kappa_{-,L}}
\to\infty.
\]

Hence plus-sign flux thinning can survive only through at least one of

\[
\boxed{
G_{+\ \rm line\text{-}residence\ concentration}
}
\]

or

\[
\boxed{
G_{+\ \rm coefficient\text{-}scale\ escalation}
}
\]

relative to the negative population.

The same statement holds with the signs interchanged.

Thus M19-338's sign-flux thinning branch is not primitive once M17-458 cancellation is imposed.

## 6. Comparability removes sign-flux thinning

Assume there exist fixed constants

\[
0<c_L\le C_L<\infty,
\qquad
0<c_\kappa\le C_\kappa<\infty
\]

such that on the retained good-time branch

\[
c_L
\le
\frac{\bar L_+}{\bar L_-}
\le
C_L,
\]

and

\[
c_\kappa
\le
\frac{\bar\kappa_{+,L}}{\bar\kappa_{-,L}}
\le
C_\kappa.
\]

Then near-perfect cancellation implies

\[
\boxed{
0<c_\eta
\le
\frac{\eta_+}{\eta_-}
\le
C_\eta<\infty.
}
\]

If the zero-flux fraction \(\eta_0\) is negligible or separately controlled, both sign flux fractions are bounded below by fixed positive constants.

M19-338 then forces simultaneous sign-resolved amplitude collapse on both signs.

## 7. Coefficient-scale segregation versus residence segregation

The triple factorization distinguishes two mechanisms that were previously mixed together.

### Residence segregation

A small flux population can carry an order-one sign moment because its lines have anomalously large

\[
L_1=\int\rho ds.
\]

This is exactly the M19-337 Radon--Nikodym concentration mechanism.

### Coefficient-scale segregation

Alternatively the small flux population can carry an order-one sign moment because

\[
|\kappa|
\]

is much larger on that population.

This returns to coefficient-scale/high-jet/own-scale mismatch rather than pure geometric residence.

Thus the current sign balance cleanly separates geometry from coefficient scale.

## 8. Relation to M19-343 baseline amplitude

M19-343 identifies

\[
\mathfrak a_{\Phi,R}\sim R^{-1}
\]

as the natural parent-length diffuse baseline when a represented tube carries fixed enstrophy and length \(\asymp R\).

M19-344 shows that this total amplitude baseline does not determine how the two coefficient signs share the flux. Their allocation is constrained by the independent triple product

\[
\eta_\pm\bar L_\pm\bar\kappa_{\pm,L}.
\]

Hence the next scale-invariant diagnostics should track simultaneously

\[
R\mathfrak a_{\pm,R},
\qquad
\frac{\bar L_+}{\bar L_-},
\qquad
\frac{\bar\kappa_{+,L}}{\bar\kappa_{-,L}}.
\]

## 9. Updated spatial mixed-sign split

Combining M19-337--344, the sign-flux-thinning branch refines to

\[
\boxed{
\begin{aligned}
G_{\rm sign\ flux\ thinning}
\Longrightarrow{}&
G_{\rm sign\text{-}specific\ line\text{-}residence\ concentration}\\
&\lor G_{\rm sign\text{-}specific\ coefficient\text{-}scale\ escalation}\\
&\lor G_{\rm near\text{-}perfect\ cancellation\ failure}\\
&\lor G_{\rm zero\text{-}population/representation/genealogy\ loss}.
\end{aligned}
}
\]

On the retained M17-458 cancellation branch with residence and coefficient-scale comparability, sign-flux thinning is eliminated.

## 10. Audit verdict

**PASS — near-perfect sign cancellation has an exact flux × residence × coefficient-scale factorization.**

One sign population cannot silently lose material-flux weight while continuing to carry an order-one compensating sign moment. It must compensate through line-residence concentration or coefficient-scale escalation. Under comparability of those two ratios, both sign flux fractions remain nontrivial and M19-338 forces simultaneous baseline amplitude dilution.

The next target is to test whether the M19-321--323 fixed coefficient variance and own-scale spectral width control the residence-weighted coefficient-scale ratio strongly enough to remove the coefficient-escalation escape, leaving residence segregation as the main spatial survivor.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
