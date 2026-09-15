# DSD M19-276 — A coarse graph cycle is not an independent continuum charge; every nonzero closed diffusion cycle is source response or export

Date: 2026-09-16  
Canonical ID: **M19-276**  
Status: **ACTIVE CONTINUUM-TO-GRAPH CORRECTION / EXACT CELL SOURCE IDENTITY / SOURCE-FREE CLOSED NETWORK CYCLE EXCLUDED / GRAPH H1 REINTERPRETED AS COARSE SOURCE RESPONSE / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-275 identifies the finite-population cycle space

\[
\ker B_G
\]

as the only graph sector invisible to scalar vertex coboundaries.

At the graph level this looks like a potential non-coboundary resource.

However the edge currents are not arbitrary graph variables. They come from one continuum scalar amplitude field through

\[
e_{ij}^{(p)}
=
\frac1p
\int_{S_{ij}}
\partial_{n_i}(\rho^p)dS.
\]

The present module restores this continuum constraint and asks whether a source-free closed continuum diffusion field can carry a nonzero coarse graph cycle.

The answer is no.

A nonzero coarse cycle must be supported by an interior Poisson source or by external exchange. Thus graph cohomology is not an independent PDE charge.

---

## 2. Scalar diffusion variable

Fix finite \(p\ge2\) and define

\[
\boxed{f:=\rho^p.}
\]

For an oriented population interface \(S_{ij}\),

\[
\boxed{
e_{ij}^{(p)}
=
\frac1p
\int_{S_{ij}}
\partial_{n_i}f\,dS.
}
\]

For an outer boundary piece of population \(P_i\), define analogously

\[
e_{i,ext}^{(p)}
=
\frac1p
\int_{\partial P_i\cap\partial_{ext}\Omega_{loc}}
\partial_{n_i}f\,dS.
\]

---

## 3. Exact cell divergence identity

By the divergence theorem on one population,

\[
\frac1p
\int_{P_i}\Delta f\,dy
=
\frac1p
\int_{\partial P_i}\partial_{n_i}f\,dS.
\]

Split the boundary into internal and external pieces:

\[
\boxed{
\frac1p
\int_{P_i}\Delta f\,dy
=
\sum_{j\ne i}e_{ij}^{(p)}
+e_{i,ext}^{(p)}.
}
\]

With the chosen graph orientation, define

\[
s_{p,i}^{\Delta}
:=
\frac1p
\int_{P_i}\Delta f\,dy.
\]

Then the finite graph current satisfies exactly

\[
\boxed{
B_Gj_p
=
s_p^{\Delta}-e_{ext,p}.
}
\]

Thus the divergence of the graph edge current is not free. It is the coarse projection of the continuum Poisson source.

---

## 4. CE-H formula for the continuum source

On CE-H,

\[
W=\rho\xi,
\qquad
\Delta W=\kappa W.
\]

Take the scalar product with \(\xi\). Since

\[
\xi\cdot\partial_a\xi=0
\]

and

\[
\xi\cdot\Delta\xi=-|\nabla\xi|^2,
\]

one gets

\[
\boxed{
\Delta\rho
=
\kappa\rho
+ho|\nabla\xi|^2.
}
\]

Now

\[
\Delta(\rho^p)
=
p\rho^{p-1}\Delta\rho
+p(p-1)\rho^{p-2}|\nabla\rho|^2.
\]

Therefore

\[
\boxed{
\frac1p\Delta(\rho^p)
=
\rho^p\kappa
+ho^p|\nabla\xi|^2
+(p-1)\rho^{p-2}|\nabla\rho|^2.
}
\]

Define the source density

\[
\boxed{
S_p
:=
\rho^p\kappa
+ho^p|\nabla\xi|^2
+(p-1)\rho^{p-2}|\nabla\rho|^2.
}
\]

Then

\[
\boxed{
(B_Gj_p)_i
=
\int_{P_i}S_p\,dy
-e_{i,ext}^{(p)}.
}
\]

---

## 5. Signed and positive pieces

The source has one signed and two nonnegative pieces:

\[
\boxed{
S_p
=
\underbrace{\rho^p\kappa}_{\text{signed diffusion eigenvalue}}
+
\underbrace{\rho^p|\nabla\xi|^2}_{\ge0}
+
\underbrace{(p-1)\rho^{p-2}|\nabla\rho|^2}_{\ge0}.
}
\]

Hence any local source-free relation

\[
S_p=0
\]

requires the signed \(\kappa\) term to cancel the two geometric gradient costs pointwise.

This is stronger than merely requiring the integrated cell source to vanish.

---

## 6. Closed-network global compatibility

Sum over all populations.

All internal interfaces cancel, so

\[
\boxed{
\int_{\Omega_{loc}}S_p\,dy
=
B_{p,ext}.
}
\]

On a closed no-export/no-import network,

\[
B_{p,ext}=0,
\]

and therefore

\[
\boxed{
\int_{\Omega_{loc}}S_p\,dy=0.
}
\]

This is the continuum form of

\[
\mathbf1^TB_Gj_p=0.
\]

---

## 7. Source-free closed continuum field has no cycle current

Assume the strong source-free branch

\[
\boxed{S_p=0\quad\text{in }\Omega_{loc}}
\]

and no external normal diffusion,

\[
\boxed{\partial_nf=0\quad\text{on }\partial_{ext}\Omega_{loc}.}
\]

Then

\[
\Delta f=0
\]

on the connected local region and \(f\) satisfies homogeneous Neumann boundary data.

Therefore \(f\) is constant on each connected component:

\[
\boxed{f\equiv\text{constant}.}
\]

Hence

\[
\nabla f=0,
\]

so every internal edge flux vanishes:

\[
\boxed{
j_p=0.}
\]

In particular,

\[
\boxed{
S_p\equiv0,\quad e_{ext}=0
\Longrightarrow
j_C=0.
}
\]

Thus there is no autonomous source-free continuum cycle hidden behind the coarse graph representation.

---

## 8. Nonzero coarse cycle requires source response or export

The contrapositive is

\[
\boxed{
 j_C\ne0
\Longrightarrow
 S_p\not\equiv0
\quad\lor\quad
 e_{ext}\ne0.
}
\]

Therefore the graph cycle is always attached to one of two physical mechanisms:

1. **interior source response** through the CE-H \(\kappa\)/direction-gradient/magnitude-gradient source density;
2. **external diffusive import/export**.

It is not an independent topological energy reservoir.

---

## 9. Global Poisson decomposition

On a closed connected network with compatibility

\[
\int_{\Omega_{loc}}S_p=0,
\]

solve the Neumann Poisson problem

\[
\boxed{
\Delta w=pS_p,
\qquad
\partial_nw=0
\text{ on }\partial_{ext}\Omega_{loc},
\qquad
\int w=0.
}
\]

Since

\[
\Delta f=pS_p,
\]

we have

\[
\Delta(f-w)=0,
\]

and

\[
\partial_n(f-w)=0
\]

on the external boundary.

Thus

\[
 f-w=\text{constant}.
\]

Therefore

\[
\boxed{
\nabla f=\nabla w.
}
\]

Every internal diffusion current is entirely the response to the interior source \(S_p\).

There is no additional harmonic cycle component in the continuum scalar field.

---

## 10. Why a graph cycle still appears after coarse projection

The Poisson response \(w\) can have different normal fluxes across different population interfaces.

When only the integrated interface fluxes are retained, the source-response field projects to a graph current with a possible cycle-space component.

Thus

\[
\boxed{
\text{graph }j_C
=
\text{cycle component of a coarse projection of the continuum source response},
}
\]

not a source-free continuum harmonic circulation.

This distinction removes a possible false topological interpretation of \(j_C\).

---

## 11. Consequence for M19-275 graph cohomology route

M19-275 correctly states that exact graph vertex forms cannot pair with \(j_C\).

But M19-276 shows that \(j_C\) itself is not an independent PDE cohomology charge.

A successful graph-affinity closure must therefore be a theorem about the **source-response operator**

\[
S_p
\longmapsto
j_C,
\]

not merely about abstract graph topology.

The dynamic target should be sharpened from

\[
\mathcal T_{graph}^{affinity}
\]

to

\[
\boxed{
\mathcal T_{source\to cycle}^{signed}:
\text{a signed nonexact source-response pairing with controlled mean}.
}
\]

---

## 12. Why this still does not close the branch

The source density contains the signed field \(\kappa\), and it may reverse in space/time.

Even when

\[
S_p\not\equiv0,
\]

its cell integrals may vanish while dipole/higher source structure drives interface exchange.

Likewise the positive gradient pieces may be repeatedly paid in similarity units without causing an infinite physical energy cost, by the M5-598 scaling firewall.

Therefore

\[
\boxed{
S_p\not\equiv0
\not\Rightarrow
\text{contradiction}.
}
\]

The gain is elimination of a false independent graph-topology resource.

---

## 13. Refined dynamic closure target

Combining M19-271, M19-275 and M19-276, the dynamic route now requires an explicit signed bridge

\[
\boxed{
\mathcal T_{lag\to source}:
\Gamma_E
\text{ or its positive-mean remainder couples to }S_p
\text{ at fixed lag},
}
\]

followed by a source-response obstruction such as

\[
\boxed{
\mathcal T_{source}^{one-way}
}
\]

or

\[
\boxed{
\mathcal T_{source\to cycle}^{signed}.
}
\]

Without such a signed bridge, the CE-H source density is another recurrent payer rather than a terminal contradiction.

---

## 14. Immediate next target

The highest-value next calculation is now to compare the finite-depth production observable from M5-587--590 with the explicit source density

\[
S_p
=
\rho^p\kappa
+ho^p|\nabla\xi|^2
+(p-1)\rho^{p-2}|\nabla\rho|^2.
\]

Both are evaluated on the same persistent material subsystem after M5-590.

Test whether the positive stretching surplus at finite depth forces a signed lower bound on an invariant/lagged average of \(S_p\), rather than only an unsigned derivative charge.

If yes, this supplies the missing M19-271 non-coboundary bridge.

If no, freeze the graph route and return to terminal stress tightness / zero-force stationary rigidity.

Global 3D Navier--Stokes regularity remains unproved.
