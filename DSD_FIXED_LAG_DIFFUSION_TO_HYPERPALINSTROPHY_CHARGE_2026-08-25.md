# DSD Fixed-Lag Diffusion Erosion -> Hyperpalinstrophy Charge

Date: 2026-08-25

Status: **DIFFUSION-EROSION EVENT FORCES A FIXED NORMALIZED HYPERPALINSTROPHY SPACETIME CHARGE / POSITIVE-DENSITY E-BRANCH GIVES A MEAN-R LOWER BOUND / EXPLICIT COMPARISON WITH THE EXISTING MEAN-R CAP DERIVED / CONSTANT CLOSURE NOT YET VERIFIED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The fixed-lag exposure audit reduced the `E` branch of FPIRG to one finite diffusion-erosion threshold.

Let

\[
n=j-k_0
\]

with fixed finite `k_0`.

The ancestor-normalized diffusion exposure is

\[
\mathcal D_n([t_n,t])
=
\frac\nu{W_n}
\int_{t_n}^{t}
\sup_{A_n(s)}|\Delta\omega(s)|ds.
\]

The aim is to show that

\[
\mathcal D_n\ge d_0>0
\]

cannot be a cost-free pointwise derivative event.

Stage-wide analyticity forces spatial persistence, converting it to an `L2` hyperpalinstrophy-time charge.

---

## 2. Parent-ancestor normalized variables

Use the stage-`n` parent coordinates throughout the fixed-lag interval:

\[
y=\frac{x-X_n}{r_n},
\qquad
r_n=\sqrt{\frac\nu{W_n}},
\]

\[
\Omega_n(y,t)=\frac{\omega(x,t)}{W_n},
\qquad
\tau=W_n(t-t_n).
\]

Then

\[
\Delta_y\Omega_n
=
\frac{r_n^2}{W_n}\Delta_x\omega
=
\frac\nu{W_n^2}\Delta_x\omega,
\]

and

\[
d\tau=W_ndt.
\]

Therefore exactly

\[
\boxed{
\mathcal D_n
=
\int_0^{T_n}
F_n(\tau)d\tau,
}
\]

where

\[
\boxed{
F_n(\tau)
:=
\sup_{y\in A_n(\tau)}
|\Delta_y\Omega_n(y,\tau)|
}
\]

and

\[
T_n:=W_n(t-t_n).
\]

Thus the material diffusion exposure is precisely an `L1_tau L-infinity_x` second-vorticity-derivative quantity in the ancestor normalization.

Status: **PROVED EXACTLY.**

---

## 3. Fixed-lag normalized time ceiling

The interval from stage `n` to a witness in stage `j=n+k_0` crosses at most `k_0+1` complete/partial first-hitting stages.

For stage `n+h`,

\[
W_{n+h}|I_{n+h}|
\le L_+.
\]

Since

\[
W_n/W_{n+h}=q^{-h},
\]

we have

\[
\begin{aligned}
T_n
&=W_n(t-t_n)\\
&\le
L_+\sum_{h=0}^{k_0}q^{-h}.
\end{aligned}
\]

Therefore

\[
\boxed{
T_n\le T_{fix}:=
L_+\frac{1-q^{-(k_0+1)}}{1-q^{-1}}
<\frac{L_+}{1-q^{-1}}.
}
\]

Status: **PROVED.**

---

## 4. Third-derivative ceiling in ancestor coordinates

The stage-wide analyticity corridor gives, in the natural parent coordinates of every intermediate stage `m=n+h`,

\[
\|\nabla^3\Omega_m\|_\infty
\le C_{3,an}.
\]

Convert this to the fixed stage-`n` coordinates.

Physical third derivatives satisfy

\[
\|\nabla_x^3\omega\|_\infty
\le
C_{3,an}
\frac{W_m}{r_m^3}.
\]

Since

\[
\nabla_y^3\Omega_n
=
\frac{r_n^3}{W_n}\nabla_x^3\omega,
\]

and

\[
\frac{r_n^3W_m}{W_nr_m^3}
=
\left(\frac{W_m}{W_n}\right)^{5/2},
\]

we obtain

\[
\boxed{
\|\nabla_y^3\Omega_n\|_\infty
\le
K_{3,fix}:=
C_{3,an}q^{5k_0/2}.
}
\]

In particular,

\[
\boxed{
\|\nabla_y\Delta_y\Omega_n\|_\infty
\le C_\Delta K_{3,fix}
}
\]

for a fixed tensor-contraction constant `C_Delta`.

Absorb `C_Delta` into `K_{3,fix}` below.

Status: **PROVED.**

---

## 5. Pointwise second derivative forces an L2 packet

Fix a normalized time `tau` and choose a point in the material packet where

\[
|\Delta\Omega_n|=F_n(\tau)
\]

up to an arbitrarily small approximation.

Because `Delta Omega_n` is `K_3,fix`-Lipschitz, on the ball

\[
|y-y_0|
\le
\ell(\tau)
:=
\frac{F_n(\tau)}{2K_{3,fix}},
\]

we have

\[
|\Delta\Omega_n(y,\tau)|
\ge
\frac12F_n(\tau).
\]

Therefore

\[
\begin{aligned}
\|\Delta\Omega_n(\tau)\|_2^2
&\ge
\frac{F_n(\tau)^2}{4}
\frac{4\pi}{3}
\left(\frac{F_n(\tau)}{2K_{3,fix}}\right)^3\\
&=
\frac{\pi}{24K_{3,fix}^3}
F_n(\tau)^5.
\end{aligned}
\]

Hence

\[
\boxed{
R_n(\tau)
:=
\|\Delta\Omega_n(\tau)\|_2^2
\ge
\frac\pi{24K_{3,fix}^3}F_n(\tau)^5.
}
\]

This is a finite-order spatial persistence lemma; no infinite derivative ladder is used.

Status: **PROVED.**

---

## 6. Integrated diffusion exposure forces hyperpalinstrophy-time charge

Suppose the diffusion-erosion event satisfies

\[
\boxed{
\mathcal D_n
=
\int_0^{T_n}F_n(\tau)d\tau
\ge d_0>0.
}
\]

Holder on the interval of length at most `T_fix` gives

\[
\int_0^{T_n}F_n^5d\tau
\ge
\frac{\left(\int_0^{T_n}F_nd\tau\right)^5}{T_n^4}
\ge
\frac{d_0^5}{T_{fix}^4}.
\]

Combining with the spatial persistence inequality,

\[
\boxed{
\int_0^{T_n}R_n(\tau)d\tau
\ge
H_{eros}
:=
\frac{\pi}{24K_{3,fix}^3T_{fix}^4}
\,d_0^5
>0.
}
\]

Thus a fixed-lag diffusion-erosion event pays a fixed positive normalized hyperpalinstrophy spacetime charge.

Status: **PROVED.**

---

## 7. Convert to standard backward-Leray hyperpalinstrophy

Let standard Leray vorticity be

\[
W_L(Y,s)=(T^*-t)\omega(x,t).
\]

For the stage-`n` parent normalization define

\[
\Theta_n(t)=W_n(T^*-t).
\]

The exact scale relation is

\[
W_L=\Theta_n\Omega_n,
\qquad
Y=\sqrt{\frac\nu{\Theta_n}}\,y
\]

up to translation.

Therefore

\[
\Delta_YW_L
=
\frac{\Theta_n^2}{\nu}\Delta_y\Omega_n
\]

and

\[
\boxed{
R_L(s)
:=
\|\Delta_YW_L\|_2^2
=
\Theta_n^{5/2}\nu^{-1/2}R_n(\tau).
}
\]

Also

\[
ds=\frac{d\tau}{\Theta_n}.
\]

Hence

\[
\boxed{
R_L(s)ds
=
\Theta_n^{3/2}\nu^{-1/2}
R_n(\tau)d\tau.
}
\]

On the two-sided first-hitting/Leray recurrent corridor, for a point at most `k_0` generations after stage `n`, there is a fixed lower bound

\[
\boxed{
\Theta_n(t)
\ge
\Theta_{fix,-}
:=q^{-(k_0+1)}\Theta_->0.
}
\]

Therefore every erosion event gives

\[
\boxed{
\int_{I_{eros}}R_L(s)ds
\ge
H_{L,eros}
:=
\Theta_{fix,-}^{3/2}\nu^{-1/2}H_{eros}
>0.
}
\]

Status: **PROVED on the stated recurrent clock corridor.**

---

## 8. Positive-density erosion events force a positive mean-R floor

Suppose the erosion branch occurs on a recurrent Leray-time set `E` of lower density

\[
\boxed{d_E>0.}
\]

Each event is associated with a backward fixed-lag interval whose Leray length is bounded above by a fixed constant `S_fix` depending only on

\[
k_0,q,\Theta_\pm,L_+.
\]

Choose a maximal set of event times separated by more than `S_fix`.

The associated backward intervals are disjoint, while maximality implies that intervals of radius `S_fix` around the selected times cover `E`.

Therefore over a long Leray interval of length `S`, the number `N(S)` of selected events obeys asymptotically

\[
N(S)
\ge
\frac{d_E}{2S_{fix}}S-o(S).
\]

Summing the disjoint hyperpalinstrophy charges,

\[
\int_0^S R_L(s)ds
\ge
N(S)H_{L,eros}.
\]

Thus

\[
\boxed{
\overline R_L
\ge
\frac{d_E}{2S_{fix}}
H_{L,eros}.
}
\]

This is an explicit positive mean hyperpalinstrophy floor generated solely by positive-density diffusion erosion.

Status: **PROVED under the positive-density branch hypothesis.**

---

## 9. Compare with the existing recurrent mean-R cap

`DSD_RECURRENT_H1_AGMON_HYPERPALINSTROPHY_CAP_2026-08-25.md` proves

\[
\boxed{
\overline R_L
\le
R_{cap}
:=
\frac{C_*^8}{16}
\frac{Z_+^5}{\nu^8}.
}
\]

Therefore a positive-density diffusion-erosion branch is impossible whenever

\[
\boxed{
\frac{d_E}{2S_{fix}}
H_{L,eros}
>
R_{cap}.
}
\]

Substituting the event charge,

\[
\boxed{
\frac{d_E}{2S_{fix}}
\Theta_{fix,-}^{3/2}\nu^{-1/2}
\frac{\pi d_0^5}
{24K_{3,fix}^3T_{fix}^4}
>
\frac{C_*^8}{16}
\frac{Z_+^5}{\nu^8}.
}
\]

This is the **Diffusion-Erosion Mean Hyperpalinstrophy Closure Test (DEMHCT)**.

Status: **PROVED SUFFICIENT CLOSURE CONDITION / NOT NUMERICALLY VERIFIED.**

---

## 10. Relation to the FPIRG finite partition

FPIRG gives a positive-density finite partition

\[
E\lor R\lor T_{multi}
\]

on the fixed-shell witness set.

If `E` is the selected positive-density survivor, its density has a positive lower bound inherited from the witness set and finite pigeonhole partition.

Thus DEMHCT can be evaluated using that branch-density lower bound rather than an arbitrarily small unspecified density once all preceding constants are made explicit.

If DEMHCT fails numerically, the E branch is still no longer a qualitative derivative escape: it is a quantitatively bracketed mean-`R` channel between an explicit positive floor and the existing finite upper cap.

---

## 11. DSD audit

The argument uses the finite derivative channels

- `Delta Omega` amplitude;
- `grad Delta Omega` analytic persistence bound;
- `R=||Delta Omega||_2^2`;
- fixed-lag normalized duration;
- recurrent time density.

No derivative order above third vorticity derivative is used, and no infinite hierarchy is formed.

The pointwise erosion channel and mean hyperpalinstrophy channel are kept distinct until the explicit persistence and averaging steps connect them.

---

## 12. Updated E-branch status

The E branch has now been reduced from

\[
\text{generic local deformation/diffusion failure}
\]

to

\[
\boxed{
\text{positive-density fixed-lag diffusion erosion}
\Longrightarrow
\overline R_L\ge R_{eros,floor}>0.
}
\]

It must coexist with

\[
\boxed{
\overline R_L\le R_{cap}<\infty.
}
\]

The next quantitative task is a constant comparison, not another qualitative derivative case split.

---

## 13. Audit verdict

### PROVED

- `D_n` is exactly an `L1_tau L-infinity_x` normalized second-vorticity-derivative exposure;
- fixed-lag third-derivative analyticity gives spatial persistence;
- one erosion event forces a fixed `integral R_n d tau` charge proportional to `d_0^5`;
- the charge transfers to standard Leray `integral R_L ds` using the two-sided clock corridor;
- positive-density erosion events force a positive recurrent mean-`R` floor;
- DEMHCT is an explicit sufficient closure comparison with the existing Agmon mean-`R` cap.

### NOT DERIVED

- numerical closure of DEMHCT with current inherited constants;
- closure of the positive-density R/contact branch;
- closure of positive-density packet replacement/multicore turnover;
- scale-uniform material return lower bounds for the full cubic tail;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
