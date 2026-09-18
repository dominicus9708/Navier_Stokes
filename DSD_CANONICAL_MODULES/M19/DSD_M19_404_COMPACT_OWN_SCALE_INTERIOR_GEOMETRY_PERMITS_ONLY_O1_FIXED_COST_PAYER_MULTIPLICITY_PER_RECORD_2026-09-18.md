# M19-404 — Compact own-scale interior geometry permits only O(1) fixed-cost payer multiplicity per record

Date: 2026-09-18

Status: **NEW GMS COMPACTNESS FIREWALL / M19-403 RULES OUT PURE RADIAL SCALE MULTIPLICITY. ON THE CANONICAL M19-318--321 INTERIOR-CARRIER BRANCH, THE CERTIFIED PAYER LIVES IN A FIXED NORMALIZED SPATIAL CORE AND FIXED NORMALIZED TIME WINDOW, WITH OWN-SCALE FREQUENCY AND UNIFORM COMPACT GEOMETRY. ANY FAMILY OF PAIRWISE DISJOINT PAYERS THAT EACH RETAIN A FIXED NORMALIZED SPACE-TIME SIZE HAS ONLY O(1) MEMBERS PER RECORD. THEREFORE THE LINEAR MULTIPLICITY \`N_R\gtrsim R\` REQUIRED BY M19-317 CANNOT COME FROM ORDINARY SAME-SCALE PACKING INSIDE THE COMPACT INTERIOR CORE. TO OBTAIN LINEAR MULTIPLICITY ONE MUST SHRINK THE PAYER SUPPORT, SPREAD INTO PARENT-LENGTH/REMOTE GEOMETRY, LOSE BOUNDED OVERLAP, OR GENERATE DERIVATIVE/TOPOLOGICAL DECOMPACTIFICATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Canonical compact interior record

M19-318--321 give, on every sufficiently late retained record:

1. a fixed normalized time interval

\[
I_0\Subset(-\infty,0);
\]

2. a fixed normalized ball

\[
B_L;
\]

3. fixed local enstrophy

\[
\int_{I_0}\int_{B_L}|\Omega_m|^2\,dy\,ds
\ge c_{\rm loc}>0;
\]

4. total record palinstrophy

\[
q_{1,m}
=
\int_I\|\nabla\Omega_m\|_2^2\,ds
\asymp1;
\]

5. a fixed own-scale Fourier annulus and a fixed spectral variance gap.

Thus the selected interior carrier is an own-scale compact object in normalized variables.

---

## 2. Fixed-size payer cells

Suppose a payer-localization theorem associates to each independent same-scale event a normalized parabolic cell

\[
Q_\alpha
=
B_{r_*}(y_\alpha)
\times
(s_\alpha-\tau_*,s_\alpha)
\]

with fixed

\[
r_*>0,
\qquad
\tau_*>0,
\]

contained in a fixed enlargement

\[
B_{L_*}\times I_*,
\]

where \(L_*,I_*\) are record-independent.

Assume pairwise disjointness, or more generally bounded overlap by a constant \(N_*\).

Then elementary volume/time packing gives

\[
\boxed{
N_{\rm cell}
\le C(L_*,|I_*|,r_*,\tau_*,N_*)
<\infty.
}
\]

The bound is independent of the record factor \(R_m\).

Therefore

\[
\boxed{
N_m=O(1)
}
\]

for any fixed-size compact-core payer family.

---

## 3. Temporal multiplicity is also O(1)

Even without spatial separation, suppose each independent event requires a fixed own-scale time thickness

\[
\tau_*>0
\]

inside the fixed record interval \(I_*\).

Then the number of pairwise time-disjoint episodes is at most

\[
\boxed{
N_{\rm time}
\le
\frac{|I_*|}{\tau_*}+1
=
O(1).
}
\]

Thus positive event rate in normalized time does not give

\[
N_m\sim R_m
\]

inside one fixed second-generation record window.

---

## 4. Angular/topological packing with fixed separation is O(1)

If independent payer packets are distinguished by a fixed angular or directional separation

\[
\angle(\xi_\alpha,\xi_\beta)\ge\vartheta_*>0
\]

inside a compact direction sphere, only finitely many such uniformly separated directions can coexist.

Likewise fixed-radius disjoint tubes/sheets in a fixed normalized core admit only finite bounded-overlap multiplicity under the retained compact geometry.

Hence ordinary finite-resolution angular/topological separation also gives

\[
\boxed{
N_{\rm ang/top}=O(1).
}
\]

---

## 5. Comparison with the linear threshold

M19-317 requires essentially

\[
N_m\gtrsim R_m
\]

or an equivalent supercritical gain.

But the compact-core estimates above give only

\[
N_m=O(1).
\]

Therefore

\[
\boxed{
\text{compact own-scale same-record multiplicity}
\not\Rightarrow
\text{GMS palinstrophy closure}.
}
\]

Combined with M19-403,

\[
\boxed{
\text{radial scale multiplicity}=O(\log R),
\qquad
\text{compact same-scale multiplicity}=O(1),
}
\]

both far below \(R\).

---

## 6. How linear multiplicity could still appear

To produce \(N_m\gtrsim R_m\), at least one compact payer premise must fail.

### A. Shrinking payer support

The normalized payer radius or time thickness tends to zero:

\[
r_{*,m}\to0
\quad\text{or}\quad
\tau_{*,m}\to0.
\]

Maintaining fixed palinstrophy charge on shrinking cells implies derivative concentration/high-frequency escalation.

### B. Parent-length spreading

The relevant carrier occupies a normalized longitudinal extent of order

\[
R_m
\]

rather than a fixed compact core.

This reconnects to the M17 parent-length diffuse / remote genealogy branches.

### C. Unbounded overlap or sheet proliferation

The number of distinguishable local structures grows while normalized geometry loses uniform tubular reach, Poincaré control, or finite-memory separation.

This is a geometry/topology decompactification exit.

### D. Remote spatial population

The payers leave every fixed normalized ball and populate increasingly remote regions.

This is the remote/critical-tail root complex.

---

## 7. Interaction with the q1 upper bound

M19-319 gives

\[
q_{1,m}\le C_1.
\]

Therefore, if each genuinely derivative-disjoint event pays

\[
p_{m,k}\ge c_*>0,
\]

then automatically

\[
N_m
\le
\frac{C_1}{c_*}.
\]

This is an even more direct compact-record multiplicity ceiling.

Consequently any claim of

\[
N_m\gtrsim R_m
\]

must simultaneously imply failure of at least one of:

1. fixed per-event palinstrophy lower bound;
2. derivative-measure disjointness/bounded reuse;
3. the canonical q1 record upper bound;
4. representation of all events inside the same retained record carrier.

Thus linear multiplicity is itself a **contradictory rigidity target**, not an expected generic feature.

---

## 8. Revised GMS compact-branch target

After M19-403--404, the compact canonical interior branch no longer has a plausible ordinary multiplicity path.

The remaining GMS options are

\[
\boxed{
\mathcal T_{GMS}^{subcritical}:
\text{gain better-than-}\rho^{-1}\text{ physical palinstrophy transfer},
}
\]

or force a typed exit:

\[
\boxed{
G_{\rm shrinking/high\text{-}frequency}
\lor
G_{\rm parent\text{-}length/remote}
\lor
G_{\rm geometry/topology}
\lor
G_{\rm representation}.
}
\]

Equivalently, a successful GMS proof on the compact core must produce a **non-scale-covariant gain**, not merely more copies of the same critical packet.

---

## 9. Strategic consequence

The highest-value GMS calculation is now to search for an extra physical factor from:

- local energy/pressure structure,
- a Morrey/Campanato improvement,
- Galilean mean subtraction plus pressure localization,
- a genuine subcritical ancient palinstrophy decay,
- or another PDE rigidity that improves the critical

\[
Q^{phys}\sim\rho^{-1}
\]

scaling.

Further radial or compact-core packet counting is not a promising independent route.

---

\[
\boxed{\text{M19-404 COMPLETE; COMPACT OWN-SCALE PAYER MULTIPLICITY IS O(1), SO GMS NEEDS SUBCRITICAL GAIN OR DECOMPACTIFICATION.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
