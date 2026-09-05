# DSD M17-214 — Director-area concentration cannot carry fixed-fraction relative-thick compact packet mass

Date: 2026-09-06  
Canonical ID: **M17-214**

Status: **DIRECTOR-AREA CONCENTRATION GATE / DIRECTOR-FLUX COORDINATES GIVE `dV=dPhi_J ds/|J_xi|`. IF A PACKET REGION WITH `|J_xi|>=J0` CARRIES A FIXED FRACTION OF THE REMOTE SHELL ENSTROPHY WHILE ITS TOTAL DIRECTOR FLUX, FIBER LENGTH, AND AMPLITUDE-TO-SHELL-MASS RATIO REMAIN UNIFORMLY BOUNDED, THEN ITS ENSTROPHY IS AT MOST `C E_R/J0`. COMPARISON WITH THE FIXED-FRACTION LOWER BOUND FORCES A UNIFORM UPPER BOUND ON `J0`. THUS LARGE DIRECTOR-AREA CURRENT CANNOT BE THE SPECTRAL EXIT ON THE RELATIVE-THICK COMPACT-PACKET LANE. IT MUST BE ACCOMPANIED BY AMPLITUDE CONCENTRATION/RELATIVE THINNESS, DIRECTOR-FLUX DECOMPACTIFICATION, FIBER-LENGTH DECOMPACTIFICATION, OR LOSS OF THE FIXED-FRACTION CARRIER PROPERTY. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Director-flux coordinates

On a regular Rank-2 director-area tube, use the frozen flux label `dPhi_J` and arclength `ds` along the current direction.

The exact tube-volume disintegration is

\[
\boxed{
dV=\frac{d\Phi_J\,ds}{|J_\xi|}.
}
\]

Let `T_R` be a packet region composed of such tube segments.

Its vorticity enstrophy is

\[
\boxed{
E(T_R)
=\int_{\Lambda_R}d\Phi_J
\int_{\Gamma_\lambda}
\frac{\rho^2}{|J_\xi|}ds.
}
\]

---

## 2. High director-area subset

Suppose on the packet region

\[
\boxed{|J_\xi|\ge J_0>0.}
\]

Then

\[
E(T_R)
\le
\frac1{J_0}
\int_{\Lambda_R}d\Phi_J
\int_{\Gamma_\lambda}\rho^2ds.
\]

Assume compact fiber length

\[
\boxed{L(\Gamma_\lambda)\le L_*}
\]

and total director flux

\[
\boxed{\Phi_J(T_R)\le\Phi^*.}
\]

Therefore

\[
\boxed{
E(T_R)
\le
\frac{\Phi^*L_*}{J_0}
\sup_{T_R}\rho^2.
}
\]

---

## 3. Relative-thick amplitude comparability

Assume the packet is relative-thick in the stronger mass-carrying sense needed for the spectral branch:

\[
\boxed{
\sup_{T_R}\rho^2
\le C_a E_R,
}
\]

where

\[
E_R=\int_{C_R}\rho^2dy
\]

is the parent shell enstrophy.

Also suppose the high-area packet carries a fixed shell fraction

\[
\boxed{E(T_R)\ge\vartheta E_R,\qquad \vartheta>0.}
\]

Combining with Section 2,

\[
\vartheta E_R
\le
\frac{C_a\Phi^*L_*}{J_0}E_R.
\]

For `E_R>0`, cancel the shell mass:

\[
\boxed{
J_0
\le
\frac{C_a\Phi^*L_*}{\vartheta}.
}
\]

Thus `J0` cannot diverge on such a fixed-fraction packet sequence.

---

## 4. Fixed-fraction high-area subsets

The same argument applies if only a subset

\[
T_R^{high}:=T_R\cap\{|J_\xi|\ge J_R\}
\]

carries a fixed fraction

\[
E(T_R^{high})\ge\vartheta E_R.
\]

Provided the subset inherits the same total flux/length/amplitude ceilings,

\[
\boxed{J_R\le C(\vartheta,C_a,\Phi^*,L_*).}
\]

Therefore an enstrophy-dominant director-area concentration sequence is impossible on the compact relative-thick packet class.

---

## 5. Exact surviving exits

For `|J_xi| -> infinity` to remain relevant to the hard shell, at least one assumption above must fail:

\[
\boxed{
G_{J_\xi,\infty}
\Longrightarrow
G_{amplitude\ concentration/thin}
\lor
G_{director\ flux\ decompactification}
\lor
G_{fiber\ length\ decompactification}
\lor
G_{carrier\ fraction\ loss}.
}
\]

The last branch means the high-area set becomes enstrophy-negligible and cannot by itself carry the hard shell stack.

---

## 6. Relation to M17-213

M17-213 gave

\[
|\nabla\xi|^2=2|J_\xi|\mathcal A_\xi.
\]

M17-214 removes the `|J_xi| -> infinity` part on the relative-thick compact mass-carrying lane.
Hence the remaining large-director-metric spectral mechanism there is primarily

\[
\boxed{\mathcal A_\xi\to\infty,}
\]

i.e. relative rank degeneration, unless one of the explicit decompactification/thin exits occurs.

---

## 7. DSD audit

- The amplitude upper comparability `sup rho^2 <= C_a E_R` is explicit. Without it, high `J_xi` may coexist with a highly concentrated amplitude spike; that is retained as a thin/concentration exit.
- The argument bounds an enstrophy-dominant high-area region, not arbitrary pointwise `J_xi` spikes.
- Total director flux and fiber length are packet compactness assumptions already used in the earlier complete-ribbon class; their failure is kept explicit.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
