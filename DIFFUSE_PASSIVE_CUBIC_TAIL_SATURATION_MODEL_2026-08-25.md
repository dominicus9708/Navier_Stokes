# Diffuse Passive Cubic-Tail Saturation Model

Date: 2026-08-25

Status: **FUNCTIONAL COUNTERMODEL TO STATIC COVERAGE/ENERGY CLOSURE / NOT A NAVIER–STOKES SOLUTION / DYNAMIC TAIL RIGIDITY STILL REQUIRED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The corrected bounded-\(Z\), recurrent, non-\(L^3\) branch requires

\[
\sum_kJ_k^{3/2}=\infty.
\]

Recent genealogy work asks whether this divergent cubic mass must be carried by identifiable first-hitting packets or center-switch descendants.

This note constructs an explicit divergence-free shell field showing that the currently available **static** norm, Morrey, fixed-frequency, and derivative ledgers do not force such packet coverage.

The construction is not claimed to solve Navier–Stokes. Its role is anti-proof: it demonstrates exactly which purely functional closures are too weak.

---

## 2. A fixed solenoidal annulus profile

Choose a nonzero smooth divergence-free vector field

\[
F\in C_c^\infty(\mathbb R^3;\mathbb R^3),
\qquad
\nabla\cdot F=0,
\]

supported in a fixed annulus

\[
1<|y|<2.
\]

Let

\[
K_m\to\infty
\]

be a geometric sequence with ratio large enough that the scaled supports are pairwise disjoint, for example a sufficiently sparse subsequence of the first-hitting shell radii.

Let \(a_m>0\) and define

\[
\boxed{
U_m(y)
:=
\frac{a_m}{K_m}
F\!\left(\frac{y}{K_m}\right).
}
\]

Then

\[
\nabla\cdot U_m=0
\]

and \(U_m\) is supported in

\[
K_m<|y|<2K_m.
\]

Because the supports are disjoint, the field

\[
\boxed{U(y):=\sum_mU_m(y)}
\]

is smooth and locally finite.

---

## 3. Exact shell-gradient scaling

Differentiating,

\[
\nabla U_m(y)
=
\frac{a_m}{K_m^2}
(\nabla F)\!\left(\frac{y}{K_m}\right).
\]

Therefore

\[
\begin{aligned}
\int|\nabla U_m|^2dy
&=
\frac{a_m^2}{K_m^4}
K_m^3
\int|\nabla F|^2dz\\
&=
C_{\nabla F}\frac{a_m^2}{K_m}.
\end{aligned}
\]

The critical annular quantity is thus

\[
\boxed{
J_m
:=
K_m\int|\nabla U_m|^2dy
=C_{\nabla F}a_m^2.
}
\]

Hence

\[
\boxed{
J_m^{3/2}
=C_{\nabla F}^{3/2}a_m^3.
}
\]

---

## 4. Critical \(L^3\) mass has the same amplitude cube

Likewise,

\[
\begin{aligned}
\|U_m\|_3^3
&=
\frac{a_m^3}{K_m^3}
K_m^3\|F\|_3^3\\
&=
C_{3}a_m^3.
\end{aligned}
\]

Thus

\[
\boxed{
\|U_m\|_3^3\asymp J_m^{3/2}.
}
\]

Choosing

\[
\boxed{a_m=m^{-1/3}}
\]

gives

\[
\sum_mJ_m^{3/2}
\asymp
\sum_m a_m^3
=
\sum_m\frac1m
=\infty.
\]

Therefore the model has a divergent critical cubic shell ledger.

---

## 5. Yet global enstrophy is finite

Since \(\Omega_m=\nabla\times U_m\) has the same first-derivative scaling,

\[
\boxed{
\|\Omega_m\|_2^2
=C_\Omega\frac{a_m^2}{K_m}.
}
\]

For geometric \(K_m\),

\[
\sum_m\frac{a_m^2}{K_m}<\infty.
\]

Hence

\[
\boxed{\Omega\in L^2.}
\]

This realizes precisely the arithmetic separation

\[
\sum J_m^{3/2}=\infty
\qquad\text{while}\qquad
\sum\|\Omega_m\|_2^2<\infty.
\]

So bounded normalized global enstrophy alone cannot convert the cubic tail into a contradiction.

---

## 6. The all-scale Morrey cost is also bounded

The velocity \(L^2\) mass of one shell is

\[
\|U_m\|_2^2
=
C_2a_m^2K_m.
\]

Hence at its own radius,

\[
\boxed{
K_m^{-1}\|U_m\|_2^2
=C_2a_m^2.
}
\]

Since \(a_m\le1\), the scale-invariant Morrey cost is uniformly bounded.

Although the total velocity \(L^2\) norm of the infinite model need not be finite, this is compatible with the ancient-limit setting where bounded global normalized enstrophy and local/Type-I Morrey control, rather than a uniform global normalized velocity \(L^2\) bound, are the relevant static tail hypotheses.

**Status: STATIC MORREY COMPATIBILITY PROVED.**

---

## 7. \(L^6\), \(L^\infty\), and weak endpoint behavior

For \(p\ge1\),

\[
\|U_m\|_p^p
=
C_p a_m^pK_m^{3-p}.
\]

In particular,

\[
\boxed{
\|U_m\|_6^6
=C_6\frac{a_m^6}{K_m^3},
}
\]

so

\[
U\in L^6.
\]

Also

\[
\boxed{
\|U_m\|_\infty
=\frac{a_m}{K_m}\|F\|_\infty,
}
\]

so the tail is pointwise small and \(U\in L^\infty\).

For this particular construction the shell quantity

\[
\left(\frac{a_m}{K_m}\right)^3K_m^3=a_m^3
\]

is bounded, so the field is compatible with weak-\(L^3\)-type endpoint scaling while failing strong \(L^3\) because \(\sum a_m^3=\infty\).

This is only one possible bounded-\(Z\) tail shape; it is not a claim that every bounded-\(Z\) tail lies in weak \(L^3\).

---

## 8. Every fixed derivative order is cheap

For any integer \(s\ge1\),

\[
\nabla^sU_m
=
\frac{a_m}{K_m^{s+1}}
(\nabla^sF)(y/K_m).
\]

Therefore

\[
\boxed{
\|\nabla^sU_m\|_2^2
=C_s a_m^2K_m^{1-2s}.
}
\]

For \(s=1\), this is \(a_m^2/K_m\).

For \(s=2\),

\[
\|\nabla^2U_m\|_2^2
\asymp
\frac{a_m^2}{K_m^3}.
\]

Every fixed derivative-order tail is summable for geometric \(K_m\).

Thus fixed-order derivative-frequency or palinstrophy estimates, without a dynamic persistence/amplification mechanism, do not eliminate this diffuse shell geometry.

**Status: PROVED.**

---

## 9. Natural-band frequency is not a high-frequency event

The shell is built by pure dilation of a fixed profile. Consequently

\[
\frac{K_m\|\nabla U_m\|_2}{\|U_m\|_2}
=
\frac{\|\nabla F\|_2}{\|F\|_2},
\]

independent of \(m\).

Therefore this construction stays on the non-high-frequency lane:

\[
\boxed{
\Gamma_m=O(1).
}
\]

It cannot be removed merely by declaring the remote tail a derivative-frequency event.

---

## 10. Physical interpretation of the diffuse amplitude

On shell radius \(K_m\), the characteristic velocity amplitude is

\[
|U_m|\sim\frac{a_m}{K_m},
\]

and characteristic vorticity amplitude is

\[
|\Omega_m|\sim\frac{a_m}{K_m^2}.
\]

The shell volume is \(O(K_m^3)\).

Thus its critical gradient cost is generated by a **broad low-amplitude population**, not by an order-one vorticity packet.

In first-hitting genealogy language, the ancestor-level vorticity scale at age \(k\) is \(K_k^{-2}\) in descendant-normalized variables. This model uses only an \(a_k\)-fraction of that amplitude across an \(O(K_k^3)\) volume:

\[
\boxed{
|\Omega_k|\sim a_kK_k^{-2}.
}
\]

If \(a_k\to0\), no fixed-positive ancestor-packet occupancy follows, even though

\[
\sum a_k^3=\infty.
\]

This makes precise the coverage obstruction.

---

## 11. Compatibility with the high-ratio forgetting selection

The amplitude-sensitive historical gate selects shells satisfying

\[
a_kK_k^2\gg1.
\]

For the present choice

\[
a_m=m^{-1/3}
\]

and geometric \(K_m\),

\[
\boxed{a_mK_m^2\to\infty.}
\]

Hence the model lies far above the quiet-forgetting threshold while remaining diffuse and low frequency.

This shows why “cannot be quietly forgotten” does not imply “must contain an order-one ancestor packet.” A diffuse natural-band shell may instead persist passively.

---

## 12. Why ordinary energy packing cannot detect it

A physical counterpart at radius \(R\) with critical amplitude parameter \(a\) has

\[
R\int_{A_R}|\nabla u|^2dx
\sim a^2\nu^2.
\]

Its first-order dissipation over one \(R\)-parabolic time is of size

\[
\sim a^2\nu^2R.
\]

For geometrically shrinking physical radii, the extra \(R\) factor makes such costs summable even when

\[
\sum a^3=\infty.
\]

Thus the static model and the first-hitting time-dissipation audit point to the same obstruction.

---

## 13. What this model does and does not prove

It **does prove** that the following implication is unavailable from the current static function-space estimates alone:

\[
\boxed{
\sum J_k^{3/2}=\infty
+\text{bounded enstrophy/Morrey/fixed-order derivative ledgers}
\not\Rightarrow
\text{fixed-fraction packet coverage}.
}
\]

It also proves that a diffuse broad-shell tail can saturate the critical cubic divergence while keeping the available lower-order and fixed-derivative global quantities finite.

It **does not prove** that such a field is a Navier–Stokes ancient solution, a blow-up profile, or dynamically persistent.

No nonlinear evolution equation has been imposed on \(U\).

Therefore this is an anti-proof functional countermodel, not a Navier–Stokes counterexample.

---

## 14. Updated frontier

The packet-coverage route is now sharply separated into two cases:

\[
\boxed{
\text{cubic tail}
\to
\text{identified occupied packet genealogy}
\lor
\text{diffuse passive shell population}.
}
\]

The first case can be charged through the material/contact/return ledgers already derived.

The second survives every purely static estimate tested here.

Hence the highest-value next target is genuinely dynamical:

\[
\boxed{
\text{Can a nontrivial recurrent ancient Leray core coexist with a diffuse, low-frequency, persistent cubic tail of this scaling?}
}
\]

A successful closure now needs a tail-decoupling, quotient-Liouville, or dynamic shell-rebuilding theorem. More static packet counting cannot suffice.