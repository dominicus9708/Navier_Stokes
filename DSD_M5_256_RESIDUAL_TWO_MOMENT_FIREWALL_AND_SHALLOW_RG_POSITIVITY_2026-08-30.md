# DSD M5-256 — Residual Two-Moment Firewall and Shallow-RG Positivity

Date: 2026-08-30

Parent: `DSD_M5_255_RELATIVE_H1_PRODUCTION_CEILING_AND_QUOTIENT_FREQUENCY_WINDOW_2026-08-30.md`

Status: **RESIDUAL-WORK STRUCTURE AUDIT / VELOCITY-LEVEL AND RELATIVE-VORTICITY-LEVEL RESIDUAL WORKS ARE TWO DIFFERENT SPECTRAL MOMENTS OF THE SAME RESIDUAL--QUOTIENT CORRELATION AND HAVE NO UNIVERSAL SIGN RELATION / HOWEVER THE EXACT RG RECONSTRUCTION `R_rho(T)=T-rho F_T+o(rho)` FORCES BOTH MOMENTS TO BE POSITIVE AT SUFFICIENTLY SMALL FIXED RG DEPTH WHEN THE CORRESPONDING RESIDUAL NORM IS NONZERO / THIS PROVIDES A SIGNED FINITE-DEPTH RESIDUAL CERTIFICATE BUT NOT YET A GLOBAL ENERGY CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Two signed residual works

At velocity level M5-250 uses

\[
\boxed{
\mathcal W_0
:=-\langle R_B,Q\rangle.
}
\]

At relative-vorticity level M5-254 uses

\[
\boxed{
\mathcal W_1
:=-\langle\nabla\times R_B,\eta\rangle,
\qquad
\eta=\nabla\times Q.
}
\]

Assume `R_B` is divergence free after Leray projection.

---

## 2. Exact spectral-moment relation

In Fourier variables,

\[
\widehat\eta=i\xi\times\widehat Q,
\qquad
\widehat{\nabla\times R_B}=i\xi\times\widehat R_B.
\]

Because both `Q` and `R_B` are divergence free,

\[
(i\xi\times\widehat R_B)
\cdot
\overline{(i\xi\times\widehat Q)}
=
|\xi|^2
\widehat R_B\cdot\overline{\widehat Q}.
\]

Hence

\[
\boxed{
\mathcal W_1
=
-\langle R_B,-\Delta Q\rangle.
}
\]

Thus `W0` and `W1` are the zeroth and second spectral moments of the same signed correlation density.

---

## 3. No universal sign relation

There is no general implication

\[
\mathcal W_0>0
\Longrightarrow
\mathcal W_1>0
\]

or conversely.

A correlation density in Fourier space may be positive at low frequencies and negative at high frequencies, or vice versa. Multiplication by `|xi|^2` changes the balance.

Therefore the following shortcut is RED:

\[
\boxed{
\text{positive velocity residual work}
\Rightarrow
\text{positive curl-residual work}.
}
\]

The two recurrent production coefficients in M5-250 and M5-255 must remain separate unless extra spectral alignment is proved.

---

## 4. Exact shallow RG expansion

Use the canonical RG reconstruction from M5-237/240 on a fixed punctured cell, or globally after a compatible smooth extension where the stated norms are finite:

\[
\partial_\rho\mathscr R_\rho(T)
=-\mathcal F(\mathscr R_\rho(T)),
\qquad
\mathscr R_0(T)=T.
\]

Write

\[
F_T:=\mathcal F(T).
\]

Then continuity of the vector field gives

\[
\boxed{
\mathscr R_\rho(T)-T
=-\rho F_T+o_X(\rho)
}
\]

in every audited fixed-cell norm `X` in which the RG vector field is continuous.

Define the shallow relative field

\[
Q_\rho:=\mathscr R_\rho(T)-T.
\]

---

## 5. Velocity-level work positivity

If `F_T` belongs to `L2` on the selected cell and

\[
\|F_T\|_2>0,
\]

then

\[
\begin{aligned}
-\langle F_T,Q_\rho\rangle
&=
-\left\langle
F_T,-\rho F_T+o_{L2}(\rho)
\right\rangle\\
&=
\boxed{
\rho\|F_T\|_2^2+o(\rho).
}
\end{aligned}
\]

Therefore there exists

\[
\rho_0(T)>0
\]

such that

\[
\boxed{
-\langle F_T,Q_\rho\rangle>0
\qquad(0<\rho<\rho_0(T)).
}
\]

On a compact residual-gap tail hull with uniform continuity and a uniform residual norm floor, one may choose a common sufficiently small `rho_*` on the selected finite cover of cells.

---

## 6. Vorticity-level work positivity

If additionally

\[
\nabla\times F_T\in L^2
\]

and is nonzero, then

\[
\eta_\rho
:=\nabla\times Q_\rho
=-\rho\nabla\times F_T+o_{L2}(\rho).
\]

Hence

\[
\boxed{
-\langle\nabla\times F_T,\eta_\rho\rangle
=
\rho\|\nabla\times F_T\|_2^2+o(\rho)>0
}
\]

for sufficiently small positive `rho`.

Thus the two spectral moments, though unrelated in sign for a general finite-depth quotient, are **simultaneously positive at shallow RG depth** when their corresponding residual components are nonzero.

---

## 7. Quantitative version on a compact residual-gap class

Suppose on a compact tail subset

\[
\|F_T\|_2\ge f_0>0
\]

and the RG remainder satisfies uniformly

\[
\|Q_\rho+\rho F_T\|_2
\le
\epsilon(\rho)\rho,
\qquad
\epsilon(\rho)\to0.
\]

Choose `rho_*` so that

\[
\epsilon(\rho_*)
\le\frac{f_0}{2}.
\]

Then

\[
\boxed{
-\langle F_T,Q_{\rho_*}\rangle
\ge
\frac12\rho_*f_0^2.
}
\]

The same argument gives

\[
\boxed{
-\langle\nabla\times F_T,\eta_{\rho_*}\rangle
\ge
\frac12\rho_*g_0^2
}
\]

when

\[
\|\nabla\times F_T\|_2\ge g_0>0
\]

uniformly.

---

## 8. Relation to M5-248 finite-depth inheritance

The shallow depth `rho_*` is one fixed positive number.

Therefore M5-248's fixed-depth reconstruction principle applies: a robust signed work certificate at `rho_*` can be transferred to

1. a fixed finite normalized W1 annulus;
2. then, by local compactness, to sufficiently deep finite first-hitting stages.

No expanding-window convergence is needed for this transfer.

---

## 9. Why this is not yet an energy contradiction

On a physical radius-`R` cell,

\[
F_T\sim R^{-3},
\]

and the first RG correction has an additional `R^{-2}` factor relative to the leading `1/R` tail. The corresponding unweighted physical work decays by a positive power of `R` and is geometrically summable across generations.

Thus

\[
\boxed{
\text{positive shallow RG work on every critical cell}
\not\Rightarrow
\text{divergent physical energy cost}.
}
\]

The certificate is scale-critical/renormalized, not a direct finite-energy contradiction.

---

## 10. DSD verdict

### PROVED

- `W0` and `W1` are distinct spectral moments;
- no universal sign relation exists at arbitrary finite depth;
- exact RG reconstruction makes both signed works positive to first order in `rho` when the corresponding residual norms are nonzero;
- compact residual-gap classes yield one uniform shallow depth with a quantitative positive work floor.

### FIREWALL

Positive work at one derivative level is not silently copied to another derivative level at finite depth.

### NEXT TARGET

Use the shallow positive-work expansion to define a **renormalized residual-work density per log scale**. Then test whether its invariant average can be balanced by the M5-250 anti-damping and M5-254 H1 taxes while all amplitude/derivative coefficients remain below their pure-corridor ceilings.

This is more promising than summing unweighted physical work across shrinking generations.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
