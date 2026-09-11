# M19-050 — First-hitting center nesting bounds eccentricity by J^{-1/4} but leaves a sharp common-center exponent gap

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC SPATIAL COHERENCE / FIRST-HITTING CENTER NESTING / EXPONENT-GAP FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-049 proves terminal-time alignment of the cubic-dominant kinetic-Morrey genealogy and reduces spatial coherence to the eccentricity

\[
\eta_k
=
\frac{|x_k-x_\infty|}{\rho_k}.
\]

A tempting route is to identify \(x_k\) with one persistent material center and integrate the M19-039 center-velocity bound all the way to \(T_*\).

M18-045 forbids that generic shortcut: remote-age recurrence need not use the same material carrier through arbitrarily many stages.

The present module instead uses the **Eulerian first-hitting center nesting theorem**, which does not assume same-material persistence.

## 2. First-hitting center nesting on the no-remote branch

Let \(X_n\) be the center of the stage-\(n\) first-hitting maximum and

\[
r_n=\sqrt{\nu/W_n}.
\]

M18-043 / M5-399 prove the exact center split.

On the complement of a formed remote satellite,

\[
\boxed{
\frac{|X_{n+1}-X_n|}{r_n}
\le A_*<\infty.
}
\]

Since

\[
r_{n+1}=q^{-1/2}r_n,
\]

the physical increments are summable:

\[
\sum_{m\ge n}|X_{m+1}-X_m|
\le
A_*\sum_{m\ge n}r_m
\le
C_qA_*r_n.
\]

Therefore the first-hitting centers converge to one terminal physical center \(X_*\) and

\[
\boxed{
|X_*-X_n|
\le
C_Xr_n.
}
\]

This is an Eulerian center statement and does not require persistent material identity.

## 3. Natural first-hitting scale associated with a shell charge J

For the cubic-dominant shell event \((J_k,\rho_k)\), M19-046 gives the amplitude floor

\[
A_k
\asymp
\frac{J_k^{1/2}}{\rho_k^2}.
\]

Choose \(n(k)\) so that

\[
W_{n(k)}\asymp A_k.
\]

Then its first-hitting natural length is

\[
\begin{aligned}
r_{n(k)}
&=
\sqrt{\frac{\nu}{W_{n(k)}}}\\
&\asymp
C_\nu
\frac{\rho_k}{J_k^{1/4}}.
\end{aligned}
\]

Thus

\[
\boxed{
\frac{r_{n(k)}}{\rho_k}
\asymp
J_k^{-1/4}.
}
\]

The factor \(J^{-1/4}\) is the exact amplitude-to-geometric-scale mismatch.

## 4. Proximity branch versus off-center realization defect

The shell witness center \(x_k\) need not automatically equal the global first-hitting center \(X_{n(k)}\).

Therefore split:

### Proximity branch

\[
\boxed{
|x_k-X_{n(k)}|
\le
C_Pr_{n(k)}.
}
\]

### Off-center realization branch

\[
\boxed{
|x_k-X_{n(k)}|
\gg
r_{n(k)}.
}
\]

The second branch is a genuine moving-center / remote-realization defect. It must not be silently discarded or called center nesting.

The present calculation first treats the proximity branch.

## 5. Eccentricity ceiling on the proximity branch

By the triangle inequality,

\[
|x_k-X_*|
\le
|x_k-X_{n(k)}|
+|X_{n(k)}-X_*|.
\]

Using Sections 2--4,

\[
|x_k-X_*|
\le
(C_P+C_X)r_{n(k)}.
\]

Therefore

\[
\boxed{
\eta_k
:=
\frac{|x_k-X_*|}{\rho_k}
\lesssim
J_k^{-1/4}.
}
\]

This is substantially stronger than an unconstrained \(\eta_k\to\infty\), but it still allows eccentricity to diverge when \(J_k\to0\).

## 6. Common-center kinetic Morrey lower bound

M19-049 gives

\[
\mathcal M_k^{com}
\gtrsim
\frac{J_k}{\eta_k+C_E}.
\]

On the proximity/nested-center branch,

\[
\eta_k+C_E
\lesssim
1+J_k^{-1/4}.
\]

For the hard small-charge sector \(J_k\le1\),

\[
1+J_k^{-1/4}
\lesssim
J_k^{-1/4}.
\]

Hence

\[
\boxed{
\mathcal M_k^{com}
\gtrsim
J_k^{5/4}.
}
\]

If instead \(J_k\ge j_*>0\) on infinitely many selected shells, then the same estimate gives a fixed positive common-center Morrey floor and the branch already enters the ordinary R-critical terminal stack.

Thus only \(J_k\to0\) is genuinely difficult.

## 7. The exponent gap

The original cubic tail criterion is

\[
\boxed{
\sum_kJ_k^{3/2}=\infty.
}
\]

The common-center Morrey lower bound gives

\[
(\mathcal M_k^{com})^{3/2}
\gtrsim
J_k^{15/8}.
\]

But

\[
\boxed{
\sum_kJ_k^{3/2}=\infty
\not\Rightarrow
\sum_kJ_k^{15/8}=\infty.
}
\]

The exponent loss is

\[
\boxed{
\frac{15}{8}-\frac32
=\frac38.
}
\]

Therefore first-hitting center nesting alone does not transfer the full cubic nonsummability into one common-center scattering stack.

## 8. Explicit arithmetic firewall

Take

\[
J_k=k^{-2/3}.
\]

Then

\[
J_k^{3/2}=k^{-1},
\]

so

\[
\sum_kJ_k^{3/2}=\infty.
\]

But

\[
J_k^{15/8}
=
k^{-5/4},
\]

and hence

\[
\sum_kJ_k^{15/8}<\infty.
\]

This sequence is also compatible with the M19-046 cubic-dominant condition for geometric \(\rho_k\), because

\[
J_k/\rho_k\to\infty.
\]

Thus the exponent gap is not a formal edge case. It survives the main sharp R-AC asymptotic regime.

## 9. Interpretation of the J^{-1/4} loss

The shell amplitude is

\[
|\omega|
\sim
\frac{J^{1/2}}{\rho^2}.
\]

The natural first-hitting length associated with that amplitude is

\[
r_A
\sim
|\omega|^{-1/2}
\sim
\frac{\rho}{J^{1/4}}.
\]

When \(J\ll1\),

\[
r_A\gg\rho.
\]

Thus a small cubic shell packet can carry large relative enstrophy density while still occupying a geometric radius smaller than the natural first-hitting core associated with its peak amplitude.

Center nesting controls displacement on the larger scale \(r_A\), not directly on \(\rho\).

This geometric mismatch is exactly the source of the \(J^{-1/4}\) eccentricity and \(J^{5/4}\) common-center loss.

## 10. Off-center realization branch

If

\[
|x_k-X_{n(k)}|/r_{n(k)}\to\infty,
\]

then the shell witness lies increasingly far from the first-hitting core even in its amplitude-natural units.

If the shell has enough amplitude/volume coherence to form an active source at that location, this is a formed remote satellite and returns to the M19-044 remote routing.

If it does not have enough natural-scale volume to form such a source, then it is a **sub-natural off-center shell realization**.

This latter case is not closed by M18-043, because M18-043's formed-remote theorem applies to a natural active maximum packet, not automatically to a smaller weak shell witness.

Thus the safe split is

\[
\boxed{
G_{offcenter\ shell}
\to
G_{formed\ remote}
\lor
G_{subnatural\ offcenter\ realization}.
}
\]

The second is a genuine representation endpoint, not to be hidden inside remote terminology.

## 11. Updated R-AC spatial frontier

The quiet kinetic-Morrey R-AC branch now has two precise spatial survivors:

\[
\boxed{
\mathcal R_{AC}^{KM}
\Longrightarrow
G_{nested\ center\ with\ exponent\ gap}
\lor
G_{subnatural\ offcenter\ realization}
\lor
G_{typed\ remote/export}.
}
\]

On the nested-center branch,

\[
\boxed{
\mathcal M_k^{com}\gtrsim J_k^{5/4}
}
\]

but cubic nonsummability is not preserved.

On the sub-natural off-center branch, the amplitude-natural scale is known but spatial proximity to the main first-hitting core is not.

## 12. What would remove the exponent gap

Any improvement from

\[
\eta_k\lesssim J_k^{-1/4}
\]

to

\[
\eta_k\lesssim J_k^{-\alpha}
\]

would give

\[
\mathcal M_k^{com}
\gtrsim
J_k^{1+\alpha}.
\]

To preserve the original cubic exponent under the \(3/2\) scattering/Morrey power, one needs

\[
\frac32(1+\alpha)
\le
\frac32,
\]

hence

\[
\boxed{\alpha=0.}
\]

In other words, no positive power loss in eccentricity is harmless for the weakest cubic-divergent sequences.

Therefore a full reduction to the existing common-center critical scattering root needs **uniform shell-scale center coherence**, not merely amplitude-natural center coherence.

## 13. New target

The next calculation should attack the sub-natural mismatch directly.

The packet has

\[
m_k\gtrsim J_k/\rho_k,
\]

peak amplitude at most/comparable to

\[
J_k^{1/2}/\rho_k^2,
\]

and geometric radius \(\rho_k\), while its amplitude-natural scale is

\[
r_A\sim\rho_kJ_k^{-1/4}.
\]

A useful dimensionless filling fraction is therefore

\[
\boxed{
\varphi_k
:=
\left(\frac{\rho_k}{r_A}\right)^3
\asymp
J_k^{3/4}.
}
\]

The next question is whether the missing \(J^{1/4}\) center factor can be recovered through multiplicity/filling inside one natural first-hitting core, or whether sparse filling creates a new concentration/derivative payment.

This is now a precise amplitude-volume geometry problem.

---

\[
\boxed{\text{M19-050 COMPLETE; FIRST-HITTING NESTING LEAVES A SHARP J^{1/4} SPATIAL COHERENCE LOSS.}}
\]