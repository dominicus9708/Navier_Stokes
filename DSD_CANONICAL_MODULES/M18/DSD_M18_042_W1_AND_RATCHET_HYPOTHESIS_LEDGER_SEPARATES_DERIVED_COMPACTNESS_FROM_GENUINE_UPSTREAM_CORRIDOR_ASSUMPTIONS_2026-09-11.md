# M18-042 — W1 and ratchet hypothesis ledger separates derived compactness from genuine upstream corridor assumptions

**Date:** 2026-09-11  
**Status:** AUTHORITATIVE R1/R2 HYPOTHESIS LEDGER / DERIVED-VS-ASSUMED FIREWALL / UPSTREAM ROOT LIST

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-041 decomposed ROOT-CERT into gates R0--R5 and identified R1 (entry into W1) and R2 (entry into the bounded first-hitting ratchet lane) as upstream conditional gates.

The present module extracts the actual assumptions appearing in the retained W1/ratchet documents and classifies them as:

\[
\text{standard input},
\quad
\text{derived},
\quad
\text{case-survivor condition},
\quad
\text{external theorem dependency},
\quad
\text{unclosed complement}.
\]

The main gain is that several conditions often spoken of as 'W1 assumptions' are in fact downstream consequences of a smaller core hypothesis set.

## 2. W1 definition recovered from the repository

The W1 endpoint document records the survivor as having

\[
\boxed{
\sup_s\|U(s)\|_{L^{3,\infty}}<\infty,
}
\]

\[
\boxed{
\sup_{R,s}
\Gamma_R(s)
\le\Gamma_*<\infty,
}
\]

with

\[
\Gamma_R
:=
\frac{R\|\nabla(U-m_R)\|_{L^2(A_R^*)}}
{\|U-m_R\|_{L^2(A_R^*)}},
\]

plus:

- bounded relative Campanato;
- bounded normalized enstrophy;
- a nonzero recurrent core;
- local analytic compactness inherited from the first-hitting/ancient corridor.

This package should not be treated as a list of mutually independent hypotheses.

## 3. Bounded relative Campanato is derived on the bounded-Z Type-I center-nested lane

The repository proves:

\[
\boxed{
\text{bounded normalized enstrophy}
+
\text{Type-I amplitude}
+
\text{center nesting}
\Longrightarrow
\text{no relative-Campanato escalation},
}
\]

using finite physical energy and the standard interior pointwise-Type-I \(\Rightarrow\) scale-invariant local-energy theorem.

Hence bounded relative Campanato is **not** an additional primitive assumption once those upstream conditions are certified.

Classification:

\[
\boxed{
H_{Camp}:\ \text{DERIVED, conditional on }H_Z+H_I+H_C+\text{external Type-I local-energy theorem}.}
\]

## 4. Global Lp tightness and precompactness are derived inside W1

From bounded Campanato and bounded shell derivative ratio, W1 proves

\[
\|U\|_{L^p(A_R)}
\lesssim
R^{3/p-1},
\qquad
3<p\le6,
\]

and therefore

\[
\boxed{
\sup_s\|U(s)\|_{L^p(\mathbb R^3)}<\infty,
\qquad 3<p\le6,
}
\]

with uniform tails and global \(L^p\) precompactness after local analytic compactness.

Thus these properties are consequences, not entry hypotheses.

Classification:

\[
\boxed{H_{Lp}:\ \text{DERIVED INSIDE W1}.}
\]

## 5. Core upstream condition H_Z — bounded normalized enstrophy

The bounded-Z condition has the form

\[
\boxed{
Z_D(t)
:=
\int|\Omega_D|^2dY
\le Z_+.
}
\]

It is used to obtain Type-I velocity control and ultimately the local-energy/Campanato bound.

Finite physical kinetic energy does not by itself imply a uniform bound on this dynamically normalized vorticity enstrophy.

Therefore bounded Z is a genuine corridor condition unless a prior branch theorem proves its complement impossible or costly.

Classification:

\[
\boxed{H_Z:\ \text{CASE-SURVIVOR CONDITION; GLOBAL COMPLEMENT NOT CERTIFIED HERE}.}
\]

Complement:

\[
\boxed{Z_D\to\infty.}
\]

This must remain an upstream root until independently closed/routed.

## 6. Core upstream condition H_I — Type-I amplitude

The retained corridor uses

\[
\boxed{
(T_*-t)\|\omega(t)\|_\infty
\le K_I.
}
\]

This is a genuine Type-I restriction on the blow-up rate.

A hypothetical Navier--Stokes singularity is not known a priori to satisfy it; Type-II behavior is a logically separate possibility.

Classification:

\[
\boxed{H_I:\ \text{GENUINE CASE SPLIT / TYPE-II COMPLEMENT REQUIRES CLOSURE}.}
\]

Complement:

\[
\boxed{
(T_*-t)\|\omega(t)\|_\infty
\to\infty
\text{ along a sequence}.}
\]

## 7. Core upstream condition H_C — center nesting / no center turnover

The Campanato exclusion uses tracked first-hitting centers satisfying

\[
\boxed{
|X_j-x_*|\lesssim r_j.
}
\]

This ensures normalized remote balls correspond to physical balls centered at the same singular point.

Failure is a center-turnover / migration branch, not a harmless coordinate choice.

Classification:

\[
\boxed{H_C:\ \text{GENUINE CASE-SURVIVOR CONDITION}.}
\]

The repository contains extensive turnover/migration analyses, but M18-042 does not certify that every possible center-turnover complement is globally closed before W1 entry.

## 8. Core upstream condition H_F — bounded shell derivative frequency

W1 retains

\[
\boxed{
\Gamma_R\le\Gamma_*.
}
\]

The complement is a high-frequency branch \(H_{freq}\).

Repository documents route several weak-L3/tail failures into this high-frequency channel and analyze active remote H via Campanato commutator decay.

Therefore bounded frequency is best classified as a **case-survivor condition produced by a split**, not an unexplained raw assumption.

However global R1 completeness still requires the high-frequency complement to be certified closed for every upstream state to which the split is applied.

Classification:

\[
\boxed{H_F:\ \text{CASE SPLIT; COMPLEMENT HAS INTERNAL ROUTES BUT GLOBAL COVERAGE REQUIRES RE-AUDIT}.}
\]

## 9. Core upstream condition H_W — bounded weak-L3 endpoint

W1 assumes

\[
\boxed{
\sup_s\|U(s)\|_{L^{3,\infty}}<\infty.
}
\]

The repository explicitly routes residual weak-L3 escalation, on the bounded-Campanato corridor, into derivative-frequency/H2-tail alternatives.

Thus bounded weak-L3 is likewise a retained endpoint of a split rather than an isolated hypothesis.

But the routing depends on the corridor hypotheses used in that argument.

Classification:

\[
\boxed{H_W:\ \text{CASE-SURVIVOR CONDITION; ROUTING IS CORRIDOR-CONDITIONAL}.}
\]

## 10. Core upstream condition H_R — nonzero recurrent core

The W1 function-space upgrade assumes a nonzero recurrent core and uses local analytic compactness to pass to a compact recurrent/minimal Leray orbit.

A nonzero core is essential to prevent the omega-limit from collapsing to zero.

The existence of such a recurrent core is not a generic consequence of bounded weak-L3 alone; it depends on the first-hitting/omega-limit selection architecture.

Classification:

\[
\boxed{H_R:\ \text{EXTRACTION/RECURRENCE CERTIFICATE REQUIRED}.}
\]

Its complement may correspond to vanishing-core / escape-to-infinity / tail-only behavior and must be separately routed.

## 11. Ratchet-lane condition H_L — controlled normalized stage lengths

M5-475 assumes inherited first-hitting stage lengths satisfy

\[
\boxed{
0<L_-\le L_k\le L_+<\infty.
}
\]

This gives geometric backward times

\[
|\tau_m|\asymp q^m
\]

and underlies the Type-I decay and second-generation record geometry.

If stage lengths collapse to zero or diverge, the geometric ratchet clock changes qualitatively.

Classification:

\[
\boxed{H_L:\ \text{GENUINE R2 CORRIDOR CONDITION}.}
\]

Complement:

\[
L_k\to0
\quad\text{or}\quad
L_k\to\infty
\]

along a subsequence must be audited rather than absorbed silently.

## 12. Ratchet-lane condition H_G — persistent first-hitting genealogy

The M5-475--478 construction uses a retained sequence of first-hitting generations with coherent scale ratio

\[
W_{j-m}=q^{-m}W_j,
\qquad
r_{j-m}=q^{m/2}r_j,
\]

and a carrier that survives on each retained scale.

This is stronger than the existence of one blow-up sequence.

Classification:

\[
\boxed{H_G:\ \text{GENEALOGY/RECURRENCE CONDITION}.}
\]

Failure includes loss of carrier identity, scale skipping, branch termination, or noncoherent record selection.

## 13. External theorem dependency H_ext

The bounded-Campanato result imports the standard interior Type-I local-energy estimate for suitable weak solutions.

This is not an open Navier--Stokes theorem but an external dependency whose hypotheses must be matched exactly:

- suitable weak/local-energy class;
- correct singular point and cylinder;
- pointwise Type-I velocity bound in the required neighborhood.

Classification:

\[
\boxed{H_{ext}:\ \text{STANDARD EXTERNAL INPUT; HYPOTHESIS MATCHING MUST BE VERIFIED}.}
\]

## 14. Minimal primitive hypothesis set

After removing derived properties, the retained W1/ratchet route depends primarily on

\[
\boxed{
\{H_Z,H_I,H_C,H_F,H_W,H_R,H_L,H_G\}
}
\]

plus standard finite-energy/suitable-solution inputs and explicit external theorem matching.

Not all eight are independent: \(H_F,H_W\) are endpoints of internal case splits, while \(H_L,H_G\) belong specifically to the later R2 ratchet lane.

A useful grouping is

\[
\boxed{
\begin{aligned}
\text{amplitude/energy:}&\quad H_Z,H_I,\\
\text{center/domain:}&\quad H_C,\\
\text{remote-tail/frequency:}&\quad H_F,H_W,\\
\text{recurrence/extraction:}&\quad H_R,H_G,\\
\text{clock regularity:}&\quad H_L.
\end{aligned}
}
\]

## 15. Upstream complement tree

The current root-completeness problem can therefore be represented by the complement menu

\[
\boxed{
\begin{aligned}
G_{R1/R2\ failure}
\Longrightarrow{}&
G_{Z\text{-escalation}}\\
&\lor G_{Type\text{-}II}\\
&\lor G_{center\ turnover}\\
&\lor G_{high\ remote\ frequency}\\
&\lor G_{weak\text{-}L3\ escalation}\\
&\lor G_{vanishing/escaping\ recurrent\ core}\\
&\lor G_{stage\text{-}length\ degeneration}\\
&\lor G_{first\text{-}hitting\ genealogy\ loss}.
\end{aligned}
}
\]

Some of these have extensive internal analyses, but their **global exhaustiveness and closure** are not yet certified by one authoritative root map.

## 16. What is already derived and need not be re-proved

Once the primitive corridor conditions hold, the following should not be counted as separate root assumptions:

- bounded relative Campanato;
- global \(L^p\) bounds/tightness for \(p>3\);
- global \(L^p\) precompactness of the W1 orbit;
- Type-I backward decay on the ratchet ancient element;
- finite ancient palinstrophy;
- nontrivial second-generation carrier at \(s=-1\).

These are downstream results under their stated hypotheses.

## 17. Audit verdict

### Certified

1. The W1 package contains fewer primitive assumptions than its final description suggests.
2. Relative Campanato and global \(L^p\) precompactness are derived inside the bounded-Z Type-I center-nested bounded-frequency lane.
3. Type-I, bounded normalized enstrophy, center nesting, recurrence, and stage regularity are genuine upstream corridor conditions.
4. W1 weak-L3/frequency bounds are endpoints of case splits whose global complement closure must be checked rather than treated as axioms.
5. The R1/R2 completeness problem now has an explicit finite complement menu.

### Not certified

1. Closure of all eight complement families in one global proof map.
2. Universal Type-I behavior.
3. Universal bounded normalized enstrophy.
4. Universal center nesting or ratchet-stage regularity.
5. Global 3D Navier--Stokes regularity.

## 18. Next target

M18-043 should prioritize the complement menu by asking which branches are already substantially closed in the repository and which are truly Millennium-level open.

The first candidates to audit are:

\[
G_{Type\text{-}II},
\quad
G_{Z\text{-escalation}},
\quad
G_{center\ turnover},
\]

because failure of any of these occurs **before** the sophisticated W1 endpoint machinery and can invalidate the entire downstream route.