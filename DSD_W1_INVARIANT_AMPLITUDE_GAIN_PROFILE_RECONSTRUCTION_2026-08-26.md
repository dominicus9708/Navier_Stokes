# DSD W1 Invariant Amplitude Gain-Profile Reconstruction

Date: 2026-08-26

Status: **THE INVARIANT AMPLITUDE DISTRIBUTION IS RECONSTRUCTED FROM A SINGLE SCALAR NET-GAIN PROFILE `G_BAR(lambda)` / THE WEAK-L3 DEFECT IS ITS TOTAL MASS AND POSITIVITY OF THRESHOLD ENERGY IMPOSES NONNEGATIVE UPPER-TAIL CUMULATIVE GAIN AT EVERY AMPLITUDE / GLOBAL REGULARITY UNPROVED.**

## 1. Net gain profile

Define

\[
\boxed{
\bar G(\lambda)
:=
\left\langle
J_P(\lambda)-\nu D_\lambda
\right\rangle_\mu.
}
\]

Let

\[
\bar K(\lambda)
=
\left\langle
\lambda\mathcal E_{\lambda,U}
\right\rangle_\mu.
\]

The invariant threshold equation gives

\[
\boxed{
\bar G(\lambda)=-\frac12\bar K'(\lambda).
}
\]

Choose a common amplitude ceiling `A_*` with

\[
\bar K(A_*)=0.
\]

## 2. Reconstruct K from G

Integrating from `lambda` to `A_*`,

\[
\boxed{
\bar K(\lambda)
=
2\int_\lambda^{A_*}\bar G(\mu)d\mu.
}
\]

Since `K_U(lambda)>=0` statewise,

\[
\boxed{
\int_\lambda^{A_*}\bar G(\mu)d\mu\ge0
\qquad\forall\lambda>0.
}
\]

Thus the gain profile may have negative subintervals, but no upper-amplitude tail integral may be negative.

## 3. Reconstruct the weak-L3 coefficient

Define

\[
\bar N(\lambda)
=
\left\langle
|\{|U|>\lambda\}|
\right\rangle_\mu,
\]

and

\[
\bar C(\lambda)=\lambda^3\bar N(\lambda).
\]

The algebraic identity

\[
\lambda\bar K'
=
\bar K-\bar C
\]

combined with `bar K'=-2bar G` gives

\[
\boxed{
\bar C(\lambda)
=
\bar K(\lambda)+2\lambda\bar G(\lambda)
}
\]

and hence

\[
\boxed{
\bar C(\lambda)
=
2\int_\lambda^{A_*}\bar G(\mu)d\mu
+2\lambda\bar G(\lambda).
}
\]

Therefore the invariant weak-L3 amplitude distribution is determined by the single net-gain profile.

## 4. Endpoint defect is total gain mass

At low amplitude,

\[
\bar K(0+)=\mathscr R_3/3.
\]

Hence

\[
\boxed{
\frac{\mathscr R_3}{3}
=
2\int_0^{A_*}\bar G(\lambda)d\lambda.
}
\]

Equivalently,

\[
\boxed{
\int_0^{A_*}\bar G(\lambda)d\lambda
=
\frac{\mathscr R_3}{6}>0.
}
\]

## 5. Boundary behavior

At the upper amplitude ceiling,

\[
\bar K(A_*)=0,
\qquad
\bar C(A_*)=0.
\]

At the low-amplitude W1 boundary,

\[
\bar K(0+)=\bar C(0+)=\mathscr R_3/3
\]

provided `lambda bar G(lambda)->0`, as holds in the established critical endpoint regime.

Thus the boundary is neutral (`C=K`), while the strict interior contains the positive-gain profile needed to connect the two boundary conditions.

## 6. DSD reduction

The invariant amplitude-state problem can be compressed to one scalar object:

\[
\boxed{
\bar G(\lambda)
=
\text{pressure work minus viscous cost at amplitude level }\lambda.
}
\]

Its constraints are

\[
\boxed{
\int_\lambda^{A_*}\bar G\ge0
\quad\forall\lambda,
}
\]

and

\[
\boxed{
\int_0^{A_*}\bar G
=\mathscr R_3/6>0.
}
\]

The full invariant amplitude distribution follows from `bar G` through the reconstruction formulas above.

## 7. Closure target

W1 would be eliminated by any theorem forcing the total gain mass to be nonpositive:

\[
\int_0^{A_*}\bar G(\lambda)d\lambda\le0.
\]

More refined routes may attempt to show that no Navier--Stokes pressure/viscous pair can realize a gain profile satisfying the required positive mass plus all cumulative-tail constraints on a compact recurrent W1 class.

No such theorem is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
