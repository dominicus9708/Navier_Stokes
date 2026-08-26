# DSD W1 Interior--Boundary Decoupling and Uniform No-Defect Target

Date: 2026-08-26

Status: **STRATEGIC AUDIT: THE CONSERVED CRITICAL DEFECT IS SEPARATED FROM RECURRENT INTERIOR FORMATION DYNAMICS / THE PRIMARY CLOSURE TARGET IS RECAST AS UNIFORM LOW-AMPLITUDE WEAK-L3 TIGHTNESS OF THE PRELIMIT / CORE NONREPEATABILITY IS DEMOTED TO A SECONDARY ROUTE / GLOBAL REGULARITY UNPROVED.**

## 1. Why the proof strategy changes

The current W1 analysis has established that

\[
\mathscr R_3(s)=\mathscr R_{3,*}>0
\]

is a first integral on the recurrent endpoint orbit.

Equivalently, the low-amplitude weak-L3 defect coefficient

\[
\mathscr C_{WL3}=\frac{\mathscr R_{3,*}}{3}
\]

is time-independent on W1.

Therefore it is inaccurate to describe the recurrent finite-core pressure/stretching cycle as repeatedly creating the defect charge.

The orbit moves **inside one fixed positive-defect sector**.

---

## 2. DSD separation of state interior and state boundary

The state description now has two distinct layers.

### Interior layer

This contains finite-parent quantities such as

- amplitude BMO oscillation;
- `D3` amplitude/direction cost;
- pressure-gradient work;
- vorticity stretching;
- pressure--stretch locking/relative-vorticity compensation.

These determine motion inside the recurrent state sector.

### Boundary layer

This contains

\[
\boxed{
K(0+)=\frac{\mathscr R_{3,*}}{3}>0,
}
\]

or equivalently the nonzero low-amplitude weak-L3 defect at the normalized state boundary `|U|=0` / spatial infinity.

This boundary charge is conserved by the W1 orbit.

Thus

\[
\boxed{
\text{interior recurrence}
\neq
\text{creation of the boundary defect}.
}
\]

---

## 3. Every fixed prelimit state has zero boundary defect

For every finite Leray time `s`, the actual prelimit state comes from a finite-energy physical solution, hence

\[
U(s)\in L^2.
\]

Therefore

\[
\boxed{
\lim_{\lambda\downarrow0}
\lambda^3
|\{|U(s)|>\lambda\}|
=0.
}
\]

Equivalently,

\[
\boxed{
K_s(0+)=0.
}
\]

The W1 omega-limit survivor instead has

\[
\boxed{
K_\infty(0+)=\mathscr R_{3,*}/3>0.
}
\]

So the entire endpoint obstruction is a nonuniformity of the low-amplitude tail under the noncompact Leray limit.

---

## 4. Exact uniform no-defect condition

Define

\[
\mathcal C(s,\lambda)
:=
\lambda^3
|\{Y:|U(Y,s)|>\lambda\}|.
\]

For each fixed `s`,

\[
\mathcal C(s,\lambda)\to0
\quad(\lambda\downarrow0).
\]

A sufficient no-defect theorem is the uniform version

\[
\boxed{
\lim_{\lambda\downarrow0}
\sup_{s\ge s_0}
\mathcal C(s,\lambda)
=0.
}
\]

If this holds on the late prelimit corridor, then every `Lp`, `p>3`, omega-limit has zero weak-L3 boundary defect and hence

\[
\boxed{
\mathscr R_3=0.
}
\]

This directly contradicts W1.

---

## 5. Physical-variable form

Let

\[
\tau=T_*-t=e^{-s}
\]

and let `L` be a physical velocity threshold. The corresponding Leray threshold is

\[
\lambda=L\sqrt\tau.
\]

The distribution functions satisfy

\[
\boxed{
\lambda^3N_U(\lambda,s)
=L^3N_u(L,t).
}
\]

Therefore the uniform no-defect condition is equivalent to

\[
\boxed{
\lim_{\delta\downarrow0}
\sup_{t\uparrow T_*}
\sup_{L\sqrt{T_*-t}\le\delta}
L^3
|\{x:|u(x,t)|>L\}|
=0.
}
\]

This is a fully physical formulation.

It says that velocity levels lying strictly below the Type-I amplitude scale

\[
L\sim (T_*-t)^{-1/2}
\]

must not carry an order-one weak-L3 volume coefficient uniformly up to the candidate singular time.

---

## 6. Why ordinary finite energy is insufficient

Chebyshev gives

\[
L^3|\{|u|>L\}|
\le
L\|u\|_2^2.
\]

This is useful only for `L downarrow 0` at fixed physical time/scale.

In the no-defect regime above, `L` may grow as `t upward T_*` while still satisfying

\[
L\sqrt{T_*-t}\to0.
\]

Then the energy bound does not force the coefficient to zero.

Thus the target is genuinely stronger than finite physical energy.

---

## 7. Augmented compactness formulation

For one fixed `p>3`, the established W1 compactness uses the `Lp` topology. That topology does not see the defect: a sequence may converge strongly in `Lp` while an `A/r` tail translates to spatial infinity and leaves a nonzero weak-L3 boundary coefficient.

Define an augmented defect-aware topology schematically by

\[
\boxed{
 d_*(U,V)
 :=
 \|U-V\|_{L^p}
 +
 |\mathscr C_{WL3}(U)-\mathscr C_{WL3}(V)|.
}
\]

Every prelimit state has defect coordinate zero. A positive-defect W1 limit therefore cannot arise if the late orbit is precompact in any topology strong enough to control this second coordinate.

Thus another equivalent proof target is:

\[
\boxed{
\text{prove late precompactness in a defect-aware critical topology.}
}
\]

---

## 8. Consequence for the core-cycle program

The previously constructed complete pressure/amplitude/vorticity formation cycles remain valid structural certificates of a positive-defect W1 survivor.

However, they are no longer the shortest logical route to contradiction.

The primary route is now

\[
\boxed{
\text{finite-energy prelimit}
\Longrightarrow
\text{uniform no-defect compactness}
\Longrightarrow
\mathscr R_3=0.
}
\]

The core-cycle nonrepeatability route remains a secondary alternative if it can independently force strong-critical regularity.

---

## 9. Single remaining endpoint theorem

At the present resolution, a complete W1 closure would follow from the single theorem

\[
\boxed{
\lim_{\lambda\downarrow0}
\sup_{s\ge s_0}
\lambda^3
|\{|U(s)|>\lambda\}|
=0.
}
\]

under the already established W1 prelimit assumptions inherited from an unforced finite-energy smooth Navier--Stokes solution.

No proof of this uniform critical tightness theorem is presently available in the repository.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
