# DSD M17-047 — Cross-aligned critical flatness forces a super-Riccati n-slope at line maxima

Date: 2026-09-04
Canonical ID: **M17-047**

Status: **INTERNAL RANK-TWO CRITICAL-FRAME FLATNESS / M17-040 SHOWS THAT EVERY LINEWISE AMPLITUDE/STRETCH CRITICAL POINT ON THE ORTHOGONAL PURE-KERNEL BRANCH IS CROSS-ALIGNED, BUT THAT ALIGNMENT HOLDS ONLY ON THE CRITICAL SET AND MUST NOT BE DIFFERENTIATED AS IF IT HELD ON A NEIGHBORHOOD. RETAINING THE GENERAL ORTHOGONAL JETS `b=p k+q n`, `a=r k+t n`, `rp+tq=0`, AND ONLY THEN SETTING `g=0`, HENCE `t=p=0`, THE EUCLIDEAN FLATNESS EQUATIONS GIVE THE EXACT CRITICAL-POINT LAW `D_n q = 2 q^2 - D_xi g`. SINCE `D_xi g=D_xi^2 log rho`, A NONDEGENERATE LINE MAXIMUM HAS `D_n q>2q^2`, STRICTLY STEEPER THAN THE CONFORMAL RICCATI RATE, WHILE A MINIMUM HAS `D_n q<2q^2`. THIS DOES NOT BY ITSELF GIVE FINITE-DISTANCE BLOWUP BECAUSE THE CRITICAL CONDITION NEED NOT PERSIST ALONG THE n-CURVE; IT CONVERTS THE OSCILLATORY-TAIL NETWORK INTO AN ALTERNATING SUPER-/SUB-RICCATI FLATNESS NETWORK. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. General orthogonal pure-kernel frame

Work on the pure-transverse-kernel Rank-2 branch with orthonormal frame

\[
(\xi,k,n),
\qquad
(k\cdot\nabla)\xi=0.
\]

Do **not** impose cross-alignment away from the critical set.
Write the two nonzero director jets in full form

\[
\boxed{
b:=(\xi\cdot\nabla)\xi=p\,k+q\,n,}
\]

\[
\boxed{
a:=(n\cdot\nabla)\xi=r\,k+t\,n.}
\]

Orthogonal stretch means

\[
\boxed{a\cdot b=rp+tq=0.}
\]

Full rank two requires the two image vectors to remain nonzero and independent.

---

## 2. Relation to the amplitude derivative

M17-040 defines

\[
\boxed{g:=D_\xi\log\rho=-\nabla\cdot\xi.}
\]

In the present frame

\[
\nabla\cdot\xi=t,
\]

so

\[
\boxed{t=-g.}
\]

From orthogonality,

\[
\boxed{p=-\frac{tq}{r}=\frac{gq}{r}}
\]

where `r!=0` on the full-rank critical branch.

At a linewise amplitude critical point,

\[
\boxed{g=0,}
\]

hence

\[
\boxed{t=0,\qquad p=0.}
\]

Thus only **at the critical point**,

\[
\boxed{b=q n,\qquad a=r k.}
\]

---

## 3. General compatible connection coefficients

Orthonormality gives

\[
D_\xi k=-p\xi+\alpha n,
\]

\[
D_\xi n=-q\xi-\alpha k,
\]

\[
D_k k=\beta n,
\qquad
D_k n=-\beta k,
\]

\[
D_n k=-r\xi+\delta n,
\]

\[
D_n n=-t\xi-\delta k.
\]

The unknown connection coefficients are

\[
\alpha,\beta,\delta.
\]

We now evaluate Euclidean flatness at one critical point `g=t=p=0` without assuming their derivatives vanish.

---

## 4. Flatness R(xi,k)xi = 0

At the critical point,

\[
[\xi,k]=\alpha n.
\]

A direct calculation gives

\[
R(\xi,k)\xi
=
\left[-D_kp+q\beta-\alpha r\right]k
-(D_kq)n.
\]

Therefore

\[
\boxed{D_kq=0,}
\]

and

\[
\boxed{q\beta-\alpha r=D_kp.}
\]

Since

\[
p=-\frac{tq}{r},
\]

at `t=0`,

\[
D_kp=-\frac qr D_kt.
\]

---

## 5. Flatness R(k,n)xi = 0

At the same point,

\[
[k,n]=r\xi-\beta k-\delta n.
\]

Flatness gives

\[
\boxed{D_kr+\delta r=0,}
\]

and

\[
\boxed{r(\beta-q)+D_kt=0.}
\]

Hence

\[
\boxed{\delta=-\frac{D_kr}{r},}
\]

\[
\boxed{\beta=q-\frac{D_kt}{r}.}
\]

Substitute this into the `R(xi,k)xi` equation.
The `D_kt` terms cancel exactly, leaving

\[
\boxed{\alpha=\frac{q^2}{r}.}
\]

This cancellation is important: the connection rotation `alpha` is fixed by the two cross-aligned jet magnitudes even though the critical condition is not assumed off the set.

---

## 6. Flatness R(xi,n)xi = 0

A direct calculation at `p=t=0` gives two component equations:

\[
\boxed{
D_\xi r-D_np+q\delta=0,
}
\]

and

\[
\boxed{
D_nq=r\alpha+D_\xi t+q^2.
}
\]

Using

\[
\alpha=\frac{q^2}{r},
\]

we obtain

\[
\boxed{
D_nq=2q^2+D_\xi t.
}
\]

Since

\[
t=-g,
\]

this becomes the exact critical flatness law

\[
\boxed{
D_nq=2q^2-D_\xi g.
}
\]

Because

\[
g=D_\xi\log\rho,
\]

we may also write

\[
\boxed{
D_nq
=2q^2-D_\xi^2\log\rho.
}
\]

---

## 7. Maxima are super-Riccati events

At a nondegenerate linewise amplitude maximum,

\[
D_\xi g=D_\xi^2\log\rho<0.
\]

Therefore

\[
\boxed{
D_nq>2q^2.
}
\]

The conformal complete branch M17-036 had the exact Riccati rate

\[
D_n\lambda=2\lambda^2.
\]

Thus every anisotropic cross-aligned **maximum** has an instantaneous `n`-direction slope strictly steeper than the conformal Riccati value.

Symbolically,

\[
\boxed{
\text{line maximum}
\Longrightarrow
\text{super-Riccati }n\text{-slope for }q.
}
\]

---

## 8. Minima are sub-Riccati events

At a nondegenerate linewise amplitude minimum,

\[
D_\xi g>0.
\]

Hence

\[
\boxed{
D_nq<2q^2.
}
\]

There is no fixed lower bound or fixed sign for `D_n q` from this identity alone.

Therefore an oscillatory line tail consists of an alternating network of super-Riccati and sub-Riccati critical events.

---

## 9. Why this is not yet a blowup proof

The tempting shortcut

\[
D_nq>2q^2
\Longrightarrow
\text{finite-distance pole}
\]

is invalid at a single maximum.

The reason is that the condition

\[
g=0
\]

need not persist as one moves in the `n` direction.
The exact super-Riccati inequality has been proved at the critical event, not on an entire `n`-integral interval.

A genuine Riccati blowup argument would require a critical surface/curve along which the inequality persists or a comparison theorem controlling departures from the critical set.

---

## 10. Additional critical connection data

The flatness calculation also gives

\[
\boxed{D_kq=0,}
\]

\[
\boxed{
\beta=q-\frac{D_kt}{r}
=q+\frac{D_kg}{r},
}
\]

\[
\boxed{
\delta=-\frac{D_kr}{r},
}
\]

\[
\boxed{
\alpha=\frac{q^2}{r}.
}
\]

Thus the only deviation from the conformal connection pattern at the critical point is encoded by anisotropic magnitudes and transverse derivatives of the criticality descriptor.

---

## 11. DSD analysis

M17-040 switched descriptors from global tail shape to line critical events.
M17-047 adds the ambient-flatness channel.

The resulting chain is

\[
\boxed{
D_\xi\rho=0
\to
(p,t)=(0,0)
\to
\text{cross-aligned director jets}
\to
D_nq=2q^2-D_\xi^2\log\rho.
}
\]

The conformal Riccati coefficient `2q^2` survives, while the line-amplitude curvature appears as the exact anisotropic correction.

---

## 12. DSD audit

### Audit A — differentiating cross alignment off the critical set
Avoided. The full `(p,q,r,t)` jet is retained until after all directional derivatives are formed.

### Audit B — treating a pointwise super-Riccati slope as an interval inequality
Rejected.

### Audit C — assuming minima give negative D_nq
Rejected. They only give `D_nq<2q^2`.

### Audit D — importing the complete conformal contradiction directly
Rejected. M17-036 requires a conformal component, whereas M17-047 is a local anisotropic critical-event law.

### Audit E — proof status
The critical network is more rigid but remains open.

---

## 13. Updated orthogonal-stretch frontier

\[
\boxed{
R_{osc-tail}^{stretch}
\Longrightarrow
R_{max}^{super-Riccati}
\ \lor\ 
R_{min}^{sub-Riccati}
\ \lor\ 
T_{crit}^{degenerate}.
}
\]

An infinite oscillatory tail must repeatedly alternate between the first two event types unless it encounters a degenerate critical event.

---

## 14. Next target — critical-surface persistence gate

The next useful calculation is to study the geometry of the spatial critical set

\[
\mathcal C:=\{g=D_\xi\log\rho=0\}.
\]

If a regular component of `C` carries maxima/minima coherently in an `n`-transverse direction, determine whether the super-/sub-Riccati law can be integrated along that component or whether the component necessarily develops a degenerate event `grad g=0`.

This is the **Critical-Surface Riccati Persistence Gate (CSRPG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
