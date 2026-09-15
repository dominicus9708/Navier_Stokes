# DSD M19-274 — Zero original momentum does not kill the terminal force without uniform stress tightness; the defect is a noncommuting-limit phenomenon

Date: 2026-09-16  
Canonical ID: **M19-274**  
Status: **ACTIVE ORIGINAL-DATA INHERITANCE AUDIT / ZERO TOTAL MOMENTUM CERTIFIED FOR RAPIDLY DECAYING DIVERGENCE-FREE DATA / TERMINAL FORCE NOT INHERITED / UNIFORM STRESS-TIGHTNESS GATE ISOLATED / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-272--273 identify the stationary terminal point-force coefficient \(\kappa\) as a signed critical stress-flux mode.

A natural objection is that the original whole-space Clay-type data are rapidly decaying and unforced. In particular their total momentum is finite and, for divergence-free rapidly decaying data, actually vanishes.

The present module audits whether that original zero-momentum fact forces

\[
\kappa=0.
\]

It does not without a uniform tightness theorem. The missing issue is the order of the blow-up and far-field limits.

---

## 2. Rapid decay plus incompressibility gives zero total momentum

Let \(u\) be a sufficiently rapidly decaying divergence-free field on \(\mathbb R^3\).

For each component,

\[
\partial_j(x_i u_j)
=
\delta_{ij}u_j+x_i\partial_j u_j
=u_i.
\]

Integrating and using the vanishing boundary term at infinity gives

\[
\boxed{
\int_{\mathbb R^3}u_i(x)dx=0.
}
\]

Thus

\[
\boxed{
\int_{\mathbb R^3}u(x)dx=0.
}
\]

For a classical rapidly decaying unforced solution this identity persists as long as the required spatial decay/integrability is available.

This is stronger than merely saying that total momentum is conserved: the conserved value is zero.

---

## 3. Each finite approximant has zero far-field stress flux

For a smooth rapidly decaying unforced solution,

\[
\partial_tu=\nabla\cdot\mathbb T.
\]

At any fixed regular physical time, rapid decay gives

\[
\boxed{
\lim_{R\to\infty}
\int_{S_R}\mathbb Tn\,dS
=0.
}
\]

The same is true for every finite blow-up/rescaled approximant before taking the noncompact limit: at sufficiently large radius one eventually sees the original decaying outer field rather than the critical inner asymptotic corridor.

Thus, if \(F_j(R)\) denotes the rescaled momentum-stress flux through the radius-\(R\) sphere of approximant \(j\), then

\[
\boxed{
\forall j<\infty,
\qquad
\lim_{R\to\infty}F_j(R)=0.
}
\]

---

## 4. The terminal point force comes from reversing the limits

Compactness produces a limiting critical field only on each fixed bounded rescaled region/annulus.

For every fixed \(R\),

\[
F_j(R)\to F_*(R)
\qquad(j\to\infty).
\]

On the stationary terminal branch,

\[
F_*(R)=\kappa
\]

for all radii in the point-force channel.

Therefore

\[
\boxed{
\lim_{R\to\infty}
\lim_{j\to\infty}F_j(R)
=
\kappa.
}
\]

But for every finite \(j\),

\[
\lim_{R\to\infty}F_j(R)=0,
\]

so

\[
\boxed{
\lim_{j\to\infty}
\lim_{R\to\infty}F_j(R)
=0.
}
\]

Hence a nonzero terminal force is precisely compatible with

\[
\boxed{
\lim_{R\to\infty}\lim_{j\to\infty}F_j(R)
\neq
\lim_{j\to\infty}\lim_{R\to\infty}F_j(R).
}
\]

There is no logical contradiction unless the two limits can be interchanged.

---

## 5. Exact uniform stress-tightness condition

A sufficient interchange condition is

\[
\boxed{
\mathcal T_{stress}^{tight}:
\lim_{R\to\infty}
\sup_{j\ge j_0}
|F_j(R)|
=0.
}
\]

Under this condition, for every \(\varepsilon>0\) choose \(R\) so large that

\[
\sup_j|F_j(R)|<\varepsilon.
\]

Then pass \(j\to\infty\):

\[
|F_*(R)|\le\varepsilon.
\]

Since the stationary terminal flux is radius independent,

\[
F_*(R)=\kappa,
\]

and therefore

\[
\boxed{
\mathcal T_{stress}^{tight}
\Longrightarrow
\kappa=0.
}
\]

Thus uniform stress tightness is the precise missing inheritance theorem behind the informal phrase “unforced decaying original data should have no terminal point force.”

---

## 6. Annular absolute-stress version

M19-272 gives a convenient sufficient size condition. Define

\[
\mathfrak S_j(R)
:=
\frac1R
\int_{R<|y|<2R}
|\mathbb T_j(y)|dy.
\]

If

\[
\boxed{
\lim_{R\to\infty}
\sup_j
\mathfrak S_j(R)=0,
}
\]

then coarea plus compact-annulus convergence gives the same conclusion

\[
\boxed{\kappa=0.}
\]

This is stronger than necessary because vector cancellations could make the flux tight even when the absolute stress is critical.

But it makes the scale obstruction explicit.

---

## 7. Why finite kinetic energy does not give uniform stress tightness

The normalized critical tail has

\[
V_j(y)\sim\frac{A}{|y|}
\]

through a radius range that expands with the blow-up scale.

Inside that corridor,

\[
|\mathbb T_j(y)|\sim |y|^{-2}.
\]

Therefore

\[
\frac1R
\int_{R<|y|<2R}|\mathbb T_j|dy
\sim O(1)
\]

uniformly while the critical corridor persists.

For each fixed approximant the corridor eventually ends and the original far-field decay restores zero flux, but the ending radius escapes to infinity as \(j\to\infty\).

This is exactly the mechanism that destroys uniformity in \(j\).

Hence

\[
\boxed{
\text{finite original energy + pointwise far-field decay for every approximant}
\not\Rightarrow
\mathcal T_{stress}^{tight}.
}
\]

---

## 8. Why zero total momentum is not enough

The identity

\[
\int u=0
\]

is a signed global cancellation over the entire physical space.

Under blow-up, regions at fixed original distance move to rescaled distance of order

\[
r_j^{-1}\to\infty.
\]

Thus compensating momentum/stress can escape every fixed rescaled ball while preserving the exact global cancellation of each finite approximant.

Local compactness then sees only one side of the cancellation.

Therefore

\[
\boxed{
\int u=0
\not\Rightarrow
\kappa=0
}
\]

without a tightness statement controlling where the compensating signed stress lives in rescaled variables.

---

## 9. First-hitting centering cannot tune the defect away

Changing a finite spatial center changes the far-field critical expansion only in lower orders. For

\[
|a|<\infty,
\]

one has schematically

\[
\frac1{|x-a|}
=
\frac1{|x|}+O(|x|^{-2}).
\]

Thus a bounded recentering changes the \(r^{-2}\) and faster correction sectors but not the leading \(r^{-1}\) scattering datum or its scale-critical stress-flux coefficient.

Equivalently, a point force may move from \(\delta_0\) to \(\delta_a\), but its vector coefficient is not removed by changing coordinates.

Hence

\[
\boxed{
\text{first-hitting center choice}
\not\Rightarrow
\kappa=0.
}
\]

---

## 10. Galilean gauge is not a free force-cancellation parameter

The retained critical ancient/scattering class fixes a decaying or \(L^6\)-type velocity gauge at spatial infinity.

A nonzero additive constant velocity is not in that decaying class and would dominate the \(1/r\) tail.

Therefore the Galilean normalization used upstream cannot be treated as a freely adjustable constant capable of canceling the stationary point-force mode after the critical class has been fixed.

The force coefficient is a property of the critical stress field, not an arbitrary gauge parameter.

---

## 11. Relation to the historical moment firewalls

M19-056--057 show that angular momentum and every fixed-degree local polynomial momentum moment fail to impose a new leading solvability condition on the critical datum: their first genuine stress information occurs at the same order as the invertible \(r^{-3}\) correction sector.

M19-274 adds a different firewall:

\[
\boxed{
\text{even exact zero global momentum of the original decaying solution}
\not\Rightarrow
\text{uniform stress tightness of the blow-up family}.
}
\]

Thus neither local finite moments nor the global zero-momentum identity currently eliminate \(\kappa\).

---

## 12. Refined stationary force target

M19-273 introduced

\[
\mathcal T_{tail}^{force-cancel}.
\]

The present module sharpens this into the explicit inheritance problem

\[
\boxed{
\mathcal T_{tail}^{force-cancel}
\Leftarrow
\mathcal T_{stress}^{tight}.
}
\]

But the critical hard tail is exactly compatible with failure of \(\mathcal T_{stress}^{tight}\).

Therefore a successful force-cancellation theorem must use either

1. signed angular cancellation stronger than absolute stress decay;
2. a new uniform original-to-blow-up tightness estimate;
3. a defect-measure theorem allowing interchange of the far-field and compactness limits;
4. endpoint stationary rigidity showing that any non-tight zero-force recurrent tail is impossible.

---

## 13. Immediate next target

The stationary branch is now reduced to an explicit two-limit problem.

The next high-value calculation is to test whether any already certified **signed** quantity, rather than an absolute norm, is uniformly tight under the blow-up family.

Candidates must survive the M19-057/M19-058 firewalls; fixed polynomial momentum moments and local helicity do not qualify.

If no such signed tight quantity exists, the stationary route should be frozen at

\[
\boxed{
\mathcal T_{stress}^{tight}
\lor
\mathcal T_{tail}^{zero-force-rigidity}
}
\]

and priority returned to the dynamic non-coboundary lag-defect/index route of M19-271.

Global 3D Navier--Stokes regularity remains unproved.
