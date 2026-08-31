# DSD M5-396 — Scale-invariant source flux has no age dilution; the missing object is an interaction charge

Date: 2026-08-31

Status: **THE AGE-DILUTION MECHANISM OF M5-385 CANNOT BE TRANSFERRED TO THE NATURAL DUAL-FLUX SOURCE GRAPH / THE AFFINE SHIELD REQUIRED A CIRCULATION `Gamma_j` THAT GREW WITH GENERATION, BUT EVERY NATURAL FIRST-HITTING MAIN OR COMPANION CARRIER REQUIRES ONLY A SCALE-INVARIANT FLUX OF ORDER `W_j r_j^2 = nu` / HENCE ONE OLD QUIET MATERIAL-FLUX LINEAGE CAN IN PRINCIPLE REMAIN AN ORDER-ONE SOURCE AT ARBITRARILY LARGE AGE / IF IT DOES, M5-393 FORCES GEOMETRIC FUNNEL DEFORMATION AND BKM-COMPATIBLE LIPSCHITZ ACTION; IF IT DOES NOT, M5-395 PRODUCES A FIXED NON-PARENT REPLACEMENT FLUX / THE PHYSICAL ENERGY/ENSTROPHY-DISSIPATION COST OF ONE NATURAL PACKET PER GEOMETRIC STAGE SCALES LIKE A POSITIVE POWER OF `r_j` AND IS SUMMABLE, SO FINITE ENERGY ALONE CANNOT CLOSE EITHER OLD REUSE OR CONTINUAL FRESH REPLACEMENT / THE REMAINING LOCAL HARD CORE IS THEREFORE A NONSUMMABLE MAIN-SOURCE INTERACTION/STRAIN CHARGE, NOT A SINGLE-CARRIER AGE OR ENERGY BUDGET / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-394 converts a natural productive Biot--Savart source into a formed companion flux carrier.

M5-395 converts fixed target-volume replacement into fixed target-flux replacement.

This suggests a source genealogy split:

\[
\text{old companion reuse}
\quad\text{vs}\quad
\text{non-parent companion replacement}.
\]

A tempting shortcut would be to import the age-dilution argument of M5-385 and claim that an old source becomes irrelevant after many generations.

That shortcut is false.

The present note proves the exact reason and identifies what type of estimate is actually still missing.

---

## 2. The M5-385 shield circulation is not scale invariant

On the saturated affine-shield corridor of M5-385,

\[
\Gamma_j\asymp r_j^{-2/5},
\]

and

\[
r_{j+k}=q^{-k/2}r_j.
\]

Therefore

\[
\Gamma_{j+k}
\asymp
q^{k/5}\Gamma_j.
\]

An age-`k` quiet descendant retaining circulation comparable to its historical value can supply only

\[
O(q^{-k/5})
\]

of the later required shield circulation.

That is the origin of the M5-385 age-dilution law.

---

## 3. Natural first-hitting source flux is exactly scale invariant

For every first-hitting stage,

\[
W_jr_j^2=\nu.
\]

The central Taylor carrier carries

\[
\Phi_j^{main}\ge c_m\nu,
\]

while the M5-394 natural companion carries

\[
\Phi_j^{src}\ge c_s\nu.
\]

The constants are independent of the late stage index.

Thus the required source-flux scale is

\[
\boxed{
\Phi_{req,j}\asymp\nu
\qquad\text{for every }j.
}
\]

There is no factor analogous to

\[
q^{k/5}
\]

in the required natural source flux.

---

## 4. Source-age relevance does not decay

Let a material source-flux carrier `alpha` be formed at generation `m` with

\[
|\Phi_\alpha(t_m)|\ge c_\alpha\nu.
\]

Call its later evolution **quiet in flux** if its material-surface flux remains comparable:

\[
|\Phi_\alpha(t)|\ge c_q\nu
\]

whenever it is reused as a retained source carrier.

Suppose it is reused at generation

\[
j=m+k.
\]

The current source requirement is still only

\[
\Phi_{req,j}\asymp\nu.
\]

Therefore its possible current supply fraction is

\[
\frac{|\Phi_\alpha(t_j)|}{\Phi_{req,j}}
\gtrsim
c>0,
\]

with no decay in `k`.

Hence

\[
\boxed{
\text{there is no source-flux analogue of }
q^{-k/5}\text{ age dilution.}
}
\]

This is a structural difference, not a technical gap.

---

## 5. DSD correction to the source genealogy

The source graph must therefore retain two genuine possibilities.

### A. Arbitrarily old persistent source reuse

One material-flux lineage can remain relevant at arbitrarily late first-hitting generations.

### B. Continual non-parent source replacement

The source flux at later generations is repeatedly carried by material labels outside the selected previous source lineage.

By M5-395, every fixed target replacement event carries a fixed directed non-parent flux of order `nu`.

Thus

\[
\boxed{
G_{\rm dual\,flux}^{formed}
\Longrightarrow
R_{\rm old\ source\ flux}
\lor
T_{\rm fixed\ source\ flux\ replacement}
}
\]

modulo projective/remote/viscous-flux exits already typed in M5-393--395.

Neither branch may be deleted by an age argument.

---

## 6. What arbitrarily old reuse actually forces

Assume a stage-`m` source surface remains a fixed-flux descendant at stage `m+k`.

M5-393 gives the material cross-sectional contraction

\[
\frac{|S_m^k|}{|S_m^0|}
\lesssim
q^{-k}.
\]

Hence at some retained material point the deformation gradient satisfies

\[
\sigma_1(F)
\gtrsim
q^k.
\]

Consequently

\[
\boxed{
\int_{t_m}^{t_{m+k}}
\|\nabla u(t)\|_\infty dt
\ge
k\log q-O(1).
}
\]

This is a real quantitative cost.

But it is exactly of the type expected under a hypothetical BKM blow-up.

Therefore

\[
\boxed{
\text{old source reuse}
\not\Longrightarrow
\bot
}
\]

from deformation action alone.

Calling the linear-in-generation Lipschitz action a contradiction would be circular.

---

## 7. Two persistent flux carriers do not double the sup-norm cost

At a natural productive event there are at least two formed flux objects:

1. the main first-hitting carrier;
2. the misaligned companion source carrier.

If both persist materially, each may require strong deformation.

However, the estimate

\[
\int\|\nabla u\|_\infty dt
\]

is a spatial supremum.

The same large strain field can in principle pay deformation for more than one nearby carrier simultaneously.

Therefore one must not add two BKM lower bounds as if they were independent charges.

Symbolically,

\[
\boxed{
\text{two persistent funnels}
\not\Longrightarrow
2\times\text{independent Lipschitz budget}.
}
\]

This is the same common-center/common-budget discipline used in the earlier shell audits.

---

## 8. Fresh natural packets are not excluded by the Leray energy budget

Now consider continual non-parent source replacement.

At generation `j`, M5-394 provides a coherent source ball of radius

\[
\asymp r_j
\]

on which

\[
|\omega|\gtrsim W_j
=\frac{\nu}{r_j^2}.
\]

Thus the instantaneous local enstrophy scale is

\[
\int_{B_{cr_j}}|\omega|^2dx
\gtrsim
W_j^2r_j^3
\asymp
\boxed{
\frac{\nu^2}{r_j}.
}
\]

This diverges as `r_j -> 0` at the event time.

But the Leray energy inequality controls the **time integral** of enstrophy,

\[
\nu\int\|\omega(t)\|_2^2dt,
\]

not its instantaneous value.

A natural parabolic stage has time scale

\[
\Delta t_j\asymp\frac{r_j^2}{\nu}.
\]

If a packet of this natural size persists for an order-one normalized time, its dissipation charge has the scaling

\[
\begin{aligned}
\nu\Delta t_j
\left(\frac{\nu^2}{r_j}\right)
&\asymp
\nu
\frac{r_j^2}{\nu}
\frac{\nu^2}{r_j}\\
&=
\boxed{\nu^2r_j.}
\end{aligned}
\]

Since

\[
r_j=r_0q^{-j/2},
\]

we have

\[
\boxed{
\sum_j\nu^2r_j<\infty.
}
\]

Therefore even one fully formed fresh natural source packet per geometric stage is **compatible in scaling with the finite Leray dissipation budget**.

This is the same summability obstruction encountered in several earlier local-packet charges.

---

## 9. Scope of the time-persistence estimate

Section 8 is a scaling anti-proof, not an unconditional theorem that every source packet persists for a full natural time.

If the packet loses coherence faster than an order-one normalized time, that rapid loss is already a reformation/projective/viscous-flux event.

If the packet remains quiet over a natural time, its Leray cost is `~nu^2 r_j`, which is summable.

Thus either way, the ordinary energy budget does not produce a new contradiction:

\[
\boxed{
\text{rapid loss}
\to T/H,
\qquad
\text{quiet natural persistence}
\to\text{summable Leray charge}.
}
\]

---

## 10. Finite-memory counting from M5-357 also does not transfer automatically

M5-357 obtained a scale-independent energy floor for a different shield descendant:

\[
E_j^{desc}\gtrsim1.
\]

That gave a uniform bound on the number of simultaneously quiet shield descendants.

The natural source carrier has a different scaling.

Its characteristic velocity scale is

\[
U_j\sim W_jr_j\sim\frac\nu{r_j},
\]

and its characteristic volume is `r_j^3`, so the natural kinetic-energy scale is

\[
U_j^2r_j^3
\sim
\boxed{\nu^2r_j},
\]

which tends to zero.

Hence no scale-independent simultaneous-count bound follows from kinetic energy by dimensional scaling alone.

Any future finite-memory theorem for natural source carriers must use a stronger interaction or topology charge, not the M5-357 shield-energy floor.

---

## 11. What is genuinely non-summable per first-hitting stage

The first-hitting record itself does provide a scale-invariant action:

\[
\boxed{
\int_{I_j}G_M(t)dt
\ge\log q,
}
\]

where `G_M` is the positive longitudinal stretching rate at vorticity maxima.

M5-362 identifies the source of this stretching through the angular Biot--Savart network.

Therefore the natural-source interaction carries an order-one dimensionless action per stage.

Summing over infinitely many stages gives

\[
\sum_j\int_{I_j}G_Mdt=\infty.
\]

But this is again BKM-compatible.

The missing estimate is not a lower bound.

The lower bound already exists.

The missing estimate is an **upper control of the repeated main-source interaction by a finite global quantity**.

---

## 12. Define the missing interaction ledger

At a stretching event in normalized variables, write schematically

\[
\mathcal A_j
:=
\int
\frac{|\Omega_j(Y+Z)|
\sin\theta_j(Y,Y+Z)}{|Z|^3}dZ.
\]

M5-362 gives a fixed lower bound on the productive contribution at some event in every stage.

M5-394 shows that on the natural branch this contribution contains an actual companion flux packet.

Thus the hard local object is not one carrier but a coupled pair:

\[
\boxed{
\mathcal C_j
=
(\text{main flux carrier},
\text{misaligned source flux carrier},
\text{their Biot--Savart interaction}).
}
\]

A successful closure would require a coercive/global estimate of the schematic form

\[
\boxed{
\sum_{j\in J_{local}}
\operatorname{Charge}(\mathcal C_j)
\le
C(E_0,\nu,\text{finite controlled data})
}
\]

while each local productive stage obeys

\[
\operatorname{Charge}(\mathcal C_j)\ge c_*>0.
\]

No such finite global interaction budget has yet been proved in the repository.

---

## 13. Why single-carrier budgets are insufficient

The audits now rule out three tempting but invalid shortcuts.

### A. Age dilution

Fails because the required natural source flux is constant `~nu`.

### B. Per-packet Leray energy/dissipation

Scales like `r_j` over one natural stage and is geometrically summable.

### C. Additive Lipschitz deformation

Uses a spatial supremum and may be reused by multiple carriers; its infinite accumulation is already compatible with BKM blow-up.

Therefore the sought non-summable charge must measure **interaction, multiplicity, or source reach** in a way that cannot be reused freely across generations.

---

## 14. Updated local frontier

After M5-394--396, the local natural-source branch can be expressed as

\[
\boxed{
G_{\rm dual\,flux}^{formed}
\Longrightarrow
R_{\rm persistent\ source\ funnel}
\lor
T_{\rm fixed\ source\ flux\ replacement/projective}
\lor
H_{\rm remote/nonlocal\ strain}.
}
\]

The first branch pays unbounded cumulative deformation but no contradiction.

The second creates repeated fixed-flux ancestry throughput but has no known finite absolute-flux budget.

The third is the existing nonlocal frontier.

Thus the former abstract label

\[
H_{\rm crit\,local\,occupancy}
\]

is now better interpreted as

\[
\boxed{
H_{\rm critical\ main-source\ interaction/genealogy}.
}
\]

---

## 15. Next target

The next efficient calculation should not attempt another source-age estimate.

The correct target is one of the following equivalent bridges:

1. a scale-time packing estimate for repeated dual-flux interaction cells;
2. a Carleson-type bound preventing the same Biot--Savart source action from being charged at infinitely many first-hitting scales;
3. a source-reach theorem showing that persistent local interaction must eventually become remote/non-tight;
4. a genuine finite critical integral controlling the repeated paired-carrier action.

Any proposed bridge must be audited against two anti-models:

- one old constant-flux source lineage reused indefinitely;
- one fresh natural source packet created at every stage with geometrically summable Leray cost.

---

## 16. DSD audit

### Corrected

- M5-385 age dilution is not applicable to natural scale-invariant flux;
- M5-357 scale-independent finite-memory energy count is not available for natural carriers;
- two carrier deformation lower bounds cannot be added merely because two carriers exist.

### Retained

- old reuse forces geometric funnel deformation;
- fixed replacement gives fixed non-parent flux by M5-395;
- every local productive stage has an order-one angular-source/stretching action.

### Firewall

Do not interpret BKM-compatible cumulative Lipschitz divergence as a contradiction.

Do not invent a finite absolute vorticity-flux budget where none has been proved.

Do not sum packet energy charges that decay like `r_j` and are therefore compatible with the Leray budget.

---

## 17. Audit verdict

### NEGATIVE RESULT / NECESSARY CORRECTION

\[
\boxed{
\text{natural companion source flux has no generation-age dilution.}
}
\]

### SHARPENED HARD CORE

\[
\boxed{
H_{\rm critical\ main-source\ interaction/genealogy}
\lor
H_{\rm remote/nonlocal\ strain}
\lor
T_{\rm fixed\ flux\ replacement/projective/export}.
}
\]

### STILL OPEN

- a non-summable interaction/packing charge for repeated dual-flux cells;
- persistent constant-flux source reuse;
- continual fresh fixed-flux source replacement;
- remote/nonlocal strain;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
