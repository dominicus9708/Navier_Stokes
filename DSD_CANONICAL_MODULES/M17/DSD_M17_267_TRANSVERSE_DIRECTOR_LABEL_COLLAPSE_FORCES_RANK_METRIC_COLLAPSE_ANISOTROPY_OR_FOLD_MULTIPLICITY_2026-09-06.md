# DSD M17-267 — Transverse director-label collapse forces rank/metric collapse, anisotropy, or fold multiplicity

Date: 2026-09-06  
Canonical ID: **M17-267**

Status: **DIRECTOR-LABEL COLLAPSE CLASSIFICATION / M17-266 SHOWS THAT LONG-FIBER DECOMPACTIFICATION WITH BOUNDED DIRECTOR JACOBIAN FORCES THE TRANSVERSE DIRECTOR-LABEL MEASURE TO COLLAPSE. ON A REGULAR RELATIVE-THICK RANK-2 FIBER TUBE, CHOOSE A FIXED-AREA TRANSVERSE SECTION `Sigma_j` AND APPLY THE TWO-DIMENSIONAL AREA FORMULA TO `xi|Sigma_j`. IF THE MAPPING MULTIPLICITY STAYS BOUNDED, COLLAPSE OF THE DIRECTOR IMAGE AREA FORCES `int_Sigma J_xi ->0`. ON A FIXED-AREA SECTION, A FIXED FRACTION THEN HAS SMALL `J_xi=s1 s2`. EITHER THE LARGE SINGULAR VALUE `s1` ALSO COLLAPSES, GIVING DIRECTOR-METRIC/RANK DEGENERATION, OR `s1` STAYS NONDEGENERATE WHILE `s2->0`, FORCING CONDITION-NUMBER ANISOTROPY TO DIVERGE. IF THE AREA-FORMULA MULTIPLICITY DOES NOT STAY BOUNDED, THE EXIT IS DIRECTOR FOLD/MULTIPLICITY ESCALATION. THUS TRANSVERSE LABEL COLLAPSE IS NOT A NEW UNTYPED ENDPOINT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-266

The unresolved bounded-Jacobian long-fiber lane satisfies

\[
\boxed{
\Phi_J(\mathcal F_j)\to0
}
\]

for the family of director fibers carrying the retained critical coefficient population.

Interpret this locally on a regular Rank-2 fiber tube by choosing a smooth transverse section

\[
\Sigma_j
\]

meeting the retained fibers once per local sheet.

Assume the relative-thick compact corridor gives

\[
\boxed{
0<A_-\le |\Sigma_j|\le A_+<\infty.
}
\]

If such a transverse section degenerates, retain a thin/interface exit instead.

---

## 2. Director map on the transverse section

Because `Sigma_j` is transverse to

\[
\ker D\xi,
\]

the restricted map

\[
\xi_j:=\xi|_{\Sigma_j}:\Sigma_j\to S^2
\]

has two-dimensional Jacobian

\[
\boxed{
J_{\xi,j}=s_{1,j}s_{2,j}
}

on the regular Rank-2 set, with

\[
s_{1,j}\ge s_{2,j}>0.
\]

The director metric is

\[
|\nabla\xi|^2=s_1^2+s_2^2
\]

and the condition number is

\[
\mathcal K_\xi=\frac{s_1}{s_2}.
\]

---

## 3. Area formula with multiplicity

For almost every director value `eta` in the image, let

\[
N_j(\eta)
\]

be the number of local transverse preimages on `Sigma_j`.

The area formula gives

\[
\boxed{
\int_{\Sigma_j}J_{\xi,j}\,dA
=
\int_{\xi_j(\Sigma_j)}N_j(\eta)\,dA_\eta.
}
\]

Split according to multiplicity.

---

## 4. Unbounded multiplicity is a fold exit

If

\[
\boxed{
\|N_j\|_{L^\infty(\xi_j(\Sigma_j))}\to\infty,
}
\]

retain

\[
\boxed{G_{director\ fold/multiplicity\ escalation}.}
\]

This represents increasing numbers of transverse sheets mapping to the same director labels.

It is not identified automatically with rank loss.

---

## 5. Bounded multiplicity forces small average Jacobian

Assume instead

\[
\boxed{N_j(\eta)\le N_*<\infty}
\]

uniformly.

If the transverse director image/label measure collapses,

\[
\boxed{
|\xi_j(\Sigma_j)|\to0,
}
\]

then the area formula gives

\[
\int_{\Sigma_j}J_{\xi,j}dA
\le
N_*|\xi_j(\Sigma_j)|
\to0.
\]

Because

\[
|\Sigma_j|\ge A_->0,
\]

we obtain

\[
\boxed{
\fint_{\Sigma_j}J_{\xi,j}dA\to0.
}
\]

---

## 6. Fixed-fraction small-J set

Choose any sequence

\[
\varepsilon_j\downarrow0
\]

slowly enough that

\[
\frac{1}{\varepsilon_j}
\int_{\Sigma_j}J_{\xi,j}dA
\to0.
\]

By Markov,

\[
\left|
\{J_{\xi,j}>\varepsilon_j\}
\right|
\le
\varepsilon_j^{-1}
\int_{\Sigma_j}J_{\xi,j}dA
=o(1).
\]

Therefore a fraction tending to one of the fixed-area transverse section satisfies

\[
\boxed{
J_{\xi,j}=s_{1,j}s_{2,j}\le\varepsilon_j.
}
\]

---

## 7. Small Jacobian splits into metric collapse or anisotropy

Fix a small threshold `delta>0`.

On the small-J set, split into

### Metric/rank weakening

\[
\boxed{s_{1,j}\le\delta.}
\]

Since

\[
s_{2,j}\le s_{1,j},
\]

we get

\[
|\nabla\xi|^2
=s_1^2+s_2^2
\le2\delta^2.
\]

If a fixed fraction enters this branch for every `delta->0`, the director differential collapses and the Rank-2 tangent degenerates.

Retain

\[
\boxed{G_{director\ metric/rank\ collapse}.}
\]

### Anisotropy

On the complementary set

\[
s_{1,j}>\delta
\]

while

\[
s_{1,j}s_{2,j}\le\varepsilon_j.
\]

Then

\[
s_{2,j}
\le\frac{\varepsilon_j}{\delta}
\]

and

\[
\boxed{
\mathcal K_{\xi,j}
=\frac{s_{1,j}}{s_{2,j}}
\ge\frac{\delta^2}{\varepsilon_j}
\to\infty.
}
\]

Thus the complementary fixed-fraction branch has divergent director anisotropy.

---

## 8. Correct label-collapse gate

Combining Sections 4--7,

\[
\boxed{
G_{transverse\ director\text{-}label\ collapse}
\Longrightarrow
G_{director\ fold/multiplicity\ escalation}
\lor
G_{director\ metric/rank\ collapse}
\lor
G_{director\ anisotropy}.
}
\]

This converts the M17-266 label-collapse residual into already recognizable director geometric currencies.

---

## 9. Return to earlier M17 gates

The three outputs already have downstream structure:

1. `director anisotropy` enters M17-215/216/218 and the corrected M17-219/220 ancestry/spectral gates;
2. `metric/rank collapse` returns to the explicit rank/interface boundary;
3. `fold/multiplicity escalation` returns to the director-fold/interface complexity lane and requires its own multiplicity budget if it persists.

Thus only the multiplicity escalation may remain genuinely unclosed after this reduction; label collapse itself does not.

---

## 10. Scope firewall

This module assumes a regular transverse section of fixed area.

If the section itself becomes thin, fragments, loses transversality, or exits the Rank-2 chart, retain

\[
G_{thin/interface/rank}.
\]

No global trivialization of the fiber bundle is assumed.

---

## 11. Updated long-fiber frontier

Combining M17-266/267,

\[
\boxed{
G_{fiber\ length\ decompactification}
\Longrightarrow
G_{director\ Jacobian/metric\ escalation}
\lor
G_{director\ fold/multiplicity\ escalation}
\lor
G_{director\ metric/rank\ collapse}
\lor
G_{director\ anisotropy}
\lor
G_{thin/interface}.
}
\]

The next narrow unresolved director target is repeated fold/multiplicity escalation after the existing anisotropy and rank gates are applied.

---

## 12. DSD audit

1. The two-dimensional area formula is applied only on transverse regular sections.
2. Bounded multiplicity and unbounded multiplicity are separated explicitly.
3. Small Jacobian is not equated directly with rank loss; anisotropy is retained as the alternative.
4. The fixed section area lower bound is an explicit relative-thickness hypothesis.
5. Fold multiplicity remains an open geometric payer unless another module closes it.
6. Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
