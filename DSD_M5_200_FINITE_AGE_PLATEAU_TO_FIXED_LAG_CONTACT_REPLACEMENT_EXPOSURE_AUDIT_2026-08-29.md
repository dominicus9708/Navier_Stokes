# DSD M5-200 — Finite-Age Plateau to Fixed-Lag Contact / Replacement / Exposure

Date: 2026-08-29

Parent: `DSD_M5_199_COHERENT_PLATEAU_REMOTE_AGE_CAP_FROM_MEAN_STRAIN_ACTION_AUDIT_2026-08-29.md`

Status: **POSITIVE TERMINAL-LEAF REMOVAL / THE QUIET COHERENT PLATEAU BRANCH IS REDUCED FROM AN ALL-AGE REMOTE STRUCTURE TO FINITELY MANY GENERATION LAGS, AND FINITE PIGEONHOLE SELECTS ONE RECURRENT FIXED LAG / THE EXISTING FIXED-LAG PACKET IDENTITY THEOREM THEN GIVES A QUANTITATIVE CONTACT--REPLACEMENT--EXPOSURE TRICHOTOMY / A HALF-PACKET CONTACT THRESHOLD MAKES THE REPLACEMENT VOLUME FRACTION EXPLICITLY POSITIVE / REPLACEMENT REJOINS THE FINITE-MEMORY POSITIVE-FREQUENCY EXIT THEOREM, EXPOSURE REJOINS H/T DERIVATIVE-DEFORMATION COSTS, AND CONTACT REJOINS THE MATERIAL-RETURN GENEALOGY / THE COHERENT PLATEAU IS THEREFORE NO LONGER AN INDEPENDENT TERMINAL BRANCH / GLOBAL REGULARITY UNPROVED.**

---

## 1. Finite-age input from M5-199

On the pure variance/tightness corridor, a quiet retained plateau can occur only at generation-adapted shell lags

\[
0\le k\le K_{plat}<\infty,
\]

where one may take

\[
K_{plat}=\lfloor k_{plat,+}\rfloor.
\]

For the robust `q=2`, quarter-tail benchmark near

\[
R_Z=1.19924130\sqrt\nu,
\]

M5-199 gives

\[
\boxed{K_{plat}\le2.}
\]

The symbolic argument below only uses finiteness.

---

## 2. Positive-density plateau recurrence selects one lag

Let `P` be the positive-density recurrent set on which the fixed-shell Poincare split lands in the low-derivative coherent plateau branch and the plateau survives the M5-199 quiet-age test.

Partition it by generation lag:

\[
P=\bigcup_{k=0}^{K_{plat}}P_k.
\]

Because the union is finite and

\[
\mu(P)>0,
\]

there exists one

\[
\boxed{k_0\in\{0,\ldots,K_{plat}\}}
\]

such that

\[
\boxed{
\mu(P_{k_0})=:d_{plat}>0.
}
\]

Thus the plateau branch is now a **fixed finite-lag recurrent event class**.

No all-age diagonal extraction is needed.

---

## 3. Plateau annulus contains a fixed-scale Eulerian packet

The recurrent plateau shell already inherits the fixed-shell critical enstrophy lower bound

\[
R_{k_0}Z_{A_{k_0}}
\ge J_*>0.
\]

Cover the fixed-aspect annulus by finitely many balls of radius

\[
\rho_*:=\sigma R_{k_0}
\]

for one fixed `sigma>0`.

The existing fixed-shell covering lemma yields a ball with

\[
\boxed{
\rho_*
\int_{B_{\rho_*}(y_*)}|\Omega_j|^2dy
\ge\kappa_*>0.
}
\]

The stage-wide first-hitting analyticity theorem then gives

\[
\eta_*
:=
\left(
\frac{3\kappa_*}{4\pi\rho_*^4}
\right)^{1/2}>0,
\]

and, with the uniform stage Lipschitz constant `C_1`,

\[
\boxed{
d_*:=
\min\left\{
\frac{\rho_*}{4},
\frac{\eta_*}{2C_1}
\right\}>0.
}
\]

Hence there is a coherent Eulerian packet

\[
C_j(t)=B_{d_*r_j}(x_c(t))
\]

on which

\[
\boxed{
|\omega|
\ge
c_EW_j,
\qquad
c_E:=\eta_*/2>0.
}
\]

All constants are fixed on the recurrent lag `k_0`.

---

## 4. Convert to ancestor units

Set

\[
n=j-k_0.
\]

Then

\[
r_n=q^{k_0/2}r_j.
\]

Therefore

\[
\operatorname{rad}C_j
=
 d_*q^{-k_0/2}r_n
=:
 d_nr_n,
\]

with

\[
\boxed{d_n=d_*q^{-k_0/2}>0.}
\]

Likewise the packet amplitude relative to the ancestor first-hitting threshold is

\[
|\omega|
\ge
c_Eq^{k_0}W_n
=:
c_nW_n,
\]

with

\[
\boxed{c_n=c_Eq^{k_0}>0.}
\]

Thus the current plateau packet and the stage-`n` material ancestor live in one fixed natural scale class.

---

## 5. Imported material ancestor and quiet exposure conditions

Let

\[
A_n^0=B_{a_0r_n}(x_n)
\]

be the stage-`n` maximum packet and transport it by the Lagrangian flow to the current event time:

\[
A_n(t)=\Phi_{t_n,t}(A_n^0).
\]

Use the already defined finite-lag exposure quantities

\[
\Sigma_n
=
\int_{t_n}^{t}
\sup_{A_n(s)}|S|ds,
\]

\[
\Lambda_n
=
\int_{t_n}^{t}
\sup_{H_n(s)}|\nabla u|ds,
\]

and

\[
\mathcal D_n
=
\frac\nu{W_n}
\int_{t_n}^{t}
\sup_{A_n(s)}|\Delta\omega|ds.
\]

Fix a finite deformation threshold `L>0`.

The quiet finite-lag corridor is

\[
\boxed{
\Sigma_n\le L,
\qquad
\Lambda_n\le L,
\qquad
\mathcal D_n\le\frac{b_0}{2}e^{-L}.
}
\]

Failure of any one is already an exposure payment.

---

## 6. Choose a canonical half-packet contact threshold

The current packet volume in ancestor units is

\[
\frac{|C_j(t)|}{r_n^3}
=
\frac{4\pi}{3}d_n^3
=:
V_C>0.
\]

Rather than introducing an arbitrary small contact parameter, choose

\[
\boxed{
\chi_0:=\frac12V_C
=
\frac{2\pi}{3}d_n^3>0.
}
\]

Define the normalized current-to-ancestor contact fraction

\[
\chi_{n,j}(t)
:=
\frac{|C_j(t)\cap A_n(t)|}{r_n^3}.
\]

Then every quiet event belongs to one of two quantitatively separated branches.

---

## 7. Contact branch

If

\[
\boxed{
\chi_{n,j}(t)
\ge
\chi_0,
}
\]

then at least half of the coherent current plateau packet volume lies in the transported material descendant of the fixed-lag first-hitting ancestor.

Since

\[
|\omega|\ge c_nW_n
\]

on `C_j`, the contact portion carries a fixed critical gradient/enstrophy witness.

Using the pointwise identity/inequality already employed in the fixed-lag theorem,

\[
|\omega|^2\le2|\nabla u|^2,
\]

one gets

\[
\boxed{
r_n
\int_{C_j\cap A_n(t)}|\nabla u|^2dx
\ge
\frac{c_n^2}{2}\nu^2\chi_0
>0.
}
\]

Thus contact is a genuine material-return certificate, not a geometric overlap with vanishing weight.

This branch rejoins the existing weighted-return/genealogy ledger.

---

## 8. Replacement branch

If

\[
\chi_{n,j}(t)<\chi_0,
\]

then more than half of the current coherent packet lies outside the transported ancestor:

\[
|C_j(t)\setminus A_n(t)|
>
\frac12V_Cr_n^3.
\]

Hence

\[
\boxed{
|C_j(t)\setminus A_n(t)|
\ge
c_Vr_n^3,
\qquad
c_V:=\frac12V_C
=
\frac{2\pi}{3}d_n^3>0,
}
\]

while

\[
|\omega|\ge c_nW_n
\]

there.

Under the quiet ancestor conditions, the transported old packet still contains its coherent inner descendant with nonzero amplitude.

Therefore the same time contains

1. the retained material ancestor population;
2. a fixed positive-volume current high-vorticity population outside that ancestor.

This is precisely the existing packet-replacement/multicore witness.

Because `c_V>0` is fixed for the recurrent lag, the replacement fraction cannot shrink to zero along the selected event set.

---

## 9. Exposure branch

If the quiet conditions fail, then at least one of

\[
\boxed{
\Sigma_n>L,
\qquad
\Lambda_n>L,
\qquad
\mathcal D_n>\frac{b_0}{2}e^{-L}
}
\]

holds over a fixed finite-lag comparison window.

Since `k_0` is fixed, these are genuine fixed-window deformation/diffusion payments.

Thus the full plateau event satisfies

\[
\boxed{
\text{material contact}
\lor
\text{fixed-fraction replacement}
\lor
\text{finite-lag exposure}.
}
\]

No fourth quiet genealogy class remains.

---

## 10. Positive-density recurrence and finite pigeonhole

The recurrent lag set `P_{k_0}` has positive density `d_plat>0`.

Partition it into

\[
P_{contact},
\qquad
P_{replace},
\qquad
P_{exposure}.
\]

At least one has positive density.

### If contact has positive density

The plateau branch rejoins the recurrent material-return ledger with a fixed positive contact weight.

### If replacement has positive density

The existing finite-memory replacement theorem applies. A bounded coherent core can store only finitely many distinguishable fixed-flux populations, so positive-density replacement forces positive-frequency exits of one of the typed forms

\[
X_{visc},
\quad
X_{proj},
\quad
X_{export},
\quad
X_H.
\]

Thus quiet local multiflux storage cannot be the terminal branch.

### If exposure has positive density

The branch directly rejoins deformation, diffusion, Hessian/palinstrophy, or material-turnover ledgers.

Therefore the plateau branch has been completely routed into already formed long-time channels.

---

## 11. Uniformity over the finite age set

The preceding argument selected one positive-density lag `k_0` and therefore already has fixed positive constants.

Equivalently, because

\[
0\le k\le K_{plat}<\infty,
\]

one may construct constants for each admissible lag and take their finite minimum wherever all lag branches are simultaneously retained.

For example,

\[
d_{min}
:=
\min_{0\le k\le K_{plat}}d_k>0
\]

provided the corresponding shell-packet lower bounds are fixed on the retained lag classes.

Then

\[
\chi_{min}
:=
\frac{2\pi}{3}d_{min}^3>0
\]

is a uniform half-packet contact/replacement threshold.

The finite-pigeonhole version is safer when different lag classes carry different extracted `kappa_*` constants; no infinite infimum is ever required.

---

## 12. What this closes

The following proposed terminal survivor is removed:

\[
\boxed{
\text{broad low-gradient coherent plateau}
\text{ persisting at remote scales without material identity cost}.
}
\]

After M5-199 the age is finite; after M5-200 each recurrent finite-age event is material contact, replacement, or exposure.

Hence the coherent plateau is not a new endgame topology.

---

## 13. What remains open

This routing does not by itself prove global regularity.

The remaining terminal frontiers are now more concentrated:

1. **material return/contact:** show recurrent fixed-weight return is incompatible with the final active-core/tail ledger or classify it as historical replenishment;
2. **replacement exits:** close the remaining finite constant comparisons for viscous/projective/H exits, while export may still feed the escaping critical-tail topology;
3. **fixed-shell derivative branch:** resolve the quartic frequency-window constant test from M5-198;
4. **escaping critical tail / generic critical drift:** close the nonrecurrent endpoint tail;
5. maintain exhaustiveness when tightness/variance assumptions fail.

The broad coherent-core/plateau ambiguity itself is no longer on this list.

---

## 14. DSD verdict

### PROVED / COMPOSED

- finite plateau-age cap gives finitely many lags;
- positive-density plateau recurrence selects one fixed lag;
- fixed-shell critical mass plus analyticity gives a coherent Eulerian packet with fixed positive size and amplitude;
- in ancestor units this packet has fixed positive radius and amplitude;
- choosing half its volume as contact threshold gives a quantitative contact/replacement split;
- quiet-condition failure is a fixed-lag exposure payment;
- positive-density replacement rejoins the already proved finite-memory positive-frequency exit mechanism;
- the coherent plateau is removed as an independent terminal branch.

### OPEN

- final closure of material return/contact;
- export/escaping critical tail;
- derivative frequency-window constants;
- all finite exit constant comparisons;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]

---

## 15. Next target

After eliminating the plateau as an independent leaf, the shortest remaining structural branch is **positive-density material contact/return**.

The next audit should combine the fixed contact weight

\[
\mathfrak R_{k_0}>0
\]

with the existing recurrent return-weight / historical-replenishment ledger and determine whether repeated return

- forces a finite positive recurrent dissipation/deformation cost;
- creates an impossible multiplicity/recycling count;
- or necessarily transfers a fixed critical amount to the escaping tail.

This is now a genuinely narrower problem than the original broad-core ambiguity.