# DSD M5-197 — Broad Enstrophy Fixed-Shell Plateau-or-Derivative Routing Audit

Date: 2026-08-29

Parent: `DSD_M5_196_ENSTROPHY_QUANTILE_RADIUS_ENVELOPE_AND_MINIMUM_TAIL_FRACTION_AUDIT_2026-08-29.md`

Status: **POSITIVE STRUCTURAL REDUCTION / THE BROAD-ENSTROPHY SURVIVOR CANNOT BE TREATED AS A NEW TOPOLOGICAL `ONE BIG CORE` LEAF / ON A POSITIVE-DENSITY RECURRENT SET THE QUANTILE-ENVELOPE TAIL FEEDS THE EXISTING FIXED-SHELL EXTRACTION, PRODUCING ONE FINITE GENERATION-ADAPTED ANNULUS WITH SCALE-CRITICAL ENSTROPHY / ON THAT ANNULUS POINCARE GIVES AN EXACT DERIVATIVE-VERSUS-COHERENT-PLATEAU DICHOTOMY / THE DERIVATIVE SIDE IS AN `H`-TYPE LOCAL PALINSTROPHY PAYER, WHILE THE LOW-DERIVATIVE SIDE IS A NONZERO MEAN-VORTICITY PLATEAU AND REJOINS THE EXISTING MEAN-STRETCHING -> BETCHOV/POSITIVE-MIDDLE -> RIBBON/PROJECTIVE/TURNOVER MAINLINE / PURE TOPOLOGICAL CONNECTEDNESS IS EXPLICITLY REJECTED AS A COERCIVE DESCRIPTOR / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input from M5-196

For a surviving pure branch, the quantile-radius envelope gives for every admissible tail fraction `epsilon`

\[
R_\varepsilon(s)\ge T_q(\varepsilon)\sqrt\nu.
\]

Equivalently, at each fixed normalized radius `R` below the corresponding threshold, a definite enstrophy fraction must remain outside `B_R`.

For `q=2`, for example,

\[
R=\sqrt\nu
\quad\Longrightarrow\quad
\frac{\int_{|Y-X|>R}|\Omega|^2}{Z}
\gtrsim0.3216
\]

on the pure quantile corridor.

This is not yet a statement about whether the exterior mass is

- part of one broad connected core,
- a separate coherent packet,
- or diffuse critical halo.

The present audit removes the first ambiguity at the correct quantitative level.

---

## 2. Use recurrent high-enstrophy times

The bounded recurrent first-hitting branch already contains a positive-density set of times on which

\[
Z(s)\ge z_*>0
\]

for one fixed `z_*`.

Choose one fixed radius `R_0` from the M5-196 envelope and let the corresponding compulsory exterior fraction be `epsilon_0>0`.

Then on that positive-density set,

\[
\boxed{
\int_{|Y-X|>R_0}|\Omega|^2dY
\ge
m_*:=\varepsilon_0z_*>0.
}
\]

Thus the broad-distribution survivor satisfies the exact hypothesis of the existing remote-witness fixed-shell extraction theorem.

No claim is made that every late time has the same `z_*`; positive-density recurrence is sufficient.

---

## 3. Import fixed-shell extraction

Let

\[
\lambda=\sqrt q,
\qquad
R_k=R_0\lambda^k,
\qquad
A_k=\{R_k\le |Y-X|<\lambda R_k\}.
\]

Write

\[
m_k(s)=\int_{A_k}|\Omega|^2dY.
\]

The existing fixed-shell theorem proves that from the positive-density exterior witness there exist

\[
k_0<\infty,
\qquad
J_*>0,
\qquad
B_*\text{ of positive time density},
\]

such that for all `s in B_*`,

\[
\boxed{
R_{k_0}m_{k_0}(s)\ge J_*>0.
}
\]

Set

\[
R_*:=R_{k_0},
\qquad
A_*:=A_{k_0}.
\]

Hence

\[
\boxed{
m_*(s):=\int_{A_*}|\Omega|^2dY\ge\frac{J_*}{R_*}.}
\]

Because `k_0` is finite, `R_*` is one fixed similarity radius and one fixed generation lag.

Therefore the broad survivor cannot evade all finite annuli merely by moving its exterior mass to larger and larger shell indices.

---

## 4. Firewall: topological connectedness is not a coercive descriptor

One tempting branch description is

\[
\text{one connected broad core}
\quad\text{versus}\quad
\text{multiple packets}.
\]

This is not quantitatively valid.

Two high-vorticity regions may be joined by an arbitrarily low-amplitude, thin transition set. Connectivity of the support or of a very low superlevel set can therefore be changed without imposing a fixed lower bound on

\[
Z,
\quad Q,
\quad\text{or any existing finite-stage dissipation ledger}.
\]

Conversely, a single connected region may contain multiple dynamically independent high-amplitude populations.

Hence

\[
\boxed{
\text{topological connectedness alone}
\not\Longrightarrow
\text{finite Navier--Stokes cost}.
}
\]

DSD therefore rejects `connected broad core` as a primitive terminal channel.

The correct formed variables on `A_*` are the annular enstrophy and gradient energy.

---

## 5. Annular Poincare split

Define

\[
Z_A(s):=\int_{A_*}|\Omega|^2dY,
\]

\[
Q_A(s):=\int_{A_*}|\nabla\Omega|^2dY,
\]

and the annular mean

\[
\bar\Omega_A(s)
:=
|A_*|^{-1}
\int_{A_*}\Omega dY.
\]

Because `A_*` has fixed aspect ratio `lambda`, Poincare gives a fixed geometric constant `C_A` such that

\[
\boxed{
\int_{A_*}|\Omega-\bar\Omega_A|^2dY
\le
C_A R_*^2Q_A.
}
\]

Fix any

\[
0<\theta<C_A^{-1}.
\]

Then every `s in B_*` belongs to exactly one of the following two quantitative branches.

### D: derivative annulus

\[
\boxed{
R_*^2Q_A\ge\theta Z_A.
}
\]

### P: coherent plateau annulus

\[
\boxed{
R_*^2Q_A<\theta Z_A.
}
\]

No third static annular possibility remains.

---

## 6. Derivative branch has a fixed local palinstrophy payer

On branch D, using

\[
Z_A\ge J_*/R_*,
\]

we obtain

\[
Q_A
\ge
\frac{\theta Z_A}{R_*^2}
\ge
\boxed{
\frac{\theta J_*}{R_*^3}>0.
}
\]

Because `R_*` and `J_*` are fixed after shell extraction, this is a genuine fixed positive local derivative cost on every D-event.

If D occupies positive time density, it supplies a positive recurrent local-palinstrophy payer and therefore routes to the existing

\[
H_{1,crit}^{tail},
\quad
H_{2,crit}^{tail},
\quad
\text{palinstrophy/hyperpalinstrophy},
\]

or related derivative ledgers according to which stronger corridor is assumed.

Status: **ROUTED TO EXISTING `H`-TYPE COST; no new universal contradiction asserted here.**

---

## 7. Low-derivative branch forces a nonzero mean plateau

On branch P,

\[
\begin{aligned}
Z_A
&=
\int_{A_*}|\Omega-\bar\Omega_A|^2dY
+
|A_*||\bar\Omega_A|^2\\
&\le
C_AR_*^2Q_A
+
|A_*||\bar\Omega_A|^2.
\end{aligned}
\]

Hence

\[
|A_*||\bar\Omega_A|^2
\ge
(1-C_A\theta)Z_A.
\]

Using the fixed-shell lower bound,

\[
\boxed{
|A_*||\bar\Omega_A|^2
\ge
(1-C_A\theta)\frac{J_*}{R_*}.
}
\]

Since

\[
|A_*|=c_\lambda R_*^3
\]

for a fixed geometric constant `c_lambda>0`,

\[
\boxed{
|\bar\Omega_A|
\ge
\left(
\frac{(1-C_A\theta)J_*}{c_\lambda}
\right)^{1/2}
R_*^{-2}
=:m_A>0.
}
\]

Thus the low-gradient annulus is not merely diffuse exterior mass. It carries a fixed nonzero mean-vorticity vector on the recurrent fixed shell.

This is exactly the **coherent annular plateau** isolated in the earlier annular-mass audit.

---

## 8. Dynamic plateau routing

Static coherence is not itself a contradiction.

The existing mean-vorticity plateau stage ledger gives the correct dynamic split.

If the same normalized plateau is retained coherently through a geometric first-hitting stage, amplification of the physical vorticity scale forces a positive mean longitudinal-strain action of order the first-hitting gain:

\[
\boxed{
A_m
=
\int_I n^T\bar\Sigma_A n\,ds
\ge a_m>0
}
\]

up to explicitly typed transport, diffusion, covariance and endpoint errors.

The existing plateau-to-Betchov bridge then converts retained mean action into actual vortex-stretching action:

\[
\boxed{
\text{retained plateau}
\Longrightarrow
\text{positive actual stretching}
}
\]

unless one of those error channels is already large.

Actual positive stretching is then split into

\[
\boxed{
\text{positive-middle source action}
\quad\lor\quad
\text{Betchov mismatch/residual}.
}
\]

On the positive-middle source-active part, the alignment-free transverse interlacing lemma gives

\[
|D_{\perp}|_F
\ge
\frac{\gamma}{\sqrt2},
\qquad
\gamma
=
\frac{\Omega^TS\Omega}{|\Omega|^2}>0.
\]

Therefore retained plateau recurrence rejoins the already existing

\[
\boxed{
\text{ribbonization/shape change}
\lor
\text{projective/eigenframe rotation}
\lor
\text{material turnover/replacement}
\lor
\text{pressure/derivative/Betchov residual}.
}
\]

---

## 9. Failure of plateau retention is already a typed exit

If the annular mean plateau present on `B_*` does **not** persist coherently through the needed comparison interval, this does not create a new quiet branch.

Loss of the plateau must occur through at least one formed channel already present in the mean-vorticity ledger:

- material/boundary transport;
- diffusion/erosion;
- covariance/shape loss;
- center/genealogy replacement;
- derivative failure.

Thus

\[
\boxed{
\text{plateau non-persistence}
\Longrightarrow
T\text{/}H\text{/residual exit}.
}
\]

The branch is not allowed to disappear from one stage and reappear later without being charged to one of these channels.

---

## 10. Updated broad-enstrophy tree

Combining M5-196 with the existing fixed-shell and plateau machinery gives

\[
\boxed{
\begin{aligned}
\text{broad enstrophy survivor}
&\Longrightarrow
\text{positive-density fixed shell}\\
&\Longrightarrow
\begin{cases}
\text{fixed local derivative payer},\\
\text{coherent annular plateau}.
\end{cases}
\end{aligned}
}
\]

The plateau branch further satisfies

\[
\boxed{
\text{coherent plateau}
\Longrightarrow
\text{retained mean-stretching action}
\lor
T/H/\text{residual exit}.
}
\]

and retained mean stretching satisfies

\[
\boxed{
\text{stretching}
\Longrightarrow
\text{positive-middle transverse action}
\lor
\text{Betchov residual}.
}
\]

Therefore `one broad coherent core` is **not a new terminal leaf**.

---

## 11. What remains open after this routing

This audit is a structural reduction, not yet a proof of global regularity.

The remaining quantitative obligations are now concentrated in already existing channels:

1. show that positive-density fixed-shell derivative payment cannot survive all global/recurrent derivative budgets;
2. complete the constant transfer from plateau mean-stretching action to the finite-stage anti-ribbon/projective thresholds where required;
3. close or further classify recurrent Betchov residual that is spatially remote/diffuse;
4. close permanent/exported critical-tail topology when it escapes the recurrent fixed-shell core;
5. preserve exhaustiveness when the pure variance/tightness assumptions fail.

The important simplification is that **broad connectedness itself no longer appears in the frontier.**

---

## 12. DSD verdict

### PROVED / IMPORTED AND COMPOSED

- M5-196 broad quantile mass yields a positive exterior witness on recurrent high-enstrophy times.
- Existing fixed-shell extraction converts this to one finite recurrent annulus with `R_* Z_A >= J_*>0`.
- Poincare gives an exact derivative-versus-plateau split on that annulus.
- The derivative side has a fixed positive local palinstrophy payer.
- The low-derivative side has a fixed nonzero mean-vorticity plateau.
- Existing plateau dynamics route retained plateaux to stretching and then to positive-middle/Betchov/transverse-action machinery.
- Plateau loss is a typed transport/diffusion/covariance/turnover/derivative exit.
- Pure topological connectedness is not a legitimate coercive proof variable.

### NOT YET CLOSED

- all recurrent derivative payers;
- all Betchov residual/export tail subbranches;
- all constants in the plateau-to-projective finite-stage comparison;
- the full singular branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]

---

## 13. Next target

The highest-value next calculation is no longer geometric connectedness.

It is the derivative side of the fixed-shell dichotomy:

\[
\boxed{
R_*^2Q_A\ge\theta Z_A,
\qquad
R_*Z_A\ge J_*.
}
\]

Because the shell and event density are fixed, this creates a fixed positive **recurrent local palinstrophy rate**.

The next audit should determine whether this rate can be inserted into the existing global/enstrophy/H1 telescoping ledger to produce a true finite-budget contradiction, or whether it necessarily moves outward as a critical derivative tail. That is now the shortest path to deciding whether the derivative branch closes or merges with the remaining escaping-tail frontier.