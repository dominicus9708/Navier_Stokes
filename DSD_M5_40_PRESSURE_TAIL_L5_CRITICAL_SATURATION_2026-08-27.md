# DSD M5-40 — Weighted Pressure Tail Saturates the L5 Spacetime Endpoint

Date: 2026-08-27

Status: **DERIVED CRITICAL-BUDGET AUDIT / GENERIC CONTROL OF `int |u| p^2` IS AT THE SERRIN-CRITICAL L5 SPACETIME LEVEL, AND THE W1 `1/r` CORRIDOR SATURATES IT WITH LOGARITHMIC TIME DIVERGENCE / PRESSURE-TAIL ROUTE DOES NOT PRODUCE A FINITE ENERGY-CLASS BUDGET / GLOBAL REGULARITY UNPROVED.**

## 1. Weighted pressure quantity

The live pressure remainder from M5-34--39 is

\[
\boxed{
\mathcal P_5(t)
:=
\int_{\mathbb R^3}|u(x,t)|\,|p(x,t)|^2dx.
}
\]

Under Navier--Stokes scaling it has the same spatial scaling as the critical `p=3` dissipation; multiplication by `dt` makes it scale invariant.

## 2. Calderon--Zygmund and Holder estimate

The pressure relation gives

\[
\|p\|_{L^{5/2}}
\lesssim
\|u\otimes u\|_{L^{5/2}}
\lesssim
\|u\|_{L^5}^2.
\]

Therefore

\[
\begin{aligned}
\mathcal P_5(t)
&\le
\|u\|_{L^5}
\|p^2\|_{L^{5/4}}\\
&=
\|u\|_{L^5}
\|p\|_{L^{5/2}}^2\\
&\lesssim
\|u\|_{L^5}^5.
\end{aligned}
\]

Hence

\[
\boxed{
\int_0^T\mathcal P_5(t)dt
\lesssim
\int_0^T\|u(t)\|_5^5dt.
}
\]

The right-hand side is exactly at the Ladyzhenskaya--Prodi--Serrin scaling line because

\[
\frac{2}{5}+\frac{3}{5}=1.
\]

## 3. W1 `1/r` corridor audit

For the critical physical corridor

\[
|u|\sim r^{-1},
\qquad
|p|\sim r^{-2},
\]

between

\[
r_*(t)\sim\sqrt{T_*-t}
\]

and a fixed parent scale `r0`,

\[
\begin{aligned}
\mathcal P_5(t)
&\sim
\int_{r_*}^{r_0}
r^{-1}r^{-4}r^2dr\\
&=
\int_{r_*}^{r_0}r^{-3}dr\\
&\sim
r_*^{-2}\\
&\sim
(T_*-t)^{-1}.
\end{aligned}
\]

Thus

\[
\boxed{
\int^{T_*}\mathcal P_5(t)dt
\sim
\int^{T_*}\frac{dt}{T_*-t}
=\infty
}
\]

logarithmically.

Likewise

\[
\|u(t)\|_5^5
\sim
(T_*-t)^{-1}.
\]

The weighted pressure remainder therefore saturates the same critical clock as the standard `L5_{t,x}` Serrin endpoint.

## 4. DSD consequence

The strict W1 pressure-tail margin of M5-37--39 does not conflict with the classical energy class because its natural spacetime action is critical rather than subcritical.

Schematically,

\[
\boxed{
\text{W1 direction compression}
\to
\text{strict weighted pressure tail}
\to
\text{L5-critical spacetime action}
\to
\text{logarithmic endpoint divergence allowed}.
}
\]

Thus the pressure-tail route reaches the same critical clock already encountered for `D3`, streamline-amplitude transport and large weak-`L3` saturation.

## 5. Route status

Generic pressure estimates, weighted pressure-tail inequalities and their spacetime integration have now been audited to the known critical endpoint.

Further progress on M5 must use a genuinely W1-specific cancellation/compactness statement, not another generic bound of `mathcal P_5` by a critical Serrin quantity.

Possible genuinely new inputs would have to constrain the **geometry or recurrence of the threshold pressure-tail events**, rather than merely their norm size.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
