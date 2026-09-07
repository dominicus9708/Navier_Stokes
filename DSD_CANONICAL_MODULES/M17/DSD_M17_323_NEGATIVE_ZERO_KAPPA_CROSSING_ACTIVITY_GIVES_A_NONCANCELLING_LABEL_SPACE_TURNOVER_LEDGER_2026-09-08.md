# DSD M17-323 — negative zero-kappa crossing activity gives a noncancelling label-space turnover ledger

Date: 2026-09-08  
Status: **ACTIVE CANONICAL CALCULATION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-314

On the high-amplitude bounded-capture CE-H branch, the stationary material flux-label current satisfies

\[
\boxed{\overline G(0)\le-d_{flux}<0.}
\]

Resolve the zero-level current by the line-weight coordinate \(l=\log L_\rho\):

\[
G(0,\theta)=\int j_k(0,l,\theta)\,dl.
\]

No sign is assumed pointwise in \(l\).

## 2. Directed crossing activities

Define the one-sided activities

\[
A_-(\theta)
:=\int(-j_k(0,l,\theta))_+\,dl,
\]

\[
A_+(\theta)
:=\int(j_k(0,l,\theta))_+\,dl.
\]

Then exactly

\[
G(0,\theta)=A_+(\theta)-A_-(\theta).
\]

Hence

\[
A_-(\theta)=A_+(\theta)-G(0,\theta)\ge -G(0,\theta).
\]

Taking long-time averages gives

\[
\boxed{
\overline{A_-}\ge-\overline G(0)\ge d_{flux}>0.
}
\]

Equivalently,

\[
\boxed{
\liminf_{T\to\infty}
\frac1T\int_0^T A_-(\theta)d\theta
\ge d_{flux}.
}
\]

Thus the total downward zero-\(\kappa\) turnover grows at least linearly in normalized time:

\[
\int_0^T A_-(\theta)d\theta
\ge d_{flux}T-o(T).
\]

This quantity is nonnegative and cannot be erased by simultaneous upward crossings.

## 3. Line-weight renormalized activity

Let

\[
\widetilde A_-(\theta)
:=\int e^{-l}(-j_k(0,l,\theta))_+\,dl.
\]

Since \(e^{-l}=L_\rho^{-1}\), if the captured family has a uniform upper line-weight bound

\[
L_\rho\le L^*<\infty,
\]

then

\[
\widetilde A_-(\theta)
\ge\frac1{L^*}A_-(\theta).
\]

Therefore

\[
\boxed{
\overline{\widetilde A_-}
\ge\frac{d_{flux}}{L^*}>0.
}
\]

If no such finite \(L^*\) survives, record instead the typed exit

\[
G_{line\text{-}weight\ decompactification}.
\]

The advantage of one-sided activity is that positive reweighting by \(e^{-l}\) cannot create a sign-covariance reversal inside the negative part.

## 4. Deterministic label representation

On a regular material-label representation, let

\[
h=D_B\kappa.
\]

At the zero level the resolved current has the Liouville form

\[
j_k(0,l,\theta)=h(0,l,\theta)H(0,l,\theta),
\]

where \(H\ge0\) is the joint label density.  Hence

\[
\widetilde A_-(\theta)
=
\int e^{-l}h_-\,H(0,l,\theta)\,dl,
\]

with \(h_-:=(-h)_+\).

Define the renormalized zero-level trace mass and square-speed density

\[
M_0(\theta)
:=\int e^{-l}H(0,l,\theta)\,dl,
\]

\[
D_0(\theta)
:=\int e^{-l}h_-^2H(0,l,\theta)\,dl.
\]

Cauchy--Schwarz gives

\[
\boxed{
\widetilde A_-(\theta)^2
\le M_0(\theta)D_0(\theta).
}
\]

## 5. Time-averaged square-speed alternative

Integrating the preceding inequality in time and applying Cauchy--Schwarz once more,

\[
\left(\int_0^T\widetilde A_-d\theta\right)^2
\le
\left(\int_0^TM_0d\theta\right)
\left(\int_0^TD_0d\theta\right).
\]

Suppose the zero-level renormalized trace mass has finite long-time mean

\[
\limsup_{T\to\infty}
\frac1T\int_0^TM_0d\theta
\le M^*<\infty.
\]

Then using the lower activity density,

\[
\boxed{
\liminf_{T\to\infty}
\frac1T\int_0^TD_0(\theta)d\theta
\ge
\frac{d_{flux}^2}{(L^*)^2M^*}>0.
}
\]

Thus a persistent negative zero-level current forces one of two outcomes:

1. zero-level trace concentration/decompactification;
2. a positive long-time density of the nonnegative coefficient-speed trace quantity \(e^{-l}h_-^2H\).

## 6. What has and has not been gained

This closes the **sign-cancellation** problem at zero \(\kappa\):

\[
\boxed{
\overline G(0)<0
\Rightarrow
\text{positive one-sided turnover density}.
}
\]

However, \(D_0\) is still a label-space boundary-trace quantity.  No theorem has yet identified

\[
\int_0^TD_0d\theta
\]

with a finite original-coordinate Navier--Stokes resource.

Therefore the implication

\[
\text{positive normalized turnover density}
\Rightarrow
\text{physical/global contradiction}
\]

is **not** allowed.

## 7. Updated gate

\[
\boxed{
\begin{aligned}
H_{fixed\ negative\ zero\text{-}\kappa\ current}
\Longrightarrow{}&
G_{line\text{-}weight\ decompactification}\\
&\lor G_{zero\text{-}level\ trace\ concentration}\\
&\lor H_{positive\ directed\ crossing\ activity}\\
&\lor H_{positive\ coefficient\text{-}speed\ trace\ ledger}.
\end{aligned}
}
\]

The last two are nonnegative normalized ledgers, but still require physicalization or a direct rigidity theorem.

## 8. Audit verdict

**PASS as a label-space noncancellation reduction.**

It does not close global regularity.  The next calculation must test whether the zero-level boundary trace can be thickened to a finite \(|\kappa|<\delta\) corridor or linked to a standard PDE norm without an uncontrolled trace constant.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
