# DSD M5-275 — Albritton--Barker Terminal-Trace Liouville Closure of the Realized Spatial-Type-I W1 Branch

Date: 2026-08-30

Parent: `DSD_M5_274_GLOBAL_RHO_RG_EXTENSION_AND_NONLINEAR_STRETCHING_NECESSITY_2026-08-30.md`

External anchor: D. Albritton and T. Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, J. Math. Pures Appl. / arXiv:1811.00502v2 (2019), Theorem 4.1.

Status: **MAJOR EXTERNAL-LIOUVILLE CLOSURE / THE GLOBAL-`rho` REALIZED RG SOLUTION FROM M5-274 IS A MILD ANCIENT SOLUTION WITH A UNIFORM `L^{3,infinity}` BOUND AT EVERY BACKWARD TIME / M5-269 SUPPLIES AN ACTUAL DISTRIBUTIONAL TERMINAL TRACE `T` / THE SPATIAL TYPE-I BOUND GIVES `|T(x)|<=C/|x|`, HENCE `T in L^{3,infinity} subset dot B^{-1}_{infinity,infinity}` AND, DIRECTLY, `T(lambda .)->0` IN DISTRIBUTIONS, SO `T` BELONGS EXACTLY TO THE ALBRITTON--BARKER SUBSPACE `mathbb B` AND THE BESOV DISTANCE IN THEIR THEOREM IS ZERO / THEOREM 4.1 THEREFORE FORCES THE GLOBAL-RG ANCIENT SOLUTION TO VANISH IDENTICALLY / AT `rho=1` THIS FORCES THE NONTRIVIAL W1 STATE TO BE ZERO, CONTRADICTING THE CHECKPOINT VORTICITY WITNESS / THUS THE ENTIRE REALIZED COMPLETE W1 BRANCH WITH THE AUDITED GLOBAL SPATIAL TYPE-I BOUND AND ACTUAL PUNCTURED TERMINAL TRACE IS CLOSED, WITHOUT SPLITTING STATIONARY VS RESIDUAL-ACTIVE TAILS / GLOBAL REGULARITY STILL REQUIRES CLOSURE OF THE PRE-W1 ESCAPE BRANCHES WHERE SPATIAL TYPE-I / COMPACTNESS / NO-H / NO-T FAILS.**

---

## 1. External theorem

Albritton--Barker define the subspace

\[
\mathbb B\subset\dot B^{-1}_{\infty,\infty}
\]

by

\[
\boxed{
f\in\mathbb B
\quad\Longleftrightarrow\quad
f(\lambda\,\cdot)\to0
\text{ in distributions as }\lambda\to\infty.
}
\]

Their Theorem 4.1 states: for every `M>0` there exists `epsilon(M)>0` such that if `v` is a mild ancient solution on

\[
\mathbb R^3\times(-\infty,0)
\]

with

\[
\|v(\cdot,t_k)\|_{L^{3,\infty}}\le M
\]

for a sequence

\[
t_k\downarrow-\infty,
\]

and

\[
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
(v(\cdot,0),\mathbb B)
\le\varepsilon(M),
\]

then

\[
\boxed{v\equiv0.}
\]

We audit each hypothesis against M5-269/M5-274 rather than invoking the theorem by analogy.

---

## 2. The global-RG ancient solution

M5-274 constructs, for every realized complete W1 tail `T`,

\[
U(Y,\tau)
:=\mathscr R_{-\tau}(T)(Y),
\qquad
\tau\in(-\infty,0),
\]

which solves

\[
\boxed{
U_\tau-\nu\Delta U
+(U\cdot\nabla)U
+\nabla P=0,
\qquad
\nabla\cdot U=0.
}
\]

The normalization `nu=1` used in the cited theorem is harmless: rescale space/time by the fixed viscosity when necessary. We keep `nu` in the project notation.

For every finite negative `tau`, the descendant is smooth on the whole space because it is a finite rescaling of a smooth W1 state.

---

## 3. Uniform weak-`L3` bound from the spatial Type-I estimate

M5-274 gives

\[
\boxed{
|U(Y,\tau)|
\le
\frac{C_*}{\sqrt{-\tau}+|Y|}.
}
\]

For fixed `a>0`, let

\[
g_a(Y)=\frac{C_*}{a+|Y|}.
\]

If `lambda>0`,

\[
\{g_a>\lambda\}
\subset
B_{C_*/\lambda},
\]

so

\[
|\{g_a>\lambda\}|
\le
\frac{4\pi}{3}
\left(\frac{C_*}{\lambda}\right)^3.
\]

Therefore

\[
\boxed{
\|U(\cdot,\tau)\|_{L^{3,\infty}}
\le C_{Lor}C_*
}
\]

uniformly for all `tau<0`.

In particular, for any sequence

\[
\tau_k\downarrow-\infty,
\]

\[
\boxed{
\sup_k
\|U(\cdot,\tau_k)\|_{L^{3,\infty}}
\le M<\infty.
}
\]

The backward-time Lorentz hypothesis of Theorem 4.1 is satisfied.

---

## 4. Mildness

For every finite `tau0<0`, the pointwise Type-I estimate gives

\[
U(\cdot,\tau_0)\in L^q(\mathbb R^3)\cap L^\infty(\mathbb R^3)
\]

for every

\[
q>3.
\]

Indeed the core is bounded by `C/sqrt(-tau0)` and the far field decays like `1/r`.

The standard `L^q`, `q>3`, Navier--Stokes local theory therefore produces a unique mild solution forward from time `tau0`.

The already constructed smooth descendant solution has the same data and lies in the same smooth uniqueness class, so it coincides with that mild solution on every compact forward subinterval of `(tau0,0)`.

Since `tau0<0` is arbitrary,

\[
\boxed{
U\text{ is a mild ancient solution on }\mathbb R^3\times(-\infty,0).
}
\]

The spatial decay excludes the parasitic spatially constant ancient solutions as well.

---

## 5. Actual terminal trace from M5-269

M5-269 identifies the RG parameter exactly with physical terminal-time depth at fixed descendant coordinate:

\[
\mathscr R_\rho(T)(Y)
=\sqrt{\tau_0}\,
 u\!\left(x_*+\sqrt{\tau_0}Y,
 T^*-\tau_0\rho\right).
\]

Hence on every punctured compact

\[
\boxed{
U(\cdot,\tau)\to T
\quad\text{smoothly locally on }\mathbb R^3\setminus\{0\}
\quad(\tau\uparrow0).
}
\]

The spatial Type-I bound also gives

\[
\boxed{
|T(Y)|\le\frac{C_*}{|Y|}.
}
\]

Since `1/|Y|` is locally integrable in three dimensions and is a tempered distribution at infinity under the same critical bound, this defines a genuine distributional terminal trace on all of `R3`.

Thus the object denoted `v(.,0)` in Albritton--Barker is available and equals `T`.

This terminal-trace property is a substantive extra input; it is not enjoyed by a generic rotating/quasiperiodic Type-I ancient solution whose phase may fail to converge as `t -> 0-`.

---

## 6. The terminal trace is uniformly weak-`L3`

The same distribution-function calculation as Section 3, now with `a=0`, gives

\[
\boxed{
T\in L^{3,\infty}(\mathbb R^3),
\qquad
\|T\|_{L^{3,\infty}}
\le C_{Lor}C_*.
}
\]

The standard Lorentz-to-Besov embedding gives

\[
\boxed{
L^{3,\infty}(\mathbb R^3)
\hookrightarrow
\dot B^{-1}_{\infty,\infty}(\mathbb R^3).
}
\]

For completeness, using the heat-kernel characterization and Lorentz Young inequality,

\[
\sqrt t\,\|e^{t\Delta}T\|_\infty
\le
C\|T\|_{L^{3,\infty}},
\]

uniformly in `t>0`, which is precisely the relevant homogeneous Besov bound.

---

## 7. Direct proof that `T` belongs to `mathbb B`

Let

\[
\varphi\in C_c^\infty(\mathbb R^3)
\]

be a test function.

From

\[
|T(\lambda x)|
\le
\frac{C_*}{\lambda|x|},
\]

we obtain

\[
\begin{aligned}
\left|
\langle T(\lambda\cdot),\varphi\rangle
\right|
&\le
\frac{C_*}{\lambda}
\int_{\operatorname{supp}\varphi}
\frac{|\varphi(x)|}{|x|}dx.
\end{aligned}
\]

The last integral is finite because `1/|x|` is locally integrable in `R3`.

Therefore

\[
\boxed{
T(\lambda\cdot)
\to0
\quad\text{in }\mathcal D'(\mathbb R^3)
\quad(\lambda\to\infty).
}
\]

Together with Section 6,

\[
\boxed{T\in\mathbb B.}
\]

Consequently

\[
\boxed{
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
(T,\mathbb B)=0.
}
\]

This is stronger than the smallness required in Theorem 4.1.

---

## 8. Apply Albritton--Barker Theorem 4.1

All hypotheses have now been matched:

1. `U` is a mild ancient solution;
2. `U` has a uniform `L^{3,infinity}` bound at every negative time, hence along a sequence `tau_k -> -infinity`;
3. `U(.,0)=T` exists distributionally;
4. `T in dot B^{-1}_{infinity,infinity}`;
5. `T in mathbb B`, so the required Besov distance is zero.

Therefore Theorem 4.1 yields

\[
\boxed{U\equiv0.}
\]

In particular, at `rho=1` (`tau=-1` in the normalized RG time),

\[
\boxed{
V=\mathscr R_1(T)=0.
}
\]

---

## 9. Contradiction with the W1 nontriviality witness

The W1/alpha-limit construction retained a nonzero normalized vorticity witness in a fixed similarity ball. In the checkpoint version,

\[
|\Omega_V(\xi_*,s_*)|
\ge c_*>0
\]

for a suitable recurrent/checkpoint state.

Thus

\[
V\not\equiv0.
\]

Section 8 gives the opposite conclusion.

Therefore

\[
\boxed{
\text{nonzero complete realized W1 branch with the audited spatial Type-I bound and terminal trace is empty.}
}
\]

This closes both of the former tail alternatives at once:

\[
\boxed{
S_{crit}^{nonhom}=\varnothing,
\qquad
R_{tail}=\varnothing
}
\]

**within the spatial-Type-I realized W1 corridor**.

M5-268 remains a valid independent stationary-subbranch audit, but is no longer needed for closure once the stronger ancient-solution theorem is invoked.

---

## 10. Why this does not solve the open RSS/RDSS problem

The conclusion must not be misread as a general theorem excluding every Type-I RSS/RDSS/aperiodic ancient solution.

The decisive extra project input is M5-269:

\[
\boxed{
\text{the global-RG ancient solution possesses an actual critical terminal trace }T
\text{ in distributions.}
}
\]

A genuinely rotating or nonconvergent ancient Type-I solution may fail to have any terminal distributional trace at `t=0`; its similarity phase can keep rotating/oscillating as the terminal time is approached.

Albritton--Barker Theorem 4.1 cannot be applied by inserting an invented terminal trace.

Thus there is no conflict with the still-open general rotated-self-similar problem discussed by Pineau--Vicol.

---

## 11. What remains in the project proof tree

The closure is conditional on reaching the **complete realized spatial-Type-I W1 corridor**.

The remaining proof obligations lie earlier in the tree, namely branches where one of the inputs needed to reach that corridor fails. These include, according to the existing audits:

1. scale-critical annular derivative escape:
   \[
   H_{1,crit}^{tail}
   \quad\text{or}\quad
   H_{2,crit}^{tail};
   \]
2. material/center/replacement turnover `T` outside the bounded-center corridor;
3. failure of the centered Morrey/local-energy compactness needed for the W1 extraction;
4. any pressure/local-energy compatibility failure not already absorbed by the existing pressure bridge;
5. any earlier `H` roughness/derivative branch excluded from the smooth compact corridor.

The hard tail dynamics no longer need to be split into stationary, DSS, or aperiodic residual-active subbranches once the terminal-trace Liouville theorem is available.

---

## 12. DSD verdict

### EXTERNAL THEOREM MATCH — GREEN

Albritton--Barker Theorem 4.1 applies exactly to the global-RG ancient solution produced by M5-274, provided the previously audited global spatial-Type-I and terminal-trace hypotheses are retained.

### CLOSED

\[
\boxed{
\text{complete realized nonzero W1 branch on the spatial-Type-I corridor}.}
\]

### NOT CLOSED

The precompactness / derivative / turnover escape branches that prevent construction of that corridor.

### GLOBAL STATUS

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]

The project should now move back one level in the proof tree and close the explicit pre-W1 escape branches rather than continue classifying the now-excluded residual-active minimal tail.
