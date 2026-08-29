# DSD M5-267 — Descendant-Radius Scaling Correction for M5-261--266

Date: 2026-08-30

Parent: `DSD_M5_266_VISCOUS_PRESSURE_MOMENTUM_FORCE_TO_DERIVATIVE_RESERVOIRS_2026-08-30.md`

Status: **MANDATORY SCOPE CORRECTION / THE ALGEBRAIC IDENTITIES IN M5-261--266 ARE VALID, BUT THEIR PRESENTATION OVERSTATED THE UNCONDITIONAL ROUTING OF THE STATIONARY TAIL INTO SMALL-BALL MEAN/MOMENTUM TURNOVER / M5-248 MAPS A TAIL UNIT CELL AT SHALLOW RG DEPTH `rho_*` TO A FIXED BUT GENERALLY LARGE W1 ANNULUS OF RADIUS `R_*=rho_*^-1/2`; THERE IS NO CURRENT PROOF THAT `R_* < pi sqrt(nu)`, SO THE M5-262 POINCARE-SIGN GATE MAY NOT APPLY TO THE INHERITED TAIL CURRENT / ALL CONSEQUENCES DEPENDING ON THAT SMALL-RADIUS SIGN MUST BE READ AS CONDITIONAL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact M5-248 scaling

M5-248 gives

\[
\rho_*=e^{-h_*},
\qquad
R_*=e^{h_*/2}=\rho_*^{-1/2},
\]

and

\[
\boxed{
\mathscr R_{\rho_*}(T_V)(Y)
=
R_*\,(S(h_*)V)(R_*Y).
}
\]

Thus a certificate on a **unit tail/RG cell** becomes a certificate for the actual W1 state `S(h_*)V` on the finite annulus

\[
\boxed{R_*K.}
\]

The radius is finite but, because `rho_*` is chosen small to stay close to the tail,

\[
\boxed{R_*\text{ is generally large}.}
\]

---

## 2. The M5-262 small-ball gate

M5-262 proved the exact local Leray identity

\[
E_R'+\nu D_R+\mathfrak J_R+\frac R4S_R-\frac12E_R=0.
\]

It then used ball Poincare to obtain

\[
\frac{M_R}{4}\langle|m_R|^2\rangle
\ge
\langle\mathfrak J_R\rangle
+
\left(\nu-\frac{R^2}{\pi^2}\right)\langle D_R\rangle
+
\frac R4\langle S_R\rangle.
\]

The clean mean floor follows only if

\[
\boxed{R<\pi\sqrt\nu.}
\]

This implication is mathematically correct.

What was not justified is the silent substitution

\[
R=R_*
\]

while assuming that the inequality remains in the favorable range.

---

## 3. Shallow RG works in the opposite radius direction

Tail approximation improves as

\[
\rho_*\downarrow0.
\]

But then

\[
R_*=\rho_*^{-1/2}\uparrow\infty.
\]

Therefore there is an inherent tension:

\[
\boxed{
\text{stronger guaranteed tail closeness}
\Longleftrightarrow
\text{larger actual W1 radius}.
}
\]

The small-ball Poincare dominance is not supplied for free by the RG bridge.

---

## 4. Why choosing a smaller tail subcell does not automatically fix this

One might choose a tail cell `K` centered at a small tail radius `r_K<<1`. Its W1 descendant radius is

\[
R_*r_K.
\]

However the uniform RG-continuity constant on that punctured cell can worsen as `r_K->0`, because the canonical tail is singular at the puncture.

To guarantee tail closeness on `K`, one may need

\[
\rho_*\ll r_K^2,
\]

which gives

\[
R_*r_K
=\frac{r_K}{\sqrt{\rho_*}}
\gg1.
\]

No uniform estimate has yet been proved allowing

\[
R_*r_K<\pi\sqrt\nu
\]

while retaining the required reconstruction closeness.

Thus the apparent small-radius shortcut is RED without a new scale-uniform RG estimate near the puncture.

---

## 5. Correct status of M5-261

M5-261 correctly establishes:

1. a nonzero compact minimal stationary tail has a uniform positive **scale-normalized** energy-current certificate;
2. the certificate can be transferred through one fixed RG depth to a finite W1 annulus;
3. it can then be transferred to finite first-hitting stages on a fixed normalized annulus.

What it does **not** establish is that the inherited annulus lies inside a small-ball regime where local anti-damping is dominated by Poincare viscosity.

Therefore the correct unconditional statement is

\[
\boxed{
S_{crit}^{stationary}
\Longrightarrow
\text{positive finite-radius W1/finite-stage energy-current certificate}.
}

The later turnover routing requires additional radius/coercivity input.

---

## 6. Correct status of M5-262

The exact local energy identity and conditional gate remain valid:

\[
\boxed{
R<\pi\sqrt\nu
\quad\Longrightarrow\quad
\text{positive current forces a mean-drift floor}.
}

But this is now labeled

\[
\boxed{\text{SMALL-RADIUS DESCENDANT SUBBRANCH}.}
\]

It is not an unconditional property of the inherited stationary tail.

---

## 7. Correct status of M5-263--266

M5-263--266 are valid **conditional reductions once the M5-262 mean floor is available**:

\[
\text{mean drift}
\to
T_{mom-stress}\lor T_{rel-trace},
\]

and

\[
T_{mom}
\to
D_{rel/local}\lor H2_{local}\lor H1_{global}.
\]

They do not by themselves show

\[
S_{crit}^{stationary}
\to
D/H/T
\]

on the general fixed-depth descendant radius.

All earlier wording suggesting that the entire stationary endpoint had already been routed through these branches is superseded by this correction.

---

## 8. Correct general-radius local balance

At the actual inherited radius `R_*`, invariant averaging gives only

\[
\boxed{
\nu\langle D_{R_*}\rangle
+\langle\mathfrak J_{R_*}\rangle
+\frac{R_*}{4}\langle S_{R_*}\rangle
=
\frac12\langle E_{R_*}\rangle.
}
\]

For large `R_*`, the local kinetic anti-damping reservoir is naturally of critical-tail size

\[
E_{R_*}\sim R_*,
\]

while the physical stationary energy current scales like

\[
\mathfrak J_{R_*}\sim R_*^{-1}.
\]

Therefore there is no scale contradiction:

\[
\boxed{
R_*^{-1}\ll R_*
\qquad(R_*\gg1).
}

This is exactly compatible with the critical `1/r` tail.

---

## 9. Why the stationary flux result remains valuable

M5-260 is not weakened. It gives the exact scale-normalized tail identity

\[
\mathcal B_r
=
\nu\left\langle
|\Phi_y|^2+|\nabla_S\Phi|^2
\right\rangle>0.
\]

The correction concerns only how that certificate is interpreted after descendant scaling.

The remaining challenge is to find a **scale-invariant** finite-radius coercivity or turnover functional, rather than a small-Euclidean-radius Poincare argument whose sign deteriorates like `R^2`.

---

## 10. Revised stationary frontier

The honest general stationary endpoint is now

\[
\boxed{
\begin{aligned}
S_{crit}^{stationary}
\Longrightarrow{}&
\text{fixed-force, zero-torque stationary critical tail}\\
&+\text{positive scale-phase residue}\\
&+\text{strict positive scale-normalized Bernoulli/energy flux}\\
&+\text{fixed-force dilation zero-mode}\\
&+\text{large-critical coefficient requirement},
\end{aligned}
}

with the positive flux inherited to one fixed **large but finite** W1 annulus.

The small-radius turnover chain M5-262--266 remains available only if a future estimate brings the descendant certificate into `R<pi sqrt(nu)` or supplies an annular analogue with scale-invariant coercivity.

---

## 11. Next target

The correct replacement for the failed small-ball shortcut is an **annular scale-invariant relative Poincare/Hardy energy identity** on the large descendant annulus `R_*K`.

The target should preserve the critical normalization under

\[
Y=R_*z
\]

so that viscosity and the stationary energy-current certificate are compared in the same units and no `R_*^2` loss is introduced.

A natural candidate is to subtract the canonical `1/r` radial mode or use a logarithmic-annulus energy in `y=log r`, where M5-260 already has a scale-invariant positive identity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
