# DSD W1 Scale-Infinity Energy Capacity and Expanding-Window Gate

Date: 2026-08-26

Status: **FINITE PHYSICAL ENERGY SHOWN TO HAVE EXACTLY THE LINEAR NORMALIZED-RADIUS CAPACITY NEEDED BY A CRITICAL 1/R TAIL / EXPLICIT DIVERGENCE-FREE TRUNCATED-TAIL ANTI-MODEL SHOWS THAT LOCAL W1 CONVERGENCE + UNIFORM p>3/ENSTROPHY CONTROL CANNOT EXCLUDE THE SCALE-INFINITY ESCAPE / EXPANDING-WINDOW GATE ISOLATED / GLOBAL REGULARITY UNPROVED.**

## 1. Similarity scaling of kinetic energy

Let

\[
\lambda(t)=\sqrt{T_*-t}=e^{-s/2},
\qquad
Y=\frac{x-X_*}{\lambda},
\]

and

\[
u(x,t)=\lambda^{-1}U(Y,s).
\]

Since `dx=lambda^3 dY`,

\[
\boxed{
\|u(t)\|_2^2
=
\lambda\|U(s)\|_2^2.
}
\]

If the physical kinetic energy is bounded by `E_0`, then

\[
\boxed{
\|U(s)\|_2^2
\le
E_0e^{s/2}.
}
\]

Thus normalized L2 energy is allowed to grow like the inverse similarity length.

---

## 2. Critical cubic shell mass has a linear L2 radius tariff

Suppose on one normalized annulus

\[
A_R=\{R<|Y|<2R\}
\]

we have

\[
\int_{A_R}|U|^3dY
\ge m>0
\]

and the W1 Type-I bound

\[
\|U\|_{L^\infty(A_R)}
\le \frac A R.
\]

Pointwise,

\[
|U|^3
\le
\frac AR|U|^2.
\]

Hence

\[
\boxed{
\int_{A_R}|U|^2dY
\ge
\frac mA R.
}
\]

A nonzero critical cubic shell therefore costs at least a fixed amount of normalized kinetic energy **per unit radius**, not per logarithmic radius.

For geometrically separated occupied shells `R_k=2^kR_0`, the sum obeys

\[
\sum_{k\le N}R_k
\asymp R_N.
\]

Consequently a critical tail populated out to `R_N` has the natural normalized kinetic-energy cost

\[
\boxed{
E_{norm}^{tail}(R_N)\gtrsim R_N.
}
\]

---

## 3. Exact matching with finite physical energy

The finite-energy capacity is

\[
E_{norm}(s)\lesssim e^{s/2}.
\]

The critical-tail cost is

\[
E_{norm}^{tail}(R)\gtrsim R.
\]

Therefore finite physical energy permits the critical tail to extend to

\[
\boxed{
R_{max}(s)\asymp e^{s/2}.
}
\]

The corresponding physical radius is

\[
r_{max}(s)
=
\lambda(s)R_{max}(s)
\asymp
 e^{-s/2}e^{s/2}
\asymp1.
\]

Thus there is no scaling contradiction.

The normalized energy growth allowed by finite physical energy is **exactly** the growth needed to carry a `1/R` critical tail to a fixed physical radius.

This explains why fixed-window W1 compactness can coexist with finite physical energy even though the limiting W1 state itself is not in L2.

---

## 4. Physical shell tariff

The physical shell corresponding to normalized radius `R` has radius

\[
r=\lambda R.
\]

Its kinetic energy is

\[
\int_{A_r}|u|^2dx
=
\lambda
\int_{A_R}|U|^2dY.
\]

Using the critical shell lower bound,

\[
\boxed{
\int_{A_r}|u|^2dx
\ge
\frac mA r.
}
\]

This lower bound tends to zero linearly as `r->0`.

Hence a critical W1 tail does not force a kinetic-energy atom at the singular point.  It is compatible with local L2 energy vanishing with radius.

This closes another false route: ordinary kinetic-energy concentration alone cannot exclude the W1 endpoint.

---

## 5. Explicit divergence-free truncated critical tail

A concrete anti-model can be written without invoking Navier--Stokes dynamics.

Let

\[
T(Y)
:=
c\frac{(-Y_2,Y_1,0)}{|Y|^2}.
\]

Away from the origin,

\[
\nabla\cdot T=0,
\qquad
|T(Y)|\lesssim |Y|^{-1},
\qquad
|\nabla T(Y)|\lesssim |Y|^{-2}.
\]

Moreover `T` is homogeneous of degree `-1`, so

\[
\frac12T+
\frac12Y\cdot\nabla T=0.
\]

Choose smooth radial cutoffs `chi_in`, `chi_out` with

\[
chi_{in}=0\text{ near }0,
\qquad
chi_{in}=1\text{ for }r\ge2,
\]

and

\[
chi_{out}(r)=1\text{ for }r\le1,
\qquad
chi_{out}(r)=0\text{ for }r\ge2.
\]

For `R_n->infinity`, define

\[
\boxed{
U_n(Y)
=
chi_{in}(|Y|)
chi_{out}(|Y|/R_n)
T(Y).
}
\]

Because `T` is tangential to spheres,

\[
T\cdot\nabla chi(|Y|)=0,
\]

so radial cutoff preserves divergence-freeness:

\[
\boxed{\nabla\cdot U_n=0.}
\]

---

## 6. Norms of the anti-model

For `1<<R_n`,

\[
\|U_n\|_2^2
\asymp
\int_1^{R_n}r^{-2}r^2dr
\asymp
R_n.
\]

Thus

\[
\boxed{\|U_n\|_2^2\asymp R_n.}
\]

For every `p>3`,

\[
\|U_n\|_p^p
\lesssim
\int_1^{R_n}r^{2-p}dr
\le C_p,
\]

uniformly in `n`:

\[
\boxed{
\sup_n\|U_n\|_p<\infty
\qquad(p>3).
}
\]

At the endpoint,

\[
\|U_n\|_3^3
\asymp
\int_1^{R_n}\frac{dr}{r}
\asymp
\log R_n.
\]

Thus the critical logarithmic residue is present.

For enstrophy,

\[
\|\nabla U_n\|_2^2
\lesssim
\int_1^{R_n}r^{-4}r^2dr
+O(R_n^{-1})
\le C,
\]

so

\[
\boxed{
\sup_n\|\nabla U_n\|_2<\infty.
}
\]

Likewise the remote `D3` density is integrable because

\[
|U_n||\nabla U_n|^2dY
\sim r^{-3}dr
\]

in radial measure after including the volume factor.

Therefore the sequence reproduces simultaneously:

- local convergence to a non-L2 critical tail;
- uniform `Lp` control for every `p>3`;
- uniform ordinary enstrophy;
- logarithmically divergent L3;
- linearly growing normalized L2 energy.

It is **not** claimed to solve Navier--Stokes.  It is an anti-proof showing that these static bounds alone cannot yield the missing contradiction.

---

## 7. Match the anti-model to finite physical energy

Take blow-up times `s_n->infinity` and choose

\[
\boxed{
R_n=\kappa e^{s_n/2}.
}
\]

Then

\[
\lambda_n=e^{-s_n/2}
\]

and the physical kinetic energy represented by `U_n` scales as

\[
\lambda_n\|U_n\|_2^2
\asymp
 e^{-s_n/2}R_n
=
\kappa.
\]

Thus

\[
\boxed{
\text{finite physical energy}
+
R_n\sim e^{s_n/2}
+
\text{local convergence to a non-L2 }1/R\text{ tail}
}
\]

are perfectly scaling-compatible.

The physical outer radius of the truncated tail is

\[
\lambda_nR_n=\kappa,
\]

also fixed.

This is the exact scale-infinity escape mechanism that any proof must control dynamically rather than by static energy counting.

---

## 8. Expanding-Window Gate

The omega-limit/W1 construction gives convergence on every fixed normalized spatial window.

The anti-model shows that this leaves complete freedom for the cutoff radius `R_n` to satisfy

\[
R_n\asymp e^{s_n/2}.
\]

To transfer a W1 far-tail statement to a fixed physical radius one therefore needs new information on windows growing at the similarity rate.

A sufficient qualitative form is

\[
\boxed{
\text{critical-topology control of }U^{pre}(s_n)-U
\text{ for }R\lesssim c e^{s_n/2}.
}
\]

Call this the **Expanding-Window Gate (EWG)**.

Equivalently, one needs control over the order of limits

\[
\boxed{
\lim_{n\to\infty}\lim_{R\to\infty}
\quad\text{versus}\quad
\lim_{R\to\infty}\lim_{n\to\infty}.
}
\]

The existing all-age W1 co-moving theorem does not provide EWG because it evolves the already formed W1 limit orbit; it does not give prelimit convergence on `n`-dependent spatial windows.

---

## 9. DSD interpretation

The relevant states must be kept separate:

1. **finite prelimit:** finite physical L2 energy;
2. **fixed normalized W1 window:** compact and convergent;
3. **expanding normalized window:** radius of order `e^(s/2)` and capable of storing the escaping normalized L2 mass;
4. **W1 scale infinity:** non-L2 critical center mode.

Conflating stages 2 and 3 creates a false energy contradiction.

The exact open bridge is therefore not ordinary energy boundedness but a dynamical restriction on how stage 3 can feed stage 4.

---

## 10. Audit verdict

### Proved

- one critical cubic shell has normalized L2 cost at least `cR` under the W1 Type-I bound;
- finite physical energy permits normalized L2 capacity `O(e^(s/2))`;
- these scalings match exactly at `R=O(e^(s/2))`;
- the corresponding physical shell energy tariff is only `cr` and vanishes as `r->0`;
- an explicit divergence-free truncated `1/R` sequence realizes local non-L2 tail convergence with uniform `Lp`, `p>3`, and uniform enstrophy while normalized L2 grows linearly with the cutoff radius.

### Not proved

- EWG for an actual Navier--Stokes prelimit;
- a dynamical obstruction to `R_n~e^(s_n/2)` tail extension;
- a contradiction from the scale-infinity defect;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
