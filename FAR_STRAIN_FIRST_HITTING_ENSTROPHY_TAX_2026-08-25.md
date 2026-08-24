# Far-Strain First-Hitting Enstrophy Tax

Date: 2026-08-25

Status: **FAR-STRAIN L2 TAX PROVED / GENEALOGY CLOSURE NOT DERIVED / GLOBAL REGULARITY NOT PROVED.**

This note quantifies the `F` branch left after the maximum-centered P-branch snapshot collapse.

The key fact is that the far part of the strain Biot-Savart operator is square-integrable as a kernel, so any sustained far-strain exposure has a direct enstrophy cost.

---

## 1. Far strain in normalized variables

Work first in a normalized frame with viscosity `nu=1` and reference length one.  Write

\[
S_F(y,s)
:=
\int_{|z|>R}K(z)\Omega(y-z,s)\,dz,
\qquad R>0,
\]

where the strain kernel satisfies

\[
|K(z)|\le C|z|^{-3}.
\]

By Cauchy-Schwarz,

\[
|S_F(y,s)|
\le
C
\left(\int_{|z|>R}|z|^{-6}dz\right)^{1/2}
\|\Omega(s)\|_2.
\]

Since in three dimensions

\[
\int_{|z|>R}|z|^{-6}dz
\sim R^{-3},
\]

we obtain

\[
\boxed{
\|S_F(s)\|_\infty
\le
C R^{-3/2}\|\Omega(s)\|_2.
}
\]

Equivalently,

\[
\boxed{
\|\Omega(s)\|_2^2
\ge
cR^3\|S_F(s)\|_\infty^2.
}
\]

**Status: PROVED.**

---

## 2. Physical normalization at a first-hitting scale

Let `W_*>0` be the reference vorticity amplitude and

\[
r_*:=\left(\frac\nu{W_*}\right)^{1/2}.
\]

Use

\[
y=\frac{x-x_*}{r_*},
\qquad
s=\frac\nu{r_*^2}(t-t_*),
\qquad
\Omega(y,s)=\frac{r_*^2}{\nu}\omega(x,t).
\]

The normalized strain is

\[
\Sigma(y,s)=\frac{r_*^2}{\nu}S(x,t).
\]

For a physical far cutoff `R r_*`, the previous estimate gives

\[
\boxed{
\frac{r_*^2}{\nu}
\|S_{>Rr_*}(t)\|_\infty
\le
CR^{-3/2}
\left(
\frac{r_*}{\nu^2}
\|\omega(t)\|_2^2
\right)^{1/2}.
}
\]

Define the normalized instantaneous enstrophy

\[
\boxed{
\mathcal E_{\omega,*}(t)
:=
\frac{r_*}{\nu^2}
\|\omega(t)\|_2^2.
}
\]

Then

\[
\boxed{
\mathcal H_F(t)
:=
\frac{r_*^2}{\nu}
\|S_{>Rr_*}(t)\|_\infty
\le
CR^{-3/2}\mathcal E_{\omega,*}(t)^{1/2}.
}
\]

**Status: PROVED.**

---

## 3. Spacetime far-strain exposure

Let `I` be an interval with normalized duration

\[
\Theta
:=
\frac{\nu|I|}{r_*^2}.
\]

Define the accumulated far-strain exposure

\[
\boxed{
\eta_F(I)
:=
\int_I
\frac{r_*^2}{\nu}
\|S_{>Rr_*}(t)\|_\infty
\frac{\nu\,dt}{r_*^2}
=
\int_{I_s}\mathcal H_F(s)ds.
}
\]

Also define the normalized enstrophy tax

\[
\boxed{
\mathfrak Z_*(I)
:=
\frac1{\nu r_*}
\int_I\|\omega(t)\|_2^2dt.
}
\]

Indeed,

\[
\int_{I_s}\mathcal E_{\omega,*}(s)ds
=
\mathfrak Z_*(I).
\]

Cauchy-Schwarz in time therefore yields

\[
\eta_F(I)
\le
CR^{-3/2}
\Theta^{1/2}
\mathfrak Z_*(I)^{1/2}.
\]

Hence

\[
\boxed{
\mathfrak Z_*(I)
\ge
cR^3
\frac{\eta_F(I)^2}{\Theta}.
}
\]

This is the central far-strain tax.

**Status: PROVED.**

---

## 4. First-hitting interpretation

Let a first-hitting epoch increase a vorticity amplitude from `W_{j-1}` to `W_j=qW_{j-1}` with fixed `q>1`, and use the parent natural radius

\[
r_{j-1}=\left(\frac\nu{W_{j-1}}\right)^{1/2}.
\]

At differentiability times of `W(t)=||omega(t)||_infty`, the maximum-vorticity inequality gives

\[
D^+\log W(t)
\le
\|S(t)\|_\infty.
\]

Therefore

\[
\boxed{
\log q
\le
\int_{t_{j-1}}^{t_j}\|S(t)\|_\infty dt.
}
\]

If the local/near strain channels account for at most a fixed fraction, for example

\[
\int_{I_j}\|S_{\rm local}(t)\|_\infty dt
\le
\frac12\log q,
\]

then the far channel must satisfy

\[
\boxed{
\eta_{F,j}\ge \eta_0(q)>0
}
\]

in the parent first-hitting normalization.

Consequently

\[
\boxed{
\mathfrak Z_j
\ge
c_{q,R}\Theta_j^{-1}.
}
\]

This reproduces, now specifically for the far-strain branch, the reciprocal epoch-duration tax previously seen in the broader first-hitting enstrophy calculation.

**Status: PROVED CONDITIONAL on the far channel carrying a fixed fraction of the first-hitting growth exposure.**

---

## 5. Global Leray energy ledger

For smooth whole-space divergence-free solutions,

\[
\|\omega(t)\|_2^2
=
\|\nabla u(t)\|_2^2.
\]

The global energy identity gives

\[
\nu\int_0^{T^*}\|\omega(t)\|_2^2dt
\le E_0,
\]

up to the conventional factor in the definition of `E0`.

For disjoint first-hitting epochs,

\[
\nu^2r_{j-1}\mathfrak Z_j
=
\nu\int_{I_j}\|\omega(t)\|_2^2dt.
\]

Hence

\[
\boxed{
\sum_jr_{j-1}\mathfrak Z_j
\lesssim
\frac{E_0}{\nu^2}
=:L_E.
}
\]

Combining with the far-strain tax,

\[
\boxed{
\sum_{j\in F}
 r_{j-1}R^3
\frac{\eta_{F,j}^2}{\Theta_j}
<\infty.
}
\]

If `R` is fixed and `eta_{F,j}>=eta0>0` on the F epochs,

\[
\boxed{
\sum_{j\in F}\frac{r_{j-1}}{\Theta_j}<\infty.
}
\]

**Status: PROVED under disjointness of the first-hitting epochs.**

---

## 6. Relation to return residence

In the `nu=1` return-density normalization, an epoch of physical radius `r_j` and duration `tau_j` contributes residence length

\[
\mathfrak L_j
=\frac{\tau_j}{r_j}
=\Theta_jr_j.
\]

The far-strain energy tax contains the reciprocal weight

\[
\frac{r_j}{\Theta_j}.
\]

Thus, for an F-active epoch,

\[
\boxed{
\mathfrak L_j
\left(\frac{r_j}{\Theta_j}ight)
=r_j^2.
}
\]

This exposes the exact tradeoff:

- long residence helps the genealogy return ledger but lowers the far-strain energy tax;
- short residence starves genealogy return but raises the far-strain energy tax.

However, because `r_j` may decrease geometrically, neither side alone is forced to diverge.

**Status: PROVED identity / NO CONTRADICTION BY ITSELF.**

---

## 7. Severe genealogy deficit on the F branch

Suppose a tracked F epoch contributes to an ancient label `k` with

\[
\mathfrak R_k\gtrsim \Theta_kr_k
\]

and severe deficit

\[
\mathfrak R_k<\varepsilon J_k^{1/2}.
\]

Then

\[
\Theta_k
\lesssim
\varepsilon\frac{J_k^{1/2}}{r_k}.
\]

If the F exposure is bounded below by `eta0`, the enstrophy tax yields

\[
\boxed{
\mathfrak Z_k
\gtrsim
\frac{r_k}{\varepsilon J_k^{1/2}}.
}
\]

and therefore the actual energy expenditure satisfies

\[
\boxed{
 r_k\mathfrak Z_k
\gtrsim
\frac{r_k^2}{\varepsilon J_k^{1/2}}.
}
\]

This is a genuine lower bound, but it does **not** yet compare directly with the divergent cubic mass `J_k^{3/2}` because no universal lower relation

\[
r_k^2\gtrsim J_k^2
\]

or equivalent has been proved for the tracked ancient annuli.

Thus the missing F-branch bridge is now explicit:

\[
\boxed{
\text{relate physical first-hitting radius }r_k
\text{ quantitatively to ancient annular amplitude }J_k.
}
\]

**Status: PROVED CONDITIONAL through the displayed tax; final amplitude-radius bridge NOT DERIVED.**

---

## 8. Audit table

| Claim | Status |
|---|---|
| Far strain `<= C R^{-3/2} ||Omega||_2` | **PROVED** |
| Integrated far exposure forces `Z >= c R^3 eta_F^2/Theta` | **PROVED** |
| A fixed far share of first-hitting growth gives `Z >= c/Theta` | **PROVED CONDITIONAL on channel occupancy** |
| Global energy gives `sum r_j Z_j < infinity` | **PROVED for disjoint epochs** |
| F epochs with fixed exposure satisfy `sum r_j/Theta_j < infinity` | **PROVED** |
| Return residence is `Theta_j r_j` in `nu=1` | **PROVED** |
| Severe return deficit forces the displayed reciprocal F-energy tax | **PROVED CONDITIONAL on genealogy tracking** |
| That tax already contradicts `sum J_k^{3/2}=infinity` | **NOT DERIVED** |
| Global regularity | **UNPROVED** |

---

## 9. Updated F-branch frontier

The far-strain branch is no longer a qualitative nonlocal escape.  It has a precise reciprocal residence/energy cost:

\[
\boxed{
F
\Longrightarrow
\mathfrak Z_j
\gtrsim
\frac{\eta_{F,j}^2}{\Theta_j},
\qquad
\mathfrak R_j\sim \Theta_jr_j.
}
\]

The remaining closure problem is not the far-field estimate itself.  It is the scale-identification bridge between the physical first-hitting radius `r_j` and the ancient annular amplitude `J_k` on the cubic-divergent bounded-Z recurrent branch.