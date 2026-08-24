# Mean-Vorticity Plateau Stage Ledger — 2026-08-24

Status: **DYNAMIC REDUCTION OF THE LOW-DERIVATIVE ANNULAR-MASS SURVIVOR / GLOBAL REGULARITY NOT PROVED.**

This note continues `ANNULAR_MASS_INFLATION_AND_BUFFER_AUDIT_2026-08-24.md`.

The anti-proof audit shows that a large annular vorticity mass with small derivative need not be a separate core. It may be a spatially coherent, almost constant-vorticity plateau. Such a plateau is a genuine static possibility and must be handled dynamically.

The key result below is an exact vector mean-vorticity equation in the dynamically normalized first-hitting variables. A plateau that retains comparable normalized mean amplitude through a stage `M_j -> q M_j` must pay approximately one full `log q` of longitudinal stretching action unless transport/diffusion or spatial incoherence is large.

## 1. Dynamically normalized vorticity equation

Use

\[
\Omega_s+V\cdot\nabla\Omega+b\Omega
=\Sigma\Omega+\nu\Delta\Omega,
\]

with

\[
\frac{ds}{dt}=M(t),
\qquad
b=\frac d{ds}\log M,
\qquad
\int_{I_j}b\,ds=\log q.
\]

The first-hitting cap is

\[
\|\Omega\|_\infty\le1.
\]

## 2. Moving weighted mean vorticity

Let

\[
\phi_a(y,s)=\Phi\!\left(\frac{y-a(s)}R\right)
\]

be a fixed-shape smooth compactly supported weight, with `0<=phi<=1`. Define

\[
\boxed{I_\phi(s):=\int\phi_a(y,s)\Omega(y,s)dy.}
\]

Since

\[
\phi_s=-a_s\cdot\nabla\phi,
\]

integration by parts in the cutoff-transport term gives the exact identity

\[
\boxed{
I_\phi'+bI_\phi
=
\int\phi\Sigma\Omega\,dy
-
\int\phi(V-a_s)\cdot\nabla\Omega\,dy
+
\nu\int\phi\Delta\Omega\,dy.
}
\]

Integrating the diffusion term by parts once,

\[
\boxed{
I_\phi'+bI_\phi
=
\int\phi\Sigma\Omega\,dy
-
\int\phi(V-a_s)\cdot\nabla\Omega\,dy
-
\nu\int\nabla\phi\cdot\nabla\Omega\,dy.
}
\]

Thus no second derivative is needed in the plateau ledger.

## 3. Exact logarithmic amplitude ledger

Whenever `I_phi != 0`, define

\[
n_\phi=\frac{I_\phi}{|I_\phi|}.
\]

Taking the scalar product with `n_phi` gives

\[
\boxed{
\frac d{ds}\log|I_\phi|+b
=\gamma_\phi+\mathcal E_{tr}+\mathcal E_\nu,
}
\]

where

\[
\boxed{
\gamma_\phi
:=
\frac{
n_\phi\cdot\int\phi\Sigma\Omega}{|I_\phi|},
}
\]

\[
\boxed{
\mathcal E_{tr}
:=
-
\frac{
n_\phi\cdot\int\phi(V-a_s)\cdot\nabla\Omega}{|I_\phi|},
}
\]

and

\[
\boxed{
\mathcal E_\nu
:=
-
u
\frac{
n_\phi\cdot\int\nabla\phi\cdot\nabla\Omega}{|I_\phi|}.
}
\]

The direct error bounds are

\[
\boxed{
|\mathcal E_{tr}|
\le
\frac{
\|V-a_s\|_{L^2(\phi)}
\|\nabla\Omega\|_{L^2(\phi)}
}{|I_\phi|},
}
\]

and

\[
\boxed{
|\mathcal E_\nu|
\le
\nu
\frac{
\|\nabla\phi\|_2
\|\nabla\Omega\|_{L^2(\operatorname{supp}\nabla\phi)}
}{|I_\phi|}.
}
\]

Hence large relative transport, local derivative action, or viscous boundary action is explicitly visible rather than hidden.

## 4. Plateau coherence turns the stretching term into a mean-strain longitudinal action

Let

\[
\mu_\phi:=\int\phi,
\qquad
\bar\Omega_\phi:=\mu_\phi^{-1}I_\phi,
\qquad
\bar\Sigma_\phi:=\mu_\phi^{-1}\int\phi\Sigma.
\]

Write

\[
\Omega=\bar\Omega_\phi+\delta\Omega,
\qquad
\int\phi\delta\Omega=0.
\]

Then

\[
\boxed{
\gamma_\phi
=
n_\phi^T\bar\Sigma_\phi n_\phi
+\mathcal E_{cov},
}
\]

where

\[
\boxed{
|\mathcal E_{cov}|
\le
\frac{
\left(\int\phi|\Sigma|^2\right)^{1/2}
\left(\int\phi|\delta\Omega|^2\right)^{1/2}
}{|I_\phi|}.
}
\]

Therefore the low-derivative/low-variance plateau lane is genuinely governed by the longitudinal component of the **mean strain** in the mean-vorticity direction.

If `E_cov` is large, the plateau is not sufficiently coherent and exits to the spatial-variation/strain-covariance residual branch.

## 5. One geometric first-hitting stage

Integrating over a stage `I_j` gives the exact identity

\[
\boxed{
\log\frac{|I_{\phi,1}|}{|I_{\phi,0}|}
+\log q
=
\int_{I_j}
n_\phi^T\bar\Sigma_\phi n_\phi\,ds
+\mathcal R_{mv,j},
}
\]

where

\[
\boxed{
\mathcal R_{mv,j}
:=
\int_{I_j}
(\mathcal E_{cov}+\mathcal E_{tr}+\mathcal E_\nu)ds.
}
\]

Thus if the plateau mean amplitude is retained through the stage and

\[
|\mathcal R_{mv,j}|\le e_{mv},
\]

then

\[
\boxed{
\int_{I_j}
n_\phi^T\bar\Sigma_\phi n_\phi\,ds
\ge
\log q
-
e_{mv}
-
\left|\log\frac{|I_{\phi,1}|}{|I_{\phi,0}|}\right|.
}
\]

For a multistage retained plateau with fixed bounds

\[
0<i_-\le|I_{\phi,j}|\le i_+<\infty,
\]

the endpoint logarithms telescope. Hence

\[
\boxed{
\liminf_{N\to\infty}
\frac1N
\sum_{j=1}^N
\int_{I_j}
n_\phi^T\bar\Sigma_\phi n_\phi\,ds
\ge
\log q-
\bar e_{mv},
}
\]

where `bar e_mv` is the asymptotic mean error action per stage.

This is a full `log q` action floor, stronger than the `1/4 log q` scale term in the localized enstrophy ledger.

## 6. Direct deformation-time consequence

Suppose the pure smooth corridor supplies

\[
\boxed{\|\bar\Sigma_\phi\|\le B_{\Sigma,+}.}
\]

Then any retained low-error plateau stage with positive action

\[
a_{mv}:=\log q-e_{mv}-e_{end}>0
\]

must satisfy

\[
\boxed{
L_j\ge L_{mv}:=\frac{a_{mv}}{B_{\Sigma,+}}.
}
\]

Therefore if the existing moving-variance/local-core upper time satisfies

\[
\boxed{L_{stage,+}<L_{mv},}
\]

the coherent plateau branch is S-closed on the original smooth finite stage.

If the inequality is not strong enough to close it, the plateau is no longer an untyped annular-mass escape: it has been reduced to the existing coherent deformation/projective lane with a fixed longitudinal strain-action requirement.

## 7. Exact complement of the plateau lane

A repeated large-annular-mass event now has the following dynamical alternatives:

\[
\boxed{
\begin{aligned}
\text{large annular mass}
\Longrightarrow\;&
\text{large local derivative/variance action}\\
&\lor\text{loss of mean-vorticity amplitude}\\
&\lor\text{large relative material transport}\\
&\lor\text{large viscous boundary action}\\
&\lor\text{large strain-vorticity covariance defect}\\
&\lor\text{coherent longitudinal strain action }\gtrsim\log q.
\end{aligned}
}
\]

The first five are already typed `H/T/rebuild/residual` payments. The final branch is the existing deformation/projective corridor and carries the explicit stage-length floor `L_mv`.

## 8. Anti-proof significance

This note does **not** claim that large annular mass is automatically multicore turnover. The static counterexample of an almost constant vorticity plateau is explicitly retained.

What is proved is that such a plateau cannot repeatedly follow the first-hitting normalization for free. If its normalized mean survives, it must receive one full geometric amplification action from mean longitudinal strain, modulo explicit derivative/transport/diffusion/covariance errors.

Status: **THE LOW-DERIVATIVE ANNULAR-MASS SURVIVOR IS REDUCED TO A MEAN-VORTICITY AMPLIFICATION LEDGER. RETAINING COMPARABLE NORMALIZED MEAN VORTICITY ACROSS `M -> qM` REQUIRES APPROXIMATELY `log q` OF LONGITUDINAL MEAN-STRAIN ACTION PER STAGE, UNLESS AN ALREADY TYPED DERIVATIVE, TRANSPORT, DIFFUSIVE, REBUILD, OR COVARIANCE RESIDUAL IS LARGE. THE ANNULAR-MASS BRANCH IS THEREFORE NO LONGER AN INDEPENDENT STATIC `T` LABEL, BUT THE FINAL DEFORMATION/TIME COMPARISON REMAINS TO BE CLOSED. GLOBAL REGULARITY REMAINS UNPROVED.**