# M17 continuation frontier — M17-250 through M17-256

Date: 2026-09-06  
Scope: continuation after `INDEX_M17_238_249_FRONTIER.md`.

This index is additive and does not replace earlier canonical indices.

---

# 1. M17-250 — scale-comparable stopping packet or nodal concentration

Define on a nested raw spectral packet

\[
Q(B)=r(B)^4\frac{H(B)}{E(B)}.
\]

A dyadic raw-numerator / buffered-denominator child can be chosen with

\[
Q_{n+1}\ge\alpha Q_n,
\qquad\alpha>0.
\]

At the first crossing below a fixed threshold `C_*`,

\[
\boxed{
\alpha C_*<Q_N\le C_*.
}
\]

Therefore

\[
\boxed{r_N\asymp\ell_N}
\]

where

\[
\ell_N=(E_N/H_N)^{1/4}.
\]

If no crossing occurs, the nested radii shrink to zero and the limiting point must satisfy

\[
\boxed{W=0.}
\]

Thus

\[
\boxed{
H_{raw\ spectral\ packet}
\Longrightarrow
H_{scale\text{-}comparable\ packet}
\lor
G_{nodal\ concentration}.
}
\]

---

# 2. M17-251 — nonzero time-zero H2 tangent or renewed subscale descent

For a scale-comparable packet with nested regions

\[
B^{in}\Subset B^{mid}\Subset B^{out},
\]

assume a fixed inner mass fraction

\[
\int_{B^{in}}|W|^2\ge\eta E.
\]

Scale comparability and interior elliptic regularity give

\[
\boxed{
\|V_j\|_{H^2(B^{in})}\le C,
\qquad
\|V_j\|_{L^2(B^{in})}^2\ge\eta.
}
\]

Hence direct Rellich compactness on the fixed domain gives

\[
\boxed{
V_j\to V_0
\text{ strongly in }L^2(B^{in}),
\qquad
V_0\not\equiv0.
}
\]

If the inner mass fraction vanishes, the derivative numerator and `L2` denominator separate, restarting a strictly smaller raw packet selection or nodal concentration.

---

# 3. M17-252 — intrinsic tangent is heat, not global similarity OU

At own scale

\[
y=q_j+r_jz,
\qquad
\theta=\theta_j+r_j^2\tau,
\]

the exact rescaled equation is

\[
\boxed{
\partial_\tau V_j
+r_j[B(q_j+r_jz)-B(q_j)]\cdot\nabla V_j
=
\Delta V_j+r_j^2\Sigma_jV_j-r_j^2V_j.
}
\]

Therefore when the scaled drift/strain coefficients vanish, the tangent equation is

\[
\boxed{\partial_\tau V=\Delta V.}
\]

M17-249 remains valid for the global linear similarity equation, but it is not the direct intrinsic endpoint.

A separate Fourier argument proves

\[
\boxed{
\sup_{\tau\le0}\|V(\tau)\|_{L^2(\mathbb R^3)}<\infty,
\quad
\partial_\tau V=\Delta V
\Longrightarrow
V\equiv0.
}
\]

The missing ingredient is therefore the extraction of a nonzero ancient heat tangent with enough global spatial control.

---

# 4. M17-253 — H2 defect is a vanishing-mass high-frequency microcarrier

If

\[
V_j\to V
\quad\text{strongly in }L^2
\]

but the `H2` norm has a positive defect, fixed low frequencies cannot carry it because

\[
\|\Delta P_{\le N}(V_j-V)\|_2
\le N^2\|V_j-V\|_2.
\]

Hence the defect escapes to

\[
|\xi|\to\infty.
\]

At the same time

\[
\boxed{
\|P_{>N}V_j\|_2^2
\le C N^{-4}.
}
\]

Thus derivative-charge loss is exactly a vanishing-`L2` high-frequency microcarrier and returns to the M17-232/250 strict-subscale or nodal channel.

It is not a new terminal branch.

---

# 5. M17-254 — backward lifetime is a finite-T payer-or-corridor gate

For each fixed rescaled horizon `T`, partition

\[
[\theta_j-Tr_j^2,\theta_j]
\]

into finitely many M17-226 windows.

If any window has a fixed normalized payment or coefficient exit, record it.

Otherwise finite iteration gives

\[
\boxed{
C_T^-M_j(\theta_j)
\le M_j(\theta)
\le C_T^+M_j(\theta_j)
}

throughout the whole interval.

A diagonal subsequence over integer `T` provides mass normalization on every compact backward cylinder if all payers are absent.

Thus backward PDE existence is not the bottleneck; payer-free normalized persistence is.

---

# 6. M17-255 — finite-cylinder parabolic compactness

Write

\[
\partial_\tau V_j-\Delta V_j
=-A_j\cdot\nabla V_j+C_jV_j.
\]

For fixed `K,T`, define normalized surrounding mass

\[
\mathcal M_j(K,T)
=
\sup_{-T\le\tau\le0}
\int_{B_K}|V_j|^2
\]

and scaled coefficient size

\[
\mathcal C_j(K,T)
=
\|A_j\|_\infty+
\|C_j\|_\infty.
\]

If both remain bounded, local Caccioppoli gives

\[
V_j\text{ bounded in }L^2_tH^1_x,
\]

and the equation gives

\[
\partial_\tau V_j\text{ bounded in }L^2_tH^{-1}_x.
\]

Aubin--Lions yields strong local spacetime `L2` compactness.

If

\[
\mathcal C_j(K,T)\to0,
\]

the limit is caloric.

Thus

\[
\boxed{
H_{packet}
\Longrightarrow
H_{parabolic\ compactness}
\lor
G_{normalized\ mass\ decompactification}
\lor
G_{scaled\ ambient/coefficient}.
}
\]

---

# 7. M17-256 — normalized mass decompactification is palinstrophy or coherent mean background

For a fixed larger own-scale ball, let

\[
M_{j,K}
=
\int_{B_{Kr_j}}|W|^2,
\qquad
L_{j,K}=M_{j,K}/E_j.
\]

If

\[
L_{j,K}\to\infty,
\]

split

\[
W=c_{j,K}+w_{j,K},
\qquad
\int w_{j,K}=0.
\]

If the fluctuation carries a fixed mass fraction, Poincare gives

\[
\boxed{
\frac{r_j^2}{E_j}
\int_{B_{Kr_j}}|\nabla W|^2
\gtrsim L_{j,K}\to\infty.
}
\]

Hence a palinstrophy-quiet decompactification must satisfy

\[
\boxed{
\frac{\|w_{j,K}\|_2^2}{M_{j,K}}\to0.
}
\]

It is an almost constant coherent ambient mean background.

Define its own-scale dynamical size

\[
\boxed{
\beta_{j,K}=r_j^2|c_{j,K}|.
}
\]

Then

\[
\boxed{
G_{mass\ decompactification}
\Longrightarrow
H_{normalized\ palinstrophy}
\lor
G_{scaled\ ambient\ coefficient}
\lor
G_{dynamically\ weak\ coherent\ mean}.
}
\]

The last branch has

\[
|c_{j,K}|/a_j\to\infty
\]

but

\[
r_j^2|c_{j,K}|\to0.
\]

It is large only relative to the tiny packet normalization and is not an absolute amplitude blowup.

---

# 8. Current compressed frontier

The intrinsic spectral route is now

\[
\boxed{
G_{tempered\ spectral}
\Longrightarrow
G_{nodal/subscale}
\lor H_{normalized\ palinstrophy}
\lor G_{scaled\ ambient/coefficient}
\lor G_{dynamically\ weak\ coherent\ mean}
\lor H_{nonzero\ ancient\ local\text{-}L2\ heat\ tangent}.
}
\]

The last branch becomes contradictory only after a global `L2` or other suitable heat-growth condition is established.

The most genuinely new residual is

\[
\boxed{
G_{dynamically\ weak\ coherent\ mean}.
}
\]

This branch requires a renormalized fluctuation/background audit rather than another instantaneous CE-H estimate.

---

# 9. Next canonical target

The next useful module should analyze

\[
W=c_j+f_j
\]

on the dynamically weak coherent-mean branch with

\[
|c_j|/a_j\to\infty,
\qquad
r_j^2|c_j|\to0.
\]

The correct question is whether, after subtracting the mean explicitly in the **rescaled dynamic equation**, the forcing terms generated by `c_j` vanish because `r_j^2|c_j|->0`, or whether they return as a scaled ambient coefficient / interface payer.

If the forcing vanishes, one may recover a nonzero caloric fluctuation tangent even though the raw normalized field decompactifies by constants.

If it does not, the coherent mean is not dynamically weak after all and returns to the scaled ambient branch.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
