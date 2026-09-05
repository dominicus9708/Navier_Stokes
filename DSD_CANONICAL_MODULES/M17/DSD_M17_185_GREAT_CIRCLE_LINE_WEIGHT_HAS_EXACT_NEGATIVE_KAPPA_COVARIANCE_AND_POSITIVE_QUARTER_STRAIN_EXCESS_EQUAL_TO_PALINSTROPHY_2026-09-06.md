# DSD M17-185 — Great-circle line weight has exact negative-`kappa` covariance and positive quarter-strain excess equal to palinstrophy

Date: 2026-09-06  
Canonical ID: **M17-185**

Status: **LINE-STRAIN COERCIVITY GATE / IN THE REGULAR GREAT-CIRCLE FLUX COORDINATES OF M17-179, `rho^2 dy=L_rho dPhi` AFTER INTEGRATING ALONG VORTEX LINES. THE ELLIPTIC CE-H IDENTITY `Delta W=kappa W` GIVES `int kappa rho^2=-int |grad W|^2`, HENCE `int kappa L_rho dPhi=-D<0`: THE ENSTROPHY LINE WEIGHT IS FORCED TO FAVOR NEGATIVE KAPPA. THE SIMILARITY ENSTROPHY BALANCE GIVES `int (sigma_bar_rho-1/4)L_rho dPhi=D+(1/2)E'`, SO ON A RECURRENT FINITE-ENSTROPHY ENSEMBLE THE TIME-AVERAGED QUARTER-STRAIN EXCESS IS EXACTLY THE POSITIVE PALINSTROPHY `D`. THUS THE LINE-STRAIN RESIDENCE CHANNEL OF M17-184 IS NOT ARBITRARY IN TOTAL: IT MUST CARRY A STRICT POSITIVE GLOBAL PAYMENT. THE REMAINING FREEDOM IS ITS DISTRIBUTION ACROSS KAPPA SPACE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Flux-coordinate decomposition

On a regular great-circle vortex-line family, M17-179 gives

\[
\boxed{d\Phi=dq\,dx_3.}
\]

For one line,

\[
L_\rho
=\int_\Gamma\rho\,ds.
\]

The flow-box identity

\[
\rho^2dy=\rho\,ds\,d\Phi
\]

therefore gives, after integration along the line family,

\[
\boxed{
E:=\int_{\mathbb R^3}\rho^2dy
=\int L_\rho\,d\Phi
}
\]

for a vortex-saturated decaying domain, or with the corresponding boundary remainder on a truncated domain.

The formulas below are stated first in the full-space/zero-boundary-remainder setting.

---

## 2. Exact negative `kappa` line-weight moment

CE-H gives

\[
\Delta W=\kappa W.
\]

Take the `L2` pairing with `W` and integrate over space:

\[
\int W\cdot\Delta W\,dy
=\int\kappa|W|^2dy.
\]

After integration by parts,

\[
\boxed{
\int\kappa\rho^2dy
=-\int|\nabla W|^2dy.
}
\]

Define

\[
\boxed{D:=\int|\nabla W|^2dy.}
\]

Using the line decomposition,

\[
\boxed{
\int\kappa L_\rho\,d\Phi
=-D\le0.
}
\]

For a nontrivial nonconstant vorticity field,

\[
\boxed{D>0}
\]

and therefore

\[
\boxed{
\int\kappa L_\rho\,d\Phi<0.
}
\]

Thus the enstrophy residence weight is necessarily biased toward negative multiplier values.

---

## 3. Interpretation as a measure-bridge covariance

The pure current-flux measure uses

\[
d\Phi,
\]

while the enstrophy measure uses

\[
L_\rho d\Phi.
\]

On a recurrent pure-flux ensemble with zero mean multiplier in the current-flux measure, the identity in Section 2 becomes a strict negative time-averaged covariance between `kappa` and `L_rho`, after normalization by the finite total flux.

Symbolically,

\[
\boxed{
\operatorname{Cov}_{d\Phi}(\kappa,L_\rho)<0
}
\]

on the nontrivial recurrent branch, with the exact numerator supplied by palinstrophy plus the harmless normalization terms.

Thus the M5-681/M5-683 measure mismatch is not free: CE-H forces a specific negative multiplier/residence correlation.

---

## 4. Similarity enstrophy balance

The amplitude law is

\[
D_B\rho
=(\sigma+\kappa-1)\rho.
\]

Since

\[
\nabla\cdot B=\frac32,
\]

the fixed-space enstrophy derivative is

\[
\begin{aligned}
E'
&=\int\left[2(\sigma+\kappa-1)+\frac32\right]\rho^2dy\\
&=2\int\sigma\rho^2dy
+2\int\kappa\rho^2dy
-\frac12E.
\end{aligned}
\]

Use Section 2:

\[
\boxed{
E'
=-2D
+2\int\sigma\rho^2dy
-\frac12E.
}
\]

---

## 5. Convert the strain term to line residence

On one vortex line,

\[
\bar\sigma_\rho
=\frac{\int_\Gamma\sigma\rho ds}
{L_\rho}.
\]

Hence

\[
\boxed{
\int\sigma\rho^2dy
=\int\bar\sigma_\rho L_\rho d\Phi.
}
\]

Substitute into the enstrophy balance:

\[
E'
=-2D
+2\int\bar\sigma_\rho L_\rho d\Phi
-\frac12E.
\]

Since

\[
E=\int L_\rho d\Phi,
\]

we obtain the exact identity

\[
\boxed{
\int
\left(\bar\sigma_\rho-\frac14\right)
L_\rho d\Phi
=D+\frac12E'.
}
\]

---

## 6. Recurrent mean quarter-strain excess

On a recurrent finite-enstrophy ensemble, the long-time mean derivative of `E` vanishes:

\[
\overline{E'}=0.
\]

Therefore

\[
\boxed{
\overline{
\int
\left(\bar\sigma_\rho-\frac14\right)
L_\rho d\Phi
}
=\overline D.
}
\]

For a nontrivial recurrent state,

\[
\boxed{\overline D>0.}
\]

Hence

\[
\boxed{
\overline{
\int
\left(\bar\sigma_\rho-\frac14\right)
L_\rho d\Phi
}>0.
}
\]

This is a genuine positive global payment carried by the line-strain residence channel.

---

## 7. Connection to M17-184 joint kinetics

M17-184 defines

\[
S_\rho(k)
=\int\bar\sigma_\rho L_\rho
\delta(k-\kappa)d\Phi.
\]

Integrating over `k` gives

\[
\int S_\rho(k)dk
=\int\bar\sigma_\rho L_\rho d\Phi.
\]

Thus the recurrent identity becomes

\[
\boxed{
\overline{
\int
\left[S_\rho(k)-\frac14F_E(k)\right]dk
}
=\overline D>0.
}
\]

The total line-strain source is therefore constrained in sign and magnitude.

What remains free is the **distribution in `kappa`**:

\[
S_\rho(k)-\frac14F_E(k)
\]

may change sign across `k` while maintaining a positive total integral.

---

## 8. Combine the first two exact moments

The two full-space identities are

\[
\boxed{
\int kF_E(k)dk=-D,
}
\]

and, in recurrent mean,

\[
\boxed{
\overline{
\int\left(S_\rho(k)-\frac14F_E(k)\right)dk
}=\overline D.
}
\]

Therefore the same palinstrophy appears with opposite signs in

1. the multiplier residence moment;
2. the quarter-strain excess moment.

This exposes a precise compensation architecture:

\[
\boxed{
\text{negative-}kappa\text{ enstrophy residence}
\quad\leftrightarrow\quad
\text{positive line-strain excess}.
}
\]

---

## 9. Why this still does not determine the zero current

The stationary `kappa`-space current at `k=0` depends on the **half-space distribution** of these quantities, not only their total moments.

The identities above do not determine how the positive strain excess is partitioned between

\[
k>0
\quad\text{and}\quad
k<0.
\]

Therefore they do not by themselves fix

\[
G_E(0)
\]

or force a contradiction with M5-683.

The next genuine target is a `kappa`-resolved inequality for

\[
S_\rho(k)-\frac14F_E(k).
\]

---

## 10. DSD audit

### Audit A — treating line strain as arbitrary
Closed in total: its recurrent quarter-excess is exactly palinstrophy.

### Audit B — inferring a pointwise/`k`-resolved sign
Rejected. Only the total `k` integral has fixed sign.

### Audit C — truncated reservoirs
Boundary/cutoff remainders must be restored when the vortex-saturated domain is not all space.

### Audit D — proof status
A new positive global payment is identified, but the zero-current branch remains open because its `kappa` distribution is unresolved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
