# H1 Threshold Curvature Bootstrap — 2026-08-20

Overall status: **NEW BOOTSTRAP FROM DANGEROUS P_V PRODUCTION TO H2 CONTROL — LOCALIZATION STILL REQUIRED FOR THE CORE-TAIL SETTING; GLOBAL REGULARITY NOT PROVED.**

This note combines the sharp trace-free H1 production bound with a scale-critical Sobolev interpolation. The key result is that a profile capable of reaching the viscous H1 threshold cannot have arbitrarily large curvature relative to palinstrophy. With an enstrophy bound, this yields quantitative `H1` and `H2` bounds and therefore provides a route to precompactness rather than assuming it a priori.

---

## 1. Notation

Let

\[
E=\|S\|_2^2,
\qquad
P=\|\nabla S\|_2^2,
\qquad
H=\|\Delta S\|_2^2,
\]

and define

\[
N=\int_{\mathbb R^3}|S||\nabla S|^2dx.
\]

The sharp P_V production result gives

\[
\boxed{
-\langle\mathcal R_{VI},-\Delta S\rangle
\le\frac4{\sqrt6}N.
}
\]

---

## 2. Scale-critical interpolation for N

Hölder with exponents `6, 12/5, 12/5` gives

\[
N
\le
\|S\|_6\|\nabla S\|_{12/5}^2.
\]

Sobolev gives

\[
\|S\|_6\lesssim\|\nabla S\|_2=P^{1/2}.
\]

Interpolate

\[
\frac{5}{12}
=
\frac34\frac12+rac14\frac16,
\]

so

\[
\|\nabla S\|_{12/5}
\le
\|\nabla S\|_2^{3/4}
\|\nabla S\|_6^{1/4}
\lesssim
P^{3/8}H^{1/8}.
\]

Therefore

\[
\boxed{
N\lesssim P^{5/4}H^{1/4}.
}
\]

Both sides scale like `lambda^5` under Navier--Stokes strain scaling.

---

## 3. A scale-invariant curvature ratio

Define

\[
\boxed{
\mathfrak K
=
\frac{H^{1/2}}{P^{5/6}}.
}
\]

This is invariant under

\[
S^\lambda(x)=\lambda^2S(\lambda x).
\]

The interpolation estimate becomes

\[
\boxed{
\frac{N}{H}
\lesssim
\mathfrak K^{-3/2}.
}
\]

Thus the exact H1 production-to-hyperdissipation ratio satisfies

\[
\boxed{
\eta_{VI}
:=
\frac{-\langle\mathcal R_{VI},-\Delta S\rangle}{H}
\lesssim
\frac4{\sqrt6}\mathfrak K^{-3/2}.
}
\]

---

## 4. Dangerous H1 production forces an upper curvature bound

Finite-time blowup requires a sequence with

\[
\eta_{VI}\ge\nu-o(1).
\]

Consequently, on every sufficiently dangerous profile in that sequence,

\[
\boxed{
\mathfrak K
\le K_\nu<\infty,
}
\]

where `K_nu` depends only on viscosity and the universal Sobolev constants.

Equivalently,

\[
\boxed{
H\le K_\nu^2P^{5/3}.
}
\]

Thus the dangerous `P_V` branch cannot escape by making hyperdissipation arbitrarily large relative to palinstrophy. Very high curvature is automatically regularizing in the exact H1 ledger.

---

## 5. Interpolation converts the curvature cap into H1/H2 bounds

Integration by parts gives

\[
P
=\langle S,-\Delta S\rangle
\le E^{1/2}H^{1/2}.
\]

Hence

\[
P^2\le EH.
\]

In terms of `Kfrak`,

\[
\mathfrak K
=
\frac{H^{1/2}}{P^{5/6}}
\ge
\frac{P^{1/6}}{E^{1/2}}.
\]

Combining with `Kfrak <= K_nu`,

\[
\boxed{
P\le K_\nu^6E^3.
}
\]

Then

\[
H^{1/2}\le K_\nu P^{5/6}
\]

gives

\[
\boxed{
H\le K_\nu^{12}E^5.
}
\]

Therefore a dangerous threshold-crossing sequence with uniformly bounded enstrophy automatically has uniformly bounded palinstrophy and hyperdissipation.

This is the main bootstrap.

---

## 6. Why this matters for the compact-class efficiency gap

Previously the strict efficiency-gap argument assumed a precompact non-H/T `H2` profile class. The present bootstrap shows a possible way to generate the required `H2` bound from the **dangerous threshold condition itself**:

\[
\boxed{
\text{H1 threshold}
+
E\text{ bounded}
\Longrightarrow
P,H\text{ bounded}.
}
\]

If spatial tightness and center fixing are also available, Rellich compactness can then produce the precompact class on which exact saturation nonattainment yields a uniform efficiency gap.

Thus the logical circle

`need H2 compactness -> get efficiency gap -> control H1 production`

can potentially be replaced by

`dangerous H1 production -> curvature cap -> H2 bound -> compactness -> strict efficiency gap`.

---

## 7. Global-tail caveat

The whole-space normalized ancient survivor necessarily carries a global critical velocity tail, and its global strain enstrophy need not be uniformly bounded. Therefore the previous bootstrap cannot simply be applied to the **entire ancient field** without additional information.

The intended use is a localized tight active core. Let `chi_R` be a cutoff around the tracked core and apply the interpolation to

\[
F=\chi_RS.
\]

For compactly supported `F`, the same estimates hold:

\[
\int|F||\nabla F|^2
\lesssim
\|\nabla F\|_2^{5/2}
\|\Delta F\|_2^{1/2}.
\]

The difference between the exact global H1 ledger and the localized core ledger generates shell/cutoff terms. The non-T program must show that these shell terms are either uniformly negligible at a sufficiently large fixed normalized parent radius or constitute a genuine influx/turnover event `T`.

Thus the remaining localization lemma is now concrete rather than qualitative.

---

## 8. Refined local endgame

On the non-H/T branch, a threshold-crossing local core should satisfy the following chain:

\[
\boxed{
\eta_{VI}\gtrsim\nu
\Longrightarrow
\mathfrak K\le K_\nu
\Longrightarrow
P_{core}+H_{core}\le C(E_{core},\nu)
\Longrightarrow
\text{precompact core class}
}
\]

provided local enstrophy, tightness, and shell errors are controlled.

Once precompactness is obtained, the full-saturation rigidity theorem yields a strict class-dependent H1 efficiency gap. The remaining question is then whether the resulting attained variational threshold `Lambda_K` is strictly below viscosity.

---

## 9. Next exact lemma

The next useful theorem target is the localized version:

\[
\boxed{
\begin{gathered}
\text{non-T shell control}
+
\text{local H1 threshold crossing}\\
\Longrightarrow
\text{uniform }H^2\text{ bound and tightness for }\chi_RS.
\end{gathered}
}
\]

If proved, the precompact `P_V` core class ceases to be an assumption and becomes a consequence of the blowup scenario itself.

Status: **DANGEROUS P_V H1 PRODUCTION FORCES A SCALE-INVARIANT CURVATURE CAP. WITH ENSTROPHY CONTROL THIS BOOTSTRAPS TO UNIFORM PALINSTROPHY AND HYPERDISSIPATION BOUNDS. THE REMAINING ISSUE IS LOCALIZATION IN THE PRESENCE OF THE NECESSARY GLOBAL PASSIVE TAIL. GLOBAL REGULARITY REMAINS UNPROVED.**