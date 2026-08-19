# Invariant Near-Max-Mid Kernel Estimate — 2026-08-20

Status: **FOLLOW-UP TO `RIGIDITY_KERNEL_2026-08-20.md` — GLOBAL REGULARITY NOT PROVED.**

This note rewrites the near-max-mid defect estimate without dependence on the arbitrary choice of basis inside the positive eigenspace.

---

## 1. Intrinsic near-max-mid variables

On the positive-middle-strain region, order

\[
\lambda_1<\lambda_2\le\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0.
\]

Write

\[
\lambda_1=-2m,
\qquad
\lambda_2=m-d,
\qquad
\lambda_3=m+d,
\]

where

\[
m>0,
\qquad
0\le d<m.
\]

The compression eigenvalue is simple because

\[
\lambda_2-\lambda_1=3m-d>2m>0.
\]

Hence the compression rank-one projector

\[
P_-=n\otimes n
\]

is intrinsically defined wherever `m>0`.

Define the max-mid base tensor

\[
S_{mm}=m(I-3P_-)
\]

and the planar anisotropy defect tensor

\[
\boxed{
D=S-S_{mm}.
}
\]

Then

\[
D n=0,
\qquad
\operatorname{tr}D=0,
\qquad
|D|_F^2=2d^2.
\]

Thus `D=0` is exact max-mid, while `D` measures the splitting of the two positive eigenvalues together with the orientation of that splitting inside the positive plane.

---

## 2. The old frame-dependent terms are controlled by grad D

In a local eigenframe, `D` has the form

\[
D=\operatorname{diag}(0,-d,d).
\]

For one spatial derivative, with `b=partial_a d` and frame connection `Omega_a`,

\[
(R^T\partial_aDR)_{22}=-b,
\qquad
(R^T\partial_aDR)_{33}=b,
\]

and

\[
(R^T\partial_aDR)_{23}=2d(\Omega_a)_{23}.
\]

Therefore

\[
\boxed{
|\partial_aD|_F^2
\ge
2(\partial_ad)^2
+8d^2(\Omega_a)_{23}^2.
}
\]

After summing over spatial directions,

\[
\boxed{
|\nabla D|_F^2
\ge
2|\nabla d|^2
+8d^2|\Omega_{23}|^2.
}
\]

The right side is exactly the pair of positive defect terms that appeared in the frame calculation.

---

## 3. Gauge-invariant near-max-mid inequality

From `RIGIDITY_KERNEL_2026-08-20.md`, under

\[
0\le d\le\eta m,
\]

one has

\[
\begin{aligned}
10\int m|\nabla m|^2
\le{}&
(4+8\eta^2)\int m|\nabla d|^2\\
&+16\int md^2|\Omega_{23}|^2\\
&+3\|\Delta S\|_2\|P_{st}Q\|_2.
\end{aligned}
\]

Using

\[
|\nabla D|^2
\ge2|\nabla d|^2+8d^2|\Omega_{23}|^2,
\]

and choosing

\[
C_\eta=2+4\eta^2,
\]

we obtain the intrinsic estimate

\[
\boxed{
10\int m|\nabla m|^2
\le
C_\eta\int m|\nabla D|^2
+3\|\Delta S\|_2\|P_{st}Q\|_2.
}
\]

Since

\[
\|m\|_9^3
\lesssim
\int m|\nabla m|^2,
\]

this yields

\[
\boxed{
\|m\|_9^3
\lesssim_\eta
\int m|\nabla D|^2
+
\|\Delta S\|_2\|P_{st}Q\|_2.
}
\]

This is the preferred near-max-mid stability inequality because every term is now basis-independent.

---

## 4. Scale consistency

Under a Navier--Stokes scaling with vorticity/strain scale `W`,

\[
S_{phys}=W S_{norm},
\qquad
Q_{phys}=W^2Q_{norm},
\qquad
y=W^{1/2}x.
\]

Then

\[
\|m\|_9^3
\sim W^{5/2},
\]

\[
\int m|\nabla D|^2dx
\sim W^{5/2},
\]

and

\[
\|\Delta S\|_2\|P_{st}Q\|_2
\sim W^{5/2}.
\]

Hence the invariant inequality is exactly scale-consistent and passes unchanged to first-hitting normalized variables after dividing by the common `W^(5/2)` factor.

---

## 5. Normalized defect alternatives

Define the dimensionless normalized ratios

\[
\mathfrak D_{mm}
=
\frac{\int m|\nabla D|^2}{\|m\|_9^3},
\]

and

\[
\mathfrak V_Q
=
\frac{\|\Delta S\|_2\|P_{st}Q\|_2}{\|m\|_9^3}.
\]

Then in any fixed near-max-mid window `d <= eta m`,

\[
\boxed{
1\lesssim_\eta
\mathfrak D_{mm}+\mathfrak V_Q.
}
\]

Therefore a scale-normalized near-max-mid state cannot simultaneously satisfy

\[
\mathfrak D_{mm}\to0
\]

and

\[
\mathfrak V_Q\to0.
\]

In particular, on `G_Q*`, where the projection factor tends to zero while the higher derivative factor remains controlled, one must have

\[
\boxed{
\mathfrak D_{mm}\gtrsim_\eta1.
}
\]

Thus projection invisibility forces a persistent max-mid-defect reorganization channel.

---

## 6. Interpretation of the defect channel

The tensor `D` records both:

1. eigenvalue splitting `lambda_3-lambda_2=2d`;
2. rotation of the preferred axes inside the positive eigenspace.

Therefore

\[
\int m|\nabla D|^2
\]

is an intrinsic mixture of non-saturation and projective reorganization.

The near-max-mid `G_Q*` branch is now typed as

\[
\boxed{
G_Q^*+\text{near-max-mid}
\Longrightarrow
P_{defect}^*\lor H,
}
\]

where `P_defect*` denotes an order-one normalized defect-gradient action.

The remaining task is not to prove that this action is nonzero — that is now established — but to determine whether it can recur over infinitely many geometric first-hitting stages without forcing an existing `H` or bounded-turnover channel.

---

## 7. Current endpoint split

The former single `G_Q*` survivor is refined into

\[
\boxed{
G_Q^*
\Longrightarrow
\begin{cases}
P_{defect}^*\lor H, & d/m\le\eta,\\
M_{nonsat}^*, & d/m>\eta.
\end{cases}
}
\]

Here `M_nonsat*` is the genuinely non-saturated positive-middle-strain branch already separated earlier by the cubic determinant saturation defect.

Thus exact/near-max-mid self-amplification is no longer an untyped endpoint.

---

## 8. Next calculation

Two complementary tasks remain:

1. **Near-max-mid packing:** derive a stagewise lower bound for the time-integrated normalized defect action `mathfrak D_mm` and connect repeated defect reorganization to palinstrophy/hyperpalinstrophy or bounded-radius turnover.

2. **Non-saturated closure:** quantify how a fixed lower bound on `d/m` produces a fixed determinant-saturation defect and combine it with the first-hitting scale-damping ledger.

Status: **NEAR-MAX-MID `G_Q*` IS NOW INVARIANTLY ROUTED TO DEFECT REORGANIZATION OR H; NON-SATURATED POSITIVE-MIDDLE STRAIN REMAINS.**
