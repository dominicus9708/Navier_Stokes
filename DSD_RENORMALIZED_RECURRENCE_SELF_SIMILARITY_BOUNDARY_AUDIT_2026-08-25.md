# DSD renormalized recurrence / self-similarity boundary audit

Date: 2026-08-25

Status: **FIRST-HITTING SCALE RATIO IDENTIFIED WITH DSS FACTOR / SNAPSHOT RECURRENCE SHOWN WEAKER THAN DSS / EXACT SELF-SIMILAR LIOUVILLE RESULTS NOT AUTOMATICALLY APPLICABLE / GLOBAL REGULARITY UNPROVED.**

This note continues `DSD_CSTCG_PARABOLIC_RENORMALIZATION_AUDIT_2026-08-25.md` and reconnects it to the repository's ancient-solution branch.

## 1. First-hitting scaling factor

Let

\[
W_{j+1}=qW_j,
\qquad
q>1,
\]

and

\[
r_j=\left(\frac{\nu}{W_j}\right)^{1/2}.
\]

Then

\[
\boxed{
r_{j+1}=q^{-1/2}r_j.}
\]

Define

\[
\boxed{\lambda:=\sqrt q>1.}
\]

Hence

\[
\boxed{r_{j+1}=\lambda^{-1}r_j.}
\]

The natural velocity scale is

\[
\frac{\nu}{r_j},
\]

so from one generation to the next it changes by

\[
\frac{\nu/r_{j+1}}{\nu/r_j}=\lambda.
\]

The natural parabolic time scale is

\[
\frac{r_j^2}{\nu},
\]

so it changes by

\[
\frac{r_{j+1}^2}{r_j^2}=\lambda^{-2}=q^{-1}.
\]

Thus the first-hitting renormalization has exactly the Navier-Stokes discrete scaling dimensions

\[
\boxed{
x\mapsto\lambda x,
\qquad
t\mapsto\lambda^2t,
\qquad	u\mapsto\lambda u,
\qquad\omega\mapsto\lambda^2\omega.
}
\]

Status: **PROVED algebraically.**

## 2. What exact block recurrence would imply

Normalize a spacetime block by

\[
U_j(y,\tau)
:=\frac{r_j}{\nu}
 u\left(X_j+r_jy,
 t_j+\frac{r_j^2}{\nu}\tau\right).
\]

Suppose, much more strongly than currently proved, that for all late `j`

\[
U_{j+1}(y,\tau)=U_j(y,\tau)
\]

on a common normalized spacetime block, with centers and time origins coherently tied to one limiting singular center/time.

Then undoing the normalization gives the discrete Navier-Stokes scaling relation with factor

\[
\lambda=\sqrt q.
\]

In that strong coherent setting, a stationary normalized block is a backward discretely self-similar candidate.

If the normalized flow is stationary also with respect to continuous similarity time rather than only the discrete generation shift, the candidate reduces further to a Leray backward self-similar profile.

Status: **PROVED AS A SCALING IMPLICATION UNDER THE STATED STRONG RECURRENCE/COHERENCE HYPOTHESIS.**

## 3. Snapshot recurrence is not DSS

The repository has various recurrence and compactness statements for finite normalized channels. None should be silently upgraded to the full block identity above.

The following are strictly weaker:

\[
U_{j_n}(\cdot,0)\to U_*(\cdot),
\]

or

\[
\Omega_{j_n}(\cdot,0)\to\Omega_*(\cdot),
\]

or recurrence of finitely many scalar descriptors.

Backward DSS requires a spacetime scaling identity, not merely similarity of selected snapshots.

Additional information would be needed about

1. normalized evolution between first hits;
2. center drift;
3. time-origin coherence relative to one `T^*`;
4. pressure/gauge compatibility;
5. global spatial tail behavior.

Therefore

\[
\boxed{
\text{snapshot recurrence}
\not\Longrightarrow
\text{backward DSS}.
}
\]

Status: **PROVED AS A LOGICAL NON-IMPLICATION.**

## 4. External self-similar exclusion boundary

Nečas--Růžička--Šverák proved that a Leray backward self-similar profile in `L^3(R^3)` is trivial. Tsai substantially extended the nonexistence theory, including profiles satisfying local energy estimates.

There are also nonexistence results for asymptotically discretely self-similar scenarios under additional integrability/regularity hypotheses, and partial removal results for discretely self-similar singularities in restricted parameter regimes.

These results are genuine external constraints, but their hypotheses cannot be imported automatically into the present bounded-`Z` branch.

In particular, the present first-hitting construction does not yet prove a global `L^3`-bounded recurrent profile.

## 5. Existing ancient `L^3` audit already identifies the escape

The repository's `ANCIENT_L3_TAIL_NECESSITY_2026-08-20.md` uses the Albritton--Barker ancient Liouville theorem to show that a nontrivial restricted Type-I ancient survivor cannot remain globally bounded in `L^3` along a backward sequence.

Thus a nontrivial survivor must retain a global critical tail whose `L^3` mass escapes the compact normalized core.

This means that the exact hypothesis which would allow a simple `L^3` Liouville closure is precisely one of the quantities the current survivor is forced to lose.

Hence

\[
\boxed{
\text{compact active core recurrence}
+
\text{global }L^3\text{ tail escape}
}
\]

is not contradicted by the classical self-similar theorem merely because the core looks recurrent.

## 6. DSD distinction: formed local recurrence versus unformed global identity

DSD requires separate channels for

- local normalized field recurrence;
- center/time provenance;
- spacetime block recurrence;
- global tail control;
- exact discrete scaling identity.

A local recurrent core and a global non-tight tail cannot be composed into `one DSS solution` unless the required global role and scaling identities are themselves formed.

This prevents the invalid implication

\[
\boxed{
\text{recurrent normalized core}
\Longrightarrow
\text{classically excluded self-similar solution}.
}
\]

The correct implication is conditional:

\[
\boxed{
\text{coherent global spacetime recurrence}
+
\text{appropriate critical tail control}
\Longrightarrow
\text{DSS/self-similar regime where external rigidity may apply}.
}
\]

## 7. Corrected fork after the parabolic audit

The bounded-`Z` branch now has a sharper two-way normalized fork.

### Branch R: renormalized compact/recurrent behavior

The normalized fields remain order one on fixed bases and admit recurrent or convergent spacetime germs.

Then the proof obligation is to upgrade the local germ far enough toward a global ancient/DSS object to trigger an existing Liouville theorem, or to show that the required global `L^3` tail is incompatible with the recurrent active core.

### Branch E: renormalized escape

Compactness fails in a formed normalized channel.

Then the escape must be represented by a finite witness such as

- spatial/tail escape;
- derivative escape;
- normalized temporal block drift;
- center/genealogy drift;
- another scale-invariant channel.

This branch cannot be replaced by the vague phrase `noncompact behavior` without an explicit finite witness.

## 8. New strategic gate

The corrected primitive question is therefore

\[
\boxed{
\text{Can a bounded-}Z\text{ first-hitting singular branch sustain}\
\text{an order-one recurrent normalized active core while the global critical tail}\
\text{escapes every Liouville class needed to exclude the corresponding ancient/DSS profile?}
}
\]

Call this the **Core--Tail Renormalized Compatibility Gate (CTRCG)**.

This gate reuses the repository's existing ancient-tail/genealogy work rather than restarting an infinite derivative escalation.

Current status:

\[
\boxed{\text{CTRCG: NOT DERIVED.}}
\]

## 9. Audit verdict

### PROVED

- first-hitting factor `q` corresponds to discrete Navier-Stokes scaling factor `lambda=sqrt(q)`;
- exact coherent block recurrence would produce a DSS-type scaling structure;
- snapshot/scalar recurrence alone is weaker than DSS;
- the current nontrivial ancient survivor is not known to satisfy the global `L^3` hypothesis that closes classical self-similar Liouville routes;
- the ancient `L^3` tail escape is therefore a real surviving channel, not a bookkeeping artifact.

### NOT DERIVED

- global spacetime DSS recurrence;
- bounded global `L^3` recurrence;
- incompatibility of recurrent core with the required critical tail;
- CTRCG;
- contradiction to the bounded-`Z` singular branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
