# DSD Material-Mean Diffusion Erosion -> Quadratic Hyperpalinstrophy Charge

Date: 2026-08-25

Status: **MATERIAL-MEAN VORTICITY RETENTION IDENTITY DERIVED / COMPRESSION AND DIFFUSION LOSS SEPARATED / DIFFUSION-EROSION CHARGE IMPROVED FROM FIFTH-POWER q^{-5k} TO QUADRATIC q^{-k/2} / NO THIRD-DERIVATIVE PERSISTENCE NEEDED / COMPRESSION-TURNOVER BRANCH REMAINS / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The previous pointwise packet-retention gate controlled every material trajectory by

\[
\sup_{A_n(t)}|\Delta\omega|.
\]

This is stronger than what the packet-identity/replacement argument actually needs.

To distinguish

- survival of a nontrivial material ancestor population,
- diffusion-driven destruction of that population,
- and replacement by a new Eulerian population,

it is enough to retain a positive **material-average vorticity amplitude** on the transported ancestor packet.

This permits a direct `L1(packet) -> L2(space)` estimate for `Delta omega` and removes the fifth-power spatial-persistence tax used in the pointwise erosion calculation.

---

## 2. Material packet and its conserved volume

At first-hitting stage `n`, use the analytic core packet

\[
A_n^0=B_{a_0r_n}(x_n),
\qquad
r_n=\sqrt{\frac\nu{W_n}}.
\]

The imported analyticity corridor gives

\[
|\omega(x,t_n)|\ge b_0W_n
\qquad(x\in A_n^0).
\]

Transport by the incompressible Lagrangian flow:

\[
A_n(t)=\Phi_{t_n,t}(A_n^0).
\]

Since `div u=0`,

\[
|A_n(t)|=|A_n^0|=:V_n,
\]

with

\[
\boxed{
V_n=c_A r_n^3,
\qquad
c_A:=\frac{4\pi}{3}a_0^3.
}
\]

Define the material mean vorticity amplitude

\[
\boxed{
M_n(t):=
\frac1{V_n}
\int_{A_n(t)}|\omega(x,t)|dx.
}
\]

Initially,

\[
\boxed{M_n(t_n)\ge b_0W_n.}
\]

---

## 3. Exact material-mean differential inequality

Write

\[
\xi=\frac\omega{|\omega|}
\]

where `omega != 0`, and use the usual regularization at zero.

The vorticity equation gives

\[
D_t\omega=S\omega+\nu\Delta\omega.
\]

Hence

\[
D_t|\omega|
=\xi\cdot S\omega
+\nu\xi\cdot\Delta\omega.
\]

Define the pointwise compressive vorticity-direction strain

\[
\boxed{
\sigma_-(x,t)
:=
\max\{-\xi\cdot S\xi,0\}.
}
\]

Then

\[
D_t|\omega|
\ge
-\sigma_-|\omega|
-\nu|\Delta\omega|.
\]

Because the domain `A_n(t)` is material and volume preserving, Reynolds transport gives

\[
\frac{d}{dt}
\int_{A_n(t)}|\omega|dx
\ge
-\int_{A_n(t)}\sigma_-|\omega|dx
-\nu\int_{A_n(t)}|\Delta\omega|dx.
\]

Whenever the material `L1` vorticity is positive, define its vorticity-weighted compressive rate

\[
\boxed{
c_n(t):=
\frac{
\int_{A_n(t)}\sigma_-|\omega|dx
}{
\int_{A_n(t)}|\omega|dx
}.
}
\]

Also define the packet-mean diffusion amplitude

\[
\boxed{
d_n(t):=
\frac1{V_n}
\int_{A_n(t)}|\Delta\omega|dx.
}
\]

Then

\[
\boxed{
M_n'(t)
\ge
-c_n(t)M_n(t)-\nu d_n(t).
}
\]

Status: **PROVED.**

---

## 4. Integrating factor and fixed compression threshold

Define cumulative compressive exposure

\[
\boxed{
C_n(t):=
\int_{t_n}^{t}c_n(s)ds.
}
\]

The integrating-factor inequality gives

\[
M_n(t)
\ge
b_0W_ne^{-C_n(t)}
-\nu\int_{t_n}^{t}
\exp[-(C_n(t)-C_n(s))]d_n(s)ds.
\]

Fix once and for all a finite compression threshold

\[
L_c>0.
\]

If

\[
C_n(t)\le L_c
\]

and

\[
\boxed{
\overline{\mathcal D}_n(t)
:=
\frac\nu{W_n}
\int_{t_n}^{t}d_n(s)ds
\le
\frac{b_0}{2}e^{-L_c},
}
\]

then

\[
\boxed{
M_n(t)
\ge
\frac{b_0}{2}e^{-L_c}W_n.
}
\]

Thus failure of material-mean retention implies the finite split

\[
\boxed{
C_n(t)>L_c
\quad\lor\quad
\overline{\mathcal D}_n(t)>
\frac{b_0}{2}e^{-L_c}.
}
\]

The first alternative is a genuine vorticity-weighted **compressive turnover** event rather than an arbitrary absolute-strain upper bound.

The second alternative is material-mean diffusion erosion with an age-independent threshold.

Status: **PROVED.**

---

## 5. Packet-mean diffusion is controlled directly by global hyperpalinstrophy

By Cauchy-Schwarz in space,

\[
\int_{A_n(t)}|\Delta\omega|dx
\le
V_n^{1/2}\|\Delta\omega(t)\|_2.
\]

Hence

\[
\boxed{
\overline{\mathcal D}_n(t)
\le
\frac\nu{W_nV_n^{1/2}}
\int_{t_n}^{t}\|\Delta\omega(s)\|_2ds.
}
\]

Since

\[
V_n^{1/2}
=c_A^{1/2}
\left(\frac\nu{W_n}\right)^{3/4},
\]

we obtain

\[
\boxed{
\frac\nu{W_nV_n^{1/2}}
=c_A^{-1/2}
\nu^{1/4}W_n^{-1/4}.
}
\]

No pointwise spatial-persistence lemma and no third vorticity derivative are needed.

---

## 6. Stage-adaptive decomposition

Let the descendant witness lie in stage `j=n+k`.

For

\[
h=0,\ldots,k,
\qquad
m=n+h,
\]

let

\[
I_h=[t_n,t]\cap[t_m,t_{m+1}).
\]

Use the natural stage normalization

\[
\Omega_m=\frac\omega{W_m},
\qquad
r_m=\sqrt{\frac\nu{W_m}},
\qquad
d\tau_m=W_mdt,
\]

and define

\[
R_m(\tau_m):=
\|\Delta\Omega_m\|_2^2.
\]

Physical scaling gives

\[
\|\Delta\omega\|_2
=
\frac{W_m^2}{\nu}r_m^{3/2}
\|\Delta\Omega_m\|_2
=
\nu^{-1/4}W_m^{5/4}R_m^{1/2}.
\]

Since

\[
dt=\frac{d\tau_m}{W_m},
\]

one stage contributes

\[
\nu^{1/4}W_n^{-1/4}
\int_{I_h}\|\Delta\omega\|_2dt
=
\left(\frac{W_m}{W_n}\right)^{1/4}
\int_{I_h}R_m^{1/2}d\tau_m.
\]

Therefore

\[
\boxed{
\overline{\mathcal D}_n(t)
\le
c_A^{-1/2}
\sum_{h=0}^{k}
q^{h/4}b_h,
}
\]

where

\[
\boxed{
b_h:=
\int_{I_h}R_m^{1/2}d\tau_m.}
\]

Status: **PROVED EXACTLY up to the spatial Cauchy upper bound.**

---

## 7. Diffusion erosion forces a quadratic stage-energy charge

Each natural stage interval has normalized length at most `L_+`.

Thus

\[
b_h^2
\le
L_+
E_h,
\qquad
E_h:=\int_{I_h}R_m\,d\tau_m.
\]

Using Cauchy-Schwarz over the discrete stage index,

\[
\begin{aligned}
\sum_{h=0}^{k}q^{h/4}b_h
&\le
L_+^{1/2}
\sum_{h=0}^{k}q^{h/4}E_h^{1/2}\\
&\le
L_+^{1/2}
\left(\sum_{h=0}^{k}q^{h/2}\right)^{1/2}
\left(\sum_{h=0}^{k}E_h\right)^{1/2}.
\end{aligned}
\]

Define

\[
\boxed{
H_k^{(2)}
:=
\sum_{h=0}^{k}q^{h/2}
=
\frac{q^{(k+1)/2}-1}{q^{1/2}-1}.
}
\]

If material-mean diffusion erosion occurs,

\[
\overline{\mathcal D}_n>d_{mean},
\qquad
\boxed{
d_{mean}:=\frac{b_0}{2}e^{-L_c},}
\]

then the preceding upper estimate forces

\[
\boxed{
\sum_{h=0}^{k}E_h
\ge
\frac{c_A d_{mean}^2}
{L_+H_k^{(2)}}.
}
\]

This is quadratic in the erosion threshold rather than fifth-power.

Status: **PROVED.**

---

## 8. Transfer directly to standard Leray hyperpalinstrophy

On each stage the two-sided first-hitting/Leray clock corridor gives

\[
\widehat\Theta_m(t)
=W_m(T^*-t)
\ge
\theta_{st,-}:=\frac{\Theta_-}{q}>0.
\]

The exact scale transfer is

\[
R_L(s)ds
=
\widehat\Theta_m(t)^{3/2}
\nu^{-1/2}
R_m\,d\tau_m.
\]

Hence

\[
\int_{s(t_n)}^{s(t)}R_L(s)ds
\ge
\theta_{st,-}^{3/2}
\nu^{-1/2}
\sum_{h=0}^{k}E_h.
\]

Therefore every material-mean diffusion-erosion event satisfies

\[
\boxed{
\int R_Lds
\ge
H_{mean}(k)
:=
\theta_{st,-}^{3/2}
\nu^{-1/2}
\frac{c_A d_{mean}^2}
{L_+H_k^{(2)}}.
}
\]

For large `k`,

\[
H_k^{(2)}\asymp C_q q^{k/2},
\]

so

\[
\boxed{
H_{mean}(k)
\asymp
C_{mean}q^{-k/2}.
}
\]

There is no material-retention factor of the form

\[
e^{-5A_{st}(k+1)L_+}
\]

because compression has been separated into its own turnover channel at the fixed threshold `L_c`.

Status: **PROVED.**

---

## 9. Comparison with the previous pointwise erosion charge

The previous stage-adaptive pointwise route gave

\[
H_{adapt}(k)
\asymp
q^{-5k}
\exp[-5A_{st}(k+1)L_+].
\]

The material-mean route gives instead

\[
\boxed{
H_{mean}(k)
\asymp q^{-k/2}
}
\]

for fixed `L_c`.

Thus two major losses are removed:

1. the fifth-power derivative persistence cost;
2. the exponentially decreasing retention threshold inherited from the worst-case total absolute strain ceiling.

This is not a stronger pointwise theorem; it is a theorem for the weaker but sufficient statement that a positive material ancestor population survives in average vorticity amplitude.

---

## 10. Updated packet trichotomy

The old `E/R/T_multi` trichotomy can now be refined before requiring pointwise coherence.

For a current fixed-age shell packet and its stage-`n` material ancestor, one has:

### C. Compressive turnover

\[
\boxed{C_n(t)>L_c.}
\]

The old material population experiences a fixed amount of vorticity-weighted compressive strain.

### D. Material-mean diffusion erosion

\[
\boxed{
\overline{\mathcal D}_n(t)>d_{mean},
}
\]

which forces the quadratic hyperpalinstrophy charge

\[
\boxed{H_{mean}(k)\asymp q^{-k/2}.}
\]

### Q. Quiet material-mean retention

If neither C nor D occurs,

\[
\boxed{
M_n(t)
\ge
\frac{b_0}{2}e^{-L_c}W_n.
}
\]

On Q, apply the enstrophy-weighted contact split between the current Eulerian shell and `A_n(t)`:

- significant weighted contact -> `R` material return;
- low weighted contact -> current shell mass lies outside the retained material ancestor, giving packet replacement / turnover `T`.

Thus

\[
\boxed{
\text{fixed-age witness}
\Longrightarrow
C\lor D\lor R\lor T.
}
\]

Since C is itself an explicit material turnover mechanism, it may be grouped structurally with T when the turnover ledger is audited:

\[
\boxed{
\text{fixed-age witness}
\Longrightarrow
D\lor R\lor T_{turn}.
}
\]

Status: **PROVED AS A REFINED FINITE PARTITION, with T closure still open.**

---

## 11. Consequence for the quantified E/D mean-R floor

The weighted fixed-shell extraction previously supplied a selected-age recurrent-density floor with intrinsic factor

\[
R_k^{-3/2}
\sim q^{-3k/4}
\]

and a chosen summable weight `w_k`.

Combining that density factor with the new event charge

\[
q^{-k/2}
\]

gives the age dependence

\[
\boxed{
\frac{w_k}{S_{fix}(k)}
q^{-5k/4}
}
\]

up to fixed constants.

This replaces the previous pointwise-stage-adaptive factor

\[
\frac{w_k}{S_{fix}(k)}
q^{-23k/4}
\exp[-5A_{st}(k+1)L_+].
\]

The remaining large-age loss is now much milder and completely algebraic.

---

## 12. Why FATG is still not automatically removed

Even

\[
q^{-5k/4}\to0.
\]

Therefore a shell ledger containing only

\[
\sum_kI_k>0
\]

still cannot force an age-uniform positive diffusion-erosion cost if all active charge is allowed to drift to arbitrarily large age.

However the required tightness is now far weaker than before.

The remaining obstruction is no longer an exponential material-deformation loss or a high-derivative analyticity loss.

It is only the scale conversion inherent in comparing an old material packet with later natural-stage `L2` hyperpalinstrophy.

---

## 13. DSD audit

The following channels remain distinct:

- material packet volume;
- material mean vorticity amplitude;
- vorticity-weighted compressive strain;
- packet-mean diffusion;
- global `L2` second-vorticity-derivative energy;
- weighted material contact;
- replacement/turnover.

The calculation deliberately weakens pointwise retention to average retention because only the latter is needed to certify that a nontrivial old material population still exists.

No third-vorticity-derivative channel is formed in this argument.

---

## 14. Updated frontier

The diffusion branch is no longer the dominant quantitative obstruction.

It now has an explicit fixed-age event cost

\[
\boxed{H_{mean}(k)\asymp q^{-k/2}.}
\]

The main unresolved mechanisms are therefore:

1. vorticity-weighted compressive turnover `C`, now naturally part of the T/turnover branch;
2. recurrent material critical halo `R`, already routed to historical replenishment `H_remote/T` or escaping-tail topology;
3. low-contact packet replacement `T`;
4. the residual large-age tightness issue in converting the D branch to a uniform all-age contradiction.

The next efficient calculation is to test whether the **compressive turnover and low-contact replacement branches admit one common material-L1 turnover budget**, which would collapse C and T into a single quantitative branch.

---

## 15. Audit verdict

### PROVED

- material packet mean-vorticity differential inequality;
- exact separation of compressive strain from diffusion erosion;
- fixed age-independent diffusion threshold after fixing a compression threshold;
- direct spatial `L1 -> L2` diffusion estimate;
- stage-adaptive weight `q^{h/4}`;
- quadratic hyperpalinstrophy event charge;
- asymptotic age loss improved to `q^{-k/2}`;
- refined finite partition `D or R or T_turn`.

### NOT DERIVED

- a global budget closing repeated compressive turnover;
- a global budget closing repeated low-contact packet replacement;
- age-uniform D-branch contradiction without some residual tightness information;
- closure of the escaping passive critical-tail topology;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
