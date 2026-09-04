# DSD M17-031 — Oblique rank-two vortex curvature has an exact material decay law and area–curvature product law

Date: 2026-09-04
Canonical ID: **M17-031**

Status: **INTERNAL OBLIQUE CO-FROZEN COMPATIBILITY / DEFINE THE VORTEX-DIRECTION CURVATURE `b=(xi·grad)xi`. BECAUSE THE CE-H DIRECTOR IS MATERIALLY FROZEN AND THE STRAIN EIGENLINE GIVES `(xi·grad)B=(sigma+1/2)xi`, COMMUTING THE MATERIAL DERIVATIVE WITH THE DIRECTIONAL DERIVATIVE YIELDS THE EXACT VECTOR LAW `D_B b=-(sigma+1/2)b`. THE DIRECTOR-AREA DENSITY OBEYS `D_B j_xi=(sigma-1)j_xi`, SO THE PRODUCT SATISFIES THE STRAIN-INDEPENDENT LAW `D_B(j_xi b)=-(3/2)j_xi b`. MULTIPLYING BY A MATERIAL VOLUME ELEMENT, WHICH GROWS AT RATE `3/2`, SHOWS THAT `j_xi b dV` IS AN EXACT MATERIAL VECTOR CHARGE. ON THE TRANSVERSE-RANK-TWO OBLIQUE SUBBRANCH (`j_xi!=0`), NONZERO OBLIQUITY IS EQUIVALENT TO NONZERO CURVATURE THROUGH THE KERNEL EQUATION. HENCE A SAME-MARKER COMPACT RECURRENT OBLIQUE ORBIT CANNOT KEEP BOTH `j_xi` AND `b` UNIFORMLY NONZERO: THE PRODUCT DECAYS EXPONENTIALLY. AN EULERIAN RECURRENT SURVIVOR MUST THEREFORE USE MATERIAL TURNOVER, TRANSVERSE-RANK LOSS, OR THE `j_xi=0` PURE-TRANSVERSE-KERNEL SUBBRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Curvature of the vortex-direction field

Define

\[
\boxed{
b:=(\xi\cdot\nabla)\xi.
}
\]

Because `|xi|=1`,

\[
b\cdot\xi=0.
\]

Thus `b` is the Euclidean curvature vector of the unit-speed vortex-direction integral curves.

- `b=0` is the straight-line case of M17-029;
- `b!=0` is the curved-line geometry relevant to the genuinely oblique rank-two branch.

---

## 2. Material derivative of a spatial gradient

For any materially frozen scalar/vector component `f` with

\[
D_Bf=0,
\]

one has

\[
D_B(\partial_jf)
=-(\partial_jB_k)\partial_kf.
\]

Apply this componentwise to `xi`, using

\[
D_B\xi=0.
\]

Then

\[
D_B(\partial_j\xi_i)
=-(\partial_jB_k)\partial_k\xi_i.
\]

---

## 3. Exact material curvature law

Compute

\[
\begin{aligned}
D_Bb_i
&=D_B(\xi_j\partial_j\xi_i)\\
&=(D_B\xi_j)\partial_j\xi_i
+\xi_jD_B(\partial_j\xi_i)\\
&=-\xi_j(\partial_jB_k)\partial_k\xi_i.
\end{aligned}
\]

Hence

\[
D_Bb
=-\big((\xi\cdot\nabla)B\cdot\nabla\big)\xi.
\]

Now

\[
B=U+\frac12y.
\]

The CE-H strain eigenline gives

\[
(\xi\cdot\nabla)U=\sigma\xi,
\]

because the antisymmetric velocity-gradient part annihilates `xi` when the vorticity is parallel to `xi`.
Therefore

\[
\boxed{
(\xi\cdot\nabla)B
=\left(\sigma+\frac12\right)\xi.
}
\]

Substitution gives

\[
\boxed{
D_Bb
=-\left(\sigma+\frac12\right)b.
}
\]

This is an exact vector law, not merely a norm estimate.

---

## 4. Curvature direction is materially fixed while nonzero

On an interval where `b!=0`,

\[
D_B\log|b|
=-\sigma-\frac12.
\]

Since the right side multiplies the vector itself,

\[
\boxed{
D_B\widehat b=0,
\qquad
\widehat b:=b/|b|.
}
\]

Thus the physical direction of the vortex-line curvature vector is materially frozen on the CE-H branch.

This is a stronger geometric constraint than a generic evolving curved vortex line.

---

## 5. Combine with director-area density

M16-025/M17-026 give

\[
\boxed{
D_B\log|j_\xi|=\sigma-1
}
\]

where

\[
j_\xi=J_\xi\cdot\xi.
\]

Therefore

\[
\begin{aligned}
D_B(j_\xi b)
&=(\sigma-1)j_\xi b
-\left(\sigma+\frac12\right)j_\xi b\\
&=-\frac32j_\xi b.
\end{aligned}
\]

Hence

\[
\boxed{
D_B(j_\xi b)
=-\frac32j_\xi b.
}
\]

Equivalently,

\[
\boxed{
D_B\log(|j_\xi||b|)
=-\frac32.
}
\]

The aligned strain `sigma` cancels exactly.

---

## 6. Material-volume cancellation

Similarity material volume satisfies

\[
D_BdV
=(\nabla\cdot B)dV
=\frac32dV.
\]

Therefore

\[
D_B\big(j_\xi b\,dV\big)=0.
\]

Thus

\[
\boxed{
j_\xi b\,dV}
\]

is an exact material vector charge.

The pointwise area–curvature density decays at `3/2`, precisely compensating the similarity-material volume expansion.

---

## 7. Kernel equation links obliquity to curvature

Rank two gives a one-dimensional kernel of `d xi` spanned by the director-area current:

\[
(J_\xi\cdot\nabla)\xi=0.
\]

Use the M17-028 decomposition

\[
J_\xi=c\widetilde W+K_\xi,
\qquad
\widetilde W=\widetilde\rho\xi,
\qquad
K_\xi\perp\xi.
\]

Then

\[
0
=c\widetilde\rho(\xi\cdot\nabla)\xi
+(K_\xi\cdot\nabla)\xi.
\]

Hence

\[
\boxed{
(K_\xi\cdot\nabla)\xi
=-c\widetilde\rho\,b.
}
\]

Suppose the restriction

\[
A_\perp:=d\xi|_{\xi^\perp}
\]

is invertible, equivalently

\[
j_\xi\ne0.
\]

Then

\[
\boxed{
K_\xi
=-c\widetilde\rho\,A_\perp^{-1}b.
}
\]

Therefore on this **transverse-rank-two** subbranch,

\[
K_\xi\ne0
\iff
b\ne0
\]

provided `c!=0`.

Thus genuine obliquity is exactly the compensation of curved vortex direction by transverse director variation.

---

## 8. Same-marker recurrence obstruction

Assume a marked material oblique trajectory remains inside a compact regular class with

\[
0<c_j\le|j_\xi|\le C_j,
\]

and

\[
0<c_b\le|b|\le C_b.
\]

Then the exact product law gives

\[
|j_\xi b|(\theta)
=|j_\xi b|(\theta_0)
\exp\left[-\frac32(\theta-\theta_0)\right].
\]

This cannot be recurrent or remain bounded below for arbitrarily large forward similarity time.

Hence

\[
\boxed{
R_2^{oblique,\,same-marker}
\not\supset
\{j_\xi,b\text{ both uniformly nonzero recurrent}\}.
}
\]

A same-marker recurrent oblique orbit must therefore lose at least one of

\[
\boxed{
|j_\xi|\ge c>0,
\qquad
|b|\ge c>0.
}
\]

---

## 9. Allowed exits

The exact law leaves the following possibilities:

1. `j_xi -> 0`: transverse director rank degenerates, even if full `rank dxi=2` may temporarily persist;
2. `b -> 0`: the vortex-line geometry approaches the parallel/straight branch;
3. material labels leave the bounded Eulerian oblique core and are replaced by new labels;
4. the special `j_xi=0` rank-two subbranch, where the kernel of `d xi` is purely transverse to `xi`.

The first two connect directly to already isolated branch interfaces.
The third is a turnover mechanism.
The fourth requires a separate audit because `A_perp` is then singular even though the full differential may still have rank two.

---

## 10. DSD interpretation

The oblique branch now has three descriptor levels:

\[
\boxed{
K_\xi
\to
b=(\xi\cdot\nabla)\xi
\to
j_\xi b.
}
\]

- `K_xi` measures area-current obliquity;
- `b` measures actual vortex-line curvature;
- `j_xi b` combines curvature with the transverse director-area content and has a universal material exponent.

This exposes a material recurrence obstruction that is invisible in the mean-strain statement of M17-028.

---

## 11. DSD audit

### Audit A — equating full rank two with j_xi != 0
Rejected. Full `rank dxi=2` can in principle coexist with `j_xi=0`; that special branch is explicitly retained.

### Audit B — claiming Eulerian recurrence is impossible
Rejected. The exact decay obstructs same-marker recurrence, but an Eulerian recurrent structure can in principle be maintained by material turnover.

### Audit C — claiming b direction must rotate with the curved line
Rejected. The CE-H material-freezing law forces `D_B bhat=0` while `b!=0`.

### Audit D — assuming c nonzero without scope
The equivalence `K_xi !=0 iff b!=0` is asserted only on the transverse-rank-two subbranch with `j_xi!=0` and nonzero parallel coefficient.

### Audit E — proof status
The general oblique Rank-2 branch is not yet closed.

---

## 12. Updated oblique frontier

The rank-two oblique branch is refined to

\[
\boxed{
R_2^{oblique}
\Longrightarrow
T_{mat}^{oblique}
\ \lor\ 
D_{j}^{transverse-rank-loss}
\ \lor\ 
P_{b\to0}^{parallel-exit}
\ \lor\ 
R_{2,j=0}^{pure-transverse-kernel}.
}
\]

The same-marker compact recurrent subbranch with both transverse director area and vortex curvature uniformly nonzero is excluded.

---

## 13. Next target

Two high-value targets remain:

1. audit the material-turnover rate required to keep an Eulerian oblique Rank-2 core recurrent despite `D_B(j_xi b)=-(3/2)j_xi b`;
2. classify the special full-rank-two but `j_xi=0` branch, where the kernel of `d xi` lies entirely in `xi^perp`.

The second is structurally cleaner and is the next preferred calculation.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
