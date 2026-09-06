# DSD M17-236 — Bounded-coefficient mean-dominated packets are sign balanced and evade the global signed kappa budget by low-amplitude cancellation

Date: 2026-09-06  
Canonical ID: **M17-236**

Status: **SIGNED-BUDGET FIREWALL / M17-233--234 GIVE, ON THE BOUNDED-DIMENSIONLESS-KAPPA MEAN-DOMINATED ROOT PACKET, A FIXED CRITICAL ABSOLUTE POTENTIAL MASS WHILE THE COMPACT CE-H TEST FORCES THE SIGNED LOCAL KAPPA MEAN TO BE SMALL. AFTER CHOOSING A CUT-OFF WITH A THIN FIXED TRANSITION AND TAKING THE MEAN-DOMINATION THRESHOLD SUFFICIENTLY SMALL, THIS IMPLIES THAT BOTH THE POSITIVE AND NEGATIVE PARTS OF KAPPA CARRY `L1` MASS OF ORDER `ell` ON THE GOOD AMPLITUDE REGION. SINCE `|W|^2` THERE IS COMPARABLE TO `M/ell^3`, EACH SIGN CARRIES A WEIGHTED CE-H FIRST-MOMENT BUDGET OF ORDER `M ell^-2`. THESE TWO LARGE RELATIVE CONTRIBUTIONS MAY CANCEL INSIDE THE SAME REMOTE PACKET. CONSEQUENTLY THE GLOBAL SIGNED IDENTITY `int kappa|W|^2=-P` AND M5-604 REMOTE SIGNED-BUDGET TIGHTNESS DO NOT CLOSE THE NEW COEFFICIENT BRANCH: `M ell^-2` MAY VANISH AS THE PACKET AMPLITUDE DEGENERATES, AND THE POSITIVE/NEGATIVE PARTS MAY nearly cancel. THE NEXT REQUIRED RETURN MUST CONTROL AN ABSOLUTE OR GRADIENT COEFFICIENT CHARGE RATHER THAN ONLY THE SIGNED KAPPA MOMENT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Root coefficient packet

Use the M17-233--235 root intrinsic packet

\[
B=B_{A\ell}(q),
\qquad
W=c+w,
\]

with

\[
\int_B|w|^2<\theta M,
\qquad
M:=\int_B|W|^2,
\]

and bounded dimensionless coefficient

\[
\boxed{
\|\kappa\|_{L^\infty(B)}
\le K_0\ell^{-2}.
}
\]

M17-233 gives

\[
\boxed{
\int_K|\kappa|^{3/2}dy
\ge d_0>0
}
\]

on an inner core `K` of volume comparable to `ell^3`.

M17-234 gives a compact weighted signed mean satisfying

\[
\boxed{
\left|\int\phi\kappa\,dy\right|
\le C\sqrt\theta\,\ell
}
\]

for a cutoff `phi` equal to one on `K`.

---

## 2. Absolute L1 kappa mass is of order ell

Using

\[
|\kappa|^{3/2}
\le
\|\kappa\|_\infty^{1/2}|\kappa|,
\]

M17-233 gives

\[
\int_K|\kappa|dy
\ge
\frac{d_0}{K_0^{1/2}\ell^{-1}}.
\]

Hence

\[
\boxed{
\int_K|\kappa|dy
\ge c_0\ell,
}
\]

with `c0>0` depending only on the fixed coefficient and geometry constants.

This is the natural first-moment scaling of a potential of size `ell^-2` occupying volume `ell^3`.

---

## 3. Sharpen the signed mean to the inner core

Choose the cutoff geometry so the transition collar

\[
T:=\operatorname{supp}\nabla\phi
\]

has a fixed small relative volume fraction `delta>0`:

\[
|T|\le C\delta\ell^3.
\]

The derivative constants of `phi` may depend on this fixed `delta`; they remain independent of the packet sequence.

The bounded coefficient gives

\[
\left|\int_T\phi\kappa\right|
\le
K_0\ell^{-2}|T|
\le C K_0\delta\ell.
\]

Since `phi=1` on `K`, M17-234 therefore yields

\[
\boxed{
\left|\int_K\kappa\,dy\right|
\le
C\left(\sqrt\theta+K_0\delta\right)\ell.
}
\]

Choose fixed `delta` and then `theta` so that

\[
C(\sqrt\theta+K_0\delta)
\le\frac14c_0.
\]

Then

\[
\boxed{
\left|\int_K\kappa\right|
\le\frac14c_0\ell.
}
\]

---

## 4. Both signs of kappa are present at order ell

Write

\[
\kappa=\kappa_+-\kappa_-,
\qquad
|\kappa|=\kappa_++\kappa_-.
\]

Let

\[
P_1:=\int_K\kappa_+dy,
\qquad
N_1:=\int_K\kappa_-dy.
\]

Section 2 gives

\[
P_1+N_1\ge c_0\ell,
\]

while Section 3 gives

\[
|P_1-N_1|\le\frac14c_0\ell.
\]

Therefore

\[
\boxed{
P_1\ge c_1\ell,
\qquad
N_1\ge c_1\ell
}
\]

for a fixed `c1>0`.

Thus the bounded coefficient packet is intrinsically sign balanced: neither the positive nor the negative potential population can disappear.

---

## 5. Remove the small vorticity-cancellation set

Let

\[
E:=\{|w|>|c|/2\}
\]

as in M17-233.

Then

\[
|E|\le C\theta\ell^3.
\]

The coefficient ceiling gives

\[
\int_E|\kappa|dy
\le K_0\ell^{-2}|E|
\le C K_0\theta\ell.
\]

Choose `theta` smaller if necessary so that this is at most `c1 ell/2`.

Then on the good set

\[
G:=K\setminus E
\]

we retain

\[
\boxed{
\int_G\kappa_+dy\ge c_2\ell,
\qquad
\int_G\kappa_-dy\ge c_2\ell.
}
\]

On `G`,

\[
|W|\ge|c|/2.
\]

---

## 6. Each sign carries weighted CE-H budget of order M ell^-2

Mean domination gives

\[
|c|^2
\ge c\frac{M}{|B|}
\ge c_A M\ell^{-3}.
\]

Therefore

\[
\begin{aligned}
\int_G\kappa_+|W|^2dy
&\ge
\frac{|c|^2}{4}
\int_G\kappa_+dy\\
&\ge cM\ell^{-3}\cdot\ell,
\end{aligned}
\]

so

\[
\boxed{
\int_G\kappa_+|W|^2dy
\ge cM\ell^{-2}.
}
\]

Likewise

\[
\boxed{
\int_G\kappa_-|W|^2dy
\ge cM\ell^{-2}.
}
\]

Thus both signs are individually large in **packet-normalized** units.

---

## 7. Why the global signed kappa identity does not close the packet

Globally CE-H gives

\[
\boxed{
\int_{\mathbb R^3}\kappa|W|^2dy
=-\int_{\mathbb R^3}|\nabla W|^2dy<0.
}
\]

M5-604 shows that the fixed global negative signed budget cannot be carried by the remote spectator tail.

However M17-236 packets satisfy a different structure:

\[
\int_G\kappa_+|W|^2
\gtrsim M\ell^{-2},
\]

and

\[
\int_G\kappa_-|W|^2
\gtrsim M\ell^{-2}.
\]

The signed difference can therefore be much smaller than either absolute part.

Moreover

\[
M\ell^{-2}
\]

may tend to zero on the relative-amplitude branch.

Hence

\[
\boxed{
\text{large relative positive/negative coefficient activity}
\not\Rightarrow
\text{fixed remote signed kappa budget}.
}
\]

M5-604 and the packet are compatible.

---

## 8. Relation to M17-209

The positive part of `kappa` is not absent; it occupies an intrinsic region with nontrivial first moment.

M17-209 shows that sufficiently persistent positive high-`kappa` regions force intrinsic amplitude growth or `kappa`-gradient concentration.

M17-234--235 already place the bounded-spike branch in the gradient-critical/diffusion channel.

Thus the sign-balanced result is consistent with the coefficient-gradient frontier rather than providing a new terminal branch.

---

## 9. Correct remaining amplitude firewall

The problem after M17-236 is not the existence of a negative `kappa` payer.

It is that all natural **weighted** coefficient costs retain powers of the vanishing vorticity amplitude.

The required Amplitude-Return Gate must therefore use one of

1. an unweighted coefficient charge such as the M17-234 critical gradient;
2. a genealogy theorem preventing `M ell^-2` from vanishing on every recurrent shell generation;
3. a shell-level aggregate that survives positive/negative cancellation;
4. a nodal/replenishment transition forced by repeated sign-balanced coefficient formation.

The global signed identity alone is insufficient.

---

## 10. DSD audit

- Absolute and signed kappa moments are explicitly separated.
- The existence of both signs is proved only on the bounded-dimensionless-coefficient mean-dominated branch.
- The transition collar is fixed geometrically before the sequence limit; no vanishing collar is used.
- Weighted positive and negative budgets are not treated as globally separately conserved quantities.
- M5-604 is not contradicted; its signed remote-tail theorem remains valid.
- The remaining obstruction is amplitude cancellation, not sign bookkeeping.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
