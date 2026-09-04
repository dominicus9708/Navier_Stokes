# DSD M17-099 — Director-area/peak tangency is a curvature resonance and a generic fold has zero net signed flux cost

Date: 2026-09-05
Canonical ID: **M17-099**

Status: **INTERNAL RANK-2 DIRECTOR-AREA/PEAK TANGENCY GATE / M17-097 OBTAINS A CANONICAL PEAK WEIGHT ONLY WHEN `D_k g != 0`, WHILE M17-098 CORRECTLY RETAINS `D_k g=0` AS A GENEALOGY EVENT. THE PRESENT MODULE RESOLVES THE LOCAL GEOMETRY OF THAT EVENT. AT ANY REGULAR PURE-KERNEL LINE PEAK `g=D_xi log rho=0`, WRITE `a=r k` AND `b=p k+q n`. EUCLIDEAN FLATNESS GIVES `D_k g=r(gamma_k-q)` AND `D_k q=-(p/r)D_k g`. THUS TANGENCY IS EXACTLY THE RESONANCE `gamma_k=q`; ON THE FROZEN-ANGLE CLASS `p!=0` IT IS ALSO EQUIVALENT TO `D_k q=0`. IF `D_k^2 g!=0` AND `D_B g!=0`, THE RESTRICTION OF THE PEAK EQUATION TO A FROZEN DIRECTOR-AREA FLUX TUBE HAS THE STANDARD QUADRATIC FOLD NORMAL FORM, SO A PAIR OF TRANSVERSE INTERSECTIONS IS CREATED OR DESTROYED WITH OPPOSITE SIGNS OF `D_k g`. THE UNSIGNED PEAK-INTERSECTION POPULATION CHANGES, BUT THE NET SIGNED DIRECTOR-AREA INTERSECTION FLUX IS ZERO. PERSISTENT SAME-TUBE TANGENCY REQUIRES `D_B g=D_xi(sigma+kappa)=0`; FOR A REGULAR LINE MAXIMUM THIS ALSO FORCES THE XI-DIRECTION PEAK RELATIVE SPEED TO VANISH. AT SUCH A PERSISTENT QUADRATIC TANGENCY THE RESIDUAL SLIDE SPEED ALONG THE FLUX TUBE IS `alpha_T=-D_k D_xi(sigma+kappa)/D_k^2 g`. THEREFORE GENERIC TANGENCY IS A RECYCLABLE PAIR-TURNOVER EVENT, NOT A DIRECTOR-AREA CHARGE LOSS. ONLY HIGHER-ORDER/PERSISTENT TANGENCY, RANK LOSS, ENDPOINT, OR INTERFACE EVENTS REMAIN CANDIDATES FOR A STRONGER OBSTRUCTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Peak frame and notation

On the pure-transverse-kernel Rank-2 branch use the orthonormal frame

\[
(\xi,k,n),
\qquad
D_k\xi=0,
\qquad
J_\xi=|J_\xi|k\neq0.
\]

Define

\[
g:=D_\xi\log\rho=-\nabla\cdot\xi.
\]

A regular line-amplitude peak lies on

\[
\boxed{g=0.}
\]

Write the two nonzero director jets as

\[
b:=D_\xi\xi=p\,k+q\,n,
\]

\[
a:=D_n\xi=r\,k+t\,n.
\]

Since `t=div xi=-g`, every peak has

\[
\boxed{t=0,\qquad a=rk.}
\]

Full Rank 2 gives

\[
\boxed{r\neq0,\qquad q\neq0.}
\]

Use the kernel-fiber curvature coefficient

\[
D_kk=\gamma_k n,
\qquad
D_kn=-\gamma_k k.
\]

---

## 2. Exact flatness identities controlling tangency

The full Euclidean-flatness calculation of M17-074 gives at `g=0`

\[
\boxed{
D_kt+r(\gamma_k-q)=0.
}
\]

Because

\[
t=-g,
\]

this is

\[
\boxed{
D_kg=r(\gamma_k-q).
}
\]

Therefore

\[
\boxed{
D_kg=0
\iff
\gamma_k=q.
}
\]

Thus director-area/peak tangency is not an arbitrary loss of coordinates. It is an exact equality between

- the curvature `gamma_k` of the kernel/director-area flux line in the `(k,n)` plane, and
- the `n` component `q` of the vortex-direction curvature `b=D_xi xi`.

This is the **kernel/vortex curvature resonance**.

The same flatness system gives

\[
\boxed{
D_kq=-\frac prD_kg.
}
\]

Hence on the frozen-angle class, where

\[
p\neq0,
\]

we obtain the three-way equivalence

\[
\boxed{
D_kg=0
\iff
\gamma_k=q
\iff
D_kq=0.
}
\]

On the orthogonal class `p=0`, `D_kq=0` is automatic at the peak and does **not** by itself imply tangency; the true tangency condition remains `D_k g=0`.

---

## 3. Why M17-097 fails precisely at tangency

The peak sheet is the regular level set

\[
S(\theta)=\{g=0\}.
\]

Since

\[
J_\xi=|J_\xi|k,
\]

its signed crossing density is

\[
J_\xi\cdot n_S
=|J_\xi|\frac{D_kg}{|\nabla g|}
\]

for the orientation

\[
n_S=\frac{\nabla g}{|\nabla g|}.
\]

Thus

\[
\boxed{
J_\xi\cdot n_S=0
\iff
D_kg=0.
}
\]

At tangency the flux tube still exists because `J_xi!=0`; only its transverse intersection with the peak sheet degenerates.

---

## 4. Restrict the peak equation to one frozen flux tube

The Cauchy law for `J_xi` implies that its regular flux tubes are transported by the similarity material flow.

Fix one such tube label `lambda` and choose a local coordinate `s` along the tube, normalized at the event so that

\[
\partial_s=D_k
\]

at the contact point.

Let

\[
\mathfrak g_\lambda(s,\theta)
:=g(X_\lambda(s,\theta),\theta)
\]

be the peak descriptor restricted to that moving tube.

At a tangency event `(s_*,theta_*)`,

\[
\boxed{
\mathfrak g_\lambda=0,
\qquad
\partial_s\mathfrak g_\lambda=0.
}
\]

A quadratic or fold tangency additionally satisfies

\[
\boxed{
C_k:=D_k^2g\big|_*\neq0.
}
\]

---

## 5. Exact temporal unfolding coefficient

M17-040 gives

\[
D_Bg
=D_\xi(\sigma+\kappa)
-\left(\sigma+\frac12\right)g.
\]

At the peak,

\[
\boxed{
A_T:=D_Bg\big|_*
=D_\xi(\sigma+\kappa)\big|_*.
}
\]

Because the tube itself is materially transported, this is the first time-unfolding coefficient of the restricted peak equation at fixed tube label.

Therefore a generic tangency has

\[
\boxed{
A_T\neq0,
\qquad
C_k\neq0.
}
\]

---

## 6. Local fold normal form

Let

\[
\tau:=\theta-\theta_*,
\qquad
\eta:=s-s_*.
\]

At a generic tangency, Taylor expansion gives

\[
\boxed{
\mathfrak g_\lambda(\eta,\tau)
=A_T\tau
+\frac12C_k\eta^2
+o(|\tau|+\eta^2).
}
\]

Hence nearby transverse intersections satisfy

\[
\eta_\pm
=\pm\sqrt{-\frac{2A_T}{C_k}\tau}
+o(\sqrt{|\tau|})
\]

on the side where

\[
-\frac{A_T}{C_k}\tau>0.
\]

Thus the intersection number changes locally as

\[
\boxed{0\longleftrightarrow2.}
\]

This is the standard fold genealogy of the peak/flux-tube intersection.

---

## 7. The two newborn intersections have opposite orientation

At the two roots,

\[
D_kg
=\partial_s\mathfrak g_\lambda
=C_k\eta+o(|\eta|).
\]

Therefore

\[
\boxed{
\operatorname{sgn}(D_kg)_+
=-\operatorname{sgn}(D_kg)_-.
}
\]

Equivalently, the signed director-area crossing density

\[
J_\xi\cdot n_S
\]

has opposite signs at the two intersections.

The same frozen tube carries the same underlying director-area flux through the event.

Therefore the pair is created or destroyed with zero net oriented intersection flux:

\[
\boxed{
\Delta\Phi_{J,\mathrm{signed}}^{fold}=0.
}
\]

By contrast, an unsigned per-intersection population counts both roots and changes by two copies of the tube flux element:

\[
\boxed{
\Delta\Phi_{J,\mathrm{unsigned}}^{fold}
=\pm2\,d\Phi_J
}
\]

for pair creation/annihilation.

Thus the M17-097 positive transverse population is not a conserved charge through tangency; only the oriented flux carrier is.

---

## 8. Consequence for M17-098

M17-098 correctly identified tangency as an event at which the transverse peak-flux population can change.

The present calculation sharpens that statement:

\[
\boxed{
\text{generic quadratic tangency}
\Longrightarrow
\text{pair creation/annihilation of transverse peak intersections}
}
\]

but

\[
\boxed{
\text{generic quadratic tangency}
\not\Longrightarrow
\text{director-area charge loss}.
}
\]

The event is recyclable at the level of signed director-area intersection flux.

Therefore tangency by itself is not yet the missing nonrecyclable cost.

---

## 9. Persistent same-tube tangency requires a new exact lock

Suppose instead that one wishes to continue a tangency on the same director-area tube by allowing a slide

\[
\alpha_Tk.
\]

The first tangency equation is

\[
0=(D_B+\alpha_TD_k)g.
\]

But at tangency

\[
D_kg=0.
\]

Therefore the slide cannot cancel the first-order material change, and persistence requires

\[
\boxed{
D_Bg=0.
}
\]

Using Section 5,

\[
\boxed{
D_\xi(\sigma+\kappa)=0.
}
\]

This is a genuine additional condition for persistent same-tube tangency.

---

## 10. Persistent tangency makes the line peak material-stationary along xi

For a regular line extremum let

\[
C:=D_\xi g\neq0.
\]

M17-040 gives its xi-direction material-relative speed

\[
v_{rel}
=-\frac{D_\xi(\sigma+\kappa)}{C}.
\]

Persistent tangency requires

\[
D_\xi(\sigma+\kappa)=0,
\]

hence

\[
\boxed{v_{rel}=0.}
\]

Thus a persistent director-area/peak tangency cannot simultaneously use the ordinary moving-line-peak drift as a recharge channel.

The peak is instantaneously material-stationary in the `xi` direction.

---

## 11. Exact second tangency equation and residual k-slide speed

To preserve tangency one must also keep

\[
D_kg=0.
\]

For any scalar `f`, the material derivative of `D_k f` is

\[
D_B(D_kf)
=(D_Bk)\cdot\nabla f
+D_k(D_Bf)
-((k\cdot\nabla)B)\cdot\nabla f.
\]

M17-033 gives

\[
D_Bk=\Omega n,
\qquad
\Omega:=\beta_\Sigma+r_W,
\]

while

\[
(\nabla B)k
=\left(\sigma_k+\frac12\right)k+\Omega n.
\]

At tangency `D_k g=0`, the two `Omega D_n g` terms cancel, so

\[
D_B(D_kg)
=D_k(D_Bg).
\]

Using

\[
D_Bg
=D_\xi(\sigma+\kappa)
-\left(\sigma+\frac12\right)g
\]

and `g=D_k g=0`, we obtain

\[
\boxed{
D_B(D_kg)
=D_kD_\xi(\sigma+\kappa).
}
\]

The second tangency-persistence equation is therefore

\[
0=(D_B+\alpha_TD_k)(D_kg)
\]

and, for a quadratic contact `D_k^2g!=0`,

\[
\boxed{
\alpha_T
=-\frac{D_kD_\xi(\sigma+\kappa)}{D_k^2g}.
}
\]

Thus a persistent quadratic tangency has an exact residual slide speed along the director-area flux tube.

---

## 12. Tangency hierarchy

The director-area/peak tangency branch now splits as

\[
\boxed{
T_{J\parallel peak}
\Longrightarrow
T_{fold}^{A_T\neq0,C_k\neq0}
\ \lor\
T_{persist}^{A_T=0,C_k\neq0}
\ \lor\
T_{high}^{C_k=0}
\ \lor\
T_{rank/interface}.
}
\]

### Generic fold

\[
A_T=D_\xi(\sigma+\kappa)\neq0,
\qquad
D_k^2g\neq0.
\]

This gives recyclable `0<->2` intersection turnover.

### Persistent quadratic tangency

\[
D_\xi(\sigma+\kappa)=0,
\qquad
D_k^2g\neq0,
\]

with exact slide speed `alpha_T` above.

### Higher-order tangency

\[
D_k^2g=0.
\]

This requires a separate finite-order jet/compactness audit and may contain cusp or higher-contact genealogies.

---

## 13. DSD analysis

The tangency descriptor has three distinct levels:

1. **carrier** — nonzero frozen director-area flux tube;
2. **intersection geometry** — transverse versus tangent contact with `g=0`;
3. **genealogy** — fold pair turnover versus persistent/higher-order contact.

A change at level 2 does not imply destruction at level 1.

This prevents a false conversion of intersection turnover into conserved-charge loss.

---

## 14. DSD audit

### Audit A — treating `D_k g=0` as Rank-2 loss
Rejected. `J_xi` may remain nonzero.

### Audit B — concluding every tangency is persistent
Rejected. Generic `D_B g!=0` unfolds as a fold.

### Audit C — counting fold pair creation as signed director-area loss
Rejected. The two roots have opposite crossing orientation.

### Audit D — using the transverse flux density at the tangent point
Rejected. `J_xi·n_S=0` there; the underlying tube flux is the carrier.

### Audit E — ignoring tube-coordinate reparametrization
The local fold classification is invariant under smooth nonzero rescaling of the tube coordinate; only the normalized coefficients change.

### Audit F — claiming persistent tangency is impossible
Rejected. It requires the explicit lock `D_xi(sigma+kappa)=0` and a residual `k`-slide law, but no contradiction is yet derived.

### Audit G — proof status
Generic tangency is classified and shown recyclable at signed-flux level. Persistent/higher-order tangency remains open.

---

## 15. Updated Rank-2 frontier

The transverse inherited-weight branch of M17-097 remains valid when

\[
D_kg\neq0.
\]

At loss of transversality,

\[
\boxed{
D_kg=0
\iff
\gamma_k=q.
}
\]

Then

\[
\boxed{
R_{2,peak}
\Longrightarrow
R_{2,peak}^{J\text{-}transverse}
\ \lor\
T_{fold}^{signed\ flux\ neutral}
\ \lor\
T_{persist}^{D_\xi(\sigma+\kappa)=0}
\ \lor\
T_{high/rank/interface}.
}
\]

The next high-value gate is the **persistent tangency compensation gate**: insert

\[
D_kg=0,
\qquad
D_\xi(\sigma+\kappa)=0,
\qquad
\alpha_T
=-\frac{D_kD_\xi(\sigma+\kappa)}{D_k^2g}
\]

into the unified Rank-2 maximum-margin transport and determine whether a positive recurrent compensation margin can survive on the same tangent flux-tube genealogy.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
