# M17-485 — Zero-tube flux collapse has a representation-safe level-width dichotomy and a genuine D4 barrier

**Date:** 2026-09-10  
**Status:** ACTIVE ZERO-TUBE LEVEL-WIDTH AUDIT / LOWER-DERIVATIVE DESCENT / SECOND-JET BARRIER

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M17-470 showed that a regular zero-level current can be thickened by coarea only when a record-uniform coefficient tube survives. M17-483 then gave a nodal-safe flux-variation estimate, while M17-484 isolated the scale-invariant coefficient-shape parameter
\[
\Lambda_{\kappa,\delta}
:=
\delta\,
\operatorname*{ess\,sup}_{|\kappa|<\delta}
\left|
\frac{\Delta\kappa}{|\nabla\kappa|^2}
\right|.
\]

The present module asks a narrower DSD-audit question:

> Before escalating the M17-484 second-coefficient-jet exit to \(D^4\Omega\), can loss of zero-tube level flux be forced to pay an already-certified lower-order resource?

The answer splits sharply by coefficient-level width.

- If a nontrivial fraction of the normalized coefficient slab survives, coarea produces a first-coefficient-jet charge and, under an upper gradient ceiling, a raw-H2/enstrophy corridor.
- If the level width collapses, the M17-483 estimate forces either palinstrophy concentration or growth of \(\Lambda_{\kappa,\delta}\) at least like the inverse relative level width.
- A direct integrated flux-loss identity gives a representation-safe trichotomy between the existing weighted first-coefficient-jet charge, palinstrophy, and a weighted second-coefficient-jet charge.
- The weighted second-jet branch is genuinely one derivative above the M17-445 ledger; there is no purely coarea/geometric descent that removes it.

Thus the M17-484 \(D^4\) barrier is not merely an artifact of taking another Laplacian pointwise.

## 2. Regular weighted level flux

On exact CE-H,
\[
\Delta\Omega=\kappa\Omega,
\qquad
\rho:=|\Omega|,
\qquad
g:=|\nabla\kappa|.
\]

For a regular coefficient level
\[
\Sigma_s:=\{x:\kappa(x)=s\},
\]
define the amplitude-weighted level flux
\[
\boxed{
F(s):=
\int_{\Sigma_s}\rho^2 g\,dS.
}
\]

At the zero level,
\[
J:=F(0).
\]

For a one-sided slab
\[
T_\ell:=\{0<\kappa<\ell\},
\qquad 0<\ell\le\delta,
\]
coarea gives the exact weighted first-coefficient-jet charge
\[
\boxed{
G_\ell
:=
\int_{T_\ell}\rho^2g^2\,dx
=
\int_0^\ell F(s)\,ds.
}
\]

M17-445 identifies the spacetime version of this resource with the \(R^{-5}\) ancestry class under a compact CE-H coefficient ceiling.

## 3. Exact flux derivative inherited from M17-483

M17-483 gives
\[
\boxed{
F'(s)
=
\int_{\Sigma_s}
\left[
2\rho\,\partial_n\rho
+
\rho^2\frac{\Delta\kappa}{g}
\right]dS.
}
\]

Define
\[
N(s):=
\int_{\Sigma_s}
\frac{|\partial_n\rho|^2}{g}\,dS.
\]

Then
\[
|F'(s)|
\le
2F(s)^{1/2}N(s)^{1/2}
+
L_\ell F(s),
\]
where
\[
L_\ell
:=
\operatorname*{ess\,sup}_{T_\ell}
\left|
\frac{\Delta\kappa}{g^2}
\right|.
\]

Writing \(Z=F^{1/2}\), the M17-483 square-root inequality gives
\[
\boxed{
Z(\ell)
\ge
 e^{-L_\ell\ell/2}Z(0)
-
\ell^{1/2}P_\ell^{1/2},
}
\]
with
\[
P_\ell
:=
\int_{T_\ell}|\nabla\Omega|^2dx,
\]
because
\[
\int_0^\ell N(s)ds
\le P_\ell.
\]

No division by \(\rho\) is required.

## 4. First fractional flux-loss width

Fix
\[
0<\theta<1.
\]
Suppose \(\ell\) is a first positive level width for which
\[
F(\ell)=\theta J,
\]
while
\[
F(s)>\theta J
\qquad(0\le s<\ell).
\]

Then coarea immediately gives
\[
\boxed{
G_\ell
\ge
\theta J\ell.
}
\]

This is already a lower-order payer: a nontrivial level interval cannot lose a fixed fraction of the zero flux without carrying weighted first-coefficient-jet mass before the loss occurs.

However, if \(\ell\to0\), this lower bound can vanish. Therefore the coefficient-level width itself must be audited rather than silently treated as fixed.

## 5. Representation-safe dimensionless collapse variables

Let \(\delta\) be the retained normalized zero-slab width with \(0<\ell\le\delta\). Define
\[
\boxed{
\eta_\ell:=\frac{\ell}{\delta},
\qquad
\Pi_P:=\frac{\ell P_\ell}{J},
\qquad
\Pi_\kappa:=\ell L_\ell.
}
\]

All three quantities are invariant under the certified Navier--Stokes record scaling.

Indeed,
\[
\kappa_R=R^2\kappa,
\quad
\ell_R=R^2\ell,
\quad
\delta_R=R^2\delta,
\]
while spatial palinstrophy scales as \(R^3\) and the level flux scales as \(R^5\), so
\[
\frac{\ell_RP_{\ell,R}}{J_R}
=
\frac{R^2\ell\,R^3P_\ell}{R^5J}
=
\Pi_P.
\]
Also
\[
L_{\ell,R}=R^{-2}L_\ell,
\]
so
\[
\ell_RL_{\ell,R}=\ell L_\ell.
\]

Thus the following width audit does not depend on which canonical record representation is used.

## 6. Quantitative level-width collapse theorem

From Section 3 and
\[
F(\ell)=\theta J,
\]
we obtain
\[
\sqrt{\theta J}
\ge
 e^{-L_\ell\ell/2}\sqrt J
-
\ell^{1/2}P_\ell^{1/2}.
\]
After division by \(\sqrt J\),
\[
\boxed{
 e^{-\Pi_\kappa/2}
\le
\sqrt\theta+\sqrt{\Pi_P}.
}
\]

Fix any
\[
0<\varepsilon<1-\sqrt\theta.
\]
Then either
\[
\boxed{
\Pi_P>\varepsilon^2,
}
\]
which means
\[
\boxed{
P_\ell
>
\varepsilon^2\frac{J}{\ell},
}
\]
or else
\[
\Pi_P\le\varepsilon^2
\]
and therefore
\[
\boxed{
\Pi_\kappa
\ge
c_{\theta,\varepsilon}
:=-2\log(\sqrt\theta+\varepsilon)>0.
}
\]

Because the full slab parameter satisfies
\[
\Lambda_{\kappa,\delta}
\ge
\delta L_\ell,
\]
the second alternative yields
\[
\boxed{
\Lambda_{\kappa,\delta}
\ge
c_{\theta,\varepsilon}
\frac{\delta}{\ell}
=
\frac{c_{\theta,\varepsilon}}{\eta_\ell}.
}
\]

Hence
\[
\boxed{
\eta_\ell\to0
\quad\Longrightarrow\quad
P_\ell\gtrsim\frac{J}{\ell}
\quad\lor\quad
\Lambda_{\kappa,\delta}\gtrsim\frac{\delta}{\ell}.
}
\]

This is the desired quantitative refinement of M17-484: a microscopic coefficient-level collapse cannot remain simultaneously palinstrophy-compact and coefficient-shape-compact.

## 7. Macroscopic level-width branch

Suppose instead that the first fractional-loss width obeys
\[
\boxed{
\ell\ge\eta_*\delta
}
\]
for some record-uniform \(\eta_*>0\).

Then
\[
G_\ell
\ge
\theta\eta_*J\delta.
\]

If one also has a normalized upper coefficient-gradient ceiling
\[
g\le G_*^{\rm max}
\]
on \(T_\ell\), then the raw-H2 content of the slab satisfies
\[
H_\ell
:=
\int_{T_\ell}\kappa^2\rho^2dx
=
\int_0^\ell
s^2
\left(
\int_{\Sigma_s}\frac{\rho^2}{g}dS
\right)ds.
\]
Since
\[
\frac1g\ge\frac{g}{(G_*^{\rm max})^2},
\]
we obtain
\[
H_\ell
\ge
\frac1{(G_*^{\rm max})^2}
\int_0^\ell s^2F(s)ds
\ge
\frac{\theta J}{(G_*^{\rm max})^2}
\int_0^\ell s^2ds.
\]
Therefore
\[
\boxed{
H_\ell
\ge
\frac{\theta}{3}
\frac{J\ell^3}{(G_*^{\rm max})^2}.
}
\]

Because \(|\kappa|\le\ell\) on \(T_\ell\),
\[
H_\ell\le\ell^2E_\ell,
\qquad
E_\ell:=\int_{T_\ell}\rho^2dx.
\]
Hence
\[
\boxed{
E_\ell
\ge
\frac{\theta}{3}
\frac{J\ell}{(G_*^{\rm max})^2}
\ge
\frac{\theta\eta_*}{3}
\frac{J\delta}{(G_*^{\rm max})^2}.
}
\]

Thus a macroscopic level-width branch with a zero-flux floor and an upper gradient ceiling descends all the way to an enstrophy payer. If this persists on a nonvanishing normalized time interval with representation-safe bounded-overlap genealogy, the standard kinetic-energy dissipation ledger is the relevant lower-order ancestry resource.

If the upper gradient ceiling fails, that failure is itself the already-recognized first-coefficient-jet/high-gradient exit.

## 8. Exact integrated payer inequality for a flux drop

The flux derivative can also be integrated without the pointwise ratio ceiling.

By coarea,
\[
F(\ell)-F(0)
=
\int_{T_\ell}
\left[
2\rho\,\nabla\rho\cdot\nabla\kappa
+
\rho^2\Delta\kappa
\right]dx.
\]

Define
\[
E_\ell:=\int_{T_\ell}\rho^2dx,
\qquad
S_\ell:=
\int_{T_\ell}\rho^2|\Delta\kappa|^2dx.
\]

The amplitude term obeys
\[
\left|
\int_{T_\ell}2\rho\,\nabla\rho\cdot\nabla\kappa\,dx
\right|
\le
2(G_\ell P_\ell)^{1/2}.
\]
The coefficient-Laplacian term obeys
\[
\left|
\int_{T_\ell}\rho^2\Delta\kappa\,dx
\right|
\le
(E_\ell S_\ell)^{1/2}.
\]
Since the fractional loss is
\[
F(0)-F(\ell)=(1-\theta)J,
\]
we obtain the exact representation-homogeneous payer inequality
\[
\boxed{
(1-\theta)J
\le
2(G_\ell P_\ell)^{1/2}
+
(E_\ell S_\ell)^{1/2}.
}
\]

This formula is important for DSD bookkeeping. It says that an actual finite flux loss is not merely a supremum witness: it must be owned by either an existing lower-order product or a volume-integrated weighted second coefficient jet.

## 9. Uniform regular-gradient trichotomy

Assume in addition a lower regularity bound
\[
\boxed{g\ge g_*>0}
\]
on \(T_\ell\).

Then
\[
E_\ell
=
\int_{T_\ell}\rho^2dx
\le
\frac1{g_*^2}
\int_{T_\ell}\rho^2g^2dx
=
\frac{G_\ell}{g_*^2}.
\]

For the concrete half-flux case \(\theta=1/2\), the payer inequality yields the following convenient scale-matched trichotomy. At least one of
\[
\boxed{
G_\ell>J\delta,
}
\]
\[
\boxed{
P_\ell>\frac{J}{64\delta},
}
\]
or
\[
\boxed{
S_\ell\ge
\frac{g_*^2J}{16\delta}
}
\]
must hold.

Proof: if the first two inequalities fail, then
\[
2(G_\ell P_\ell)^{1/2}
\le
2\left(J\delta\cdot\frac{J}{64\delta}\right)^{1/2}
=
\frac J4.
\]
The total half-flux loss is \(J/2\), so
\[
\left|
\int_{T_\ell}\rho^2\Delta\kappa dx
\right|
\ge
\frac J4.
\]
Also
\[
E_\ell\le\frac{J\delta}{g_*^2}.
\]
Therefore
\[
S_\ell
\ge
\frac{(J/4)^2}{E_\ell}
\ge
\frac{g_*^2J}{16\delta}.
\]

The three thresholds are exactly scale matched:

- \(G_\ell\) and \(J\delta\) both scale as \(R^7\) spatially;
- \(P_\ell\) and \(J/\delta\) both scale as \(R^3\);
- \(S_\ell\) and \(g_*^2J/\delta\) both scale as \(R^9\).

Thus the trichotomy is representation safe.

If \(g_*\downarrow0\), the argument correctly exits through the M17-484 critical-level branch instead of dividing by a vanishing gradient.

## 10. Derivative-order audit of the second-jet payer

The new weighted second-coefficient-jet resource is
\[
S_\ell
=
\int_{T_\ell}\rho^2|\Delta\kappa|^2dx.
\]

M17-484 already records the twice-differentiated CE-H identity
\[
\Delta^2\Omega
=(\Delta\kappa)\Omega
+2\nabla\kappa\cdot\nabla\Omega
+\kappa^2\Omega.
\]
Projecting onto \(\xi=\Omega/\rho\) gives
\[
\boxed{
\rho\Delta\kappa
=
\xi\cdot\Delta^2\Omega
-2\nabla\kappa\cdot\nabla\rho
-\kappa^2\rho.
}
\]

Therefore the natural vorticity derivative order associated with \(S_\ell\) is \(D^4\Omega\), not \(D^3\Omega\).

The spatial scaling confirms this:
\[
S_{\ell,R}=R^9S_\ell.
\]
After time integration the scaling is \(R^7\), so a direct spacetime ancestry ledger would carry
\[
\boxed{R^{-7}.}
\]

This is two powers weaker than the existing M17-445 \(R^{-5}\) first-coefficient-jet/D3 ledger, exactly as predicted by the general derivative-order ancestry rule.

No lower bound on \(S_\ell\) can be converted to a lower bound on \(\|D^4\Omega\|_2^2\) without controlling the two lower terms in the displayed identity, because cancellation is possible. Conversely, if those lower terms are compact, then genuine second-jet growth reaches the D4 branch.

## 11. Why pure level geometry cannot generically remove the D4 branch

A local coefficient-field model shows the derivative firewall.

Let \(\rho\) and the transverse area be approximately constant and choose
\[
\kappa_\ell(x_1)
=
\ell\,\phi(x_1/\ell),
\]
where \(\phi'>0\) is smooth and changes by an order-one fraction over an order-one interval in its argument.

Then on a physical transition of width \(O(\ell)\),
\[
|\partial_1\kappa_\ell|=O(1),
\qquad
|\partial_1^2\kappa_\ell|=O(\ell^{-1}).
\]
Consequently
\[
\int|\nabla\kappa_\ell|^2dx
=O(\ell),
\]
while
\[
\int|\Delta\kappa_\ell|^2dx
=O(\ell^{-1}).
\]

Thus a level-flux change can be compressed into a vanishing coefficient interval while its first-jet mass tends to zero and its second-jet mass diverges.

This is only a local coefficient-geometry firewall, not a constructed Navier--Stokes or exact-CE-H solution. Its role is narrower: it proves that coarea and level geometry alone cannot justify an inequality that replaces the second coefficient jet by a fixed first-jet payer. Any such descent would need an additional CE-H/Navier--Stokes identity or dynamical input.

## 12. Time-thickness and ancestry firewall

All results above are snapshot statements. An ancestry contradiction requires spacetime ownership.

If a payer persists for normalized time \(\tau_m\), the corresponding parent weights are:

\[
\boxed{
\begin{aligned}
\rho^2|\nabla\kappa|^2 &: R_m^{-5},\\
|\nabla\Omega|^2 &: R_m^{-1},\\
\rho^2|\Delta\kappa|^2 &: R_m^{-7}.
\end{aligned}
}
\]

Therefore a fixed snapshot lower bound is not by itself a global contradiction. One must still prove sufficient temporal occupation/growth or non-reused multiplicity against the corresponding ancestry weight.

For the narrow-width palinstrophy branch,
\[
P_{\ell,m}
\gtrsim
\frac{J_m}{\ell_m},
\]
so with time thickness \(\tau_m\) the exact weighted series to test is of the form
\[
\boxed{
\sum_m
R_m^{-1}
\frac{J_m\tau_m}{\ell_m}.
}
\]
If \(J_m\) and \(\tau_m\) have fixed normalized positive floors, the recordwise threshold
\[
\ell_m\lesssim R_m^{-1}
\]
is sufficient to make the palinstrophy parent payment order one per record. This is a sufficient threshold, not a necessary condition for series divergence.

The second-jet branch is more expensive: a direct D4-order spacetime route must defeat \(R_m^{-7}\), so escalating derivatives without a descent identity is structurally unfavorable.

## 13. Updated DSD branch split

Combining M17-470, M17-483, M17-484, and the present audit gives
\[
\boxed{
\begin{aligned}
G_{\rm zero\text{-}tube\ flux\ loss}
\Longrightarrow{}&
G_{\rm macroscopic\ level\ width\to lower\ order\ payer}\\
&\lor G_{\rm palinstrophy\ level\ concentration}\\
&\lor G_{\rm weighted\ first\ coefficient\ jet/D3}\\
&\lor G_{\rm critical\ level}\\
&\lor G_{\rm weighted\ second\ coefficient\ jet/D4}\\
&\lor G_{\rm upper\ gradient/interface/domain\ loss}\\
&\lor G_{\rm temporal\ thinning/genealogy\ loss}.
\end{aligned}
}
\]

The important correction is that `second coefficient jet` is no longer merely a pointwise-supremum label. Actual fractional flux loss supplies the integrated payer inequality of Section 8, while Section 9 shows how this becomes a volume second-jet charge when the lower-order payers and critical-level exit are excluded.

## 14. Audit status

Closed/refined here:

- the coefficient-level width is made an explicit representation-safe variable;
- microscopic level-width collapse is quantitatively routed to palinstrophy concentration or inverse-width growth of \(\Lambda_{\kappa,\delta}\);
- macroscopic level width descends to the existing first-coefficient-jet resource and, with an upper gradient ceiling, to raw-H2/enstrophy;
- an actual half-flux loss obeys a scale-homogeneous integrated payer trichotomy;
- critical-level degeneration is kept separate and no division by a vanishing \(|\nabla\kappa|\) is used;
- the D4 barrier for the genuine weighted second coefficient jet is confirmed rather than assumed.

Still open:

- temporal thickening of a zero-tube flux-loss/second-jet event;
- a new identity that could descend \(\rho^2|\Delta\kappa|^2\) below D4 order;
- ancestry growth/multiplicity sufficient to defeat \(R^{-5}\), \(R^{-1}\), or \(R^{-7}\) as appropriate;
- parent-to-record genealogy and non-CE-H/ROOT-CERT exits.

## 15. Next target

The next useful audit should not immediately differentiate CE-H again. It should first test whether a fractional zero-tube flux-loss event has a one-sided minimum **time thickness** under the existing vorticity/strain controls. If such temporal thickening exists, Sections 6, 8, and 9 become spacetime payers. If not, temporal concentration becomes the next explicit representation-safe escape variable.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
