# Anti-Proof Audit — Tail Endpoint Scope Correction — 2026-08-24

Status: **OVER-COMPRESSION CORRECTED / WEAK-L3 ENDPOINT IS CONDITIONAL ON ANNULAR CRITICAL H1/H2 CONTROL / GLOBAL REGULARITY NOT PROVED.**

Recent frontier summaries compressed the bounded-enstrophy ancient survivor to

\[
\text{locally recurrent core}
+
\text{escaping weak-}L^3\text{ endpoint tail}.
\]

That statement is too strong without an additional spatial tail bridge.

The bounded-Z ancient information

\[
V\in L_s^\infty(L_x^6\cap L_x^\infty),
\qquad
W=\nabla\times V\in L_s^\infty L_x^2
\]

allows spatial tails slower than `1/R` while still keeping `V in L6` and `W in L2`. Therefore weak-L3 endpoint behavior is not automatic.

---

## 1. Exact annular quantities

For dyadic annuli

\[
A_R=\{R<|Y|<2R\},
\]

define

\[
\mathfrak E_1(R,s)
=R\int_{A_R^*}|\nabla V|^2dY,
\]

and

\[
\mathfrak E_2(R,s)
=R^3\int_{A_R^*}|\nabla^2V|^2dY.
\]

For the critical model `V~1/R`, both are order one.

`ANNULAR_H2_SPATIAL_TYPEI_TAIL_BRIDGE_2026-08-24.md` proves

\[
\boxed{
\sup_{s,R}\mathfrak E_1<\infty,
\quad
\sup_{s,R}\mathfrak E_2<\infty
\Longrightarrow
|V(Y,s)|\lesssim |Y|^{-1}.
}
\]

Only after this step is a weak-L3 / borderline Type-I tail description justified.

---

## 2. Bounded global enstrophy does not bound the critical shell sup

Let

\[
e_k(s)=\int_{A_{2^k}}|\nabla V|^2dY.
\]

Global bounded enstrophy gives

\[
\sum_ke_k(s)\le Z_+.
\]

But

\[
\mathfrak E_1(2^k,s)
\sim2^ke_k(s)
\]

may still diverge.

For example, a summable sequence such as

\[
e_k\sim2^{-k/2}
\]

has

\[
\sum_ke_k<\infty
\]

while

\[
2^ke_k\sim2^{k/2}\to\infty.
\]

Thus

\[
\boxed{
W\in L^2
\not\Longrightarrow
\sup_RR\int_{A_R}|W|^2<\infty.
}
\]

The same distinction applies even more strongly to the second-derivative quantity `E2`.

---

## 3. Finite mean global palinstrophy is still insufficient

The recurrent statistical enstrophy identity gives

\[
\frac14\overline Z+
u\overline Q
=\overline{\mathcal P},
\]

and the bounded recurrent corridor implies a finite time-average

\[
\overline Q<\infty.
\]

However

\[
Q(s)=\int_{\mathbb R^3}|\nabla W|^2dY
\]

controls only the unweighted sum of shell second-derivative mass.

It does **not** imply

\[
\sup_RR^3
\int_{A_R}|\nabla W|^2<\infty.
\]

Therefore the critical annular H2 tail cannot be silently absorbed into the recurrent mean-palinstrophy budget.

---

## 4. Correct bounded-Z tail trichotomy

The honest bounded-Z ancient tail frontier is

\[
\boxed{
\text{spatial Type-I / weak-L3-like corridor}
\quad\lor\quad
H_{1,crit}^{tail}
\quad\lor\quad
H_{2,crit}^{tail},
}
\]

where

\[
H_{1,crit}^{tail}:
\sup_{R\to\infty}
R\int_{A_R}|\nabla V|^2=\infty,
\]

and

\[
H_{2,crit}^{tail}:
\sup_{R\to\infty}
R^3\int_{A_R}|\nabla^2V|^2=\infty.
\]

Only the first branch may be further refined into a weak-L3/Lorentz endpoint shell stack.

---

## 5. Relation to older H_remote

It is tempting to rename both critical failures as `H_remote`, but this is not automatic.

The older `H_remote` branch arose from derivative mass escaping normalized compact sets in the first-hitting sequence. The present quantities are **scale-weighted annular sup failures in the ancient/Leray limit**.

A valid identification requires a transfer lemma:

\[
\boxed{
H_{1,crit}^{tail}\lor H_{2,crit}^{tail}
\Longrightarrow
\text{prelimit remote derivative/enstrophy escape with the repository's H threshold}.
}
\]

Until this is written, the two critical tail failures remain explicit separate subbranches.

---

## 6. Spatial examples showing the necessity of the split

A schematic tail

\[
|V(Y)|\sim |Y|^{-\alpha},
\qquad
\frac12<\alpha<1,
\]

has

\[
V\in L^6(\{|Y|>1\})
\]

and

\[
\nabla V\in L^2(\{|Y|>1\}),
\]

but generally

\[
V\notin L^{3,\infty}
\]

and

\[
R\int_{A_R}|\nabla V|^2
\sim R^{2-2\alpha}\to\infty.
\]

Thus the supercritical annular H1 tail is not an artificial bookkeeping possibility; it is compatible with the currently inherited global norms.

Whether such a profile can be an actual ancient Navier--Stokes tail under all recurrent/first-hitting constraints is the problem to be proved, not assumed away.

---

## 7. Revised endgame

On the bounded-Z branch the accurate endgame is

\[
\boxed{
\begin{aligned}
\text{nonzero recurrent ancient core}
\Longrightarrow{}&
\text{spatial Type-I / weak-L3-like tail}
\\
&\lor H_{1,crit}^{tail}
\\
&\lor H_{2,crit}^{tail}
\\
&\lor\text{already typed projective/turnover exits}.
\end{aligned}
}
\]

The spatial Type-I branch can use the one-slice/RSS/RDSS and Lorentz endpoint machinery already collected.

The two critical shell failures require a transfer back to prelimit H/T or a direct ancient tail rigidity argument.

---

## 8. Anti-proof conclusion

The earlier phrase

\[
\text{``the final survivor is a recurrent core plus an escaping weak-L3 endpoint tail''}
\]

must be read only as a **subcorridor statement**, not as an exhaustive theorem.

The corrected exhaustive statement retains the two scale-weighted annular escape modes explicitly.

Status: **ANTI-PROOF AUDIT FOUND A SECOND REAL SCOPE ISSUE: GLOBAL L6 + VORTICITY L2 DOES NOT FORCE A WEAK-L3 ENDPOINT TAIL. THE ENDPOINT DESCRIPTION REQUIRES UNIFORM CRITICAL ANNULAR H1/H2 CONTROL. FAILURE OF EITHER BOUND IS A DISTINCT TAIL SUBBRANCH UNTIL A PRELIMIT H/T TRANSFER LEMMA IS PROVED. GLOBAL REGULARITY REMAINS UNPROVED.**