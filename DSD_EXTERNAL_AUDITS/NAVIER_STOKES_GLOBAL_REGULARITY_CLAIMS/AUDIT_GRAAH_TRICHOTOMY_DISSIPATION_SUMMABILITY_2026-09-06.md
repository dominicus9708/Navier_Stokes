# DSD Deep Audit — Graah Thick/Tube/Fragmented Trichotomy: Dissipation Summability Gate

Date: 2026-09-06
Target: Hannes Graah, *Global Regularity for 3D Navier-Stokes*, Zenodo 18132364 / 18132365 (2026).
Status: **OPEN_DEEP / PHYSICAL-DISSIPATION SUMMABILITY GATE**

## 1. Public proof architecture

The public abstract states a contradiction scheme:

1. assume a first singular time `T`;
2. at every approaching parabolic scale classify vorticity as thick, tube-like, or fragmented;
3. in each regime obtain a scale-invariant lower bound on dissipation on a comparable time interval;
4. use a Calderon-Zygmund packing argument to extract infinitely many disjoint dissipation intervals accumulating at `T`;
5. contradict the finite global energy dissipation budget.

The trichotomy itself may contain useful geometric information. The present audit isolates the dimensional/summability bridge in step 4 -> 5.

## 2. Exact NSE scaling of the physical dissipation

Under the standard Navier-Stokes scaling

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\]

one has

\[
\nabla u_\lambda=\lambda^2\nabla u.
\]

For a parabolic cylinder `Q_r=B_r x I_r` with `|I_r|~r^2`, define the actual energy-budget dissipation

\[
D(Q_r):=\int_{I_r}\int_{B_r}|\nabla u|^2\,dx\,dt.
\]

Its scaling dimension is one spatial length:

\[
D(Q_r)\sim r.
\]

Hence the familiar scale-invariant local quantity is

\[
\mathcal D(r):=r^{-1}D(Q_r).
\]

Therefore a scale-invariant lower bound

\[
\mathcal D(r)\ge c_*>0
\]

exports only

\[
\boxed{D(Q_r)\ge c_*r}
\]

into the globally finite physical dissipation budget.

## 3. Infinite count is not enough

Suppose the packing provides infinitely many pairwise disjoint intervals/cylinders with radii `r_j -> 0` and

\[
D_j\ge c_*r_j.
\]

The energy inequality gives a contradiction only if

\[
\sum_j D_j=\infty.
\]

The displayed lower bound implies this only if

\[
\boxed{\sum_j r_j=\infty.}
\]

But an infinite sequence of scales may be summable. For example

\[
r_j=2^{-j}
\]

gives

\[
\sum_jr_j<\infty.
\]

Moreover, disjoint time intervals of parabolic length `~r_j^2` contained in a finite time interval imply only

\[
\sum_jr_j^2<\infty,
\]

which does not force divergence of `sum r_j` and certainly does not provide a scale-independent physical dissipation quantum.

Thus

\[
\boxed{
\text{infinitely many scale-invariant local payments}
\not\Rightarrow
\text{infinite global physical dissipation}.
}
\]

## 4. What would close the argument

Any one of the following would be sufficient in principle:

1. **Actual fixed physical quantum:** prove `D_j >= d_*>0` independent of scale;
2. **Nonsummable radii:** prove the packing/genealogy forces `sum_j r_j=infinity`;
3. **Multiplicity compensation:** at scale `r`, prove enough disjoint carriers that total physical payment is nonsummable;
4. **Different global budget:** identify another globally finite quantity whose local normalized lower bound has zero scaling dimension when converted back to the physical variables.

Without such a bridge, a scale-invariant lower bound by itself is not enough.

## 5. Relation to internal M17 audit

This is exactly the external analogue of the M17 amplitude/scale firewall:

- M17-230: summable scale-ladder physical costs do not close a contradiction;
- M17-235/237: normalized multiplier costs can retain an amplitude/scale factor;
- M17-242: amplitude-independent geometry does not create amplitude-independent physical energy.

New regression test:

\[
\boxed{
R21:\ \text{counting infinitely many normalized payments is invalid unless their physical weights are proved nonsummable.}
}
\]

## 6. Current verdict

From the currently accessible abstract, it is not possible to determine whether Graah's detailed Calderon-Zygmund packing includes the necessary `sum r_j=infinity` theorem or instead produces an unnormalized fixed quantum.

Therefore the fair status is

\[
\boxed{
\text{OPEN_DEEP — verify the physical-cost summability theorem before accepting the final contradiction.}
}
\]

If the full proof uses only “infinitely many disjoint intervals” plus `r^{-1}D(Q_r)>=c`, the final contradiction has a root summability gap. If an explicit nonsummability/multiplicity theorem is present, that theorem is the decisive survivor to audit and potentially cite.

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
