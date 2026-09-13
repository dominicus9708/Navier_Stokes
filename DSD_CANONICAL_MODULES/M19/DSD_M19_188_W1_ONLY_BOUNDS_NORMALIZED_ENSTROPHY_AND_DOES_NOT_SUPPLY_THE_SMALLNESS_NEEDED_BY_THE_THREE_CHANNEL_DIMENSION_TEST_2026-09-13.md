# M19-188 — W1 only bounds normalized enstrophy and does not supply the smallness needed by the three-channel dimension test

**Date:** 2026-09-13  
**Status:** ACTIVE CALCULATION / UPSTREAM HYPOTHESIS AUDIT / GENUINE FRONTIER CERTIFICATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Question

M19-187 obtained the sufficient condition

\[
\boxed{
K_*\frac{Z_+^2}{\nu^3}<\frac14
\Longrightarrow
N\le1.
}
\]

Does the retained W1 / first-hitting corridor already force this smallness?

## 2. Authoritative M18-042 ledger

M18-042 defines the bounded-normalized-enstrophy condition as

\[
\boxed{
Z_D(t)=\int|\Omega_D|^2\,dY\le Z_+.
}
\]

Its classification is explicitly

\[
\boxed{
H_Z:\ \text{CASE-SURVIVOR CONDITION; GLOBAL COMPLEMENT NOT CERTIFIED HERE}.
}
\]

Moreover M18-042 states that finite physical kinetic energy does not itself imply a uniform bound on this dynamically normalized enstrophy.

Thus W1 uses `Z_+<infinity` as a retained corridor quantity. It does not provide a universal numerical smallness theorem for `Z_+`.

## 3. Boundedness is not the M19-187 threshold

The M19-187 condition is not merely

\[
Z_+<\infty.
\]

It requires the dimensionless quantitative inequality

\[
\boxed{
\frac{Z_+^2}{\nu^3}<\frac1{4K_*}.
}
\]

No retained W1 theorem in the M18-042 hypothesis ledger supplies this inequality.

Hence

\[
\boxed{
H_Z\not\Rightarrow \mathcal T_{dim1}.
}
\]

## 4. Why first-hitting amplitude normalization does not by itself fix enstrophy

First-hitting normalization fixes an amplitude/scale representative. Even if one normalizes a pointwise vorticity amplitude at a selected generation, enstrophy is a spatially integrated quantity:

\[
Z=\int|\Omega|^2dy.
\]

A pointwise amplitude normalization does not determine the effective support volume or the amount of moderate-amplitude vorticity spread through the similarity domain.

Therefore

\[
\boxed{
\text{first-hitting amplitude normalization}
\neq
\text{small normalized enstrophy}.
}
\]

This is the same magnitude-versus-distribution firewall that appears elsewhere in the repository.

## 5. Exact branch consequence

The recurrent hard lane now has the quantitative split

\[
\boxed{
\mathcal R_{hard}^{rec}
\Longrightarrow
\begin{cases}
K_*Z_+^2/\nu^3<1/4:
&N\le1\Rightarrow\text{relative-periodic after finite quotient return},\\
K_*Z_+^2/\nu^3\ge1/4:
&\mathcal R_{large-Z}^{hard}.
\end{cases}
}
\]

The second branch is a genuine current frontier, not a bookkeeping artifact.

## 6. Relationship to the old Z-escalation root

This branch must not be confused with the upstream complement

\[
Z_D\to\infty.
\]

from M18-042.

The new M19 branch can have a **finite** enstrophy ceiling while still lying above the dimension-one threshold:

\[
\boxed{
\frac1{2\sqrt{K_*}}\nu^{3/2}
\lesssim Z_+<\infty.
}
\]

Therefore

\[
\boxed{
\text{large-but-finite recurrent enstrophy}
\neq
\text{Z-escalation/decompactification}.
}
\]

This is a new quantitative subdivision inside the bounded-Z corridor.

## 7. What could close it

The branch can be closed only by additional information such as:

1. a sharper recurrent identity that forces a universal upper bound below the threshold;
2. a sign/alignment restriction reducing the compensation constants `K_*`;
3. an additional exact neutral/symmetry channel increasing the minimum paying dimension beyond three;
4. a new structural theorem routing large-but-finite `Z_+` to an already typed remote/critical/derivative exit.

None is currently certified universally.

## 8. Audit verdict

### Certified

\[
\boxed{
\text{W1 bounded normalized enstrophy does not close M19-187.}
}
\]

### Still open

\[
\boxed{
\mathcal R_{large-Z}^{hard}:
K_*Z_+^2/\nu^3\ge1/4,
\quad Z_+<\infty.
}
\]

---

\[
\boxed{\text{M19-188: LARGE-BUT-FINITE RECURRENT ENSTROPHY IS A GENUINE QUANTITATIVE HARD BRANCH.}}
\]
