# DSD M5-486 — Similarity-enstrophy balance forces a second recurrent stretching channel on the marked dilation hull

Date: 2026-09-01

Status: **SIMILARITY-DYNAMICS SHARPENING / THE M5-485 MARKED DILATION HULL CAN BE WRITTEN AS A COMPACT BACKWARD-SIMILARITY FLOW; IN THESE VARIABLES THE NORMALIZED VORTICITY ENSTROPHY SATISFIES `1/2 E' + 1/4 E + P = Q`, WHERE `P` IS NORMALIZED PALINSTROPHY AND `Q` IS AXIAL VORTEX-STRETCHING PRODUCTION / EVERY NONZERO PERIODIC DSS COMPONENT, AND MORE GENERALLY EVERY INVARIANT SUSPENSION COMPONENT OF THE APERIODIC MARKED HULL, MUST THEREFORE HAVE STRICTLY POSITIVE MEAN AXIAL STRETCHING SUFFICIENT TO PAY BOTH SELF-SIMILAR DAMPING AND VISCOUS DISSIPATION / THIS AXIAL CHANNEL IS ALGEBRAICALLY INDEPENDENT OF THE PROJECTIVE RATCHET-TILT CHANNEL, SO THE SURVIVING HARD CORE MUST SUSTAIN TWO RECURRENT CRITICAL CHANNELS SIMULTANEOUSLY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-483--485

On the compact/no-defect lane we now have a complete ancient dilation genealogy

\[
\mathcal U_{n+1}
=
\mathscr D_{\lambda_n}\mathcal U_n,
\qquad
1<\lambda_-\le\lambda_n\le\lambda_+<\infty,
\]

with

\[
\|\mathcal\Omega_n(s)\|_\infty\le C|s|^{-1},
\]

\[
\|\mathcal\Omega_n(s)\|_2^2\le C|s|^{-1/2},
\]

and the M5-484 truncated palinstrophy bound.

M5-485 further gives a compact marked shift hull with an invariant probability measure carrying positive mean ratchet frequency.

The next question is what ordinary Navier--Stokes balance every recurrent dilation component must satisfy.

---

## 2. Backward similarity variables

For one ancient hull member `(mathcal U,mathcal P)` on `s<0`, set

\[
a:=-s>0,
\qquad
\theta:=-\log a,
\qquad
y:=\frac{x}{\sqrt a}.
\]

Define the similarity velocity, pressure, and vorticity

\[
\boxed{
U(y,\theta)
:=
\sqrt a\,\mathcal U(\sqrt a\,y,-a),
}
\]

\[
\boxed{
\Pi(y,\theta)
:=
a\,\mathcal P(\sqrt a\,y,-a),
}
\]

and

\[
\boxed{
W(y,\theta)
:=
\nabla_y\times U
=
a\,\mathcal\Omega(\sqrt a\,y,-a).
}
\]

The M5-483 Type-I bounds become uniform similarity bounds.

In particular

\[
\|W(\theta)\|_\infty\le C,
\]

and

\[
\|W(\theta)\|_2^2
=
a^{1/2}\|\mathcal\Omega(-a)\|_2^2
\le C.
\]

---

## 3. Similarity Navier--Stokes equation

Direct differentiation gives

\[
\boxed{
\partial_\theta U
+
\frac12U
+
\frac12(y\cdot\nabla)U
+
U\cdot\nabla U
=
-\nabla\Pi+\Delta U,
}
\]

with

\[
\nabla\cdot U=0.
\]

Taking curl gives

\[
\boxed{
\partial_\theta W
+W
+\frac12(y\cdot\nabla)W
+U\cdot\nabla W
=
(W\cdot\nabla)U
+
\Delta W.
}
\]

Write the similarity strain

\[
\Sigma:=\frac12(\nabla U+\nabla U^T).
\]

---

## 4. Exact similarity-enstrophy balance

Define

\[
E(\theta):=\|W(\theta)\|_2^2,
\]

\[
P(\theta):=\|\nabla W(\theta)\|_2^2,
\]

and

\[
Q(\theta)
:=
\int_{\mathbb R^3}
W\cdot\Sigma W\,dy.
\]

Take the `L2` inner product of the similarity-vorticity equation with `W`.

The transport term vanishes:

\[
\int W\cdot(U\cdot\nabla W)dy=0.
\]

The dilation transport gives

\[
\frac12\int W\cdot(y\cdot\nabla W)dy
=
-\frac34E.
\]

Together with the explicit `+W` term, the net linear contribution is

\[
E-\frac34E=\frac14E.
\]

Therefore

\[
\boxed{
\frac12\frac{dE}{d\theta}
+
\frac14E
+
P
=
Q.
}
\]

This is the key M5-486 identity.

---

## 5. Relation to the physical M5-484 palinstrophy ledger

The similarity quantities obey

\[
E(\theta)
=
a^{1/2}
\|\mathcal\Omega(-a)\|_2^2,
\]

and

\[
P(\theta)
=
a^{3/2}
\|\nabla\mathcal\Omega(-a)\|_2^2.
\]

Thus the similarity palinstrophy is the natural scale-normalized version of the M5-484 critical tail.

The estimate

\[
\int_{-\infty}^{-\varepsilon}
\|\nabla\mathcal\Omega(s)\|_2^2ds
\le C\varepsilon^{-1/2}
\]

is exactly compatible with bounded average `P` over logarithmic similarity-time intervals.

No contradiction is obtained from this scaling alone.

---

## 6. Exact DSS becomes periodic similarity dynamics

If an ancient hull member is backward `Lambda`-DSS,

\[
\mathcal U(x,s)
=
\Lambda
\mathcal U(\Lambda x,\Lambda^2s),
\]

then its similarity representative satisfies

\[
\boxed{
U(y,\theta+\Theta)=U(y,\theta),
\qquad
\Theta=2\log\Lambda.
}
\]

The same holds for `W,E,P,Q`.

Integrating the similarity-enstrophy identity over one period yields

\[
\boxed{
\frac14
\int_0^\Theta E\,d\theta
+
\int_0^\Theta P\,d\theta
=
\int_0^\Theta Q\,d\theta.
}
\]

For a nonzero DSS solution, `E` is not identically zero. Hence

\[
\boxed{
\int_0^\Theta Q\,d\theta>0.
}
\]

Therefore every nonzero finite-enstrophy periodic DSS component must have strictly positive mean axial vortex-stretching production.

---

## 7. Aperiodic hull: suspension-flow formulation

The M5-485 discrete shift has variable dilation step

\[
\lambda(\mathbf Y)\in[\lambda_-,\lambda_+].
\]

Define the positive roof time

\[
\boxed{
\Theta(\mathbf Y):=2\log\lambda(\mathbf Y).
}
\]

Then

\[
0<\Theta_-\le\Theta(\mathbf Y)\le\Theta_+<\infty.
\]

The compact marked shift hull therefore admits the standard suspension space

\[
\widehat{\mathfrak H}
=
\{(\mathbf Y,r):0\le r<\Theta(\mathbf Y)\}/\sim,
\]

with

\[
(\mathbf Y,\Theta(\mathbf Y))
\sim
(\sigma\mathbf Y,0).
\]

The M5-485 invariant shift measure `mu` induces a finite invariant suspension measure `hat mu` after normalization by the mean roof length.

Thus the periodic and aperiodic dilation cases can be treated by one invariant similarity-time framework.

---

## 8. Invariant averaged enstrophy identity

On the suspension flow, `E` is bounded on the Type-I compact hull.

Invariance implies zero mean time derivative:

\[
\left\langle\frac{dE}{d\theta}\right\rangle_{\widehat\mu}=0.
\]

Averaging M5-486's exact balance gives

\[
\boxed{
\frac14\langle E\rangle
+
\langle P\rangle
=
\langle Q\rangle.
}
\]

Since the retained hull is nontrivial,

\[
\langle E\rangle>0
\]

on every invariant component that carries the nonzero record-carrier state.

Therefore

\[
\boxed{
\langle Q\rangle
>
0.
}
\]

The surviving compact hull must continuously regenerate normalized enstrophy against both similarity damping and viscosity.

---

## 9. Axial and projective strain channels are distinct

On the active set write

\[
W=\rho\xi,
\qquad
|\xi|=1.
\]

Decompose

\[
\boxed{
\Sigma\xi
=
\sigma\xi+\tau,
}
\]

where

\[
\sigma:=\xi\cdot\Sigma\xi,
\]

and

\[
\tau:=(I-\xi\otimes\xi)\Sigma\xi.
\]

Then

\[
Q
=
\int\rho^2\sigma\,dy.
\]

The M5-471 projective tilt mark is controlled by `tau`, not by `sigma`.

Algebraically,

\[
|\Sigma\xi|^2
=
\sigma^2+|\tau|^2.
\]

But neither component controls the sign or size of the other.

---

## 10. Explicit anti-conflation witness

Take

\[
\Sigma
=
\begin{pmatrix}
0&a&0\\
a&0&0\\
0&0&0
\end{pmatrix},
\qquad
\xi=e_1.
\]

Then `Sigma` is symmetric and trace free, while

\[
\sigma
=
e_1\cdot\Sigma e_1
=0,
\]

but

\[
\tau
=(I-e_1\otimes e_1)\Sigma e_1
=a e_2.
\]

Hence

\[
\boxed{
|\tau|=|a|>0
\quad\text{while}\quad
\sigma=0.
}
\]

Therefore a projective ratchet event cannot be counted as axial enstrophy production.

This is an algebraic firewall analogous to the earlier Fourier anti-shortcut firewall.

---

## 11. Magnitude-direction decomposition of palinstrophy

For

\[
W=\rho\xi,
\]

one has exactly

\[
\boxed{
|\nabla W|^2
=
|\nabla\rho|^2
+
\rho^2|\nabla\xi|^2.
}
\]

Thus

\[
P
=
\int|\nabla\rho|^2dy
+
\int\rho^2|\nabla\xi|^2dy.
\]

The similarity magnitude equation is

\[
\boxed{
\partial_\theta\rho
+
\rho
+
\frac12 y\cdot\nabla\rho
+
U\cdot\nabla\rho
=
\sigma\rho
+
\Delta\rho
-
\rho|\nabla\xi|^2.
}
\]

The last term is genuinely dissipative and records spatial direction variation.

However the M5-471 directional-diffusion ratchet term involves

\[
\frac{(I-\xi\otimes\xi)\Delta W}{\rho},
\]

which contains second derivatives and amplitude-direction coupling. No quantitative coercive implication from its one-trajectory `L1` action to the global `P` ledger has yet been proved.

That implication must not be assumed.

---

## 12. Two-channel recurrent hard core

M5-485 gives positive invariant mean of the material-ratchet channel.

M5-486 gives strictly positive invariant mean of axial stretching production:

\[
\boxed{
\langle Q\rangle
=
\frac14\langle E\rangle+
\langle P\rangle
>0.
}
\]

Thus a surviving compact marked hull must sustain simultaneously

### Channel A — longitudinal maintenance

\[
\rho^2\sigma
\]

with positive mean sufficient to pay similarity damping plus viscous palinstrophy.

### Channel B — projective/directional reorganization

positive-density material-axis ratchet action from tilt and/or directional diffusion.

The two channels are not the same algebraic quantity.

This is a genuine narrowing of the endpoint.

---

## 13. Critical strain consequence

By Holder,

\[
|Q|
\le
\|\Sigma\|_3
\|W\|_3^2.
\]

The compact Type-I bounds give uniform control of `||W||_2` and `||W||_infinity`, hence of `||W||_3`.

Therefore positive mean `Q` implies that the similarity strain cannot vanish in mean on the invariant hull.

Equivalently, the surviving endpoint necessarily pays a recurrent scale-critical strain charge in addition to its ratchet mark.

This is consistent with M5-472 and does not by itself contradict known blow-up criteria.

---

## 14. Why enstrophy is not yet the M5-485 strict cocycle

The similarity balance can be rearranged as

\[
\frac12E'
=
Q-rac14E-P.
\]

Because `Q` has no fixed sign pointwise, `E` is not monotone.

Thus the bounded observable `E` does not satisfy

\[
E\circ\sigma-E
\ge c a_{ratchet}.
\]

M5-486 therefore narrows the problem but does not supply the strict cocycle required by M5-485.

---

## 15. Correct next rigidity target

A closing theorem now has to exploit the **coupling** of the two recurrent channels.

The most precise targets are:

### R1 — axial/projective incompatibility

Show that a compact finite-enstrophy Type-I similarity hull cannot have both

\[
\langle\rho^2\sigma\rangle>0
\]

and positive-density order-one projective ratchet action without triggering a strong frequency/amplitude defect.

### R2 — directional-dissipation coercivity

On the active compact carrier, convert positive mean directional-diffusion action into a quantitatively positive normalized spatial direction-dissipation term

\[
\int\rho^2|\nabla\xi|^2dy,
\]

then determine whether the enstrophy balance plus source genealogy forces an unsustainable axial production rate.

### R3 — source/flux cocycle

Use the dual-source/finite-memory genealogy to construct a bounded similarity observable whose drift is positive whenever the two-channel ratchet/axial package is active.

R3 would directly feed the M5-485 invariant-measure contradiction.

---

## 16. Updated frontier

The bounded compact endpoint is now more accurately described as

\[
\boxed{
E_{dual}^{marked}
:
\text{nonzero compact Type-I similarity hull}
+
\langle Q\rangle>0
+
\langle a_{ratchet}\rangle>0.
}
\]

Hence

\[
\boxed{
\text{hypothetical singular tower}
\Longrightarrow
H_{amp/freq/mass}^{strong}
\lor
E_{dual}^{marked}.
}
\]

The remaining proof obligation is no longer merely "exclude backward DSS". It is the narrower problem of excluding a recurrent finite-enstrophy critical similarity hull that simultaneously maintains axial stretching and projective/directional ratchet action while preserving the terminal critical tail.

---

## 17. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
