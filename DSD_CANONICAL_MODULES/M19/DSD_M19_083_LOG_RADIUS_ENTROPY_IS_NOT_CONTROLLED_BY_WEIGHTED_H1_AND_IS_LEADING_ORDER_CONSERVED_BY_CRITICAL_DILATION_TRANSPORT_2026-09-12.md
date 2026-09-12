# DSD M19-083 — Log-radius entropy is not controlled by weighted H1 and is leading-order conserved by critical dilation transport

Date: 2026-09-12

Status: **LOG-DIFFUSE ESCAPE AUDIT / A SUPERPOSITION OF MANY DISJOINT NORMALIZED ESCAPING ANNULAR PACKETS HAS UNIT WEIGHTED L2 MASS, UNIFORMLY SMALL WEIGHTED GRADIENT COST, AND DYADIC SHELL ENTROPY GROWING LIKE LOG N / THEREFORE THE CURRENT A2 ENERGY AND DIFFUSION LEDGERS DO NOT CONTROL LOG-RADIUS ENTROPY OR VARIANCE / AT THE LEADING CRITICAL TAIL LEVEL q=LOG r-THETA/2 IS A CHARACTERISTIC INVARIANT, SO PURE DILATION TRANSPORT DOES NOT MIX OR COMPRESS THE q-DISTRIBUTION / REMOTE VISCOUS/NONLINEAR CORRECTIONS ARE R^-2-SUPPRESSED / THUS THE LOG-DIFFUSE BRANCH CANNOT BE COLLAPSED TO ONE ANNULAR PACKET BY A BARE ENTROPY ARGUMENT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Target from M19-082

M19-082 left the genuine diffuse branch

\[
\sup_jm_{j,n}\to0,
\]

where \(m_{j,n}\) is the normalized weighted mass in the j-th dyadic shell.

A natural idea is to control the Shannon entropy

\[
\boxed{
H(m):=-\sum_jm_j\log m_j
}
\]

or a first/second log-radius moment.

If \(H\) were uniformly bounded, then the mass could not spread over arbitrarily many comparable shells.

M19-083 shows that the currently certified weighted energy and diffusion bounds do not provide such a bound.

---

## 2. One normalized escaping packet

From M19-081, choose a fixed nonzero divergence-free annular profile

\[
F\in C_c^\infty(\{1<|z|<2\})
\]

and define at radius \(R\)

\[
W_R(y)=c_RR^{-1}F(y/R),
\qquad
c_R=R^{(a-1)/2}.
\]

After fixed normalization of \(F\),

\[
\boxed{
\|W_R\|_{L^2(w)}^2\asymp1,
\qquad
\|\nabla W_R\|_{L^2(w)}^2\asymp R^{-2}.
}
\]

---

## 3. Many-packet superposition

Choose radii

\[
R_{1,N}\ll R_{2,N}\ll\cdots\ll R_{N,N}
\]

so that the corresponding annular supports are pairwise disjoint.

Define

\[
\boxed{
W_N
:=
\frac1{\sqrt N}
\sum_{k=1}^N W_{R_{k,N}}.
}
\]

Because the supports are disjoint,

\[
\|W_N\|_{L^2(w)}^2
\asymp
\frac1N\sum_{k=1}^N1
=1.
\]

Likewise,

\[
\boxed{
\|\nabla W_N\|_{L^2(w)}^2
\asymp
\frac1N\sum_{k=1}^NR_{k,N}^{-2}.
}
\]

If all radii tend to infinity, this gradient cost can be made arbitrarily small.

Thus the diffuse sequence can have **less**, not more, weighted diffusion cost than a fixed packet.

---

## 4. Shell entropy diverges

Take each packet to occupy a distinct dyadic shell.

Then the normalized shell masses satisfy approximately

\[
\boxed{
m_{j_k,N}\approx\frac1N,
\qquad k=1,\ldots,N.}
\]

Hence

\[
\begin{aligned}
H_N
&=-\sum_{k=1}^N\frac1N\log\frac1N\\
&=\log N.
\end{aligned}
\]

Therefore

\[
\boxed{H_N\to\infty.}
\]

At the same time,

\[
\|W_N\|_{L^2(w)}\asymp1,
\qquad
\|\nabla W_N\|_{L^2(w)}\to0.
\]

So no inequality of the form

\[
H(m)
\le C(E_w,G_w)
\]

can follow from the current weighted L2/H1 control alone.

---

## 5. Log-radius variance is also uncontrolled

Let the shell coordinate be

\[
q_k\sim\log R_{k,N}.
\]

The normalized discrete mean is

\[
\bar q_N=\sum_km_kq_k.
\]

By choosing the radii increasingly separated, the centered variance

\[
\boxed{
\operatorname{Var}_q
:=
\sum_km_k(q_k-\bar q_N)^2
}
\]

can be made arbitrarily large while the same weighted energy/gradient estimates remain valid.

Thus neither the first absolute moment relative to a chosen center nor the second centered moment is controlled by the current norms.

---

## 6. Leading critical transport preserves the q-label

The passive critical tail uses

\[
\boxed{
q=\log r-\theta/2.
}
\]

Along the outward similarity characteristic

\[
R(\tau)=R_0e^{\tau/2},
\]

we have

\[
\frac{d}{d\tau}
\left(
\log R(\tau)-\frac{\theta_0+\tau}{2}
\right)=0.
\]

Hence q is exactly a characteristic invariant of the leading similarity drift.

Therefore the leading transport equation carries a q-profile without mixing its q-labels.

For a formal center datum

\[
B(q,\omega),
\]

a broad or multi-packet q-distribution remains broad under the pure dilation conveyor.

Thus

\[
\boxed{
\text{critical dilation transport does not create an entropy-dissipation mechanism in q.}
}
\]

---

## 7. Remote PDE corrections are too small to give an immediate uniform entropy collapse

M5-563 and M19-069 show that along a passive spectator characteristic the exact corrections appear with coefficient

\[
R_0^{-2}e^{-\tau}.
\]

Their total future deformation budget is finite:

\[
\int_0^\infty R_0^{-2}e^{-\tau}d\tau
=R_0^{-2}.
\]

Consequently an arbitrarily remote broad q-profile experiences only an \(O(R_0^{-2})\) total scattering deformation in the controlled corridor.

There is no certified mechanism here capable of reducing an arbitrarily large log-shell entropy \(\log N\) to order one uniformly in \(R_0\).

---

## 8. Entropy production would require a new inter-q coupling estimate

To collapse the diffuse branch one would need an equation-level estimate that couples distinct q-shells strongly enough to penalize spread, for example a positive term schematically like

\[
\int |\partial_q B|^2dq
\]

with a coefficient that remains order one at large radius.

But in the critical tail reduction, q-derivatives enter through spatial derivatives accompanied by inverse powers of r.

Hence their dynamical effect is scale-suppressed in the remote spectator limit.

The present equations do not supply an order-one q-diffusion.

---

## 9. Relation to quasi-periodic scattering

A quasiperiodic or almost-periodic datum can distribute activity over many q-phases without concentrating into one packet.

Since scattering is translation-equivariant and near identity, such a broad q-history is structurally compatible with the current formal tail center.

Thus the diffuse branch is not an artificial concentration-compactness artifact; it matches the very factor dynamics that remains to be excluded.

---

## 10. Certified conclusion

\[
\boxed{
\text{weighted }L^2/H^1
+\text{critical dilation transport}
\not\Rightarrow
\text{bounded log-radius entropy or variance}.
}

Therefore

\[
\boxed{
\mathcal C_{log\text{-}diffuse}
\text{ remains a genuine branch.}
}
\]

Any closure must use a stronger interior realization constraint, not a bare tail entropy inequality.

---

## 11. Revised branch picture

The center/factor frontier now has two genuinely tail-related realizability channels:

\[
\boxed{
\mathcal C_{annular}^{critical}
\lor
\mathcal C_{log\text{-}diffuse}.
}

The first is a localized q-packet realization problem.

The second is a broad-history realization problem.

Both are compatible with leading critical transport and near-identity scattering.

---

## 12. Next calculation

M19-084 should move back to the **finite spectator boundary** and ask whether a broad q-history necessarily requires a broad temporal frequency spectrum of the boundary trace.

If the recurrent interior cocycle has parabolic time-analyticity, one can test whether uniform analytic-strip bounds impose an exponential temporal Fourier envelope strong enough to restrict the log-diffuse branch.

The key firewall is that analytic quasiperiodic functions can still have infinitely many frequencies, so analyticity alone may give decay of frequency amplitudes without forcing periodicity.
