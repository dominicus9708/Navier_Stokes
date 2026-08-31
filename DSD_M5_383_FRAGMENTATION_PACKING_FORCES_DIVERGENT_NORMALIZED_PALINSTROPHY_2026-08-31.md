# DSD M5-383 — Fragmentation packing forces divergent normalized palinstrophy

Date: 2026-08-31

Status: **A FIXED-FRACTION OPPOSITE-SIGNED CIRCULATION RESERVOIR CANNOT EVADE M5-382 MERELY BY BREAKING INTO MANY SEPARATED MICROCOMPONENTS / EACH TRUE FRAGMENT HAS A TRANSITION-CAPACITY COST OF ORDER `W^2 ell_i`, WHILE THE FIRST-HITTING AMPLITUDE CAP LIMITS ITS FLUX TO ORDER `W ell_i^2` / THE TOTAL FLUX REQUIREMENT THEREFORE FORCES `sum ell_i^2 >= c d^2` AND HENCE TOTAL PALINSTROPHY `>= c W^2 d` / IN NATURAL UNITS THIS IS `P_hat >= c d/r ~ r^(-1/5) -> infinity` / HEAVY OVERLAP OR FAILURE OF A CONTRASTING EXTERIOR MEANS THE PIECES ARE NOT SEPARATE FRAGMENTS AND ROUTES BACK TO A MERGED RESERVOIR OR TO SPATIAL/DESCRIPTIVE LOSS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-382 closed every **regular coherent sheet** by the thickness-independent estimate

\[
 \mathfrak P_j\gtrsim d_j/r_j\to\infty.
\]

The remaining cancellation-related T frontier retained

\[
 T_{\rm fragmentation/microshape}
\]

because an arbitrary fragmented set need not admit one regular tubular normal foliation.

This note asks whether fragmentation itself can lower the derivative cost.

The answer is no on the separated-fragment corridor: the circulation requirement produces a simple flux-packing inequality, while each genuinely separate fragment has its own local transition-capacity cost.

---

## 2. Scales and required opposite flux

On the saturated affine-shield corridor,

\[
 W_j\asymp \frac{\nu}{r_j^2},
 \qquad
 d_j\asymp r_j^{4/5},
 \qquad
 \Gamma_j\asymp W_j d_j^2.
\]

To cancel or Eulerianly screen a fixed fraction `c_Gamma>0` of the shield circulation with opposite-signed high vorticity, the retained opposite reservoir must carry total signed flux magnitude at least

\[
 \boxed{
 \sum_i |\Gamma_{j,i}^{-}|
 \ge c_\Gamma W_jd_j^2.
 }
\]

The index `i` labels separated retained fragments.

---

## 3. Definition of a genuine fragment

For each fragment choose a characteristic physical radius `ell_i>0` and a ball

\[
 B_i=B_{C\ell_i}(x_i)
\]

with fixed `C` such that:

1. a fixed positive fraction of `B_i` contains opposite-signed vorticity of magnitude at least `c_1W_j`;
2. another fixed positive fraction of `B_i` contains a vector state separated from that opposite state by at least `c_2W_j`;
3. the selected family of balls has uniformly bounded overlap after the standard Vitali pruning;
4. the fragment's relevant cross-sectional area is at most `C_A ell_i^2`.

These are not extra hidden assumptions about all geometry. They define the **separated-fragment corridor**.

If item 2 fails, the high-vorticity state continues through the surrounding ball and the piece is not a separate fragment at scale `ell_i`; enlarge/merge it.

If no bounded-overlap pruning retaining a fixed fraction of the required flux is possible because the pieces overlap at arbitrarily many scales, that failure is a multiscale spatial/reach degeneration and remains explicitly typed as T rather than being counted additively.

---

## 4. Flux capacity of one fragment

The first-hitting amplitude cap gives

\[
 |\omega|\le C_W W_j
\]

on the retained stage/window, with fixed `C_W`.

A fragment with cross-sectional area `<= C_A ell_i^2` therefore carries at most

\[
 \boxed{
 |\Gamma_{j,i}^{-}|
 \lesssim W_j\ell_i^2.
 }
\]

Summing and using the fixed-fraction flux requirement gives

\[
 W_j\sum_i\ell_i^2
 \gtrsim
 W_jd_j^2.
\]

Hence

\[
 \boxed{
 \sum_i\ell_i^2\gtrsim d_j^2.
 }
\]

This is the geometric packing obligation created solely by the amplitude cap and the amount of circulation to be screened.

---

## 5. Local transition-capacity cost of one fragment

Inside `B_i`, two positive-volume subsets carry vector values separated by `>=c_2W_j`.

Therefore the vector variance on `B_i` obeys

\[
 \int_{B_i}
 |\omega-\overline\omega_{B_i}|^2dx
 \gtrsim
 W_j^2\ell_i^3.
\]

The ordinary vector Poincare inequality on `B_i` yields

\[
 \int_{B_i}
 |\omega-\overline\omega_{B_i}|^2dx
 \lesssim
 \ell_i^2
 \int_{B_i}|\nabla\omega|^2dx.
\]

Consequently

\[
 \boxed{
 \int_{B_i}|\nabla\omega|^2dx
 \gtrsim
 W_j^2\ell_i.
 }
\]

This is a capacity statement and requires no smooth normal surface.

---

## 6. Add the separated fragments

After bounded-overlap Vitali pruning,

\[
 \int_{\cup_iB_i}|\nabla\omega|^2dx
 \gtrsim
 W_j^2\sum_i\ell_i.
\]

For nonnegative radii,

\[
 \left(\sum_i\ell_i\right)^2
 \ge
 \sum_i\ell_i^2.
\]

Thus Section 4 implies

\[
 \boxed{
 \sum_i\ell_i
 \gtrsim d_j.
 }
\]

Hence

\[
 \boxed{
 \int_{\cup_iB_i}|\nabla\omega|^2dx
 \gtrsim
 W_j^2d_j.
 }
\]

This lower bound is independent of the number of fragments.

Making the pieces smaller does not help; the flux constraint forces enough total linear capacity to compensate.

---

## 7. Natural normalization

Use

\[
 \mathfrak P_j
 :=
 \frac{r_j^3}{\nu^2}
 \int|\nabla\omega|^2dx.
\]

Since

\[
 W_j\asymp\nu/r_j^2,
\]

we obtain

\[
 \begin{aligned}
 \mathfrak P_j
 &\gtrsim
 \frac{r_j^3}{\nu^2}
 \frac{\nu^2}{r_j^4}d_j\\
 &=
 \frac{d_j}{r_j}.
 \end{aligned}
\]

Therefore

\[
 \boxed{
 \mathfrak P_j
 \gtrsim
 \frac{d_j}{r_j}
 \asymp
 r_j^{-1/5}
 \to\infty.
 }
\]

Thus separated fragmentation is a derivative/palinstrophy H event on the late saturated corridor.

---

## 8. Fragment-count interpretation

Suppose, for intuition, `N` fragments have comparable radius `ell`.

The flux constraint gives

\[
 N\ell^2\gtrsim d_j^2,
\]

whereas the derivative cost is

\[
 \int|\nabla\omega|^2
 \gtrsim
 W_j^2N\ell.
\]

Therefore

\[
 N\ell
 \gtrsim
 d_j\sqrt N.
\]

So increasing the fragment count actually increases the lower bound on total transition capacity.

The cheapest separated configuration is the least fragmented one, consistent with the merged-sheet analysis of M5-382.

---

## 9. Relation to M5-81 fragmentation

M5-81 identified a different fragmentation mechanism: an order-one total coarea crossing density could split among many connected amplitude-level components.

The present result does not claim to solve every analytic level-set fragmentation problem.

It closes the specific **circulation-disposal fragmentation** relevant to M5-381--382, because here each fragment must carry a portion of a fixed macroscopic opposite-signed flux and is subject to the first-hitting amplitude cap.

Thus the two uses of the word fragmentation must remain separate in the DSD ledger.

---

## 10. What happens if the fragment balls overlap too strongly?

There are three possibilities.

### A. Same-scale heavy overlap

The opposite high-vorticity pieces form one larger connected/merged reservoir at the shield scale.

This returns to M5-382 and pays

\[
 \mathfrak P_j\gtrsim d_j/r_j.
\]

### B. Multiscale nested overlap

The description requires an unbounded hierarchy of radii/reaches.

This is a scale-capacity degeneration:

\[
 H_{\rm freq/cap}
 \lor
 T_{\rm irregular\ multiscale\ reach}.
\]

No additive count is asserted until a bounded-overlap subfamily carrying definite flux is selected.

### C. No local exterior contrast

Then the retained object is not a separate fragment at that scale and must be enlarged until either contrast appears or it merges with a macroscopic reservoir.

Thus fragmentation cannot be created merely by relabeling overlapping parts of one coherent object.

---

## 11. DSD audit

### Derived on the separated-fragment corridor

- fragment flux cap
  \[
  |\Gamma_i|\lesssim W\ell_i^2;
  \]
- macroscopic cancellation forces
  \[
  \sum_i\ell_i^2\gtrsim d^2;
  \]
- local vector contrast plus Poincare forces
  \[
  \int_{B_i}|\nabla\omega|^2\gtrsim W^2\ell_i;
  \]
- bounded-overlap packing gives
  \[
  \mathfrak P_j\gtrsim d_j/r_j\to\infty.
  \]

### Firewall

Do not sum overlapping fragment transition balls without a bounded-overlap selection.

Do not assume every irregular fractal set admits one scale `ell_i`; failure of finite-scale component description remains the multiscale-reach T/H frontier.

Do not equate this circulation-fragmentation lemma with the unrelated M5-81 amplitude-level component fragmentation problem.

---

## 12. Updated T frontier

For circulation disposal on the no-H saturated corridor, the following are now excluded as independent quiet T leaves:

- thick coherent reservoir;
- regular coherent sheet;
- regular thin material destruction layer;
- separated finite-scale fragmentation.

The remaining geometric T possibilities are reduced to

\[
 \boxed{
 T_{\rm irregular\ multiscale\ reach/curvature}
 \lor
 T_{\rm spatial/non-tight}
 \lor
 T_{\rm descriptive\ mix\ with\ material\ charge\ preserved}
 \lor
 T_{\rm return/recycling}.
 }
\]

The next useful audit is whether an unbounded multiscale reach hierarchy can avoid the derivative-capacity branch, and whether material return into a much smaller later core forces a scale-amplifying circulation mismatch.

---

## 13. Audit verdict

### NEW RESULT

\[
 \boxed{
 \text{separated circulation fragmentation}
 \Longrightarrow
 \mathfrak P_j\gtrsim d_j/r_j
 \asymp r_j^{-1/5}\to\infty.
 }
\]

### REMOVED AS INDEPENDENT T

Separated finite-scale fragmentation/microcomponents.

### STILL OPEN

- irregular multiscale reach/curvature with no bounded-overlap fixed-scale description;
- pure spatial export/non-tightness;
- descriptive mixing with material circulation preserved;
- material return/recycling into later smaller scales;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
