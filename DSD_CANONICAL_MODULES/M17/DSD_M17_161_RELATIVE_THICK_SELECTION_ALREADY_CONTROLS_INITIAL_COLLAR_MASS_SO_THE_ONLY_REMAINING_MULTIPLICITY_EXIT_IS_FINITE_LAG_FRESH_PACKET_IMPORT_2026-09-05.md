# DSD M17-161 — Relative-thick selection already controls initial collar mass, so the only remaining multiplicity exit is finite-lag fresh-packet import

Date: 2026-09-05  
Canonical ID: **M17-161**

Status: **MULTIPLICITY AUDIT / M17-160 RETAINED A `NEARBY MASS/MULTIPLICITY` EXIT BECAUSE ITS LARGE-CUTOFF CACCIoppoli ESTIMATE NEEDS THE NORMALIZED MASS IN AN ENLARGED COLLAR TO STAY BOUNDED. AT THE OBSERVATION TIME THIS IS NOT AN EXTRA HYPOTHESIS ON THE ORIGINAL M17-155 RELATIVE-THICK PACKET: THAT CONSTRUCTION CHOOSES `a_R=|W(p_R)|` WITH `a_R^2 >= c_* E_R`, WHERE `E_R` IS THE WHOLE RETAINED REMOTE-SHELL VORTICITY MASS. HENCE EVERY SUBCOLLAR AUTOMATICALLY HAS MASS `<= C a_R^2`. THE ONLY WAY THE COLLAR COMPARISON CAN FAIL DURING A FIXED LAG IS BY NEW MASS ENTERING/FORMING NEAR THE PACKET AFTER THE OBSERVATION TIME. IF THAT NORMALIZED COLLAR MASS BLOWS UP, A SIMPLE MAXIMUM ARGUMENT PRODUCES A NEW POINT WITH AMPLITUDE MUCH LARGER THAN THE ORIGINAL NORMALIZATION, STILL AT THE SAME REMOTE SCALE. THUS `NEARBY MULTIPLICITY` IS NOT A STATIC HIGH-JET ESCAPE: IT IS A FINITE-LAG FRESH-PACKET / AMPLITUDE-ESCALATION EVENT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Original M17-155 relative-thick choice

Let

\[
E_R(0):=\int_{C_R}|W(y,0)|^2dy
\]

be the retained enlarged-shell vorticity mass.

M17-155 assumes a compact ribbon packet `T_R` carrying a fixed fraction of that mass and with uniformly bounded similarity volume. Hence one can choose `p_R in T_R` such that

\[
\boxed{
a_R^2:=|W(p_R,0)|^2
\ge c_*E_R(0),
}
\]

with `c_*>0` independent of the remote scale.

---

## 2. Initial collar mass is automatic

Let `A_L(p_R)` be any fixed translated collar contained in `C_R` for all sufficiently large `R`.
Then trivially

\[
\int_{A_L(p_R)}|W(y,0)|^2dy
\le E_R(0).
\]

Therefore

\[
\boxed{
\frac1{a_R^2}
\int_{A_L(p_R)}|W(y,0)|^2dy
\le c_*^{-1}.
}
\]

Thus the normalized collar-mass upper bound required by M17-160 is **already built into the initial relative-thick selection**.

It must not be listed as an independent time-zero assumption.

---

## 3. What can fail at later fixed lag

Follow the same material center `p_R(tau)` over a fixed similarity-time lag `|tau|<=T`.
For the dilation-comoving collar of M17-160 define

\[
M_R(\tau;L_0)
:=
\frac1{a_R^2}
\int_{A_{L_0}(\tau)}
|W(p_R(\tau)+z,\tau)|^2dz.
\]

At `tau=0`,

\[
M_R(0;L_0)\le c_*^{-1}.
\]

Hence the multiplicity exit is precisely

\[
\boxed{
\sup_{|\tau|\le T}
M_R(\tau;L_0)
\to\infty
}
\]

along a remote sequence.

This is a **finite-lag mass import/formation event**, not a pre-existing static collar defect.

---

## 4. Mass blow-up forces amplitude escalation

Fix `T,L_0`.
The dilation-comoving collar has uniformly bounded Euclidean volume

\[
|A_{L_0}(\tau)|\le V(T,L_0)<\infty.
\]

If for some `tau_R in[-T,T]`

\[
M_R(\tau_R;L_0)\to\infty,
\]

then there exists `q_R` in that collar with

\[
|W(q_R,\tau_R)|^2
\ge
\frac1{V(T,L_0)}
\int_{A_{L_0}(\tau_R)}|W|^2.
\]

Therefore

\[
\boxed{
\frac{|W(q_R,\tau_R)|}{a_R}
\to\infty.
}
\]

Since the collar radius is fixed in translated similarity variables and the material center is remote, `q_R` remains at the same remote shell scale.

Thus normalized collar-mass explosion always contains a **stronger fresh packet center**.

---

## 5. The stronger packet is still low amplitude under the quiet critical shell ceiling

Assume the same quiet shell bound at `tau_R`:

\[
R(\tau_R)
\int_{C_{R(\tau_R)}}|W|^2dy
\le J_*.
\]

The bounded-potential elliptic estimate gives on a fixed local core around `q_R`

\[
|W(q_R,\tau_R)|^2
\le
C(K_0)
\int_{B_1(q_R)}|W|^2dy
\le
\frac{C J_*}{R(\tau_R)}.
\]

Hence

\[
\boxed{
|W(q_R,\tau_R)|\to0
}
\]

although it is arbitrarily larger than the old normalization `a_R`.

So the event is not a return to an order-one-vorticity core. It is a **hierarchical low-amplitude packet escalation**.

---

## 6. Recenter at the new amplitude maximum

Set

\[
b_R:=|W(q_R,\tau_R)|.
\]

Choose `q_R` as a local maximum on a slightly enlarged fixed collar. Then, on a smaller fixed neighborhood,

\[
|W|\le b_R.
\]

Normalize anew:

\[
\widetilde V_R(z,s)
:=
\frac{W(\widetilde p_R(s)+z,\tau_R+s)}{b_R},
\]

where `tilde p_R` is the material trajectory through `q_R`.

Then

\[
|\widetilde V_R(0,0)|=1,
\]

and the new packet has immediate fixed-core amplitude-relative compactness.
With bounded `kappa`, quiet strain, and remote Type-I velocity, it enters the same M17-155 OU extraction mechanism on every fixed local cylinder.

Thus the multiplicity branch is recursively transformed into another **fresh OU packet candidate** with a stronger local normalization.

---

## 7. Updated branch interpretation

The M17-160 exit

\[
G_{nearby\ mass/multiplicity}
\]

must therefore be read as

\[
\boxed{
G_{fresh\ packet\ import/escalation}
}
\]

rather than as an arbitrary static geometry defect.

At the initial relative-thick observation time there is no independent collar-mass escape.
The only issue is whether fixed-lag dynamics can repeatedly import/create progressively stronger low-amplitude packets near the tracked carrier.

---

## 8. What is still not proved

The present module does **not** show that repeated recentering terminates.
A sequence

\[
a_R^{(0)}\ll a_R^{(1)}\ll a_R^{(2)}\ll\cdots\to0
\]

may in principle occur across successive finite-lag observations while all amplitudes remain below the remote critical ceiling.

Therefore the next gate is a **finite-lag amplitude-escalation packing law**:

> can quiet bounded-`kappa` dynamics create arbitrarily many successively stronger low-amplitude packets at the same remote scale without paying order-one packet-boundary action or exhausting the shell `L2` mass?

---

## 9. DSD audit

1. Whole-shell mass and collar mass are not identified; only the subset inequality is used at time zero.
2. The new center `q_R` need not lie on the original ribbon. The OU packet argument is a vorticity-packet argument and does not require preservation of the original director label after recentering.
3. Stronger relative amplitude does not mean physical amplitude is large; the critical shell ceiling still sends it to zero.
4. Repeated recentering is not yet a contradiction.
5. The next problem is packing/turnover, not another jet differentiation.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
