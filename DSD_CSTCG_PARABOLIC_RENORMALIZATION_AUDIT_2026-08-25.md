# DSD CSTCG parabolic-renormalization audit

Date: 2026-08-25

Status: **PHYSICAL STRAIN SPIKE REINTERPRETED AS SCALE-COVARIANT / CSTCG NOT A PRIMITIVE CONTRADICTION GATE / RENORMALIZED ESCAPE NOT DERIVED / GLOBAL REGULARITY UNPROVED.**

This note audits `DSD_CRITICAL_STRAIN_SPECTRAL_CHARGE_GATE_2026-08-25.md` and `DSD_ACTIVE_STAGE_BKM_ENERGY_COMPATIBILITY_2026-08-25.md`.

The previous notes correctly proved that on positive-density active first-hitting stages the physical `L_x^2` middle-strain norm becomes large while its `L_t^2 L_x^2` budget remains finite and its critical `L_t^4 L_x^2` charge stays order one per active generation.

What requires correction is the interpretation: **physical temporal concentration alone is not necessarily concentration relative to the shrinking Navier-Stokes scale.**

## 1. First-hitting parabolic variables

At generation `j`, use

\[
r_j=\left(\frac{\nu}{W_j}\right)^{1/2}.
\]

Introduce the parabolic variables

\[
\boxed{
y=\frac{x-X_j}{r_j},
\qquad
\tau=\frac{\nu(t-t_j)}{r_j^2}.
}
\]

Normalize the strain tensor by

\[
\boxed{
\Sigma_j(y,\tau)
:=\frac{r_j^2}{\nu}S(x,t).
}
\]

If `lambda_2^+` is the positive middle eigenvalue of `S`, define its normalized counterpart

\[
\boxed{
\Lambda_{2,j}^+(y,\tau)
:=\frac{r_j^2}{\nu}\lambda_2^+(x,t).
}
\]

Let

\[
\boxed{
A_j(\tau)
:=\|\Lambda_{2,j}^+(\cdot,\tau)\|_{L_y^2}^2.
}
\]

## 2. Exact scaling of the physical `L^2` middle-strain norm

Since `dx=r_j^3dy`,

\[
\begin{aligned}
\|\lambda_2^+(t)\|_{L_x^2}^2
&=
\int
\left(\frac{\nu}{r_j^2}\Lambda_{2,j}^+\right)^2
r_j^3dy\\
&=
\boxed{
\frac{\nu^2}{r_j}A_j(\tau).
}
\end{aligned}
\]

Thus a physical growth of order `nu^2/r_j` is exactly an order-one normalized `L_y^2` strain profile.

At a first-hitting endpoint, the bounded-`Z` hypothesis gives

\[
\frac{r_j}{\nu^2}\|\omega(t_j)\|_2^2=Z_j\le Z_*.
\]

Using

\[
\|S\|_2^2=\frac12\|\omega\|_2^2,
\]

one has

\[
\boxed{
\|\Sigma_j(\cdot,0)\|_2^2=\frac12Z_j\le\frac12Z_*.
}
\]

So the endpoint strain state is already order one in these variables.

## 3. The critical `L_t^4L_x^2` charge is exactly scale invariant

The previous note proved on every active stage

\[
\int_{t_j}^{t_{j+1}}
\|\lambda_2^+(t)\|_2^4dt
\ge
\kappa_2\nu^3.
\]

But

\[
dt=\frac{r_j^2}{\nu}d\tau,
\]

and therefore

\[
\begin{aligned}
\nu^{-3}
\int
\|\lambda_2^+\|_2^4dt
&=
\nu^{-3}
\int
\left(\frac{\nu^2}{r_j}A_j(\tau)\right)^2
\frac{r_j^2}{\nu}d\tau\\
&=
\boxed{
\int A_j(\tau)^2d\tau.
}
\end{aligned}
\]

Hence the active-stage result is simply

\[
\boxed{
\int A_j(\tau)^2d\tau\ge\kappa_2.
}
\]

This is an order-one normalized critical charge. It does **not** imply that the normalized profile itself becomes increasingly singular from one generation to the next.

## 4. The finite energy-level charge is weighted by `r_j`

Similarly,

\[
\begin{aligned}
\int_{t_j}^{t_{j+1}}
\|\lambda_2^+(t)\|_2^2dt
&=
\int
\frac{\nu^2}{r_j}A_j(\tau)
\frac{r_j^2}{\nu}d\tau\\
&=
\boxed{
\nu r_j\int A_j(\tau)d\tau.
}
\end{aligned}
\]

The global energy-level estimate therefore controls a weighted series of the form

\[
\boxed{
\sum_j r_j
\int A_j(\tau)d\tau<\infty
}
\]

up to the fixed viscosity factor.

Because

\[
\sum_jr_j<\infty,
\]

this finite budget is fully compatible with

\[
\int A_jd\tau\asymp1
\]

on every generation.

Thus the coexistence

\[
L_t^2L_x^2\text{ finite},
\qquad
L_t^4L_x^2\text{ critical charge divergent by generations}
\]

does not, after renormalization, require any super-parabolic concentration.

## 5. Explicit scale-covariant model of all current bounds

Consider only a bookkeeping profile, not a Navier-Stokes solution, with

\[
A_j(\tau)=A_*(\tau)
\]

for every generation, where

\[
0<\int A_*^2d\tau<\infty,
\qquad
0<\int A_*d\tau<\infty.
\]

Then automatically

\[
\int\|\lambda_2^+\|_2^4dt
\asymp\nu^3
\]

per generation, while

\[
\int\|\lambda_2^+\|_2^2dt
\asymp\nu r_j.
\]

Therefore

\[
\sum_j
\int\|\lambda_2^+\|_2^2dt<\infty
\]

but

\[
\sum_j
\nu^{-3}
\int\|\lambda_2^+\|_2^4dt=\infty.
\]

Also

\[
\sup_t\|\lambda_2^+(t)\|_2^2
\asymp\frac{\nu^2}{r_j}\to\infty.
\]

So the previously derived physical `high/narrow` behavior is reproduced by a completely stationary normalized profile.

This model is used only to test logical implication. It is **not** asserted to solve Navier-Stokes.

Status: **PROVED AS A SCALING-COMPATIBILITY COUNTERMODEL TO THE INTERPRETATION, NOT TO THE PDE.**

## 6. BKM persistence has the same parabolic scaling

The previous BKM audit proved on every active stage

\[
\int_{t_j}^{t_{j+1}}\|\omega(t)\|_\infty dt
\ge\beta_*>0
\]

and

\[
\Delta t_j
\gtrsim
\frac{r_j^2}{\nu}.
\]

Under the same parabolic variable,

\[
\int\|\omega\|_\infty dt
=
\int
\left(\frac{\nu}{r_j^2}\mathcal W_j(\tau)\right)
\frac{r_j^2}{\nu}d\tau
=
\int\mathcal W_j(\tau)d\tau.
\]

Thus the fixed BKM charge and minimum duration are also exactly natural order in the normalized variables.

Likewise, the mandatory kinetic-energy dissipation

\[
D_j^{cross}\gtrsim\nu^2r_j
\]

is precisely the geometrically weighted physical cost expected from an order-one normalized stage.

## 7. DSD audit: what was formed, and what was only scale drift

DSD requires a distinction between

1. **physical amplitude growth caused by changing the reference scale**, and
2. **new normalized structural concentration within that scale**.

The previous physical statement

\[
\operatorname*{ess\,sup}_{I_j}
\|\lambda_2^+\|_2^2\to\infty
\]

is valid.

But it does not imply

\[
\operatorname*{ess\,sup}_{\tau}
A_j(\tau)\to\infty.
\]

Nor does it imply shrinking normalized temporal support, loss of normalized compactness, or divergence of an order-one normalized derivative channel.

Therefore the phrase **Critical Strain Temporal-Concentration Gate (CSTCG)** is too strong if it refers only to the physical spike already proved.

The primitive CSTCG is pruned in that form.

## 8. Corrected remaining gate

A genuinely new obstruction would require a renormalized escape such as at least one of

\[
\boxed{
\sup_\tau A_j(\tau)\to\infty,
}
\]

or

\[
\boxed{
\text{normalized temporal support of the critical charge}\to0,
}
\]

or

\[
\boxed{
\text{loss of compactness / recurrence in a formed normalized strain state},
}
\]

or another scale-invariant quantity that cannot remain order one on infinitely many generations.

None of these statements has been derived from the current active-stage balances.

Call the corrected question the **Renormalized Critical-Strain Escape Gate (RCSEG)**:

\[
\boxed{
\text{Do the bounded-}Z\text{ first-hitting equations force a genuinely}\
\text{noncompact escape in the normalized middle-strain channel?}
}
\]

Current status:

\[
\boxed{\text{RCSEG: NOT DERIVED.}}
\]

## 9. Relation to recurrent/self-similar routes

The audit changes the next strategic direction.

If the normalized strain/vorticity states remain order one and approach a recurrent or approximately stationary profile, then the problem is no longer one of raw temporal concentration. It becomes a **renormalized recurrence / ancient-profile compatibility** question.

The repository already contains ancient-solution, recurrence, and genealogy branches. Those results should be re-used before creating a new derivative ladder.

Conversely, if normalized compactness fails, that failure itself must be represented by a finite formed witness: spatial escape, derivative escape, shape drift, or another scale-invariant channel.

## 10. Audit verdict

### PROVED

- exact parabolic rescaling of the `L_x^2` middle-strain norm;
- exact scale invariance of the active `L_t^4L_x^2` charge;
- energy-level `L_t^2L_x^2` cost equals `nu r_j` times a normalized order-one charge;
- fixed BKM charge, parabolic persistence, and `nu^2 r_j` energy cost are all compatible with an order-one repeating normalized stage;
- physical strain spikes do not imply normalized strain concentration.

### PRUNED / CORRECTED

- CSTCG as a primitive gate based only on physical high/narrow strain spikes.

### NOT DERIVED

- normalized middle-strain amplitude blowup;
- shrinking normalized support;
- normalized loss of compactness;
- RCSEG;
- contradiction to the bounded-`Z` singular branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
