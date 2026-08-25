# DSD Weighted Fixed-Shell Quantification and DEMHCT Age Obstruction

Date: 2026-08-25

Status: **QUANTITATIVE WEIGHTED FIXED-SHELL EXTRACTION PROVED / EXPLICIT SHELL-DENSITY AND LOCAL-MASS FLOORS DERIVED / FIXED-LAG LERAY LENGTH MADE EXPLICIT / DEMHCT LARGE-AGE DETERIORATION IDENTIFIED / NO UNIFORM E-BRANCH CLOSURE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose and correction

`DSD_REMOTE_WITNESS_FIXED_SHELL_EXTRACTION_2026-08-25.md` proved that some finite shell index `k_0` has positive recurrent mean and hence supports a positive-density threshold set.

That qualitative Tonelli argument does **not** by itself give a uniform numerical lower bound for the selected shell integral, density, or threshold in terms of the total remote-witness charge alone.

Indeed a fixed positive total sum can be distributed over arbitrarily many shell indices with arbitrarily small individual summands.

Therefore the statement in the first DEMHCT note that the branch density can simply be replaced by a fixed inherited numerical lower bound requires an additional quantitative extraction step.

This note supplies such a step with an arbitrary summable weight sequence and then audits its dependence on shell age.

---

## 2. Imported remote-shell ledger

On the recurrent remote-witness set `A_rw`, let

\[
\mu(A_{rw})=d_{rw}>0.
\]

Use

\[
\lambda=\sqrt q>1,
\qquad
R_k=R_0\lambda^k,
\]

and shell enstrophy

\[
m_k(s)=\int_{A_k}|\Omega(y,s)|^2dy.
\]

Define

\[
a_k(s):=(R_km_k(s))^{3/2}.
\]

The previous shell inequality gives, for every `s in A_rw`,

\[
\boxed{
\sum_{k=0}^{\infty}a_k(s)\ge A_*>0.
}
\]

Hence

\[
\boxed{
\sum_{k=0}^{\infty}I_k\ge A_*d_{rw},
\qquad
I_k:=\int_{A_{rw}}a_k(s)d\mu(s).
}
\]

On the bounded normalized-enstrophy branch,

\[
m_k(s)\le Z_+,
\]

so pointwise

\[
\boxed{
a_k(s)\le M_k:=(R_kZ_+)^{3/2}.}
\]

---

## 3. Weighted pigeonhole extraction

Let

\[
w_k>0,
\qquad
\sum_{k=0}^{\infty}w_k=1.
\]

If every shell satisfied

\[
I_k<A_*d_{rw}w_k,
\]

then summing would give

\[
\sum_k I_k<A_*d_{rw},
\]

contradicting the imported lower bound.

Therefore there exists at least one finite index `k_*` such that

\[
\boxed{
I_{k_*}\ge A_*d_{rw}w_{k_*}.
}
\]

This is the quantitative replacement for the purely qualitative Tonelli shell selection.

Status: **PROVED.**

---

## 4. Explicit positive-density threshold at the selected shell

For the selected shell define

\[
\delta_{k_*}:=\frac{I_{k_*}}{2d_{rw}}
\]

and

\[
B_{k_*}:=\{s\in A_{rw}:a_{k_*}(s)\ge\delta_{k_*}\}.
\]

Because `a_{k_*}<=M_{k_*}`,

\[
\begin{aligned}
I_{k_*}
&=\int_{A_{rw}\setminus B_{k_*}}a_{k_*}d\mu
+\int_{B_{k_*}}a_{k_*}d\mu\\
&\le
\delta_{k_*}d_{rw}
+M_{k_*}\mu(B_{k_*})\\
&=\frac12I_{k_*}+M_{k_*}\mu(B_{k_*}).
\end{aligned}
\]

Hence

\[
\boxed{
\mu(B_{k_*})
\ge
\frac{I_{k_*}}{2M_{k_*}}
\ge
\frac{A_*d_{rw}w_{k_*}}
{2(R_{k_*}Z_+)^{3/2}}.
}
\]

Also on `B_{k_*}`,

\[
(R_{k_*}m_{k_*})^{3/2}
\ge
\delta_{k_*}
\ge
\frac{A_*w_{k_*}}2,
\]

so

\[
\boxed{
R_{k_*}m_{k_*}
\ge
J_{k_*}:=
\left(\frac{A_*w_{k_*}}2\right)^{2/3}.
}
\]

Thus both the threshold and its recurrent density are now explicit once the selected age `k_*` and weight sequence are specified.

Status: **PROVED.**

---

## 5. Explicit local-ball concentration

Use the same scale-invariant finite annular covering as in the fixed-shell extraction note.

Let `sigma in (0,1)` be fixed and let `N_*=N_*(lambda,sigma)` be a shell-independent covering number.

Then on `B_{k_*}` at least one ball of radius

\[
\rho_{k_*}=\sigma R_{k_*}
\]

obeys

\[
\boxed{
\rho_{k_*}
\int_{B_{\rho_{k_*}}}|\Omega|^2dy
\ge
\kappa_{k_*}:=
\frac{\sigma}{N_*}
\left(\frac{A_*w_{k_*}}2\right)^{2/3}.
}
\]

The covering number does not deteriorate with `k_*`; all age dependence is explicit through `w_{k_*}` and `R_{k_*}`.

Status: **PROVED.**

---

## 6. Geometric weights as one concrete choice

For

\[
0<\beta<1,
\qquad
w_k=(1-\beta)\beta^k,
\]

we obtain

\[
\boxed{
J_k
=\left(\frac{A_*(1-\beta)}2\right)^{2/3}
\beta^{2k/3}.
}
\]

Since

\[
R_k=R_0q^{k/2},
\]

the shell-density floor becomes

\[
\boxed{
\mu(B_k)
\ge
C_{dens}(1-\beta)
\left(\beta q^{-3/4}\right)^k,
}
\]

where

\[
\boxed{
C_{dens}:=
\frac{A_*d_{rw}}
{2(R_0Z_+)^{3/2}}.
}
\]

This is explicit but decays exponentially with shell age.

A slower summable sequence, such as polynomial weights, can remove the artificial geometric decay from `w_k`, but it cannot remove the intrinsic factor

\[
q^{-3k/4}
\]

coming from the pointwise shell ceiling `M_k=(R_kZ_+)^{3/2}`.

---

## 7. Explicit fixed-lag Leray interval length

Let the selected shell correspond to the finite generation lag `k` and let an event time lie in stage `j`, with ancestor stage

\[
n=j-k.
\]

The first-hitting/Leray clock identity gives

\[
s_m=m\log q+\log W_0-\log\Theta_m
\]

with

\[
\Theta_-\le\Theta_m\le\Theta_+.
\]

Since the event time is no later than `t_{j+1}`,

\[
s(t)-s_n\le s_{j+1}-s_n.
\]

Therefore

\[
\boxed{
S_{fix}(k)
:=(k+1)\log q
+\log\frac{\Theta_+}{\Theta_-}
}
\]

is a valid explicit Leray-length ceiling for the backward fixed-lag event interval.

Using

\[
\Theta_-=
\frac{L_-}{q-1},
\qquad
\Theta_+=
\frac{qL_+}{q-1},
\]

this becomes

\[
\boxed{
S_{fix}(k)
=(k+1)\log q
+\log\frac{qL_+}{L_-}.
}
\]

Status: **PROVED on the two-sided first-hitting/Leray corridor.**

---

## 8. Make the E-branch erosion constants age-explicit

The fixed-lag deformation ceiling is

\[
\boxed{
L_{fix}(k)=A_{st}(k+1)L_+.
}
\]

Hence the erosion threshold inherited from material amplitude retention is

\[
\boxed{
d_0(k)=\frac{b_0}{2}
\exp[-A_{st}(k+1)L_+].
}
\]

The ancestor normalized-time ceiling is

\[
\boxed{
T_{fix}(k)
=L_+\sum_{h=0}^{k}q^{-h}
=L_+\frac{1-q^{-(k+1)}}{1-q^{-1}}.
}
\]

The fixed-parent third-derivative ceiling is

\[
\boxed{
K_{3,fix}(k)=C_{3,an}q^{5k/2}.
}
\]

For a witness in stage `j`, the remaining-time factor satisfies

\[
\boxed{
\Theta_{fix,-}(k)
=q^{-(k+1)}\Theta_-.
}
\]

Therefore one diffusion-erosion event at age `k` forces the Leray hyperpalinstrophy charge

\[
\boxed{
H_{L,eros}(k)
=
\Theta_{fix,-}(k)^{3/2}\nu^{-1/2}
\frac{\pi d_0(k)^5}
{24K_{3,fix}(k)^3T_{fix}(k)^4}.
}
\]

Substituting the age dependence gives

\[
\boxed{
H_{L,eros}(k)
=
C_{eros}
\frac{
q^{-9k-3/2}
\exp[-5A_{st}(k+1)L_+]
}
{T_{fix}(k)^4},
}
\]

where

\[
\boxed{
C_{eros}:=
\nu^{-1/2}
\frac{\pi\Theta_-^{3/2}}{24C_{3,an}^3}
\left(\frac{b_0}{2}\right)^5.
}
\]

The exponent `q^{-9k}` is exact from

\[
q^{-3k/2}
\times
q^{-15k/2}
=q^{-9k},
\]

coming respectively from the Leray scale transfer and the cube of the third-derivative persistence constant.

Status: **PROVED algebraically from the existing gates.**

---

## 9. Quantified DEMHCT floor for the selected shell

Suppose the finite partition on `B_k` selects the E branch as a pigeonhole survivor among

\[
E\lor R\lor T_{multi}.
\]

Then the selected branch can be taken to have density at least

\[
\boxed{
d_E(k)\ge\frac13\mu(B_k).}
\]

The disjoint-event packing argument then yields

\[
\boxed{
\overline R_L
\ge
\frac{d_E(k)}{2S_{fix}(k)}
H_{L,eros}(k)
\ge
\frac{\mu(B_k)}{6S_{fix}(k)}
H_{L,eros}(k).
}
\]

Using the weighted shell-density floor,

\[
\boxed{
\overline R_L
\ge
\frac{A_*d_{rw}w_k}
{12(R_kZ_+)^{3/2}S_{fix}(k)}
H_{L,eros}(k).
}
\]

This is now a fully explicit age-dependent lower floor, to be compared with

\[
\boxed{
\overline R_L
\le
R_{cap}
=
\frac{C_*^8}{16}
\frac{Z_+^5}{\nu^8}.
}
\]

Call the resulting age-dependent comparison **qDEMHCT(k)**.

---

## 10. Large-age obstruction

Since

\[
R_k^{3/2}=R_0^{3/2}q^{3k/4},
\]

the explicit qDEMHCT lower floor contains the intrinsic age factor

\[
\boxed{
\frac{w_k}{S_{fix}(k)}
q^{-39k/4}
\exp[-5A_{st}(k+1)L_+]
}
\]

up to fixed positive constants and the bounded factor `T_fix(k)^{-4}`.

Indeed

\[
q^{-3k/4}
\times q^{-9k}
=q^{-39k/4}.
\]

For every summable positive weight sequence `w_k`, this lower floor tends to zero as `k -> infinity`.

Therefore the current weighted extraction plus DEMHCT does **not** give a shell-age-uniform contradiction with the finite mean hyperpalinstrophy cap.

This is not a failure of positivity; it is a quantitative age-loss obstruction.

Status: **PROVED.**

---

## 11. Consequence for the proof tree

The E branch is now sharper than before:

\[
\boxed{
\text{positive-density remote witness}
\Longrightarrow
\exists k<\infty\text{ with explicit weighted shell density and mass floors}.
}
\]

For that selected age,

\[
\boxed{
E_k
\Longrightarrow
\overline R_L\ge R_{eros,floor}(k)>0.
}
\]

However the existing machinery does not prevent the selected finite age from being arbitrarily large across admissible recurrent survivors.

Hence a universal E-branch closure now requires at least one genuinely new ingredient:

1. an a priori upper bound on the recurrent shell age `k`;
2. a genealogy/transport estimate whose cost does not deteriorate exponentially in `k`;
3. a direct age-weighted spacetime budget capable of summing all shell ages before fixed-shell selection; or
4. an independent closure of the remote/contact/turnover alternatives that bypasses material age.

The first three are the natural continuation of the current line.

---

## 12. Audit correction to the previous DEMHCT note

The previous DEMHCT statement remains correct as a **fixed-age sufficient condition**.

What must be corrected is only the implicit suggestion that the currently proved Tonelli fixed-shell extraction already supplies a shell-age-uniform numerical density lower bound.

It does not.

The weighted extraction above supplies an explicit age-dependent lower bound and shows exactly why that is still insufficient for a uniform contradiction.

---

## 13. DSD audit

The following channels are kept distinct:

- remote-witness total shell charge `A_*`;
- shell index / finite age `k`;
- shell critical mass `R_km_k`;
- threshold-set density `mu(B_k)`;
- material deformation threshold `L_fix(k)`;
- diffusion erosion threshold `d_0(k)`;
- hyperpalinstrophy event charge `H_L,eros(k)`;
- recurrent mean hyperpalinstrophy cap `R_cap`.

The calculation explicitly records the information loss caused by passing from a total countable shell ledger to one selected finite shell.

No channel is identified merely because both are positive.

---

## 14. Updated frontier

The immediate frontier is no longer `compute DEMHCT constants` in the abstract.

It is

\[
\boxed{
\text{remove or compensate the large-age factor}
\quad
q^{-39k/4}e^{-5A_{st}(k+1)L_+}.
}
\]

The most promising next calculation is to avoid fixed-shell selection and charge the full age distribution directly against a single spacetime budget, or else to prove that recurrent remote witnesses force a bounded-age subfamily.

---

## 15. Audit verdict

### PROVED

- qualitative Tonelli extraction alone has no shell-uniform numerical lower bound;
- weighted fixed-shell selection with explicit `I_k` lower bound;
- explicit density floor for the selected threshold set;
- explicit critical shell-mass and local-ball floors;
- explicit fixed-lag Leray duration `S_fix(k)`;
- exact age dependence of the existing diffusion-erosion hyperpalinstrophy charge;
- qDEMHCT(k) as an explicit fixed-age comparison;
- large-age deterioration of the resulting mean-R floor.

### NOT DERIVED

- a uniform upper bound on selected shell age;
- an age-uniform positive E-branch mean-R floor;
- a direct all-age erosion budget closing the weighted sum;
- closure of the R/contact branch;
- closure of packet replacement / multicore turnover;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
