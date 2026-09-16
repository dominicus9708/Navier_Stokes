# M19-330 — Log-kappa diffusion splits into intrinsic self-recycling or residual strain-phase excess

**Date:** 2026-09-16  
**Status:** ACTIVE CALCULATION / SELF-RECYCLING SUBTRACTION / RESIDUAL SIGNED EXCESS / NOT GLOBAL CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Normalized entropy identity

M19-328 gives on a recurrent sign-preserving CE-H material packet

\[
0=
\langle D_z\rangle
+
\langle S_{interface}\rangle
+
\langle S_{force}\rangle
+2\langle C_{\sigma z}\rangle
+2\langle C_{\kappa z}\rangle,
\]

where

\[
D_z=\langle|\nabla z|^2\rangle_\pi,
\qquad
z=\log|\kappa|,
\]

\[
C_{\sigma z}=\operatorname{Cov}_\pi(\sigma,z),
\qquad
C_{\kappa z}=\operatorname{Cov}_\pi(\kappa,z).
\]

M19-329 shows that on a negative-kappa component

\[
C_{\kappa z}\le -\frac1{M_\kappa}\operatorname{Var}_\pi(\kappa)<0.
\]

## 2. Define the self-recycling residual

Set

\[
\boxed{
\mathcal R_z
:=
D_z+2C_{\kappa z}.
}
\]

Then the recurrent entropy balance becomes

\[
\boxed{
\langle\mathcal R_z\rangle
+
2\langle C_{\sigma z}\rangle
+
\langle S_{force}\rangle
+
\langle S_{interface}\rangle
=0.
}
\]

This subtracts the coefficient self-recycling mechanism before asking for any external payer.

## 3. Branch A: intrinsic self-recycling is sufficient

If

\[
\boxed{
\langle\mathcal R_z\rangle\le0,
}
\]

then the negative coefficient self-covariance is large enough, in invariant mean, to offset the positive log-diffusion channel without requiring a positive residual diffusion debt.

This is compatible with compact recurrence.

Therefore

\[
\boxed{
\langle\mathcal R_z\rangle\le0
\text{ is a genuine recyclable survivor, not a contradiction.}
}
\]

## 4. Branch B: residual positive excess

Suppose instead

\[
\boxed{
\langle\mathcal R_z\rangle=r_*>0.
}
\]

Then

\[
2\langle C_{\sigma z}\rangle
+
\langle S_{force}\rangle
+
\langle S_{interface}\rangle
=-r_*.
\]

Hence at least one of

\[
\boxed{
\langle C_{\sigma z}\rangle\le-\frac{r_*}{6},
}
\]

\[
\boxed{
\langle S_{force}\rangle\le-\frac{r_*}{3},
}
\]

or

\[
\boxed{
\langle S_{interface}\rangle\le-\frac{r_*}{3}
}
\]

must occur, up to harmless redistribution of the constants.

Thus only the residual excess beyond automatic coefficient self-recycling needs a separate signed payer.

## 5. Strain-phase branch forces strain heterogeneity

On a compact sign-preserving coefficient collar,

\[
\operatorname{Var}_\pi(z)\le V_z^*<\infty.
\]

Cauchy--Schwarz gives

\[
|C_{\sigma z}|^2
\le
\operatorname{Var}_\pi(\sigma)
\operatorname{Var}_\pi(z).
\]

Therefore a fixed negative strain-phase covariance

\[
C_{\sigma z}\le-c_{\sigma z}<0
\]

forces

\[
\boxed{
\operatorname{Var}_\pi(\sigma)
\ge
\frac{c_{\sigma z}^2}{V_z^*}
>0.
}
\]

Hence the residual branch cannot be paid by spatially uniform axial strain. It requires genuine strain-phase heterogeneity.

## 6. Two strain populations

Compactness also gives

\[
|\sigma-\bar\sigma|\le M_\sigma.
\]

Applying the same bounded-variance lemma used in M19-324 to the positive lower bound on \(\operatorname{Var}_\pi(\sigma)\) yields two strain populations of fixed positive packet probability separated by a fixed strain gap.

Thus

\[
\boxed{
\mathcal R_z^+ + \text{small force/interface}
\Longrightarrow
\text{two quantitative axial-strain phases correlated with coefficient phase}.
}
\]

This is stronger than merely saying that strain is nonzero.

## 7. Resource firewall

Fixed strain heterogeneity is still an order-one normalized recurrent structure. It does not automatically create a nonsummable ancestral cost.

The trace-free strain estimate and compact-hull bounds can turn it into local strain-square/enstrophy or derivative activity, but M18-058--059 and M19-317 prohibit interpreting another fixed unsigned local charge as a global contradiction.

Therefore the strain-phase branch is best viewed as a joint recurrent factor unless a further theorem forces

- supercritical duration/multiplicity;
- non-coboundary signed transport;
- interface/geometry escape;
- or coupling to an independently finite resource.

## 8. Positive-kappa component

On a positive-kappa sign-preserving component,

\[
C_{\kappa z}\ge0.
\]

Hence

\[
\mathcal R_z\ge D_z\ge0.
\]

There is no intrinsic negative self-recycling. Positive coefficient components with nontrivial spatial variance therefore necessarily demand strain-phase, forcing, interface, or zero-crossing compensation.

Since the whole-space enstrophy-weighted mean is \(\bar\kappa=-P/E\le0\), positive components cannot constitute the entire nonzero-vorticity state; they require negative coefficient mass elsewhere.

## 9. Canonical reduction

The spatial coefficient-current branch is now

\[
\boxed{
\begin{aligned}
\text{spatial kappa variance}
\Longrightarrow{}&
\text{zero/interface/geometry exit}\\
&\lor
\text{negative-kappa self-recycling survivor}\\
&\lor
\text{positive residual }\mathcal R_z^+
\end{aligned}
}
\]

and

\[
\boxed{
\mathcal R_z^+
\Longrightarrow
\text{strain-phase heterogeneity}
\lor
\text{typed force source}
\lor
\text{interface current}.
}
\]

## 10. Conclusion

After removing the automatic negative-kappa self-covariance, the true internal debt is not the full log-diffusion but

\[
\boxed{
\mathcal R_z=D_z+2\operatorname{Cov}(\kappa,\log|\kappa|).
}
\]

Only its positive invariant-mean part requires an additional payer.

\[
\boxed{
\text{M19-330 COMPLETE; NEXT TARGET: TEST WHETHER THE STRAIN-PHASE HETEROGENEITY IS ALREADY ENCODED BY THE CE-H AMPLITUDE EQUATION OR CREATES A NEW JOINT FACTOR.}
}
\]
