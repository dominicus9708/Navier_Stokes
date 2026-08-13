# Four-channel Gaussian residual pulse: small-state Osgood growth

Date: 2026-08-13

Status: **DERIVED SMALL-STATE MULTIPLICATIVE STRUCTURE + OSGOOD PULSE COST / DOES NOT CLOSE GLOBAL REGULARITY**.

At terminal normalization `W1=q W0`, the earlier first-hitting slice satisfies `||Omega||_infty <= 1/q`.  Hence the self-consistent Gaussian residual state starts at order `q^(-2)` when the Gaussian distortion is controlled.  A residual-dominant terminal event requires order-one accumulated residual action later in the window.

This note refines the residual-variance dynamics near the zero-residual state.  The main point is that, except for pressure-Hessian forcing, the residual state is generated multiplicatively rather than by an order-one additive source.

---

## 1. Initial residual size at the earlier checkpoint

Normalize by the terminal first-hitting value

\[
W_1=qW_0.
\]

At the earlier checkpoint,

\[
\boxed{\|\Omega(s_0)\|_\infty\le q^{-1}.}
\]

Therefore

\[
\operatorname{Var}_\gamma(\Omega(s_0))\le q^{-2}.
\]

Since strain is a zero-order Calderon--Zygmund transform of vorticity,

\[
\|S(s_0)\|_{BMO}\lesssim q^{-1}.
\]

For a Gaussian with bounded condition number, John--Nirenberg then gives

\[
\operatorname{Var}_\gamma(S(s_0))\lesssim_K q^{-2}.
\]

Hence

\[
\boxed{\mathcal B_\gamma(s_0)\lesssim_K q^{-2}.}
\]

---

## 2. Vorticity variance is multiplicatively generated

Let

\[
\delta\Omega=\Omega-\bar\Omega_\gamma,
\qquad
V_\omega=\int\gamma|\delta\Omega|^2.
\]

The exact identity is

\[
V_\omega'
=-2\nu D_\omega
+2\int\gamma\delta\Omega\cdot L\delta\Omega
+2\int\gamma\delta\Omega\cdot f_r.
\]

For the residual stretching part, write

\[
\Omega=\bar\Omega_\gamma+\delta\Omega.
\]

Using `||Omega||_infty<=1` and

\[
\int\gamma|\nabla r|^2=\mathcal B_\gamma,
\]

Cauchy--Schwarz gives

\[
\left|
\int\gamma\delta\Omega\cdot(\Omega\cdot\nabla)r
\right|
\le C\sqrt{V_\omega\mathcal B_\gamma}
\le C\mathcal B_\gamma.
\]

For residual transport, `div r=0` gives

\[
-2\int\gamma\delta\Omega\cdot(r\cdot\nabla)\Omega
=
\int\gamma|\delta\Omega|^2r\cdot\nabla\log\gamma.
\]

Because `|delta Omega|<=2`,

\[
\||\delta\Omega|^2\|_{L^2(\gamma)}
\le2V_\omega^{1/2},
\]

while the Gaussian drift estimate gives

\[
\|r\cdot\nabla\log\gamma\|_{L^2(\gamma)}
\le C_K\mathcal B_\gamma^{1/2}.
\]

Thus

\[
\boxed{
V_\omega'+2\nu D_\omega
\le
C_K(1+|\operatorname{sym}L|)\mathcal B_\gamma.
}
\]

In particular, the vorticity residual variance has no independent order-one additive source at `B_gamma=0`.

---

## 3. BMO plus small variance gives logarithmic higher-moment control

Let `X` be a mean-zero scalar or finite-dimensional Gaussian-weighted field component with

\[
\|X\|_{BMO(\gamma)}\le C_K
\]

and

\[
\int\gamma|X|^2=V\ll1.
\]

Combining Chebyshev

\[
\gamma(|X|>t)\le V/t^2
\]

with the John--Nirenberg exponential tail and splitting where the two tails intersect yields

\[
\boxed{
\int\gamma|X|^3
\le
C_KV\left[1+\log\frac{C_K}{V}\right].
}
\]

Likewise,

\[
\boxed{
\left(\int\gamma|X|^4\right)^{1/2}
\le
C_KV^{1/2}\left[1+\log\frac{C_K}{V}\right].
}
\]

These estimates are qualitative small-variance improvements; no sharp constants are claimed.

---

## 4. Strain-variance small-state structure

Let

\[
\delta S=S-\bar S,
\qquad
V_S=\int\gamma|\delta S|^2.
\]

The exact strain-variance equation contains

- residual transport,
- `delta S : S^2`,
- `delta S : A^2`,
- pressure-Hessian fluctuation.

The constant `bar S^2` contribution vanishes because `int gamma delta S=0`.

The terms linear in `bar S` are bounded by

\[
C|\bar S|V_S.
\]

The mean-free cubic term satisfies the BMO-small-variance estimate

\[
\left|\int\gamma\delta S:(\delta S)^2\right|
\le
C_KV_S
\left[1+\log\frac{C_K}{V_S}\right].
\]

The `A^2` fluctuation is controlled by the vorticity variance and therefore by `B_gamma`; residual transport is controlled by the residual-gradient variance together with the logarithmic `L4` estimate above.

The pressure fluctuation remains

\[
2\sqrt{V_S}\,\Pi_P.
\]

Thus, after dropping favorable viscous terms, the total four-channel state satisfies schematically for small `B_gamma`

\[
\boxed{
\mathcal B_\gamma'
\le
C_K(1+|\operatorname{sym}L|)
\mathcal B_\gamma
\left[1+\log\frac{C_K}{\mathcal B_\gamma}\right]
+C_K\sqrt{\mathcal B_\gamma}\,\Pi_P.
}
\]

This is the small-state Osgood growth inequality.

---

## 5. Pressure-small pulse cost

If the pressure-Hessian fluctuation term is negligible on the pulse-generation interval, write

\[
B=\mathcal B_\gamma,
\qquad
A(s)=C_K(1+|\operatorname{sym}L(s)|).
\]

Then

\[
B'\le A(s)B\left[1+\log(C_K/B)\right].
\]

An Osgood integration shows that taking

\[
B(s_0)\lesssim q^{-2}
\]

to a fixed `B(s1)>=b_*>0` requires

\[
\boxed{
\int_{s_0}^{s_1}A(s)ds
\ge
c\log\log q-C_{K,b_*}
}
\]

for large `q`.

Thus an adaptive large-q residual pulse cannot be generated solely by a uniformly bounded amount of multiplicative non-affine/affine action.

---

## 6. Pressure-forced alternative

If the Osgood action is below the required size, the pressure term must contribute substantially.  In terms of `z=sqrt(B)`, the pressure forcing is additive:

\[
z'\lesssim
A(s)z[1+\log(C/z)]
+C_K\Pi_P.
\]

Therefore rapid generation of an order-one residual state with insufficient multiplicative action forces an order-one pressure-Hessian impulse in the corresponding weighted norm.

Schematically,

\[
\boxed{
q^{-2}\to O(1)
\Longrightarrow
\text{Osgood affine/non-affine action }\gtrsim\log\log q
\quad\text{or}\quad
\text{pressure-Hessian impulse}.
}
\]

---

## 7. Scaling audit: this is not yet a global contradiction

An order-one normalized gradient/strain action on a terminal natural window corresponds physically to a cost of order

\[
W^{-1/2}.
\]

For fixed geometric first-hitting factors, these physical costs are summable over `W_j`.

Even a `log log q` normalized pulse cost does not automatically defeat that critical summability after converting back to physical variables.

Therefore the present result is a **strict typing/growth result**, not a proof of global regularity.

A proof-producing use would need either

1. a pulse cost growing sufficiently fast with an adaptive `q`,
2. a scale-invariant packing quantity not multiplied by `W^{-1/2}`, or
3. a compactness/Liouville argument that treats repeated pulse generation as a rigidity obstruction rather than an energy sum.

---

## 8. DSD interpretation

At the previous checkpoint the four unresolved channels are all small:

\[
\mathcal B_\gamma=O(q^{-2}).
\]

A residual-dominant amplification must create a finite unresolved structural state and then the terminal Gaussian coercivity forces it back toward zero.

Thus the residual branch is a genuine **structural pulse**:

\[
\boxed{q^{-2}\ \longrightarrow\ O(1)\ \longrightarrow\ 0.}
\]

Its generation is not free: away from pressure forcing it obeys an Osgood multiplicative law.

Status: **FOUR-CHANNEL PULSE GENERATED MULTIPLICATIVELY / LOG-LOG-Q COST DERIVED CONDITIONALLY / GLOBAL PACKING STILL OPEN**.
