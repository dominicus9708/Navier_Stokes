# DSD M17-303 — Unit-window payments physicalize with packet-mass weights and do not yet force a nonsummable budget

Date: 2026-09-07  
Canonical ID: **M17-303**

Status: **PHYSICAL-WEIGHT / R21 GATE. AFTER THE M17-302 H3-FREE CORRECTION, THE FIXED-BAND BRANCH OF M17-301 RETURNS A LOGARITHMIC ANCESTOR FAILURE TO ONE RESCALED UNIT WINDOW WITH COEFFICIENT/RECHARGE ACTION, GRADIENT-INTERFACE ACTION, OR MASS-INTERFACE ACTION. PULLING THESE QUANTITIES BACK THROUGH `W=a_j V_j`, `y=q_j+r_j z`, `theta=theta_j+r_j^2 tau` SHOWS THAT A FIXED NORMALIZED GRADIENT PAYMENT COSTS ONLY `m_j=a_j^2 r_j^3` IN THE PARENT-VARIABLE SPACETIME GRADIENT LEDGER, WHILE A FIXED NORMALIZED MASS PAYMENT COSTS ONLY `m_j r_j^2`. THE COEFFICIENT PAYMENT EITHER RETURNS TO THE ALREADY TYPED SCALED-COEFFICIENT / SURROUNDING-MASS ESCAPES OF M17-255 OR, AFTER PULLBACK, CARRIES AN `m_j^(1/2)` L1_t L2_x FORCING WEIGHT RATHER THAN A FIXED PHYSICAL QUANTUM. ON THE CONDITIONAL M17-299 REPRESENTATIVE FLOOR, THE GUARANTEED `m_j` AND `m_j r_j^2` LOWER FLOORS ARE SUMMABLE ACROSS DYADIC REMOTE SHELLS. THIS DOES NOT PROVE THE ACTUAL WEIGHT SUM IS FINITE; IT PROVES THAT THE CURRENT LOWER BOUNDS CANNOT FORCE NONSUMMABILITY. THEREFORE THE DIRECT 'INFINITELY MANY UNIT PAYMENTS -> INFINITE BUDGET' LANE IS CLOSED AS A PROOF SHORTCUT. THE SURVIVING TARGET IS AGGREGATE/MULTIPLICITY COMPENSATION, STRICT SCALE DESCENT, OR BOUNDED-MULTIPLICITY ANCESTOR MIGRATION TO A TRUE FINITE/SIGNED RESOURCE. GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.**

---

## 1. Correct inherited late branch

M17-302 corrects M17-300/301 by adding the high-frequency alternative.  On the branch where the raw `H2` tail is tight, a fixed Fourier annulus survives and M17-301 applies.

After the audit-debt closure note of 2026-09-07, the parent-amplitude part of the old exit label is sharpened: first hitting supplies the amplitude ceiling on every represented parent past time.  What can still fail over the logarithmic lookback is the parent-to-M17 representation itself.

Thus the late branch entering this module is

\[
\boxed{
\begin{aligned}
H_{shell\text{-}relevant\ packet}
\Longrightarrow{}&
G_{high\text{-}frequency/subscale/nodal}\\
&\lor G_{cross\text{-}scale\ allocation}\\
&\lor G_{parent\text{-}to\text{-}M17\ scale\text{-}map/domain/genealogy}\\
&\lor H_{unit\text{-}window\ coefficient/recharge}\\
&\lor H_{unit\text{-}window\ gradient\ interface}\\
&\lor H_{unit\text{-}window\ mass\ interface}.
\end{aligned}
}
\]

The present module audits the last three payment alternatives.

---

## 2. Own-scale pullback

Use the M17-251/255 own-scale normalization

\[
\boxed{
W(y,\theta)=a_jV_j(z,\tau),
\qquad
y=q_j(\theta)+r_jz,
\qquad
\theta=\theta_j+r_j^2\tau.
}
\]

The moving center changes the drift term but not the following Jacobian identities:

\[
\boxed{
dy=r_j^3dz,
\qquad
d\theta=r_j^2d\tau,
}
\]

and

\[
\boxed{
\nabla_yW=\frac{a_j}{r_j}\nabla_zV_j.
}
\]

Define the packet `L2` mass scale

\[
\boxed{
m_j:=a_j^2r_j^3.}
\]

This is exactly the normalization used in M17-251/296.

The quantities below are first pulled back only to the **parent similarity variables** `(y,theta)`.  A claim about an original physical Navier–Stokes global budget would require the additional parent-to-original scaling and a theorem identifying a finite/signed resource.  That extra step is not silently assumed here.

---

# 3. Gradient-interface payment has parent weight m_j

M17-301 gives, on the gradient-interface branch, a fixed unit-window action.  After Cauchy–Schwarz on the unit interval and the fixed cutoff support, it yields

\[
\boxed{
\int_{I_j}\int_{\operatorname{supp}\nabla\chi}
|\nabla_zV_j|^2\,dz\,d\tau
\ge c_{grad}>0.
}
\]

Pull back the spacetime gradient quantity:

\[
\begin{aligned}
\int |\nabla_yW|^2\,dy\,d\theta
&=
\int
\frac{a_j^2}{r_j^2}|\nabla_zV_j|^2
r_j^3dz\,r_j^2d\tau\\
&=
\boxed{
a_j^2r_j^3
\int|\nabla_zV_j|^2dz\,d\tau}.
\end{aligned}
\]

Therefore

\[
\boxed{
\text{fixed normalized gradient payment}
\Longrightarrow
\text{parent gradient cost}\ge c_{grad}m_j.
}
\]

It is **not** a fixed parent-variable quantum independent of the packet.

This is the exact R21 weight.

---

# 4. Mass-interface payment has parent weight m_j r_j^2

On the mass-interface branch M17-301 yields

\[
\boxed{
\int_{I_j}\int_{\operatorname{supp}\Delta\chi}
|V_j|^2\,dz\,d\tau
\ge c_{mass}>0.
}
\]

The parent-variable spacetime `L2` mass is

\[
\begin{aligned}
\int |W|^2\,dy\,d\theta
&=
\int a_j^2|V_j|^2r_j^3dz\,r_j^2d\tau\\
&=
\boxed{
a_j^2r_j^5
\int|V_j|^2dz\,d\tau}\\
&=
\boxed{m_jr_j^2
\int|V_j|^2dz\,d\tau}.
\end{aligned}
\]

Hence

\[
\boxed{
\text{fixed normalized mass-interface payment}
\Longrightarrow
\text{parent spacetime mass cost}\ge c_{mass}m_jr_j^2.
}
\]

This weight is even smaller than the gradient weight when `r_j<<1`.

Moreover, a cutoff mass-interface payment is not automatically dissipative.  It may represent spatial migration of normalized packet mass through the localization annulus.  It therefore needs a migration/genealogy theorem rather than being counted as signed dissipation.

---

# 5. Coefficient/recharge payment returns to existing M17-255 exits unless the coefficient corridor is genuinely active

M17-255 writes the own-scale equation as

\[
\partial_\tau V_j-\Delta V_j
=-A_j\cdot\nabla V_j+C_jV_j,
\]

with

\[
A_j(z,\tau)
=r_j\big[B(q_j+r_jz,\theta)-B(q_j,\theta)\big],
\]

and

\[
C_j(z,\tau)
=r_j^2\Sigma(q_j+r_jz,\theta)-r_j^2I.
\]

Write

\[
\mathcal N_j=-A_j\cdot\nabla V_j+C_jV_j.
\]

Suppose M17-301 gives

\[
\boxed{
\int_{I_j}\|\chi\mathcal N_j\|_2d\tau\ge\delta_N>0.
}
\]

On a fixed unit window,

\[
\begin{aligned}
\int_{I_j}\|\chi\mathcal N_j\|_2d\tau
\lesssim{}&
\|A_j\|_{L^\infty}
\left(\int_{I_j}\|\nabla V_j\|_2^2d\tau\right)^{1/2}\\
&+
\|C_j\|_{L^\infty}
\left(\int_{I_j}\|V_j\|_2^2d\tau\right)^{1/2}.
\end{aligned}
\]

Therefore, if the scaled coefficients tend to zero and the normalized local `H1/L2` spacetime norms remain bounded, the coefficient/recharge action tends to zero and cannot pay `delta_N`.

Conversely, a fixed coefficient payment forces at least one of:

\[
\boxed{
G_{scaled\ coefficient}
\lor
G_{normalized\ surrounding\text{-}mass/H1\ decompactification}.
}
\]

The second alternative is compatible with the M17-255 Caccioppoli gate: with bounded coefficients, bounded surrounding mass would bound the interior gradient norm, so unbounded normalized `H1` action cannot occur without surrounding-mass/cylinder exit.

Thus the coefficient branch is not a new terminal budget.  It returns to already typed ambient/coefficient or decompactification exits.

---

## 6. Optional parent forcing norm and its weight

The own-scale nonheat term satisfies schematically

\[
\mathcal N_j
=\frac{r_j^2}{a_j}\,G_j
\]

where `G_j` denotes the corresponding parent-variable lower-order forcing after the moving-center translation has been removed.

Hence

\[
\|G_j\|_{L^2_y}
=a_jr_j^{-1/2}\|\mathcal N_j\|_{L^2_z},
\]

and over one own-scale unit time window

\[
\boxed{
\int\|G_j\|_{L^2_y}d\theta
=a_jr_j^{3/2}
\int\|\mathcal N_j\|_2d\tau
=m_j^{1/2}
\int\|\mathcal N_j\|_2d\tau.
}
\]

Thus even this direct pullback carries a packet-dependent `m_j^(1/2)` weight.  More importantly, no finite global `L1_tL2_x` budget for this lower-order forcing has been established.  It cannot be declared a contradiction merely because the normalized action is fixed.

---

# 7. Insert the conditional M17-299 representative floor

The following subsection is conditional on the still-open M17-298 cross-scale allocation theorem, because M17-299 inherits that dependency.

M17-299 gives on an infinite selected dyadic-shell subsequence

\[
\boxed{
a_j
\ge
cR_j^{-2}
(\log R_j)^{-4/3-\varepsilon/2}
(\log\log R_j)^{-1/2}}
\]

and

\[
\boxed{
r_j^2\ge c(\log R_j)^{-1}.}
\]

Therefore

\[
\begin{aligned}
m_j
&=a_j^2r_j^3\\
&\ge
cR_j^{-4}
(\log R_j)^{-8/3-\varepsilon}
(\log\log R_j)^{-1}
(\log R_j)^{-3/2}.
\end{aligned}
\]

Hence

\[
\boxed{
m_j
\ge
cR_j^{-4}
(\log R_j)^{-25/6-\varepsilon}
(\log\log R_j)^{-1}.}
\]

Similarly,

\[
\boxed{
m_jr_j^2
\ge
cR_j^{-4}
(\log R_j)^{-31/6-\varepsilon}
(\log\log R_j)^{-1}.}
\]

And the direct `L1_tL2_x` forcing-action weight has the guaranteed floor

\[
\boxed{
m_j^{1/2}
\ge
cR_j^{-2}
(\log R_j)^{-25/12-\varepsilon/2}
(\log\log R_j)^{-1/2}.}
\]

---

# 8. These guaranteed floors are summable on dyadic remote shells

For dyadic shell radii

\[
R_k\asymp2^k,
\]

the guaranteed gradient-payment floor has the model form

\[
2^{-4k}
 k^{-25/6-\varepsilon}
(\log k)^{-1},
\]

which is summable.

The mass-interface floor contains one further factor comparable to `k^-1`, and is also summable.

The `m_j^(1/2)` forcing-action floor contains `2^-2k` and is likewise summable.

Therefore the present representative lower bounds do **not** imply

\[
\sum_jm_j=\infty,
\qquad
\sum_jm_jr_j^2=\infty,
\qquad
\text{or}\qquad
\sum_jm_j^{1/2}=\infty.
\]

The exact logical statement is important:

\[
\boxed{
\text{a summable proved lower floor does NOT prove the actual weights are summable.}
}
\]

It proves only

\[
\boxed{
\text{the current lower-floor information is insufficient to force nonsummability.}
}
\]

Thus R21 blocks the direct contradiction.

---

# 9. Even a nonsummable parent gradient occupancy would still need a true finite-resource theorem

The field `W` here is the parent similarity/vorticity-side field.  The quantity

\[
\int|\nabla_yW|^2dy\,d\theta
\]

is a palinstrophy-like parent-variable quantity.

It is not automatically identical to the basic finite kinetic-energy dissipation budget of the original velocity equation.  Therefore even an eventual proof that some selected parent gradient costs are nonsummable would still require:

1. a correct parent-to-original scaling map;
2. controlled multiplicity in physical space-time;
3. identification with a globally finite or signed/monotone resource.

This firewall prevents a second version of the normalized-payment error at the parent-variable level.

---

# 10. Aggregate-family check

One might hope that the representative floor is weak only because M17-299 selected one packet per shell.

Suppose, conditionally on a valid M17-298 allocation, a shell-relevant family carries a fixed fraction of `H^{sh}` and every such packet lies above the logarithmic floor

\[
r_i^2\gtrsim(\log R)^{-1}.
\]

Since scale comparability gives

\[
m_i\asymp H_ir_i^4,
\]

an entire paying family would satisfy schematically

\[
\sum_i m_i
\gtrsim
(\log R)^{-2}
\sum_iH_i
\gtrsim
(\log R)^{-2}H^{sh}.
\]

Using only the current shell lower bound

\[
H^{sh}\gtrsim
R^{-1}(\log R)^{-2/3-\varepsilon}
\]

gives

\[
\boxed{
\sum_i m_i
\gtrsim
R^{-1}(\log R)^{-8/3-\varepsilon}.}
\]

Across dyadic `R`, this guaranteed aggregate floor is still summable because of the factor `R^-1`.

Thus even the most direct fixed-fraction aggregate upgrade does not by itself create the required nonsummable parent budget from the currently proved shell floor.

A stronger multiplicity/time-density mechanism or a different signed/critical resource is needed.

---

# 11. Corrected late gate after physical weighting

Combining M17-302, M17-301, M17-255, and the present pullback gives the DSD-safe frontier

\[
\boxed{
\begin{aligned}
H_{shell\text{-}relevant\ late\ packet}
\Longrightarrow{}&
G_{high\text{-}frequency/subscale/nodal}\\
&\lor G_{cross\text{-}scale\ raw\text{-}H2\ allocation}\\
&\lor G_{parent\text{-}to\text{-}M17\ scale\text{-}map/domain/genealogy}\\
&\lor G_{scaled\ coefficient/normalized\ decompactification}\\
&\lor H_{gradient\ interface\ payment\ with\ weight\ m_j}\\
&\lor H_{mass\ interface/migration\ with\ weight\ m_jr_j^2}.
\end{aligned}
}
\]

The last two alternatives are **weighted occupations**, not terminal contradictions.

---

# 12. What has been closed by M17-303

The following shortcut is now formally retired:

\[
\boxed{
\text{infinitely many fixed unit-window normalized payments}
\Longrightarrow
\text{infinite physical/global budget}.
}
\]

It fails at the first pullback because the payment weights depend on the packet:

\[
\boxed{m_j,\qquad m_jr_j^2,\qquad m_j^{1/2}.}
\]

The M17-299 representative lower floors are too small to force nonsummability, and no true global finite resource has yet been attached to the interface quantities.

This is a **negative closure of a proof shortcut**, not a negative result about global regularity.

---

# 13. Next canonical target

The next useful theorem must exploit information that a one-representative-per-shell payment cannot see.

The narrow alternatives are:

1. **payment multiplicity / density**: prove many disjoint packets or many disjoint unit windows must pay, with enough multiplicity to compensate the small weights;
2. **bounded-multiplicity ancestor migration**: show mass-interface events can be followed through a genealogy with a finite number of reuses of the same parent resource;
3. **strict scale descent**: every unpaid/migrating event descends to a strictly smaller intrinsic scale and cannot restart indefinitely away from the nodal channel;
4. **signed or monotone ledger**: replace unsigned occupancy by a quantity whose repeated same-sign change is globally finite;
5. **critical-resource conversion**: relate the paying family to the nonsummable M17-207 critical shell quantity without losing the fatal powers of `R`.

A suitable next module is therefore a **payment multiplicity / genealogy gate**, not another direct summation of representative packet costs.

---

# 14. DSD audit

- `R21`: PASS as a firewall; the physicalized packet weights are explicit.
- The Jacobian and derivative scaling are exact under the own-scale map.
- The coefficient branch is returned to M17-255 exits unless scaled coefficients genuinely remain active.
- The M17-299 numerical floors are used only conditionally on the unresolved M17-298 allocation theorem.
- Summability of a proved lower floor is not confused with summability of the actual unknown weights.
- Mass-interface occupancy is not relabeled as dissipation.
- Parent-variable palinstrophy-like cost is not silently equated with a globally finite original physical energy budget.
- No global regularity claim is made.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
