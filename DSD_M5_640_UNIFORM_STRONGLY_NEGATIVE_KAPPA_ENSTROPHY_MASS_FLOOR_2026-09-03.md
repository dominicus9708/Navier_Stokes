# DSD M5-640 — Uniform strongly-negative-kappa enstrophy mass floor

Date: 2026-09-03

Status: **INTERNAL QUANTITATIVE RAYLEIGH CONSEQUENCE / ON THE COMPACT CE-H HARD COMPONENT, THE UNIFORM BOUNDS `E<=Z_*`, `P>=p_*>0`, AND `H=integral kappa^2 |W|^2<=H_*` FORCE A FIXED POSITIVE AMOUNT OF ENSTROPHY TO LIVE ON A LEVEL SET UNIFORMLY SEPARATED FROM ZERO KAPPA. WITH `kappa_*:=p_*/(2Z_*)`, EVERY STATE SATISFIES `integral_{kappa<=-kappa_*}|W|^2 >= p_*^2/(4H_*)`. THUS THE NONZERO-KAPPA SHEATH FROM M5-639 CANNOT COLLAPSE TO ARBITRARILY WEAK NEAR-ZERO LEVELS; A STRONGLY NEGATIVE VOLUMETRIC POPULATION IS PRESENT AT EVERY RECURRENT STATE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Uniform CE-H inputs

On the retained compact hard component, the previous steps provide uniform constants

\[
E(\theta)=\int|W|^2dy\le Z_*<\infty,
\]

\[
P(\theta)=\int|\nabla W|^2dy\ge p_*>0,
\]

and, from the bounded second-derivative branch,

\[
H(\theta)=\int|\Delta W|^2dy\le H_*<\infty.
\]

On CE-H,

\[
\Delta W=\kappa W,
\]

so

\[
\boxed{H=\int\kappa^2|W|^2dy.}
\]

The Rayleigh identity is

\[
\boxed{P=\int(-\kappa)|W|^2dy.}
\]

---

## 2. Define a uniformly negative level threshold

Set

\[
\boxed{\kappa_*:=\frac{p_*}{2Z_*}>0.}
\]

Define

\[
A_-(\theta):=\{y:\kappa(y,\theta)\le-\kappa_*\}.
\]

On the complement,

\[
-\kappa<\kappa_*.
\]

Therefore

\[
\int_{A_-^c}(-\kappa)|W|^2dy
\le
\kappa_*E
\le
\frac{p_*}{2}.
\]

Since the full integral is at least `p_*`, we get

\[
\boxed{
\int_{A_-}(-\kappa)|W|^2dy
\ge\frac{p_*}{2}.
}
\]

---

## 3. Convert weighted negative budget to enstrophy mass

By Cauchy--Schwarz,

\[
\left(\int_{A_-}(-\kappa)|W|^2dy\right)^2
\le
\left(\int_{A_-}\kappa^2|W|^2dy\right)
\left(\int_{A_-}|W|^2dy\right).
\]

The first factor is bounded by `H_*`.

Hence

\[
\frac{p_*^2}{4}
\le
H_*\int_{A_-}|W|^2dy.
\]

Thus

\[
\boxed{
\int_{\{\kappa\le-\kappa_*\}}|W|^2dy
\ge
m_-:=\frac{p_*^2}{4H_*}>0.
}
\]

This bound holds uniformly at every state of the compact CE-H component.

---

## 4. Meaning for the zero-level skeleton branch

M5-639 proves that the exact zero-kappa persistent set has zero three-dimensional enstrophy measure.

M5-640 strengthens this dramatically:

not only must the volumetric enstrophy lie away from the zero-level skeleton, but a fixed amount must lie a fixed distance into the negative-kappa side.

Thus

\[
\boxed{
\text{persistent zero-kappa skeleton}
+
\text{uniform strongly-negative enstrophy sheath}.
}
\]

The sheath cannot degenerate to `kappa=-epsilon(theta)` with `epsilon->0` everywhere.

---

## 5. Relation to the all-power sign identity

M5-634 gives

\[
\int\kappa\rho^p<0
\qquad\forall p\ge2.
\]

M5-640 is a quantitative `p=2` strengthening using the second kappa moment.

It says the negative mean is supported by a nontrivial amount of strongly negative enstrophy, not merely by an arbitrarily small set with unbounded negative `kappa`.

---

## 6. Spatial localization

Because the compact branch has global `H^s` tail tightness, choose a fixed `R_-` so that

\[
\sup_{hull}\int_{|y|>R_-}|W|^2dy
<\frac{m_-}{2}.
\]

Then every state satisfies

\[
\boxed{
\int_{B_{R_-}\cap\{\kappa\le-\kappa_*\}}|W|^2dy
\ge\frac{m_-}{2}.
}
\]

Thus a fixed positive amount of strongly negative enstrophy is present in one fixed finite similarity core at every recurrent time.

This permits a coherent-packet extraction using the existing uniform derivative bounds.

---

## 7. Next target

Use the fixed-core mass floor and smooth compactness to extract a coherent packet with

\[
|W|\ge w_*>0,
\qquad
\kappa\le-\frac12\kappa_*<0,
\]

on a fixed ball.

On the relabeling zero-level branch, the sign of a negative kappa material label cannot cross zero, while its material vorticity flux obeys

\[
D_B\log|\phi|=\kappa<0.
\]

Therefore one material label cannot repeatedly carry a fixed-flux strongly-negative packet indefinitely. The expected next conclusion is a uniform coherent-packet turnover requirement.

---

## 8. Firewall

The uniform lower bound `P>=p_*` is inherited from the marked compact CE-H component/derivative floors; if final audit weakens that input to a merely positive time average, M5-640 must be correspondingly downgraded to a positive-density-in-time statement.

No contradiction is claimed from the mass floor alone.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]