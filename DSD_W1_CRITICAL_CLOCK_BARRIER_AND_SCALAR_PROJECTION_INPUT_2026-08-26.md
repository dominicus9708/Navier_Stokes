# DSD W1 Critical-Clock Barrier and Scalar Projection Input

Date: 2026-08-26

Status: **PROJECTION CASCADE REDUCED TO THE SCALAR STREAMLINE-AMPLITUDE INPUT / ENERGY-LEVEL GLOBAL BUDGETS SHOWN TOO SUBCRITICAL IN TIME TO EXCLUDE RECURRENT W1 / GLOBAL REGULARITY UNPROVED.**

## 1. Projection commutator has one scalar input

Let

\[
\mathbb P
\]

be the Leray projector and

\[
\mathbb Q=I-\mathbb P.
\]

For divergence-free `U` and a scalar multiplier `m`,

\[
[\mathbb P,m]U
=
\mathbb P(mU)-mU
=
-\mathbb Q(mU).
\]

Since

\[
\nabla\cdot(mU)=U\cdot\nabla m,
\]

we obtain

\[
\boxed{
[\mathbb P,m]U
=
-\nabla\Delta^{-1}(U\cdot\nabla m).
}
\]

Thus the Hodge commutator is driven by one scalar channel.

For the large-scale critical multiplier `m=|U|`, the input is

\[
\boxed{
e:=U\cdot\nabla|U|.
}
\]

The nonlocal projection does not constitute an independent branch; it converts this scalar amplitude transport into a gradient/solenoidal split.

---

## 2. Relation to the direction field

Write

\[
U=a n,
\qquad
a=|U|,
\qquad
|n|=1.
\]

Incompressibility gives

\[
0=\nabla\cdot(an)
=n\cdot\nabla a+a\nabla\cdot n.
\]

Hence

\[
\boxed{
e
=U\cdot\nabla a
=-a^2\nabla\cdot n.
}
\]

Therefore the scalar projection input is exactly velocity-direction compression weighted by amplitude squared.

---

## 3. The physical Lamb vector has a finite energy-level spacetime budget

Let

\[
L_{phys}=\omega\times u.
\]

At each regular time,

\[
\|L_{phys}\|_{L^1}
\le
\|u\|_2\|\omega\|_2.
\]

Consequently

\[
\boxed{
\int_0^{T_*}
\|L_{phys}(t)\|_1^2dt
\le
\sup_{t<T_*}\|u(t)\|_2^2
\int_0^{T_*}\|\omega(t)\|_2^2dt
<\infty.
}
\]

This is a genuine finite-parent bound.

---

## 4. Why that bound does not exclude W1 recurrence

Under the backward Leray scaling

\[
u(x,t)=\tau^{-1/2}U(Y,s),
\qquad
\omega(x,t)=\tau^{-1}\Omega(Y,s),
\]

with

\[
\tau=T_*-t=e^{-s},
\qquad
dt=\tau ds,
\]

the Lamb vector scales as

\[
L_{phys}(x,t)
=\tau^{-3/2}L(Y,s).
\]

Since `dx=tau^(3/2)dY`,

\[
\boxed{
\|L_{phys}(t)\|_{L^1_x}
=
\|L(s)\|_{L^1_Y}.
}
\]

Therefore the finite physical budget becomes

\[
\boxed{
\int^{\infty}
e^{-s}\|L(s)\|_1^2ds<\infty.
}
\]

A recurrent W1 orbit with

\[
\|L(s)\|_1\sim O(1)
\]

is fully compatible with this bound because

\[
\int^{\infty}e^{-s}ds<\infty.
\]

Thus the global kinetic-energy/enstrophy budget is too subcritical in the Leray clock to forbid recurrent normalized Lamb activity.

---

## 5. Critical-clock formulation

The singularity endpoint lives on the logarithmic clock

\[
\boxed{
ds=\frac{dt}{T_*-t}.
}
\]

A fixed positive recurrent action in `s` produces a contradiction only if one has an a priori physical estimate at the corresponding scale-critical time weight.

Examples already encountered:

- kinetic-energy or ordinary enstrophy budgets acquire decaying weights in `s` and are summable;
- fixed normalized turnover energy costs acquire the same half-power/geometric summability;
- `D3_phys dt`, critical `L_t^2L_x^(3/2)` streamline-amplitude work, and the endpoint Gaussian currents are unweighted in `ds` and therefore detect the W1 obstruction.

Hence the correct barrier is

\[
\boxed{
\text{SUBCRITICAL PHYSICAL BUDGET}
\not\Rightarrow
\text{NO RECURRENT W1}.
}
\]

A closure theorem must control a genuinely scale-critical quantity or use information that breaks self-similar scaling.

---

## 6. DSD interpretation

The current structural chain is

\[
\boxed{
\text{amplitude/direction deformation}
\to
e=U\cdot\nabla|U|
\to
\text{Hodge projection conversion}
\to
\text{critical Bernoulli/Lamb current}.
}
\]

The projection step is a transformation of the scalar input, not an independent source.

The remaining difficulty is therefore not to bound the raw Lamb force by the finite energy budget. That route is subcritical in time.

The remaining target is a **critical-clock incompatibility** for the scalar amplitude transport / solenoidal cascade, or a global parent-interface theorem that introduces a nonshrinking scale.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
