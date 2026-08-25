# DSD Weak-L3 Escalation -> Direct Derivative-Frequency Routing

Date: 2026-08-25

Status: **W2 RESIDUAL PRUNED AS AN INDEPENDENT FRONTIER / BOUNDED-CAMPANATO WEAK-L3 ESCALATION ROUTES DIRECTLY TO THE EXISTING DERIVATIVE-FREQUENCY H BRANCH / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The previous audit isolated a residual branch

\[
W_2:\quad \|U\|_{L^{3,\infty}}\to\infty
\]

and then reduced it to critical annular H1 escalation plus, through interpolation, a remote H2/subscale branch.

That reduction was correct but unnecessarily indirect. The repository already contains the shell derivative-frequency descriptor used in

`AMPLITUDE_SENSITIVE_HISTORICAL_GENEALOGY_GATE_2026-08-24.md`:

\[
\Gamma_R:=\frac{R\|\nabla f_R\|_2}{\|f_R\|_2},
\]

where `f_R` is the divergence-free localized shell packet after cutoff/Bogovskii correction.

The present note shows that once relative Campanato is bounded, unbounded critical shell H1 energy forces \(\Gamma_R\to\infty\) directly. Hence the supposed diffuse-multiplicity survivor is already the typed derivative-frequency branch `H`.

---

## 2. Annular quantities

On a fixed-shape shell `A_R` define

\[
E_1(R):=R\int_{A_R^*}|\nabla U|^2,
\]

and the relative Campanato quantity

\[
\mathfrak C_A(R)
:=R^{-1}\int_{A_R^*}|U-(U)_{A_R^*}|^2.
\]

Let `f_R` denote the localized mean-free divergence-free packet. Standard cutoff/Bogovskii estimates on a fixed enlargement give

\[
\|f_R\|_2^2\lesssim R\,\mathfrak C_A(R)
\]

up to the already controlled dyadic-mean contribution, and

\[
\|\nabla f_R\|_2^2
\gtrsim
\int_{A_R}|\nabla U|^2
-CR^{-2}\|U-(U)_{A_R^*}\|_2^2.
\]

Therefore, whenever `E_1(R)` is above a fixed multiple of the Campanato error,

\[
R\|\nabla f_R\|_2^2\gtrsim E_1(R).
\]

---

## 3. Exact scale relation

By definition,

\[
\Gamma_R^2
=
\frac{R^2\|\nabla f_R\|_2^2}{\|f_R\|_2^2}.
\]

Using the preceding packet bounds,

\[
\boxed{
\Gamma_R^2
\gtrsim
\frac{E_1(R)}{\mathfrak C_A(R)}
}
\]

once `E_1` is in the genuinely escalating regime.

In the idealized no-cutoff-loss identity this is simply

\[
\Gamma_R^2
=
\frac{R\|\nabla f_R\|_2^2}{R^{-1}\|f_R\|_2^2}.
\]

Hence if

\[
\sup_R\mathfrak C_A(R)\le C_0<\infty
\]

but

\[
E_1(R_n)\to\infty,
\]

then

\[
\boxed{
\Gamma_{R_n}\to\infty.
}
\]

This is exactly the derivative-frequency failure criterion already typed as `H` in the amplitude-sensitive genealogy gate.

---

## 4. Combine with the weak-L3 annular gate

The annular weak-L3 calculation gives

\[
\sup_R E_1(R)<\infty,
\qquad
\sup_R\mathfrak C_A(R)<\infty
\quad\Longrightarrow\quad
U\in L^{3,\infty}.
\]

Therefore

\[
\|U\|_{L^{3,\infty}}\to\infty
\]

forces either

\[
\mathfrak C_A(R_n)\to\infty
\]

or

\[
E_1(R_n)\to\infty.
\]

The first branch was already reduced to the Type-I local-energy/Campanato turnover complement.

On the bounded-Campanato branch, the second implies

\[
\Gamma_{R_n}\to\infty,
\]

hence `H`.

Thus

\[
\boxed{
W_2
\Longrightarrow
T_{Campanato}
\lor
H_{freq}.
}
\]

Inside the bounded-Z Type-I corridor where Campanato escalation is excluded/routed, this simplifies to

\[
\boxed{
W_2\Longrightarrow H_{freq}.
}
\]

---

## 5. Audit of the diffuse-multiplicity countermodel

The previous snapshot countermodel used

\[
N=A^4,
\qquad
\text{velocity amplitude}\sim \frac A R,
\qquad
\delta=\frac R{A^2}.
\]

It has

\[
\|U\|_2^2\asymp R,
\]

and

\[
\|\nabla U\|_2^2\asymp \frac{A^4}{R}.
\]

Therefore

\[
\boxed{
\Gamma_R
=
\frac{R\|\nabla U\|_2}{\|U\|_2}
\asymp A^2\to\infty.
}
\]

So the countermodel is useful as an anti-proof example showing that fixed-order pointwise analyticity bounds alone do not produce a single strong packet, but it is **not** a quiet non-H survivor under the repository's already-defined phase-space derivative-ratio gate.

This corrects the prior interpretation that `diffuse multiplicity` constituted a new final branch independent of `H`.

---

## 6. Updated endpoint frontier

The residual weak-L3 tree is now

\[
\boxed{
\begin{aligned}
\|U\|_{L^{3,\infty}}\uparrow
\Longrightarrow{}&
\text{relative-Campanato escalation}
\\
&\lor H_{freq}.
\end{aligned}
}
\]

After the existing bounded-Z Type-I Campanato reduction, no independent `W2` branch remains.

The genuine critical endpoint frontier is therefore again concentrated in the bounded derivative-ratio, uniformly weak-critical/persistent passive tail class, denoted `W1` in the running audit.

---

## 7. Status

### PROVED

- bounded Campanato plus unbounded critical shell H1 implies unbounded localized derivative ratio;
- the diffuse-multiplicity countermodel has \(\Gamma_R\asymp A^2\) and is therefore an `H` example, not a non-H endpoint survivor;
- `W2` is not an independent final DSD branch.

### STILL OPEN

- closure/rigidity of the bounded-derivative-ratio, uniformly weak-critical persistent passive tail (`W1`);
- completion of the existing H ledgers into the final master contradiction;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
