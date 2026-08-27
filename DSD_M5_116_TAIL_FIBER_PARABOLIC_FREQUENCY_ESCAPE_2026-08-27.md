# DSD M5-116 — Tail-Fiber Parabolic Frequency Escape

Date: 2026-08-27

Status: **W1-CONDITIONAL FIBER SCALE AUDIT / ANY NONTRIVIAL SAME-TAIL FIBER DIFFERENCE VANISHES ON EVERY FIXED PHYSICAL FREQUENCY WINDOW AS THE TERMINAL TIME IS APPROACHED / ITS SURVIVING CRITICAL CONTENT MUST ESCAPE TO FREQUENCIES OF ORDER (T*-t)^-1/2 OR HIGHER / THIS MATCHES KNOWN NECESSARY ACTIVE-SCALE BEHAVIOR FOR HYPOTHETICAL NAVIER-STOKES SEPARATION BUT IS NOT A CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Same-tail fiber difference

From M5-115, for two same-tail W1 trajectories define

\[
Z(s)=V(s)-W(s).
\]

The difference belongs uniformly to

\[
L^2\cap L^3.
\]

Its physical inverse-Leray realization is

\[
\boxed{
z(x,t)
=\tau^{-1/2}Z\left(\frac{x-x_*}{\sqrt\tau},s\right),
\qquad
\tau=T_*-t=e^{-s}.
}
\]

---

## 2. Exact Fourier scaling

With the standard Fourier convention, parabolic scaling gives

\[
\boxed{
\widehat z(\xi,t)
=\tau\,e^{-ix_*\cdot\xi}
\widehat Z(\sqrt\tau\,\xi,s).
}
\]

The phase from `x_*` is irrelevant to Fourier energy.

For a fixed physical cutoff `K>0`,

\[
\begin{aligned}
\|P_{\le K}z(t)\|_2^2
&=
\tau^2
\int_{|\xi|\le K}
|\widehat Z(\sqrt\tau\xi,s)|^2d\xi\\
&=
\tau^{1/2}
\int_{|\eta|\le K\sqrt\tau}
|\widehat Z(\eta,s)|^2d\eta.
\end{aligned}
\]

Meanwhile

\[
\boxed{
\|z(t)\|_2^2
=\tau^{1/2}\|Z(s)\|_2^2.
}
\]

Thus the relative low-frequency fraction is exactly

\[
\boxed{
\frac{\|P_{\le K}z(t)\|_2^2}{\|z(t)\|_2^2}
=
\frac{
\int_{|\eta|\le K\sqrt\tau}|\widehat Z(\eta,s)|^2d\eta
}{\|Z(s)\|_2^2}
}
\]

whenever the denominator is nonzero.

---

## 3. Uniform low-frequency evacuation on a compact separated fiber segment

The same-tail quotient construction gives a precompact family of fiber differences in `L2` on every compact pair-orbit closure for which the two states remain separated.

Let `K_Z` be such a compact set of normalized differences.

Compactness in `L2` implies uniform absolute continuity of Fourier mass near the origin:

\[
\boxed{
\sup_{Z\in K_Z}
\int_{|\eta|\le r}|\widehat Z(\eta)|^2d\eta
\longrightarrow0
\qquad(r\downarrow0).
}
\]

If in addition the selected robust pair segment satisfies

\[
\|Z\|_2\ge z_*>0,
\]

then for every fixed physical `K`,

\[
\boxed{
\sup
\frac{\|P_{\le K}z(t)\|_2}{\|z(t)\|_2}
\longrightarrow0
\qquad(t\uparrow T_*).
}
\]

Thus no fixed physical Fourier band can carry a positive fraction of a persistent fiber difference.

---

## 4. Natural active frequency

To observe a fixed normalized frequency `|eta|~1`, the physical frequency must satisfy

\[
\sqrt\tau|\xi|\sim1.
\]

Hence

\[
\boxed{
|\xi|\sim\tau^{-1/2}=(T_*-t)^{-1/2}.
}
\]

This is the parabolic terminal frequency.

Therefore a nontrivial tail fiber can survive only by concentrating its error at the same shrinking physical scale as the singular core.

---

## 5. Spatial version

The same conclusion holds for fixed physical spatial resolution.

A normalized core of radius `O(1)` occupies physical radius

\[
\boxed{r_{phys}\sim\sqrt\tau.}
\]

Since same-tail differences are strong `L2 cap L3` in normalized variables and have no critical far-tail residue, their nontrivial content is localized to the shrinking terminal core rather than to fixed macroscopic annuli.

Thus the fiber is a **core-only critical separation channel** above a common passive tail.

---

## 6. Relation to current separation literature

Bradshaw, `Remarks on the separation of Navier-Stokes flows`, Nonlinearity 37 (2024) 095023, proves necessary active-scale properties for the error of hypothetical non-unique Navier-Stokes flows; in particular, some scales must remain comparable to the full error as flows separate, and scale activation propagates as decorrelation develops.

The present W1 fiber calculation is consistent with that general picture but sharper in one respect because the self-similar terminal geometry fixes the active scale explicitly:

\[
\boxed{k_{active}\asymp(T_*-t)^{-1/2}.}
\]

This consistency is a stress test, not a closure theorem.

---

## 7. DSD four-chain audit

### Formation

A nontrivial separated fiber pair is fixed before the Fourier scale statement is made.

### Axis

Physical frequency and normalized Leray frequency are related by the exact parabolic scaling and are not identified directly.

### Static aggregation

Low-frequency energy is compared with the total error only on a segment carrying a positive normalized L2 separation floor.

### Dynamics

The escape `K sqrt(tau)->0` comes from the terminal scaling; no backward-uniqueness claim is inserted.

### RED firewall

High-frequency escape is a necessary survival mechanism, not a contradiction.

It may be exactly how a hypothetical large-critical nonunique/separated fiber survives while having zero terminal L2 difference.

---

## 8. Updated fiber frontier

A noninjective canonical-tail factor is now forced into the narrow class

\[
\boxed{
\text{compact recurrent strong-L3 fiber difference}
+
\text{zero cubic residue}
+
\text{terminal L2 collapse}
+
\text{parabolic frequency escape }k\sim\tau^{-1/2}.
}
\]

Any injectivity proof must rule out this scale-escaping relative solution, not merely show that fixed physical scales agree at the terminal time.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
