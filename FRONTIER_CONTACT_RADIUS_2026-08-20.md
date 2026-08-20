# Contact/Radius Endgame Frontier — 2026-08-20

Overall status: **ACTIVE DSD-ASSISTED 3D NAVIER--STOKES PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This frontier records the reductions obtained after `FRONTIER_VARIATIONAL_ENDGAME_2026-08-20.md`: H1 Helmholtz rigidity of the KKT contact reaction, first-hitting analytic smoothing, elimination of the effective singular contact reaction on the non-H/T threshold core, the explicit vorticity rms-radius threshold constant, and the corresponding similarity-scale compactness of ancient threshold times.

---

## 1. Contact reaction no longer survives smooth non-H/T first-hitting cores

Let the active `L^infinity` KKT multiplier be `mu`, supported on

\[
\mathcal M=\{|\omega|=1\}.
\]

Only

\[
f=P_{df}\mu
\]

is visible to strain variations. The strain-vorticity transform satisfies

\[
\mathcal B\mathcal B^*=2P_{df}.
\]

Thus if the KKT Euler field is `F(S)=B^*mu`,

\[
\mathcal BF(S)=2f.
\]

For a nonzero finite-energy analytic snapshot, `|M|=0`. If `f in H^1`, then on the complement of `M` the Helmholtz decomposition gives `f=-grad phi`, so `curl f=0` there. Since `curl f in L^2`, it cannot be supported only on a measure-zero set, hence `curl f=0` globally. Together with `div f=0` and `f in L^2`, this implies

\[
\boxed{f=0.}
\]

Therefore an active contact reaction requires failure of H1 regularity of the visible reaction field, i.e. a higher-derivative escape.

---

## 2. First-hitting analyticity supplies the missing local regularity

At a first-hitting time `t_j`, restart the smooth solution at

\[
t_j^-=t_j-\theta/W_j,
\qquad
W_j=\|\omega(t_j)\|_\infty.
\]

Since the first-hitting property gives

\[
\|\omega(t_j^-)\|_\infty\le W_j,
\]

standard vorticity analyticity theory provides an analytic time interval of size `c/W_j` and spatial analyticity radius `~sqrt(theta/W_j)`.

In the normalized coordinates `r_j=W_j^{-1/2}`, this becomes a uniform order-one analyticity strip. Cauchy estimates give uniform local bounds on every fixed spatial derivative of normalized vorticity. On the non-T Type-I tower, local energy plus the elliptic relation between velocity, strain, and vorticity transfers this to local high Sobolev bounds for the strain on every fixed threshold-core parent ball.

Hence the effective contact reaction is locally H1 across its support, and the previous Helmholtz rigidity applies.

Thus on the non-H/T threshold core,

\[
\boxed{P_{df}\mu=0,\qquad \Gamma_K=0.}
\]

The first-hitting maximum set may remain geometrically present, but it is variationally invisible.

---

## 3. Smooth confined variational system

The KKT-corrected Pohozaev identities

\[
\alpha E=(N-5\Gamma_K)/4,
\qquad
\beta M=(N+3\Gamma_K)/4
\]

therefore reduce to

\[
\boxed{\alpha E=\beta M=N/4.}
\]

The remaining non-H/T local threshold profile must satisfy

\[
\boxed{
P_{st}[\mathcal E_N
-2\Lambda\Delta^2S
-2\alpha S
-2\beta|x|^2S]=0,
}
\]

with

\[
\Lambda=\frac{N}{\|\Delta S\|_2^2}\ge\nu.
\]

Thus the singular-measure KKT problem has been reduced to a smooth confined fourth-order strain-compatible variational problem.

---

## 4. Explicit sharp vorticity rms-radius threshold

Let

\[
Z=\|\omega\|_2^2,
\qquad
M_\omega=\int|x-X|^2|\omega|^2dx,
\qquad
R_\omega^2=M_\omega/Z.
\]

Combining:

- the sharp trace-free H1 production bound;
- the sharp 3D Sobolev constant;
- interpolation between `L2` and `L6` for `grad S`;
- exact strain-vorticity L2 identities;
- the 3D Heisenberg inequality;
- the sharp bathtub lower bound for the second moment of a density bounded by `||omega||_infty^2`;

gives

\[
\boxed{
\eta_{VI}
\le
C_0\|\omega\|_\infty R_\omega^2,
}
\]

where

\[
\boxed{
C_0=\frac{8\sqrt2\,5^{3/4}}{27\sqrt\pi}
\approx0.79048528.
}
\]

Therefore in first-hitting variables `||Omega||_infty=1`,

\[
\boxed{
\eta_{VI}\ge\nu
\Longrightarrow
R_\Omega\ge1.1248\sqrt\nu.
}
\]

For `nu=1`, every threshold core with vorticity rms radius below approximately `1.125` is rigorously subcritical.

---

## 5. Ancient threshold times are self-similar in radius

The restricted ancient limit satisfies

\[
\|\Omega(\tau)\|_\infty\le C_I/|\tau|
\]

for large negative times. Hence every ancient time at which

\[
\eta_{VI}(\tau)\ge\nu
\]

must satisfy

\[
\boxed{
R_\Omega(\tau)
\ge
\sqrt{\frac{\nu}{C_0C_I}}\sqrt{|\tau|}.
}
\]

The non-T Type-I tower supplies the matching upper scale `R_Omega(tau)<=c_+sqrt(|tau|)` along the recurrent active sequence.

Therefore in Leray coordinates

\[
Y=y/\sqrt{|\tau|}
\]

the threshold rms radius remains in a compact annulus

\[
\boxed{
0<r_-\le\widetilde R_\Omega(s_k)\le r_+<\infty.
}
\]

The dangerous active orbit is thus similarity-scale precompact in radius.

---

## 6. Current global picture

The non-H/T ancient survivor now has the form

\[
\boxed{
\text{similarity-scale recurrent active threshold core}
+
\text{global low-vorticity L3-critical passive tail}.
}
\]

The active core is no longer allowed singular KKT contact reaction and must solve the smooth confined threshold variational system. The passive tail remains necessary to evade global ancient L3 Liouville theorems, but the aggregate halo estimate prevents remote tail vorticity from supplying order-one core strain without derivative escape.

Exact backward self-similar and several discretely/asymptotically self-similar profiles are excluded by known Liouville theorems under integrability/local-energy hypotheses. The present survivor still avoids a direct application because its similarity orbit need only be recurrent, not periodic, and its global critical tail may violate the required global integrability.

---

## 7. Next targets

1. Analyze the smooth confined fourth-order threshold equation with `alpha E=beta M=N/4` and seek an additional virial/spectral identity forcing `Lambda<nu`.
2. Improve the radius constant `C0` using strain compatibility, since the present constant uses only trace-free algebra and sharp scalar inequalities, not the full Fourier strain constraint.
3. Quantify tail-core decoupling in Leray variables. If the globally necessary critical tail can be removed by a Galilean/harmonic far-field decomposition on every compact similarity ball, the active recurrent orbit may fall into a stronger local-energy/self-similar Liouville class.
4. If the smooth threshold equation admits nonzero profiles, classify their similarity-scale dynamics and test whether compact recurrence can force a stationary or periodic minimal orbit.

Status: **THE NON-H/T LOCAL P_V BRANCH HAS BEEN REDUCED FROM A SINGULAR KKT CONTACT SYSTEM TO A SMOOTH CONFINED FOURTH-ORDER VARIATIONAL SYSTEM. A VISCOSITY-THRESHOLD CORE MUST HAVE RMS VORTICITY RADIUS AT LEAST 1.1248*SQRT(NU), AND ANCIENT THRESHOLD RECURRENCES ARE PRECOMPACT AT THE SELF-SIMILAR RADIUS SCALE. GLOBAL REGULARITY REMAINS UNPROVED.**