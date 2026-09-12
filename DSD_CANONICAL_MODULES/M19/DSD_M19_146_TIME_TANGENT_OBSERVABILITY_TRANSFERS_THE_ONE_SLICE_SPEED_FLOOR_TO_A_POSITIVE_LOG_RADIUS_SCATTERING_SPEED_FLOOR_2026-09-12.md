# DSD M19-146 — Time-tangent observability transfers the one-slice speed floor to a positive log-radius scattering-speed floor

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXACT TIME-SHIFT COVARIANCE IDENTIFIES THE SCATTERING IMAGE OF THE INTERIOR TIME TANGENT WITH -1/2 PARTIAL_q A / M19-131 UNIFORM HARD OBSERVABILITY AND THE M19-096--097/142 ONE-SLICE REGULARITY CONTRAPOSITIVE GIVE A POSITIVE LOWER BOUND ON LOG-RADIUS SCATTERING SPEED FOR ANY SURVIVING SINGULAR HARD ORBIT / STATIONARY OR ARBITRARILY SLOW q-HISTORY IS EXCLUDED ON THIS APPLICATION LANE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Differentiate time covariance at t=0

The exact scattering covariance is

\[
\mathscr S(\sigma_tU)(q)
=
A_U(q-t/2).
\]

Differentiate at `t=0`.
Since

\[
\left.\frac d{dt}\sigma_tU\right|_{t=0}
=
\partial_sU,
\]

we obtain

\[
\boxed{
D\mathscr S_U(\partial_sU)
=
-\frac12\partial_qA_U.
}
\]

This is exact.

---

## 2. Uniform observability of the time tangent

The time tangent is an exact zero-growth hard symmetry mode.
Before quotienting it, M19-131 gives the uniform equivalence

\[
 c_{obs}\|\partial_sU\|_H
\le
\|D\mathscr S_U(\partial_sU)\|_{X_{sc}}
\le
C_{obs}\|\partial_sU\|_H.
\]

Insert the exact scattering derivative:

\[
\boxed{
2c_{obs}\|\partial_sU\|_H
\le
\|\partial_qA\|_{X_{sc}}
\le
2C_{obs}\|\partial_sU\|_H.
}
\]

Thus similarity-time speed in the interior hard core and log-radius speed of the scattering datum are quantitatively equivalent.

---

## 3. One-slice regularity gives an interior speed floor

On the M19-142 certified Pineau--Vicol application lane, a singular survivor cannot possess a sufficiently late slice with the required weighted similarity-time derivative below the regularity threshold.

Hence M19-096 gives

\[
\boxed{
\mathcal V_G(s)
=\int|\partial_sU|(1+|y|)e^{-|y|^2/8}dy
\ge v_*>0
}
\]

for every sufficiently late time.

On the compact finite-dimensional hard symmetry bundle, all retained hard norms are uniformly equivalent. Therefore

\[
\boxed{
\|\partial_sU\|_H
\ge c_Gv_*>0.
}
\]

---

## 4. Positive q-speed floor

Combine Sections 2 and 3:

\[
\boxed{
\|\partial_qA\|_{X_{sc}}
\ge
2c_{obs}c_Gv_*
=:v_q>0.
}
\]

Thus every surviving singular recurrent critical datum on the certified hard lane satisfies

\[
\boxed{
\|\partial_qA\|_{X_{sc}}
\ge v_q>0.
}
\]

The tail cannot be stationary or arbitrarily slowly varying in log radius.

---

## 5. Upper speed bound

Compactness of the smooth hard corridor also gives

\[
\|\partial_sU\|_H\le V^*.
\]

Hence

\[
\boxed{
\|\partial_qA\|_{X_{sc}}
\le2C_{obs}V^*.
}
\]

Therefore the singular hard tail has a two-sided q-speed corridor:

\[
\boxed{
0<v_q
\le
\|\partial_qA\|_{X_{sc}}
\le V_q^*<\infty.
}
\]

---

## 6. Consequences for recurrence classes

### Stationary/self-similar tail

If

\[
\partial_qA=0,
\]

then the speed floor fails.
Thus no nontrivial stationary critical tail survives on this one-slice application lane.

This is consistent with the earlier self-similar Liouville exclusion.

### DSS

For an L-periodic tail,

\[
A(q+L)=A(q),
\]

the periodic history must have nonzero q-speed everywhere in the hard norm sense supplied by the corresponding time slices.

### RSS

M19-125 gives

\[
\partial_qA=-2\alpha\mathcal R_\omega A.
\]

Therefore

\[
\boxed{
2|\alpha|\|\mathcal R_\omega A\|_{X_{sc}}
\ge v_q,
}
\]

recovering the tail form of the RSS rotation-anisotropy lower bound in M19-144.

### Finite-rank quasiperiodic tail

For a Fourier--Bohr expansion

\[
A(q)=\sum_k A_ke^{i\xi_kq},
\]

the speed floor gives a positive lower bound on the frequency-weighted hard amplitude.
It forbids all spectral mass from drifting toward zero q-frequency while keeping the orbit singular.

---

## 7. What this does not prove

A periodic or quasiperiodic curve may move with a positive speed floor forever.
Therefore

\[
\boxed{
\text{positive q-speed}
\neq
\text{periodicity contradiction}.
}
\]

The gain is the removal of stationary/near-stationary degenerations and an exact quantitative link between the external one-slice regularity gate and the far-field scattering dynamics.

---

## 8. Updated hard-core description

On the fully certified late hard lane, a surviving critical recurrent tail must simultaneously have

\[
\boxed{
\begin{aligned}
&A\not\equiv0,\\
&0<v_q\le\|\partial_qA\|_{X_{sc}}\le V_q^*,\\
&\text{finite-dimensional observable neutral hard dynamics},\\
&\text{no positive hard Lyapunov exponent},\\
&\text{the exact pressure/divergence/scattering constraints already retained.}
\end{aligned}
}
\]

The remaining zero-center problem is therefore genuinely an additional neutral phase problem, not a slow-drift artifact.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
