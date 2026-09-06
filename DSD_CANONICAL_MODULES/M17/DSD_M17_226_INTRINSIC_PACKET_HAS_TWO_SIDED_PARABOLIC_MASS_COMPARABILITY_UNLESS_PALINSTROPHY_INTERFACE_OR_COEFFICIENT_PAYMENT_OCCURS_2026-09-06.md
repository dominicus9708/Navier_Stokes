# DSD M17-226 — Intrinsic packet has two-sided parabolic mass comparability unless palinstrophy, interface, or coefficient payment occurs

Date: 2026-09-06  
Canonical ID: **M17-226**

Status: **TWO-SIDED STOPPING-TIME UPGRADE / M17-225 PROVED THAT A BUFFERED INTRINSIC PACKET CANNOT LOSE A FIXED MASS FRACTION FORWARD IN `O(r_j^2)` TIME WITHOUT LOCAL PALINSTROPHY, TRANSITION/INTERFACE TURNOVER, OR A COEFFICIENT EXIT. THE SAME EXACT LOCALIZED ENSTROPHY IDENTITY ALSO HAS AN UPPER DIFFERENTIAL INEQUALITY: FORWARD GROWTH OF THE PACKET CANNOT BE PRODUCED BY THE DISSIPATIVE PALINSTROPHY TERM AND THEREFORE REQUIRES TRANSITION/INTERFACE INPUT OR A COEFFICIENT EXIT. APPLYING THE LOWER AND UPPER INEQUALITIES TO FORWARD AND BACKWARD STOPPING TIMES SHOWS THAT, UNLESS A FIXED `O(M_j(0))` PAYMENT OCCURS, THE LOCALIZED ENSTROPHY REMAINS UNIFORMLY COMPARABLE TO ITS OBSERVATION-TIME VALUE THROUGH THE ENTIRE SYMMETRIC PARABOLIC WINDOW `[-c r_j^2,c r_j^2]`. THUS THE PERSISTENT BRANCH NOW HAS A GENUINE TWO-SIDED NONVANISHING MASS NORMALIZATION SUITABLE FOR A PARABOLIC TANGENT EXTRACTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-225

Let `q_j(theta)` be the material center and let

\[
\zeta_j(y,\theta)
=\zeta_0\!\left(\frac{y-q_j(\theta)}{r_j}\right),
\qquad r_j\to0.
\]

Define

\[
M_j(\theta):=\int \zeta_j^2 |W|^2dy,
\]

\[
D_j(\theta):=\int \zeta_j^2 |\nabla W|^2dy,
\]

and transition-region enstrophy

\[
N_j(\theta)
:=\int_{\operatorname{supp}\nabla\zeta_j(\theta)}|W|^2dy.
\]

On a short corridor where

\[
\|\nabla B\|_{L^\infty(B_{Cr_j})}\le L_*,
\qquad
\|\Sigma\|_{L^\infty(B_{Cr_j})}\le S_*,
\]

M17-225 gives the exact localized enstrophy identity

\[
\begin{aligned}
M_j'
={}&-2D_j
-4\int\zeta_j W\cdot(\nabla\zeta_j\cdot\nabla W)dy\\
&+2\int\zeta_j^2 W\cdot\Sigma Wdy
-\frac12M_j
+2\int\zeta_j(D_B\zeta_j)|W|^2dy.
\end{aligned}
\]

---

## 2. Two one-sided differential inequalities

Young's inequality gives

\[
4\left|\int\zeta_j W\cdot(\nabla\zeta_j\cdot\nabla W)dy\right|
\le D_j+C r_j^{-2}N_j.
\]

The bounded strain, reaction, and material-cutoff terms contribute at most `C_0 M_j` in absolute value.

Hence the exact identity gives both

\[
\boxed{
M_j'
\ge
-C_DD_j-C_Br_j^{-2}N_j-C_0M_j
}
\]

and

\[
\boxed{
M_j'
\le
-c_DD_j+C_Br_j^{-2}N_j+C_0M_j
}
\]

for fixed positive constants independent of `j`.

The second inequality is the new ingredient used here.

Its sign structure is important:

\[
\boxed{
\text{palinstrophy cannot create forward packet-mass growth.}
}
\]

---

## 3. Forward fixed-fraction loss

Fix `0<eta<1/4` and a small fixed `c_p>0`.

Suppose a first forward time

\[
\tau_{j,\downarrow}^+\in[0,c_pr_j^2]
\]

satisfies

\[
M_j(\tau_{j,\downarrow}^+)
=(1-\eta)M_j(0),
\]

while `M_j<=2M_j(0)` before that time.

M17-225 already gives

\[
\boxed{
\int_0^{\tau_{j,\downarrow}^+}D_jd\theta
+r_j^{-2}\int_0^{\tau_{j,\downarrow}^+}N_jd\theta
\ge c_\eta M_j(0).
}
\]

Thus a forward downward excursion is paid by palinstrophy and/or interface turnover.

---

## 4. Forward fixed-fraction growth

Suppose instead that a first forward time

\[
\tau_{j,\uparrow}^+\in[0,c_pr_j^2]
\]

satisfies

\[
M_j(\tau_{j,\uparrow}^+)
=(1+\eta)M_j(0),
\]

with

\[
M_j(\theta)\le2M_j(0)
\]

before that time.

Integrate the upper differential inequality and drop the favorable negative palinstrophy term:

\[
\eta M_j(0)
\le
C_Br_j^{-2}
\int_0^{\tau_{j,\uparrow}^+}N_jd\theta
+C_0\int_0^{\tau_{j,\uparrow}^+}M_jd\theta.
\]

Since the interval length is at most `c_p r_j^2`,

\[
\int_0^{\tau_{j,\uparrow}^+}M_jd\theta
\le2c_pr_j^2M_j(0).
\]

For sufficiently large `j`,

\[
2C_0c_pr_j^2\le\eta/2.
\]

Therefore

\[
\boxed{
r_j^{-2}
\int_0^{\tau_{j,\uparrow}^+}N_jd\theta
\ge c_\eta M_j(0).
}
\]

So forward packet amplification requires transition/interface replenishment unless the coefficient corridor fails.

---

## 5. Backward ancestor deficit

Now inspect the interval

\[
[-c_pr_j^2,0].
\]

Suppose there is a latest backward time

\[
\tau_{j,\downarrow}^-<0
\]

such that

\[
M_j(\tau_{j,\downarrow}^-)
=(1-\eta)M_j(0),
\]

and

\[
M_j(\theta)\le2M_j(0)
\]

for

\[
\tau_{j,\downarrow}^-\le\theta\le0.
\]

Viewed in the physical forward direction, the packet grows from `(1-eta)M_j(0)` to `M_j(0)`.

Integrating the upper inequality from `tau_{j,downarrow}^-` to `0` therefore gives

\[
\eta M_j(0)
\le
C_Br_j^{-2}
\int_{\tau_{j,\downarrow}^-}^{0}N_jd\theta
+C_0\int_{\tau_{j,\downarrow}^-}^{0}M_jd\theta.
\]

Again the lower-order term is `o(M_j(0))`, so

\[
\boxed{
r_j^{-2}
\int_{\tau_{j,\downarrow}^-}^{0}N_jd\theta
\ge c_\eta M_j(0).
}
\]

Thus a current packet cannot appear from an enstrophy-poor ancestor for free.

This is the precise backward replenishment gate.

---

## 6. Backward ancestor excess

Suppose instead that at some backward time

\[
\tau_{j,\uparrow}^-<0
\]

we have

\[
M_j(\tau_{j,\uparrow}^-)
=(1+\eta)M_j(0),
\]

with `M_j<=2M_j(0)` on the interval from that time to `0`.

In the forward direction this is a fixed-fraction mass loss.

Applying the lower differential inequality over

\[
[\tau_{j,\uparrow}^-,0]
\]

gives

\[
\boxed{
\int_{\tau_{j,\uparrow}^-}^{0}D_jd\theta
+r_j^{-2}
\int_{\tau_{j,\uparrow}^-}^{0}N_jd\theta
\ge c_\eta M_j(0).
}
\]

Thus a much larger ancestor followed by substantial decay is also quantitatively paid.

---

## 7. Two-sided parabolic comparability

Assume now that throughout

\[
I_j
:=[-c_pr_j^2,c_pr_j^2]
\]

there is no coefficient hard exit and that

\[
\int_{I_j}D_jd\theta
+r_j^{-2}\int_{I_j}N_jd\theta
=o(M_j(0)).
\]

Then none of the four stopping events in Sections 3--6 can occur for sufficiently large `j`.

Hence

\[
\boxed{
(1-\eta)M_j(0)
\le
M_j(\theta)
\le
(1+\eta)M_j(0)
\qquad
\forall\theta\in I_j.
}
\]

More generally, with fixed payment thresholds rather than `o(1)`, one obtains constants

\[
0<c_M<C_M<\infty
\]

such that

\[
\boxed{
c_MM_j(0)
\le M_j(\theta)
\le C_MM_j(0)
\qquad
\forall\theta\in I_j.
}
\]

This is the two-sided mass corridor required for a nonzero parabolic tangent normalization.

---

## 8. Correct branch statement

The intrinsic packet branch now satisfies

\[
\boxed{
H_{buffered\ intrinsic\ packet}
\Longrightarrow
H_{two\text{-}sided\ parabolic\ mass\ corridor}
\lor
H_{local\ palinstrophy}
\lor
H_{interface/replenishment}
\lor
G_{local\ coefficient\ spike}.
}
\]

The backward side introduces no new free mechanism.

A deficient ancestor is exactly a forward replenishment event.

An excessive ancestor is exactly a forward dissipation/turnover event.

---

## 9. Parabolic normalization

On the two-sided corridor define

\[
\boxed{
V_j(z,\tau)
:=
\frac{r_j^{3/2}}{M_j(0)^{1/2}}
W\!\left(q_j(r_j^2\tau)+r_jz,r_j^2\tau\right).
}
\]

Then

\[
\int\zeta_0(z)^2|V_j(z,\tau)|^2dz
=
\frac{M_j(r_j^2\tau)}{M_j(0)}.
\]

Therefore on every fixed `|tau|<=c_p`,

\[
\boxed{
c_M
\le
\int\zeta_0^2|V_j|^2dz
\le C_M.
}
\]

The tangent sequence is thus normalized neither to zero nor to infinity on the packet core.

---

## 10. What M17-226 does not yet prove

Two-sided `L2` mass comparability alone does not imply compactness of `V_j`.

In particular M17-224 supplies a **lower** intrinsic `H2/L2` ratio but does not by itself give the uniform **upper** local derivative bounds required for strong compactness after rescaling.

Therefore the next step must audit whether one can extract a scale-matched spectral band/packet with two-sided derivative control, or else route derivative escalation to an existing higher-frequency/palinstrophy hard branch.

It would be invalid to claim a nonzero heat tangent from mass persistence alone.

---

## 11. DSD analysis

### 11.1 Time orientation

No dissipative inequality is reversed.

Backward information is obtained by viewing the interval in the physical forward direction and using the appropriate upper or lower differential inequality.

### 11.2 Growth versus decay payers

- fixed forward growth: interface/replenishment;
- fixed forward decay: palinstrophy or interface turnover;
- backward deficit: forward replenishment;
- backward excess: forward decay payment.

This exhausts the two-sided mass alternatives under bounded coefficients.

### 11.3 Normalization boundary

The theorem produces a robust nonzero `L2` normalization, not a derivative compactness theorem.

---

## 12. DSD audit

- The exact M17-225 identity is used in both inequality directions.
- Dissipation is never used as a source of forward growth.
- Backward persistence is not obtained by reversing the heat flow.
- Upward mass events are no longer left unclassified.
- The coefficient ceiling remains explicit; its failure is exported.
- Two-sided mass comparability is separated from derivative compactness.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
