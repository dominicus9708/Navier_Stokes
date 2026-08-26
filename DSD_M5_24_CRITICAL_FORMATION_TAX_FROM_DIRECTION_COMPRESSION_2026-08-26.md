# DSD M5-24 — Critical Formation Tax from Direction Compression

Date: 2026-08-26

Status: **DERIVED INSTANTANEOUS SCALE TAX + CONDITIONAL PARABOLIC-EVENT INTEGRATION / FIRST-HITTING DIRECTION COMPRESSION IS SUBCRITICAL FOR ORDINARY ENERGY BUT CRITICAL FOR `D3` AND STREAMLINE-AMPLITUDE TRANSPORT / THIS RECOVERS THE KNOWN W1 STRONG-ENDPOINT FAILURE RATHER THAN CLOSING IT / GLOBAL REGULARITY UNPROVED.**

## 1. Input from M5-23

At a first-hitting event for a large physical amplitude threshold `L`, M5-23 gives a normalized direction-compression floor

\[
\|\mathbf1_{\{|V|>1\}}\operatorname{div}_z n\|_2
\ge d_*>0,
\]

where

\[
z=L(x-X_*),
\qquad
n=\frac{u}{|u|}.
\]

Since

\[
\operatorname{div}_z n
=L^{-1}\operatorname{div}_x n,
\qquad
dz=L^3dx,
\]

we obtain the physical instantaneous floor

\[
\boxed{
\int_{\{|u|>L\}}
|\operatorname{div}_x n|^2dx
\ge
\frac{d_*^2}{L}.
}
\]

The active region is understood in the W1 phase-space window associated with the threshold.

## 2. Ordinary enstrophy cost

On the active region

\[
|u|\ge L.
\]

Since

\[
|\nabla n|^2
\ge
\frac13|\operatorname{div}n|^2
\]

pointwise up to the elementary matrix norm constant, the direction part of ordinary enstrophy satisfies

\[
\int |u|^2|\nabla n|^2dx
\ge
cL^2
\int_{|u|>L}|\operatorname{div}n|^2dx.
\]

Therefore

\[
\boxed{
\int |u|^2|\nabla n|^2dx
\ge
c d_*^2 L.
}
\]

At the natural parabolic duration

\[
\Delta t_L\sim L^{-2},
\]

the corresponding ordinary viscous cost scales as

\[
L\Delta t_L\sim L^{-1}.
\]

Hence over geometric thresholds `L_j~2^j`,

\[
\sum_jL_j^{-1}<\infty.
\]

Thus the first-hitting direction-compression mechanism is fully compatible with finite ordinary total dissipation.

## 3. Critical `p=3` direction cost

The direction part of the cubic dissipation is

\[
D_{3,dir}(u)
:=
\int |u|^3|\nabla n|^2dx.
\]

Using the same floor,

\[
D_{3,dir}
\ge
cL^3
\int_{|u|>L}|\operatorname{div}n|^2dx.
\]

Therefore at the first hitting,

\[
\boxed{
D_{3,dir}(t_L)
\ge
c d_*^2 L^2.
}
\]

This is the critical scaling: multiplication by one parabolic time unit `L^{-2}` gives order one.

## 4. Event-duration audit

An instantaneous lower bound does not by itself yield a time-integrated lower bound.

To obtain one fixed normalized duration, one needs uniform local-in-`z, sigma` continuity of the active W1 phase-space cell. In the late W1 corridor this is consistent with the retained local smoothness/compactness assumptions after rescaling, but the duration must not be silently assumed.

If the local W1 compactness gives a fixed normalized interval

\[
|\sigma-\sigma_L|\le c_0
\]

on which a fixed fraction of the direction-compression floor persists, then in physical time

\[
\Delta t_L\ge c_0L^{-2}.
\]

Under this explicit persistence hypothesis,

\[
\boxed{
\int_{J_L}D_{3,dir}(t)dt
\ge c_{D3}>0
}
\]

with a constant independent of `L`.

This is a **critical per-scale tax**, not an ordinary energy tax.

## 5. Streamline-amplitude transport cost

Define

\[
e:=u\cdot\nabla|u|.
\]

Incompressibility gives

\[
\boxed{
e=-|u|^2\operatorname{div}n.}
\]

In the normalized phase-space variables,

\[
e(x,t)=L^3 e_V(z,\sigma),
\]

and therefore

\[
\|e(t)\|_{L^{3/2}_x}
=L\|e_V(\sigma)\|_{L^{3/2}_z}.
\]

On the fixed normalized active cell, `|V|>=1`; together with the direction-compression floor and the fixed-volume/amplitude bounds, the W1 local compactness converts the nonzero direction-compression event into a nonzero normalized `L^{3/2}` amplitude-transport event.

If that event persists for a fixed normalized time interval as in Section 4, then

\[
\boxed{
\int_{J_L}
\|u\cdot\nabla|u|\|_{L^{3/2}}^2dt
\ge c_e>0.
}
\]

Again the scale factors cancel:

\[
L^2\times L^{-2}=1.
\]

## 6. Comparison with previous W1 endpoint saturation

Earlier W1 audits already found that a nontrivial recurrent survivor must saturate the critical clocks:

\[
D_{3,phys}
\in L_t^{1,\infty}
\setminus L_t^1
\]

schematically at the endpoint, and

\[
u\cdot\nabla|u|
\in L_t^{2,\infty}L_x^{3/2}
\setminus L_t^2L_x^{3/2}.
\]

M5-24 identifies a concrete formation mechanism for that strong-endpoint failure:

\[
\boxed{
\text{large-threshold first hit}
\to
\text{pressure-coupled direction compression}
\to
\text{order-one critical `D3` / amplitude-transport action per scale}.
}
\]

Thus the logarithmic endpoint divergence is not an abstract tail artifact; it is tied to the repeated creation of new high-amplitude state boundaries.

## 7. Why this still does not close M5

The critical taxes in Sections 3--5 are not controlled by the classical finite-energy inequality.

Ordinary energy and ordinary dissipation only see the summable per-scale cost `~L^{-1}`.

Therefore summing the order-one `D3` or amplitude-transport tax over infinitely many scales proves only that the strong critical endpoint diverges, which is already compatible with the hypothetical W1 singular survivor.

Hence

\[
\boxed{
\text{critical formation tax}
\neq
\text{contradiction without an independently finite critical budget}.
}
\]

## 8. Updated DSD picture

The formation chain is now

\[
\boxed{
\begin{array}{c}
K\text{-defect at threshold }L\\
\Downarrow\\
\text{first-hitting pressure source}\\
\Downarrow\\
\text{direction compression at }r\sim L^{-1}\\
\Downarrow\\
D_{3,dir}(t_L)\sim L^2\\
\Downarrow\\
\text{order-one critical action over }L^{-2}\text{ time}.
\end{array}
}
\]

This closes the formation ledger but not the regularity theorem.

## 9. Next target

A further proof step must exploit something beyond the existence of the critical tax. Candidate mechanisms are:

1. a finite critical budget not already known to diverge under W1;
2. a cross-scale incompatibility preventing every threshold from paying the same pressure-driven direction-compression tax;
3. a conversion constraint between the first-hitting gradient/Hodge source and the mature solenoidal/helical excess;
4. an established direction regularity criterion plus a new upper estimate from finite-energy/W1 data.

The most W1-specific next route is item 3: determine whether every newly created gradient excess must convert into solenoidal/helical critical content before it can support the recurrent W1 defect, and whether that conversion has an additional non-reusable cost.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
