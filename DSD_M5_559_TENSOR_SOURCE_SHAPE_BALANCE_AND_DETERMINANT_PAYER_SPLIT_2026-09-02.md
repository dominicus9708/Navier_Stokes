# DSD M5-559 — Tensor source-shape balance and determinant payer split

Date: 2026-09-02

Status: **MATRIX SHAPE AUDIT / THE MOVING-MARKER VORTICITY SECOND-MOMENT TENSOR OBEYS AN EXACT MATRIX BALANCE / ITS TRACE RECOVERS M5-558, WHILE ITS TRACE-FREE AND DETERMINANT CHANNELS RETAIN DIRECTIONAL SOURCE-SHAPE INFORMATION / HOWEVER NEITHER THE PRINCIPAL AXES NOR THE DETERMINANT GIVE A STRICT LYAPUNOV FUNCTION: TRANSPORT, VORTEX-STRETCHING, AND WEIGHTED PALINSTROPHY CAN CANCEL THE POSITIVE SIMILARITY DILATION / ON THE UNIFORMLY NONDEGENERATE SHAPE BRANCH, RECURRENCE FORCES A NEW SHAPE-PAYER IDENTITY WITH A UNIVERSAL `+3/2` DETERMINANT-DILATION BASELINE / OTHERWISE THE SOURCE COVARIANCE DEGENERATES, PRODUCING A THIN-SOURCE GEOMETRIC BRANCH / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-558

In backward similarity variables let

\[
B(y,\theta)=U(y,\theta)+\frac12y,
\qquad
\nabla\cdot B=\frac32,
\]

and let a material marker satisfy

\[
Y'(\theta)=B(Y(\theta),\theta).
\]

Set

\[
z=y-Y(\theta),
\qquad
e(y,\theta)=|W(y,\theta)|^2.
\]

The enstrophy density obeys

\[
\partial_\theta e+B\cdot\nabla e+2e
=2W\cdot\Sigma W+\Delta e-2|\nabla W|^2.
\]

Equivalently, using `div B=3/2`,

\[
\partial_\theta e+\nabla\cdot(Be)+\frac12e
=2W\cdot\Sigma W+\Delta e-2|\nabla W|^2.
\]

M5-558 derived the exact moving-weight identity for any bounded smooth scalar weight.

The purpose here is to retain the full matrix geometry instead of only the scalar radius.

---

## 2. Matrix second moment

For the formal uncut expression define

\[
\boxed{
\mathsf M(\theta)
:=
\int z\otimes z\,e(y,\theta)\,dy.
}
\]

Because a global second moment is not part of the inherited ancient package, the rigorous object on the compact core is the cut-off version

\[
\boxed{
\mathsf M_R
:=
\int \chi_R(z)\,z\otimes z\,e\,dy,
}
\]

where `chi_R=1` on the retained recurrent source architecture and vanishes in a slightly larger fixed ball.

All formulas below are exact in the principal region `chi_R=1`; the cut-off version carries a boundary commutator `mathcal B_R` supported on the fixed shell.

That shell is audited separately and cannot be silently discarded.

---

## 3. Exact matrix moving-weight identity

Apply the M5-558 moving-weight identity componentwise to

\[
\psi_{ij}(z)=z_i z_j.
\]

Since

\[
\partial_k(z_i z_j)
=\delta_{ki}z_j+\delta_{kj}z_i,
\]

and

\[
\Delta(z_i z_j)=2\delta_{ij},
\]

we obtain

\[
\boxed{
\begin{aligned}
\mathsf M'
={}&
\int
\Big[
(B(y)-B(Y))\otimes z
+z\otimes(B(y)-B(Y))
\Big]e\,dy\\
&+2E\,I
-\frac12\mathsf M
+2\mathsf Q^{(2)}
-2\mathsf P^{(2)},
\end{aligned}
}
\]

where

\[
E:=\int e\,dy,
\]

\[
\boxed{
\mathsf Q^{(2)}
:=
\int z\otimes z\,igl(W\cdot\Sigma W\bigr)\,dy,
}
\]

and

\[
\boxed{
\mathsf P^{(2)}
:=
\int z\otimes z\,|\nabla W|^2\,dy.
}
\]

For the cut-off core one adds

\[
\mathcal B_R,
\]

a symmetric matrix of the usual cut-off transport/diffusion commutators.

---

## 4. Separate explicit similarity dilation from physical relative velocity

Write

\[
B(y)-B(Y)
=
\frac12z+\delta U,
\]

with

\[
\delta U
:=U(y)-U(Y).
\]

Then

\[
\left(\frac12z\right)\otimes z
+z\otimes\left(\frac12z\right)
=z\otimes z.
\]

Combining this with the `-M/2` term gives

\[
\boxed{
\mathsf M'
=
\frac12\mathsf M
+2E I
+\mathsf T
+2\mathsf Q^{(2)}
-2\mathsf P^{(2)}
+\mathcal B_R,
}
\]

where

\[
\boxed{
\mathsf T
:=
\int
\Big[
\delta U\otimes z+z\otimes\delta U
\Big]e\,dy.
}
\]

This is the matrix analogue of M5-558.

---

## 5. Trace recovers the scalar width law

Taking the trace gives

\[
\boxed{
\frac d{d\theta}\operatorname{tr}\mathsf M
=
\frac12\operatorname{tr}\mathsf M
+6E
+\operatorname{tr}\mathsf T
+2\operatorname{tr}\mathsf Q^{(2)}
-2\operatorname{tr}\mathsf P^{(2)}
+\operatorname{tr}\mathcal B_R.
}
\]

Since

\[
\operatorname{tr}\mathsf M
=\int|z|^2|W|^2dy,
\]

this is precisely the quadratic-width balance of M5-558.

Thus M5-559 is a genuine refinement, not a different observable.

---

## 6. Trace-free anisotropy equation

Define the trace-free shape tensor

\[
\boxed{
\mathsf A
:=
\mathsf M
-\frac13(\operatorname{tr}\mathsf M)I.
}
\]

The isotropic diffusion source `2E I` cancels exactly from the trace-free equation.

Hence

\[
\boxed{
\mathsf A'
=
\frac12\mathsf A
+\mathsf T^{\circ}
+2(\mathsf Q^{(2)})^{\circ}
-2(\mathsf P^{(2)})^{\circ}
+\mathcal B_R^{\circ},
}
\]

where the superscript `circle` denotes trace-free part.

This isolates directional shape deformation from the isotropic second-moment injection.

Nevertheless every remaining forcing term is sign-indefinite as a matrix.

There is therefore no immediate monotonicity of the principal axes.

---

## 7. Projection onto a fixed direction

For a fixed unit vector `n`, define

\[
m_n:=n^T\mathsf M n.
\]

Then

\[
\boxed{
\begin{aligned}
m_n'
={}&
\frac12m_n
+2E
+n^T\mathsf T n
+2n^T\mathsf Q^{(2)}n\\
&-2n^T\mathsf P^{(2)}n
+n^T\mathcal B_R n.
\end{aligned}
}
\]

The weighted palinstrophy term is nonpositive in this scalar equation,

\[
n^T\mathsf P^{(2)}n
=
\int(n\cdot z)^2|\nabla W|^2dy
\ge0,
\]

but the transport and stretching moments have no fixed sign.

So even a directional second moment is not a one-sign cocycle.

---

## 8. Projection into the recurrent connector frame

For the M5-554 persistent pair let

\[
n(\theta)=\frac{Y_a-Y_b}{|Y_a-Y_b|}.
\]

Now `n` moves.

Define

\[
m_{conn}(\theta)
:=n(\theta)^T\mathsf M(\theta)n(\theta).
\]

Then

\[
\boxed{
\frac d{d\theta}m_{conn}
=n^T\mathsf M'n
+2n'\cdot\mathsf M n.
}
\]

M5-554 gives

\[
n'
=(I-n\otimes n)G_{ab}n.
\]

Therefore connector-frame rotation contributes another signed recurrent term

\[
\boxed{
2n'\cdot\mathsf M n.
}
\]

Even after aligning the covariance observable with the compressive pair direction, the frame motion prevents a scalar one-sign law.

---

## 9. Uniformly nondegenerate shape branch

Suppose on a recurrent compact subbranch the core covariance is uniformly positive definite:

\[
\boxed{
0<m_-I
\le
\mathsf M_R
\le
m_+I.
}
\]

Then

\[
\log\det\mathsf M_R
\]

is a bounded smooth observable on the recurrent component.

Jacobi's formula gives

\[
\frac d{d\theta}\log\det\mathsf M_R
=
\operatorname{tr}(\mathsf M_R^{-1}\mathsf M_R').
\]

Insert the matrix balance.

One obtains

\[
\boxed{
\begin{aligned}
(\log\det\mathsf M_R)'
={}&
\frac32
+2E_R\operatorname{tr}(\mathsf M_R^{-1})\\
&+\operatorname{tr}(\mathsf M_R^{-1}\mathsf T_R)\\
&+2\operatorname{tr}(\mathsf M_R^{-1}\mathsf Q_R^{(2)})\\
&-2\operatorname{tr}(\mathsf M_R^{-1}\mathsf P_R^{(2)})\\
&+\operatorname{tr}(\mathsf M_R^{-1}\mathcal B_R).
\end{aligned}
}
\]

The first term

\[
\boxed{\frac32}
\]

is universal and comes solely from similarity dilation of three independent shape directions.

The isotropic `2E I` term is also nonnegative.

---

## 10. Invariant determinant payer identity

Because `log det M_R` is bounded on the recurrent nondegenerate branch,

\[
\left\langle
(\log\det\mathsf M_R)'
\right\rangle=0.
\]

Thus

\[
\boxed{
\begin{aligned}
\frac32
+2\left\langle
E_R\operatorname{tr}(\mathsf M_R^{-1})
\right\rangle
={}&
2\left\langle
\operatorname{tr}(\mathsf M_R^{-1}\mathsf P_R^{(2)})
\right\rangle\\
&-\left\langle
\operatorname{tr}(\mathsf M_R^{-1}\mathsf T_R)
\right\rangle\\
&-2\left\langle
\operatorname{tr}(\mathsf M_R^{-1}\mathsf Q_R^{(2)})
\right\rangle\\
&-\left\langle
\operatorname{tr}(\mathsf M_R^{-1}\mathcal B_R)
\right\rangle.
\end{aligned}
}
\]

This is an exact **shape-payer identity**.

At least one of the right-hand channels must repeatedly compensate the strictly positive left-hand side.

---

## 11. Why the determinant still does not prove a contradiction

The determinant identity is more rigid than the scalar width law, but it is not a strict Lyapunov law.

The compensators are legitimate PDE terms:

1. weighted palinstrophy;
2. compressive relative transport;
3. negative weighted vortex-stretching production;
4. cut-off shell exchange.

Any one of them can have order-one recurrent mean.

Therefore the positive `3/2` similarity dilation baseline does not by itself accumulate without bound.

It is exactly canceled in a recurrent source-shape state.

The correct conclusion is a payer split, not a contradiction.

---

## 12. Degenerate covariance branch

If uniform positive definiteness fails, there exists a recurrent sequence with

\[
\lambda_{min}(\mathsf M_R)\to0.
\]

Because the retained source architecture has fixed nonzero enstrophy and bounded total second moment, this means its vorticity-weighted spatial distribution collapses toward a lower-rank geometry in at least one direction.

Thus

\[
\boxed{
\text{failure of determinant control}
\Longrightarrow
\text{thin-source / covariance-collapse branch}.
}
\]

This is a genuine geometric alternative and must not be merged with the nondegenerate determinant balance.

Derivative bounds may thicken or rule out arbitrarily thin collapse only if one can prove a fixed lower transverse mass scale; that has not yet been established globally for the entire recurrent source architecture.

---

## 13. DSD audit split

The tensor observable therefore produces the audited dichotomy

\[
\boxed{
E_{source\ shape}^{recurrent}
\Longrightarrow
E_{shape}^{nondegenerate\ payer}
\lor
H_{thin\ source}^{covariance}.
}
\]

On the first branch,

\[
\boxed{
\frac32
+2\langle E_R\operatorname{tr}(\mathsf M_R^{-1})\rangle
=
\text{palinstrophy/transport/production/shell compensation}.
}
\]

On the second branch, at least one covariance eigenvalue collapses.

---

## 14. Relation to M5-554--558

M5-554 showed the persistent pair requires

\[
\left\langle n^TS_{ab}n\right\rangle=-\frac12.
\]

M5-556 showed the leading point-source cross-stretching mode has zero radial strain in the source-target direction.

M5-557 therefore forced additional finite-width source shape or a third source.

M5-558 showed scalar source width is not monotone.

M5-559 now shows the stronger matrix source shape is also recurrently cancellable, but only by paying an explicit determinant ledger.

Thus the obstruction is not lack of directional bookkeeping.

It is the absence, so far, of a theorem that makes one of these recurrent compensation channels globally finite or nonrecyclable.

---

## 15. Highest-value next step

Two targets now dominate.

### A. Material-volume expansion audit

The similarity material velocity has exact divergence

\[
\nabla\cdot B=\frac32.
\]

Hence every genuine positive-volume material set transported by `B` satisfies

\[
|A(\theta)|
=e^{\frac32(\theta-\theta_0)}|A(\theta_0)|.
\]

A fixed positive-volume material carrier cannot remain forever inside one bounded similarity core.

The key audit question is whether the persistent fixed-flux lineage plus coherent carrier construction yields such a genuinely material positive-volume carrier, or whether repeated Eulerian re-thickening can evade the volume law through material turnover/diffusive deactivation.

This should be computed next.

### B. Localized ancient rigidity

Independently, use the already proved remote spectator decoupling to ask whether the global `L^3` hypothesis in known ancient Liouville mechanisms can be replaced by a finite-core critical bound plus quantitative tail decoupling.

The material-volume calculation is more elementary and should be exhausted first.

---

## 16. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
