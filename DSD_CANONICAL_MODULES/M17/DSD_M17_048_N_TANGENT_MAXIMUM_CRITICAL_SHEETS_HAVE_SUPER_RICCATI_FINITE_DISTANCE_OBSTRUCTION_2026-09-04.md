# DSD M17-048 — n-tangent maximum critical sheets have a super-Riccati finite-distance obstruction

Date: 2026-09-04
Canonical ID: **M17-048**

Status: **INTERNAL CRITICAL-SURFACE PERSISTENCE CLOSURE / ON THE ORTHOGONAL PURE-KERNEL RANK-TWO BRANCH, A NONDEGENERATE LINE MAXIMUM LIES ON THE REGULAR SURFACE `C={g=D_xi log rho=0}` WITH `D_xi g<0`. M17-047 GIVES `D_n q=2q^2-D_xi g>2q^2`. IF `D_n g=0`, THEN `n` IS TANGENT TO THE CRITICAL SURFACE. IF AN n-INTEGRAL CURVE REMAINS INSIDE A MAXIMUM COMPONENT OF `C`, THE STRICT DIFFERENTIAL INEQUALITY `dq/ds>2q^2` HOLDS ALONG IT. FOR ANY NONZERO INITIAL q, THE RECIPROCAL `1/q` HAS DERIVATIVE STRICTLY BELOW `-2`, SO A COMPLETE TWO-SIDED n-CURVE IS IMPOSSIBLE: ONE SIGNED DIRECTION REACHES A FINITE-DISTANCE POLE. THEREFORE A SMOOTH MAXIMUM NETWORK MUST EXIT THROUGH CRITICAL-SURFACE TILT `D_n g != 0`, FINITE PATCH TERMINATION, RANK LOSS, OR CRITICAL DEGENERATION BEFORE SUCH COMPLETENESS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Critical surface

Define

\[
\boxed{g:=D_\xi\log\rho.}
\]

At a nondegenerate linewise extremum,

\[
\boxed{g=0,\qquad D_\xi g\ne0.}
\]

Because `D_xi g` is one component of `grad g`, the implicit-function theorem gives a regular spatial surface

\[
\boxed{\mathcal C:=\{g=0\}}
\]

near the event.

For a linewise maximum,

\[
\boxed{D_\xi g<0.}
\]

For a linewise minimum,

\[
D_\xi g>0.
\]

---

## 2. Tangency of the n direction

At a point of `C`, the vector `n` is tangent to the critical surface exactly when

\[
\boxed{D_ng=0.}
\]

Indeed

\[
D_ng=\nabla g\cdot n.
\]

Thus the maximum branch splits geometrically into

\[
\boxed{
D_ng=0
\quad\text{(n-tangent maximum)}
}
\]

or

\[
\boxed{
D_ng\ne0
\quad\text{(tilted maximum surface)}.
}
\]

---

## 3. Super-Riccati law on a maximum

M17-047 gives at every nondegenerate line critical point

\[
\boxed{
D_nq=2q^2-D_\xi g.
}
\]

On a maximum,

\[
D_\xi g<0,
\]

hence

\[
\boxed{
D_nq>2q^2.
}
\]

This is pointwise on the maximum set.

---

## 4. Persisting n-tangent maximum curve

Let `gamma(s)` be an integral curve of `n`:

\[
\frac{d\gamma}{ds}=n(\gamma(s)).
\]

Assume on an interval `I` that

1. `gamma(s)` remains in one regular maximum component of `C`;
2. rank two remains active, so `q(s)!=0`;
3. the cross-aligned maximum description remains valid.

Then for all `s in I`,

\[
\boxed{
\frac{dq}{ds}>2q^2.
}
\]

This is now an interval inequality, unlike the merely pointwise result of M17-047.

---

## 5. Reciprocal comparison

Where `q!=0`, define

\[
\boxed{u:=\frac1q.}
\]

Then

\[
\frac{du}{ds}
=-\frac{q'}{q^2}.
\]

Since

\[
q'>2q^2,
\]

we obtain

\[
\boxed{u'<-2.}
\]

Therefore for `s>s_0`,

\[
u(s)<u(s_0)-2(s-s_0).
\]

For `s<s_0`, equivalently,

\[
u(s)>u(s_0)+2(s_0-s).
\]

---

## 6. Either sign of q has a finite-distance obstruction

### Case A: q(s0)>0

Then

\[
u(s_0)>0.
\]

The forward upper bound reaches zero by

\[
s-s_0\le \frac{u(s_0)}2=\frac1{2q(s_0)}.
\]

Before or at that distance, a smooth nonzero `q` satisfying the inequality cannot continue without `u` reaching zero, corresponding to unbounded `q` or exit from the assumed branch.

### Case B: q(s0)<0

Then

\[
u(s_0)<0.
\]

Moving backward, the lower bound

\[
u(s)>u(s_0)+2(s_0-s)
\]

becomes positive at finite distance.
By continuity, a branch remaining finite and nonzero would have to pass through `u=0`, again corresponding to an unbounded `q` or exit.

Thus either sign has a finite signed-direction obstruction.

---

## 7. Complete n-tangent maximum sheet is impossible

A complete two-sided `n`-integral curve lying entirely in a smooth full-rank maximum component would require finite nonzero `q` for all

\[
s\in\mathbb R.
\]

The reciprocal comparison forbids this.

Hence

\[
\boxed{
R_{2,j=0}^{maximum,\,n\text{-}tangent,\,complete}
\Longrightarrow\bot.
}
\]

This is a genuine geometric closure of a Rank-2 subbranch.

---

## 8. Allowed local exits

The result does not prohibit a finite maximum patch.
It says that before the super-Riccati focal distance, at least one assumption must fail.

The exits are

\[
\boxed{
D_ng\ne0
\ \lor\ 
\text{maximum patch termination}
\ \lor\ 
\text{rank loss}
\ \lor\ 
\nabla g=0\text{ critical degeneration}
\ \lor\ 
\text{orthogonal-branch exit}.
}
\]

Thus the generic surviving maximum network must tilt relative to the `n` direction or repeatedly undergo finite-interface events.

---

## 9. Minima are different

At a linewise minimum,

\[
D_\xi g>0,
\]

so M17-047 gives only

\[
D_nq<2q^2.
\]

This does not provide the reciprocal inequality needed for a two-sided finite-distance obstruction.

Therefore the maximum and minimum sheets are not symmetric in this audit.

---

## 10. Relation to M17-036

The closed conformal branch obeyed exactly

\[
D_n\lambda=2\lambda^2
\]

along a straight `n` line.

M17-048 shows that an anisotropic **maximum sheet** tangent to `n` is even more restrictive:

\[
D_nq>2q^2.
\]

Thus conformal Riccati focusing is not removed at maxima by unequal stretch; it becomes strictly stronger whenever the critical geometry is n-tangent.

---

## 11. DSD audit

### Audit A — applying the pointwise inequality along an arbitrary n curve
Avoided. The interval comparison is used only after explicitly assuming the n curve remains in the maximum critical surface.

### Audit B — claiming every maximum surface is n-tangent
Rejected. `D_n g != 0` is a genuine tilt escape.

### Audit C — treating the finite-distance pole as established Navier--Stokes blowup
Rejected. A local branch may exit before the pole through tilt, rank loss, interface, or degeneracy.

### Audit D — applying the same argument to minima
Rejected; the sign is insufficient.

### Audit E — proof status
One further Rank-2 subbranch is closed; the tilted maximum/minimum network remains open.

---

## 12. Updated orthogonal-stretch network

The nondegenerate oscillatory network now splits as

\[
\boxed{
R_{crit}^{orthogonal}
\Longrightarrow
R_{max}^{tilted}
\ \lor\ 
R_{min}
\ \lor\ 
T_{crit}^{degenerate}
\ \lor\ 
I_{crit}^{finite-interface}.
}
\]

The complete n-tangent maximum class is removed.

---

## 13. Next target — tilt/turnover gate

For the surviving maximum branch define the critical-surface tilt ratio

\[
\boxed{
\Theta_n:=\frac{D_ng}{|D_\xi g|}.
}
\]

A persistent maximum network avoiding the super-Riccati closure must repeatedly maintain nonzero `Theta_n` or terminate through interfaces.

The next calculation should derive the material evolution of this tilt and test whether a recurrent bounded maximum network can keep it separated from zero without creating a degenerate critical event.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
