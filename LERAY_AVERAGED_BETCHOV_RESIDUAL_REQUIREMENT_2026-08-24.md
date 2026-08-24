# Leray-Averaged Betchov Residual Requirement — 2026-08-24

Status: **RECURRENT SURVIVOR MUST PAY A POSITIVE AVERAGE NEGATIVE-MIDDLE BETCHOV RESIDUAL UNLESS THE IMPROVED ENSTROPHY GATE ALREADY CLOSES / GLOBAL REGULARITY NOT PROVED.**

This note combines

- `LERAY_ACTIVE_CORE_INVARIANT_MEASURE_2026-08-24.md`;
- `POSITIVE_MIDDLE_BETCHOV_RESIDUAL_PRODUCTION_SPLIT_2026-08-24.md`;
- the tail-independent ancient enstrophy-rigidity route.

The key point is that the Gronwall coefficient need not be controlled pointwise in time. Physical logarithmic time is exactly Leray time, so the invariant probability measure gives the natural average quantity.

---

## 1. Leray enstrophy identity

For the Leray vorticity `W`,

\[
W_s+W+\frac12Y\cdot\nabla W+V\cdot\nabla W
=SW+\nu\Delta W.
\]

Set

\[
Z_L(s):=\|W(s)\|_2^2,
\qquad
Q_L(s):=\|\nabla W(s)\|_2^2,
\]

\[
P_L(s):=\int W^TSW\,dY.
\]

Multiplication by `W` and integration give

\[
\boxed{
\frac12 Z_L'
+\frac14 Z_L
+\nu Q_L
=P_L.
}
\]

The coefficient `1/4` comes from the combination of the `+W` term and the dilation term `(1/2)Y dot grad W` in three dimensions.

---

## 2. Leray form of the production split

Let

\[
M_L(s):=\|W(s)\|_\infty.
\]

Define the Leray negative-middle Betchov residual

\[
\mathcal R_{B,L}(s)
:=\int_{\{\lambda_2(S)<0\}}
\bigl(W^TSW+4\det S\bigr)_+\,dY.
\]

The production split is scale invariant, so

\[
\boxed{
P_L(s)
\le
\frac12 M_L(s)Z_L(s)
+\mathcal R_{B,L}(s).
}
\]

---

## 3. Average under the invariant measure

Let `mu` be a Leray invariant probability measure supported on the compact local orbit closure and carrying positive active-core mass.

For an invariant measure, the average of the time derivative of the bounded smooth observable `Z_L` vanishes after standard truncation/approximation if needed. Equivalently, average the exact identity over long Leray intervals and pass to the invariant limit. Then

\[
\boxed{
\frac14\langle Z_L\rangle_\mu
+\nu\langle Q_L\rangle_\mu
=
\langle P_L\rangle_\mu.
}
\]

Hence

\[
\boxed{
\frac14\langle Z_L\rangle
+\nu\langle Q_L\rangle
\le
\frac12\langle M_LZ_L\rangle
+\langle\mathcal R_{B,L}\rangle.
}
\]

The brackets below denote this invariant/Leray-time average.

---

## 4. First-hitting amplitude ceiling gives a compulsory residual

The continuous backward first-hitting bound gives

\[
M_L(s)=|t|\,\|\Omega(t)\|_\infty
\le K_I
\]

on the restricted ancient branch. Therefore

\[
\langle M_LZ_L\rangle
\le K_I\langle Z_L\rangle.
\]

Thus every nonzero recurrent survivor must satisfy

\[
\boxed{
\langle\mathcal R_{B,L}\rangle
\ge
\left(\frac14-\frac{K_I}{2}\right)
\langle Z_L\rangle
+\nu\langle Q_L\rangle.
}
\]

This formula is meaningful even when the first coefficient is negative, because the viscous term remains positive.

If `K_I<1/2`, then already

\[
\boxed{
\langle\mathcal R_{B,L}\rangle
\ge
\frac{1-2K_I}{4}
\langle Z_L\rangle
+\nu\langle Q_L\rangle>0
}
\]

for every nonzero recurrent state.

Thus a recurrent state with `K_I<1/2` cannot be both nonzero and Betchov-residual-free.

---

## 5. Normalize by mean enstrophy

Because the invariant measure carries positive active-core mass,

\[
\langle Z_L\rangle>0.
\]

Define

\[
\bar\varepsilon_B
:=
\frac{\langle\mathcal R_{B,L}\rangle}
{\langle Z_L\rangle},
\qquad
\bar\lambda
:=
\frac{\langle Q_L\rangle}
{\langle Z_L\rangle}.
\]

Then nonzero recurrence requires

\[
\boxed{
\bar\varepsilon_B
\ge
\frac14-\frac{K_I}{2}
+\nu\bar\lambda.
}
\]

This is the invariant-measure counterpart of the pointwise production-efficiency split.

The recurrent active-window calculation supplies a positive lower bound

\[
\bar\lambda\ge c_{\log}>0
\]

on the pure active branch. Therefore

\[
\boxed{
\bar\varepsilon_B
\ge
\frac14-\frac{K_I}{2}
+\nu c_{\log}.
}
\]

So if the right side is positive, a fixed positive normalized Betchov residual is not optional: it is forced by the existence of the recurrent survivor.

---

## 6. Connection to the tail-independent rigidity certificate

Suppose instead the averaged residual is known to satisfy

\[
\langle\mathcal R_{B,L}\rangle
\le
\varepsilon_*\langle M_LZ_L\rangle
\le
\varepsilon_*K_I\langle Z_L\rangle.
\]

Then

\[
\frac14+\nu\bar\lambda
\le
\left(\frac12+\varepsilon_*\right)K_I.
\]

Thus the invariant-measure closure condition is

\[
\boxed{
\left(\frac12+\varepsilon_*\right)K_I
<
\frac14+\nu c_{\log}.
}
\]

Multiplying by two gives exactly the physical backward-Gronwall certificate

\[
\boxed{
(1+2\varepsilon_*)K_I
<
\frac12+2\nu c_{\log}.
}
\]

Hence the two formulations are the same theorem in different clocks.

---

## 7. Why averaging is a real improvement

The previous pointwise formulation asked for an eventual upper bound on `epsilon_B(t)`. That is stronger than necessary and could fail because the recurrent orbit may alternate between

- nearly pure positive-middle production; and
- brief negative-middle Betchov-mismatch bursts.

The invariant-measure identity shows that only their long-time Leray average matters for the enstrophy exponent.

Therefore the next localization theorem should target

\[
\boxed{
\langle\mathcal R_{B,L}\rangle
}
\]

rather than a pointwise supremum of the residual fraction.

---

## 8. Residual localization frontier

The repository local Betchov-buffer theorem says a coherent positive mismatch on a fixed ball forces

\[
\text{buffer strain reservoir}
\lor
\text{buffer derivative concentration}.
\]

The current invariant-measure calculation says a nonzero recurrent survivor may be forced to carry a positive **mean total mismatch**.

The precise remaining bridge is therefore:

\[
\boxed{
\text{positive invariant-average }\mathcal R_{B,L}
\Longrightarrow
\text{positive-density fixed-cell mismatch}
\lor
\text{remote/diffuse residual tail}.
}
\]

On the vorticity-tight recurrent lane, the first alternative is expected to be accessible by finite covering of the fixed active Leray core. The second must be kept as an explicit escape until its tail contribution is quantitatively controlled.

Status: **A NONZERO RECURRENT LERAY SURVIVOR MUST SATISFY AN EXACT AVERAGE BETCHOV-RESIDUAL LOWER BOUND. POINTWISE RESIDUAL SMALLNESS IS NOT NEEDED; THE NATURAL OBJECT IS THE INVARIANT-MEASURE AVERAGE. THE NEXT GAP IS LOCALIZING THAT AVERAGE INTO A FIXED ACTIVE CORE OR IDENTIFYING A GENUINE REMOTE/DIFFUSE RESIDUAL TAIL. GLOBAL REGULARITY REMAINS UNPROVED.**