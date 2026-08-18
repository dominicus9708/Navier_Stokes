# Frontier: heterochiral radial-stack / same-scale nonlocal strain wall

Date: 2026-08-18

Overall status: **THE EXHAUSTIVE FIRST-HITTING I/V MAP REMAINS INTACT. THE COMPACT/NATURAL-SCALE LANE HAS BEEN FURTHER REDUCED: DIRECTIONAL ROUGHNESS IS DIRECTLY VISCOUSLY DAMPED IN THE EXACT VORTICITY-MAGNITUDE EQUATION; PROJECTIVE ISOTROPY DEPLETES AFFINE PRODUCTION; A COMMON MESOSCOPIC STRAIN EXTRACTS A SIGNED COHERENT SUBPOPULATION; POSITIVE STRETCHING REQUIRES POSITIVE MIDDLE STRAIN OR BETCHOV COMPENSATION WITHOUT ANY ALIGNMENT ASSUMPTION; PURE HOMOCHIRAL OR PURE SAME-RADIUS ANGULAR INTERACTIONS CANNOT GROW THE POSITIVE H^(1/2) CRITICAL CHARGE. A BOUNDED-PER-BAND BLOW-UP MUST THEREFORE BUILD AN UNBOUNDED SIMULTANEOUS RADIAL STACK OF HETEROCHIRAL, RADIALLY TRANSFERRING, SAME-SCALE NONLOCAL STRAIN NETWORKS. GLOBAL REGULARITY NOT PROVED.**

---

## 1. Exhaustive outer map

Assume a finite maximal smooth time.  First hitting produces

\[
W_j=\|\omega(t_j)\|_\infty\to\infty.
\]

The exact Cauchy-defect decomposition gives the top-level causal split

\[
\boxed{
\text{I: material/deformation amplification}
\quad\lor\quad
\text{V: viscous Cauchy rewriting}.
}
\]

The bounded-condition residual asymptotics still split into

\[
\boxed{m_j\to0}
\]

(the large-radius coherent lane) or

\[
\boxed{m_j\ge m_0>0}
\]

(the compact/natural-scale non-affine lane).

The present frontier concerns the second lane after the large-scale/coherent escapes have already been routed.

---

## 2. Exact magnitude-direction damping

Write

\[
\Omega=\rho\xi,
\qquad\rho=|\Omega|.
\]

Exactly,

\[
\boxed{
(\partial_t+U\cdot\nabla-\nu\Delta)\rho
=
\rho\left(\xi^TS\xi-\nu|\nabla\xi|^2\right).
}
\]

and

\[
\boxed{
(\partial_t+U\cdot\nabla-\nu\Delta)\frac{\rho^2}{2}
=
\rho^2\xi^TS\xi
-\nu|\nabla\rho|^2
-\nu\rho^2|\nabla\xi|^2.
}
\]

Using the exact terminal adjoint kernel `K`, define

\[
E_K=\int K\rho^2,
\quad
P_{\rm mag,K}=\int K|\nabla\rho|^2,
\quad
P_{\rm ang,K}=\int K\rho^2|\nabla\xi|^2.
\]

Then

\[
\boxed{
\frac12E_K'
+\nu P_{\rm mag,K}
+\nu P_{\rm ang,K}
=Q_K,
}
\]

with no cutoff or transport-error terms.

From a `q`-earlier first-hitting cap to terminal unit vorticity,

\[
\boxed{
\int Q_Kds
\ge
\frac12(1-q^{-2})
+\nu\int P_{\rm ang,K}ds.
}
\]

Thus angular roughness is a direct magnitude loss that must be repaid by stretching.

---

## 3. Projective disorder hurts both source and damping

Define

\[
C_K
=\frac{\int K\Omega\otimes\Omega}{E_K},
\qquad
J_K=1-\operatorname{tr}(C_K^2),
\qquad
0\le J_K\le2/3.
\]

Let

\[
\bar S_K=\int KS,
\qquad
V_{S,K}=\int K|S-\bar S_K|^2.
\]

Then exactly

\[
\boxed{
Q_K
\le
E_K|\bar S_K|_F
\sqrt{\frac23-J_K}
+\sqrt{E_KV_{S,K}}.
}
\]

Hence projective isotropy `J_K -> 2/3` eliminates affine production.

On a thick bounded-condition unit cell, weighted projective Poincare gives schematically

\[
P_{\rm ang,K}\gtrsim E_KJ_K.
\]

Therefore

\[
\boxed{
\frac12E_K'
+c\nu E_KJ_K
\lesssim
E_K|\bar S_K|_F\sqrt{\frac23-J_K}
+\sqrt{E_KV_{S,K}}.
}
\]

For fixed affine strain and small residual strain, source efficiency is strictly decreasing in `J_K`; the scalar-minimal state is driven toward projective coherence.

---

## 4. Common strain extracts a signed coherent subpopulation

For packet energy weights `e_i` and unit directions `xi_i`, define

\[
C_{\rm ens}=\sum_iw_i\xi_i\otimes\xi_i.
\]

A common trace-free mesoscopic strain satisfies

\[
Q_{\rm common}
=E\operatorname{tr}(S_LC_{\rm ens})
\]

and therefore

\[
\boxed{
|Q_{\rm common}|
\le
E|S_L|_F
\left\|C_{\rm ens}-\frac13I\right\|_F.
}
\]

If it supplies a fixed fraction `alpha` of generic source efficiency, then

\[
\operatorname{tr}(C_{\rm ens}^2)
\ge
\frac13+\alpha^2
\]

and a fixed energy fraction lies in one projective cone.  Splitting orientation gives a fixed signed-cone subpopulation.

Hence a common lower-frequency amplifier automatically returns a fixed packet fraction to signed coherent geometry.

Avoiding this extraction forces the responsible strain to vary from packet to packet; the finite-energy sampling bound then pushes its frequency toward the packet frequency.

---

## 5. Positive stretching needs middle strain or Betchov compensation

At every point with

\[
q=\omega\cdot S\omega>0,
\]

no vorticity/eigenvector alignment assumption is necessary.

If

\[
\lambda_2>0,
\]

we are in the positive-middle-strain branch.

If

\[
\lambda_2\le0,
\]

then trace-free ordering gives

\[
\det S\ge0
\]

and hence

\[
\boxed{
q+4\det S\ge q>0.
}
\]

The local Betchov divergence identity then forces buffer strain-energy, buffer palinstrophy/Hessian, or residual-shape compensation.

Thus misalignment does not provide a third source-active lane.

---

## 6. Exact three-defect compact state

The local Gaussian residual decomposition is

\[
\boxed{
B
=V_S
+\frac12D_{\rm proj}
+\frac12D_{\rm line}.
}
\]

Therefore:

- large `D_proj` -> angular/projective damping and regeneration;
- large `D_line` -> polarity/magnitude-gradient/flux-reset branch;
- both small -> vorticity is close to one constant signed vector;
- if `V_S` is also small -> signed-coherent affine state, already routed through positive-middle strain / Betchov compensation.

Thus the distinct compact residual is an order-one `V_S` supplied nonlocally by neighboring structures.

A common mesoscopic version creates a coherent cone, so the irreducible residual becomes same-scale high--high nonlocal strain correlation.

---

## 7. Helical-sign requirement

Use the helical decomposition

\[
u=u^++u^-,
\qquad
\nabla\times u^\pm=\pm\Lambda u^\pm.
\]

Define

\[
H_\pm=\|\Lambda^{1/2}u^\pm\|_2^2.
\]

Then

\[
H_+-H_-
=\int u\cdot\omega,
\qquad
H_++H_-
=\|u\|_{\dot H^{1/2}}^2.
\]

Pure `+++` and `---` nonlinear contributions to `H_++H_-` vanish by inviscid helicity conservation. Therefore

\[
\boxed{
\frac12\frac d{dt}\|u\|_{\dot H^{1/2}}^2
+\nu\|u\|_{\dot H^{3/2}}^2
=\mathcal T_{\rm het},
}
\]

where `T_het` consists only of mixed-helicity interactions.

On a fixed normalized shell,

\[
|\mathcal T_{\rm het}|
\lesssim
A_+A_-(A_++A_-).
\]

Hence a generic-size same-shell critical source requires a non-negligible minority helicity sector.

---

## 8. Radial transfer is mandatory

For a narrow annulus centered at frequency `K`, shell critical charge and shell enstrophy equal `K` and `K^2` times shell kinetic energy up to `O(delta)` radial-spread errors.

Thus pure angular redistribution on an exact frequency sphere cannot change either quantity.

Globally, define the high-frequency kinetic-energy tail

\[
\mathcal E_{>K}
=\frac12\int_{|\xi|>K}|\hat u|^2.
\]

Then exactly

\[
\boxed{
\frac12\|u\|_{\dot H^{1/2}}^2
=\int_0^\infty\mathcal E_{>K}dK,
}
\]

\[
\boxed{
\frac12\|\omega\|_2^2
=\int_0^\infty2K\mathcal E_{>K}dK.
}
\]

If `Pi_E(K)` denotes net nonlinear kinetic-energy flux to frequencies above `K`, then

\[
\boxed{
\mathcal T_{1/2}
=\int_0^\infty\Pi_E(K)dK,
}
\]

\[
\boxed{
Q
=\int_0^\infty2K\Pi_E(K)dK.
}
\]

Thus critical growth and enstrophy production require genuine radial kinetic-energy transfer.

The irreducible spectral motif must therefore be both heterochiral and radially transferring.

---

## 9. Known hybrid vorticity-direction criterion is exactly saturated

The local Grujic--Guberovic hybrid criterion contains the critical special case

\[
\int\!\int
(\rho_{1/2,r}|\omega|)^2dxdt<\infty.
\]

For a natural physical packet at frequency `K`, critical directional roughness has

\[
\rho_{1/2,r}\sim K^{1/2},
\qquad
|\omega|\sim K^2,
\qquad
r\sim K^{-1},
\qquad
\Delta t\sim K^{-2}.
\]

One packet therefore contributes order one to the criterion over one natural block.  A family of `N` simultaneous critically rough packets contributes order `N` under bounded overlap.

Hence the known criterion confirms that the DSD unit cell sits exactly on the geometric-analytic critical boundary; it does not automatically close the branch.

---

## 10. Critical-space gate forces simultaneous radial-scale multiplicity

Known critical-space regularity theory implies that bounded `dot H^(1/2)` prevents finite-time singularity.

Since

\[
\|u\|_{\dot H^{1/2}}^2
\asymp
\sum_k\mathfrak h_k,
\]

a bounded-per-band unit-cell scenario cannot blow up by moving only one order-one band to higher frequency.  It must either

\[
\boxed{
\text{make an individual band charge diverge}
}
\]

or

\[
\boxed{
M(t)\to\infty
}
\]

where `M(t)` is the number of simultaneously active radial critical bands.

The first is a stronger amplitude/derivative branch.  Thus the minimal bounded-amplitude scenario is an unbounded simultaneous radial stack.

---

## 11. Parabolic Zeno timing still survives

Under the first-hitting vorticity cap, a frequency-`K` band has velocity amplitude at most `O(K)` and turnover rate at most `O(K^2)`.  Hence an order-one bounded-channel repopulation needs at least

\[
\Delta t_K\gtrsim cK^{-2}.
\]

But for a geometric sequence `K_j`,

\[
\sum_jK_j^{-2}<\infty.
\]

Therefore temporal noncollapse at each individual scale still permits a finite-time parabolic Zeno stack.

---

## 12. Current irreducible wall

After the present reductions, the bounded-amplitude compact singular motif must simultaneously realize

\[
\boxed{
\begin{gathered}
\text{unbounded simultaneous radial-scale multiplicity},\\
\text{positive radial kinetic-energy flux},\\
\text{heterochiral mixing},\\
\text{packet-scale nonlocal strain--vorticity correlation},\\
\text{quantitative projective anisotropy without excessive angular damping},\\
\text{signed-line organization or paid polarity/magnitude defects},\\
\text{positive-middle strain or local Betchov compensation}.
\end{gathered}
}
\]

A common mesoscopic amplifier collapses a fixed fraction back to the coherent geometry already studied.  Avoiding that forces packet-dependent same-scale strain and hence the full high--high network above.

No current positive global budget excludes this organized critical network.  At natural rescaling, every term is order one and no scale power remains.  This is a genuine form of the unresolved three-dimensional critical Navier--Stokes dynamics.

Overall status: **COMPACT UNIT-CELL WALL SHARPENED TO AN UNBOUNDED SIMULTANEOUS HETEROCHIRAL RADIAL-TRANSFER STACK WITH PROJECTIVE/SIGNED PHYSICAL-SPACE ORGANIZATION / KNOWN GEOMETRIC AND CRITICAL-SPACE CRITERIA ARE SATURATED, NOT VIOLATED / GLOBAL REGULARITY NOT PROVED.**