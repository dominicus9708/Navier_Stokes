# M17 continuation frontier — M17-226 through M17-231

Date: 2026-09-06  
Scope: continuation after `INDEX_M17_219_225_FRONTIER.md`.

This index is additive and does not replace the earlier canonical indices.

---

# 1. M17-226 — two-sided packet mass bookkeeping

M17-225's exact localized enstrophy identity gives both a lower and an upper differential inequality.

Therefore fixed-fraction forward/backward changes of localized packet mass are not free:

\[
\boxed{
\text{forward loss}
\to
\text{palinstrophy/interface payment},
}
\]

\[
\boxed{
\text{forward growth or backward ancestor deficit}
\to
\text{interface/replenishment input},
}
\]

and backward ancestor excess is a forward loss event.

Conditionally, if all such payments are negligible, the packet has a two-sided parabolic mass corridor

\[
M_j(\theta)\asymp M_j(0)
\quad
\text{for }|\theta|\lesssim r_j^2.
\]

M17-226 explicitly warns that two-sided mass comparability is not yet derivative compactness.

---

# 2. M17-227 — free persistence is removed by Poincare

For the compact cutoff packet

\[
F_j=\zeta_jW,
\]

scale-`r_j` Poincare gives

\[
\boxed{
M_j
\le
C r_j^2D_j+C N_j.
}
\]

Hence a packet that retains a fixed mass fraction for one parabolic lifetime automatically satisfies

\[
\boxed{
\int D_jd\theta
+r_j^{-2}\int N_jd\theta
\gtrsim M_j(0).
}
\]

Combined with M17-225, both early loss and persistence force this cutoff-coercive quantity.

Thus the previously anticipated no-cost heat-tangent route is not needed to eliminate free compact persistence.

---

# 3. M17-228 — transition occupancy is not automatically physical turnover

A DSD audit corrects the interpretation of

\[
N_j
=\int_{\operatorname{supp}\nabla\zeta_j}|W|^2.
\]

This is cutoff transition occupancy, not by itself a signed physical flux.

To remove the artifact, decompose on the physical buffer ball

\[
W=\bar W+w,
\qquad
\int w=0.
\]

The mean satisfies

\[
\Delta\bar W=0,
\]

so all raw spectral charge belongs to `w`.

For a fixed threshold `theta`:

### fixed-fraction fluctuation

If

\[
\|w\|_2^2\ge\theta\|W\|_2^2,
\]

then mean-zero Poincare gives genuine cutoff-independent palinstrophy

\[
\boxed{
\int|\nabla W|^2
\gtrsim
\theta\ell^{-2}\|W\|_2^2.
}
\]

### mean-dominated packet

If

\[
\|w\|_2^2<\theta\|W\|_2^2,
\]

then the same raw `H2` numerator is divided by a smaller `L2` denominator and

\[
\boxed{
\ell_{new}<\theta^{1/4}\ell_{old}.
}
\]

Thus

\[
\boxed{
G_{intrinsic\ spectral}
\Longrightarrow
H_{palinstrophy}
\lor
G_{strict\ spectral\ microcarrier\ descent}.
}
\]

---

# 4. M17-229 — the microcarrier cascade is only a family of finite scale ladders

An indefinitely descendable branch is not treated as one formed infinite object.

For every finite depth `N`, define

\[
\mathcal S_{0\to N}.
\]

If no palinstrophy return occurs before depth `N`, then

\[
\boxed{
\ell_N\le\theta^{N/4}\ell_0,
\qquad
M_N\le\theta^NM_0.
}
\]

M17-009 cannot close this branch because it concerns nodal topology changes in a fixed compact marked core, whereas the present carrier is remote and may sit on a nonzero mean background.

The finite derivative-witness audit likewise forbids treating arbitrarily long finite descent as an automatic infinite contradiction.

A new proof obligation is therefore defined:

\[
\boxed{\text{Scale-Return Gate (SRG)}.}
\]

An SRG must force a uniformly finite-depth scale ladder back into a lower-order budgeted channel with a charge independent of internal ladder depth.

Current status:

\[
\boxed{\text{SRG NOT DERIVED}.}
\]

---

# 5. M17-230 — naive palinstrophy summation is pruned

The model descent

\[
M_n=\theta^nM_0,
\qquad
\ell_n=\theta^{n/4}\ell_0
\]

shows

\[
\boxed{
\frac{M_n}{\ell_n^2}
=	heta^{n/2}\frac{M_0}{\ell_0^2}.
}
\]

Hence the instantaneous Poincare palinstrophy floors are summable in scale depth.

Over one own-scale parabolic lifetime,

\[
\mathcal A_n^{min}
\sim M_n
=\theta^nM_0,
\]

which is also summable.

Therefore

\[
\boxed{
\ell_n\to0
\not\Rightarrow
\text{nonsummable lower-order cost}.
}
\]

The SRG needs additional amplitude-scale, genealogy, coefficient, or nodal information.

---

# 6. M17-231 — parent-scale analyticity does not provide SRG

M5-392 gives global fixed-order derivative bounds in the original parent first-hitting normalization.

If those bounds transfer to the M17 packet representation, then for a packet of radius `O(ell)`

\[
H=\int|\Delta W|^2
\lesssim\ell^3.
\]

Since

\[
M=\ell^4H,
\]

one may have

\[
\boxed{M\lesssim\ell^7.}
\]

Thus bounded absolute derivatives are compatible with rapidly vanishing carrier mass and divergent derivative-to-mass ratios.

The surviving mechanism is therefore

\[
\boxed{
\text{relative-amplitude / occupancy degeneration},
}
\]

not pointwise derivative blowup.

If the M17 representation is not parent-scale equivalent, M5-392 cannot be imported without an explicit scale map.

In neither case does parent-scale analyticity close the scale ladder.

---

# 7. Current compressed frontier

The old anticipated route

\[
\text{intrinsic packet}
\to
\text{two-sided persistence}
\to
\text{heat tangent}
\to
\text{Liouville}
\]

is no longer the canonical main line.

The corrected frontier is

\[
\boxed{
G_{tempered\ whole\text{-}shell\ H2/L2\ spectral}
\Longrightarrow
H_{intrinsic\ palinstrophy}
\lor
G_{relative\text{-}amplitude\ finite\ scale\ ladders}
\lor
G_{nodal/thin/rank/interface}
\lor
G_{coefficient/nonlocal\ criticality}.
}
\]

The genuinely new unresolved core is

\[
\boxed{
G_{relative\text{-}amplitude\ finite\ scale\ ladders}
\xrightarrow{\ ?\ }
\text{depth-independent lower-order budget charge}.
}
\]

This is the **Scale-Return Gate** problem.

---

# 8. Next canonical target

The next useful module should test a relative-amplitude or genealogy quantity, not another fixed-order derivative bound.

Candidate targets are:

1. local amplitude/doubling lower bounds for `Delta W=kappa W` strong enough to prevent `M/ell^alpha ->0` too rapidly;
2. material genealogy preventing each scale level from using a completely new vanishing mass carrier;
3. a coefficient-return theorem showing sufficiently deep relative-amplitude descent forces an amplitude-independent `kappa`, `grad kappa`, rank, or nodal charge;
4. a direct shell-charge preservation theorem linking a fixed fraction of the M17-207 nonsummable shell defect to one lower-order payment independent of microcarrier depth.

None is yet derived.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
