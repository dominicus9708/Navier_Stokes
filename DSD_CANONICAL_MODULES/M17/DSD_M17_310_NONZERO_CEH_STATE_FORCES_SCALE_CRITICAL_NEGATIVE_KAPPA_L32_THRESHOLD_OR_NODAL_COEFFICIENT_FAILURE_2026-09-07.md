# DSD M17-310 — Every nonzero regular CE-H state forces a scale-critical negative-`kappa` `L^{3/2}` threshold or a nodal/coefficient failure

Date: 2026-09-07  
Canonical ID: **M17-310**

Status: **LOSSLESS CE-H COEFFICIENT RIGIDITY GATE / M17-308 SHOWS THAT AN INVERSE-LENGTH-SQUARED COEFFICIENT HAS STATIC CRITICAL SPACE `L^(3/2)` UNDER THE M5-478 RECORD BLOW-DOWN. ON THE REGULAR CE-H COEFFICIENT BRANCH, `Delta W=kappa W`. TESTING AGAINST `W` GIVES `||grad W||_2^2=-int kappa|W|^2`, SO THE NEGATIVE PART OF `kappa` MUST SUPPORT ALL OF THE POSITIVE DIRICHLET ENERGY. HOLDER PLUS THE 3D SOBOLEV INEQUALITY THEN GIVES A UNIVERSAL AMPLITUDE-INDEPENDENT THRESHOLD `||kappa_-||_(L^(3/2)) >= S_3>0` FOR EVERY NONZERO `H1` CE-H STATE. THIS THRESHOLD IS EXACTLY INVARIANT UNDER RECORD BLOW-DOWN: NO `R_m^-1` FACTOR APPEARS. IF `kappa` CANNOT BE EXTENDED AS A REGULAR `L^(3/2)` COEFFICIENT ACROSS THE RELEVANT NODAL SET, THAT FAILURE IS EXPORTED AS AN EXPLICIT NODAL/COEFFICIENT-SINGULARITY BRANCH RATHER THAN HIDDEN. THE RESULT DOES NOT YET GIVE A FINITE BUDGET OR CONTRADICTION; IT IDENTIFIES A GENUINELY LOSSLESS, SIGNED, AMPLITUDE-INDEPENDENT CE-H CURRENCY THAT SURVIVES EVERY RECORD GENERATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Regular CE-H coefficient branch

Let

\[
W\in H^1(\mathbb R^3;\mathbb R^3),
\qquad
W\not\equiv0,
\]

be one CE-H state.

On the present regular coefficient branch assume there exists a real measurable scalar `kappa` such that

\[
\boxed{
\Delta W=\kappa W
}
\]

in the weak/distributional sense on all of `R3`, with

\[
\boxed{
\kappa_-:=\max\{-\kappa,0\}
\in L^{3/2}(\mathbb R^3).
}
\]

If the scalar multiplier cannot be extended across a relevant nodal set so that the equation has this global weak meaning, retain instead the explicit exit

\[
\boxed{G_{nodal/coefficient}.}
\]

If `kappa_-` exists but is not in `L^(3/2)`, retain

\[
\boxed{G_{critical\ kappa_-\ tail}.}
\]

The theorem below concerns the finite critical-coefficient branch.

---

## 2. Exact signed elliptic identity

Take the weak `L2` pairing of

\[
\Delta W=\kappa W
\]

with `W`.

Integration by parts gives

\[
\boxed{
-\int_{\mathbb R^3}|\nabla W|^2dy
=
\int_{\mathbb R^3}\kappa|W|^2dy.
}
\]

Equivalently,

\[
\boxed{
\|\nabla W\|_2^2
=
-\int\kappa|W|^2.
}
\]

Split

\[
\kappa=\kappa_+-\kappa_-.
\]

Then

\[
\|\nabla W\|_2^2
=
\int\kappa_-|W|^2
-
\int\kappa_+|W|^2
\le
\int\kappa_-|W|^2.
\]

Thus

\[
\boxed{
\|\nabla W\|_2^2
\le
\int\kappa_-|W|^2.
}
\]

The positive part of `kappa` cannot pay the CE-H Dirichlet energy; only the negative part can.

---

## 3. Holder at the critical exponent

By Holder,

\[
\int\kappa_-|W|^2
\le
\|\kappa_-\|_{L^{3/2}}
\||W|^2\|_{L^3}.
\]

Since

\[
\||W|^2\|_{L^3}=\|W\|_{L^6}^2,
\]

we get

\[
\boxed{
\|\nabla W\|_2^2
\le
\|\kappa_-\|_{3/2}
\|W\|_6^2.
}
\]

Let `S_3>0` denote any valid Sobolev coercivity constant in

\[
\boxed{
S_3\|f\|_6^2
\le
\|\nabla f\|_2^2
\qquad
(f\in\dot H^1(\mathbb R^3)).
}
\]

Apply this componentwise/vectorially to `W`:

\[
\|W\|_6^2
\le
S_3^{-1}\|\nabla W\|_2^2.
\]

Therefore

\[
\|\nabla W\|_2^2
\le
S_3^{-1}
\|\kappa_-\|_{3/2}
\|\nabla W\|_2^2.
\]

---

## 4. Nonzero `L2` state has nonzero gradient

If

\[
\|\nabla W\|_2=0,
\]

then `W` is spatially constant almost everywhere.

Because

\[
W\in L^2(\mathbb R^3),
\]

the only such constant is zero, contradicting

\[
W\not\equiv0.
\]

Hence

\[
\boxed{
\|\nabla W\|_2>0.
}
\]

We may divide the inequality of Section 3 by the Dirichlet energy.

This gives the universal threshold

\[
\boxed{
\|\kappa_-\|_{L^{3/2}(\mathbb R^3)}
\ge
S_3>0.
}
\]

The constant depends only on the Sobolev normalization, not on the amplitude, location, or scale of `W`.

---

## 5. Stronger weighted negative-part statement

The exact identity also gives

\[
\int\kappa_-|W|^2
=
\|\nabla W\|_2^2
+
\int\kappa_+|W|^2.
\]

Therefore

\[
\boxed{
\int\kappa_-|W|^2
\ge
\|\nabla W\|_2^2.
}
\]

Thus the negative coefficient population carries at least the full vorticity Dirichlet charge in the `|W|^2`-weighted measure.

This weighted statement retains the amplitude firewall, but the `L^(3/2)` threshold of Section 4 does not.

---

## 6. Exact record-blow-down invariance

Under M5-478 scaling,

\[
W_R(y,s)=R^2W(Ry,R^2s)
\]

for vorticity and

\[
\boxed{
\kappa_R(y,s)=R^2\kappa(Ry,R^2s)
}
\]

for the CE-H coefficient, because

\[
\Delta_yW_R
=R^4\Delta_xW
=R^4\kappa W
=\kappa_R W_R.
\]

The negative part scales identically:

\[
(\kappa_R)_-(y,s)
=R^2\kappa_-(Ry,R^2s).
\]

Hence

\[
\begin{aligned}
\int|(\kappa_R)_-|^{3/2}dy
&=
\int R^3|\kappa_-(Ry)|^{3/2}dy\\
&=
\int|\kappa_-(x)|^{3/2}dx.
\end{aligned}
\]

Therefore

\[
\boxed{
\|(\kappa_R)_-\|_{3/2}
=
\|\kappa_-\|_{3/2}.
}
\]

In particular every nonzero regular CE-H record cell satisfies

\[
\boxed{
\|(\kappa_R)_-\|_{3/2}
\ge S_3.
}
\]

There is no `R^-1` ancestry loss.

---

## 7. Comparison with the late amplitude-weighted coefficient firewall

M17-235 produces a natural multiplier-gradient diffusion charge of the form

\[
\int\rho^2|\nabla\kappa|^2,
\]

whose lower bound still contains packet mass/amplitude.

The present quantity is fundamentally different:

\[
\boxed{
\|\kappa_-\|_{3/2}
}
\]

is

1. amplitude independent;
2. scale critical;
3. sign resolved;
4. invariant under the record blow-down;
5. forced by the mere existence of a nonzero regular CE-H `H1` state.

Thus it is a genuine candidate currency for a cross-generation CE-H rigidity theorem.

---

## 8. Relation to M17-233/234

M17-233 derives a critical `|kappa|^(3/2)` occupancy on a mean-dominated intrinsic packet under a bounded dimensionless coefficient ceiling.

M17-234 then forces coefficient variation/gradient.

M17-310 differs in scope:

- it is global rather than a root intrinsic packet estimate;
- it requires the regular global coefficient branch;
- it selects specifically the **negative** part;
- it requires no mean-dominance assumption;
- it gives a universal threshold directly from the elliptic identity and Sobolev inequality.

Thus it does not replace M17-233/234, but it gives a lossless signed background constraint that those local packet arguments must respect.

---

## 9. What this does not prove

A fixed lower bound

\[
\|\kappa_-\|_{3/2}\ge S_3
\]

is not a contradiction.

Schrodinger-type zero-energy structures can in principle require critical negative potential strength, and the present calculation does not exclude them.

Nor does the spatial `L^(3/2)` threshold imply that a fixed material carrier spends a fixed fraction of time in negative `kappa`.

The missing bridge is therefore now precise:

\[
\boxed{
\text{spatial critical negative-}kappa\text{ mass}
\Longrightarrow
\text{material/flux residence, turnover, or another critical endpoint}.
}
\]

That conversion must preserve the amplitude-independent and record-invariant nature of the coefficient threshold.

---

## 10. Corrected CE-H critical frontier

Combining M17-307--310 gives

\[
\boxed{
\begin{aligned}
\text{CE-H record survivor}
\Longrightarrow{}&
H_{palinstrophy\ critical\ saturation}\\
&\lor H_{critical\ kappa_-\ threshold}\\
&\lor G_{critical\ kappa_-\ tail}\\
&\lor G_{nodal/coefficient}\\
&\lor G_{strict\ scale\ descent/interface}.
\end{aligned}
}
\]

The palinstrophy branch has a finite but `R^-1`-weighted ancestry ledger.

The `kappa_- L^(3/2)` branch has **lossless ancestry but no known finite cumulative budget**.

This isolates the exact tradeoff that the next theorem must overcome.

---

## 11. DSD audit

- The sign of `kappa` is fixed by the exact integration-by-parts identity; no heuristic damping interpretation is used.
- The negative part is separated before Holder.
- The exponent `3/2` is exactly the scale-critical coefficient exponent in three dimensions.
- Division by the Dirichlet energy is justified because a nonzero `L2` field cannot have zero gradient.
- Nodal/global-coefficient failure is retained explicitly.
- Infinite `L^(3/2)` coefficient mass is an exit, not silently treated as finite.
- The threshold is not called a finite budget or contradiction.
- No external theorem beyond the standard Sobolev inequality is required.
- Global regularity remains unproved.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
