# DSD M5-190 — Scale-Local Convex-Bump Divergence-Source Carleman and Critical Stokes Coercivity

Date: 2026-08-28

Status: **CRITICAL LOG-ANNULUS DIVERGENCE-SOURCE CARLEMAN: GREEN / LOCAL PRESSURE-COMPATIBLE CRITICAL STOKES COERCIVITY: GREEN / TERMINAL-BACKWARD PROPAGATION ACROSS TIME: OPEN / THE LIN–WANG DIVERGENCE-SOURCE CARLEMAN PROOF CAN BE REUSED AT THE CRITICAL ENDPOINT ON EACH FIXED-WIDTH LOGARITHMIC ANNULUS BY REPLACING THE SUBCRITICAL GLOBAL WEIGHT WITH A SCALE-LOCAL CONVEX-BUMP PHASE SATISFYING `psi' ~ beta` AND `psi'' ~ beta` THROUGHOUT THE SUPPORT / GLOBAL REGULARITY UNPROVED.**

---

## 1. The M5-189 open lemma

M5-189 reduced the pressure/Stokes part to a single endpoint estimate for

\[
\partial_t\eta-\nu\Delta\eta+\nabla\cdot F=0,
\]

with the critical tensor bound

\[
\boxed{
|F|\le C\left(r^{-1}|\nabla Z|+r^{-2}|Z|\right),
\qquad r=|x-x_*|.
}
\]

The missing point was to control `div F` without differentiating `F`, while retaining the weighted gradient coercivity needed for the elliptic Stokes recovery.

Abstract `H^{-1}` duality alone gives a weaker norm and is therefore not enough to close M5-189 in the required form.

---

## 2. What Lin–Wang Lemma 2.3 actually provides

For a scalar `w` and vector source `f`, their divergence-source Carleman estimate has the structural form

\[
\boxed{
\begin{aligned}
&\iint \varphi^2(1+\psi'')
\left(r^4|\nabla(\chi w)|^2+\beta^2r^2|\chi w|^2\right)\\
&\quad\lesssim
\iint\varphi^2r^2
\left(\chi r^2\Delta w-\chi r^2\partial_tw+r\,\operatorname{div}f\right)^2\\
&\qquad+
\beta^2\iint\varphi^2r^2|f|^2
+
\iint\varphi^2r^6|\chi' w|^2.
\end{aligned}}
\]

The important fact is that the source appears as `f` itself in the second term.  No derivative of `f` is paid there.

Their proof is carried out after `y=-log r` and uses the phase through the coercive conditions

\[
\boxed{
\frac12\beta\le\psi'\le2\beta,
\qquad
\operatorname{dist}(2\psi',\mathbb Z)+\psi''\gtrsim1.
}
\]

The separate subcritical relation

\[
C\beta r^\varepsilon\le1+\psi''
\]

is used later when the Stokes lower-order coefficients are absorbed; it is not the source mechanism of Lemma 2.3 itself.

This distinction is essential at `epsilon=0`.

---

## 3. Fixed-width logarithmic annulus

Fix once and for all a logarithmic half-width

\[
L>1.
\]

For each large centre `Y`, define the target annulus in `y=-log r` by

\[
I_Y=[Y-L,Y+L].
\]

Use an enlarged interval

\[
I_Y^+=[Y-L-1,Y+L+1]
\]

which contains the support of all spatial cutoffs used in the local Carleman argument.

Choose a smooth function `h` independent of `Y` such that on `[-L-1,L+1]`

\[
\boxed{
|h'|\le\frac14,
\qquad
h''\ge c_L>0,
}
\]

where, for example, `c_L` may be chosen smaller than `1/[16(L+1)]` and the function smoothly flattened outside a slightly larger interval.

Now set

\[
\boxed{
\psi_{Y,\beta}(y)
:=
\beta y+\beta h(y-Y).
}
\]

On `I_Y^+`,

\[
\boxed{
\frac34\beta\le\psi'_{Y,\beta}\le\frac54\beta,
\qquad
\psi''_{Y,\beta}\ge c_L\beta.
}
\]

Hence, for `beta >= beta_L`,

\[
\boxed{
\frac12\beta\le\psi'\le2\beta,
\qquad
\operatorname{dist}(2\psi',\mathbb Z)+\psi''\ge1
}
\]

throughout the support of the unknown and its cutoffs.

The resonance-separation part of the original weight is therefore unnecessary on this localized support: the positive convexity `psi'' ~ beta` already supplies the coercivity.

---

## 4. Uniformity under radial scale translation

The phase is translated only in `y`:

\[
Y\mapsto Y+c.
\]

After the parabolic rescaling

\[
x-x_*=R X,
\qquad
t-T_*=R^2T,
\qquad R=e^{-Y},
\]

a fixed-width logarithmic annulus becomes a fixed unit annulus in `X`.

The critical coefficient classes

\[
r^{-1}\nabla,
\qquad r^{-2}
\]

are invariant under exactly this rescaling.

Therefore all constants in the localized Carleman estimate may be chosen independent of the annulus centre `Y`.

They depend only on

- dimension;
- viscosity;
- the fixed width `L`;
- the fixed shape of the cutoff;
- the critical coefficient ceiling.

This uniformity is what will be needed in any later scale iteration.

---

## 5. Critical divergence-source estimate

Apply the Lin–Wang polar-coordinate proof with the phase `psi_{Y,beta}`.

Because `1+psi'' ~_L beta` on the full spatial support, the left-hand side becomes

\[
\boxed{
\beta\iint\varphi^2r^4|\nabla(\chi w)|^2
+
\beta^3\iint\varphi^2r^2|\chi w|^2.
}
\]

Now suppose

\[
\partial_tw-\nu\Delta w+\operatorname{div}F=0.
\]

For simplicity normalize viscosity by parabolic rescaling in the proof; restoring `nu` only changes fixed constants.

Choose the source in Lemma 2.3 as

\[
\boxed{f=\chi rF}
\]

componentwise.

Then

\[
r\operatorname{div}(\chi rF)
=
\chi r^2\operatorname{div}F
+
\chi r\,\hat r\cdot F
+
\text{spatial-cutoff terms}.
\]

The first term cancels the equation residual.

The extra radial derivative of `r` contributes only

\[
O(r|F|)
\]

inside the squared residual and is subordinate to the explicit source term below.

The main source norm is

\[
\beta^2\iint\varphi^2r^2|f|^2
=
\boxed{
\beta^2\iint\varphi^2r^4|F|^2.
}
\]

Thus the localized endpoint estimate is

\[
\boxed{
\begin{aligned}
&\beta\iint\varphi^2r^4|\nabla(\chi w)|^2
+
\beta^3\iint\varphi^2r^2|\chi w|^2\\
&\qquad\lesssim_L
\beta^2\iint\varphi^2r^4|F|^2
+
\text{time/spatial cutoff errors}.
\end{aligned}}
\]

This is exactly the M5-189 missing divergence-source scaling.

No derivative of `F` is required.

---

## 6. Vector vorticity version

The heat principal part is diagonal in the components of `eta`.

Apply Section 5 to each component of

\[
\partial_t\eta-\nu\Delta\eta+\nabla\cdot F=0
\]

and sum.

We obtain

\[
\boxed{
\begin{aligned}
&\beta\iint\varphi^2r^4|\nabla\eta|^2
+
\beta^3\iint\varphi^2r^2|\eta|^2\\
&\qquad\lesssim
\beta^2\iint\varphi^2r^4|F|^2
+
\text{cutoff errors}.
\end{aligned}}
\]

This closes the parabolic half of M5-189 locally on every fixed-width logarithmic annulus.

---

## 7. Matching elliptic Stokes recovery

The same phase satisfies the hypotheses used in the matching singular elliptic Carleman argument.

For

\[
-\Delta Z=\nabla\times\eta,
\qquad\nabla\cdot Z=0,
\]

the localized estimate gives

\[
\boxed{
\beta^2\iint\varphi^2r^2|\nabla Z|^2
+
\beta^4\iint\varphi^2|Z|^2
\lesssim
\beta\iint\varphi^2r^4|\nabla\eta|^2
+
\text{cutoff errors}.
}
\]

The constants are again uniform in `Y`.

---

## 8. Critical Oseen/Stokes absorption

For the W1 relative system,

\[
|F|^2
\lesssim
r^{-2}|\nabla Z|^2+r^{-4}|Z|^2.
\]

Therefore

\[
\beta^2\iint\varphi^2r^4|F|^2
\lesssim
\boxed{
\beta^2\iint\varphi^2r^2|\nabla Z|^2
+
\beta^2\iint\varphi^2|Z|^2.
}
\]

The first term is absorbed by the elliptic gradient channel.

The second is absorbed by the elliptic zeroth-order channel

\[
\beta^4\int\varphi^2|Z|^2
\]

for sufficiently large `beta`.

After a fixed linear combination of the parabolic and elliptic estimates,

\[
\boxed{
\begin{aligned}
&\beta\int\varphi^2r^4|\nabla\eta|^2
+\beta^3\int\varphi^2r^2|\eta|^2\\
&\quad+
\beta^2\int\varphi^2r^2|\nabla Z|^2
+\beta^4\int\varphi^2|Z|^2\\
&\qquad\lesssim
\text{spatial/time cutoff errors only}.
\end{aligned}}
\]

Thus the **local pressure-compatible critical Stokes coercivity is GREEN**.

There is no remaining critical power-counting or divergence-source obstruction.

---

## 9. What is still open

The estimate is localized in both radial scale and time.

It does not by itself prove

\[
Z(\cdot,T_*)=0
\Longrightarrow
Z\equiv0\quad(t<T_*).
\]

The remaining obligation is no longer pressure or critical coefficient absorption.

It is:

\[
\boxed{
\text{terminal-backward localization / scale-time propagation with cutoff errors.}
}
\]

In particular, one must choose time cutoffs and radial scale iteration so that the error regions are ordered forward in the proof and do not silently import the desired past vanishing.

---

## 10. DSD four-chain audit

### Formation — GREEN

The phase is formed on the actual support of a fixed-width logarithmic annulus.  No global weight behavior is claimed outside the region where the unknown/cutoffs live.

### Axis — GREEN

Radial scale translation `Y`, Carleman strength `beta`, and physical time localization remain independent parameters.

### Static aggregation — GREEN

`F` is counted once through the divergence-source Carleman source norm.  The elliptic velocity estimate is then used only for absorption; it is not counted as a second physical cost.

### Dynamics — GREEN locally / OPEN terminal-backward

The local endpoint coercivity is uniform in radial scale.  No backward propagation in time is inferred yet.

### Cross-audit — GREEN

- no `epsilon -> 0` limit of the published subcritical theorem is taken;
- no derivative of `F` is assumed;
- no global log-square phase with uncontrolled `psi'` is inserted into the Lin–Wang spectral proof;
- no spatial unique-continuation result is relabeled as backward uniqueness.

---

## 11. Updated major-gate status

The first major gate is now

\[
\boxed{
\begin{aligned}
\text{critical Oseen--Stokes backward Carleman}
={}&\underbrace{\text{critical drift/potential absorption}}_{\text{M5-188 GREEN}}\\
&+\underbrace{\text{divergence-source pressure bridge}}_{\text{M5-190 GREEN, local}}\\
&+\underbrace{\text{elliptic Stokes recovery}}_{\text{M5-190 GREEN, local}}\\
&+\underbrace{\text{terminal-backward localization}}_{\text{ONLY OPEN SUBGATE}}.
\end{aligned}}
\]

The next calculation should therefore stop modifying the spatial singular weight and instead solve the **time-cutoff / backward propagation** problem using the now-uniform log-annulus coercivity.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
