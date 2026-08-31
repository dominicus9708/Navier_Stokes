# DSD M5-399 — Unbounded adjacent center turnover is a formed remote satellite

Date: 2026-08-31

Status: **THE OLD `T_center` BRANCH IS NOT INDEPENDENT / IF THE DIMENSIONLESS ADJACENT FIRST-HITTING CENTER DISPLACEMENT IS UNBOUNDED, THE NEXT FIRST-HITTING MAXIMUM ITSELF IS A FORMED REMOTE ACTIVE SATELLITE IN THE PREVIOUS-STAGE NORMALIZATION / IF THE DISPLACEMENT IS UNIFORMLY BOUNDED, THE EXISTING GEOMETRIC-SERIES ARGUMENT GIVES ONE NESTED PHYSICAL SINGULAR CENTER / THUS CENTER TURNOVER IS EXHAUSTED BY NESTING OR THE EXISTING REMOTE-SATELLITE FRONTIER / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

The earlier center-nesting lemma defined

\[
\mathfrak T_j:=\frac{|X_{j+1}-X_j|}{r_j},
\qquad
r_j=\sqrt{\frac{\nu}{W_j}},
\qquad
W_{j+1}=qW_j,
\quad q>1.
\]

It treated

\[
\mathfrak T_j\gg1
\]

as a dynamic center-turnover event.

After M5-280--281 and M5-392--398, the remote-active-satellite language is sufficiently precise to revisit this label.

The question is whether unbounded adjacent center motion is genuinely different from a remote active satellite.

It is not.

---

## 2. Normalize the next first-hitting maximum in the previous stage

At stage `j`, introduce the parent normalized coordinate

\[
Y=\frac{x-X_j}{r_j}.
\]

At the next first-hitting time `t_{j+1}`, choose a maximum point `X_{j+1}` satisfying

\[
|\omega(X_{j+1},t_{j+1})|=W_{j+1}=qW_j.
\]

In the stage-`j` normalization the next center is located at

\[
Y_{j+1}
=
\frac{X_{j+1}-X_j}{r_j},
\]

so

\[
\boxed{|Y_{j+1}|=\mathfrak T_j.}
\]

The normalized vorticity there is

\[
\Omega_j(Y_{j+1},t_{j+1})
=
\frac{\omega(X_{j+1},t_{j+1})}{W_j},
\]

hence

\[
\boxed{|\Omega_j(Y_{j+1},t_{j+1})|=q.}
\]

Thus the displaced next center is not a weak passive tail point. It is a fully formed record-amplitude active object.

---

## 3. Its own natural scale is fixed relative to the parent scale

The next first-hitting natural radius is

\[
r_{j+1}
=
\sqrt{\frac{\nu}{W_{j+1}}}
=
q^{-1/2}r_j.
\]

Therefore in stage-`j` normalized units the next core's natural radius is

\[
\boxed{\ell_{j+1}^{(j)}=q^{-1/2}.}
\]

Consequently

\[
\frac{|Y_{j+1}|}{\ell_{j+1}^{(j)}}
=q^{1/2}\mathfrak T_j.
\]

If

\[
\mathfrak T_j\to\infty
\]

along a subsequence, then

\[
\boxed{
\frac{|Y_{j+1}|}{\ell_{j+1}^{(j)}}\to\infty.
}
\]

This is exactly the spatial/natural-scale separation defining the remote active-satellite corridor.

---

## 4. Direct comparison with the M5-280 satellite parameter

M5-280 uses

\[
\Lambda_R
:=
R^2\sup_{A_R}|\Omega|.
\]

Choose a fixed-shape annulus centered at `X_j` whose radius is comparable to

\[
R_j:=|Y_{j+1}|=\mathfrak T_j
\]

and which contains the point `Y_{j+1}`.

Since

\[
|\Omega_j(Y_{j+1},t_{j+1})|=q,
\]

we obtain

\[
\boxed{
\Lambda_{R_j}
\ge
c qR_j^2
=
cq\mathfrak T_j^2.
}
\]

Therefore

\[
\boxed{
\mathfrak T_j\to\infty
\Longrightarrow
\Lambda_{R_j}\to\infty.
}
\]

This is stronger than merely detecting a remote critical tail: the next record core itself realizes the active-satellite parameter.

---

## 5. Point-picking is immediately available

Because the next center is a true first-hitting active point and

\[
\frac{|Y_{j+1}|}{\ell_{j+1}^{(j)}}\to\infty,
\]

M5-281's backward parabolic point-picking applies directly after choosing the appropriate physical/ancient representation.

Thus the unbounded-center subsequence routes to

\[
\boxed{
T_{center}^{unbounded}
\Longrightarrow
T_{dynamic/localization}
\lor
H_{ambient}
\lor
A_{detached},
}
\]

with the same scope and firewalls as the existing remote-satellite theorem.

No separate center-turnover compactness object is required.

---

## 6. Bounded center motion gives the opposite complete alternative

If instead

\[
\sup_j\mathfrak T_j\le C_T<\infty,
\]

then the existing geometric-series nesting theorem gives for every `m>=1`

\[
|X_{j+m}-X_j|
\le
C_T\sum_{k=0}^{m-1}r_{j+k}
\le
\frac{C_T}{1-q^{-1/2}}r_j.
\]

Hence there is a physical point `X_*` such that

\[
\boxed{
|X_*-X_j|\lesssim r_j.
}
\]

Therefore the center geometry has an exact exhaustive split:

\[
\boxed{
\text{adjacent center genealogy}
\Longrightarrow
\text{nested single center}
\lor
S_{remote}^{formed}.
}
\]

---

## 7. Relation to M5-398

M5-398 shows that a local formed recurrent configuration which retains center nesting, spatial tightness, and the compact ancient package cannot remain an independent quiet terminal: it enters the `W1/W2` ancient dichotomy.

M5-399 now supplies the complementary center statement:

- bounded adjacent center displacement supports the nested compact route;
- unbounded adjacent displacement is itself a remote active satellite.

Thus center motion does not produce a third option between local compact recurrence and remote activity.

---

## 8. DSD audit

### Derived

- the next first-hitting center is a formed high-vorticity object in the previous normalization;
- unbounded dimensionless center displacement gives unbounded distance-to-natural-scale ratio;
- the same event forces the M5-280 satellite parameter `Lambda_R` to diverge.

### Firewall

- do not infer a contradiction from unbounded center displacement alone;
- it is a routing into the already-existing remote-satellite/ambient-strain/detached-ancient frontier;
- bounded adjacent displacement, not pointwise equality of centers, is sufficient for nesting because the natural radii form a geometric series.

---

## 9. Updated dynamic frontier

The label

\[
T_{center}
\]

can be removed as an independent long-time terminal.

After M5-397--399, formed replacement and center turnover route into already typed flux/remote/compactness channels.

The remaining high-level frontier is sharpened toward

\[
\boxed{
H_{crit\,mass/frequency/direction}
\lor
H_{ambient/nonlocal\,strain}
\lor
T_{projective/export/remote/compactness/realization}.
}
\]

The next target is the ambient/nonlocal-strain side: separate an actual rotational source at some scale from a genuinely source-free harmonic/affine shield, and preserve the energy-bearing versus energy-vanishing distinction.

---

## 10. Audit verdict

### REMOVED AS INDEPENDENT T

\[
\boxed{T_{center}^{unbounded}.}
\]

### REPLACEMENT

\[
\boxed{
T_{center}^{unbounded}
\Longrightarrow
S_{remote}^{formed}
\Longrightarrow
T_{dynamic}
\lor H_{ambient}
\lor A_{detached}.
}
\]

### STILL OPEN

- ambient/nonlocal harmonic strain;
- detached ancient restart/critical inheritance;
- projective/export/realization escape;
- critical mass/frequency/direction H;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
