# DSD M5-484 — Audit the inheritance ledger for the ancient dilation hull

Date: 2026-09-01

Status: **AUDIT CORRECTION / THE M5-477 FINITE TOTAL PALINSTROPHY OF THE FIRST ANCIENT ELEMENT DOES NOT PASS THROUGH THE M5-478 SECOND BLOW-DOWN AS A UNIFORM FINITE TOTAL PALINSTROPHY BOUND; WHAT DOES PASS IS A SHARP BACKWARD-TRUNCATED CRITICAL TAIL ESTIMATE `int_{-infinity}^{-eps} ||grad Omega_m||_2^2 ds <= C eps^{-1/2}` / THE M5-474 SINGLE MATERIAL-RATCHET EVENT IS SENT TO `s=0` BY THE SECOND BLOW-DOWN AND IS THEREFORE NOT YET AN INTERIOR MARK OF THE M5-483 HULL / THE NONTRIVIAL FIRST-HITTING CARRIER, TYPE-I ENSTROPHY/VORTICITY BOUNDS, EXACT PARABOLIC DILATION GENEALOGY, AND TERMINAL CRITICAL TAIL REMAIN VALID / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose of this audit

M5-483 reached a genuine open hard core:

\[
\text{nonzero Type-I ancient parabolic dilation hull}.
\]

Before trying to derive a new rigidity theorem from extra marks, every proposed mark must be classified as one of

1. **exactly inherited**;
2. **inherited only after rescaling with a changed quantitative ledger**;
3. **lost at the second blow-down**;
4. **not yet proved to survive the compactness limit**.

This is the DSD distinction between a property of the parent representation and a property of the descendant representation.

---

## 2. M5-477 input

Let the first marked ancient element be `(V,Omega)` and write

\[
E(\tau):=\|\Omega(\tau)\|_2^2,
\qquad
P(\tau):=\|\nabla\Omega(\tau)\|_2^2.
\]

M5-475--477 give for sufficiently large negative time

\[
E(\tau)\le C(-\tau)^{-1/2},
\]

\[
\|\Omega(\tau)\|_\infty\le C(-\tau)^{-1},
\]

and

\[
\left|\int S\Omega\cdot\Omega\,dx\right|
\le C(-\tau)^{-3/2}.
\]

M5-477 also proves

\[
\boxed{
\int_{-\infty}^{0}P(\tau)\,d\tau<\infty.
}
\]

---

## 3. A sharper backward palinstrophy-tail estimate

Integrate the vorticity-enstrophy identity from `-infinity` to `-T`:

\[
\frac12E(-T)
+
\int_{-\infty}^{-T}P(\tau)\,d\tau
=
\int_{-\infty}^{-T}
\int S\Omega\cdot\Omega\,dx\,d\tau.
\]

Because the left palinstrophy term is nonnegative,

\[
\int_{-\infty}^{-T}P(\tau)\,d\tau
\le
\int_{-\infty}^{-T}
\left|\int S\Omega\cdot\Omega\,dx\right|d\tau.
\]

Using the M5-477 production bound,

\[
\boxed{
\int_{-\infty}^{-T}P(\tau)\,d\tau
\le CT^{-1/2}.
}
\]

This quantitative tail estimate is stronger than the bare statement of finite total palinstrophy and is the correct object to rescale.

---

## 4. Exact scaling of enstrophy and palinstrophy

For the M5-478 record scale

\[
T_m=R_m^2
\]

define

\[
V_m(y,s)=R_mV(R_my,T_ms),
\]

\[
\Omega_m(y,s)=R_m^2\Omega(R_my,T_ms).
\]

Then

\[
\boxed{
\|\Omega_m(s)\|_2^2
=R_mE(T_ms).
}
\]

For palinstrophy,

\[
\nabla_y\Omega_m
=R_m^3(\nabla\Omega)(R_my,T_ms),
\]

hence

\[
\boxed{
\|\nabla\Omega_m(s)\|_2^2
=R_m^3P(T_ms).
}
\]

Since `ds=d tau/T_m=d tau/R_m^2`,

\[
\boxed{
\int_I\|\nabla\Omega_m(s)\|_2^2ds
=R_m
\int_{T_mI}P(\tau)d\tau.
}
\]

---

## 5. What survives uniformly on `s<=-eps`

For every fixed `eps>0`,

\[
\begin{aligned}
\int_{-\infty}^{-\varepsilon}
\|\nabla\Omega_m(s)\|_2^2ds
&=
R_m
\int_{-\infty}^{-\varepsilon T_m}P(\tau)d\tau\\
&\le
R_m C(\varepsilon T_m)^{-1/2}\\
&=C\varepsilon^{-1/2}.
\end{aligned}
\]

Therefore

\[
\boxed{
\sup_m
\int_{-\infty}^{-\varepsilon}
\|\nabla\Omega_m(s)\|_2^2ds
\le C\varepsilon^{-1/2}.
}
\]

After local compactness and lower semicontinuity, every M5-483 hull member `mathcal U_n` with vorticity `mathcal Omega_n` satisfies

\[
\boxed{
\int_{-\infty}^{-\varepsilon}
\|\nabla\mathcal\Omega_n(s)\|_2^2ds
\le C\varepsilon^{-1/2},
\qquad
\varepsilon>0.
}
\]

This is a genuine inherited mark.

It is exactly scale-critical: a backward DSS solution may saturate this rate, so the estimate alone is not a contradiction.

---

## 6. What does **not** survive as a uniform global finite ledger

Over the complete interval `(-infinity,0)`,

\[
\int_{-\infty}^{0}
\|\nabla\Omega_m(s)\|_2^2ds
=
R_m
\int_{-\infty}^{0}P(\tau)d\tau.
\]

Unless the parent palinstrophy is identically zero, the right side grows like `R_m`.

Therefore there is no uniform estimate of the form

\[
\sup_m
\int_{-\infty}^{0}
\|\nabla\Omega_m(s)\|_2^2ds<\infty.
\]

Consequently M5-477's finite total palinstrophy may be cited as **ancestry**, but not as an already inherited finite-total-palinstrophy property of the M5-483 ancient dilation hull.

---

## 7. Audit of the material-ratchet mark

M5-474 gives an order-one material-axis ratchet event on a fixed parent normalized interval

\[
\tau\in J=O(1).
\]

Under the second blow-down

\[
s=\frac{\tau}{T_m}.
\]

Thus the same fixed parent event is located at

\[
J_m=J/T_m,
\]

and

\[
J_m\to\{0\}.
\]

Hence on every fixed compact cylinder

\[
K\Subset\mathbb R^3\times(-\infty,0)
\]

the original M5-474 single ratchet event eventually lies outside `K`.

Therefore

\[
\boxed{
\text{one parent ratchet event}
\not\Rightarrow
\text{an interior ratchet mark in the second blow-down limit}.
}
\]

This is the main scope correction of M5-484.

M5-483 Section 10 should therefore interpret "inherited material-axis ratchet mark" as a **candidate structure requiring an additional recurrence extraction**, not as an already established property.

---

## 8. Marks that are genuinely inherited

The following survive the M5-478 to M5-483 passage on the compact/no-defect lane.

### 8.1 Exact Navier--Stokes dynamics

\[
\partial_s\mathcal U_n
+
\mathcal U_n\cdot\nabla\mathcal U_n
=-\nabla\mathcal P_n+\Delta\mathcal U_n.
\]

### 8.2 Exact parabolic genealogy

\[
\boxed{
\mathcal U_{n+1}
=\mathscr D_{\lambda_n}\mathcal U_n.
}
\]

### 8.3 Type-I vorticity and velocity bounds

\[
\|\mathcal\Omega_n(s)\|_\infty\le C|s|^{-1},
\]

\[
\|\mathcal\Omega_n(s)\|_2^2\le C|s|^{-1/2},
\]

\[
\|\mathcal U_n(s)\|_\infty\le C|s|^{-1/2}.
\]

### 8.4 Nontrivial old first-hitting carrier

At `s=-1`, the record-scale carrier remains at finite position and unit scale, producing a fixed nonzero local enstrophy mark.

### 8.5 Backward-truncated palinstrophy tail

\[
\int_{-\infty}^{-\varepsilon}
\|\nabla\mathcal\Omega_n\|_2^2ds
\le C\varepsilon^{-1/2}.
\]

### 8.6 Terminal critical-tail alternative

The suitable-terminal compactness chain M5-479--482 remains the route into the critical `L3`/Dirichlet dilation tail.

---

## 9. DSD inheritance ledger

| Parent property | Second blow-down status | Audit classification |
|---|---|---|
| exact NS equation | survives | exact |
| exact parabolic scaling | survives | exact |
| Type-I `Linf` vorticity | survives | exact bound |
| Type-I enstrophy rate | survives | exact bound |
| first-hitting carrier at record time | survives at `s=-1` | marked nontriviality |
| terminal critical tail | survives on suitable/no-defect lane | conditional inherited structure |
| total parent palinstrophy finite | not uniform after rescaling | ancestry only |
| truncated palinstrophy tail | survives as `C eps^-1/2` | critical inherited bound |
| single M5-474 ratchet event | collapses to `s=0` | not inherited in the interior |
| recurrent ratchet pattern | not yet extracted | new proof obligation |

---

## 10. Literature firewall

Barker--Prange, *Quantitative Regularity for the Navier--Stokes Equations Via Spatial Concentration* (Commun. Math. Phys. 385, 2021), explicitly records the general nonzero backward discretely self-similar problem as open while deriving consequences under additional decay/integrability assumptions.

Chae's asymptotically DSS nonexistence theorem assumes a time-periodic profile in strong `L3`-type integrability.

Therefore the M5-483 hull cannot be closed by importing those theorems unless a strong critical spatial class is first proved.

---

## 11. Corrected highest-value next target

There are now two honest possibilities.

### Route A — recurrent-mark extraction

Use the positive-generation-density ratchet statement from M5-471--473 to construct a **log-scale recurrent ratchet mark** that survives the second blow-down at fixed negative times.

This requires a density-centered/shift-compact extraction, not merely the single marked event of M5-474.

### Route B — new rigidity from the inherited critical ledger

Find a rigidity theorem for a nonzero Type-I ancient dilation hull satisfying simultaneously

\[
\int_{-\infty}^{-\varepsilon}
\|\nabla\Omega\|_2^2ds
\le C\varepsilon^{-1/2}
\]

and the record-scale nontrivial carrier/terminal Dirichlet-tail structure.

The estimate is critical and therefore cannot be expected to close the hull by itself.

---

## 12. Updated frontier

The audited compact bounded lane is

\[
\boxed{
E_{ratchet}^{ancient}
\Longrightarrow
E_{dil}^{ancient,Type-I}
}
\]

with the rigorously inherited package

\[
\boxed{
\text{exact dilation genealogy}
+
\text{Type-I bounds}
+
\text{record carrier}
+
\text{critical terminal tail}
+
\text{truncated palinstrophy tail}.
}
\]

A recurrent material-axis mark is **not yet part of this package**.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
