# DSD M17-253 — H2 compactness defect is a vanishing-L2 high-frequency microcarrier and returns to the subscale or nodal channel

Date: 2026-09-06  
Canonical ID: **M17-253**

Status: **DERIVATIVE-DEFECT CLASSIFICATION / AFTER M17-251, A SCALE-COMPARABLE PACKET CAN GIVE `V_j -> V` STRONGLY IN LOCAL `L2` WITH A UNIFORM `H2` CEILING. A POSITIVE PRELIMIT `H2` CHARGE NEED NOT SURVIVE WEAK `H2` CONVERGENCE. HOWEVER ANY SUCH DEFECT IS FORCED TO HIGH FREQUENCY: ON EVERY FIXED FOURIER BALL, STRONG `L2` CONVERGENCE CONTROLS THE `H2` DIFFERENCE BY `N^4 ||V_j-V||_2^2`. THUS A NONZERO `H2` DEFECT LIVES AT FREQUENCIES `|xi|->infinity`. THE ASSOCIATED HIGH-FREQUENCY PART HAS `L2` MASS AT MOST `N^-4` TIMES THE UNIFORM `H2` BUDGET, SO IT IS A VANISHING-MASS HIGH-DERIVATIVE MICROCARRIER. THE RAW-LAPLACIAN RE-EXTRACTION OF M17-232/250 CONVERTS THIS FREQUENCY DEFECT BACK INTO A STRICTLY SMALLER PHYSICAL PACKET OR NODAL CONCENTRATION. THEREFORE DERIVATIVE-CHARGE LOSS IS NOT A NEW TERMINAL BRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Compactness input

Let `Omega` be one fixed bounded rescaled domain on the retained-mass branch of M17-251.

Assume

\[
\boxed{
V_j\to V
\quad\text{strongly in }L^2(\Omega),
}
\]

and

\[
\boxed{
\sup_j\|V_j\|_{H^2(\Omega)}\le C_*.
}
\]

After a fixed smooth interior cutoff `eta` supported in `Omega`, set

\[
F_j:=\eta V_j,
\qquad
F:=\eta V.
\]

Then

\[
F_j\to F
\quad\text{strongly in }L^2(\mathbb R^3),
\]

and

\[
\sup_j\|F_j\|_{H^2(\mathbb R^3)}\le C_\eta.
\]

The cutoff is used only to formulate the Fourier compactness audit.

---

## 2. Low frequencies cannot carry an H2 defect

Let `P_{<=N}` denote the Fourier projection to

\[
|\xi|\le N.
\]

Then

\[
\begin{aligned}
\|\Delta P_{<=N}(F_j-F)\|_2^2
&=
\int_{|\xi|\le N}|\xi|^4|\widehat{F_j-F}|^2d\xi\\
&\le
N^4\|F_j-F\|_2^2.
\end{aligned}
\]

For every fixed `N`, strong `L2` convergence gives

\[
\boxed{
\Delta P_{<=N}F_j
\to
\Delta P_{<=N}F
\quad\text{strongly in }L^2.
}
\]

Therefore a positive defect in the second-derivative norm cannot remain at any fixed frequency scale.

---

## 3. Any derivative defect escapes to high frequency

Suppose there is a defect

\[
\boxed{
\limsup_{j\to\infty}\|\Delta F_j\|_2^2
>\|\Delta F\|_2^2+d_*
}
\]

for some `d_*>0`.

By Section 2, for every sufficiently large fixed `N`, after passing to a subsequence the excess must satisfy

\[
\boxed{
\limsup_j
\|\Delta P_{>N}F_j\|_2^2
\ge c d_*>0.
}
\]

Thus the defect is a genuine high-frequency tail.

---

## 4. The high-frequency defect has vanishing L2 mass

The uniform `H2` ceiling gives

\[
\begin{aligned}
\|P_{>N}F_j\|_2^2
&=
\int_{|\xi|>N}|\widehat F_j|^2d\xi\\
&\le
N^{-4}
\int_{|\xi|>N}|\xi|^4|\widehat F_j|^2d\xi\\
&\le
C_\eta N^{-4}.
\end{aligned}
\]

Hence

\[
\boxed{
\sup_j\|P_{>N}F_j\|_2^2
\le C_\eta N^{-4}
\to0
\qquad(N\to\infty).
}
\]

So the same component that carries a fixed second-derivative defect can have arbitrarily small `L2` mass.

This is exactly a **vanishing-mass high-frequency microcarrier**.

---

## 5. This is the same concentration mechanism isolated in M17-228/232

M17-228 identified the physical-space alternative

\[
\text{fixed-fraction fluctuation}
\lor
\text{vanishing-mass spectral microcarrier}.
\]

M17-232 then showed that a vanishing-mass derivative carrier can be re-extracted into an actual smaller physical buffer while preserving raw `|Delta W|^2` charge.

The Fourier defect found above is the same concentration-compactness mechanism in frequency language.

Therefore

\[
\boxed{
G_{H2\ compactness\ defect}
\Longrightarrow
G_{strict\ physical\ subscale}
\lor
G_{nodal\ concentration}.
}
\]

If the smaller packet remains mean-dominated on the original CE-H field, M17-233 may further return it to the critical `kappa` coefficient channel.

---

## 6. No-defect branch

On the complementary branch where no high-frequency microcarrier survives, the second-derivative norm is tight.

After subsequence,

\[
\boxed{
\Delta F_j\to\Delta F
\quad\text{strongly in }L^2.
}
\]

Thus any fixed raw derivative charge retained by the chosen interior cutoff survives the tangent limit.

In particular, if the packet selection provides a positive localized normalized raw-Laplacian floor

\[
\|\Delta F_j\|_2^2\ge h_*>0,
\]

then

\[
\boxed{
\|\Delta F\|_2^2\ge h_*>0.
}
\]

So the no-defect tangent cannot become locally constant.

---

## 7. Corrected tangent frontier

The derivative-retention problem is therefore reduced to

\[
\boxed{
H_{nonzero\ time\text{-}zero\ H2\ tangent}
\Longrightarrow
H_{nonzero\ derivative\text{-}retaining\ tangent}
\lor
G_{strict\ subscale}
\lor
G_{nodal\ concentration}.
}
\]

The subscale branch is already part of the M17-232/250 coefficient/nodal ledger.

Hence `H2 compactness defect` is removed as an independent frontier label.

---

## 8. DSD audit

- Strong `L2` convergence is used only to kill fixed low-frequency derivative defects.
- Weak `H2` convergence is not assumed to preserve norm lower bounds.
- The defect is explicitly identified as high-frequency before being called a microcarrier.
- High-frequency `L2` smallness follows quantitatively from the uniform `H2` ceiling.
- Fourier projection is an audit device; CE-H is not assigned to the projected field.
- Physical re-extraction is delegated to the already proved raw-Laplacian M17-232/250 machinery on the original field.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
