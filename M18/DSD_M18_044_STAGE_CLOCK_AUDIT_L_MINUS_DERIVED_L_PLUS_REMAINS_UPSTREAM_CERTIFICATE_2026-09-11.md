# DSD M18-044 — Stage-clock audit: `L_-` is derived, `L_+` remains an upstream corridor certificate

Date: 2026-09-11

Status: **ROOT-CERT / FIRST-HITTING CLOCK AUDIT. THE LOWER NORMALIZED STAGE LENGTH IS NOT AN INDEPENDENT ASSUMPTION: FINITE FIRST-HITTING AMPLIFICATION PLUS A BOUNDED NORMALIZED STRAIN CEILING FORCES A POSITIVE LOWER CLOCK. THE UPPER STAGE-LENGTH CEILING `L_+`, HOWEVER, IS IMPORTED BY THE LATE W1/RATCHET NOTES FROM THE PRE-EXISTING NON-H/T RECURRENT CORRIDOR. THUS THE GENUINE CLOCK-COMPLETENESS OBLIGATION IS AN UPPER-CLOCK CERTIFICATE OR A COMPLETE ROUTING OF ITS FAILURE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Clock notation

Let

\[
W_{j+1}=qW_j,
\qquad q>1,
\]

and let

\[
L_j:=\int_{t_j}^{t_{j+1}}\overline W(t)\,dt
\]

be the dynamically normalized first-hitting stage length.

The late ancient/ratchet modules often use

\[
0<L_-\le L_j\le L_+<\infty.
\]

The present audit asks which side is derived and which side is still a corridor input.

---

## 2. The lower clock is forced by amplification

The vorticity maximum satisfies the standard growth estimate

\[
\frac{d}{dt}\log\overline W(t)
\le \|S(t)\|_\infty
\]

at differentiability times. Therefore one first-hitting amplification gives

\[
\log q
\le
\int_{t_j}^{t_{j+1}}\|S(t)\|_\infty\,dt.
\]

On a bounded normalized strain corridor,

\[
\|S(t)\|_\infty\le B_+\overline W(t),
\]

so

\[
\boxed{
\log q\le B_+L_j.
}
\]

Hence

\[
\boxed{
L_j\ge\frac{\log q}{B_+}>0.
}
\]

Thus `L_-` is not a primitive datum.

This agrees with the earlier stage-lower-length elimination module, which already removed `L_-` as an independent parameter.

---

## 3. Two-sided physical clock once an upper ceiling exists

During one first-hitting stage,

\[
W_j\le\overline W(t)\le qW_j.
\]

Define

\[
\tau_j:=W_j(t_{j+1}-t_j).
\]

Then

\[
\tau_j\le L_j\le q\tau_j.
\]

Therefore, if a uniform upper ceiling

\[
L_j\le L_+
\]

is available, one obtains

\[
\frac{1}{q}\frac{\log q}{B_+}
\le
\tau_j
\le L_+.
\]

Consequently the first-hitting clock is genuinely parabolic and the later exact ancestry formulas follow.

In particular, with

\[
\Theta_j:=W_j(T^*-t_j),
\]

one has

\[
\Theta_j
=
\sum_{n=0}^{\infty}q^{-n}\tau_{j+n},
\]

and hence fixed positive upper/lower bounds on `Theta_j`, provided the upper clock is certified.

This yields the known bounded Leray-clock defect

\[
s_j=j\log q+O(1).
\]

---

## 4. Provenance of `L_+`

The late modules do not derive `L_+` from the lower clock identity itself.

The sliding-history remaining-time module explicitly begins with the pre-existing non-H/T recurrent corridor assumption

\[
0<L_-\le L_k\le L_+<\infty
\]

and then derives

\[
T^*-t_j
\le
\frac{L_+}{1-q^{-1}}W_j^{-1}.
\]

Thus the remaining-time compression argument is downstream of the upper-clock certificate.

Likewise the first-hitting/Leray coboundary module imports the same two-sided stage corridor and does not independently close the `L_j\to\infty` alternative.

Therefore

\[
\boxed{
L_+
\text{ is a surviving upstream certificate, not a consequence of the late clock algebra.}
}
\]

---

## 5. Correct branch-completeness split

The stage-clock question should no longer be written as a generic two-sided degeneration

\[
L_j\to0
\lor
L_j\to\infty.
\]

The first alternative is already excluded whenever the normalized strain ceiling remains finite.

The correct split is

\[
\boxed{
\text{bounded normalized strain}
\Longrightarrow
L_j\ge c(q,B_+)>0,
}
\]

and then

\[
\boxed{
L_j\le L_+<\infty
\quad\lor\quad
L_j\to\infty\text{ along a subsequence}.
}
\]

Thus only upper-clock failure is a genuine independent escape at this level.

---

## 6. What upper-clock failure means structurally

If

\[
L_j
=
\int_{t_j}^{t_{j+1}}\overline W(t)\,dt
\to\infty,
\]

while the stage still only amplifies the record level by the fixed factor `q`, then one cannot interpret this as merely 'more time'.

It means that the stage accumulates arbitrarily large normalized vorticity-time action before the next record threshold is reached.

A complete ROOT-CERT argument must therefore do one of the following:

1. prove a universal upper bound on `L_j` on every branch not already typed as H/T/remote/Type-II;
2. or show that `L_j\to\infty` forces one of those typed exits.

Until that routing is explicit, the late W1/ratchet ancestry package remains conditional on the upper-clock corridor.

---

## 7. Dependency consequence

The modules depending on the two-sided clock include, among others,

- backward Type-I decay of the marked ancient element;
- geometric record times `|\tau_m|\asymp q^m`;
- second-generation blow-down normalization;
- annular ancestry ledgers and bounded-overlap genealogy;
- first-hitting/Leray clock locking;
- remaining-time compression for historical shells.

These conclusions remain valid on the certified upper-clock corridor.

They must not be promoted to arbitrary singular histories before the upper-clock complement is routed.

---

## 8. Updated ROOT-CERT clock gate

The clock component of ROOT-CERT is therefore

\[
\boxed{
\text{CLOCK-CERT}
=
\text{bounded normalized strain}
+
\bigl(
\text{uniform upper stage clock}
\lor
\text{typed upper-clock exit}
\bigr).
}
\]

The lower stage clock no longer appears as an independent premise.

This reduces the number of primitive corridor assumptions and prevents double-counting the same amplification information.

---

## 9. Next target

Audit the origin of the finite upper stage clock and test whether

\[
L_j\to\infty
\]

can be converted quantitatively into

\[
\text{Type-II/remote activity}
\lor
\text{critical derivative action}
\lor
\text{turnover/export}
\lor
\text{another already typed root}.
\]

This has higher ROOT-CERT priority than adding another late CE-H derivative payer.

---

## 10. Status

\[
\boxed{
L_-\text{ IS DERIVED; }L_+\text{ REMAINS AN UPSTREAM CERTIFICATE OR ROUTING OBLIGATION.}
}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
