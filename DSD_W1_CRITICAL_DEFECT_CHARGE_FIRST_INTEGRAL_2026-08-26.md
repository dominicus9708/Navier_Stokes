# DSD W1 Critical Defect Charge as a First Integral

Date: 2026-08-26

Status: **THE `p downarrow 3` ABELIAN DEFECT COEFFICIENT IS SHOWN TO BE TIME-INDEPENDENT ALONG ANY W1 ORBIT ON WHICH THE ESTABLISHED UNIFORM ENDPOINT LIMITS HOLD / THE POSITIVE WEAK-L3 DEFECT IS THEREFORE A DYNAMICAL FIRST INTEGRAL, NOT A QUANTITY RECREATED BY EACH RECURRENT CORE EVENT / GLOBAL REGULARITY UNPROVED.**

## 1. Endpoint family

For

\[
p=3+\varepsilon,
\qquad \varepsilon>0,
\]

define

\[
X_p(s):=\|U(s)\|_p^p
\]

and the Abelian critical quantity

\[
\boxed{
Y_\varepsilon(s)
:=
\varepsilon X_{3+\varepsilon}(s).
}
\]

The existing W1 endpoint analysis identifies

\[
\boxed{
\mathscr R_3(s)
:=
\lim_{\varepsilon\downarrow0}Y_\varepsilon(s)
}
\]

with the critical cubic mass per unit logarithmic radius, equivalently with three times the low-amplitude weak-L3 defect coefficient.

---

## 2. Exact `Lp` balance

The Leray `Lp` identity is

\[
\frac1pX_p'
+\frac{p-3}{2p}X_p
+\nu D_p
=\Pi_p.
\]

Hence

\[
X_p'
=-\frac{p-3}{2}X_p
-p\nu D_p
+p\Pi_p.
\]

Set `p=3+epsilon` and multiply by `epsilon`:

\[
\boxed{
Y_\varepsilon'
=-\frac\varepsilon2Y_\varepsilon
-(3+\varepsilon)\nu\varepsilon D_{3+\varepsilon}
+(3+\varepsilon)\varepsilon\Pi_{3+\varepsilon}.
}
\]

---

## 3. Uniform endpoint bounds

The previous pressure-gauge repair and `D3` endpoint audit establish, on the compact W1 class and for `p` in one fixed interval `[3,3+epsilon0]`, uniform bounds of the form

\[
\sup_{s\in\mathbb R}
D_p(s)\le C_D,
\]

and

\[
\sup_{s\in\mathbb R}
|\Pi_p(s)|\le C_\Pi,
\]

or the corresponding local-in-time compact bounds sufficient for the passage below.

Therefore

\[
\boxed{
|Y_\varepsilon'(s)|
\le C\varepsilon
+
\frac\varepsilon2|Y_\varepsilon(s)|.
}
\]

Since the endpoint family `Y_epsilon` is uniformly bounded on W1 by the established Abelian shell-density control,

\[
\boxed{
\sup_s|Y_\varepsilon'(s)|\le C_*\varepsilon.
}
\]

---

## 4. Passage to the endpoint

For any two times `s1<s2`,

\[
|Y_\varepsilon(s_2)-Y_\varepsilon(s_1)|
\le C_*\varepsilon|s_2-s_1|.
\]

Let `epsilon downarrow 0`. Wherever the Abelian endpoint limit exists,

\[
\boxed{
\mathscr R_3(s_2)=\mathscr R_3(s_1).
}
\]

Thus

\[
\boxed{
\partial_s\mathscr R_3=0
}
\]

in the orbitwise sense.

The critical defect coefficient is a first integral of the W1 dynamics.

---

## 5. Equivalent invariant quantities

Because the previous endpoint identifications give

\[
K(0+)=\frac{\mathscr R_3}{3},
\]

and

\[
\mathscr C_{WL3}=\frac{\mathscr R_3}{3}
\]

at the exact/Abelian defect level, all of the following are time-independent along the W1 orbit:

\[
\boxed{
\mathscr R_3,
\qquad
K(0+),
\qquad
\mathscr C_{WL3}.
}
\]

Thus the recurrent finite-core formation cycle does not generate and destroy this charge periodically. It evolves inside one fixed critical-defect sector.

---

## 6. Consequence for minimal sets

Every orbit in a minimal invariant set is dense in that set. Since the critical defect is invariant along each orbit, a minimal W1 set lies inside one defect-charge level

\[
\boxed{
\mathscr R_3=\mathscr R_{3,*}.
}
\]

For the current survivor,

\[
\boxed{
\mathscr R_{3,*}>0.
}
\]

Therefore periodic and aperiodic recurrent dynamics are both motions on the same positive-defect hypersurface in the current state-space description.

---

## 7. DSD audit: source vs invariant state label

Earlier proof language sometimes described the recurrent core as continuously 'creating' the endpoint residue.

The present calculation shows that this language is too causal.

The exact DSD statement is

\[
\boxed{
\text{W1 state enters a positive critical-defect sector}
\quad\Longrightarrow\quad
\text{the defect charge is preserved by the W1 orbit}.
}
\]

Core pressure/stretching cycles are required to maintain the full Navier--Stokes dynamics inside this sector, but `R3` itself is an orbit label rather than a periodically recreated source.

---

## 8. Why this still does not close the proof

Every fixed finite-energy prelimit state has zero low-amplitude defect,

\[
\mathscr R_3^{pre}(s)=0,
\]

whereas the W1 omega-limit survivor has

\[
\mathscr R_{3,*}>0.
\]

The discontinuity is possible because the Leray limit is noncompact in `L2`: critical mass can escape to spatial infinity while remaining compact in every `Lp`, `p>3`.

Thus the remaining no-defect theorem is now even more sharply stated:

\[
\boxed{
\text{exclude the creation of a positive conserved critical-defect sector in the omega-limit of a finite-energy prelimit.}
}
\]

No proof of that compactness theorem is given here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
