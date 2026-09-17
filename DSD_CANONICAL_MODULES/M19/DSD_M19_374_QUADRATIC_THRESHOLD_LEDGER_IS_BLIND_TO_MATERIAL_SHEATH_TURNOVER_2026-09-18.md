# DSD M19-374 — The quadratic threshold ledger is blind to material sheath turnover

Date: 2026-09-18

Status: **INTERNAL AUDIT / NO-GO FOR USING THE M5-666 QUADRATIC TRUNCATED-AMPLITUDE LEDGER AS A DIRECT FINITE-RESOURCE PRICE FOR M5-662/M5-665 SHEATH TURNOVER / THE MOVING-LEVEL REYNOLDS BOUNDARY TERM VANISHES IDENTICALLY BECAUSE THE TEST DENSITY `(rho-a)^2/2` IS ZERO ON `rho=a` / THEREFORE ORDER-ONE MATERIAL CROSSING THROUGH THE FIXED AMPLITUDE THRESHOLD CAN OCCUR WITHOUT ANY DIRECT EVENT TERM IN `N_a` / A VOLUME-NORMALIZED VERSION REINTRODUCES THE TURNOVER RATE BUT ONLY AS A RECYCLABLE BALANCE TERM, NOT A ONE-SIGN DECREMENT / GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.**

---

## 1. Fixed-threshold survivor from M5-665--666

The static high-amplitude multi-sheet geometry has been compressed to positive-rate dynamic activity

\[
C_{rot}^{force}
\lor
C_{crit}^{higher\text{-}jet}
\lor
T_{sheath}^{\rho=a_0}.
\]

M5-666 proposes the bounded fixed-threshold observable

\[
\boxed{
N_a(\theta)
:=
\frac12\int_{\mathbb R^3}(\rho-a)_+^2\,dy
}
\]

with exact ledger

\[
\boxed{
N_a'
+\frac12N_a
+aM_a
+D_a^{(2)}
=
Q_a^{(2)}.
}
\]

The natural question is whether the positive material turnover across `rho=a` forced by M5-662 is itself priced by this observable.

---

## 2. Moving superlevel formulation

Let

\[
\Omega_a(\theta):=\{y:\rho(y,\theta)>a\},
\qquad
q_a:=\rho-a
\quad\text{on }\Omega_a.
\]

Then

\[
N_a
=
\frac12\int_{\Omega_a}q_a^2\,dy.
\]

Let `V_a` denote the normal velocity of the moving level surface `rho=a`.

For a moving domain, Reynolds transport relative to the similarity material velocity `B` gives

\[
\frac d{d\theta}\int_{\Omega_a}F\,dy
=
\int_{\Omega_a}(D_BF+F\nabla\cdot B)\,dy
+
\int_{\partial\Omega_a}F\,(V_a-B)\cdot n\,dS.
\]

Take

\[
F=\frac12q_a^2.
\]

On the moving amplitude boundary,

\[
q_a=\rho-a=0.
\]

Therefore

\[
\boxed{
\int_{\partial\Omega_a}
\frac12q_a^2\,(V_a-B)\cdot n\,dS
=0.
}
\]

This is exact and does not require the material crossing speed to be small.

---

## 3. Turnover current is invisible to `N_a`

M5-662 defines the material crossing/turnover current at the threshold by

\[
\boxed{
\mathcal T_a
:=
\int_{\partial\Omega_a}(B-V_a)\cdot n\,dS.
}
\]

For a recurrent sheet-domain attached to the amplitude boundary, M5-662 obtains a positive mean lower bound of the form

\[
\langle\mathcal T_{a_0}\rangle
\ge
\frac32v_0>0.
\]

But the previous section shows that even an order-one value of `mathcal T_a` produces no direct boundary contribution to `N_a'`.

Thus

\[
\boxed{
T_{sheath}^{\rho=a_0}
\not\Rightarrow
\text{a direct decrement of }N_{a_0}.
}
\]

The absence of the boundary term in M5-666 is therefore both a technical advantage and an event-detection blind spot.

---

## 4. The same blindness holds for the linear truncated mass

For

\[
M_a=\int(\rho-a)_+\,dy,
\]

the moving-domain boundary density is again zero:

\[
(\rho-a)_+|_{\rho=a}=0.
\]

Hence direct threshold turnover is also absent from the Reynolds boundary term for `M_a`.

The surface term in the M5-652 linear ledger comes from integration by parts in the elliptic equation,

\[
\int_{\rho=a}|\nabla\rho|\,dS,
\]

not from material crossing of the moving threshold.

These two mechanisms must not be conflated.

---

## 5. Volume does see turnover

The bare superlevel volume

\[
V_a:=|\Omega_a|
\]

does not vanish on the boundary and obeys

\[
\boxed{
V_a'
=
\frac32V_a
-
\mathcal T_a
}
\]

with the appropriate orientation convention.

Thus `V_a` is the natural observable for material threshold crossing.

However on a recurrent bounded branch,

\[
\langle V_a'\rangle=0
\]

merely gives

\[
\boxed{
\langle\mathcal T_a\rangle
=
\frac32\langle V_a\rangle,
}
\]

which is exactly the recyclable sheath-turnover balance already identified in M5-662.

It is not a contradiction.

---

## 6. Volume-normalized quadratic amplitude

Define

\[
R_a:=\frac{N_a}{V_a}
\]

whenever `V_a>0`.

Combining

\[
N_a'
=Q_a^{(2)}
-\frac12N_a
-aM_a
-D_a^{(2)}
\]

with

\[
V_a'
=\frac32V_a-\mathcal T_a
\]

gives

\[
\boxed{
R_a'
=
\frac{Q_a^{(2)}}{V_a}
-2R_a
-a\frac{M_a}{V_a}
-\frac{D_a^{(2)}}{V_a}
+
R_a\frac{\mathcal T_a}{V_a}.
}
\]

Thus normalization reintroduces the turnover current explicitly.

But the turnover term has the form

\[
R_a\frac{\mathcal T_a}{V_a},
\]

which is balanced by axial production and the other recurrent terms. No one-sign bounded-state drift follows from the identity alone.

Hence

\[
\boxed{
\text{volume normalization restores observability of turnover, but not irreversibility.}
}
\]

---

## 7. Consequence for the current CE-H dynamic frontier

The M5-666 quadratic ledger cannot by itself unify the three M5-665 dynamic mechanisms into a finite-resource contradiction.

In particular,

\[
\boxed{
T_{sheath}^{\rho=a_0}
}

is directly invisible to the unnormalized truncated-amplitude observables.

The live dynamic frontier should therefore remain split as

\[
\boxed{
C_{rot}^{force}
\lor
C_{crit}^{higher\text{-}jet}
\lor
T_{sheath}^{\rho=a_0},
}

with the following distinct currencies:

1. generalized-kappa-force orientation/creation for the first two branches;
2. moving-level volume/current for the sheath branch.

A genuine closure requires a new coupling theorem showing that one of these currencies necessarily causes a nonrecyclable change in another bounded or finite base resource.

---

## 8. Immediate next target

The highest-value next question is not another amplitude moment.

It is

\[
\boxed{
\mathcal T_{couple}^{force\leftrightarrow turnover}:
\text{does every complete recurrent sheet-renewal cycle require a force-rotation/higher-jet event and a threshold-turnover event with a common nonreused material label or finite transversal charge?}
}
\]

If not, the two event classes may recycle independently on a compact recurrent hull.

---

## 9. Firewall

This note does not weaken the exact M5-666 ledger.

It only limits its use as an event-counting observable.

The quadratic truncation deliberately eliminates the amplitude-level boundary term, and therefore cannot simultaneously be treated as a direct meter of material crossing through that boundary.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
