# DSD M5-194S — Two-Leray-Clock Alignment and Alpha-Limit Speed-Floor Transfer

Date: 2026-08-29

Parent: `DSD_M5_194R_PERIOD_AVERAGED_STRESS_FLUX_AND_EFFECTIVE_LANDAU_FORCE_AUDIT_2026-08-29.md`

Status: **CLOCK-SEPARATION CORRECTION + POSITIVE ASYMPTOTIC TRANSFER / THE PINEAU--VICOL LOCAL SPEED FLOOR LIVES IN THE LERAY CLOCK CENTERED AT THE ACTUAL CANDIDATE SINGULAR TIME, WHILE M5-194K'S BACKWARD ALPHA FLOW USES A CLOCK CENTERED AT A FIRST-HITTING CHECKPOINT / THESE CLOCKS MUST NOT BE IDENTIFIED AT FINITE BACKWARD TIME / ON THE TYPE-I FIRST-HITTING TOWER THE ACTUAL SINGULAR TIME IS ONLY `O(1)` STAGE UNITS AHEAD, SO AT CHECKPOINT AGE `a=|tau|->infinity` THE TWO CLOCKS, COORDINATES, AND SCALING GENERATORS DIFFER BY `O(1/a)` UNDER THE EXISTING DERIVATIVE CORRIDOR / HENCE THE SINGULARITY-CENTERED POSITIVE LOCAL LERAY-SPEED FLOOR PASSES TO ANY STRONGLY COMPACT BACKWARD CHECKPOINT ALPHA-LIMIT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Two distinct similarity clocks

Let the physical candidate singular time be `T*` and the limiting spatial center be `X*`.

At first-hitting generation `j`, use

\[
r_j=W_j^{-1/2},
\]

and define stage variables

\[
y=\frac{x-X_*}{r_j},
\qquad
\tau=\frac{t-t_j}{r_j^2},
\qquad
U_j(y,\tau)=r_j u(X_*+r_jy,t_j+r_j^2\tau).
\]

The first-hitting checkpoint is at

\[
\tau=0.
\]

The actual candidate singular time appears at

\[
\boxed{
\kappa_j
:=
\frac{T^*-t_j}{r_j^2}
=W_j(T^*-t_j)>0.
}
\]

Thus the two relevant Leray clocks are different.

### Checkpoint-centered clock

For `tau<0`, set

\[
a:=-\tau>0,
\]

\[
\boxed{
s_0=-\log a,}
\]

\[
\xi_0=\frac y{\sqrt a},
\qquad
V_0(\xi_0,s_0)=\sqrt a\,U_j(y,\tau).
\]

This is the clock used in M5-194K to study the backward alpha-limit.

### Singularity-centered clock

Set

\[
b:=\kappa_j-\tau=a+\kappa_j,
\]

\[
\boxed{
s_*=-\log b,}
\]

\[
\xi_*=\frac y{\sqrt b},
\qquad
V_*(\xi_*,s_*)=\sqrt b\,U_j(y,\tau).
\]

This is the clock corresponding to the actual candidate singular time `T*` and is the one relevant to the Pineau--Vicol one-slice criterion.

Therefore

\[
\boxed{s_0\ne s_*}
\]

at finite backward age.

---

## 2. The singular time is `O(1)` stage units ahead

The established first-hitting parabolic nesting gives

\[
T^*-t_j\asymp r_j^2.
\]

Hence there exist constants independent of late `j` such that

\[
\boxed{
0<\kappa_-\le\kappa_j\le\kappa_+<\infty.
}
\]

This boundedness is the key scale separation.

At an old backward checkpoint,

\[
a=|\tau_{j,m}|\asymp q^m\to\infty.
\]

Thus

\[
\boxed{
\frac{\kappa_j}{a}\to0.
}
\]

---

## 3. Clock alignment

At the same physical stage point,

\[
s_*-s_0
=-\log(a+\kappa_j)+\log a
=-\log\left(1+\frac{\kappa_j}{a}\right).
\]

Therefore

\[
\boxed{
|s_*-s_0|
\le C\frac{\kappa_j}{a}
}
\]

for large `a`.

Hence

\[
\boxed{
s_*-s_0\to0}
\]

uniformly along the old-generation Type-I checkpoints.

The same remains true on every fixed translated similarity-time window around such a checkpoint because multiplying `a` by a bounded factor does not alter `kappa_j/a -> 0`.

---

## 4. Coordinate and amplitude alignment

The spatial variables satisfy

\[
\boxed{
\xi_*
=
\left(1+\frac{\kappa_j}{a}\right)^{-1/2}\xi_0.
}
\]

Hence on every fixed similarity ball,

\[
\xi_*-\xi_0
=O\left(\frac{\kappa_j}{a}\right).
\]

The normalized velocities satisfy

\[
V_*
=
\left(1+\frac{\kappa_j}{a}\right)^{1/2}V_0
\]

after accounting for the coordinate rescaling above.

Therefore, under the already used local derivative compactness,

\[
\boxed{
V_*-V_0
=O_{loc}\left(\frac{\kappa_j}{a}\right).
}
\]

Thus the two profile snapshots become identical in the backward alpha-limit.

---

## 5. The two scaling generators

For the checkpoint-centered scaling define

\[
\boxed{
\mathcal Z_0[U]
:=
U+y\cdot\nabla U+2\tau U_\tau.
}
\]

A direct differentiation gives

\[
\boxed{
\partial_{s_0}V_0
=-\frac12\sqrt a\,\mathcal Z_0[U].
}
\]

For the singularity-centered scaling define

\[
\boxed{
\mathcal Z_*[U]
:=
U+y\cdot\nabla U
+2(\tau-\kappa_j)U_\tau.
}
\]

Then

\[
\boxed{
\partial_{s_*}V_*
=-\frac12\sqrt b\,\mathcal Z_*[U].
}
\]

Their unnormalized generators differ exactly by

\[
\boxed{
\mathcal Z_*[U]-\mathcal Z_0[U]
=-2\kappa_j U_\tau.
}
\]

This is the finite-time origin error.

---

## 6. Derivative scale makes the generator error vanish

On the Type-I analytic/derivative corridor, the old-stage time derivative has the natural parabolic size

\[
|U_\tau|
\lesssim a^{-3/2}
\]

on fixed similarity balls after conversion to the backward scale.

Consequently

\[
\sqrt a\,
|\mathcal Z_* -\mathcal Z_0|
\lesssim
\kappa_j a^{-1}.
\]

Together with the amplitude/coordinate difference,

\[
\boxed{
\|\partial_{s_*}V_*-\partial_{s_0}V_0\|_{X(B_R)}
\le
C_R\frac{\kappa_j}{a}
}
\]

for any fixed local norm controlled by the compactness corridor.

Therefore

\[
\boxed{
\partial_{s_*}V_*
-
\partial_{s_0}V_0
\to0
}
\]

at old backward checkpoints.

---

## 7. Import the existing singularity-centered speed floor

On the spatial-Type-I/pressure-annulus singular corridor, the Pineau--Vicol contrapositive already gives a fixed core ball and constant

\[
R_{PV}<\infty,
\qquad
\sigma_{PV}>0
\]

such that the actual singularity-centered Leray orbit satisfies

\[
\boxed{
\|\partial_{s_*}V_*\|_{L^2(B_{R_{PV}})}
\ge\sigma_{PV}
}
\]

at every sufficiently late physical similarity time.

The old first-hitting checkpoints used in the diagonal construction still correspond to physical times tending to `T*` when the terminal generation `j` is sent to infinity before/along with the backward age in the standard diagonal manner.

Thus the speed floor applies to those finite-stage checkpoints.

---

## 8. Transfer to the checkpoint-centered backward profiles

For sufficiently old checkpoint age `a`, the clock-alignment estimate gives

\[
\|\partial_{s_0}V_0\|_{L^2(B_{R_{PV}})}
\ge
\sigma_{PV}
-
C\frac{\kappa_j}{a}.
\]

Hence, after increasing the backward age,

\[
\boxed{
\|\partial_{s_0}V_0\|_{L^2(B_{R_{PV}})}
\ge
\frac12\sigma_{PV}.
}
\]

The same estimate holds on every fixed translated `s_0` window around an old checkpoint, after harmless enlargement of the fixed ball to account for the vanishing coordinate mismatch.

---

## 9. Passage to a checkpoint alpha-limit

Let

\[
V_m^{tr}(\xi,\sigma)
:=V_0(\xi,s_m+\sigma)
\]

be the checkpoint-translated profiles from M5-194L.

Assume the strong local compactness needed to pass one time derivative on fixed balls, or enough equation compactness to recover it in the limit.

Then any alpha-limit `V_alpha` satisfies

\[
\boxed{
\|\partial_\sigma V_\alpha(\cdot,\sigma)\|_{L^2(B_{R_{PV}})}
\ge
\sigma_\alpha>0
}
\]

for every finite `sigma`, with for example

\[
\sigma_\alpha=\sigma_{PV}/2
\]

up to the final compactness-loss constants.

Thus every compact alpha-limit on the pure spatial-Type-I singular corridor is **uniformly dynamically active**.

---

## 10. Consequences

### Stationary alpha-limit

Immediately impossible, consistently with M5-194L.

### Periodic alpha-limit

Not excluded by the speed floor alone. A periodic orbit may move at nonzero speed for all time.

But any periodic survivor must now satisfy simultaneously

\[
\boxed{
\inf_s
\|V_s(s)\|_{L^2(B_{R_{PV}})}
\ge\sigma_\alpha>0
}
\]

and the long-period/nonsummable-tail restrictions from M5-194O.

### Aperiodic compact alpha-limit

Also forced to maintain the same positive core-speed floor for its entire complete orbit.

This removes heteroclinic or near-stationary alpha-limit trajectories that pass arbitrarily close to a stationary state in the Pineau--Vicol core-speed topology.

---

## 11. DSD warning about order of limits

The transfer uses the diagonal first-hitting construction in which physical checkpoint times still tend to the original candidate singular time.

It would be invalid to take one already-extracted ancient solution in complete isolation, forget its provenance, and then assert that every arbitrarily old time in that ancient solution automatically lies in the original late-time Pineau--Vicol regime.

The provenance channel is essential.

Thus the correct statement is about **checkpoint alpha-limits inherited through the first-hitting diagonal construction**, not every possible blow-down of an arbitrary ancient solution.

---

## 12. DSD verdict

### CORRECTED

- singularity-centered and checkpoint-centered Leray clocks are distinct;
- the earlier speed-floor result cannot be imported by notation alone.

### PROVED ON THE DIAGONAL TYPE-I DERIVATIVE CORRIDOR

- the clocks differ by `O(kappa/a)`;
- the normalized coordinates and profiles align;
- the scaling generators differ by a vanishing `O(kappa/a)` error;
- the positive singularity-centered local speed floor therefore passes to strongly compact checkpoint alpha-limits.

### REMAINS OPEN

- exclusion of complete compact Leray orbits with a uniform positive local speed floor;
- long-period DSS with critical tail;
- aperiodic recurrent dynamics;
- tail/derivative compactness failures;
- global regularity.

---

## 13. Next audit target

The final dynamic core problem can now be stated without the frozen tail:

\[
\boxed{
V_\alpha\text{ complete bounded/local-Morrey Leray orbit},
\qquad
\inf_{s\in\mathbb R}
\|\partial_sV_\alpha(s)\|_{L^2(B_R)}
\ge\sigma_0>0.
}
\]

The next audit should combine this with the repository's projective/eigenframe action ledger.

A complete orbit which moves forever at positive local speed must either

1. accumulate unbounded projective/shape action;
2. repeatedly replace/export material structure;
3. generate recurrent derivative/palinstrophy cost;
4. or organize into a relative equilibrium/periodic orbit.

The first three are already typed H/T costs; the fourth is the RSS/RDSS branch partially constrained by 2026 Liouville results.

The task is now to make that four-way implication quantitative for the alpha-limit core itself.
