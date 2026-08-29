# DSD M5-199 — Coherent Plateau Remote-Age Cap from Mean-Strain Action

Date: 2026-08-29

Parent: `DSD_M5_197_BROAD_ENSTROPHY_FIXED_SHELL_PLATEAU_OR_DERIVATIVE_ROUTING_AUDIT_2026-08-29.md`

Status: **NEW POSITIVE FINITE-AGE REDUCTION / A LOW-DERIVATIVE COHERENT ANNULAR PLATEAU THAT RETAINS ITS NORMALIZED MEAN THROUGH A FIRST-HITTING STAGE CANNOT LIVE AT ARBITRARILY LARGE SIMILARITY RADIUS / THE REQUIRED `~log q` MEAN-LONGITUDINAL-STRAIN ACTION IS LIMITED BY THE GLOBAL L2 STRAIN BUDGET, WHOSE ANNULAR MEAN DECAYS LIKE `R^{-3/2}` / COMBINING THIS WITH THE PURE VARIANCE STAGE-TIME CEILING GIVES AN EXPLICIT MAXIMUM RADIUS AND THEREFORE A FINITE GENERATION-AGE CAP / BEYOND THAT AGE THE PLATEAU MUST PAY TRANSPORT, DIFFUSION, COVARIANCE, DERIVATIVE, OR REPLACEMENT COST / GLOBAL REGULARITY UNPROVED.**

---

## 1. Plateau action input

Use the exact mean-vorticity plateau ledger.

For a retained coherent plateau on one fixed-shape annulus `A_R`, suppose the endpoint-amplitude and error terms satisfy

\[
\left|
\log\frac{|I_{\phi,1}|}{|I_{\phi,0}|}
\right|
+
|\mathcal R_{mv,j}|
\le
\log q-a_{mv}
\]

for some fixed

\[
\boxed{a_{mv}>0.}
\]

Then the stage must carry the longitudinal mean-strain action

\[
\boxed{
\int_{I_j}
 n_\phi^T\bar\Sigma_A n_\phi\,ds
\ge a_{mv}.
}
\]

For a robust benchmark one may require that endpoint plus error action consumes at most half the first-hitting amplification:

\[
\boxed{
a_{mv}=\frac12\log q.}
\]

No such numerical choice is needed for the symbolic result.

---

## 2. Mean strain on a remote finite annulus

Let

\[
A_R
=
\{R<|Y-X|<\lambda R\},
\qquad
\lambda=\sqrt q.
\]

Its volume is

\[
\boxed{
|A_R|
=c_\lambda R^3,
\qquad
c_\lambda
:=
\frac{4\pi}{3}(\lambda^3-1).
}
\]

The annular mean strain is

\[
\bar\Sigma_A
=
|A_R|^{-1}
\int_{A_R}\Sigma dY.
\]

By Cauchy--Schwarz,

\[
|\bar\Sigma_A|
\le
|A_R|^{-1/2}
\|\Sigma\|_{L^2(A_R)}
\le
|A_R|^{-1/2}
\|\Sigma\|_2.
\]

For an incompressible whole-space field,

\[
\|\Sigma\|_2^2
=
\frac12\|\Omega\|_2^2
=
\frac12 Z.
\]

On the bounded-`Z` recurrent corridor,

\[
Z\le Z_+.
\]

Therefore

\[
\boxed{
|\bar\Sigma_A|
\le
\sqrt{
\frac{Z_+}{2c_\lambda R^3}
}.
}
\]

This is a purely global `L2` consequence. No Biot--Savart pointwise estimate is needed.

---

## 3. Plateau action forces a stage-length lower bound

Since

\[
|n_\phi^T\bar\Sigma_A n_\phi|
\le
|\bar\Sigma_A|,
\]

the action floor implies

\[
a_{mv}
\le
L_j
\sqrt{
\frac{Z_+}{2c_\lambda R^3}
}.
\]

Hence every quiet retained plateau stage at radius `R` satisfies

\[
\boxed{
L_j
\ge
L_{plat,-}(R)
:=
 a_{mv}
\sqrt{
\frac{2c_\lambda R^3}{Z_+}
}.
}
\]

Thus the time required to amplify a coherent remote mean plateau grows like

\[
\boxed{R^{3/2}.}
\]

This is the key new scale separation.

---

## 4. Insert the pure variance stage ceiling

On the pure low-turnover variance corridor at the selected central tightness radius `R_Z`, the repository already proves

\[
\boxed{
L_j
\le
L_{var,+}
=
\Pi_{pure}(q)
\frac{R_Z^2}{\nu}.
}
\]

Therefore a quiet retained plateau at radius `R` can exist only if

\[
 a_{mv}
\sqrt{
\frac{2c_\lambda R^3}{Z_+}
}
\le
\Pi_{pure}(q)
\frac{R_Z^2}{\nu}.
\]

Solving for `R`,

\[
\boxed{
R
\le
R_{plat,+}
:=
\left[
\frac{\Pi_{pure}(q)}{a_{mv}}
\frac{R_Z^2}{\nu}
\sqrt{
\frac{Z_+}{2c_\lambda}
}
\right]^{2/3}.
}
\]

This is the finite remote-radius cap.

---

## 5. Eliminate `Z_+` by tightness

If the central `epsilon_Z`-tight corridor has

\[
Z_+
\le
\frac{4\pi}{3(1-\varepsilon_Z)}R_Z^3,
\]

then

\[
\frac{Z_+}{2c_\lambda}
\le
\frac{R_Z^3}
{2(1-\varepsilon_Z)(\lambda^3-1)}.
\]

Hence

\[
\boxed{
\frac{R_{plat,+}}{R_Z}
\le
C_{plat}(q,\varepsilon_Z,a_{mv})
\left(
\frac{R_Z}{\sqrt\nu}
\right)^{4/3},
}
\]

where

\[
\boxed{
C_{plat}
:=
\left[
\frac{\Pi_{pure}(q)}{a_{mv}}
\frac1{
\sqrt{2(1-\varepsilon_Z)(q^{3/2}-1)}
}
\right]^{2/3}.
}
\]

This is dimensionless and depends only on the formed corridor constants.

---

## 6. Convert radius cap to generation-age cap

Use generation-adapted shells based at the central tightness scale:

\[
R_k
=R_Z\lambda^k,
\qquad
\lambda=\sqrt q.
\]

A quiet retained plateau on shell `k` must satisfy

\[
\lambda^k
\le
C_{plat}
\left(
\frac{R_Z}{\sqrt\nu}
\right)^{4/3}.
\]

Therefore

\[
\boxed{
k
\le
k_{plat,+}
:=
\frac{
\log C_{plat}
+
\frac43\log(R_Z/\sqrt\nu)
}
{\log\lambda}.
}
\]

Only integer shell indices below this value can support a quiet retained coherent plateau.

Thus

\[
\boxed{
\text{quiet coherent plateau}
\Longrightarrow
\text{finite generation lag}.
}
\]

There is no arbitrarily old quiet plateau survivor on this corridor.

---

## 7. Robust `q=2`, quarter-tail benchmark

Take

\[
q=2,
\qquad
\lambda=\sqrt2,
\qquad
\varepsilon_Z=\frac14,
\]

and require at least half of the ideal plateau action to survive the endpoint/error ledger:

\[
\boxed{
a_{mv}=\frac12\log2.}
\]

Using

\[
\Pi_{pure}(2)
\approx1.4967761748,
\]

one obtains

\[
\boxed{
C_{plat}
\approx1.89460186.
}
\]

Hence

\[
\boxed{
\frac{R_{plat,+}}{R_Z}
\lesssim
1.89460186
\left(
\frac{R_Z}{\sqrt\nu}
\right)^{4/3}.
}
\]

At the new M5-194Z/M5-196 quarter-tail survival threshold

\[
R_Z
\approx
1.19924130\sqrt\nu,
\]

this gives

\[
\boxed{
\frac{R_{plat,+}}{R_Z}
\lesssim2.41394.
}
\]

Since

\[
(\sqrt2)^2=2,
\qquad
(\sqrt2)^3\approx2.828,
\]

the corresponding integer generation-adapted plateau lag satisfies

\[
\boxed{k\le2}
\]

at this benchmark.

In words: **near the smallest still-surviving quarter-tail radius, a quiet retained coherent plateau cannot sit three or more first-hitting generations away from the central core.**

For larger `R_Z/sqrt(nu)` the cap grows explicitly by the formula above; it remains finite for every fixed corridor parameter.

---

## 8. Meaning of failure of the age bound

Suppose a recurrent plateau witness appears at a shell with

\[
R>R_{plat,+}.
\]

Then it cannot simultaneously satisfy

1. retained normalized mean amplitude;
2. small plateau covariance error;
3. small relative transport error;
4. small viscous-boundary error;
5. the pure variance stage-time ceiling.

Therefore at least one typed exit must occur:

\[
\boxed{
T_{transport}
\lor
T_{replacement}
\lor
H_{derivative}
\lor
H_{diffusion}
\lor
R_{covariance}
\lor
\text{loss of pure variance/tightness corridor}.
}
\]

Thus excessive plateau age is itself a finite witness of leaving the quiet survivor.

---

## 9. Reconnection to fixed-lag genealogy

The existing fixed-lag packet identity/replacement gate is strongest when the remote witness can be assigned a finite generation age.

M5-199 supplies exactly that prerequisite for the coherent plateau branch.

On a low-derivative plateau, Poincare gives a nonzero mean-vorticity amplitude over a fixed-volume region. Stage-wide analyticity/regularity converts this into a coherent finite-scale vorticity population. Since its age is bounded by `k_plat,+`, only finitely many ancestor lags need be considered.

Therefore finite pigeonhole gives one recurrent lag `k_0` if the quiet plateau branch occurs at positive time density.

At that fixed lag, the existing genealogy machinery applies:

\[
\boxed{
\text{material contact/return}
\lor
\text{packet replacement}
\lor
\text{deformation/diffusion exposure}.
}
\]

The replacement side then enters the finite-memory positive-frequency exit theorem.

Hence the remote coherent plateau is no longer an all-age topology.

---

## 10. Firewall: this does not close the whole plateau branch by itself

The finite age cap is not a contradiction.

A coherent plateau may survive at one of the finitely many allowed near ages and repeatedly pay the required longitudinal strain action.

What M5-199 removes is the possibility that the broad enstrophy survivor hides in an **arbitrarily old, arbitrarily remote, low-gradient coherent plateau while all local finite-memory comparisons remain irrelevant**.

That escape is closed.

The remaining finite-age plateau cases must now be charged through existing material-contact/replacement/projective/Betchov ledgers.

---

## 11. Updated broad-enstrophy frontier

After M5-197--199:

\[
\boxed{
\text{broad enstrophy}
\Longrightarrow
\begin{cases}
\text{derivative shell}\to\text{finite frequency window},\\
\text{plateau shell}\to\text{finite age genealogy},\\
\text{loss of recurrent fixed-shell compactness}\to\text{escaping critical tail}.
\end{cases}
}
\]

This is a meaningful reduction in topology.

The `one broad coherent core` branch is replaced by a finite-age material/genealogy problem.

---

## 12. DSD verdict

### PROVED / COMPOSED

- mean strain of a radius-`R` annular plateau is bounded by `sqrt(Z_+/(2 c_lambda R^3))`;
- retained normalized plateau amplification requires a stage duration at least proportional to `R^(3/2)`;
- the pure variance stage ceiling yields an explicit maximum quiet plateau radius;
- generation-adapted shell geometry converts this to a finite lag cap;
- for `q=2`, quarter-tail, `a_mv=(1/2)log2`, and `R_Z=1.19924130 sqrt(nu)`, the benchmark cap is `k<=2`;
- plateau witnesses beyond the cap must activate an already typed transport/diffusion/covariance/derivative/replacement exit;
- positive-density quiet plateau recurrence can therefore be reduced to finitely many material ancestor lags.

### OPEN

- closure of all finitely many allowed plateau lags;
- exact constant transfer from plateau action into replacement/projective exits;
- the fixed-shell derivative quartic comparison;
- escaping critical tails;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]

---

## 13. Next target

The next shortest calculation is now finite.

For each allowed plateau lag

\[
0\le k\le k_{plat,+},
\]

combine the plateau mean-amplitude lower bound with the existing fixed-lag contact/replacement theorem.

The goal is to derive one uniform positive lower bound on either

- material contact/return weight;
- replacement volume fraction;
- or deformation/diffusion exposure

that depends only on the finite corridor constants and `k_plat,+`.

Because the lag set is finite, the minimum of these positive constants is itself positive. If successful, the broad plateau branch will enter the already established finite-memory positive-frequency costed-exit mechanism with no remaining all-age loss.