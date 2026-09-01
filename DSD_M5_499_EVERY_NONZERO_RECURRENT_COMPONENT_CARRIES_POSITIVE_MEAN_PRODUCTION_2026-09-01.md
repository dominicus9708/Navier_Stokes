# DSD M5-499 — Every nonzero recurrent component carries positive mean axial production

Date: 2026-09-01

Status: **PARTIAL COMPONENT COUPLING / M5-498 CORRECTLY WARNS THAT POSITIVE PRODUCTION, DUAL ACTIVITY, AND RATCHET ACTIVITY NEED NOT ALL OCCUR ON ONE ERGODIC COMPONENT / HOWEVER THE EXACT M5-486 SIMILARITY-ENSTROPHY BALANCE APPLIES TO EVERY INVARIANT COMPONENT SEPARATELY / ANY COMPONENT SUPPORTING A DUAL-FLUX MARK OR A RATCHET MARK IS NECESSARILY NONZERO, AND THEREFORE HAS STRICTLY POSITIVE MEAN AXIAL VORTEX-STRETCHING PRODUCTION / THUS THERE EXISTS A RECURRENT DUAL+PRODUCTION COMPONENT AND A RECURRENT RATCHET+PRODUCTION COMPONENT; ONLY THE DUAL+RATCHET INTERSECTION REMAINS UNRESOLVED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Ergodic decomposition of the common invariant measure

Let the common M5-485/M5-498 invariant suspension measure be

\[
\widehat\mu
=
\int \nu_\alpha\,d\pi(\alpha),
\]

where each `nu_alpha` is an ergodic invariant probability measure on a recurrent component.

M5-498 records positive global means for

- dual activity `d`;
- ratchet activity `r`;
- and total production `Q`.

The first two could, in principle, live on distinct ergodic components.

---

## 2. Componentwise similarity-enstrophy identity

For every invariant component on which the similarity solution belongs to the retained finite-enstrophy Type-I class,

\[
\frac12E'
+
\frac14E
+
P
=
Q.
\]

Invariance of `nu_alpha` gives

\[
\boxed{
\frac14\langle E\rangle_{\nu_\alpha}
+
\langle P\rangle_{\nu_\alpha}
=
\langle Q\rangle_{\nu_\alpha}.
}
\]

All terms on the left are nonnegative.

---

## 3. Nonzero component implies positive production

Suppose a component is nonzero in the vorticity sense:

\[
\nu_\alpha(E>0)>0.
\]

By ergodicity and invariance, its mean enstrophy is then strictly positive:

\[
\langle E\rangle_{\nu_\alpha}>0.
\]

Hence

\[
\boxed{
\langle Q\rangle_{\nu_\alpha}
\ge
\frac14\langle E\rangle_{\nu_\alpha}
>0.
}
\]

Therefore

\[
\boxed{
\text{every nonzero recurrent component}
\Longrightarrow
\text{positive mean axial production}.
}
\]

No extra dual or ratchet hypothesis is needed for this implication.

---

## 4. Dual component is automatically a production component

If

\[
\langle d\rangle_{\nu_\alpha}>0,
\]

then the component contains recurrent fixed-flux noncollinear vorticity carriers.

Therefore it is nonzero.

By Section 3,

\[
\boxed{
\langle d\rangle_{\nu_\alpha}>0
\Longrightarrow
\langle Q\rangle_{\nu_\alpha}>0.
}
\]

Moreover M5-492--493 apply on such a dual component and give

\[
\boxed{
\langle P\rangle_{\nu_\alpha}
\ge p_{mean,\alpha}>0.
}
\]

Thus every positive-dual component is actually a

\[
\boxed{
\text{dual + palinstrophy + production recurrent component}.
}
\]

---

## 5. Ratchet component is automatically a production component

If

\[
\langle r\rangle_{\nu_\beta}>0,
\]

then the active carrier satisfies a nonzero projective/directional action on a positive invariant set.

In particular the vorticity cannot vanish identically on that component.

Hence

\[
\boxed{
\langle r\rangle_{\nu_\beta}>0
\Longrightarrow
\langle Q\rangle_{\nu_\beta}>0.
}
\]

Thus every positive-ratchet component is a

\[
\boxed{
\text{ratchet + production recurrent component}.
}
\]

M5-487 still prevents converting the directional-tension part of `r` directly into a global direction-Dirichlet lower bound.

---

## 6. What remains genuinely uncoupled

The only missing component intersection is

\[
\boxed{
\text{dual activity}
\cap
\text{ratchet activity}.
}
\]

Positivity of their global means does not force an ergodic component with both.

Therefore the accurate alternatives are

### Same-component realization

There exists `nu_*` with

\[
\langle d\rangle_{\nu_*}>0,
\qquad
\langle r\rangle_{\nu_*}>0.
\]

Then that one component also has

\[
\langle P\rangle_{\nu_*}>0,
\qquad
\langle Q\rangle_{\nu_*}>0.
\]

### Split-component realization

Dual and ratchet activity live on different recurrent components, each of which independently has positive production.

This split is not contradictory.

---

## 7. Strengthened dual-component threshold

On every dual ergodic component, M5-494 can be repeated componentwise.

If

\[
E\le Z_{*,\alpha}
\]

on that component and

\[
\langle P\rangle_{\nu_\alpha}
\ge p_{mean,\alpha},
\]

then

\[
\boxed{
Z_{*,\alpha}
\ge
C_*^{-4/3}
p_{mean,\alpha}^{1/3}.
}
\]

Thus the quantitative critical-enstrophy threshold is not merely a global-measure statement; every recurrent dual component separately satisfies it.

---

## 8. Componentwise payer dichotomy

Likewise M5-496 applies to every dual component.

Each positive-dual ergodic component satisfies either

\[
\boxed{
H_{tail}^{remote-E}
}

through failure of enstrophy tightness, or

\[
\boxed{
L_{payer}^{local}
}

with recurrent positive local production in a fixed ball.

On the tight branch M5-497 then reduces that component to a finite persistent lineage production network.

Thus the dual side of the hard core can be studied componentwise without first solving the ratchet-intersection problem.

---

## 9. Ratchet component split

For a positive-ratchet ergodic component, split the ratchet observable into tilt and directional-diffusion/tension parts:

\[
r
\le r_{tilt}+r_{diff}.
\]

At least one has positive mean on a positive-ratchet component:

\[
\boxed{
\langle r_{tilt}\rangle>0
\lor
\langle r_{diff}\rangle>0.
}
\]

The component simultaneously has

\[
\langle Q\rangle>0.
\]

This creates two ratchet-production subproblems:

1. recurrent axial production + recurrent projective strain tilt;
2. recurrent axial production + recurrent weighted harmonic-map tension.

These can be attacked independently of the dual component if the ergodic split persists.

---

## 10. Updated component frontier

The invariant hard core is now decomposed into recurrent component types:

\[
\boxed{
\mathcal C_{dual}:
\quad
\langle d\rangle>0,
\quad
\langle P\rangle>0,
\quad
\langle Q\rangle>0,
}
\]

and

\[
\boxed{
\mathcal C_{ratchet}:
\quad
\langle r\rangle>0,
\quad
\langle Q\rangle>0.
}
\]

They may coincide.

If they do not, the proof attempt must exclude both component classes separately or prove a dynamical coupling theorem between them.

---

## 11. Highest-value next targets

### D-component target

Continue M5-496--498 on one positive-dual ergodic component, where all required dual palinstrophy and production now coexist automatically.

### R-component target

Derive a componentwise balance for the ratchet split

\[
D_\theta\xi
=\tau+\mathcal D_\xi
\]

and determine whether positive mean tilt/tension plus positive mean axial production forces a third recurrent critical norm.

The dual-ratchet intersection can be postponed unless one of the separate components survives all dedicated rigidity audits.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
