# Moving weighted-variance lemma for whole-space suitable solutions

Date: 2026-08-12

Status: **DERIVED LEMMA / WHOLE-SPACE FINITE-ENERGY SUITABLE CLASS**.

This note completes the functional-analytic bridge sketched in `2026-08-12-weighted-variance-suitable-weak-lemma.md`.  It is not claimed to be a novel theorem; it is the internal proof lemma used by this repository.

## Lemma

Let `(u,p)` be a finite-energy suitable weak solution of the unforced incompressible Navier--Stokes equations on

\[
\mathbb R^3\times(0,T),
\]

with

\[
u\in L^\infty(0,T;L^2(\mathbb R^3))\cap L^2(0,T;\dot H^1(\mathbb R^3)),
\qquad
p\in L^{3/2}_{\rm loc}.
\]

Fix `ell>0` and a nonnegative nonzero

\[
\phi\in C_c^\infty(\mathbb R^3),
\qquad
\phi_\ell(x)=\phi(x/\ell),
\]

and set

\[
M_\ell=\int_{\mathbb R^3}\phi_\ell dx.
\]

Define

\[
\mathcal U_\ell(X,t)
=
M_\ell^{-1}
\int\phi_\ell(x-X)u(x,t)dx.
\]

For every initial center `X(s)=X_s`, the ODE

\[
\dot X(t)=\mathcal U_\ell(X(t),t)
\]

has a unique absolutely continuous solution on `[s,T]`.

Let

\[
\varphi(x,t)=\phi_\ell(x-X(t)),
\qquad
\bar U(t)=\dot X(t),
\qquad
v(x,t)=u(x,t)-\bar U(t).
\]

Then

\[
\int\varphi vdx=0
\]

for almost every `t`, and for almost every pair of Lebesgue times `s<t` one has

\[
\boxed{
\begin{aligned}
&\frac12\int\varphi(x,t)|v(x,t)|^2dx
+\nu\int_s^t\int\varphi|\nabla u|^2dxdt'\\
&\le
\frac12\int\varphi(x,s)|v(x,s)|^2dx\\
&\quad+
\int_s^t\int
\frac{|v|^2}{2}
v\cdot\nabla\varphi\,dxdt'\\
&\quad+
\int_s^t\int
p\,v\cdot\nabla\varphi\,dxdt'\\
&\quad+
\frac\nu2
\int_s^t\int
|v|^2\Delta\varphi\,dxdt'.
\end{aligned}
}
\]

For smooth solutions the inequality is an equality.

## Proof

### 1. Construction of the moving center

For every fixed `ell`, Cauchy--Schwarz gives

\[
|\mathcal U_\ell(X,t)|
\le
M_\ell^{-1}\|\phi_\ell\|_2\|u(t)\|_2.
\]

Also

\[
|\mathcal U_\ell(X,t)-\mathcal U_\ell(Y,t)|
\le
M_\ell^{-1}\|\nabla\phi_\ell\|_2
\|u(t)\|_2|X-Y|.
\]

The global energy bound makes the right sides essentially bounded in time.  Hence `mathcal U_ell` is measurable in `t`, bounded, and globally Lipschitz in `X` with an integrable Lipschitz coefficient.  The Caratheodory ODE theorem gives a unique absolutely continuous `X(t)`.

By definition,

\[
\int\varphi(x,t)u(x,t)dx=M_\ell\dot X(t),
\]

so

\[
\int\varphi vdx=0.
\]

### 2. The moving cutoff is admissible by approximation

The path `X` is absolutely continuous and in fact Lipschitz at fixed `ell` under the global energy bound.  Therefore

\[
\varphi(x,t)=\phi_\ell(x-X(t))
\]

is smooth in space and Lipschitz in time, with

\[
\partial_t\varphi
=-\dot X\cdot\nabla\varphi
=-\bar U\cdot\nabla\varphi
\]

for almost every `t`.

Mollify `X` in time on compact subintervals and multiply by the usual nonnegative smooth temporal cutoff used to select endpoints.  The resulting nonnegative test functions are admissible in the suitable local energy inequality.  The mollified paths converge uniformly while their derivatives converge in `L^1`; all spatial derivatives of the translated cutoff remain uniformly bounded and compactly supported.  The energy-class bounds on `u`, together with local `p in L^{3/2}`, permit passage to the limit by dominated/Hölder estimates.  Thus the local energy inequality is valid with the Lipschitz moving cutoff at Lebesgue endpoint times.

It gives

\[
\begin{aligned}
K(t)+\nu\int_s^t\int\varphi|\nabla u|^2
\le K(s)
&+\int_s^t\int
\frac{|u|^2}{2}(u-\bar U)\cdot\nabla\varphi\\
&+\int_s^t\int p\,u\cdot\nabla\varphi\\
&+\frac\nu2\int_s^t\int |u|^2\Delta\varphi,
\end{aligned}
\]

where

\[
K(t)=\frac12\int\varphi|u|^2dx.
\]

### 3. Weighted mean momentum is absolutely continuous

Use the weak momentum equation with vector test functions obtained from the same time-mollified moving cutoff.  Passing to the limit yields, in distributions in time,

\[
\frac{d}{dt}
\int\varphi u\,dx
=
\int u\,[(u-\bar U)\cdot\nabla\varphi]dx
+
\int p\nabla\varphi dx
+
\nu\int u\Delta\varphi dx.
\]

Every term on the right belongs to `L^1_{loc}` in time:

- the quadratic velocity term is controlled by the local/global energy class and the bounded cutoff gradient;
- the pressure term is integrable because `p in L^{3/2}_{loc}` and the cutoff is smooth and compactly supported;
- the final term is controlled by `u in L^\infty_tL^2_x`.

Hence the weighted momentum

\[
P_\phi(t)=\int\varphi u\,dx=M_\ell\bar U(t)
\]

belongs to `W^{1,1}_{loc}`.  Therefore `bar U in W^{1,1}_{loc}` and the Sobolev chain rule gives

\[
\frac{M_\ell}{2}
\left(|\bar U(t)|^2-|\bar U(s)|^2\right)
=
\int_s^t\bar U\cdot P_\phi'\,dt'.
\]

### 4. Subtract the coherent mean energy

The weighted variance is exactly

\[
E_{\rm osc}(t)
=
\frac12\int\varphi|u-\bar U|^2dx
=K(t)-\frac{M_\ell}{2}|\bar U(t)|^2.
\]

Subtract the chain-rule identity of Step 3 from the local energy inequality of Step 2.

For transport,

\[
\frac{|u|^2}{2}-\bar U\cdot u
=
\frac{|v|^2}{2}-\frac{|\bar U|^2}{2}.
\]

Since `div v=0`,

\[
\int v\cdot\nabla\varphi dx=0,
\]

so the constant term disappears and only

\[
\int\frac{|v|^2}{2}v\cdot\nabla\varphi dx
\]

remains.

For pressure,

\[
p\,u\cdot\nabla\varphi
-
\bar U\cdot(p\nabla\varphi)
=
p\,v\cdot\nabla\varphi.
\]

For the cutoff Laplacian term the same quadratic identity applies, while

\[
\int\Delta\varphi dx=0,
\]

leaving

\[
\frac\nu2\int|v|^2\Delta\varphi dx.
\]

Finally `grad v=grad u` because `bar U` is spatially constant.  This gives the stated inequality.

QED.

## Scope and claim boundary

The lemma is derived for the whole-space finite-energy suitable class, which is sufficient for the present Clay-aligned proof track.  A purely local suitable solution without global `L^2` control would require a localized construction of the center field and corresponding ODE estimates.

The lemma does **not** prove regularity.  It only supplies a rigorous moving local-energy inequality for the internal velocity oscillation after coherent local translation has been removed.

## DSD interpretation

The proof track can now use the typed critical channels

\[
C_\phi,
\qquad
D_\phi,
\qquad
A_\phi,
\qquad
P_\phi,
\qquad
B_\phi
\]

without appealing to an accelerating coordinate system.

This closes the former `moving-frame/suitable-weak bridge` obligation.  The remaining hard obligation is quantitative: force a pressure-free epsilon-regularity smallness threshold from these channels at every candidate singular scale.
