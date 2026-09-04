# DSD M17-034 — Area–curvature density has a source-free continuity law and an exact oblique turnover ledger

Date: 2026-09-04
Canonical ID: **M17-034**

Status: **INTERNAL MATERIAL-TURNOVER BRIDGE / M17-031 GIVES THE UNIVERSAL POINTWISE LAW `D_B(j_xi b)=-(3/2)j_xi b`. BECAUSE THE SIMILARITY MATERIAL VELOCITY HAS `div B=3/2`, THE AREA–CURVATURE VECTOR DENSITY SATISFIES AN EXACT SOURCE-FREE EULERIAN CONTINUITY EQUATION. THE POSITIVE MAGNITUDE DENSITY `Q=|j_xi||b|` SATISFIES `partial_theta Q + div(B Q)=0` ON EVERY NONZERO-SIGN REGULAR MATERIAL COMPONENT. THUS A BOUNDED RECURRENT OBLIQUE CORE CANNOT REGENERATE THIS CHARGE INTERNALLY: ITS LONG-TIME MEAN CONTENT MUST BE MAINTAINED BY MATCHED BOUNDARY IMPORT/EXPORT. COMBINED WITH M5-560, EVERY POSITIVE-Q MATERIAL PACKET HAS FINITE RESIDENCE IN A BOUNDED SIMILARITY CORE, SO RECURRENT OBLIQUE RANK-TWO GEOMETRY REQUIRES AN EXACT CHARGE-CARRYING MATERIAL TURNOVER CONVEYOR OR A LOWER-DIMENSIONAL/DEGENERATING EXIT. THIS DOES NOT YET ASSIGN A NONRECYCLABLE COST TO TURNOVER, SO IT IS A LEDGER CLOSURE RATHER THAN A GLOBAL CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Area-curvature vector density

On a regular component with

\[
j_\xi\ne0,
\qquad
b=(\xi\cdot\nabla)\xi\ne0,
\]

define

\[
\boxed{C:=j_\xi b.}
\]

M17-031 gives

\[
\boxed{
D_BC=-\frac32C.
}
\]

Since both `j_xi` and the direction of `b` preserve their material sign/orientation while nonzero, the positive magnitude density

\[
\boxed{Q:=|j_\xi|\,|b|}
\]

obeys the same scalar law

\[
\boxed{
D_BQ=-\frac32Q.
}
\]

---

## 2. Similarity material divergence

For

\[
B=U+\frac12y,
\]

incompressibility of `U` gives

\[
\boxed{
\nabla\cdot B=\frac32.
}
\]

Therefore

\[
D_BQ+Q\nabla\cdot B=0.
\]

Using

\[
D_BQ=\partial_\theta Q+B\cdot\nabla Q,
\]

we obtain

\[
\boxed{
\partial_\theta Q
+\nabla\cdot(BQ)=0.
}
\]

This is an exact scalar continuity equation.

---

## 3. Vector form

Componentwise, since

\[
D_BC_i=-\frac32C_i,
\]

we also have

\[
\boxed{
\partial_\theta C_i
+\partial_j(B_jC_i)=0.
}
\]

Equivalently,

\[
\boxed{
\partial_\theta C
+\operatorname{div}(B\otimes C)=0
}
\]

with the divergence taken in the transport index.

Thus the oriented area-curvature charge is materially conserved as a vector density.

---

## 4. Material-set conservation

Let `A(theta)` be any material set transported by `B` while remaining inside the regular nonzero component.
Then Reynolds transport gives

\[
\boxed{
\frac d{d\theta}
\int_{A(\theta)}Q\,dy
=0.
}
\]

Likewise

\[
\boxed{
\frac d{d\theta}
\int_{A(\theta)}C\,dy
=0.
}
\]

This is the integral version of M17-031's pointwise cancellation with the `3/2` material-volume expansion.

---

## 5. Fixed Eulerian core ledger

Let `Omega` be a fixed bounded similarity-coordinate core.
Then

\[
\frac d{d\theta}
\int_\Omega Q\,dy
=
-\int_{\partial\Omega}Q\,B\cdot n\,dA.
\]

Hence a recurrent core with bounded nonzero mean content

\[
\left\langle
\int_\Omega Q\,dy
\right\rangle>0
\]

must satisfy zero long-time net drift of the charge and therefore a matched import/export ledger:

\[
\boxed{
\left\langle
\int_{\partial\Omega}Q\,B\cdot n\,dA
\right\rangle=0.
}
\]

This does **not** mean no turnover.
It means recurrent turnover must import as much area-curvature charge as it exports on average.

---

## 6. M5-560 residence-time firewall

M5-560 proves that every positive-volume material set expands as

\[
|A(\theta)|
=e^{3(\theta-\theta_0)/2}|A_0|.
\]

Consequently a fixed positive-volume packet cannot remain forever inside a bounded similarity core.

Apply this to any material packet carrying positive `Q` charge.
Its total `Q` charge is conserved, but its similarity volume expands exponentially.
Therefore its average `Q` density decays like

\[
\boxed{
\overline Q_{A(\theta)}
\sim e^{-3(\theta-\theta_0)/2}
}
\]

if the packet remains regular.

Thus a recurrent fixed Eulerian `Q` density cannot be represented indefinitely by one fixed positive-volume material packet.

---

## 7. Exact oblique-turnover consequence

A recurrent bounded oblique Rank-2 core with a fixed positive area-curvature content must therefore use at least one of

\[
\boxed{
\text{material charge turnover}
\ \lor\ 
\text{collapse toward a lower-volume spine}
\ \lor\ 
 j_\xi\to0
\ \lor\ 
 b\to0.
}
\]

The first option is now stronger than the generic M5-560 turnover statement:
newly entering material must carry the conserved area-curvature charge required to replace the exiting population.

The geometry cannot simply be recreated from zero charge inside the core, because the continuity equation has no source term.

---

## 8. Relation to the M5 flux conveyor

M5's vorticity-flux genealogy is not identical to the `Q` ledger.
The two conserved/transported quantities are different descriptors:

- vorticity flux is modified by the `kappa` amplification channel;
- `Q` is a source-free area-curvature charge after the exact `3/2` volume cancellation.

A recurrent Rank-2 oblique survivor must therefore coordinate **two ledgers simultaneously**:

\[
\boxed{
\text{M5 flux/hysteresis turnover}
\quad+
\text{M17 area-curvature charge turnover}.
}
\]

No theorem yet shows that servicing both ledgers incurs an irrecoverable positive cost.

---

## 9. DSD interpretation

M17-031 identified a pointwise material decay.
M17-034 changes the descriptor from pointwise density to Eulerian conserved charge.

The apparent decay

\[
Q\sim e^{-3\theta/2}
\]

is exactly compensated by the expanding material measure.
Thus the correct invariant object is

\[
Q\,dV,
\]

not the pointwise `Q` value.

This prevents a false contradiction from the `3/2` decay while exposing the exact turnover requirement.

---

## 10. DSD audit

### Audit A — interpreting Q decay as charge destruction
Rejected. `Q dV` is materially conserved.

### Audit B — interpreting zero mean boundary flux as no turnover
Rejected. Large balanced import/export can have zero net mean.

### Audit C — claiming turnover can regenerate Q internally
Rejected on the regular branch: the continuity equation has no source.

### Audit D — identifying Q with vorticity flux
Rejected. They are separate ledgers that must be serviced simultaneously.

### Audit E — proof status
No nonrecyclable turnover cost has yet been derived.

---

## 11. Updated turnover frontier

The remaining Eulerian recurrent oblique branch must satisfy

\[
\boxed{
\begin{aligned}
&\partial_\theta Q+\nabla\cdot(BQ)=0,\\
&\text{finite positive-volume residence time},\\
&\text{matched recurrent }Q\text{ import/export},\\
&\text{simultaneous M5 flux/hysteresis turnover}.
\end{aligned}
}
\]

This converts the vague `material turnover` exit of M17-032 into an exact conserved-charge conveyor problem.

---

## 12. Next target

Two remaining high-value routes are now explicit:

1. **WHRFG:** project the weighted harmonic-director stress on the pure-transverse-kernel frame and determine whether the resonant `(-1/2,1,-1/2)` branch can exist;
2. **dual-ledger turnover:** test whether simultaneous M5 flux hysteresis and source-free `Q` transport force a finite irrecoverable exchange at each bounded-core recurrence.

The first is locally cleaner and is taken next.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
