# DSD vorticity non-tightness -> frequency H or Campanato turnover

Date: 2026-08-25

Status: **DYADIC NON-TIGHTNESS ROUTING PROVED / INTERMEDIATE V_REMOTE REMOVED AS AN INDEPENDENT PURE-CORRIDOR BRANCH / GLOBAL REGULARITY UNPROVED.**

## 1. Setup

Let `U` be a first-hitting normalized velocity, `Omega=curl U`, and fix a large radius `R0`.
Assume that a fixed amount of normalized enstrophy remains outside that radius,

\[
\int_{|y|>R_0}|\Omega|^2\,dy\ge \varepsilon_0>0.
\]

Use dyadic annuli

\[
A_k=\{R_k<|y|<2R_k\},\qquad R_k=2^kR_0,
\]

and define

\[
m_k:=\int_{A_k}|\Omega|^2\,dy.
\]

Then

\[
\sum_{k\ge0}m_k\ge\varepsilon_0.
\]

## 2. A shell with large radius-weighted enstrophy

Put

\[
M:=\sup_{k\ge0}R_km_k.
\]

Since `m_k<=M/R_k`,

\[
\varepsilon_0
\le\sum_{k\ge0}m_k
\le M\sum_{k\ge0}R_k^{-1}
=\frac{2M}{R_0}.
\]

Therefore some shell satisfies

\[
\boxed{R_km_k\ge \frac{\varepsilon_0R_0}{2}.}
\]

This uses only the geometric dyadic spacing and is independent of any fixed shell occupancy hypothesis.

## 3. Localized solenoidal packet

Let `f_k` be the standard Bogovskii-corrected shell localization used elsewhere in the repository, with `f_k=U` on `A_k`.
Then

\[
\|\nabla f_k\|_2^2\ge\int_{A_k}|\nabla U|^2dy\ge\frac12m_k.
\]

Define the shell derivative ratio

\[
\Gamma_k:=\frac{R_k\|\nabla f_k\|_2}{\|f_k\|_2}.
\]

Fix a finite non-H threshold `Gamma_*`.

If

\[
\Gamma_k>\Gamma_*,
\]

the selected shell is already in the existing remote derivative-frequency channel `H_freq`.

Assume instead

\[
\Gamma_k\le\Gamma_*.
\]

Then

\[
\|f_k\|_2^2
\ge\frac{R_k^2}{\Gamma_*^2}\|\nabla f_k\|_2^2
\ge\frac{R_k^2m_k}{2\Gamma_*^2}.
\]

Define the localized shell Campanato/relative-variance quantity

\[
\mathfrak C_k:=R_k^{-1}\|f_k\|_2^2.
\]

Hence

\[
\mathfrak C_k
\ge\frac{R_km_k}{2\Gamma_*^2}
\ge\boxed{\frac{\varepsilon_0R_0}{4\Gamma_*^2}}.
\]

Therefore, as the non-tightness radius `R0` tends to infinity, every non-H realization forces unbounded shell relative variance.

## 4. Pure-corridor consequence

The moving relative-variance ledger identifies unbounded normalized relative variance as a turnover/Campanato channel: a reservoir of this size cannot be created, relabeled, contracted, or removed while all material/radial/viscous/pressure boundary actions remain uniformly quiet.

Thus the rigorous routing is

\[
\boxed{
V_{remote}
\Longrightarrow
H_{freq}\ \lor\ T_{Campanato}.
}
\]

More quantitatively, if the non-turnover corridor supplies a uniform shell Campanato ceiling

\[
\mathfrak C_k\le C_T,
\]

then vorticity non-tightness beyond `R0` is impossible whenever

\[
\boxed{R_0>\frac{4\Gamma_*^2C_T}{\varepsilon_0}.}
\]

Hence `V_remote` need not remain an independent intermediate branch inside the pure non-H/non-T corridor.

## 5. Relation to active remote H

The existing direct Biot-Savart gate gives

\[
H_{remote}^{active}\text{ at }R\to\infty
\Longrightarrow V_{remote}
\]

when vorticity tightness fails, whereas passive exterior derivative mass is not a naked core obstruction.
Combining with the present lemma,

\[
\boxed{
H_{remote}^{active}
\Longrightarrow
H_{freq}\ \lor\ T_{Campanato}
}
\]

at genuinely escaping radii, modulo the already separated passive/neutralized sector.

## 6. Audit limitation

This note does **not** prove that every `H_freq` event is impossible.
It proves that loss of vorticity tightness cannot be used as a third independent escape mechanism between remote-H and turnover.
The high-frequency remote sector must still be treated by the existing derivative/palinstrophy/historical genealogy ledgers or shown dynamically passive.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
