# DSD M17-296 — Super-Gaussian infinity feed returns to a logarithmic mesoscopic radius or heat-scale exponential amplitude degeneration

Date: 2026-09-06  
Canonical ID: **M17-296**

Status: **AMPLITUDE-RADIUS RETURN GATE / M17-295 SHOWS THAT A NONVANISHING FAR-BOUNDARY REMAINDER REQUIRES PACKET-NORMALIZED SPATIAL GROWTH AT LEAST `exp(cR^2)` ALONG LARGE TANGENT RADII. THE PARENT FIRST-HITTING/ANALYTIC CORRIDOR HAS A FIXED ABSOLUTE VORTICITY AMPLITUDE CEILING `|W_j|<=C0`; IF THE PACKET AMPLITUDE SCALE IS `a_j`, THEN THE NORMALIZED FIELD SATISFIES `|V_j|<=C0/a_j`. THE RADIUS AT WHICH `exp(cR^2)` REACHES THIS CEILING IS `R_j^log ~ sqrt(log(C0/a_j))`, WITH PHYSICAL RADIUS `L_j^log=r_j R_j^log`. IF `L_j^log->0` AND THE GROWING MESOSCOPIC COEFFICIENT/INTERFACE CORRIDOR REMAINS QUIET, THE SUPER-GAUSSIAN LOWER GROWTH CANNOT BE REALIZED BEFORE HITTING THE PARENT AMPLITUDE CEILING, GIVING CONTRADICTION. HENCE THE NO-PAYER SURVIVOR MUST SATISFY `r_j^2 log(C0/a_j) not->0`, I.E. AMPLITUDE AS SMALL AS `exp(-c/r_j^2)` ALONG A SUBSEQUENCE. THIS IS HEAT-SCALE EXPONENTIAL AMPLITUDE DEGENERATION, STRICTLY STRONGER THAN THE EARLIER ALGEBRAIC `r^7` OCCUPANCY DEFECT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Parent absolute-amplitude ceiling

On the parent first-hitting analytic corridor, import the fixed zeroth-order bound

\[
\boxed{
\|W_j\|_{L^\infty}\le C_0.
}
\]

If the precise M17 representation is not parent-scale equivalent on a candidate branch, retain that scale-map failure explicitly rather than using this bound.

Let the selected packet amplitude normalization be

\[
\boxed{
a_j:=m_j^{1/2}r_j^{-3/2}.}
\]

Then

\[
V_j(z,\tau)
=\frac{1}{a_j}
W_j(q_j+r_jz,\theta_j+r_j^2\tau)
\]

satisfies the pointwise ceiling

\[
\boxed{
|V_j|\le\frac{C_0}{a_j}.
}
\]

---

## 2. Super-Gaussian tangent requirement

M17-295 shows that a nonvanishing cutoff boundary remainder at a fixed backward horizon forces annular normalized growth of the form

\[
\boxed{
\mathcal N_R
\gtrsim
\operatorname{poly}(R)^{-1}e^{cR^2}
}
\]

along a sequence `R->infinity` after fixing the time-scale constant.

An `L2` annular norm lower bound of this size also forces a pointwise amplitude at least

\[
\boxed{
\sup_{A_R}|V|
\gtrsim
\operatorname{poly}(R)^{-1}e^{cR^2}
}
\]

because the annulus has only polynomial volume.

Polynomial factors are negligible compared with the exponential scale.

---

## 3. Logarithmic critical radius

Choose a fixed large constant `alpha>0` and define

\[
\boxed{
R_j^{log}
:=
\alpha\sqrt{\log\!\left(\frac{C_0}{a_j}\right)}
}
\]

when `a_j<C_0`.

Then

\[
\exp\!\left(c(R_j^{log})^2\right)
=\left(\frac{C_0}{a_j}\right)^{c\alpha^2}.
\]

Choose `alpha` so that

\[
c\alpha^2>1.
\]

Ignoring only fixed polynomial factors, the super-Gaussian lower requirement then exceeds the parent normalized ceiling

\[
C_0/a_j.
\]

Thus the super-Gaussian tangent cannot be realized out to `R_j^log` while the parent amplitude ceiling and the tangent approximation remain simultaneously valid.

---

## 4. Physical logarithmic radius

The tangent radius corresponds to physical similarity length

\[
\boxed{
L_j^{log}
:=
r_jR_j^{log}
=\alpha r_j
\sqrt{\log(C_0/a_j)}.
}
\]

Its physical parabolic time is

\[
(L_j^{log})^2.
\]

If

\[
\boxed{L_j^{log}\to0,}
\]

then the contradiction is sought entirely inside a shrinking mesoscopic neighborhood.

As in M17-289, split explicitly:

1. mesoscopic scaled coefficient/ambient action;
2. interface/domain exit;
3. failure of growing-radius compactness;
4. or quiet mesoscopic approximation.

On case 4, the parent amplitude ceiling contradicts the M17-295 super-Gaussian lower growth before the logarithmic radius is reached.

---

## 5. Heat-scale exponential amplitude survivor

Therefore the no-payer survivor must fail the shrinking-logarithmic-radius condition.

Along a subsequence there exists `c_L>0` such that

\[
\boxed{
r_j^2
\log\!\left(\frac{C_0}{a_j}\right)
\ge c_L.}
\]

Equivalently,

\[
\boxed{
a_j
\le
C_0\exp\!\left(-\frac{c_L}{r_j^2}\right).}
\]

This is **heat-scale exponential amplitude degeneration**.

It is much stronger than every algebraic statement

\[
a_j=O(r_j^N)
\]

for a fixed `N`.

---

## 6. Relation to packet mass

Since

\[
m_j=a_j^2r_j^3,
\]

the exponential survivor satisfies

\[
\boxed{
m_j
\le
C_0^2r_j^3
\exp\!\left(-\frac{2c_L}{r_j^2}\right).}
\]

Thus the packet mass is beyond all algebraic occupancy scales.

The earlier `m_j=O(E_j^{sh}r_j^7)` branch is therefore superseded on this super-Gaussian lane by a much sharper heat-scale exponential defect.

---

## 7. Interpretation

The exponent `1/r_j^2` is the natural diffusion frequency/lifetime scale.

A scale-`r_j` derivative packet that is smaller than

\[
e^{-c/r_j^2}
\]

can in principle encode the enormous backward amplification needed by a high-frequency linear heat mode without violating a fixed absolute parent amplitude ceiling.

Thus the new survivor has a precise meaning:

\[
\boxed{
\text{heat-scale frequency}
+
\text{exponentially tiny absolute amplitude}.
}
\]

The next target is to determine whether the repository's first-hitting analyticity / finite-order derivative bounds permit such beyond-all-orders amplitude-frequency decoupling, or whether it necessarily returns to a nodal/flatness genealogy.

---

## 8. DSD audit

- The parent amplitude ceiling is explicitly conditional on the parent-to-M17 scale map.
- The growing-radius tangent approximation is not assumed automatically; its failure remains a payer/escape.
- The logarithmic threshold follows from comparing `exp(cR^2)` with `1/a_j`, not from an arbitrary rate choice.
- Exponential amplitude degeneration is a survivor classification, not a contradiction.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
