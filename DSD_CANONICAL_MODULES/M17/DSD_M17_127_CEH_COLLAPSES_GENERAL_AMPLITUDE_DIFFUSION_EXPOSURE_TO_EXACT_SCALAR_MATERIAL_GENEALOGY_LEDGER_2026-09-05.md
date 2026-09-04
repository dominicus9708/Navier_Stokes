# DSD M17-127 — CE-H collapses general amplitude/diffusion exposure to an exact scalar material genealogy ledger

Date: 2026-09-05
Canonical ID: **M17-127**

Status: **EXACT CE-H AMPLITUDE GENEALOGY / EARLIER M5 MATERIAL-PACKET ARGUMENTS FOR GENERAL NAVIER–STOKES REQUIRED SEPARATE STRAIN AND ADDITIVE DIFFUSION EXPOSURES TO RETAIN VORTICITY AMPLITUDE. ON THE CURRENT CE-H BRANCH, `Delta W=kappa W` MAKES THE DIFFUSION TERM EXACTLY COLLINEAR WITH VORTICITY, SO THE MATERIAL AMPLITUDE OBEYS THE HOMOGENEOUS SCALAR LAW `D_B rho=(sigma+kappa-1)rho`. COMBINED WITH M17-126 SAME-MATERIAL SPATIAL LOCALIZATION, THE REMAINING REMOTE GENEALOGY GAP IS REDUCED TO ONE EXACT INTER-STAGE EXPOSURE `E_rho=int(sigma+kappa-1)dtheta`. BOUNDED EXPOSURE GIVES TWO-SIDED AMPLITUDE RETENTION; FAILURE IS EXACTLY LARGE SIGNED MULTIPLICATIVE EXPOSURE, NOT AN UNCONTROLLED ADDITIVE DIFFUSION ERROR. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Earlier general packet equation

For general Navier–Stokes vorticity,

\[
D_t\omega=S\omega+\nu\Delta\omega.
\]

A material lower-amplitude estimate must normally control the additive diffusion term `Delta omega` independently of the strain exposure.

That is why the earlier M5 amplitude-location genealogy bridge introduced both local strain and diffusion exposures.

---

## 2. CE-H removes the additive diffusion channel

On the current CE-H branch,

\[
\boxed{
\Delta W=\kappa W,
}
\]

and the strain eigenline gives

\[
\boxed{
\Sigma W=\sigma W.
}
\]

The similarity vorticity equation therefore reduces along the material velocity `B` to

\[
D_BW
=(\sigma+\kappa-1)W.
\]

Writing

\[
W=\rho\xi,
\qquad
D_B\xi=0,
\]

gives the exact scalar law

\[
\boxed{
D_B\rho
=(\sigma+\kappa-1)\rho.
}
\]

No additive remainder remains.

---

## 3. Exact inter-stage amplitude ratio

For one positive-vorticity material carrier tracked from `theta_{j-k}` to `theta_j`, define

\[
\boxed{
\mathcal E_\rho(j,k)
:=
\int_{\theta_{j-k}}^{\theta_j}
(\sigma+\kappa-1)(X(\theta),\theta)d\theta.
}
\]

Then

\[
\boxed{
\rho_j
=\rho_{j-k}e^{\mathcal E_\rho(j,k)}.
}
\]

Equivalently,

\[
\boxed{
\log\frac{\rho_j}{\rho_{j-k}}
=\mathcal E_\rho(j,k).
}
\]

This is exact as long as the CE-H regular trajectory exists and `rho>0`, which is preserved by M17-105 on every finite regular interval.

---

## 4. Quiet-exposure retention

If

\[
|\mathcal E_\rho(j,k)|\le L,
\]

then

\[
\boxed{
 e^{-L}\rho_{j-k}
\le
\rho_j
\le
 e^L\rho_{j-k}.
}
\]

Thus two-sided same-carrier amplitude retention needs only one scalar exposure bound on CE-H.

In particular, if the descendant remote carrier satisfies

\[
\rho_j\ge c_\rho>0
\]

and

\[
\mathcal E_\rho(j,k)\le L,
\]

then

\[
\boxed{
\rho_{j-k}\ge c_\rho e^{-L}>0.
}
\]

Combined with M17-126, this places a nontrivial same material Rank-2 carrier at a comparable ancestor physical radius with retained normalized amplitude.

---

## 5. Exact failure mode

If the descendant amplitudes remain nontrivial but the same ancestor carriers lose normalized amplitude,

\[
\rho_j\ge c_\rho>0,
\qquad
\rho_{j-k}\to0,
\]

then necessarily

\[
\boxed{
\mathcal E_\rho(j,k)\to+\infty.
}
\]

Thus amplitude genealogy failure is not an untyped diffusion escape. It is an exact large positive cumulative multiplier exposure.

Similarly, descendant forgetting along a positive material carrier is exactly a large negative exposure.

---

## 6. Relation to director-area genealogy

M17-123 gives

\[
D_B\log\eta_J
=\sigma_k-\sigma-\kappa,
\qquad
\eta_J=\frac{|J_\xi|}{\rho}.
\]

The director-area magnitude satisfies

\[
D_B\log|J_\xi|=\sigma_k-1.
\]

Hence the three exact exposures satisfy the identity

\[
\boxed{
\mathcal E_J
=
\mathcal E_\rho+\mathcal E_\eta,
}
\]

where

\[
\mathcal E_J:=\int(\sigma_k-1)d\theta,
\qquad
\mathcal E_\eta:=\int(\sigma_k-\sigma-\kappa)d\theta.
\]

This is simply the logarithmic identity `|J_xi|=rho eta_J`, but it is useful genealogically: amplitude amplification, director-area distortion, and rank-boundary approach cannot be assigned independently.

---

## 7. Connection to the old M5 packet audit

The earlier material-packet bridge remains useful for spatial coherence and general non-CE-H branches.
On CE-H, however, its separate additive diffusion exposure is superseded by the exact multiplier `kappa`.

Therefore the CE-H remote genealogy tree becomes

\[
\boxed{
\text{remote carrier}
\Longrightarrow
\begin{cases}
\text{bounded }\mathcal E_\rho
&\Rightarrow\text{same-carrier amplitude retention},\\
\mathcal E_\rho\to+\infty
&\Rightarrow\text{large cumulative amplification},\\
\mathcal E_\rho\to-\infty
&\Rightarrow\text{large cumulative forgetting}.
\end{cases}
}
\]

There is no fourth additive diffusion-error branch inside CE-H.

---

## 8. DSD audit

### Audit A — setting kappa to zero because diffusion is collinear

Rejected. Diffusion is not absent; it is encoded exactly by the signed scalar `kappa`.

### Audit B — bounded coefficients imply bounded long-time exposure

Rejected. The interval length is `2 log K_k`, so a bounded nonzero mean may still produce `O(log K_k)` exposure.

### Audit C — spatial localization implies amplitude retention

Rejected. M17-126 and M17-127 are independent pieces; retention requires control of `mathcal E_rho`.

### Audit D — large positive exposure is itself a contradiction

Rejected. It is a typed exact requirement, not yet an excluded event.

### Audit E — proof status

The amplitude genealogy is scalarized exactly, but no aggregate bound yet controls `mathcal E_rho` on the cubic-divergent remote-shell population.

---

## 9. Updated genealogy frontier

On the bounded-similarity-velocity CE-H Rank-2 branch,

\[
\boxed{
\text{remote flux-carrying carrier}
\Longrightarrow
\text{same-material ancestor-scale location}
+
\text{exact amplitude exposure }\mathcal E_\rho.
}
\]

The next target is to combine the M5 amplitude-sensitive arithmetic selection

\[
J_k^{1/2}K_k^2\gg1
\]

with M17-121/M17-122 flux capture and test whether a cubic-divergent set can have unbounded positive `mathcal E_rho` on essentially all of its same-material ancestor carriers without forcing rank/nodal accumulation or a global strain/kappa budget violation.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
