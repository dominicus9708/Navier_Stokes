# DSD M5-194C — Carleman Shell-Separation Recovery and Bulk-Tail Priority Audit

Date: 2026-08-29

Parent: `DSD_M5_194B_VORTICITY_CUTOFF_CRITICALITY_AND_RADIAL_COMPONENT_BOTTLENECK_AUDIT_2026-08-29.md`

Status: **POSITIVE LOCALIZATION RECOVERY / M5-194B'S RAW CRITICAL-SCALING VERDICT FOR CUTOFF COMMUTATORS IS CORRECT BUT DOES NOT BY ITSELF BLOCK THE CARLEMAN ROUTE / SPATIALLY LOCALIZED COMMUTATORS CAN BE EXPORTED TO SEPARATED SHELLS AND SUPPRESSED BY WEIGHT RATIOS / THE COMMON RADIAL COMPONENT `Phi_r` CONTROLS BOTH BULK WEIGHTED TRANSPORT AND SHELL DRIFT COMMUTATORS ALGEBRAICALLY, BUT ONLY THE BULK TERM PERSISTS THROUGH THE CARLEMAN REGION / ENDPOINT BULK COERCIVITY IS THEREFORE THE HIGHER-PRIORITY OBSTRUCTION / BACKWARD UNIQUENESS AND GLOBAL REGULARITY REMAIN UNPROVED.**

---

## 1. Reason for this follow-up audit

M5-194B established that for a critical Type-I scale ledger,

\[
|u|\sim r^{-1},\qquad
|\omega|\sim r^{-2},\qquad
|\nabla\omega|\sim r^{-3},
\]

ordinary spatial-cutoff commutators have the same raw scaling as the principal vorticity terms.

That statement remains correct.

However, a Carleman proof does not necessarily need to absorb a cutoff commutator pointwise or scale-by-scale in the bulk. A standard localization architecture can move the commutator to shells where the Carleman weight is quantitatively separated from the target region.

The present audit therefore distinguishes

\[
\boxed{
\text{critical raw scaling}
\quad\text{from}\quad
\text{weighted shell suppressibility}.
}
\]

---

## 2. Literature cross-check: what the Lin--Wang proof actually does

Reference:

Ching-Lung Lin and Jenn-Nan Wang, *Quantitative uniqueness estimates for the generalized non-stationary Stokes system*, Applicable Analysis 101 (2022), 3591--3611, DOI 10.1080/00036811.2020.1747611.

Their spatial Carleman weight has the form

\[
\varphi(r)=e^{\psi(y)},\qquad y=-\log r,
\]

and their construction gives, in the relevant region,

\[
\boxed{
\frac12\beta\le\psi'(y)\le2\beta.
}
\]

In the proof of the three-cylinder estimate they introduce a spatial cutoff which equals zero on a small inner ball, one on an intermediate annulus, and zero again outside a larger radius. The cutoff derivatives therefore live only on an inner shell and an outer shell.

After the Carleman estimates are combined, the localization errors appear as shell integrals rather than as a coefficient that must be absorbed everywhere in the target annulus.

This observation materially changes the interpretation of M5-194B.

---

## 3. General weight-separation inequality

Let

\[
0<r_a<r_b
\]

and assume

\[
\frac12\beta\le\psi'\le2\beta.
\]

Then

\[
\begin{aligned}
\log\frac{\varphi(r_a)}{\varphi(r_b)}
&=
\psi(-\log r_a)-\psi(-\log r_b)\\
&=
\int_{-\log r_b}^{-\log r_a}\psi'(y)\,dy.
\end{aligned}
\]

Therefore

\[
\boxed{
\frac\beta2\log\frac{r_b}{r_a}
\le
\log\frac{\varphi(r_a)}{\varphi(r_b)}
\le
2\beta\log\frac{r_b}{r_a}.
}
\]

Equivalently,

\[
\boxed{
\left(\frac{r_b}{r_a}\right)^{\beta/2}
\le
\frac{\varphi(r_a)}{\varphi(r_b)}
\le
\left(\frac{r_b}{r_a}\right)^{2\beta}.
}
\]

For squared weights,

\[
\boxed{
\left(\frac{r_b}{r_a}\right)^\beta
\le
\frac{\varphi(r_a)^2}{\varphi(r_b)^2}
\le
\left(\frac{r_b}{r_a}\right)^{4\beta}.
}
\]

This is the quantitative mechanism behind shell separation.

---

## 4. Outer shell: exponential suppression in the Carleman parameter

Let `r_*` be a target radius and let the outer cutoff shell lie at

\[
r_{\rm out}>r_*.
\]

Because the weight increases as `r` decreases,

\[
\frac{\varphi(r_{\rm out})^2}
{\varphi(r_*)^2}
\le
\left(\frac{r_*}{r_{\rm out}}\right)^\beta.
\]

Thus, if the shell is separated from the target by any fixed multiplicative factor

\[
\frac{r_{\rm out}}{r_*}\ge1+\delta>1,
\]

then

\[
\boxed{
\frac{\varphi(r_{\rm out})^2}
{\varphi(r_*)^2}
\le
\exp\!\left[-\beta\log(1+\delta)\right].
}
\]

This gives exponential suppression as `beta -> infinity`.

Consequently, an outer-shell commutator can remain **critical in raw PDE scaling** and nevertheless be **small in the normalized Carleman inequality**.

This is why M5-194B's scale-criticality firewall does not close the localization route.

---

## 5. Inner shell: weight amplification requires a vanishing input

If instead

\[
r_{\rm in}<r_*,
\]

then

\[
\frac{\varphi(r_{\rm in})^2}
{\varphi(r_*)^2}
\le
\left(\frac{r_*}{r_{\rm in}}\right)^{4\beta},
\]

which grows rapidly as `r_in -> 0` for fixed `beta`.

In a strong unique-continuation proof this is compensated by an independent vanishing hypothesis such as

\[
\int_{|x|<r}|u|^2\,dxdt=O(r^N)
\qquad\text{for every }N.
\]

For each fixed `beta`, one can choose a sufficiently high vanishing order and then send the inner cutoff radius to zero.

Therefore

\[
\boxed{
\text{inner-shell suppression is not supplied by the Carleman weight alone.}
}
\]

It needs a separate vanishing datum.

For the present Type-I/backward-uniqueness route, the corresponding datum must be identified from the actual backward-uniqueness geometry; one cannot simply import spatial infinite-order vanishing from a strong unique-continuation theorem.

---

## 6. Reassessment of the `Phi_r` bottleneck

M5-194A gave the bulk weighted-transport residual for a radial phase:

\[
\boxed{
B_T\cdot\nabla\Psi
=-\beta r^{-2}\Phi_r.
}
\]

M5-194B gave the radial-cutoff transport commutator:

\[
\boxed{
B_T\cdot\nabla\chi
\propto
\Phi_r.
}
\]

Algebraically, both are governed by the same radial tail component.

But their support is fundamentally different.

### Bulk phase term

The weighted transport potential

\[
\beta r^{-2}\Phi_r |W|^2
\]

exists throughout the Carleman bulk wherever the common tail and weighted unknown coexist.

It cannot be removed merely by moving a cutoff shell.

### Shell drift term

The cutoff term

\[
(B_T\cdot\nabla\chi)\omega
\]

exists only where `nabla chi` is nonzero.

If that support is placed on the lower-weight outer side, it can acquire the exponential shell-separation factor derived above.

Hence

\[
\boxed{
\text{same coefficient }\Phi_r
\not\Rightarrow
\text{same obstruction severity.}
}
\]

The **bulk weighted transport term is the higher-priority endpoint obstruction.**

---

## 7. Diffusive cutoff commutators are similarly shell-localized

The terms

\[
-2\nabla\chi\cdot\nabla\omega
-(\Delta\chi)\omega
\]

remain critical in raw scaling, as M5-194B showed.

But they also vanish outside the transition shell.

Therefore they are candidates for the same shell-separation treatment.

This does not automatically prove their control: one still needs sufficient local norms of `omega` and `nabla omega` on the shell. It does show that their critical scaling is **not by itself a fatal endpoint obstruction**.

The relevant question is weighted leakage into the shell, not merely pointwise homogeneity.

---

## 8. Logarithmically slow cutoff branch

M5-194B suggested considering a cutoff that changes over log-radius width `L`.

If

\[
\chi=\eta\!\left(\frac{y-Y}{L}\right),
\qquad y=-\log r,
\]

then in three dimensions

\[
|\nabla\chi|\lesssim\frac1{Lr},
\]

and

\[
|\Delta\chi|
\lesssim
\left(\frac1L+\frac1{L^2}\right)r^{-2}.
\]

Thus the raw diffusive commutator indeed acquires `1/L`-type smallness.

However, across the same transition region,

\[
\Delta\psi\sim\beta L,
\]

so the Carleman weight changes by an exponential factor of order

\[
e^{O(\beta L)}.
\]

Therefore increasing `L` is not a free perturbative parameter in a weighted estimate.

Because ordinary shell separation already supplies an exponential weight ratio on the favorable side, the slow-cutoff branch is now **secondary**, not the main route.

---

## 9. DSD verdict

### RECOVERED

The following mechanism survives M5-194B:

\[
\boxed{
\text{critical cutoff commutator}
\ +\ 
\text{support localization}
\ +\ 
\text{Carleman weight separation}
\ \Longrightarrow\ 
\text{possible shell suppression}.
}
\]

In particular, raw scale-criticality alone is insufficient to reject the spatial-cutoff architecture.

### STILL BLOCKED / OPEN

The more serious endpoint problems remain:

1. the strict subcritical coefficient gain `r^epsilon` used in the Lin--Wang curvature absorption disappears at `epsilon=0`;
2. an order-one radial common-tail component recreates the bulk signed potential `beta r^-2 Phi_r` under a radial weight;
3. the common-tail strain remains a signed critical bulk channel;
4. a backward-uniqueness proof needs the correct final-time/temporal vanishing input and cannot simply borrow the inner-shell infinite-order spatial vanishing used by strong unique continuation;
5. no endpoint Carleman coercivity estimate controlling these bulk terms has yet been established.

---

## 10. Reprioritized next target

The next audit should stop treating the cutoff commutator as the primary endpoint and instead isolate the **bulk critical operator after conjugation**.

Write schematically

\[
\mathcal L_T\omega
=
(\partial_t-\Delta)\omega
+B_T\cdot\nabla\omega
-(\nabla B_T)\omega
+\text{remainder}.
\]

After conjugation by a candidate endpoint weight, compute the symmetric and skew pieces of the `B_T` transport and strain together and ask whether any structural cancellation survives at the **bulk quadratic-form level**.

The decisive object is no longer the shell source but the combined critical form

\[
\boxed{
\beta r^{-2}\Phi_r |W|^2
\;-
W^T S_{B_T}W
}
\]

(up to sign convention and additional conjugated diffusion terms).

If this combined form has no universal lower bound, the scalar endpoint route must rely on additional PDE-specific canonical-tail rigidity or be replaced by a matrix/symmetrizer architecture.
