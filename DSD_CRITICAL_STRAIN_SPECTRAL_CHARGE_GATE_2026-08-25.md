# DSD critical strain spectral charge gate

Date: 2026-08-25

Status: **ACTIVE FIRST-HITTING STAGE -> FIXED CRITICAL STRAIN CHARGE PROVED / POSITIVE-DENSITY CRITICAL CHARGE DIVERGENCE PROVED / L2-STRAIN TEMPORAL CONCENTRATION PROVED / NO CONTRADICTION WITH KNOWN REGULARITY THEORY / GLOBAL REGULARITY UNPROVED.**

This note continues `DSD_RENORMALIZED_ENSTROPHY_FORMATION_BALANCE_2026-08-25.md` and sharpens the open Stretching Budget-Closure Gate (SBCG).

The aim is to replace the unsigned phrase "large vortex stretching" by a finite, scale-critical spectral witness carried by the positive middle eigenvalue of the strain tensor.

## 1. Previous active-stage input

Let

\[
Z_j:=\frac{r_j}{\nu^2}\|\omega(t_j)\|_2^2,
\qquad
z_a\le Z_j\le Z_*,
\]

and let

\[
\lambda:=\frac{r_j}{r_{j+1}}>1.
\]

The previous note defined

\[
N_j
:=
\frac{r_j}{\nu^2}
\int_{t_j}^{t_{j+1}}
\left[
\int\omega^TS\omega\,dx
-\nu\|\nabla\omega\|_2^2
\right]dt
\]

and proved

\[
N_j=\frac12(\lambda Z_{j+1}-Z_j).
\]

There exist constants

\[
\eta>0,
\qquad
p_0>0,
\]

such that a positive asymptotic fraction of sufficiently late stages satisfy

\[
\boxed{N_j\ge\eta.}
\]

Call these indices **active stages**.

## 2. Active net formation gives a fixed multiplicative enstrophy jump

Let

\[
E_S(t):=\|S(t)\|_2^2
=\frac12\|\omega(t)\|_2^2.
\]

At a first-hitting time,

\[
E_S(t_j)
=\frac{\nu^2}{2r_j}Z_j.
\]

Also

\[
N_j
=\frac{r_j}{\nu^2}
\left(E_S(t_{j+1})-E_S(t_j)\right).
\]

Therefore

\[
\frac{E_S(t_{j+1})}{E_S(t_j)}
=
1+\frac{2N_j}{Z_j}.
\]

On an active stage, using `Z_j <= Z_*`,

\[
\boxed{
\frac{E_S(t_{j+1})}{E_S(t_j)}
\ge
1+\delta_* ,
\qquad
\delta_*:=\frac{2\eta}{Z_*}>0.
}
\]

Thus every active first-hitting generation contains a fixed nonzero multiplicative increase of strain enstrophy.

Status: **PROVED.**

## 3. Critical middle-strain regularity inequality

Let

\[
\lambda_1(x,t)\le\lambda_2(x,t)\le\lambda_3(x,t)
\]

be the eigenvalues of the symmetric strain tensor `S`, and define

\[
\lambda_2^+:=\max\{\lambda_2,0\}.
\]

A known scale-critical regularity estimate for 3D incompressible Navier-Stokes gives, after restoring viscosity `nu`,

\[
\boxed{
E_S(t_2)
\le
E_S(t_1)
\exp\left[
C_s\nu^{-(p-1)}
\int_{t_1}^{t_2}
\|\lambda_2^+(t)\|_{L^s}^pdt
\right],
}
\]

where

\[
\frac{2}{p}+\frac{3}{s}=2,
\qquad
\frac32<s\le\infty.
\]

This is the middle-eigenvalue strain criterion proved by Evan Miller, `A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor`, Arch. Rational Mech. Anal. 235 (2020), DOI: 10.1007/s00205-019-01419-z.

The use here is only as an already-proved Navier-Stokes inequality; DSD adds no physical or PDE assumption to it.

## 4. Fixed critical spectral charge on every active stage

Apply the inequality to an active stage `[t_j,t_{j+1}]`.

The lower multiplicative jump from Section 2 and the regularity inequality imply

\[
1+\delta_*
\le
\exp\left[
C_s\nu^{-(p-1)}
\int_{t_j}^{t_{j+1}}
\|\lambda_2^+\|_{L^s}^pdt
\right].
\]

Hence

\[
\boxed{
\nu^{-(p-1)}
\int_{t_j}^{t_{j+1}}
\|\lambda_2^+\|_{L^s}^pdt
\ge
\kappa_s,
}
\]

where

\[
\boxed{
\kappa_s
:=
\frac{1}{C_s}
\log(1+\delta_*)
=
\frac{1}{C_s}
\log\left(1+\frac{2\eta}{Z_*}\right)
>0.
}
\]

Thus each active generation spends an order-one amount of a **scale-critical middle-strain spectral charge**.

Status: **PROVED, conditional only on the previously established bounded-Z active-stage hypotheses and the cited standard regularity inequality.**

## 5. Positive-density stages force linear-in-generation critical charge

Let

\[
A_{J,N}
:=
\{j\in\{J,\dots,N-1\}:N_j\ge\eta\}.
\]

The previous note proved

\[
\liminf_{N-J\to\infty}
\frac{|A_{J,N}|}{N-J}
\ge p_0>0.
\]

Since the stage intervals are disjoint up to endpoints,

\[
\begin{aligned}
\nu^{-(p-1)}
\int_{t_J}^{t_N}
\|\lambda_2^+\|_{L^s}^pdt
&\ge
\sum_{j\in A_{J,N}}
\nu^{-(p-1)}
\int_{t_j}^{t_{j+1}}
\|\lambda_2^+\|_{L^s}^pdt\\
&\ge
\kappa_s |A_{J,N}|.
\end{aligned}
\]

Therefore

\[
\boxed{
\liminf_{N-J\to\infty}
\frac{1}{N-J}
\nu^{-(p-1)}
\int_{t_J}^{t_N}
\|\lambda_2^+\|_{L^s}^pdt
\ge
p_0\kappa_s>0.
}
\]

Consequently, along the hypothetical bounded-Z singular branch,

\[
\boxed{
\int^{T^*}
\|\lambda_2^+(t)\|_{L^s}^pdt
=+\infty
}
\]

for every admissible critical pair `(p,s)` above.

This is stronger than merely saying that the total critical norm diverges: under the branch hypotheses, the divergence carries a fixed positive charge on a positive density of first-hitting generations.

Status: **PROVED.**

## 6. The concrete `s=2, p=4` channel

Choose

\[
s=2,
\qquad
p=4.
\]

Then every active stage satisfies

\[
\boxed{
\int_{t_j}^{t_{j+1}}
\|\lambda_2^+(t)\|_2^4dt
\ge
\kappa_2\nu^3.
}
\]

At the same time,

\[
\|\lambda_2^+\|_2^2
\le
\|S\|_2^2.
\]

The kinetic-energy equality gives

\[
\nu\int_0^{T^*}\|\nabla u\|_2^2dt
\le
\frac12\|u_0\|_2^2,
\]

and

\[
\|S\|_2^2=\frac12\|\nabla u\|_2^2.
\]

Hence

\[
\boxed{
\int_0^{T^*}\|\lambda_2^+(t)\|_2^2dt
\le
\frac{\|u_0\|_2^2}{4\nu}
<\infty.
}
\]

Thus this branch must simultaneously have

\[
\lambda_2^+
\in L_t^2L_x^2
\]

in the energy-controlled sense, while its critical

\[
L_t^4L_x^2
\]

charge diverges with fixed positive cost per active generation.

## 7. Temporal concentration consequence

Define

\[
a(t):=\|\lambda_2^+(t)\|_2^2.
\]

For each active stage `j`, let

\[
m_j:=\int_{t_j}^{t_{j+1}}a(t)dt.
\]

Because the active intervals are disjoint and

\[
\int_0^{T^*}a(t)dt<\infty,
\]

one has

\[
m_j\to0
\]

along any infinite sequence of active stages.

But Section 6 gives

\[
\int_{t_j}^{t_{j+1}}a(t)^2dt
\ge
\kappa_2\nu^3.
\]

Since

\[
\int_I a^2
\le
(\operatorname*{ess\,sup}_I a)
\int_I a,
\]

we obtain

\[
\boxed{
\operatorname*{ess\,sup}_{t\in[t_j,t_{j+1}]}
\|\lambda_2^+(t)\|_2^2
\ge
\frac{\kappa_2\nu^3}{m_j}
\to+\infty.
}
\]

Therefore the bounded-Z active branch cannot carry its critical strain charge through a temporally diffuse middle-strain field. It must form increasingly narrow/high `L^2_x` middle-strain bursts.

Status: **PROVED.**

## 8. DSD audit

The finite DSD channel chain is now

\[
\boxed{
\text{first-hitting scale transition}
\to
\text{positive net enstrophy formation}
\to
\text{fixed multiplicative strain-enstrophy growth}
\to
\text{positive middle-strain critical charge}
\to
\text{temporal critical concentration}.
}
\]

This is useful because it distinguishes three different objects that should not be conflated:

1. **formation**: the positive net enstrophy charge `N_j`;
2. **spectral carrier**: the positive middle eigenvalue `lambda_2^+` of the strain;
3. **remaining escape mode**: temporal concentration of a critical strain norm while the lower `L_t^2L_x^2` energy channel remains finite.

The DSD role is classificatory and auditing: it prevents the positive source from being mistaken for a boundary-transfer effect or for an already finite global budget.

## 9. Why this still does not prove global regularity

The result does **not** provide a finite a-priori bound for

\[
\int^{T^*}\|\lambda_2^+\|_{L^s}^pdt.
\]

Known Navier-Stokes regularity theory says precisely that this scale-critical quantity must diverge if a finite-time singularity occurs. Therefore the divergence proved here is compatible with, rather than contradictory to, a hypothetical blowup.

Likewise,

\[
\int a(t)dt<\infty
\qquad\text{and}\qquad
\int a(t)^2dt=\infty
\]

are perfectly compatible through temporal spikes.

So the previous SBCG is not closed. It has been decomposed into a sharper terminal question:

\[
\boxed{
\text{Can the first-hitting / bounded-Z hypotheses themselves forbid the required}\
\text{positive-density temporal concentration of }\lambda_2^+\text{?}
}
\]

Call this the **Critical Strain Temporal-Concentration Gate (CSTCG)**.

Current status:

\[
\boxed{\text{CSTCG: NOT DERIVED.}}
\]

## 10. Audit verdict

### PROVED

- active `N_j` implies a fixed multiplicative strain-enstrophy jump;
- every active stage carries a fixed positive scale-critical `lambda_2^+` charge;
- positive density of active stages implies linear-in-generation accumulation and total divergence of every admissible middle-strain critical norm;
- in the `L_t^4L_x^2` channel, the critical divergence coexists with a finite energy-level `L_t^2L_x^2` budget;
- this coexistence forces temporal concentration of the middle-strain `L_x^2` norm.

### NOT DERIVED

- an upper bound on the critical middle-strain charge;
- exclusion of temporal critical spikes from first-hitting hypotheses alone;
- CSTCG;
- contradiction to the bounded-Z singular branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
