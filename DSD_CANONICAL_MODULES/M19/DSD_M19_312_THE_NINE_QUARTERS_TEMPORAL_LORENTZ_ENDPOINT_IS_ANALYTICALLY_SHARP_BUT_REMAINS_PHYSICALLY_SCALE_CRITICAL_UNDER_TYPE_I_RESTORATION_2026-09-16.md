# M19-312 — The m=9/4 temporal-Lorentz endpoint is analytically sharp but remains physically scale critical under Type-I restoration

**Date:** 2026-09-16  
**Status:** ACTIVE GMS ENDPOINT AUDIT / LORENTZ DOES NOT REMOVE BASE-SCALE GATE / PHYSICAL CRITICALITY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Analytic gain from M19-311

M19-311 identified the exact derivative endpoint

\[
m=9/4
\]

and showed that the weighted GMS payer is finite if the physical derivative satisfies

\[
\boxed{
D^{9/4}u
\in
L_t^{2,4/3}L_x^2.
}
\]

This is stronger in temporal concentration than ordinary `L_t^2`, and it resolves the logarithmic Holder endpoint analytically.

The present module asks whether this concentration improvement by itself removes the physical base-scale amplification.

## 2. Type-I size of the endpoint derivative

For a Type-I velocity profile

\[
V(x,-T)
\sim
T^{-1/2}U(x/\sqrt T),
\]

a derivative of order `m` has spatial `L2` size

\[
\|D^mV(-T)\|_2
\sim
T^{1/4-m/2}.
\]

Indeed, the derivative contributes `T^{-m/2}`, velocity contributes `T^{-1/2}`, and the spatial `L2` volume factor contributes `T^{3/4}`.

At

\[
m=9/4,
\]

this becomes

\[
\boxed{
\|D^{9/4}V(-T)\|_2
\sim
T^{-7/8}.
}
\]

## 3. Lorentz tail homogeneity

Let

\[
h(\tau)=\|D^{9/4}V(\tau)\|_2.
\]

For a homogeneous model

\[
h(-T)\sim T^{-7/8},
\]

the time tail norm in any finite Lorentz second index `q` scales as

\[
\boxed{
\|h\|_{L_t^{2,q}(-\infty,-T)}
\sim
T^{1/2-7/8}
=
T^{-3/8}.
}
\]

The Lorentz second index changes concentration requirements but not the parabolic scaling exponent.

In particular, the analytically useful space

\[
L_t^{2,4/3}
\]

has the same Type-I homogeneity

\[
T^{-3/8}.
\]

## 4. Physical restoration of the Lorentz norm

For velocity derivative order `m`, the spatial `L2` derivative norm scales as

\[
\|D^m u_{phys}(t)\|_2
=
r_j^{1/2-m}
\|D^mV(s)\|_2,
\qquad
t=r_j^2s.
\]

A time `L^{2,q}` norm gains one factor `r_j` from the parabolic time change, so

\[
\boxed{
\|D^m u_{phys}\|_{L_t^{2,q}L_x^2}
=
r_j^{3/2-m}
\|D^mV\|_{L_s^{2,q}L_y^2}.
}
\]

At `m=9/4`,

\[
\boxed{r_j^{3/2-m}=r_j^{-3/4}.}
\]

Therefore a Type-I Lorentz tail through backward age `T` restores as

\[
r_j^{-3/4}T^{-3/8}.
\]

With composite physical radius

\[
\rho=r_j\sqrt T,
\]

we obtain

\[
\boxed{
r_j^{-3/4}T^{-3/8}
=
\rho^{-3/4}.}
\]

## 5. Lorentz improvement is not base gain

Thus even the exact analytically sharp temporal concentration class has critical physical homogeneity under Type-I restoration:

\[
\boxed{
L_t^{2,4/3}
\text{ concentration refinement}
\not\Rightarrow
\text{physical scale gain}.
}
\]

The two issues are distinct:

1. **analytic endpoint:** temporal Lorentz index `4/3` defeats the logarithmic GMS kernel;
2. **physical transfer:** the norm must remain finite/adequately small after the shrinking base scale is restored.

M19-311 solves only the form of the first requirement.

## 6. Required subcritical improvement

A successful endpoint transfer would need, on relevant backward ages,

\[
\boxed{
\|D^{9/4}V\|_{L_s^{2,4/3}(-\infty,-T;L_x^2)}
=
o(T^{-3/8})
}
\]

with a rate strong enough relative to

\[
\rho_j=r_j\sqrt{T_j}\to0,
\]

or an equivalent incidence/packing theorem producing extra physical smallness.

A power improvement

\[
T^{-3/8-\delta}
\]

would restore as

\[
\rho^{-3/4}T^{-\delta}.
\]

## 7. Revised endpoint gate

The sharp Lorentz lane is therefore

\[
\boxed{
\mathcal T_{GMS}^{9/4,Lorentz-base}:
\begin{cases}
D^{9/4}u\text{ has the }L_t^{2,4/3}L_x^2\text{ concentration structure},\\
\text{and that structure gains subcritical physical strength under base restoration.}
\end{cases}
}
\]

Neither clause can be silently substituted for the other.

## 8. Unified conclusion with M19-309--311

The GMS route now has a clean hierarchy:

\[
\boxed{
\begin{array}{ll}
\text{analytic derivative threshold:}&m>9/4\text{ strong, or }m=9/4\text{ Lorentz},\\
\text{known ancient scaling:}&\text{critical at every }m\in[2,3],\\
\text{missing physical ingredient:}&\text{subcritical base gain / incidence / concentration improvement}.
\end{array}
}
\]

This is strictly sharper than the previous `physical D3` formulation while preserving the base-scale firewall.

---

\[
\boxed{\text{M19-312 COMPLETE; LORENTZ FIXES THE ANALYTIC LOG ENDPOINT BUT NOT THE PHYSICAL BASE-SCALE CRITICALITY.}}
\]