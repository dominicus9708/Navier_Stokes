# DSD W1 Persistence--Reformation Action Dichotomy

Date: 2026-08-26

Status: **H2-COHERENT VS H2-ESCALATING TAILS RECAST AS FINITE VS INFINITE REFORMATION ACTION / SUBQUADRATIC CRITICAL-H2 GROWTH SHOWN SUFFICIENT FOR STRONG SHELL INHERITANCE / ONLY NEAR-QUADRATIC OR NONSUMMABLE DERIVATIVE ESCALATION CAN BLOCK THE PRESSURE-FREE CURRENT LIMIT / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The current W1 endpoint has two exact critical descriptions:

\[
\mathcal S_B(R)\to \mathscr R_3/6>0
\]

for the velocity/Bernoulli current, and, when the remote shell state is sufficiently coherent,

\[
\mathcal S_\Omega(R)\to \mathscr R_\Omega/4>0
\]

for the pressure-free weighted-vorticity current.

Previously the obstruction to the second limit was recorded as a binary label:

\[
H_{2,crit}^{tail}
\quad\lor\quad
H2\text{-coherent}.
\]

That label is too coarse for the DSD logical chain.  The correct distinction is whether the remote shell state is **inherited** with summable variation or must be **re-formed** through nonsummable derivative-scale variation.

This note quantifies that distinction.

---

## 2. Fixed-cell shell state and all-age weak defect

For a remote shell radius `R`, define

\[
F_R(z,s):=R U(Rz,s)
\]

on a fixed enlarged annulus `A_1^*`.

The W1 all-age co-moving transport theorem gives

\[
\boxed{
\|\delta F_R(h)\|_{H^{-1}(A_1^*)}
\le C R^{-2}
\qquad \forall h\ge0,
}
\]

where `delta F_R(h)` is the difference between the shell state and its co-moving descendant after age `h`.

The W1 fixed-cell H1 bound gives

\[
\|F_R\|_{H^1}\le C_1.
\]

Define the critical second-derivative shell quantity

\[
\boxed{
\mathfrak E_2(R,s)
:=
R^3\int_{A_R^*}|\nabla^2U(Y,s)|^2dY.
}
\]

Critical scaling gives

\[
\|F_R\|_{H^2}^2\asymp \mathfrak E_2(R,s).
\]

For a one-step co-moving comparison, write

\[
\mathfrak E_{2,R}^{pair}
:=
1+\mathfrak E_2(R,s)+\mathfrak E_2(e^{h/2}R,s+h).
\]

Then

\[
\|\delta F_R(h)\|_{H^2}
\le C\bigl(\mathfrak E_{2,R}^{pair}\bigr)^{1/2}.
\]

---

## 3. Exact interpolation cost for changing the shell state

Interpolate `H^-1` and `H2` to `H1`:

\[
\|f\|_{H^1}
\le C
\|f\|_{H^{-1}}^{1/3}
\|f\|_{H^2}^{2/3}.
\]

Therefore

\[
\boxed{
\|\delta F_R(h)\|_{H^1}
\le
C R^{-2/3}
\bigl(\mathfrak E_{2,R}^{pair}\bigr)^{1/3}.
}
\]

This is the quantitative DSD inheritance/reformation inequality.

A remote shell can fail to inherit its predecessor strongly only by paying critical-H2 derivative growth.

---

## 4. Dyadic reformation action

Take the dyadic Leray time

\[
h_0=2\log2,
\qquad
R_k=2^kR_0.
\]

Define

\[
\boxed{
d_k
:=
\left\|
F_{R_{k+1}}(\Phi_{h_0}U)-F_{R_k}(U)
\right\|_{H^1},
}
\]

and the upper reformation action

\[
\boxed{
\mathfrak A_{reform}
:=
\sum_{k=0}^{\infty}
R_k^{-2/3}
\bigl(\mathfrak E_{2,k}^{pair}\bigr)^{1/3}.
}
\]

Then

\[
\boxed{
\sum_k d_k
\le C\mathfrak A_{reform}.
}
\]

Hence

\[
\boxed{
\mathfrak A_{reform}<\infty
\Longrightarrow
\sum_k d_k<\infty.
}
\]

The co-moving shell states are then Cauchy in `H1` along the dyadic scale ladder.

This is stronger than merely assuming a uniform H2 bound.

---

## 5. Subquadratic critical-H2 growth is already enough

Suppose that for some fixed `epsilon>0`,

\[
\mathfrak E_{2,k}^{pair}
\le C R_k^{2-\varepsilon}
\]

for all sufficiently large `k`.

Then

\[
R_k^{-2/3}
(\mathfrak E_{2,k}^{pair})^{1/3}
\le C R_k^{-\varepsilon/3}.
\]

Because `R_k` is geometric,

\[
\sum_k R_k^{-\varepsilon/3}<\infty.
\]

Therefore

\[
\boxed{
\mathfrak E_2(R)=O(R^{2-\varepsilon})
\text{ for one }\varepsilon>0
\Longrightarrow
\mathfrak A_{reform}<\infty.
}
\]

Consequently the pressure-free weighted-vorticity shell charge has the same positive asymptotic limit already derived on the uniformly H2-bounded corridor.

Thus the old phrase `H2 escalation` was much too weak.  Merely having `mathfrak E_2(R)->infinity` does not block shell inheritance.

---

## 6. What is required to obstruct inheritance

If the pressure-free shell charge fails to settle by this mechanism, then necessarily

\[
\boxed{
\mathfrak A_{reform}=\infty.
}
\]

In particular, no fixed subquadratic power ceiling can hold eventually:

\[
\boxed{
\forall\varepsilon>0,
\qquad
\mathfrak E_2(R)\not=O(R^{2-\varepsilon})
}
\]

along the relevant scale sequence.

A model borderline behavior is

\[
\mathfrak E_2(R_k)
\sim
\frac{R_k^2}{k^3},
\]

for which

\[
R_k^{-2/3}\mathfrak E_2(R_k)^{1/3}
\sim
\frac1k,
\]

and the reformation action diverges even though the critical H2 quantity is slightly below `R^2` by a logarithmic factor.

The correct obstruction is therefore **nonsummable near-quadratic derivative escalation**, not generic H2 growth.

---

## 7. Physical meaning: remote microstructure becomes an absolute-scale packet

On a shell with a nontrivial H1 state, the fixed-cell derivative frequency is schematically

\[
q_R
\sim
\frac{\|F_R\|_{H^2}}{\|F_R\|_{H^1}}.
\]

If

\[
\mathfrak E_2(R)\gtrsim R^{2-o(1)},
\]

then

\[
q_R\gtrsim R^{1-o(1)}.
\]

The corresponding length scale in the original Leray coordinate is

\[
\ell_R
\sim
\frac{R}{q_R}
\lesssim
R^{o(1)},
\]

and hence

\[
\boxed{
\frac{\ell_R}{R}\to0.
}
\]

Thus the only derivative mechanism capable of indefinitely destroying scale inheritance is a genuinely remote subscale packet whose size is nearly absolute rather than proportional to its shell radius.

This is precisely the geometric content previously recorded qualitatively by the `H` hierarchy.

---

## 8. DSD persistence/reformation dichotomy

The W1 critical memory now has the exact logical form

\[
\boxed{
M_{crit}>0
\Longrightarrow
\begin{cases}
\mathfrak A_{reform}<\infty,
&\text{persistent inherited shell state},\\[1mm]
\mathfrak A_{reform}=\infty,
&\text{nonsummable structural re-formation}.
\end{cases}
}
\]

On the finite-action side,

\[
\boxed{
\mathcal S_B(\infty)>0,
\qquad
\mathcal S_\Omega(\infty)>0.
}
\]

On the infinite-action side, the survivor must create derivative substructure at a nonsummable scale-critical rate.

Therefore `coherent tail` and `H2 tail` are not independent terminal mechanisms. They are the two values of one DSD structural quantity: **reformation action**.

---

## 9. No-third-branch theorem at the present resolution

The current W1 proof management can be written as

\[
\boxed{
W1
\Longrightarrow
\left[
\mathfrak A_{reform}=\infty
\right]
\ \lor\
\left[
\mathcal S_B(\infty)>0
\ \&\
\mathcal S_\Omega(\infty)>0
\right].
}
\]

There is no remaining third branch caused merely by moderate H2 growth.

Any tail with derivative growth bounded by `R^(2-epsilon)` for even one fixed positive epsilon belongs to the persistent-current side.

---

## 10. What is still missing

This dichotomy is not yet a contradiction.

The finite-action side requires a theorem excluding simultaneous nonzero velocity and vorticity critical currents.

The infinite-action side requires a theorem showing that nonsummable near-quadratic remote derivative reformation cannot occur in an unforced finite-energy Navier--Stokes prelimit.

The DSD gain is that these are no longer unrelated cases. They are complementary outcomes of the same inheritance inequality.

A complete endpoint theorem may therefore target one common quantity that prices both persistent current and reformation action.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
