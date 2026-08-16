# Deep-checkpoint affine tradeoff after correct terminal/deep normalization

Date: 2026-08-16

Status: **CORRECTED SCALING AUDIT. THE EARLIER SUPERLARGE `W^(5/2)` PRODUCT CLAIM WAS WRONG BECAUSE THE PRECURSOR MIXED NORM, ENSTROPHY, PALINSTROPHY, TIME, AND STRAIN ENERGY ALSO RESCALE BETWEEN DEEP AND TERMINAL NORMALIZATIONS. THE CORRECT TERMINAL-NORMALIZED AFFINE COST DECAYS LIKE `1/q`. GLOBAL REGULARITY NOT PROVED.**

## 1. Why a correction is necessary

At the deep first-hitting level let

\[
W_-=W/q,
\qquad
q=q_\beta=W/R^\beta.
\]

Terminal normalization uses length

\[
r=W^{-1/2},
\]

while deep normalization uses

\[
r_-=W_-^{-1/2}=\sqrt q\,r.
\]

If `Omega_term(y)` is the terminal-normalized precursor field and `Omega_deep(z)` the same physical field in the deep normalization, then

\[
\boxed{
\Omega_{\rm deep}(z)
=q\,\Omega_{\rm term}(\sqrt q\,z).
}
\]

Thus one cannot apply the deep-normalized affine theorem to terminal-normalized norms without transforming both amplitude and coordinates.

---

## 2. Exact scaling of the relevant precursor norms

For the transverse mixed norm

\[
M_\Pi
=\|\Omega\|_{L^\infty_{e_1}L^2_{e_2,e_3}},
\]

two transverse coordinates contribute area scaling `q^-1`, while vorticity amplitude contributes `q`. Therefore

\[
\boxed{
M_{\Pi,\rm deep}^2
=q\,M_{\Pi,\rm term}^2.
}
\]

For enstrophy,

\[
\boxed{
E_{\rm deep}
=q^{1/2}E_{\rm term}.
}
\]

For palinstrophy,

\[
\boxed{
P_{\rm deep}
=q^{3/2}P_{\rm term}.
}
\]

Hence

\[
\boxed{
E_{\rm deep}P_{\rm deep}
=q^2E_{\rm term}P_{\rm term}.
}
\]

---

## 3. Exact scaling of affine strain energy

Deep normalized time and terminal normalized time satisfy

\[
ds_{\rm term}=q\,ds_{\rm deep}.
\]

The normalized velocity gradient satisfies

\[
S_{\rm deep}=q\,S_{\rm term}.
\]

Therefore the affine strain-square action obeys

\[
\boxed{
J_{\rm deep}
=\int|S_{\rm deep}|^2ds_{\rm deep}
=q\,J_{\rm term}.
}
\]

---

## 4. Correct transformation of the affine heat tradeoff

The exact affine theorem in the deep normalization states, for a genuine `q` amplification from order-one deep-normalized vorticity to order-`q` final vorticity,

\[
\boxed{
J_{\rm deep}M_{\Pi,\rm deep}^2
\gtrsim
\nu q.
}
\]

Substitute

\[
J_{\rm deep}=qJ_{\rm term},
\qquad
M_{\Pi,\rm deep}^2=qM_{\Pi,\rm term}^2.
\]

Then

\[
q^2J_{\rm term}M_{\Pi,\rm term}^2
\gtrsim
\nu q,
\]

so the correct terminal-normalized form is

\[
\boxed{
J_{\rm term}M_{\Pi,\rm term}^2
\gtrsim
\frac\nu q.
}
\]

The cost becomes smaller at deeper amplification ratios. It does **not** grow like `nu q` in terminal normalization.

---

## 5. Correct trace-product form

The deep-normalized trace consequence is

\[
J_{\rm deep}^2
E_{\rm deep}P_{\rm deep}
\gtrsim
\nu^2q^2.
\]

Using

\[
J_{\rm deep}^2=q^2J_{\rm term}^2,
\qquad
E_{\rm deep}P_{\rm deep}=q^2E_{\rm term}P_{\rm term},
\]

we get

\[
q^4J_{\rm term}^2E_{\rm term}P_{\rm term}
\gtrsim
\nu^2q^2.
\]

Therefore

\[
\boxed{
J_{\rm term}^2E_{\rm term}P_{\rm term}
\gtrsim
\frac{\nu^2}{q^2}.
}
\]

This is scale critical and weakens as `q->infinity`.

---

## 6. Insert the deep-checkpoint enstrophy ceiling

The terminal-normalized deep enstrophy satisfies

\[
E_-
\lesssim
\frac{R^\beta}{W^{1/2}}.
\]

The corrected trace product gives only

\[
J_{\rm term}^2P_{e,-}
\gtrsim
\frac{\nu^2}{q^2E_-}.
\]

With

\[
q=W/R^\beta,
\]

this becomes

\[
\boxed{
J_{\rm term}^2P_{e,-}
\gtrsim
\nu^2
\frac{R^\beta}{W^{3/2}}.
}
\]

This tends to zero on the late coherent branch and therefore provides no contradiction.

The previous claim

\[
J^2P\gtrsim \nu^2W^{5/2}R^{-3\beta}
\]

was the reciprocal scaling error and is withdrawn.

---

## 7. What survives from the affine analysis

The rotation-independent affine theorem remains correct in its own normalization. What changes is its interpretation in the deep-to-terminal cascade.

The correct conclusion is:

\[
\boxed{
\text{pure affine deformation--diffusion is itself scale critical under terminal normalization.}
}
\]

Thus a proof cannot be completed merely by taking `q` arbitrarily large and invoking the affine precursor product.

The actual useful affine information is instead

1. deformation forces an anisotropic accumulated diffusion area;
2. axis rotation cannot remove that area;
3. in the fully nonlinear stochastic flow, the same matrix area bound holds pathwise through the Malliavin Gramian;
4. converting that random Gramian into a smoothing estimate produces Hessian/deformation-weighted derivative errors.

---

## 8. Updated proof target

The affine route therefore does **not** produce a superlarge ordinary palinstrophy barrier by itself.

The active target remains

\[
\boxed{
\text{pathwise large deformation}
\Longrightarrow
\text{large Malliavin diffusion area}
\Longrightarrow
\text{precursor smoothing}
}
\]

with every failure of the final implication charged to the Hessian / deformation-weighted derivative channel.

Overall status: **SCALING ERROR CORRECTED / AFFINE PRODUCT RECLASSIFIED AS CRITICAL / PATHWISE MALLIAVIN DEFORMATION--DIFFUSION THEOREM REMAINS VALID AND IS THE PREFERRED ROUTE.**
