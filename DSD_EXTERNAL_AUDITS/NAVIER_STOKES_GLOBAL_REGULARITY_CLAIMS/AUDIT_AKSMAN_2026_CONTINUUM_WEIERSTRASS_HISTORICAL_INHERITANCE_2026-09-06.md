# DSD Versioned Audit — Aksman 2026 Continuum Weierstrass Isomorphism: Historical-Inheritance Gate

Date: 2026-09-06
Target: Michael Aksman, *GLOBAL REGULARITY OF 3D NAVIER–STOKES VIA CONTINUUM WEIERSTRASS ISOMORPHISM*, Zenodo 22098919, published 2026-08-25.

## Status

**FAIL_ROOT at the historical/foundational inheritance claimed in the public architecture.**

This verdict does not purport to audit every new Weierstrass formula in the August 25 manuscript. It establishes that a central theorem imported as already proved by the 1983–1988 vorton literature is not supported by those cited sources.

---

# Public 2026 claim

The August 25 record claims an unconditional continuum proof based on:

- a Continuum Weierstrass Isomorphism;
- a Modular Coercivity Theorem;
- exact material evolutions of kinematic invariants \(Q,R\);
- a solenoidal vorton decomposition;
- and, crucially, the statement that the Constantin–Foias–Temam \(Re^{3/4}\) scaling is an **exact topological covering number**.

Related 2026 manuscripts in the same program state more strongly that the foundational vorton papers

- Novikov (1983),
- Aksman–Novikov–Orszag (1985),
- Aksman–Novikov (1988)

already establish that arbitrary 3D vorticity is irreducibly represented by vorton chains, that tube core equals inter-vorton spacing, that a Kolmogorov-scale UV floor follows, and that the 3D NSE attractor dimension is exactly \(Re^{3/4}\).

The historical sources do not support that inheritance.

---

# Source audit 1 — Novikov 1983

Novikov's 1983 paper derives ordinary differential equations for three-dimensional vortical singularities (vortons), solves the interaction of two vortons analytically, and discusses collapse and discrete analogues of vortex filaments/rings.

This is a result about a singular-vorton dynamical model and selected discrete analogues.

It is not a theorem that every smooth finite-energy 3D NSE vorticity field admits an exact vorton representation with a positive core floor or a finite-dimensional attractor.

Therefore:

\[
\boxed{
\text{vorton ODE model/discrete analogues}
\not\Rightarrow
\text{exact universal continuum NSE decomposition}.
}
\]

---

# Source audit 2 — Aksman–Novikov–Orszag 1985

The 1985 Physical Review Letters article states explicitly that the vorton method is applied to mutual penetration of two and four vorton rings.

Its full-text introduction distinguishes prior analytic work from the 1985 study and says, in substance, that the more complicated problems in that paper are investigated **numerically**.

The published abstract reports observed abrupt jumps of vorticity and major changes in energy spectra in destruction/instability of vorton rings.

Thus the 1985 paper is not an exact representation/completeness theorem for arbitrary classical NSE data.

In particular it does not prove:

\[
\boxed{
\omega(x,t)=\sum_{i=1}^{N}\Gamma_i\phi_i(x-X_i(t))\xi_i(t)
}
\]

with a universal fixed finite \(N\), nor an \(H^1\leftrightarrow\mathbb R^{3N}\) diffeomorphism for the full infinite-dimensional NSE phase space.

---

# Source audit 3 — Aksman–Novikov 1988

The 1988 paper *Reconnections of vortex filaments* studies breakdown/reconnection of vortex filaments using the vorton method in several configurations and compares the simulations with other methods and observations.

Its advertised scope is reconnection dynamics, global integrals, inviscid energy dissipation and visualization of an effective core.

That is not a proof that:

1. every smooth divergence-free NSE field is globally represented by finite-core vorton chains;
2. the effective core has a universal positive lower bound under arbitrary NSE evolution;
3. the 3D global attractor exists and has exact covering dimension \(Re^{3/4}\).

---

# Source audit 4 — the \(Re^{3/4}\) exponent is misidentified

Classical turbulence scaling gives a length-scale ratio of the form

\[
\ell_0/\ell_d\sim Re^{3/4}.
\]

If one counts three-dimensional resolution cells, the conventional number of degrees of freedom behaves as

\[
N\sim(\ell_0/\ell_d)^3\sim Re^{9/4}.
\]

Foias/Temam-related literature explicitly distinguishes these two quantities.

Hence:

\[
\boxed{
Re^{3/4}\ \text{length-scale ratio}
\neq
Re^{3/4}\ \text{exact 3D attractor covering number}.
}
\]

The exponent has been reassigned to a stronger geometric object without a theorem establishing the reassignment.

---

# Source audit 5 — a general finite-dimensional 3D NSE attractor is not available to inherit

The mathematical attractor theory is rigorous in 2D. For the general 3D NSE, the usual finite-dimensional global-attractor route cannot simply be completed because global regularity remains open.

Modern literature explicitly notes that the 2D finite-dimensional-attractor program cannot be transferred as an established theorem to general 3D NSE while the Millennium regularity problem remains unresolved.

Therefore the phrase

\[
\boxed{
\text{"the exact dimension of the 3D NS attractor is }Re^{3/4}\text{"}
}
\]

cannot be imported as a classical Constantin–Foias–Temam theorem for arbitrary 3D NSE.

Doing so presupposes an object whose strong global regularity/compact attractor structure is itself part of the unresolved problem.

---

# DSD classification of the error

This is an **inheritance-strength error**:

\[
\text{historical model/simulation/scaling result}
\xrightarrow{\text{silent upgrade}}
\text{universal exact continuum theorem}.
\]

The upgrade changes all of the following:

- model class: finite/discrete singular vortons -> arbitrary smooth NSE fields;
- statement type: numerical/selected dynamics -> universal analytic representation;
- scale meaning: Kolmogorov length ratio -> topological covering number;
- existence level: heuristic/conditional turbulent attractor -> exact global 3D NSE attractor.

No citation can carry that larger theorem unless the missing bridge is itself proved.

---

# Consequence for the Aug. 25 Weierstrass proof

The public Aug. 25 architecture consumes the vorton decomposition and \(Re^{3/4}\) covering claim as foundations for modular coercivity and pressure control.

Since those foundations are not established by the cited 1983–1988 literature, the manuscript must independently prove at minimum:

1. an exact, convergent, norm-faithful vorton decomposition for every relevant NSE state;
2. compatibility of that representation with classical NSE time evolution;
3. no loss under dense-chain/continuum limits;
4. the claimed topological covering theorem from standard NSE quantities;
5. a proof that the covering object exists without presupposing global regularity.

Until then, the unconditional conclusion does not follow from the cited historical foundation.

---

# Additional Weierstrass-isomorphism firewall

Even if a 3D Biot–Savart kernel and the Weierstrass \(\wp\)-function both exhibit inverse-power singular behavior, matching singularity order is not an isomorphism theorem.

A valid continuum Weierstrass reduction must establish a map that preserves, in both directions:

- the 3D vector/tensor structure;
- incompressibility;
- the full nonlinear convolution/triad structure;
- relevant Sobolev/critical norms;
- time evolution;
- continuum scale information.

This remains a separate formula-level obligation and is not declared failed here solely from the public abstract.

---

# Survivor

The historical vorton papers remain legitimate studies of vortex-singularity dynamics and vortex-filament reconnection. Their value does not depend on converting them into a universal NSE representation theorem.

---

# M17 regression test

### R28 — Citation inheritance must preserve theorem strength

Whenever M17 imports an older result, record:

\[
\boxed{
\text{object class} + \text{quantifiers} + \text{norm} + \text{limit} + \text{domain}.
}
\]

A numerical model, a special-solution theorem, a scaling law, and a universal continuum PDE theorem are not interchangeable merely because their formulas share an exponent or kernel singularity.

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
