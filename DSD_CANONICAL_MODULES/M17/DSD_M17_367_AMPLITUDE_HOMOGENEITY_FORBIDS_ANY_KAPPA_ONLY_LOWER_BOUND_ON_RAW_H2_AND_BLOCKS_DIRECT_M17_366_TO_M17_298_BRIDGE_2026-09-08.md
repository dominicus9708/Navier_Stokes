# DSD M17-367 — Amplitude homogeneity forbids any kappa-only lower bound on raw H2 and blocks a direct M17-366 to M17-298 bridge

Date: 2026-09-08  
Canonical ID: **M17-367**

Status: **ACTIVE NO-GO / AMPLITUDE FIREWALL REASSERTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. CE-H elliptic homogeneity

The exact CE-H coefficient equation is

\[
\boxed{\Delta W=\kappa W.}
\]

For any constant amplitude factor

\[
\varepsilon>0,
\]

define

\[
W_\varepsilon:=\varepsilon W.
\]

Then

\[
\Delta W_\varepsilon
=
\varepsilon\Delta W
=
\kappa(\varepsilon W)
=
\kappa W_\varepsilon.
\]

Therefore

\[
\boxed{
\kappa[W_\varepsilon]=\kappa[W].
}
\]

The coefficient field is invariant under uniform amplitude rescaling of the CE-H eigenfunction.

## 2. Critical coefficient mass is amplitude blind

The M17-310/M17-366 critical coefficient measure is

\[
K_-
:=
\int\kappa_-^{3/2}dx.
\]

Under `W -> epsilon W`,

\[
\boxed{K_-[W_\varepsilon]=K_-[W].}
\]

The same is true of every descriptor built only from `kappa` and its spatial geometry after the corresponding coordinate scale is fixed.

## 3. Raw enstrophy and raw H2 are amplitude weighted

By contrast,

\[
E[W]
:=
\int|W|^2dx
\]

obeys

\[
\boxed{E[W_\varepsilon]=\varepsilon^2E[W].}
\]

Likewise the raw `H2`/Laplacian charge

\[
H[W]
:=
\int|\Delta W|^2dx
=
\int\kappa^2|W|^2dx
\]

satisfies

\[
\boxed{H[W_\varepsilon]=\varepsilon^2H[W].}
\]

The same amplitude factor multiplies local packet versions of these quantities.

## 4. No kappa-only positive lower bound for raw H2

Suppose one attempted an estimate of the form

\[
H[W]
\ge
F(K_-[W])
\]

with

\[
F(c)>0
\]

for some positive critical coefficient mass `c`.

Apply it to `W_epsilon`:

\[
\varepsilon^2H[W]
\ge
F(K_-[W]).
\]

Letting

\[
\varepsilon\to0
\]

contradicts any strictly positive right-hand side.

Hence

\[
\boxed{
\text{there is no amplitude-independent positive lower bound on raw }H^2
\text{ from }\kappa_-^{3/2}\text{ mass alone.}
}
\]

This is an exact algebraic obstruction, not merely a missing estimate.

## 5. Consequence for the M17-366 concentration branches

M17-366 organizes the moving nodal critical coefficient mass into compact, strict-subscale, escape, and diffuse-multiplicity branches.

It is tempting to send every fixed critical coefficient cluster directly into the M17-298 raw-`H2` allocation problem.

Section 4 forbids that shortcut.

Thus

\[
\boxed{
H_{critical\ coefficient\ cluster}
\not\Rightarrow
H_{fixed\ raw\ H2\ packet\ charge}
}

without an additional amplitude/flux/line-weight bridge.

## 6. Ratio quantities do not automatically fix the problem

The amplitude factor cancels from

\[
\frac{H}{E}
=
\frac{\int\kappa^2|W|^2}{\int|W|^2}.
\]

However the unweighted coefficient mass

\[
\int\kappa_-^{3/2}
\]

does not control this amplitude-weighted ratio, because the large coefficient may live precisely where `|W|` is small.

Therefore

\[
\boxed{
K_-\text{ large}
\not\Rightarrow
H/E\text{ large}
}

without a coefficient--amplitude correlation theorem.

This is the same amplitude firewall already seen in M17-233--235, now stated as an exact homogeneity no-go.

## 7. What a valid bridge must contain

Any future bridge from coefficient concentration to raw `H2` must break the amplitude homogeneity using at least one independent datum such as

\[
\boxed{
\text{material flux floor},
}
\]

\[
\boxed{
\text{high-amplitude capture},
}

\[
\boxed{
\text{line-weight/residence lower bound},
}

\[
\boxed{
\text{packet }L^2\text{ mass floor},
}
\]

or a genuine PDE theorem coupling coefficient concentration to amplitude return.

M17-340--346 and M17-363--364 are examples of bridges that explicitly insert such information rather than using `kappa` alone.

## 8. DSD-theory role

The heuristic is to audit whether the proposed descriptor changes under a symmetry that leaves the claimed cause unchanged. The proof is the elementary homogeneity of the CE-H elliptic equation.

No DSD axiom is used as a PDE hypothesis.

## 9. Updated frontier

The strict-subscale/diffuse coefficient branches of M17-366 cannot be closed by a direct coefficient-only import into M17-298.

The correct next target is instead

\[
\boxed{
\text{coefficient concentration}
+
\text{independent flux/amplitude carrier}
\Longrightarrow
\text{raw }H2\text{ allocation or another critical physical currency}.
}
\]

Absent such a carrier, the amplitude firewall is exact.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
