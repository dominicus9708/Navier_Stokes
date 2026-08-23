# Anti-Proof Corrected Global Frontier — 2026-08-24

Status: **EXHAUSTIVENESS AUDIT CONSOLIDATION / TWO OVER-COMPRESSIONS CORRECTED / SEVERAL GAUGE GAPS REPAIRED / GLOBAL REGULARITY NOT PROVED.**

This note records the proof tree after deliberately trying to break the DSD-guided classification from the original Navier--Stokes equations.

The audit found two real scope problems:

1. uniform normalized global enstrophy was used too broadly in one ancient-compactness route;
2. a weak-L3 endpoint tail was stated too broadly as the unique bounded-Z tail.

Both are now corrected. Additional Galilean-drift auditing shows that relative Campanato, not absolute local drift, is the correct invariant local-energy object.

---

## 1. What remains valid before the ancient step

The late first-hitting tower still has

\[
W_j=q^jW_0,
\qquad
r_j=W_j^{-1/2},
\]

and on the non-long/short-stage corridor

\[
0<L_-\le L_j\le L_+<\infty.
\]

First-hitting analyticity yields uniform fixed-order normalized derivative amplitudes, so local derivative blow-up is removed and the original `H` branch reduces to derivative spatial non-tightness.

No-T center replacement gives

\[
|X_{j+1}-X_j|\lesssim r_j,
\]

hence a unique candidate physical singular point.

Historical fixed-occupancy shell recycling is already routed to

\[
H_{remote}\lor T.
\]

These statements were not invalidated by the anti-proof audit.

---

## 2. Correction A: global normalized enstrophy need not be uniformly bounded

The first-hitting cap gives the unconditional enstrophy differential estimate

\[
Z_j'\le\sqrt2Z_j,
\]

and therefore

\[
\sum_jW_j^{-1/2}Z_j(0)<\infty.
\]

But this still allows

\[
Z_j\to\infty
\]

slowly.

Thus

\[
\boxed{
\text{no-H/T}
\not\Rightarrow
\sup_jZ_j<\infty
}
\]

has not been proved.

If `Z_j` diverges, its half-enstrophy radius tends to normalized infinity, so the excess is necessarily spatially non-tight.

---

## 3. Repair A: local ancient compactness does not need global Z

On a scale-invariant local-energy Morrey corridor, fixed-R local `A/E/C/D` bounds follow from

- local kinetic energy;
- the first-hitting vorticity cap;
- local/far strain decomposition;
- parent pressure decay.

Therefore local suitable ancient extraction remains available even if

\[
Z_j\to\infty.
\]

The compactness issue is thus widened from a bounded-Z ancient class to a local-energy/Morrey ancient class rather than lost entirely.

---

## 4. Galilean repair: relative Campanato is fundamental

Define

\[
\mathcal C_R
=R^{-1}
\int_{B_R}|U-(U)_{B_R}|^2.
\]

Remote strain annihilates constant velocity and is controlled directly by the dyadic relative-Campanato ledger.

The apparent problem that absolute Morrey is not Galilean invariant is resolved at all scales by finite kinetic energy.

For a finite-energy first-hitting field,

\[
(U)_{B_R}\to0
\qquad(R\to\infty).
\]

If

\[
\sup_{R\ge R_0}\mathcal C_R\le C_*,
\]

then adjacent mean telescoping gives

\[
|(U)_{B_R}|\lesssim C_*^{1/2}R^{-1},
\]

and hence

\[
\boxed{
R^{-1}\int_{B_R}|U|^2
\lesssim C_*.
}
\]

Thus

\[
\boxed{
\text{finite energy + all-scale relative Campanato}
\Longrightarrow
\text{absolute Type-I Morrey}.
}
\]

A large coherent drift can be invisible locally, but finite energy forces it to transition to zero, and that transition creates relative-Campanato escalation at some parent scale.

---

## 5. Time-dependent drift is also typed exactly

For the self-consistent moving mean path

\[
\dot a=m_\phi,
\]

with `v=u-m_phi`,

\[
\boxed{
M_\phi\dot m_\phi
=
\int(v\otimes v)\nabla\phi
+
\int(p-c)\nabla\phi
+
\nu\int v\Delta\phi.
}
\]

So large drift acceleration requires

\[
\text{relative variance}
\lor
\text{pressure oscillation}
\lor
\text{viscous boundary action}.
\]

No term proportional to the absolute drift survives.

This prevents a large but harmless Galilean translation from being mislabeled as turnover.

---

## 6. Core tracking no longer requires a maximum trajectory

Along the same relative-mean path, the localized enstrophy satisfies

\[
\boxed{
E_\phi'
+
u\int\phi|\nabla\Omega|^2
=
\int\phi\Omega^TS\Omega
+
\int e(U-m)\cdot\nabla\phi
+
\nu\int e\Delta\phi.
}
\]

Therefore a fixed loss/rebuild of local vorticity mass pays a fixed amount of

\[
\text{stretching}
\lor
\text{material crossing}
\lor
\text{viscous boundary leakage}
\lor
\text{palinstrophy}.
\]

If the packet remains, it can be used as the next compactness center even if the identity of the maximum-vorticity point changes.

This removes another possible DSD bookkeeping artifact.

---

## 7. Correction B: weak-L3 is not the automatic bounded-Z tail

Even if

\[
V\in L^6\cap L^\infty,
\qquad
W\in L^2,
\]

a tail

\[
|V(Y)|\sim |Y|^{-\alpha},
\qquad
1/2<\alpha<1,
\]

is compatible with those global norms and need not belong to weak-L3.

Therefore the phrase

\[
\text{``recurrent core + weak-L3 endpoint tail''}
\]

is valid only after an additional borderline spatial-tail reduction.

---

## 8. H2crit is not terminal for the L3 route

The pointwise spatial-Type-I route uses

\[
R^3\int_{A_R}|\nabla^2V|^2,
\]

but the global-L3 route does not require it.

Define

\[
\mathfrak C_A(R)
=R^{-1}\int_{A_R^*}|V-m_R|^2,
\]

\[
\mathfrak E_1(R)
=R\int_{A_R^*}|\nabla V|^2.
\]

Then

\[
\boxed{
\int_{A_R}|V-m_R|^3
\lesssim
\mathfrak C_A(R)^{3/4}
(\mathfrak E_1(R)+\mathfrak C_A(R))^{3/4}.
}
\]

The mean is controlled by dyadic Campanato/mean telescoping.

Thus a large scale-weighted second derivative may be only a tiny high-frequency packet that obstructs a pointwise estimate while contributing negligibly to the cubic tail.

It must not be treated as a universal final obstruction.

---

## 9. Simplification on the bounded-Z branch

On an annulus, Poincare gives

\[
\mathfrak C_A(R)
\lesssim
\mathfrak E_1(R).
\]

Consequently the mean-free cubic shell satisfies schematically

\[
\boxed{
\int_{A_R}|V-m_R|^3
\lesssim
\mathfrak E_1(R)^{3/2}.
}
\]

The dyadic mean is a one-sided convolution of `E1^(1/2)` with the summable kernel `2^-k`, so discrete Young's inequality gives the corresponding global estimate

\[
\boxed{
\|V\|_{L^3(|Y|>R_0)}^3
\lesssim
\sum_k
\mathfrak E_1(R_k)^{3/2}
}
\]

up to fixed core/enlargement constants.

Therefore a non-L3 bounded-Z recurrent state necessarily requires

\[
\boxed{
\sum_k
\left(
R_k\int_{A_{R_k}}|\nabla V|^2
\right)^{3/2}
=\infty.
}
\]

This is the most useful current tail characterization for the L3 route.

---

## 10. Weighted enstrophy interpretation

Let

\[
e_k=\int_{A_{R_k}}|W|^2.
\]

Up to local/far strain equivalence constants,

\[
\mathfrak E_1(R_k)\sim R_ke_k.
\]

Thus the required non-L3 tail is a nonsummable stack of **critical radial derivative weights**.

If

\[
\sum_kR_ke_k<\infty,
\]

then eventually `R_ke_k<1` and

\[
\sum_k(R_ke_k)^{3/2}<\infty,
\]

so the velocity tail is L3.

Hence every non-L3 survivor also requires divergence of the first radial enstrophy moment, schematically

\[
\boxed{
\int |Y|\,|W(Y)|^2dY=\infty.
}
\]

This identifies the exact weighted quantity that historical shell recycling must sustain.

---

## 11. Current honest alternatives

The proof tree is no longer represented honestly by one terminal label.

A safer current organization is

\[
\boxed{
\begin{aligned}
\text{hypothetical blow-up}
\Longrightarrow{}&
\text{relative-Campanato/Morrey ancient corridor}
\\
&\lor
\text{Campanato / pressure / material-turnover escalation}
\\
&\lor
\text{projective / derivative residual exits}.
\end{aligned}
}
\]

Inside the stronger bounded-Z recurrent ancient corridor:

\[
\boxed{
\text{L3 recurrent state}
\quad\lor\quad
\sum_k\mathfrak E_1(R_k)^{3/2}=\infty.
}
\]

The first is the desired Liouville-class endpoint. The second is the exact amplitude-sensitive historical-tail frontier.

---

## 12. Next theorem target

The highest-value remaining calculation is now

\[
\boxed{
\sum_k\mathfrak E_1(R_k)^{3/2}=\infty
\Longrightarrow
\text{historical replenishment / packet genealogy}
\Longrightarrow
H/T/\text{fixed stage cost},
}
\]

**without** assuming a fixed positive cubic occupancy on each shell.

This is the amplitude-sensitive extension missing from the 2026-08-23 historical-shell argument.

If this extension succeeds, the bounded-Z no-H/T recurrent state enters global L3 and the standard ancient Liouville route becomes available.

The parallel remaining audit is to determine whether the broader Morrey ancient class can be reduced to bounded-Z or treated by a local Type-I Liouville theorem.

Status: **THE ANTI-PROOF AUDIT DID FIND REAL OVER-COMPRESSIONS, BUT IT ALSO PRODUCED REPAIRS: LOCAL ANCIENT COMPACTNESS SURVIVES GLOBAL-Z ESCAPE ON A MORREY CORRIDOR; FINITE ENERGY CONVERTS ALL-SCALE RELATIVE CAMPANATO TO ABSOLUTE MORREY; DRIFT AND CORE TRACKING HAVE EXACT RELATIVE LEDGERS; AND H2CRIT IS NOT NEEDED FOR THE L3 ROUTE. THE SHARPEST CURRENT BOUNDED-Z OBSTRUCTION IS THE NONSUMMABLE DYADIC CRITICAL-H1 STACK. GLOBAL REGULARITY REMAINS UNPROVED.**