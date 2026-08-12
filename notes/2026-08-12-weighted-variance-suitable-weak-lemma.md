# Candidate suitable-weak lemma: moving weighted variance

Date: 2026-08-12

Status: **BRIDGE LEMMA CANDIDATE — ALGEBRA CLOSED, FUNCTIONAL-ANALYTIC PASSAGE TO BE WRITTEN**.

## 1. Intended statement

Let `(u,p)` be a suitable weak solution on a spacetime region containing the support of a moving cutoff. Fix `ell>0` and a nonnegative radial

\[
\phi_\ell(x)=\phi(x/\ell),
\qquad
\phi\in C_c^\infty(B_2),
\]

with

\[
M_\ell=\int\phi_\ell dx>0.
\]

Define the weighted velocity convolution

\[
\mathcal U_\ell(X,t)
=
M_\ell^{-1}
\int\phi_\ell(x-X)u(x,t)dx
\]

and let `X(t)` solve the Caratheodory ODE

\[
\boxed{
\dot X(t)=\mathcal U_\ell(X(t),t).
}
\]

Set

\[
\varphi(x,t)=\phi_\ell(x-X(t)),
\]

\[
\bar U(t)=\dot X(t),
\qquad
v(x,t)=u(x,t)-\bar U(t).
\]

Then

\[
\int\varphi vdx=0.
\]

The target local variance inequality is

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

For smooth solutions this is an equality.

## 2. Why the center ODE is well posed at fixed scale

For energy-class `u`, the convolution `mathcal U_ell(X,t)` is finite for each fixed `ell`.

By Cauchy--Schwarz,

\[
|\mathcal U_\ell(X,t)|
\le
M_\ell^{-1}
\|\phi_\ell\|_2
\|u(t)\|_2.
\]

Likewise

\[
|\nabla_X\mathcal U_\ell(X,t)|
\le
M_\ell^{-1}
\|\nabla\phi_\ell\|_2
\|u(t)\|_2.
\]

Since suitable/Leray energy control gives an essentially bounded `L^2` norm in time, `mathcal U_ell` is measurable in `t`, bounded, and uniformly locally Lipschitz in `X` at every fixed positive `ell`.

This is the standard Caratheodory setting for an absolutely continuous center path.

## 3. Moving cutoff identity

Because `X` is absolutely continuous,

\[
\partial_t\varphi
=-\dot X\cdot\nabla\varphi
=-\bar U\cdot\nabla\varphi
\]

for almost every time.

Inserting `varphi` into the ordinary local energy inequality groups the time-cutoff term with the cubic transport term:

\[
|u|^2\partial_t\varphi
+|u|^2u\cdot\nabla\varphi
=|u|^2v\cdot\nabla\varphi.
\]

Thus moving the cutoff automatically replaces Eulerian transport by relative transport.

## 4. Weighted mean momentum identity

Let

\[
P_\phi(t)=\int\varphi(x,t)u(x,t)dx
=M_\ell\bar U(t).
\]

Testing the weak momentum equation against the moving cutoff in each coordinate gives, formally and then by approximation,

\[
\boxed{
M_\ell\dot{\bar U}
=
\int u\,(v\cdot\nabla\varphi)dx
+
\int p\nabla\varphi dx
+
\nu\int u\Delta\varphi dx.
}
\]

This identity supplies the evolution of the coherent mean channel without introducing an accelerating-frame pressure.

## 5. Variance subtraction

Use

\[
\frac12\int\varphi|v|^2dx
=
\frac12\int\varphi|u|^2dx
-
\frac{M_\ell}{2}|\bar U|^2.
\]

Subtract the scalar product of the mean-momentum identity with `bar U` from the local kinetic-energy inequality.

The three algebraic cancellations are:

### Transport

\[
\left(\frac{|u|^2}{2}-\bar U\cdot u\right)
(v\cdot\nabla\varphi)
=
\left(\frac{|v|^2}{2}-\frac{|\bar U|^2}{2}\right)
(v\cdot\nabla\varphi).
\]

Since `div v=0`,

\[
\int v\cdot\nabla\varphi=0,
\]

so only the `|v|^2/2` term remains.

### Pressure

\[
p\,u\cdot\nabla\varphi
-\bar U\cdot(p\nabla\varphi)
=p\,v\cdot\nabla\varphi.
\]

### Cutoff viscosity

The same quadratic identity, together with

\[
\int\Delta\varphi=0,
\]

leaves

\[
\frac\nu2\int|v|^2\Delta\varphi.
\]

This yields the target weighted-variance inequality.

## 6. Why this bridge is preferable to accelerating coordinates

The construction uses only

\[
X\in W^{1,1}_{loc}
\]

through `Xdot=bar U`; it never requires `Xddot` or a linear pressure correction.

Therefore it is much closer to the standard suitable-weak formulation than the accelerating-frame derivation.

The accelerating-frame identity remains a valid smooth consistency check, but it is no longer the primary rigorous route.

## 7. Functional-analytic details still required

Before marking the lemma **DERIVED THEOREM**, the following points must be written carefully:

1. approximate the absolutely-continuous moving cutoff by admissible smooth nonnegative spacetime test functions;
2. justify the moving-cutoff weak momentum test and absolute continuity of the weighted mean momentum;
3. justify the chain rule for `|bar U(t)|^2`;
4. pass to almost-everywhere endpoint times in the local energy inequality;
5. confirm all pressure terms are integrable under the standard suitable assumptions;
6. state whether the argument is local-in-space or uses whole-space energy control only to construct the center ODE.

None of these is presently expected to change the algebraic channel structure, but they must not be skipped in a proof claim.

Status: **OPEN FUNCTIONAL-ANALYTIC COMPLETION**.

## 8. Proof-route consequence

Once this lemma is completed, the primary local proof object is entirely Eulerian-compatible:

\[
\boxed{
\text{moving smooth weighted sphere}
+
\text{mean-zero internal velocity}
+
\text{standard suitable local-energy inequality}.
}
\]

The DSD task is then concentrated on estimating the three signed redistribution channels

\[
A_\phi,
\qquad
P_\phi,
\qquad
B_\phi
\]

against the weighted oscillation and dissipation channels so that a known pressure-free epsilon-regularity threshold is eventually forced.
