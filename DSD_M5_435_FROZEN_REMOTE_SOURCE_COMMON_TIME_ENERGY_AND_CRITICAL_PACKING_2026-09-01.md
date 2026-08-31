# DSD M5-435 — Common-time packing of frozen remote strain sources

Date: 2026-09-01

Status: **M5-434 CONVERTS EVERY SUFFICIENTLY REMOTE QUIET FIXED-FRACTION STRAIN SOURCE INTO A FROZEN PHYSICAL OLD-SHELL PACKET / A GEOMETRICALLY SEPARATED SUBSEQUENCE OF SUCH PACKETS CAN BE OBSERVED SIMULTANEOUSLY AT ONE LATE PHYSICAL TIME, SO ORDINARY KINETIC ENERGY BECOMES ADDITIVE WITHOUT SUMMING DIFFERENT TIME SLICES / THE RIGOROUS RESULT FORCES `SUM (R_n/r_n^(4/5))^5 < INFINITY` ON THE NON-ATOMIC FROZEN REMOTE LANE / EACH LOCALIZED PACKET INDIVIDUALLY HAS CRITICAL SIZE `~nu^2 K_n^4`, BUT A CUMULATIVE GLOBAL `dot H^(1/2)` LOWER BOUND REQUIRES A SEPARATE UNIFORM ALMOST-ORTHOGONALITY THEOREM FOR THE SCALE-DEPENDENT BOGOVSKII LOCALIZATION OPERATORS AND IS THEREFORE RETAINED ONLY AS A CANDIDATE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Frozen remote-source sequence

Consider a sequence of first-hitting stages `j_n` carrying fixed-fraction remote strain sources with target natural scales

\[
r_n:=r_{j_n}
\]

and source radii

\[
R_n\gg r_n.
\]

Assume the lane avoids the derivative/forcing throughput exits of M5-434. Then each source produces a compact natural-band packet that is not strongly forgotten before `T_*`.

The formation lower bound is

\[
\boxed{
\|P_{R_n}f_n(t_{j_n})\|_2^2
\ge c_0\nu^2\frac{R_n^5}{r_n^4}.
}
\]

The frozen-conveyor estimate implies that after the packet is sufficiently old its total future relative variation is small. Passing to a tail if necessary, fix a retained fraction `0<c_f<1` such that for all later times before `T_*`,

\[
\boxed{
\|P_{R_n}f_n(t)\|_2
\ge c_f\|P_{R_n}f_n(t_{j_n})\|_2.
}
\]

If this fails, M5-434 routes the stage to strong derivative/forcing throughput rather than the frozen lane.

---

## 2. Select geometrically separated physical source radii

On the non-atomic remote branch M5-433 gives

\[
R_n\to0.
\]

Choose a subsequence, still denoted `R_n`, such that

\[
\boxed{
R_{n+1}\le\lambda R_n
}
\]

for a fixed sufficiently small `0<lambda<1` depending only on the fixed annular support aspect ratios.

Because center nesting gives

\[
|X_{j_n}-X_*|\lesssim r_n=o(R_n),
\]

the corresponding physical source annuli are, for all sufficiently late `n`, contained in mutually disjoint annular regions centered at `X_*` after enlarging the fixed cutoffs by a harmless constant.

The later motion of the common tracked center is only `O(r_n)` from the formation time onward and is therefore also `o(R_n)`.

Thus the selected frozen packets remain spatially separated in physical space.

---

## 3. Observe finitely many frozen sources at one common time

Fix `N` and choose a time immediately after the formation of the `N`th selected packet but before `T_*`.

By the frozen-lane assumption, packets `1,...,N` are all still present at that same physical time.

The compact solenoidal localization satisfies a fixed estimate

\[
\|f_n(t)\|_2
\le C_B\|u(t)\|_{L^2(\widetilde A_n)},
\]

where the enlarged annuli `\widetilde A_n` remain disjoint after the geometric separation selection.

Therefore

\[
\begin{aligned}
E_0
&\ge\|u(t)\|_2^2\\
&\ge c_B\sum_{n=1}^N\|f_n(t)\|_2^2\\
&\ge c_B\sum_{n=1}^N\|P_{R_n}f_n(t)\|_2^2.
\end{aligned}
\]

Using frozen persistence and the formation lower bound,

\[
\boxed{
E_0
\ge
c_E\nu^2
\sum_{n=1}^N
\frac{R_n^5}{r_n^4}.
}
\]

Letting `N->infinity`,

\[
\boxed{
\sum_n
\frac{R_n^5}{r_n^4}
<\infty.
}
\]

This is a common-time energy packing theorem. No energy from different time slices is added.

---

## 4. Fifth-root saturation parameters are l5-summable

Define

\[
\boxed{
a_n:=\frac{R_n}{r_n^{4/5}}.}
\]

Then

\[
\frac{R_n^5}{r_n^4}=a_n^5.
\]

Hence

\[
\boxed{
\sum_n a_n^5
\le C\frac{E_0}{\nu^2}
<\infty.
}
\]

In particular,

\[
\boxed{a_n\to0.}
\]

M5-433 obtained this little-o conclusion from non-atomicity one shell at a time. M5-435 strengthens it on every geometrically separated frozen-source subsequence to a literal `ell^5` packing condition.

Thus a quiet non-atomic frozen remote conveyor must be not merely sub-fifth-root, but summably sub-fifth-root in the physical source stack.

---

## 5. Critical size of one localized frozen source

Because `P_{R_n}f_n` lies at frequency comparable to `R_n^-1`, its own homogeneous critical norm satisfies

\[
\|P_{R_n}f_n\|_{\dot H^{1/2}}^2
\asymp
R_n^{-1}\|P_{R_n}f_n\|_2^2.
\]

Therefore

\[
\boxed{
\|P_{R_n}f_n\|_{\dot H^{1/2}}^2
\ge
c_X\nu^2
\frac{R_n^4}{r_n^4}
=
c_X\nu^2K_n^4,
}
\]

where

\[
K_n:=\frac{R_n}{r_n}\to\infty.
\]

Thus every genuinely remote frozen source is individually a large critical localized object even though its physical kinetic energy may tend to zero.

This makes explicit the distinction

\[
\boxed{
\text{small physical energy}
\not\Rightarrow
\text{small localized scale-critical content}.
}
\]

---

## 6. Audit correction: cumulative global H1/2 packing is not yet automatic

It is tempting to use the separated frequency bands to write

\[
\|u(t)\|_{\dot H^{1/2}}^2
\stackrel{?}{\gtrsim}
\sum_n
\|P_{R_n}f_n(t)\|_{\dot H^{1/2}}^2.
\]

This is **not yet proved**.

The reason is that

\[
f_n=\chi_{R_n}u-b_{R_n}[u]
\]

is the output of a scale-dependent spatial cutoff plus Bogovskii correction. The packets `P_{R_n}f_n` are not literal orthogonal Fourier projections of the original global field `u`.

A cumulative global critical lower bound requires a separate vector-valued estimate of the schematic form

\[
\boxed{
\sum_n
\|P_{R_n}\mathcal L_{R_n}u\|_{\dot H^{1/2}}^2
\le C
\|u\|_{\dot H^{1/2}}^2,
}
\]

for the localized solenoidal operators `\mathcal L_R`, uniformly over geometrically separated phase-space cells.

Such an almost-orthogonality theorem is plausible but is not imported silently.

Therefore the previously suggested cumulative `dot H^(1/2)` stack is demoted to a **candidate next lemma**, not a derived result.

---

## 7. Why the rigorous l5 ledger still does not contradict a singular tower

The ordinary-energy packing is strong but scale-compatible.

For example, if along a geometric first-hitting subsequence

\[
R_n\asymp r_n^\alpha,
\qquad
\frac45<\alpha<1,
\]

then

\[
a_n^5
\asymp
r_n^{5\alpha-4},
\]

which is geometrically summable because `5\alpha-4>0`.

Thus the frozen sub-fifth-root conveyor remains a mathematically compatible critical escape at the present resolution.

---

## 8. Relation to the old frozen critical conveyor

The 2026-08-25 frozen-conveyor theorem began with an already formed historical critical tail and proved summable future variation.

The M5-433--435 chain now derives such a frozen stack directly from the need to source first-hitting strain:

\[
\boxed{
\text{remote strain payer}
\to
\text{source energy}
\to
\text{natural-band old-shell packet}
\to
\text{frozen packet or strong throughput}
\to
\text{common-time ordinary-energy stack}.
}
\]

This is a genuine connection between the formerly separate remote-source and historical-tail programs.

---

## 9. DSD audit

### Derived

- geometrically separated quiet frozen remote packets coexist at one late physical time;
- ordinary energy yields additive common-time packing;
- fifth-root saturation factors satisfy an `ell^5` condition;
- each localized natural-band source individually has critical size `>=c nu^2 K_n^4`.

### Conditional / next lemma

- cumulative global `dot H^(1/2)` packing of the Bogovskii-localized packets;
- any `L4_t dot H^(1/2)` consequence that depends on that cumulative lower bound.

### Firewall

- `ell^5` sub-saturation is not a contradiction;
- the critical norm is allowed to diverge near a hypothetical singularity;
- selected shells must be physically separated before ordinary-energy additivity is used;
- no fixed-volume material ancestry is assumed.

---

## 10. Updated quiet remote hard core

The only remote source lane not already routed to atom or strong throughput is now

\[
\boxed{
F_{sub5}^{frozen}:
\quad
\frac{R_n}{r_n}\to\infty,
\quad
\sum_n
\left(
\frac{R_n}{r_n^{4/5}}
\right)^5
<\infty,
}
\]

with a persistent natural-frequency physical shell stack.

This is the exact rigorously retained quiet conveyor for the final master audit.

---

## 11. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
