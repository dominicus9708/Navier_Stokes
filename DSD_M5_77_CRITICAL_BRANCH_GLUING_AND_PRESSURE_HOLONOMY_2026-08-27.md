# DSD M5-77 — Critical-Branch Gluing and Pressure-Mean Holonomy

Date: 2026-08-27

Status: **GLOBAL BRANCH-COMPATIBILITY LAYER FOR THE M5-70 ENDPOINT / LOCAL REGULAR-BRANCH RECONSTRUCTIONS CARRY ONLY ADDITIVE PRESSURE GAUGES, AND THESE GAUGES MUST GLUE WHERE BRANCHES ACTUALLY MEET AT THE SAME CRITICAL POINT / CLOSED BRANCH-GRAPH CYCLES REQUIRE ZERO PRESSURE HOLONOMY / CONDITIONAL ON CONTINUOUS EXTENSION TO THE CRITICAL JUNCTIONS / GLOBAL REGULARITY UNPROVED.**

## 1. What M5-76 leaves undetermined

On each smooth regular nested branch `e`, M5-75 and M5-76 reconstruct

\[
\beta_e(a,t)=m_{e,a}(a,t)
\]

from velocity data and impose the local second-derivative closure.

Therefore

\[
\boxed{
m_e(a,t)
=C_e(t)
+\int_{a_{e,0}}^a\beta_e(s,t)\,ds.
}
\]

The only branch-local freedom left is an additive scalar `C_e(t)`.

These constants cannot be chosen independently if all branch means come from one smooth spatial pressure field.

---

## 2. Gluing at an actual critical junction point

Let several regular level branches approach the same spatial critical point

\[
x_v,
\qquad
a(x_v,t)=a_v>0,
\qquad
\nabla a(x_v,t)=0.
\]

Then

\[
b(x_v,t)
=U\cdot\nabla\log a
=0.
\]

Assume the exact endpoint relation on the incident regular branches extends continuously to the junction.

Since

\[
P-m_e(a,t)=2\nu b,
\]

we obtain along every incident branch

\[
\boxed{
\lim_{a\to a_v}m_e(a,t)=P(x_v,t).
}
\]

Thus if branches `e_1,...,e_r` actually meet at the same critical point,

\[
\boxed{
\lim_{a\to a_v}m_{e_1}
=
\cdots
=
\lim_{a\to a_v}m_{e_r}.
}
\]

This gives linear gluing equations for their additive constants `C_e(t)`.

---

## 3. Important guardrail

Equal critical amplitude does **not** by itself imply equal branch pressure means.

If two distinct branches terminate at two different spatial critical points with the same numerical value `a_v`, smoothness of `P` does not require

\[
P(x_{v,1},t)=P(x_{v,2},t).
\]

Therefore gluing is imposed only when the branches genuinely share the same spatial critical junction, or when an additional geometric argument identifies their pressure values.

This prevents a false global identification based only on equal speed.

---

## 4. Branch graph formulation

At fixed time, represent the regular nested components as edges of a level-component graph, with actual critical junctions as vertices.

Along an oriented edge `e` from level `a_-` to `a_+`, the pressure-mean increment is

\[
\boxed{
\Delta m_e
=
\int_{a_-}^{a_+}\beta_e(a,t)\,da.
}
\]

At each junction vertex, incident edge limits must agree as in Section 2.

Thus the endpoint reconstructs a one-form on this branch graph:

\[
\omega_e:=\beta_e(a,t)\,da.
\]

A globally single-valued pressure mean requires this one-form to be exact on the graph after the allowed vertex identifications.

---

## 5. Pressure holonomy on a graph cycle

If the branch graph contains a closed cycle `gamma`, the sum of edge increments around the cycle must vanish:

\[
\boxed{
\mathcal H_\gamma
:=
\sum_{e\subset\gamma}
\sigma_e
\int_e\beta_e(a,t)\,da
=0,
}
\]

where `sigma_e=+1` or `-1` records the cycle orientation.

A nonzero value

\[
\mathcal H_\gamma\ne0
\]

would mean that the locally reconstructed pressure mean returns to the same junction with a different value, which is incompatible with one globally single-valued pressure field.

This is a global obstruction not visible in M5-73--M5-76.

---

## 6. Tree case

If the relevant branch graph is a tree, there is no cycle holonomy condition.

In that case the vertex gluing equations determine all edge constants recursively from one reference pressure gauge, provided every local compatibility condition already holds.

Therefore topology alone does not rule out the endpoint in the tree case.

This distinction is essential:

- cycle -> possible additional holonomy obstruction;
- tree -> no topological contradiction merely from additive gauges.

---

## 7. Scaling audit

The pressure-mean slope scales as

\[
\beta_\Lambda=\Lambda\beta,
\]

while

\[
da_\Lambda=\Lambda\,da.
\]

Hence

\[
\Delta m_{e,\Lambda}=\Lambda^2\Delta m_e
\]

and

\[
\mathcal H_{\gamma,\Lambda}=\Lambda^2\mathcal H_\gamma,
\]

as expected for pressure.

For any transported reference amplitude `a_*`,

\[
\boxed{
\widehat{\mathcal H}_\gamma
:=
\frac{\mathcal H_\gamma}{a_*^2}
}
\]

is scale invariant.

---

## 8. DSD audit

### GREEN

Once `m_a` is known on a regular branch, only an additive time-dependent constant remains.

### GREEN

Branches converging to the same spatial critical point must have the same limiting pressure mean if the endpoint relation extends continuously there.

### GREEN

A closed branch-graph cycle requires zero accumulated mean-pressure increment.

### YELLOW

The graph description is conditional on enough regularity to follow nested branches and identify their true critical junctions.

### YELLOW

The M5-70 equality was derived on the active regular weighted region. Extension all the way to a critical junction requires a limiting argument and is not automatic.

### RED

Branches with equal critical amplitude but different spatial junction points must not be glued solely because the amplitude values agree.

### RED

No argument currently proves that the relevant branch graph must contain a nonzero-holonomy cycle.

---

## 9. Next calculation

One apparent escape remains: a regular level on which

\[
b=U\cdot\nabla\log a\equiv0.
\]

M5-75 cannot recover `m_a` dynamically there because its denominator vanishes.

The next audit should determine whether an exact **positive** M5-70 pump can hide entirely inside such tangential/degenerate levels.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
