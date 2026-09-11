# M19-007 — Scale mismatch rules out standard-energy control of material-flux total variation and exhausts the current signed-budget shortcuts

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC SIGNED-BUDGET NO-GO / SCALING OBSTRUCTION / STRATEGY PIVOT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-006 identifies a genuinely scale-critical signed parent observable: material vorticity flux.

Its recurrent fixed-size variation forces

\[
\operatorname{Var}\Phi=\infty
\]

unless one-sign drift exhausts the bounded flux range.

The natural hope is to control that total variation by the original finite-energy dissipation budget

\[
\int_0^{T^*}\|\omega(t)\|_2^2dt<\infty.
\]

This module shows that no **scale-free universal estimate of that form** can hold on scale-adapted material surfaces. The obstruction follows directly from Navier--Stokes scaling.

It then audits the other currently available signed candidates and concludes that the present signed-budget shortcut family is exhausted.

The R-AC calculation should therefore pivot to a direct return-weight / transport theorem rather than search for another unstructured additive budget.

## 2. Flux variation is scale critical

Material vorticity flux satisfies

\[
\Phi_r=\Phi
\]

under parabolic scaling.

Therefore its total variation is also invariant:

\[
\boxed{
\operatorname{Var}\Phi_r
=
\operatorname{Var}\Phi.
}
\]

Equivalently, since

\[
\Phi_r'(s)=r^2\Phi'(t)
\]

under \(t=r^2s\) when using the inverse scaling convention consistently, the time integral of the absolute rate remains unchanged after the corresponding time change.

The only point needed below is the invariant homogeneity:

\[
\boxed{\beta_{Var\Phi}=0.}
\]

## 3. Standard kinetic-energy dissipation is ancestry-cheap

For the physical dissipation charge

\[
\mathcal D_E
:=
\int\|\omega(t)\|_2^2dt,
\]

Navier--Stokes scaling gives

\[
\boxed{
\mathcal D_{E,r}=r\,\mathcal D_E
}
\]

when an event of normalized unit scale is mapped to physical length scale \(r\).

Thus

\[
\boxed{\beta_{\mathcal D_E}=+1.}
\]

This is exactly the M18-059 standard-energy homogeneity.

## 4. Scaling contradiction for a universal scale-free variation bound

Suppose there were a universal constant \(C\), independent of event scale, such that every controlled scale-adapted material surface satisfied

\[
\boxed{
\operatorname{Var}\Phi
\le
C\mathcal D_E.
}
\]

Take one nontrivial smooth local event with

\[
\operatorname{Var}\Phi=A>0
\]

and

\[
\mathcal D_E=D<\infty.
\]

Rescale it to physical length \(r\).

Then

\[
A
=\operatorname{Var}\Phi_r
\le
C rD.
\]

Letting

\[
r\downarrow0
\]

would force

\[
A=0,
\]

a contradiction.

Therefore

\[
\boxed{
\text{there is no scale-independent estimate }
\operatorname{Var}\Phi\lesssim\mathcal D_E
\text{ on scale-adapted events.}
}
\]

Any valid trace estimate must contain an inverse geometric length, a higher derivative, or another scale-critical quantity.

That extra factor restores dimensional balance but also restores the ancestry difficulty.

## 5. What a trace estimate must pay

The exact rate is

\[
\Phi'(t)
=
\nu\int_{S(t)}\Delta\omega\cdot n\,dA.
\]

A bound for this surface trace naturally involves quantities such as

\[
\|\Delta\omega\|,
\qquad
\|D^3u\|,
\qquad
\text{surface trace norms},
\]

or inverse powers of the surface length scale.

These are not controlled by the original kinetic-energy dissipation total of a hypothetical singular solution.

Thus the total-variation route does not secretly descend to the standard finite-energy budget.

## 6. Circulation is the same candidate, not a new one

By Stokes,

\[
\Phi(t)
=
\oint_{\partial S(t)}u\cdot dl.
\]

Therefore material circulation is not an independent signed ancestry observable here. It is the same scale-critical state variable expressed on the boundary loop.

Its recurrent variation encounters the same total-variation barrier.

Hence

\[
\boxed{
\text{flux route}
=\text{circulation route}
}
\]

for the present purpose.

## 7. Helicity does not provide the missing finite variation budget

The whole-space helicity

\[
\mathcal H(t)
:=
\int u\cdot\omega\,dx
\]

is scale critical.

For smooth viscous flow,

\[
\boxed{
\mathcal H'(t)
=-2\nu\int\omega\cdot(\nabla\times\omega)\,dx.
}
\]

Thus helicity is another signed scale-critical state.

However:

1. finite kinetic energy alone does not give a uniform bound on \(|\mathcal H(t)|\) approaching a hypothetical singular time;
2. the absolute helicity variation requires
   \[
   \int\left|\int\omega\cdot\nabla\times\omega\,dx\right|dt,
   \]
   which is not controlled by the standard energy dissipation budget;
3. the integrand reaches one derivative above enstrophy and has the same budget problem already exposed by M18-059.

Thus helicity does not supply the required finite scale-critical total-variation budget.

## 8. Normalized amplitude moments are recurrent balances, not parent monotone states

M18-060--070 derive exact signed amplitude-moment identities, but on the recurrent compact CE-H component they take source-sink forms such as

\[
\frac1pM_p'
=A_p-D_p-c_pM_p.
\]

Their invariant means balance exactly.

Moreover, these are normalized similarity-state observables, not automatically fixed-parent scale-critical additive quantities.

Therefore they do not replace the missing parent total-variation budget.

Their value is structural: they classify the strain/diffusion/sheath architecture, which M19-001--004 has already used to recompress the finite-current cycle.

## 9. Finite graph current also does not create a new parent budget

M19-001--004 proves that a nonzero finite-population cycle descends to

\[
G_{strain/geometry}
\lor
G_{palinstrophy/interface}
\lor
G_{coefficient+normalized\ diffusion}
\lor
G_{geometry/topology\ loss}.
\]

These are real PDE payers, but their available unsigned totals retain the ancestry economics audited in M18.

Hence the graph reduction identifies where recurrent flux variation is paid locally; it does not manufacture a finite scale-critical original-parent total.

## 10. Current signed-candidate exhaustion

The main signed candidates now have the following status:

\[
\begin{array}{c|c|c}
\text{candidate}
&\text{advantage}
&\text{failure}\cr
\hline
\text{remaining-time clock}
&\text{bounded Type-I state}
&\text{exact geometric discount}\cr
\text{material flux/circulation}
&\text{scale critical}
&\text{no finite total-variation budget}\cr
\text{helicity}
&\text{scale critical signed state}
&\text{no certified bounded/finite-variation budget}\cr
\text{amplitude moments}
&\text{exact recurrent balances}
&\text{source-sink compensation / normalized state}\cr
\text{finite graph current}
&\text{explicit cycle decomposition}
&\text{descends to existing non-finite parent payers}
\end{array}
\]

Therefore no currently certified signed observable has all three properties

\[
\boxed{
\begin{aligned}
&\text{fixed-parent scale-criticality},\\
&\text{bounded or finite total parent budget},\\
&\text{fixed recurrent one-way payment without reversible compensation}.
\end{aligned}
}
\]

## 11. Strategy pivot

The R-AC problem should no longer be attacked by an unrestricted search for another additive or signed budget.

M18-054 already gives the sharper surviving structure:

\[
\boxed{
\sum_kJ_k^{3/2}=\infty,
\qquad
\sum_kJ_k\mathfrak R_k<\infty,
}
\]

so the divergent cubic mass is forced onto shells with

\[
\frac{\mathfrak R_k}{J_k^{1/2}}\to0
\]

in cubic-mass density.

The next M19 calculation should therefore address the kinematics of this return deficiency directly.

The first question is:

> how much ancestral dwell can one coherent scale-\(r\) carrier produce from a single controlled passage?

If the answer is only the parabolic \(r^2\) amount, then single-pass kinematics is provably insufficient and any successful R-AC closure must force multiplicity, long trapping, or a nonlocal return mechanism.

## 12. M19-007 verdict

\[
\boxed{
\text{standard-energy dissipation cannot scale-freely control scale-critical material-flux total variation.}
}
\]

The present signed-budget shortcuts are therefore exhausted at the certified level.

The next calculation complex is direct return-weight kinematics.

---

\[
\boxed{\text{M19-007 COMPLETE; NEXT = DIRECT R-AC RETURN-WEIGHT CALCULATION.}}
\]
