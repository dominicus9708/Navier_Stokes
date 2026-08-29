# DSD M5-270 — Residual Terminal-Derivative Critical-Summability Firewall

Date: 2026-08-30

Parent: `DSD_M5_269_RG_FLATNESS_PHYSICAL_TERMINAL_TIME_CERTIFICATION_2026-08-30.md`

Status: **CRITICAL-SUMMABILITY AUDIT / ON THE SURVIVING RESIDUAL-ACTIVE REALIZED TAIL, THE FIRST TERMINAL-TIME COEFFICIENT IS THE STATIONARY RESIDUAL `F_T`, WHICH HAS CRITICAL DEGREE `-3` / AFTER THE NATURAL PARABOLIC CORE CUTOFF `r~sqrt(tau)`, ITS `H^-1` SIZE GROWS ONLY LIKE `tau^-1/4`, WHILE THE CRITICAL GRADIENT DISSIPATION GROWS LIKE `tau^-1/2` AT THE SQUARED-NORM LEVEL / BOTH ARE TIME-INTEGRABLE IN THE STANDARD LERAY-HOPF ENERGY / `u_t in L^(4/3)_t H^-1` CLASSES, AND EVEN THE MODEL `H^-1` SIZE IS SQUARE-INTEGRABLE IN TIME / THEREFORE A NONZERO FIRST RESIDUAL COEFFICIENT DOES NOT BY ITSELF CONTRADICT THE ORDINARY GLOBAL ENERGY OR WEAK TIME-DERIVATIVE BUDGETS / ANY CLOSURE MUST GAIN BEYOND CRITICAL PARABOLIC SUMMABILITY / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input from M5-269

On the realized RG reconstruction,

\[
\mathscr R_\rho(T)(Y)
=\sqrt{\tau_0}\,
 u\!\left(x_*+\sqrt{\tau_0}Y,
 T^*-\tau_0\rho\right),
\]

and

\[
\partial_\rho\mathscr R_\rho
=-\mathcal F(\mathscr R_\rho),
\qquad
\mathcal F(U)=\nu\Delta U-\mathbb P\nabla\cdot(U\otimes U).
\]

At the terminal boundary,

\[
\boxed{
\partial_\rho\mathscr R_\rho\big|_{\rho=0}
=-F_T,
\qquad
F_T:=\mathcal F(T).
}
\]

Thus the residual-active endpoint

\[
\mathbf F(T)\ge\varepsilon_{glob}>0
\]

is genuinely a nonzero first terminal-time coefficient, not an external forcing.

---

## 2. Critical spatial degrees

On the retained smooth critical tail class,

\[
|T(x)|\lesssim |x|^{-1},
\qquad
|\nabla T(x)|\lesssim |x|^{-2},
\qquad
|F_T(x)|\lesssim |x|^{-3}
\]

on punctured scale-normalized cells, with the corresponding local derivative bounds.

The degree `-3` for `F_T` follows both from stationary Navier--Stokes scaling and from M5-239:

\[
\mathcal F(S_\lambda T)
=\lambda^2S_\lambda\mathcal F(T).
\]

---

## 3. Natural inner cutoff near terminal time

Let

\[
\tau:=T^*-t.
\]

The natural first-hitting/parabolic core radius is

\[
\boxed{a(\tau)\asymp\sqrt\tau.}
\]

Outside this core, the terminal/Fuchsian expansion is the relevant description. To test whether the first residual coefficient already violates standard weak-solution budgets, use the worst critical model on

\[
A_{a,1}:=\{a<|x|<1\}.
\]

This is deliberately an upper-cost model: if even the full `r^-3` coefficient is compatible with the standard budgets, a local residual-gap certificate cannot give a contradiction by those budgets alone.

---

## 4. `H^-1` size of the `r^-3` terminal derivative

In three dimensions,

\[
L^{6/5}(\mathbb R^3)\hookrightarrow H^{-1}(\mathbb R^3).
\]

For

\[
f(x)\sim |x|^{-3}
\]

on `A_(a,1)`,

\[
\begin{aligned}
\|f\|_{L^{6/5}(A_{a,1})}^{6/5}
&\lesssim
\int_a^1 r^{-18/5}r^2dr\\
&=
\int_a^1r^{-8/5}dr\\
&\lesssim a^{-3/5}.
\end{aligned}
\]

Hence

\[
\boxed{
\|f\|_{H^{-1}}
\lesssim
\|f\|_{6/5}
\lesssim a^{-1/2}.
}
\]

With

\[
a\asymp\sqrt\tau,
\]

this becomes

\[
\boxed{
\|f(\tau)\|_{H^{-1}}
\lesssim\tau^{-1/4}.
}
\]

Thus the critical residual coefficient has exactly a mild terminal singularity in the natural negative Sobolev norm.

---

## 5. Standard time-derivative integrability is not violated

The Leray-Hopf weak formulation naturally accommodates time derivatives in spaces such as

\[
u_t\in L^{4/3}_{loc}(H^{-1})
\]

(or comparable negative-Sobolev formulations after the usual nonlinear estimates).

The model critical growth gives

\[
\|u_t(\tau)\|_{H^{-1}}^{4/3}
\lesssim
\tau^{-1/3}.
\]

Therefore

\[
\boxed{
\int_0^{\tau_1}
\tau^{-1/3}d\tau<\infty.
}
\]

In fact the model `H^-1` size is even square-integrable in time:

\[
\|u_t\|_{H^{-1}}^2
\lesssim\tau^{-1/2},
\]

and

\[
\boxed{
\int_0^{\tau_1}\tau^{-1/2}d\tau<\infty.
}
\]

No standard weak time-derivative budget is therefore contradicted.

---

## 6. Critical gradient dissipation is also time-integrable

For the critical velocity profile,

\[
|\nabla u|\sim r^{-2}.
\]

On `A_(a,1)`,

\[
\begin{aligned}
\|\nabla u\|_2^2
&\lesssim
\int_a^1r^{-4}r^2dr\\
&\lesssim a^{-1}.
\end{aligned}
\]

Thus with `a~sqrt(tau)`,

\[
\boxed{
\|\nabla u(\tau)\|_2^2
\lesssim\tau^{-1/2}.
}
\]

Hence

\[
\boxed{
\int_0^{\tau_1}\|\nabla u(\tau)\|_2^2d\tau
<\infty.
}
\]

This is precisely the familiar critical-parabolic summability that allows a Type-I cascade to remain compatible with finite total kinetic-energy dissipation.

---

## 7. Stronger norms can diverge, but there is no corresponding global budget

The same `r^-3` model has

\[
\|f\|_2^2
\sim
\int_a^1r^{-6}r^2dr
\sim a^{-3},
\]

so

\[
\|f\|_2\sim a^{-3/2}\sim\tau^{-3/4}.
\]

Consequently

\[
\int_0\|f\|_2^2dt
\sim\int_0\tau^{-3/2}d\tau
=\infty.
\]

Likewise higher derivative/palinstrophy quantities become increasingly nonintegrable.

But the Navier--Stokes energy inequality does not provide a global `L2_t L2_x` budget for `u_t`, nor a global finite palinstrophy budget up to a hypothetical singular time.

Therefore these divergences cannot be used as contradictions without a separately proved higher-order a priori estimate.

---

## 8. Discrete-generation version

At physical scale `r_j`, the critical gradient dissipation rate is of order

\[
\|\nabla u\|_2^2\sim r_j^{-1}.
\]

The natural stage duration is

\[
\Delta t_j\sim r_j^2.
\]

Thus the stage energy cost is

\[
\boxed{
\Delta E_j
\sim r_j.
}
\]

Since

\[
r_j=r_0q^{-j/2},
\]

one has

\[
\boxed{
\sum_j\Delta E_j
\lesssim
\sum_jr_j<\infty.
}
\]

This is the generation-by-generation version of the continuous `tau^-1/2` integrability.

---

## 9. DSD firewall

The following implications are RED:

\[
\boxed{
F_T\ne0
\Longrightarrow
u_t\text{ violates the standard }H^{-1}\text{ time budget},
}
\]

and

\[
\boxed{
F_T\ne0
\Longrightarrow
\text{critical gradient dissipation is non-summable}.
}
\]

Both are false at the natural Type-I scaling.

A successful residual-active closure therefore needs at least one genuinely noncritical gain, such as

1. a strict power beyond the `r^-3` / `r^-2` critical scaling;
2. a logarithmically non-summable lower bound;
3. a sign-definite state functional whose total variation is finite;
4. a spectral/nondegeneracy theorem excluding the realized backward-RG range;
5. a regularity theorem triggered by recurrence/approximate self-similarity.

---

## 10. Updated frontier

After M5-268/M5-269, the stationary branch is closed. The sole minimal-tail endpoint is

\[
\boxed{
\mathbf F(T)\ge\varepsilon_{glob}>0
}
\]

on the compact realized tail hull.

M5-270 shows that the first obvious global budgets are exactly too weak:

\[
\boxed{
\text{residual-active Type-I scaling is critically summable in energy and }H^{-1}\text{ time derivative.}
}
\]

The next useful calculation should therefore exploit a genuinely Navier--Stokes structural moment of `F_T`, rather than another unweighted norm lower bound.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
