# DSD M5-473 — Log-improved Serrin audit of the ratchet charge

Date: 2026-09-01

Status: **EXTERNAL-CRITERION CROSS-AUDIT / M5-472 FORCES A LOGARITHMIC-IN-GENERATION DIVERGENCE OF CRITICAL STRAIN/DERIVATIVE ACTION, BUT KNOWN LOGARITHMIC IMPROVEMENTS OF PRODI--SERRIN DO NOT TURN THIS LOWER BOUND INTO A CONTRADICTION / THE RATCHET CORRIDOR CAN LIVE AT THE LOGARITHMIC BORDERLINE UNLESS AN UPPER CONTROL OR A MINIMAL CRITICAL ELEMENT IS ADDED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Ratchet lower rate from M5-472

Let

\[
\mathcal R(t)
:=
\int_0^t
\left(
\|S(s)\|_3^2
+
\|\nabla\omega(s)\|_{3/2}^2
\right)ds.
\]

On a positive-density ratchet tower,

\[
\mathcal R(t_j)
\ge c\nu j-O(1).
\]

Since

\[
W_j=q^jW_0,
\]

this is

\[
\boxed{
\mathcal R(t_j)
\gtrsim
c\nu\log\frac{W_j}{W_0}.
}
\]

---

## 2. Relation to classical critical regularity criteria

The velocity-gradient Prodi--Serrin scale is

\[
\nabla u\in L_t^qL_x^p,
\qquad
\frac2q+\frac3p=2,
\qquad p>\frac32.
\]

The point

\[
(p,q)=(3,2)
\]

is exactly the critical quantity appearing in the tilt branch.

The directional-diffusion quantity also controls the same scale because

\[
\|\omega\|_3
\lesssim
\|\nabla\omega\|_{3/2},
\qquad
\|S\|_3\lesssim\|\omega\|_3.
\]

Thus M5-472 is consistent with, and quantitatively refines along the selected first-hitting tower, the necessary divergence of a critical regularity norm at blow-up.

---

## 3. Logarithmically improved criteria do not close the lane

Known logarithmic improvements have the schematic form

\[
\int_0^{T_*}
\frac{\|\nabla u(t)\|_{L^{p,\infty}}^q}
{1+\log(e+\mathcal H(t))}
\,dt
<\infty
\quad\Longrightarrow\quad
\text{regularity},
\]

at critical gradient exponents.

M5-472 supplies a **lower bound** on the numerator integrated stage by stage.

A lower bound cannot prove the log-improved integral finite. In fact, if the auxiliary high norm `H(t)` grows polynomially in the first-hitting amplitude, then the logarithmic denominator on stage `j` is only `O(j)`, while the ratchet supplies an `O(1)` critical numerator charge. The resulting model contribution is harmonic:

\[
\sum_j\frac{c}{j},
\]

which diverges.

Thus the ratchet corridor is fully compatible with the necessary failure of the logarithmically improved criterion.

---

## 4. Comparison with quantitative critical-norm blow-up results

Quantitative regularity work of Tao and later Barker--Prange and Lorentz-space refinements gives explicit lower growth requirements for critical velocity norms near a hypothetical singularity.

Those results constrain how slowly a critical norm may diverge, but M5-472 concerns a different object: an accumulated critical **strain/directional-action integral** tied to first-hitting genealogy.

The logarithmic generation rate obtained here is not presently incompatible with those known lower blow-up rates.

Therefore no literature theorem currently converts

\[
\mathcal R(t_j)\gtrsim c j
\]

into a contradiction.

---

## 5. Consequence for proof strategy

Further refinement of the same stage-sum lower bound is unlikely to close the problem unless one also obtains an **upper** estimate from finite energy or another globally finite invariant.

M5-471 already shows that the ordinary energy budget is too weak because natural-scale physical costs carry the summable factor `r_j`.

The remaining productive route is therefore concentration/compactness:

\[
\boxed{
A_{ratchet}^{dens}
\to
\text{minimal ancient ratchet element}
}
\]

on the bounded-amplitude/frequency branch.

Any strong noncompactness preventing this extraction is returned to `H_amp/freq^strong`.

---

## 6. Updated frontier

\[
\boxed{
\text{singular tower}
\Longrightarrow
H_{amp/freq}^{strong}
\lor
E_{ratchet}^{ancient},
}
\]

provided the ancient-element extraction in the next note is carried out.

---

## 7. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
