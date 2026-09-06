# DSD Audit — Pompetzki Claimed ZFC Independence of Navier–Stokes Regularity

Date: 2026-09-06
Source family: Christopher Michael Pompetzki, *The Independence of Navier-Stokes Global Regularity from ZFC*, Zenodo 18292041 / 18292042, Jan 2026.
Audit status: **METAMATHEMATICAL CATEGORY ERROR**

## 1. Claimed structure

The manuscript argues two directions:

1. ZFC cannot prove global regularity because classical energy/critical estimates do not close the vortex-stretching gap.
2. ZFC cannot prove finite-time blow-up because a blow-up proof would allegedly “relativize” to a hyperdissipative family, contradicting known regularity for sufficiently strong fractional dissipation.

The manuscript compares the proposed obstruction with oracle-relativization barriers in complexity theory.

## 2. Failure-of-method versus independence

A mathematical statement `Φ` is independent of ZFC only after establishing, relative to appropriate consistency assumptions, that neither `Φ` nor `¬Φ` is provable in ZFC.

Showing that several known analytic methods fail to prove `Φ` establishes at most

\[
\text{those methods do not currently close }\Phi.
\]

It does not establish

\[
ZFC\nvdash\Phi.
\]

There may be other analytic, geometric, logical, or combinatorial proofs formalizable in ZFC.

Thus:

\[
\boxed{
\text{methodological barrier}\neq\text{formal unprovability}.
}
\]

## 3. Hyperdissipation “relativization” audit

Consider a family

\[
\partial_tu+(u\cdot\nabla)u+\nabla p
=-(-\Delta)^\alpha u.
\]

The fact that sufficiently strong dissipation has known regularity does not imply that any hypothetical proof of blow-up at `α=1` must transfer to other values of `α`.

The PDE changes with α. A proof can use an identity, scaling, instability, or self-similar mechanism specific to one exponent. No analogue of a complexity-theoretic oracle-relativization theorem is supplied merely by placing the equations in a parameterized family.

Therefore

\[
\boxed{
\text{blow-up proof at }\alpha=1
\not\Rightarrow
\text{blow-up proof at }\alpha>5/4.
}
\]

without a separate robustness theorem.

## 4. Euler premise audit

The manuscript's analogy treats the low/no-dissipation end as if classical smooth 3D Euler finite-time singularity were already proved. For smooth finite-energy, boundaryless 3D Euler data, the general blow-up/global-regularity question remains open. Rigorous blow-up results in bounded-domain/axisymmetric settings or at reduced regularity do not establish the unrestricted smooth boundaryless case.

Thus an input premise used to draw the “regular on one side / singular on the other” independence-zone picture is not valid in the stated generality.

## 5. What a genuine independence proof would require

A valid independence result would need genuine metamathematical content, for example a relative-consistency/model construction showing:

\[
\operatorname{Con}(ZFC)\Rightarrow\operatorname{Con}(ZFC+\Phi)
\]

and

\[
\operatorname{Con}(ZFC)\Rightarrow\operatorname{Con}(ZFC+\neg\Phi),
\]

or another accepted proof-theoretic route. An analogy with barriers or failure of PDE estimates is not a substitute.

## 6. Surviving value

The manuscript correctly emphasizes genuine analytic facts:

- ordinary energy control alone does not settle vortex stretching;
- criticality of the standard dissipation matters;
- hyperdissipative models can have different regularity behavior;
- proof methods can fail to transfer uniformly across model parameters.

These observations support a “method barrier” discussion, not a ZFC-independence theorem.

## 7. DSD verdict

\[
\boxed{
\text{The stated arguments do not prove ZFC independence.}
}
\]

The central error is a category shift from analytic difficulty/non-robustness to formal logical unprovability.

Navier–Stokes global regularity remains an open mathematical problem under the standard accepted baseline.
