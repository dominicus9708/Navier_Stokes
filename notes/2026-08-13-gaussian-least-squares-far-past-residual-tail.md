# Gaussian least-squares affine regression and far-past residual tail — scaling-audited version

Date: 2026-08-13

Status: **EXACT GAUSSIAN REGRESSION IDENTITY + PHYSICAL-TIME INTEGRABLE TAIL / FIXED NORMALIZED-HORIZON CLAIM RETRACTED**.

This note records both the valid Gaussian least-squares tail estimate and an important scaling correction.

The self-consistent Gaussian affine representative is exactly the Gaussian least-squares affine regression of the velocity.  This gives a `tau^(-5/4)` residual-source tail in physical variables.  However finite physical kinetic energy scales like `W^(1/4)` in the terminal first-hitting normalization.  Therefore the tail cannot be cut off at a backward horizon that is uniform in normalized time along a blow-up sequence.

The earlier stronger statement claiming confinement to a fixed normalized-time annulus is retracted.

---

## 1. Gaussian least-squares affine representative

Let `gamma=N(0,Sigma)` in coordinates `y=x-a(s)` and define

\[
a'(s)=\int\gamma_s u(a+y,s)dy,
\qquad
L(s)=\int\gamma_s\nabla u(a+y,s)dy.
\]

Set

\[
r(y,s)=u(a+y,s)-a'(s)-L(s)y.
\]

Gaussian integration by parts gives the Stein identity

\[
\boxed{
\int\gamma\,[u-a']y^T
=\left(\int\gamma\nabla u\right)\Sigma.
}
\]

Hence

\[
\boxed{
L=\left[\int\gamma(u-a')y^T\right]\Sigma^{-1}.
}
\]

This is exactly the normal equation for the Gaussian least-squares problem

\[
\min_{b,M}\int\gamma|u-b-My|^2dy.
\]

Therefore

\[
\boxed{
(a',L)=\arg\min_{b,M}\int\gamma|u-b-My|^2dy
}
\]

and

\[
\boxed{
\int\gamma|r|^2dy
\le\int\gamma|u|^2dy
\le\|\gamma\|_\infty\|u(s)\|_2^2.
}
\]

Using kinetic-energy dissipation,

\[
\boxed{
\|r\|_{L^2(\gamma)}
\le\|\gamma\|_\infty^{1/2}\|u_0\|_2.
}
\]

---

## 2. Physical residual-source tail

The residual source is

\[
f_r=\nabla\cdot(r\otimes\omega-\omega\otimes r).
\]

If the physical first-hitting terminal amplitude is `W`, then on the preceding interval

\[
\|\omega(s)\|_\infty\le W.
\]

Integration by parts gives

\[
\left|\int\gamma f_r\right|
\le
C W\|r\|_{L^2(\gamma)}
\left(\operatorname{tr}\Sigma^{-1}\right)^{1/2}.
\]

Assume bounded affine distortion `K` so that, with physical backward time `tau=T-s`,

\[
2\nu e^{-2K}\tau I
\preceq\Sigma(s)
\preceq2\nu e^{2K}\tau I.
\]

Then

\[
\|\gamma\|_\infty^{1/2}
\lesssim_K(\nu\tau)^{-3/4},
\qquad
(\operatorname{tr}\Sigma^{-1})^{1/2}
\lesssim_K(\nu\tau)^{-1/2}.
\]

Thus

\[
\boxed{
\left|\int\gamma_sf_r\right|
\lesssim_K
W\|u_0\|_2\nu^{-5/4}\tau^{-5/4}.
}
\]

After division by the terminal vorticity scale `W`, the normalized endpoint contribution from physical times with `T-s>=R_phys` obeys

\[
\boxed{
\mathfrak R_{\rm tail}^{\rm norm}
\lesssim_K
\|u_0\|_2\nu^{-5/4}R_{\rm phys}^{-1/4}.
}
\]

Therefore the tail is genuinely integrable in **physical backward time**.

---

## 3. Scaling audit

Use terminal first-hitting Navier--Stokes scaling

\[
r=W^{-1/2},
\qquad
U=ru,
\qquad
\Omega=r^2\omega,
\qquad
s=W(t-T).
\]

Then

\[
\boxed{
\|U\|_2
=W^{1/4}\|u\|_2.
}
\]

If `R_norm=W R_phys`, the previous physical tail estimate becomes

\[
\boxed{
\mathfrak R_{\rm tail}^{\rm norm}
\lesssim_K
W^{1/4}\|u_0\|_2\nu^{-5/4}R_{\rm norm}^{-1/4}.
}
\]

Consequently a fixed normalized cutoff `R_norm` is **not** uniform along a sequence `W->infinity`.

To make the tail below a fixed epsilon using kinetic energy alone may require

\[
R_{\rm norm}\gtrsim W
\]

up to constants, corresponding to a fixed physical backward horizon rather than a fixed normalized one.

---

## 4. Correct conclusion

The valid statement is

\[
\boxed{
\text{finite kinetic energy prunes sufficiently remote physical history}
}
\]

but not

\[
\boxed{
\text{finite kinetic energy prunes the ancient tail at a fixed normalized time}.
}
\]

Thus the first-hitting blow-up normalization can still turn a finite physical-time reservoir into an increasingly long normalized ancient interval.

This phenomenon must remain an explicit channel in any compactness argument.

---

## 5. Relation to terminal collapse

The companion Gaussian residual-variance lemma still gives, under bounded affine distortion and weighted pressure-Hessian budget,

\[
\mathfrak R_{\gamma,\,0<T-s<\delta/W}^{\rm norm}
\lesssim_{K,C_P}\delta^{3/2}
\]

when written with a fixed **normalized** terminal thickness `delta`.

Hence terminal-time concentration can be pruned uniformly, but the far-past side cannot yet be cut at a fixed normalized horizon using kinetic energy alone.

---

## 6. Revised active frontier

The residual route now separates into

1. **terminal normalized layer:** collapses under bounded affine/pressure channels;
2. **intermediate/ancient normalized history:** may extend to order `W` in normalized time even though it corresponds to only order-one physical time;
3. **truly remote physical history:** integrably suppressed by finite kinetic energy.

The next proof-producing question is therefore whether the long normalized ancient reservoir can repeatedly transmit an order-one residual endpoint signal while the physical kinetic-energy dissipation budget, first-hitting amplitude cap, and affine/pressure channels remain bounded.

Status: **SCALING-AUDITED PHYSICAL TAIL CLOSED / UNIFORM NORMALIZED ANCIENT-TAIL CLOSURE OPEN**.
