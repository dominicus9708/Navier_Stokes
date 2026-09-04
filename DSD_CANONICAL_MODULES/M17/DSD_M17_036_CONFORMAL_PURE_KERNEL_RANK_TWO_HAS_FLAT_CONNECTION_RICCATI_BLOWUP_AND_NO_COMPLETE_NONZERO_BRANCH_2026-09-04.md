# DSD M17-036 — Conformal pure-kernel rank two has a flat-connection Riccati blowup and no complete nonzero branch

Date: 2026-09-04
Canonical ID: **M17-036**

Status: **INTERNAL CONFORMAL PURE-KERNEL CLOSURE / M17-035 REDUCES THE CONFORMAL `j_xi=0` RANK-TWO BRANCH TO THE ORTHONORMAL FRAME `(xi,k,n)` WITH `D_k xi=0`, `D_xi xi=lambda n`, `D_n xi=epsilon lambda k`, `|epsilon|=1`, `D_xi rho=0`, AND `div xi=0`. IMPOSING THE VANISHING RIEMANN CURVATURE OF EUCLIDEAN SPACE ON THIS MOVING FRAME DETERMINES THE REMAINING CONNECTION COEFFICIENTS AND FORCES `D_k lambda=0`, `D_xi lambda=0`, `D_n lambda=2 lambda^2`, WHILE ALSO FORCING `D_n n=0`. THUS THE `n`-INTEGRAL CURVES ARE EUCLIDEAN STRAIGHT LINES AND `lambda` OBEYS THE SCALAR RICCATI ODE `d lambda/ds=2 lambda^2` ALONG EACH SUCH COMPLETE LINE. EVERY NONZERO INITIAL lambda BLOWS UP AT FINITE SIGNED DISTANCE. THEREFORE A SMOOTH COMPLETE NONZERO CONFORMAL PURE-KERNEL RANK-TWO COMPONENT CANNOT EXIST. A LOCAL CONFORMAL PATCH MUST EXIT THROUGH `lambda->0`/RANK LOSS, ANISOTROPY, OR A BRANCH INTERFACE BEFORE THE FOCAL DISTANCE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-035

On the conformal pure-transverse-kernel branch, choose the orientation so that

\[
(\xi,k,n)
\]

is an orthonormal frame and write

\[
\boxed{
D_k\xi=0,
}
\]

\[
\boxed{
D_\xi\xi=\lambda n,
}
\]

and

\[
\boxed{
D_n\xi=\varepsilon\lambda k,
\qquad
\varepsilon\in\{+1,-1\}.
}
\]

The sign `epsilon` records the orientation of the two equal-magnitude orthogonal director jets.

Rank two requires

\[
\boxed{\lambda\ne0.}
\]

M17-035 also gives

\[
D_\xi\rho=0
\]

and

\[
\nabla\cdot\xi=0.
\]

The closure below uses only the frame geometry.

---

## 2. General compatible Euclidean connection coefficients

Orthonormality determines the most general connection derivatives consistent with Section 1.
Write

\[
D_\xi k=\alpha n,
\]

so

\[
D_\xi n=-\lambda\xi-\alpha k.
\]

Write

\[
D_k k=\beta n,
\]

so

\[
D_k n=-\beta k.
\]

Finally write

\[
D_nk=-\varepsilon\lambda\xi+\delta n,
\]

so

\[
D_nn=-\delta k.
\]

Thus the unknown Euclidean connection data are the three scalar coefficients

\[
\alpha,
\qquad
\beta,
\qquad
\delta.
\]

---

## 3. First flatness equation R(xi,k)xi = 0

Euclidean space has zero Riemann curvature:

\[
R(\xi,k)\xi=0.
\]

The frame commutator is

\[
[\xi,k]
=D_\xi k-D_k\xi
=\alpha n.
\]

Compute

\[
\begin{aligned}
R(\xi,k)\xi
&=D_\xi D_k\xi
-D_kD_\xi\xi
-D_{[\xi,k]}\xi\\
&=0
-D_k(\lambda n)
-\alpha D_n\xi.
\end{aligned}
\]

Using

\[
D_kn=-\beta k,
\qquad
D_n\xi=\varepsilon\lambda k,
\]

we obtain

\[
R(\xi,k)\xi
=-(D_k\lambda)n
+\lambda(\beta-\varepsilon\alpha)k.
\]

Therefore

\[
\boxed{D_k\lambda=0}
\]

and, since `lambda!=0`,

\[
\boxed{\beta=\varepsilon\alpha.}
\]

---

## 4. Second flatness equation R(k,n)xi = 0

The commutator is

\[
[k,n]
=D_kn-D_nk
=\varepsilon\lambda\xi
-\beta k
-\delta n.
\]

Compute

\[
R(k,n)\xi
=D_kD_n\xi
-D_nD_k\xi
-D_{[k,n]}\xi.
\]

Since

\[
D_n\xi=\varepsilon\lambda k,
\qquad
D_k\xi=0,
\qquad
D_k\lambda=0,
\]

we find

\[
R(k,n)\xi
=\varepsilon\lambda\delta\,k
+\varepsilon\lambda(\beta-\lambda)n.
\]

Therefore

\[
\boxed{\delta=0}
\]

and

\[
\boxed{\beta=\lambda.}
\]

Together with

\[
\beta=\varepsilon\alpha
\]

this gives

\[
\boxed{
\alpha=\varepsilon\lambda,
\qquad
\beta=\lambda,
\qquad
\delta=0.
}
\]

---

## 5. Third flatness equation R(xi,n)xi = 0

The commutator is

\[
[\xi,n]
=-\lambda\xi
-(\alpha+\varepsilon\lambda)k.
\]

Compute

\[
R(\xi,n)\xi
=D_\xiD_n\xi
-D_nD_\xi\xi
-D_{[\xi,n]}\xi.
\]

A direct substitution gives the two independent components

\[
\varepsilon D_\xi\lambda
+\lambda\delta=0
\]

and

\[
\varepsilon\lambda\alpha
-D_n\lambda
+\lambda^2=0.
\]

Using

\[
\delta=0,
\qquad
\alpha=\varepsilon\lambda,
\]

we obtain

\[
\boxed{D_\xi\lambda=0}
\]

and

\[
\boxed{D_n\lambda=2\lambda^2.}
\]

Thus the scalar conformal director-gradient amplitude is constant in the `xi` and `k` directions and evolves only in the `n` direction.

---

## 6. The n curves are straight

From

\[
\delta=0
\]

and

\[
D_nn=-\delta k,
\]

we get

\[
\boxed{D_nn=0.}
\]

Therefore the unit `n` integral curves are Euclidean straight lines.

Let `s` be arclength along one such line:

\[
\frac{dx}{ds}=n.
\]

Then

\[
\boxed{
\frac{d\lambda}{ds}=2\lambda^2.
}
\]

---

## 7. Explicit Riccati solution

For initial value

\[
\lambda(0)=\lambda_0,
\]

the scalar ODE has solution

\[
\boxed{
\lambda(s)
=\frac{\lambda_0}{1-2\lambda_0s}.
}
\]

If

\[
\lambda_0>0,
\]

it blows up at

\[
s=\frac1{2\lambda_0}>0.
\]

If

\[
\lambda_0<0,
\]

it blows up at the finite negative distance

\[
s=\frac1{2\lambda_0}<0.
\]

Thus every nonzero initial value develops a finite-distance pole in one direction along the complete straight line.

---

## 8. Complete smooth branch contradiction

A complete smooth conformal rank-two component would require

\[
\lambda(s)
\]

to remain finite and nonzero for all

\[
s\in\mathbb R.
\]

The Riccati solution shows this is impossible unless

\[
\lambda_0=0.
\]

But

\[
\lambda=0
\]

would give

\[
D_\xi\xi=0,
\qquad
D_n\xi=0,
\qquad
D_k\xi=0,
\]

so

\[
\operatorname{rank}d\xi=0,
\]

contradicting the active rank-two hypothesis.

Therefore

\[
\boxed{
R_{2,j=0}^{conformal,complete}
\Longrightarrow\bot.
}
\]

---

## 9. Local branch exits

The argument does not say that a finite conformal patch cannot occur.
A local patch can avoid the finite-distance pole only by leaving the assumed class before the focal distance.

The exits are

\[
\boxed{
\lambda\to0\text{ / rank loss}
\ \lor\ 
\mathcal D>0\text{ / anisotropy}
\ \lor\ 
\text{branch/interface termination}.
}
\]

Thus complete persistence is closed while finite conformal episodes become interface events.

---

## 10. DSD interpretation

The closure chain is

\[
\boxed{
\text{weighted harmonic conformality}
\to
\text{canonical frame}
\to
\text{Euclidean flatness}
\to
\text{scalar Riccati blowup}.
}
\]

The decisive information does not come from an integral sign estimate.
It comes from compatibility of the director's two equal-magnitude channels with the flat ambient connection.

---

## 11. DSD audit

### Audit A — treating lambda as nonnegative
Avoided. `lambda` is signed; either sign blows up in one signed direction along a complete line.

### Audit B — confusing finite-distance frame blowup with proven Navier-Stokes singularity
Avoided. A local branch can exit into anisotropy/rank loss before the pole. The contradiction applies only to a complete persistent conformal component.

### Audit C — assuming n curves are straight
Derived from flatness: `delta=0` forces `D_n n=0`.

### Audit D — importing external conformal-foliation theorems
Not needed. The closure is an internal Euclidean connection calculation.

### Audit E — proof status
One more intrinsic Rank-2 subbranch is closed; the anisotropic pure-kernel branch and turnover/interfaces remain.

---

## 12. Updated intrinsic Rank-2 frontier

After M17-036,

\[
\boxed{
R_2^{intrinsic}
\Longrightarrow
R_{2,j=0}^{anisotropic}
\ \lor\ 
T_{2\to1}
\ \lor\ 
I_{2}^{interface/turnover}.
}
\]

The complete parallel branch is closed by M17-030.
The recurrent nonzero-transverse-area oblique branch is closed by M17-032 under same-marker recurrence.
The complete conformal pure-kernel branch is closed here.

The cleanest unresolved intrinsic Rank-2 geometry is therefore

\[
\boxed{R_{2,j=0}^{anisotropic}.}
\]

---

## 13. Next target

For the anisotropic pure-kernel class define

\[
\boxed{
\mathcal D
=E^2-4|J_\xi|^2>0.
}
\]

M17-033 already supplies exact scalar material laws for the two independent jets `a,b`.
The next calculation should derive the material evolution of `mathcal D` and its normalized shape ratio.

If anisotropy is materially frozen or obeys a one-sign multiplier, it may force either conformal approach, rank loss, or a new recurrence exponent incompatible with the resonant mean frame.

This is the **Rank-Two Anisotropy Evolution Gate (R2AEG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
