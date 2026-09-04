# DSD M17-085 — A decaying pure-kernel line component must contain a finite peak; the noncritical tail is not an independent survivor

Date: 2026-09-04
Canonical ID: **M17-085**

Status: **INTERNAL RANK-2 COVERAGE CORRECTION / M17-081 RESTORED A NONCRITICAL/ASYMPTOTIC PURE-KERNEL TAIL BECAUSE M17-079--080 REQUIRE A FINITE REGULAR LINE MAXIMUM. HOWEVER, ON ANY CONNECTED VORTEX-LINE COMPONENT OF `rho>0` WHOSE TWO ENDS BOTH HAVE `rho->0` (FINITE ZERO-SET ENDS OR INFINITE DECAYING ENDS), CONTINUITY FORCES A POSITIVE FINITE MAXIMUM. AT SUCH A POINT `g=D_xi log rho=0` AND `C=D_xi g<=0`. IF `C<0`, THE COMPONENT ENTERS THE M17-079--080 UNIFIED MAXIMUM MARGIN DIRECTLY. IF `C=0`, ANALYTICITY IMPLIES A FINITE EVEN-ORDER DEGENERATE MAXIMUM UNLESS `rho` IS LINEWISE CONSTANT TO INFINITE ORDER, WHICH WOULD CONTRADICT A NONZERO DECAYING COMPONENT. THUS THE M17-039 ASYMPTOTIC-CONFORMAL `d<0, d->0^-` PROFILE MAY EXIST AS END GEOMETRY BUT CANNOT BY ITSELF BE A COMPLETE NONCRITICAL NON-INTERFACE SURVIVOR. THE GENUINE COVERAGE EXITS ARE NOW: REGULAR MAXIMUM, FINITE-ORDER DEGENERATE MAXIMUM, A NONDECAYING/RECURRENT LINE END, OR RANK/ZERO/INTERFACE TERMINATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Vortex-line component

Work on the pure-kernel Rank-2 branch in a connected active component where

\[
\rho=|W|>0.
\]

Let `s` be arclength along an integral curve of the unit vortex direction `xi` and let

\[
I=(a,b)
\]

be one connected line component of the active set.

The endpoints may be finite or infinite.
Assume the component has decaying/zero ends:

\[
\boxed{
\lim_{s\to a^+}\rho(s)=0,
\qquad
\lim_{s\to b^-}\rho(s)=0.
}
\]

This includes a complete two-ended decaying line as well as a component ending on the vorticity zero set at finite arclength.

---

## 2. A positive finite maximum must exist

Choose any interior point `s_0`.
Since

\[
\rho(s_0)>0,
\]

set

\[
\varepsilon=\frac12\rho(s_0)>0.
\]

By the two endpoint limits there exist

\[
a<s_-<s_0<s_+<b
\]

such that

\[
\rho(s)<\varepsilon
\]

near both component ends outside `[s_-,s_+]`.

On the compact interval `[s_-,s_+]`, continuity gives a maximum at some `s_*`.
Because `rho(s_0)>2 epsilon`, this maximum is strictly positive and is also the global maximum on the whole component.
Therefore

\[
\boxed{
\exists s_*\in(a,b):
\quad
\rho(s_*)=\max_I\rho>0.
}
\]

Thus a two-ended decaying active line component cannot avoid a finite linewise amplitude peak.

---

## 3. Critical data at the peak

Define

\[
\boxed{
g:=D_\xi\log\rho.}
\]

At the peak,

\[
D_\xi\rho=0,
\]

so

\[
\boxed{g(s_*)=0.}
\]

Also

\[
D_\xi^2\rho(s_*)\le0.
\]

Because `g=0` there,

\[
D_\xi g
=\frac{D_\xi^2\rho}{\rho}-g^2
=\frac{D_\xi^2\rho}{\rho}.
\]

Hence

\[
\boxed{
C:=D_\xi g\le0.
}
\]

The peak therefore splits into a regular or degenerate critical class.

---

## 4. Regular maximum enters M17-079--080

If

\[
\boxed{C<0,}
\]

then the maximum is exactly the regular line maximum assumed in M17-079.
The unified compensation margin is

\[
\boxed{
\mathcal M_{R2}
=C+rD_ks-\Theta D_\xi q,
}
\]

and sub-Riccati survival requires

\[
\boxed{\mathcal M_{R2}>0.}
\]

M17-080 then gives the weighted moving-margin equation

\[
\boxed{
D_{max}N_{R2}
=-\frac32N_{R2}
+|a|\mathcal R_{R2}
+v_{rel}D_\xi N_{R2}.
}
\]

Therefore every decaying line component with a regular peak is already inside the existing Rank-2 maximum firewall.

---

## 5. Degenerate maximum is finite order under analyticity

Suppose instead

\[
\boxed{C=0.}
\]

Then the second line derivative vanishes at the maximum.
Because the retained smooth hard branch is analytic, restrict `rho` to the analytic vortex line near `s_*`.

If every line derivative vanished at `s_*`, analyticity would make `rho` locally constant along the connected line and then, by analytic continuation on that component, incompatible with the assumed nonzero peak and two decaying ends.

Therefore there is a finite first nonzero derivative order.
At a local maximum it must be even:

\[
\boxed{
2r\ge4,
\qquad
D_\xi^j\rho(s_*)=0\ (1\le j<2r),
\qquad
D_\xi^{2r}\rho(s_*)<0.
}
\]

Thus the only peak not covered by M17-079 is a finite-order degenerate maximum, not a genuinely noncritical tail.

---

## 6. Oscillatory tails also contain finite maxima

M17-039 retained an oscillatory-tail firewall with infinitely many linewise amplitude reversals.
Every reversal sequence containing rises and falls has local maxima.
Each such maximum again satisfies

\[
g=0,
\qquad
C\le0.
\]

Hence an oscillatory tail produces an infinite sequence of either

1. regular M17-079 maxima; or
2. finite-order degenerate maxima.

It does not avoid the critical network.
What remains difficult is uniform control of the degeneracy order and the moving sequence of critical points.

---

## 7. Reinterpret the M17-039 asymptotic-conformal tail

M17-039 showed that on a monotone decreasing orthogonal tail with

\[
d<0,
\]

one may have

\[
\boxed{
d(s)\to0^-}
\]

as

\[
\rho(s)\to0.
\]

This remains correct.
M17-085 changes only its branch status.

Such a tail is an **end geometry** attached to the rest of its connected vortex-line component.
If the opposite end also decays/terminates at `rho=0`, the component contains a finite peak somewhere between the ends.
Therefore

\[
\boxed{
R_{d<0}^{asym-conf}
\text{ is not by itself a complete noncritical survivor.}
}
\]

It must be attached to a regular/degenerate peak or to a different endpoint exit.

---

## 8. Exact endpoint split when no finite peak is available

Contrapositively, if a connected positive line component contains no finite linewise maximum, then the two-ended decay hypothesis must fail.
At least one end must enter one of the following classes:

\[
\boxed{
R_{end}^{nondecay/recurrence}
\ \lor\
T_{rank/zero/interface}
\ \lor\
T_{line-chart/completeness}.
}
\]

For example, an infinite end may fail to approach zero, may recurrently revisit an active compact region, or the pure-kernel/rank chart may terminate before a two-ended active component is obtained.

These are genuinely different exits from the asymptotically decaying tail of M17-039.

---

## 9. DSD analysis

The prior descriptor

\[
R_{2,tail}^{noncritical/asymptotic}
\]

mixed two different levels:

1. local end behavior of `rho,d`;
2. global critical structure of the connected line component.

M17-085 separates them.
The corrected descriptor chain is

\[
\boxed{
\text{decaying end geometry}
\to
\text{connected line component}
\to
\text{finite peak}
\to
\text{regular or finite-order degenerate maximum}.
}
\]

Thus end asymptotics do not remove the peak ledger.

---

## 10. DSD audit

### Audit A — using whole-space finite energy to force linewise decay
Rejected. M17-085 does not infer the endpoint limits from finite energy alone; it conditions only on the decaying/zero-end class already used in M17-039.

### Audit B — treating an asymptotic tail as the whole line
Corrected. It is only one end of a connected active component unless an interface/chart endpoint intervenes.

### Audit C — assuming every maximum is nondegenerate
Rejected. `C=0` is retained as a finite-order analytic degenerate maximum branch.

### Audit D — claiming analyticity gives a uniform degeneracy order globally
Not claimed. Compactness may later provide a uniform finite-order bound, but this module establishes only pointwise finiteness.

### Audit E — treating oscillatory tails as noncritical
Rejected. Oscillation creates infinitely many critical points; the unresolved issue is their degeneracy/turnover, not peak existence.

### Audit F — proof status
The Rank-2 coverage gap is reduced but not closed because degenerate maxima and nondecaying/recurrent endpoints remain.

---

## 11. Corrected Rank-2 pure-kernel frontier

For a connected pure-kernel active line component,

\[
\boxed{
R_{2,pk}
\Longrightarrow
R_{2,max}^{regular}
\ \lor\
R_{2,max}^{degenerate\ finite\ jet}
\ \lor\
R_{2,end}^{nondecay/recurrence}
\ \lor\
T_{2,pk}.
}
\]

On the two-ended decaying subclass,

\[
\boxed{
R_{2,pk}^{two-end\ decay}
\Longrightarrow
R_{2,max}^{regular}
\ \lor\
R_{2,max}^{degenerate\ finite\ jet}.
}
\]

The regular class is governed by M17-079--080.

---

## 12. Next target — Degenerate Maximum Finite-Jet Gate

The highest-value Rank-2 continuation is now the finite-order degenerate peak:

\[
C=D_\xi g=0,
\]

with the first negative even line derivative at order `2r>=4`.

The next calculation should derive a division-free replacement for the M17-079 tilt/margin formula that uses the first nonzero critical line jet instead of dividing by `C`.

If compact recurrence forces a uniform finite `r`, the formerly noncritical tail gap becomes a finite collection of higher-jet maximum gates.

This is the **Degenerate Maximum Finite-Jet Gate (DMFJG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
