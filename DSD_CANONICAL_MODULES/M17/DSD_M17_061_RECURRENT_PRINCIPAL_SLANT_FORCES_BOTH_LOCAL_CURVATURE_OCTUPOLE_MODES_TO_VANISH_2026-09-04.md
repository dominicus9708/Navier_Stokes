# DSD M17-061 — Recurrent principal slant forces both local curvature-octupole modes to vanish

Date: 2026-09-04
Canonical ID: **M17-061**

Status: **INTERNAL PRINCIPAL-SLANT LOCAL-OCTUPOLE CLOSURE / M17-060 SHOWS THAT THE TWO PRINCIPAL-SLANT CURVATURE-OCTUPOLE MODES ARE UNFORCED: `D_BX_-=mu_-X_-`, `D_BX_+=mu_+X_+`. IN THE SAME LOCAL NODAL GAUGE USED TO DERIVE THESE LAWS, `q_3=0`, SO THE FULL VERTICAL VELOCITY DERIVATIVE `partial_3U_3=G_q q_3+G_3` REDUCES TO `G_3`. M17-010 CORE STRAIN ISOTROPY GIVES `partial_3U_3=-2lambda`, HENCE THE EXACT GAUGE-FIXED IDENTITY `G_3=-2lambda`. THEREFORE `mu_-=2kappa-7/2-lambda` AND `mu_+=2kappa-7/2+5lambda`. A UNIFORMLY RECURRENT REGULAR NODAL FILAMENT HAS `mean kappa=3/2`, AND UNIFORMLY RECURRENT NONZERO SLANT HAS `mean lambda=0`. BOTH MODE EXPONENTS THEREFORE HAVE THE STRICT NEGATIVE MEAN `-1/2`. ANY NONZERO MODE WOULD DECAY EXPONENTIALLY IN LOGARITHMIC MEAN AND CANNOT RETURN RECURRENTLY TO A STATE WHERE THAT CONTINUOUS MODE IS NONZERO. SINCE THE ZERO-MODE SETS ARE MATERIAL INVARIANT, THE ONLY UNIFORMLY RECURRENT PRINCIPAL-SLANT POSSIBILITY IS `X_-=X_+=0`. M17-058 ALSO GIVES ZERO KAPPA-GRADIENT PROJECTION ON PRINCIPAL SLANT, SO THE ENTIRE LOCAL PAYER-OCTUPOLE MISMATCH VANISHES ON THE RECURRENT PRINCIPAL BRANCH. THIS CLOSES THE NONZERO LOCAL-OCTUPOLE SUBBRANCH, NOT THE WHOLE PRINCIPAL-SLANT BRANCH: GLOBAL/MESOSCOPIC PRESSURE L=3 MOMENTS AND VISCOUS DSAIG FORCING MAY STILL SUSTAIN ALIGNMENT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Unforced principal modes

M17-060 proves

\[
\boxed{
D_BX_-
=\left(2\kappa-G_3-\frac72-3\lambda\right)X_-,
}
\]

\[
\boxed{
D_BX_+
=\left(2\kappa-G_3-\frac72+3\lambda\right)X_+.
}
\]

No additive source remains.

Consequently

\[
X_-=0
\]

and

\[
X_+=0
\]

are invariant submanifolds.

---

## 2. Nodal gauge fixes G3 by the actual core strain

M17-059 chooses the local streamfunction gauge so that

\[
q=0
\]

along the nodal filament.
Since

\[
\nabla_hq=0
\]

there, differentiation along the filament gives

\[
\boxed{q_3=0}
\]

at the marked core.

The vertical velocity law is

\[
\boxed{U_3=G(q,x_3,\theta).}
\]

Its full vertical derivative is

\[
\partial_3U_3
=G_q q_3+G_3.
\]

In the nodal gauge,

\[
\boxed{\partial_3U_3=G_3.}
\]

M17-010 gives at every regular winding node

\[
\boxed{
\nabla U
=\operatorname{diag}(\lambda,\lambda,-2\lambda).
}
\]

Therefore

\[
\boxed{
\partial_3U_3=-2\lambda.
}
\]

Combining,

\[
\boxed{G_3=-2\lambda}
\]

in this gauge.

This is not a new physical assumption. It is simply the chain-rule decomposition of the already fixed physical derivative `partial_3 U_3` after the local streamfunction gauge has set `q_3=0`.

---

## 3. Exact mode rates in nodal gauge

Substitute

\[
G_3=-2\lambda.
\]

Then

\[
\boxed{
\mu_-
=2\kappa-\frac72-\lambda,
}
\]

and

\[
\boxed{
\mu_+
=2\kappa-\frac72+5\lambda.
}
\]

Thus

\[
\boxed{
D_BX_-=\left(2\kappa-\frac72-\lambda\right)X_-,
}
\]

\[
\boxed{
D_BX_+=\left(2\kappa-\frac72+5\lambda\right)X_+.
}
\]

---

## 4. Recurrent mean exponents

For the uniformly regular recurrent nodal branch, M17-010 gives

\[
\boxed{\langle\kappa\rangle=\frac32.}
\]

For uniformly recurrent nonzero slant, M17-024 gives

\[
\boxed{\langle\lambda\rangle=0.}
\]

Hence

\[
\begin{aligned}
\langle\mu_-\rangle
&=2\cdot\frac32-\frac72-0\\
&=-\frac12,
\end{aligned}
\]

and

\[
\begin{aligned}
\langle\mu_+\rangle
&=2\cdot\frac32-\frac72+0\\
&=-\frac12.
\end{aligned}
\]

Therefore

\[
\boxed{
\langle\mu_-\rangle
=\langle\mu_+\rangle
=-\frac12<0.
}
\]

The negative drift is strict and independent of the detailed time history of `lambda`.

---

## 5. Nonzero recurrent mode contradiction

Suppose

\[
X_-(0)\ne0.
\]

The exact homogeneous law gives

\[
X_-(T)
=X_-(0)
\exp\left(
\int_0^T\mu_-(\theta)d\theta
\right).
\]

Along recurrence intervals with the audited long-time means,

\[
\frac1T\int_0^T\mu_-d\theta\to-\frac12.
\]

Hence

\[
|X_-(T)|\sim e^{-T/2}
\]

at logarithmic mean scale.
It cannot return arbitrarily close to a state with the original nonzero continuous value of `X_-`.

Therefore a uniformly recurrent branch cannot have

\[
X_-\ne0.
\]

The same argument gives

\[
X_+\ne0
\]

impossible on a uniformly recurrent branch.

Thus

\[
\boxed{
R_{principal}^{recurrent}
\Longrightarrow
X_-=X_+=0.
}
\]

---

## 6. The exact ratio invariant becomes vacuous on the recurrent branch

M17-060 derives

\[
\mathcal I_{oct}
=\frac{X_+}{P^2X_-}
\]

when both modes are nonzero.

M17-061 shows that this nonzero/nonzero subbranch cannot be uniformly recurrent.
The invariant remains correct dynamically but does not label a recurrent principal survivor.

Likewise the one-zero/one-nonzero branches are excluded because the nonzero mode has the same strict negative mean exponent.

Thus the recurrent frontier collapses to the double-zero class.

---

## 7. Entire local payer-octupole mismatch vanishes

M17-058 proves that on principal slant

\[
\boxed{\mathfrak o_\kappa=0.}
\]

M17-059/M17-060 give

\[
\mathfrak o_W
=\varepsilon_E\frac{\sqrt2\kappa_0}{15}(X_-+X_+).
\]

The recurrence closure gives

\[
X_-=X_+=0.
\]

Therefore

\[
\boxed{
\mathfrak o_{loc}
=\mathfrak o_\kappa+\mathfrak o_W
=0.
}
\]

This is the main result of the module.

---

## 8. DSD interpretation

The local payer-octupole descriptor has been pruned completely on the recurrent principal-slant branch:

\[
\boxed{
\text{principal orientation}
\to
\text{kappa-gradient silence}
\to
\text{alignment source silence}
\to
\text{strictly decaying homogeneous modes}
\to
\text{recurrent double zero}.
}
\]

The surviving pressure-lock burden is therefore displaced out of the local `kappa rho^2` octupole descriptor and into the global/mesoscopic pressure and viscous channels.

This is a descriptor transfer, not yet a total contradiction.

---

## 9. DSD audit

### Audit A — treating G3 as gauge invariant
Avoided. The identity `G_3=-2lambda` is stated in the explicit nodal gauge. The physical full derivative `partial_3U_3` is gauge invariant.

### Audit B — mixing generic-gauge mean G3 from M17-060 with the nodal gauge
Avoided. The contradiction is recomputed directly from the gauge-fixed mode rates.

### Audit C — assuming a negative mean multiplier forbids transient nonzero modes
Rejected. It forbids **uniform recurrence with a nonzero continuous mode**, not transient episodes.

### Audit D — claiming X decay is Navier--Stokes singularity
Rejected. The branch can leave principal slant, lose rank, or undergo turnover before recurrence.

### Audit E — claiming local-octupole silence means pressure-l=3 silence
Rejected. The global STF pressure tensor has independent source-production/relative-transport architecture.

### Audit F — proof status
One substantial recurrent principal subbranch is closed, but Rank-1 remains open through global pressure/viscous locking and oblique slant.

---

## 10. Updated principal-slant frontier

\[
\boxed{
R_{principal}^{recurrent}
\Longrightarrow
R_{00}^{local-oct=0}
\ \lor\
T_{nodal/rank/interface}.
}
\]

The former `R_{++}`, `R_{+0}`, and `R_{0+}` recurrent classes are closed.

---

## 11. Next target — principal global pressure/viscous lock with local-octupole silence

On the only recurrent principal survivor,

\[
\boxed{\mathfrak o_{loc}=0.}
\]

Therefore any persistent DSAIG perpendicular cancellation must be maintained entirely by

1. local viscous higher-jet forcing;
2. the explicit pressure-source-gradient trace part;
3. the global STF `l=3` pressure moment;
4. turnover/interface exits.

The next calculation should exploit the principal frame to reduce the **exact full perpendicular DSAIG balance**, not merely the payer octupole.

This is the sharpened **Principal Global-Octupole Lock Gate (PGOLG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
