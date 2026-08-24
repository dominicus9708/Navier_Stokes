# DSD Direct Betchov High-Enstrophy Positive-Density Gate

Date: 2026-08-25

Status: **CUBIC-MOMENT RECURRENCE NECESSITY DERIVED / POSITIVE-DENSITY HIGH-ENSTROPHY WINDOWS DERIVED ON BOUNDED-Z BRANCH / POSITIVE-DENSITY REMOTE-MASS WITNESSES DERIVED / GLOBAL REGULARITY NOT PROVED.**

## 1. Scope

Work in standard backward-Leray variables on a nonzero recurrent state.

Let

\[
Z(s)=\|W(s)\|_2^2,
\qquad
Q(s)=\|\nabla W(s)\|_2^2,
\]

and

\[
\mathcal P(s)=\int W^T\Sigma W\,dy.
\]

The exact recurrent enstrophy balance is

\[
\boxed{
\frac14\overline Z
+\nu\overline Q
=\overline{\mathcal P}.
}
\]

Assume the recurrent active core is nonzero, so

\[
\overline Z>0.
\]

---

## 2. Direct Betchov production ceiling

The full Betchov identity and sharp determinant/Sobolev estimates give pointwise

\[
\boxed{
\mathcal P
\le
C_D Z^{3/4}Q^{3/4},
}
\]

where

\[
C_D=rac{2}{\pi3^{9/4}}.
\]

Therefore

\[
\mathcal P-\nu Q
\le
C_D Z^{3/4}Q^{3/4}-\nu Q.
\]

For fixed `Z`, optimize the right-hand side over `Q>=0`.

Set

\[
y=Q^{1/4}.
\]

Then

\[
C_D Z^{3/4}Q^{3/4}-\nu Q
=
C_DZ^{3/4}y^3-
u y^4.
\]

The positive maximizer is

\[
\boxed{
y_*=rac{3C_DZ^{3/4}}{4\nu}.}
\]

Substitution gives

\[
\boxed{
\mathcal P-\nu Q
\le
\frac{1}{11664\pi^4\nu^3}Z^3.
}
\]

This estimate contains no uniform `Z_+` assumption.

---

## 3. Recurrent cubic-moment necessity

Average the pointwise optimized inequality.

From the exact recurrent balance,

\[
\frac14\overline Z
=
\overline{\mathcal P-\nu Q}.
\]

Therefore

\[
\frac14\overline Z
\le
\frac1{11664\pi^4\nu^3}
\overline{Z^3}.
\]

Hence

\[
\boxed{
\overline{Z^3}
\ge
2916\pi^4\nu^3\,\overline Z.
}
\]

Define the direct-Betchov enstrophy scale

\[
\boxed{
Z_c:=54\pi^2\nu^{3/2}.
}
\]

Then

\[
Z_c^2=2916\pi^4\nu^3,
\]

so the recurrent necessity is simply

\[
\boxed{
\overline{Z^3}
\ge
Z_c^2\overline Z.
}
\]

This strengthens the earlier supremum consequence `Z_+>=Z_c`.

---

## 4. Z-weighted invariant measure

Define the `Z`-weighted probability measure on recurrent time by

\[
\boxed{
d\mu_Z
:=
\frac{Z(s)}{\overline Z}\,d\mu(s),
}
\]

where `mu` is the invariant/time-average probability measure selected along the recurrent orbit.

Then

\[
\int Z^2d\mu_Z
=
\frac{\overline{Z^3}}{\overline Z}.
\]

Thus

\[
\boxed{
\mathbb E_{\mu_Z}[Z^2]
\ge
Z_c^2.
}
\]

So the direct Betchov threshold is fundamentally a weighted second-moment statement, not merely a supremum statement.

---

## 5. Positive weighted density above any subcritical fraction

Now assume the bounded-enstrophy branch

\[
0\le Z(s)\le Z_+<\infty.
\]

Necessarily

\[
Z_+\ge Z_c.
\]

Fix

\[
0<\theta<1
\]

and define the high-enstrophy set

\[
\boxed{
A_\theta
:=
\{s:Z(s)\ge\theta Z_c\}.
}
\]

Let

\[
p_\theta:=\mu_Z(A_\theta).
\]

On the complement,

\[
Z^2<\theta^2Z_c^2,
\]

while globally

\[
Z^2\le Z_+^2.
\]

Therefore

\[
Z_c^2
\le
\mathbb E_{\mu_Z}[Z^2]
\le
\theta^2Z_c^2(1-p_\theta)
+Z_+^2p_\theta.
\]

Hence

\[
\boxed{
p_\theta
\ge
\frac{(1-\theta^2)Z_c^2}
{Z_+^2-\theta^2Z_c^2}.
}
\]

For every fixed `theta<1` this is strictly positive whenever `Z_+<infinity`.

Thus high-enstrophy states cannot occur only as a `Z`-weighted zero-density set.

---

## 6. Convert to ordinary recurrent time density

Because

\[
\mu_Z(A_\theta)
=
\frac{\int_{A_\theta}Z\,d\mu}{\overline Z}
\le
\frac{Z_+}{\overline Z}\mu(A_\theta),
\]

we have

\[
\boxed{
\mu(A_\theta)
\ge
\frac{\overline Z}{Z_+}
p_\theta.
}
\]

The recurrent active-core windows give a positive mean enstrophy floor. If their time density is at least `d_*` and their local enstrophy mass is at least `z_*`, then

\[
\boxed{
\overline Z\ge d_*z_*.
}
\]

Therefore

\[
\boxed{
\mu(A_\theta)
\ge
\frac{d_*z_*}{Z_+}
\frac{(1-\theta^2)Z_c^2}
{Z_+^2-\theta^2Z_c^2}
>0.
}
\]

This is an explicit positive recurrent-time density of high-enstrophy states.

---

## 7. First-hitting transfer of every high-enstrophy time

At any time in `A_theta`, standard Leray enstrophy satisfies

\[
Z_L(s)\ge\theta Z_c
=
\theta54\pi^2\nu^{3/2}.
\]

Let the time lie in first-hitting stage `j`. The exact normalization bridge gives

\[
Z_L(s)
=
\nu^{3/2}\Theta_j(t)^{1/2}\widetilde Z_j(t).
\]

On the recurrent stage corridor,

\[
\Theta_j(t)\le\Theta_+
=
\frac{q}{q-1}L_+.
\]

Hence every high-enstrophy time satisfies

\[
\boxed{
\widetilde Z_j(t)
\ge
\theta54\pi^2
\Theta_+^{-1/2}
}
\]

or

\[
\boxed{
\widetilde Z_j(t)
\ge
\theta54\pi^2
\sqrt{\frac{q-1}{qL_+}}.
}
\]

Thus the large parent-normalized enstrophy witness occurs on a positive Leray-time density, not merely along an exceptional sequence.

---

## 8. Positive-density canonical remote-mass witnesses

During stage `j`, parent-normalized vorticity obeys

\[
\|\Omega_j\|_\infty\le q.
\]

Fix `0<epsilon<1` and define its canonical enstrophy quantile radius

\[
R_\varepsilon[\Omega_j]
=
\inf\left\{
R:
\int_{B_R}|\Omega_j|^2
\ge
(1-\varepsilon)\widetilde Z_j
\right\}.
\]

The amplitude cap gives

\[
R_\varepsilon^3
\ge
\frac{3(1-\varepsilon)}{4\pi q^2}
\widetilde Z_j.
\]

Therefore on every `A_theta` time,

\[
\boxed{
R_\varepsilon^3
\ge
\theta
\frac{81\pi}{2q^2}
(1-\varepsilon)
\sqrt{\frac{q-1}{qL_+}}.
}
\]

Moreover for every `0<alpha<1`,

\[
\boxed{
\int_{|y|>\alpha R_\varepsilon}
|\Omega_j|^2dy
>
\varepsilon\widetilde Z_j
\ge
\varepsilon\theta54\pi^2
\sqrt{\frac{q-1}{qL_+}}.
}
\]

Hence a bounded-`Z` recurrent survivor must generate **positive-density finite remote-vorticity witnesses**.

---

## 9. Consequence for the common branch map

The previous result only showed that at least one late high-enstrophy witness exists.

The present density upgrade gives

\[
\boxed{
\text{bounded-Z recurrent survivor}
\Longrightarrow
\text{positive-density high-enstrophy/remote-mass windows}.
}
\]

At each such window the amplitude-sensitive shell decomposition gives the finite alternatives

\[
\boxed{
H_{remote}
\lor
\text{kinetic / critical-cubic velocity reservoir}.
}
\]

Therefore a hypothetical survivor cannot hide all large remote reservoirs in an asymptotically zero-density exceptional set.

This is the needed bridge toward the genealogy/return-density ledger.

---

## 10. What is still not proved

Positive Eulerian time density does not by itself identify the same material packet across different stages.

Therefore one still may not conclude

\[
\text{positive-density remote mass}
\Longrightarrow
\mathfrak R_k\gtrsim J_k^{1/2}
\]

without a physical genealogy or transport lemma.

The remaining distinction is now sharply isolated:

\[
\boxed{
\text{Eulerian positive-density recurrence}
\quad\text{versus}\quad
\text{material return/genealogy}.
}
\]

---

## 11. DSD audit

The new formed channels are finite:

- recurrent time-average measure `mu`;
- `Z`-weighted measure `mu_Z`;
- high-enstrophy set `A_theta`;
- finite density lower bound;
- finite canonical remote-mass witness at each selected time.

No material identity is inferred merely from repeated Eulerian occupancy.

---

## 12. Updated frontier

The common remaining cubic-tail branch now has a stronger property:

\[
\boxed{
\text{the remote/high-enstrophy structure is recurrent with positive Eulerian time density.}
}
\]

Thus the next genuine gate is not to prove repeated occurrence; that is now done.

The next gate is the **Eulerian-to-Material Genealogy Gate (EMGG)**:

\[
\boxed{
\text{Does positive-density recurrent remote vorticity occupancy force either}
\text{ material return density, turnover, or derivative action?}
}
\]

If EMGG yields the existing weighted return estimate

\[
\mathfrak R_k\gtrsim J_k^{1/2}
\]

on a cubic-divergent subset, the finite Leray dissipation ledger closes that branch.

Current status:

\[
\boxed{\text{EMGG: NOT DERIVED.}}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
