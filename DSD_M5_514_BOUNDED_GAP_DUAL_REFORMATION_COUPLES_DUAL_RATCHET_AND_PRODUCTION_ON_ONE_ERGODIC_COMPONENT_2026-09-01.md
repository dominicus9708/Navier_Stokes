# DSD M5-514 — Bounded-gap dual reformation couples dual activity, ratchet activity, and production on one ergodic component

Date: 2026-09-01

Status: **COMPONENT-COUPLING UPGRADE / M5-455 DID NOT MERELY PRODUCE A DUAL-SOURCE EVENT SOMEWHERE: OUTSIDE THE ALREADY TYPED STRONG REMOTE/DERIVATIVE EXIT, EVERY FIXED-LENGTH QUIET FIRST-HITTING BLOCK REFORMS A COHERENT MISALIGNED DUAL-FLUX COMPANION / ON THE M5-508 GLOBAL SMOOTH COMPACT HARD CORE THESE STRONG EXITS HAVE BEEN REMOVED, SO DUAL EVENTS HAVE A UNIFORM BOUNDED GENERATION GAP / THIS TOPOLOGICAL BOUNDED-GAP PROPERTY PASSES TO EVERY SHIFT-INVARIANT AND EVERY ERGODIC MEASURE SUPPORTED ON THE COMPACT HULL / CHOOSING AN ERGODIC COMPONENT WITH POSITIVE RATCHET MEAN FROM M5-485 THEREFORE AUTOMATICALLY GIVES POSITIVE DUAL ACTIVITY ON THE SAME COMPONENT, AND M5-499 GIVES POSITIVE AXIAL PRODUCTION ON EVERY NONZERO COMPONENT / THE OLD M5-498 FIREWALL THAT THE THREE POSITIVE MEANS MAY LIVE ON DIFFERENT COMPONENTS IS THUS REMOVED ON THE RETAINED COMPACT HARD CORE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. The old component-coupling firewall

M5-498 correctly warned that from three global positive means alone one cannot infer that

\[
\text{production},
\qquad
\text{dual activity},
\qquad
\text{ratchet activity}
\]

occur on the same ergodic component.

That warning was necessary at the time because the proof used only positivity after invariant averaging.

M5-514 returns to the stronger *pointwise-in-generation* information already established earlier in M5-455.

---

## 2. M5-455 is a bounded-gap statement

On the bounded uniformly elliptic metric corridor, M5-455 fixes an integer

\[
L_\kappa<\infty
\]

such that every quiet block of `L_kappa` first-hitting generations satisfies

\[
\boxed{
G_{dual\ flux}^{metric}
\lor
H_{remote/derivative}^{strong}.
}
\]

The dual event contains a coherent natural-scale companion with

- fixed nonzero directed flux;
- fixed positive amplitude/thickness;
- a direction separated from the productive direction by a fixed angle.

The important logical form is

\[
\boxed{
\text{every fixed-length quiet block}
\Longrightarrow
\text{dual event or strong exit}.
}
\]

This is stronger than a single positive-density statement.

---

## 3. On the global smooth compact hard core the strong exit is absent

The chain M5-502--508 separated and typed

\[
H_{tail}^{remote-P},
\qquad
H_{tail}^{remote-Sob},
\qquad
H_{tail}^{remote-E},
\]

and then restricted the retained branch to

\[
\mathcal C_{smooth}^{global}.
\]

On this branch there is no remaining vorticity derivative/mass escape of the type used as the `H_remote/derivative^strong` alternative in M5-455.

The bounded-deformation/quiet lineage assumptions are also part of the retained bounded critical corridor leading to M5-474--508.

Therefore M5-455 reduces on the present hard core to

\[
\boxed{
\text{every }L_\kappa\text{-generation block contains a dual event}.
}
\]

This is the bounded-gap dual-reformation property.

---

## 4. Generation indicator

Let

\[
d_j\in[0,1]
\]

be a time-smoothed dual-event mark for generation `j`, chosen so that a full fixed dual event contributes at least one fixed amount

\[
d_*>0.
\]

The bounded-gap statement gives, after harmless adjustment of block boundaries,

\[
\boxed{
\sum_{j=m}^{m+L_\kappa-1}d_j
\ge d_*
\qquad
\text{for every }m.
}
\]

Hence every sequence in the retained marked shift hull obeys

\[
\liminf_{N\to\infty}
\frac1N\sum_{j=0}^{N-1}d_j
\ge
\frac{d_*}{L_\kappa}.
\]

Define

\[
\delta_{dual}
:=
\frac{d_*}{L_\kappa}>0.
\]

Then

\[
\boxed{
\underline{\mathrm{dens}}(dual)
\ge\delta_{dual}
\quad\text{on every retained hull sequence}.
}
\]

---

## 5. Pass to invariant measures

Let `mu` be any shift-invariant probability measure supported on the retained compact marked hull.

Averaging the bounded-gap inequality gives

\[
\boxed{
\int d\,d\mu
\ge
\delta_{dual}>0.
}
\]

This conclusion is independent of which invariant measure is selected.

In particular, if

\[
\mu
=
\int\mu_\alpha\,d\pi(\alpha)
\]

is the ergodic decomposition, then every ergodic component supported on the same bounded-gap subshift satisfies

\[
\boxed{
\int d\,d\mu_\alpha
\ge
\delta_{dual}>0.
}
\]

Thus dual activity cannot be confined to one special ergodic component.

---

## 6. Select the positive-ratchet component

M5-485 gives a shift-invariant measure with

\[
\boxed{
\int a_{rat}\,d\mu>0.
}
\]

By ergodic decomposition, there exists at least one ergodic component

\[
\mu_*
\]

such that

\[
\boxed{
\int a_{rat}\,d\mu_*>0.
}
\]

Because `mu_*` is supported on the retained bounded-gap compact hull, Section 5 gives simultaneously

\[
\boxed{
\int d\,d\mu_*
\ge\delta_{dual}>0.
}
\]

Therefore the same ergodic component carries both

\[
\boxed{
\text{positive ratchet activity}
+
\text{positive dual-source activity}.
}
\]

---

## 7. Production is automatically on the same component

M5-486 derived the exact similarity enstrophy identity

\[
\frac12E'
+
\frac14E
+
P
=
Q.
\]

M5-499 then audited the invariant-component consequence: every nonzero recurrent component satisfies

\[
\boxed{
\langle Q\rangle
=
\frac14\langle E\rangle
+
\langle P\rangle
>0.
}
\]

The component `mu_*` has positive ratchet activity and is therefore nonzero.

Hence

\[
\boxed{
\int Q\,d\mu_*>0.
}
\]

Thus on one and the same ergodic component,

\[
\boxed{
\begin{aligned}
&\langle a_{rat}\rangle_{\mu_*}>0,\\
&\langle d_{dual}\rangle_{\mu_*}\ge\delta_{dual}>0,\\
&\langle Q\rangle_{\mu_*}>0.
\end{aligned}
}
\]

This is the desired component coupling.

---

## 8. Correction to the M5-498 firewall

The M5-498 statement

\[
\text{the positive production, dual and ratchet means need not lie on the same component}
\]

was correct when only the three averaged positivity statements were being used.

After restoring the stronger bounded-gap theorem of M5-455, it can be sharpened on the present compact branch.

The correct current statement is

\[
\boxed{
\text{on }\mathcal C_{smooth}^{global},
\text{ choose a positive-ratchet ergodic component;}
\]

\[
\boxed{
\text{that same component necessarily has positive dual activity and positive production.}
}
\]

This does **not** mean the three events occur at the same instant.

It means they belong to the same irreducible recurrent statistical dynamics.

---

## 9. Event-time intersection remains separate

From

\[
\langle a_{rat}\rangle>0,
\qquad
\langle d_{dual}\rangle>0,
\qquad
\langle Q\rangle>0
\]

on one ergodic component, it does not follow that there exists a time at which all three pointwise event thresholds are simultaneously active.

An ergodic orbit can alternate between distinct regions of phase space.

Therefore the remaining coupling problem is no longer **component coupling** but rather

\[
\boxed{
\text{cycle/path coupling inside one ergodic component}.
}
\]

This is a much smaller obstruction.

---

## 10. Combine with M5-512 dynamic action

M5-512 gives on the same compact marked dynamics a positive mean local phase-space speed

\[
\langle v\rangle>0.
\]

Hence the selected component `mu_*` can be taken to carry the full package

\[
\boxed{
\begin{aligned}
&\text{positive full-state dynamic action},\\
&\text{positive projective/diffusive ratchet activity},\\
&\text{bounded-gap dual-source reformation},\\
&\text{positive axial production}.
\end{aligned}
}
\]

The hard core is therefore one genuine active recurrent system, not a measure-theoretic mixture of unrelated mechanisms.

---

## 11. Relation to the finite lineage graph

M5-497--498 reduced the quiet tight branch to finitely many persistent lineages and recurrent transfer cycles.

On `mu_*`, bounded-gap dual reformation means that the finite graph cannot spend arbitrarily long generation intervals in a purely single-direction state.

At least one persistent pair interaction is revisited with bounded gaps, possibly after label permutation inside the finite network.

Because the pair set is finite, a pigeonhole refinement gives at least one persistent pair `(a,b)` whose dual mark has positive `mu_*` mean.

Thus one can now work entirely inside one ergodic component with one recurrent finite lineage network.

---

## 12. New frontier: rigid pair or relative pair action

For a persistent pair define, whenever the carrier directions are nondegenerate,

\[
c_{ab}
:=
\xi_a\cdot\xi_b.
\]

M5-491 gives

\[
\boxed{
\frac{dc_{ab}}{d\theta}
=
R_{strain}^{ab}
+
R_{diff}^{ab}.
}
\]

On the selected ergodic component there are now only two qualitative possibilities:

1. `c_ab` is invariant almost everywhere, giving a rigid relative-angle pair;
2. `c_ab` is not invariant, in which case ergodicity forces positive relative-angle activity.

This dichotomy is the next direct route to coupling the dual pair itself to the ratchet mechanism.

---

## 13. Updated compact hard core

The old three-component uncertainty is replaced by

\[
\boxed{
\mathcal E_*:
\text{one nonzero ergodic compact component with}
}
\]

\[
\boxed{
\langle Q\rangle>0,
\qquad
\langle a_{rat}\rangle>0,
\qquad
\langle d_{dual}\rangle\ge\delta_{dual}>0,
\qquad
\langle v\rangle>0.
}
\]

The remaining question is how these activities circulate inside that one component.

---

## 14. Highest-value next target

Use the persistent-pair relative-angle observable on `mu_*`.

Prove the exact ergodic dichotomy

\[
\boxed{
\text{rigid noncollinear pair}
\lor
\langle|c_{ab}'|\rangle>0.
}
\]

In the second case, M5-491 converts the positive derivative into positive same-pair transverse-strain/directional-diffusion action, giving a direct dual--ratchet coupling rather than merely a common-component coupling.

In the first case, the pair defines a persistent moving frame and the problem becomes a rigid-frame/breather audit.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
