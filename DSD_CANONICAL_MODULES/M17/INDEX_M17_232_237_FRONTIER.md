# M17 continuation frontier — M17-232 through M17-237

Date: 2026-09-06  
Scope: continuation after `INDEX_M17_226_231_FRONTIER.md`.

This index is additive and does not replace earlier canonical indices.

---

# 1. M17-232 — nested physical re-extraction is valid, homogeneous CE-H inheritance is not

M17-228's fluctuation scale

\[
\widetilde\ell=(V/H)^{1/4}
\]

was only a numerical scale until an actual smaller buffer was re-extracted.

M17-232 applies the M17-224 raw-numerator / buffered-denominator pigeonhole recursively and proves a nested finite ladder

\[
B_0\supset B_1\supset\cdots\supset B_N
\]

with

\[
\ell_{n+1}\le q_*\ell_n,
\qquad0<q_*<1,
\]

and

\[
M_{n+1}<\theta M_n.
\]

Every numerator remains raw `|Delta W|^2` from the original field.

However, after subtracting constants,

\[
F_n=W-C_n
\]

satisfies

\[
\boxed{
\Delta F_n
=\kappa(F_n+C_n),
}
\]

not

\[
\Delta F_n=\kappa F_n.
\]

Thus the finite scale ladder is a genuine derivative-concentration ladder but not a ladder of new homogeneous CE-H solutions.

Any coefficient or unique-continuation theorem must return to the original `W` or keep the inhomogeneous source explicitly.

---

# 2. M17-233 — one-step Scale-Return Gate to an amplitude-independent coefficient channel

At the root intrinsic buffer,

\[
M=\int_B|W|^2,
\qquad
H=\int_K|\Delta W|^2,
\qquad
\ell^4=M/H.
\]

The exact CE-H identity is still

\[
H=\int_K\kappa^2|W|^2.
\]

Split

\[
W=c+w.
\]

If the fluctuation carries a fixed mass fraction, M17-228 gives intrinsic palinstrophy.

If the packet is mean dominated, then for any fixed coefficient ceiling

\[
\ell^2\|\kappa\|_\infty\le K_0
\]

and sufficiently small fixed mean-domination threshold `theta`, the small cancellation set cannot carry the full weighted spectral charge.

A fixed portion lies where

\[
W\asymp c.
\]

Removing the amplitude weight gives

\[
\boxed{
\int_B\kappa^2dy\gtrsim\ell^{-1}.
}
\]

The coefficient ceiling then yields

\[
\boxed{
\int_B|\kappa|^{3/2}dy
\ge c(A,K_0)>0.
}
\]

Therefore

\[
\boxed{
G_{intrinsic\ spectral}
\Longrightarrow
H_{palinstrophy}
\lor
G_{dimensionless\ \kappa\ spike}
\lor
H_{critical\ \kappa\ L^{3/2}}
\lor
G_{nodal/interface}.
}
\]

This is a one-step SRG in the sense of M17-229.

The relative-amplitude finite scale ladder remains mathematically valid, but it is no longer needed as an independent **root spectral** exit.

---

# 3. M17-234 — critical kappa occupancy must be nonconstant

Project

\[
\Delta W=\kappa W
\]

onto the local mean direction and test against a compact cutoff `phi`.

The constant vorticity mean drops out of

\[
\int W\Delta\phi,
\]

which gives

\[
\boxed{
\ell^2|\kappa_\phi|
\lesssim\sqrt\theta.
}
\]

But M17-233 gives a fixed scale-critical absolute `L^(3/2)` norm of `kappa`.

For sufficiently small `theta`, a nearly constant local potential cannot explain the packet.

Local Poincare yields

\[
\boxed{
\ell\|\nabla\kappa\|_{L^{3/2}(B)}
\ge c>0.
}
\]

Hence the bounded-spike coefficient branch is sharpened to amplitude-independent `kappa`-gradient criticality.

---

# 4. M17-235 — return to the existing weighted multiplier-diffusion ledger

If

\[
\ell^3\|\nabla\kappa\|_\infty
\]

is unbounded, retain an explicit dimensionless coefficient-derivative spike.

Otherwise the small cancellation set cannot carry all of the critical `L^(3/2)` gradient norm.

A fixed portion lies where

\[
|W|\gtrsim|c|.
\]

Then

\[
\int_G|\nabla\kappa|^2
\gtrsim\ell^{-3}
\]

and mean domination restores the vorticity weight:

\[
\boxed{
\int_B|W|^2|\nabla\kappa|^2dy
\gtrsim M\ell^{-6}.
}
\]

Equivalently,

\[
\boxed{
\frac{\ell^6}{M}
\int_B\rho^2|\nabla\kappa|^2dy
\gtrsim1.
}
\]

This connects the new coefficient branch to the multiplier-diffusion descriptor of M5-687/M17-145.

But the factor `M` remains.

Therefore the low-amplitude firewall is not removed.

---

# 5. M17-236 — the packet is sign balanced, so the global signed kappa budget does not close it

On the bounded coefficient branch,

\[
\int_K|\kappa|dy\gtrsim\ell
\]

while the compact CE-H test makes the signed local integral small.

After removing the small cancellation set,

\[
\boxed{
\int_G\kappa_+dy\gtrsim\ell,
\qquad
\int_G\kappa_-dy\gtrsim\ell.
}
\]

Since

\[
|W|^2\asymp M\ell^{-3}
\]

on the good set,

\[
\boxed{
\int_G\kappa_+|W|^2dy
\gtrsim M\ell^{-2},
}
\]

and

\[
\boxed{
\int_G\kappa_-|W|^2dy
\gtrsim M\ell^{-2}.
}
\]

The two parts may cancel in the signed quantity

\[
\int\kappa|W|^2.
\]

Moreover `M ell^-2` may vanish.

Thus M5-604's remote signed-budget tightness is fully compatible with the new packet.

The remaining obstruction is amplitude cancellation, not sign bookkeeping.

---

# 6. M17-237 — M17-207 cubic packing cannot remove the amplitude firewall by itself

At cell level M17-235 gives

\[
D_i
\gtrsim
\frac{H_i^{3/2}}{M_i^{1/2}}.
\]

Holder removes cell fragmentation:

\[
\boxed{
\sum_i\frac{H_i^{3/2}}{M_i^{1/2}}
\ge
\frac{(\sum_iH_i)^{3/2}}
{(\sum_iM_i)^{1/2}}.
}
\]

Thus a shell with

\[
H_k=\Lambda_k^2E_k
\]

has at best the aggregate floor

\[
\boxed{
D_{\kappa,k}^{agg}
\gtrsim
E_k\Lambda_k^3.
}
\]

On M17-207 shells

\[
E_k=\frac{b_k}{R_k},
\]

so

\[
\boxed{
D_{\kappa,k}^{agg}
\gtrsim
\frac{b_k}{R_k}\Lambda_k^3.
}
\]

M17-207 provides

\[
\sum b_k^{3/2}=\infty,
\]

but this does not imply divergence of the multiplier-diffusion sum.

The abstract sequence

\[
R_k=2^k,
\qquad
b_k=(k+1)^{-2/3},
\qquad
\Lambda_k=(k+1)^{1/10}
\]

satisfies

\[
\sum b_k^{3/2}=\infty,
\qquad
\Lambda_k\to\infty,
\]

but

\[
\sum\frac{b_k}{R_k}\Lambda_k^3<\infty.
\]

Therefore the apparent `3/2` exponent match is not a closure theorem.

---

# 7. Correct compressed frontier

The M17-231 frontier

\[
G_{relative\text{-}amplitude\ finite\ scale\ ladders}
\]

has now been reduced.

The corrected root spectral frontier is

\[
\boxed{
G_{tempered\ whole\text{-}shell\ H2/L2\ spectral}
\Longrightarrow
H_{intrinsic\ palinstrophy}
\lor
G_{\kappa\text{-}spike}
\lor
G_{\nabla\kappa\text{-}spike}
\lor
H_{weighted\ multiplier\ diffusion}
\lor
G_{nodal/interface}.
}
\]

The scale-return problem is therefore no longer the main bottleneck.

The new bottleneck is an **Amplitude-Return / Genealogy Rate Bridge**:

\[
\boxed{
\text{low-amplitude coefficient activity}
\xrightarrow{\ ?\ }
\text{radius-independent lower-order budget charge}
\lor
\text{formed replenishment/nodal event}.
}
\]

---

# 8. Next canonical target

The next useful module should not repeat shell summation or fixed-order derivative estimates.

It should test one of the following genuinely missing bridges:

1. **material genealogy:** a remote high-coefficient packet cannot be independently replaced at every shell without a fixed replenishment action;
2. **amplitude persistence:** derive a lower bound preventing `M ell^-2` from vanishing on all recurrent coefficient packets;
3. **coefficient-spike descent:** show `ell^2||kappa||_infty` or `ell^3||grad kappa||_infty` escalation returns to a formed positive/negative amplitude event;
4. **absolute coefficient ledger:** control `int |kappa||W|^2` or an unweighted critical coefficient norm by a genuine spacetime budget.

No such bridge is currently derived.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
