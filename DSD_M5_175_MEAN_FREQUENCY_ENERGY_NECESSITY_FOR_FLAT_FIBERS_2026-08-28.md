# DSD M5-175 — Mean-Frequency Energy Necessity for Flat Fibers

Date: 2026-08-28

Status: **P1_B^S FLATNESS NECESSITY REFINEMENT / THE HEURISTIC REPRESENTATIVE-FREQUENCY STATEMENT OF M5-154 IS REPLACED BY A DIRECT INVARIANT-HILBERT ENERGY INEQUALITY / ANY NONZERO SUPERALGEBRAICALLY FLAT STATISTICAL SAME-TAIL FIBER MUST SATISFY `integral z N(tau) dtau = infinity`, WHERE `N` IS THE ACTUAL CROSS-SECTION DIRICHLET MEAN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Energy and frequency

Use the stable same-tail relative-vorticity field `F` and define

\[
E(\tau):=\|F(\tau)\|^2,
\qquad
N(\tau):=\frac{\langle AF,F\rangle}{E},
\]

with

\[
A=1-4G^2-\Delta_{S^2}\ge1.
\]

A flat fiber satisfies

\[
E(\tau)=O(e^{-M\tau})
\quad\forall M<\infty,
\]

and in particular

\[
E(\tau)\to0.
\]

---

## 2. Global upper bound for the exact frozen damping

Use the M5-173 notation

\[
\sqrt D=u+iv,
\qquad
\Gamma_z=\frac{u-1}{8\nu z},
\qquad
z=e^{-\tau}.
\]

Let

\[
S:=4\omega^2+\ell(\ell+1),
\qquad b:=\nu z.
\]

As in M5-174,

\[
d=1+12b+4b^2+16b^2\ell(\ell+1),
\]

and

\[
y^2=64b^2\bigl(S-\ell(\ell+1)\bigr).
\]

Since

\[
u^2=\frac{\sqrt{d^2+y^2}+d}{2},
\]

we have

\[
u-1=\frac{u^2-1}{u+1}.
\]

Moreover

\[
\sqrt{d^2+y^2}+d-2
=
\frac{y^2+4d-4}
{\sqrt{d^2+y^2}+2-d}
\le
\frac{y^2+4d-4}{2},
\]

because `sqrt(d^2+y^2)>=d` and hence the denominator is at least `2`.

A direct substitution gives

\[
y^2+4d-4
=48b+16b^2+64b^2S.
\]

Therefore

\[
\boxed{
\Gamma_z
\le
\frac34+C_\nu z(1+S)
\le
\frac34+C_\nu zA.
}
\]

No support restriction is used.

---

## 3. Frozen principal energy rate

M5-173 gives the frozen stable real growth rate

\[
\operatorname{Re}\lambda_s
=\frac34-\Gamma_z.
\]

Therefore Section 2 implies

\[
\boxed{
\operatorname{Re}\lambda_s
\ge
-CzA.
}
\]

After averaging over the normalized spectral measure,

\[
\boxed{
\frac{1}{2}\frac{E_\tau}{E}
\ge
-CzN
}
\]

for the frozen principal channel.

---

## 4. Nonautonomous stable-root correction

M5-173 gives

\[
|e_z|\le Cz(1+\Gamma_z).
\]

By Section 2,

\[
\int\Gamma_z\,d\mu_F
\le
\frac34+CzN.
\]

Hence the averaged tracking correction satisfies

\[
\boxed{
\left|\int e_zd\mu_F\right|
\le
Cz(1+zN)
\le
Cz(1+N)
}
\]

for `0<z<=1`.

---

## 5. Variable relative coupling in the energy channel

The forward-`tau` relative transport/stretching/Biot--Savart channel carries the normal coefficient `z`.

Its transport part is divergence-free at top order and is energy-skew after integration by parts.  The stretching, coefficient-divergence, and Biot--Savart lower-order pieces are uniformly bounded on the compact W1 background class.

Thus

\[
\boxed{
\left|
\frac{2z}{E}\operatorname{Re}\langle B_zF,F\rangle
\right|
\le Cz.
}
\]

Combining with Sections 3--4 gives the global lower energy inequality

\[
\boxed{
\frac d{d\tau}\log E(\tau)
\ge
-Cz\bigl(1+N(\tau)\bigr).
}
\]

---

## 6. Necessary mean-frequency divergence

Assume

\[
\int_{\tau_0}^{\infty}z(\tau)N(\tau)d\tau<\infty.
\]

Since

\[
\int_{\tau_0}^{\infty}z(\tau)d\tau<\infty,
\]

Section 5 gives

\[
\log E(\tau)
\ge
\log E(\tau_0)-C<\infty
\]

for all future `tau`.

Therefore a nonzero state at `tau_0` cannot satisfy `E(tau)->0`.

Consequently every nonzero flat fiber must obey

\[
\boxed{
\int^{\infty}z(\tau)N(\tau)d\tau=\infty.
}
\]

This is the rigorous mean-frequency replacement for the representative scale `Omega(tau)` used heuristically in M5-154.

---

## 7. DSD audit

### Formation — GREEN

Only the actual invariant-pair energy and Dirichlet mean are used.

### Axis — GREEN

Normal depth `z` and cross-section frequency `A` remain separate.

### Static aggregation — GREEN

No representative frequency or support bound is inferred from the mean.

### Dynamics — GREEN

The conclusion is a necessary condition for flat decay, not an assumed cascade model.

### Cross-audit — GREEN

This note strengthens M5-154 and is compatible with M5-174.

---

## 8. Next use

Combine M5-175 with the M5-174 corridor inequality.  If `zN` remains bounded along arbitrarily deep ages, the corridor dynamics forces bounded `N`, contradicting Section 6.  Therefore any surviving flat fiber must in fact be **eventually super-parabolic in the mean**, a strictly stronger escape statement than M5-154.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
