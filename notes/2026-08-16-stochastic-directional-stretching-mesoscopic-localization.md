# Stochastic directional stretching localizes on the final crossing-parabolic block

Date: 2026-08-16

Status: **CORRECTED BLOCK-LOCAL STATEMENT / CORE SELF-STRETCH AND MACROSCOPIC FAR FIELD ARE O(1) ON THE FINAL `O(R^2)` CROSSING BLOCK / NO CLAIM THAT THE FULL DEEP-CHECKPOINT `log q` ACTION OCCURS IN THIS BLOCK.**

## 1. Coherent crossing geometry

At the first Gaussian Reynolds-one crossing,

\[
B R^4=1,
\qquad
|\bar\Omega|\ge c_0>0,
\qquad
V_\omega\lesssim R^{-4},
\qquad
R\to\infty.
\]

Let

\[
e=\bar\Omega/|\bar\Omega|.
\]

For a Gaussian of radius `R`, its density on a fixed fractional core `B_{cR}` is bounded below by `c R^{-3}`. Hence

\[
\int_{B_{cR}}|\Omega-\bar\Omega|^2dy
\lesssim
R^3V_\omega
\lesssim
R^{-1}.
\]

In particular

\[
\boxed{
\|P_{e^\perp}\Omega\|_{L^2(B_{cR})}
\lesssim R^{-1/2}.
}
\]

---

## 2. Buffered constant-axis strain decomposition

The whole-space exact identity for a fixed axis is

\[
2\|Se\|_2
=
\|e\times\Omega\|_2.
\]

Its local use requires a cutoff/divergence correction and therefore produces explicit annular commutator terms. We retain those rather than setting them to zero.

Write schematically on the coherent core

\[
Se
=(Se)_{\rm core}
+(Se)_{\rm ann}
+(Se)_{\rm far},
\]

where the existing buffered local constant-axis route gives

\[
\boxed{
\|(Se)_{\rm core}\|_{L^2(B_{cR})}
\lesssim R^{-1/2}
}
\]

provided the cutoff/divergence-correction leakage is assigned to `(Se)_ann`.

Thus the coherent one-axis core has only `R^-1/2` local `L2` axial-strain content; all failure is explicitly annular/projective/derivative.

---

## 3. Exact directional growth

For a stochastic Cauchy deformation vector `Z`, define

\[
n_s=Z_s/|Z_s|.
\]

Along each stochastic history,

\[
\boxed{
\frac d{ds}\log|Z_s|
=n_s^T S(X_s,s)n_s.
}
\]

When `n_s` stays close to `e`,

\[
|n_s^TSn_s-e^TSe|
\le
2|n_s-e|\,|S|.
\]

The second term is retained as the direction-rotation/projective channel.

---

## 4. Core self-stretching is `O(1)` on the final `R^2` block

Let `K_tau` be the backward advection--diffusion transition density from the terminal point. The divergence-free Nash estimate gives

\[
\|K_\tau\|_2
\lesssim
(\nu\tau)^{-3/4}.
\]

Hence

\[
\mathbb E
\left[1_{\{X_\tau\in B_{cR}\}}
|e^T(Se)_{\rm core}(X_\tau)|
\right]
\lesssim
(\nu\tau)^{-3/4}R^{-1/2}.
\]

Integrating over

\[
0<\tau<cR^2,
\]

we get

\[
\boxed{
A_{\rm core}^{\rm final}
\lesssim_\nu 1.
}
\]

This is a statement only about the final crossing-parabolic block.

---

## 5. Macroscopic far strain is also `O(1)` on that block

The finite-kinetic-energy remote-strain tail in terminal normalization is

\[
\|S_{>M}\|_\infty
\lesssim
M^{-5/2}W^{1/4}\|u_0\|_2.
\]

Choose

\[
\boxed{
M_*=R^{4/5}W^{1/10}.
}
\]

Then

\[
M_*^{5/2}=R^2W^{1/4},
\]

so

\[
\boxed{
R^2\|S_{>M_*}\|_\infty
\lesssim C(\|u_0\|_2).
}
\]

Also, using `R \lesssim W^{1/10}`,

\[
M_*/R\to\infty,
\qquad
M_*/\sqrt W\to0.
\]

Thus the final-block intermediate annulus is broad in terminal normalized coordinates but physically shrinking.

---

## 6. Correct block-local conclusion

Define the directional stochastic action accumulated **only on the final crossing-parabolic block** by

\[
A_{\rm final}
=
\int_{-cR^2}^{0}
 n_s^TS(X_s,s)n_s\,ds
\]

with the appropriate backward-time convention.

The core and region beyond `M_*` contribute only `O(1)` to this final-block action. Therefore

\[
\boxed{
A_{\rm final}
\lesssim
O(1)
+A_{\rm ann}^{\rm final}
+A_{\rm dir}^{\rm final}
+A_{\rm deriv}^{\rm final}.
}
\]

Consequently, **if the final block itself carries a divergent amount of directional action**, then that divergent part must lie in

\[
R\lesssim|y-x_*|\lesssim M_*,
\]

or in direction/projective rotation, or in derivative/cutoff/Hessian forcing.

---

## 7. What this note does NOT say

A deeper first-hitting checkpoint may satisfy

\[
\|\Omega(s_-)\|_\infty\le q^{-1}
\]

with `q -> infinity`. The stochastic Cauchy formula then requires an amplification action comparable to `log q` over the **entire interval from that checkpoint to the terminal state**.

It is not proved that this whole `log q` action occurs in the last `O(R^2)` block. In fact the coherent mean vorticity is already order one at the first Reynolds-one crossing, so a substantial portion of the amplification may have occurred earlier.

Therefore the previous stronger schematic statement

\[
\log q
\lesssim
O(1)+A_{\rm ann}^{\rm final}+A_{\rm dir}^{\rm final}+A_{\rm deriv}^{\rm final}
\]

is withdrawn.

The correct next task is a **time-scale decomposition** of the full deep-checkpoint-to-crossing interval.

---

## 8. Relation to the deep stochastic-ancestor geometry

The deep-checkpoint ancestor results remain independent of this correction. They force large ancestor circulation into

- long diameter/length escape;
- small reach;
- large curvature;
- or geometrically inefficient folding.

The efficient precursor slab has separately been excluded by the first-hitting global enstrophy ceiling.

Thus the global proof frontier is not invalidated; only the localization of the full `log q` action to the final block was too strong.

Overall status: **FINAL CROSSING BLOCK LOCALIZATION VALID / FULL DEEP-CHECKPOINT AMPLIFICATION REQUIRES A SEPARATE TIME-SCALE PACKING ARGUMENT.**
