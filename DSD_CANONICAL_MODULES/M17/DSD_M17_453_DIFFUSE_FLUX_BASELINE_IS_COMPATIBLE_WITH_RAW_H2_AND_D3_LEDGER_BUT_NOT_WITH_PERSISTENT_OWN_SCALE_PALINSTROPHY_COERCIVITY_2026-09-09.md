# DSD M17-453 — The diffuse-flux baseline is compatible with raw-H2 and D3 ledgers but not with persistent own-scale palinstrophy coercivity

Date: 2026-09-09  
Canonical ID: **M17-453**

Status: **ACTIVE RESOURCE-COMPARISON AUDIT / PALINSTROPHY PRIORITY REDUCTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Baseline from M17-450--452

The minimal enstrophy-compatible parent-length positive-flux carrier has the scaling

\[
\boxed{
\ell_R\sim R,
\qquad
\mathfrak A_R\sim R,
\qquad
\rho_R\sim R^{-1},
\qquad
\Phi_R\sim1.
}
\]

The corresponding normalized tube volume is

\[
V_R\sim R^2.
\]

This is a scaling audit, not the assertion that an exact Navier--Stokes solution with perfectly uniform geometry exists.

## 2. Snapshot enstrophy

The scaling gives

\[
E_R^{tube}
\sim
V_R\rho_R^2
\sim
R^2R^{-2}
\sim1.
\]

This agrees with the M17-450 uniform record-enstrophy bound.

## 3. Raw-H2 currency

On an own-scale exact CE-H coefficient region with

\[
|\kappa_R|\sim1,
\]

one has

\[
|\Delta\Omega_R|^2
=\kappa_R^2\rho_R^2.
\]

Hence snapshot raw-`H2` is also

\[
H_R^{snap}\sim1.
\]

If the diffuse carrier persists through `O(R^2)` own-time units inside a parent-time record window, then

\[
H_R^{space\text{-}time}\sim R^2.
\]

M17-405 applies the ancestry factor `R^-3`, so the record contribution is

\[
\boxed{
R^{-3}H_R^{space\text{-}time}
\sim R^{-1}.
}
\]

This is summable on geometric records.

Therefore the minimal diffuse baseline is fully compatible with the finite raw-`H2` ancestral ledger.

## 4. Coefficient-gradient / D3 currency

If normalized coefficient gradients remain order one,

\[
|\nabla\kappa_R|\sim1,
\]

then

\[
G_{\kappa,R}^{snap}
:=
\int\rho_R^2|\nabla\kappa_R|^2dx
\sim1.
\]

Over `O(R^2)` own-time units,

\[
G_{\kappa,R}^{space\text{-}time}\sim R^2.
\]

M17-445 weighs this by `R^-5`, yielding

\[
\boxed{
R^{-5}G_{\kappa,R}^{space\text{-}time}
\sim R^{-3}.
}
\]

This is even more strongly summable.

Thus the new M17-444--445 higher resource does not close the minimal diffuse carrier by scaling alone.

## 5. Palinstrophy is radically different

Suppose, however, that on a fixed positive fraction of the active diffuse spacetime one has an own-scale coercive estimate

\[
\boxed{
P_{cell}
:=
\int_{cell}|\nabla\Omega_R|^2dx
\ge
c_P
\int_{cell}|\Omega_R|^2dx.
}
\]

If such coercivity captures a fixed positive fraction of the order-one tube enstrophy, then snapshot palinstrophy is

\[
P_R^{snap}\gtrsim c>0.
\]

Persistence for `O(R^2)` own-time units gives

\[
P_R^{space\text{-}time}\gtrsim cR^2.
\]

M17-307 uses ancestry weight `R^-1`, hence

\[
\boxed{
R^{-1}P_R^{space\text{-}time}
\gtrsim cR.
}
\]

This cannot be summed over growing geometric records.

Therefore persistent own-scale palinstrophy coercivity is incompatible with the diffuse baseline.

## 6. Exact surviving requirement

The diffuse branch can survive only if the effective spacetime fraction/mass fraction on which own-scale coercivity holds collapses fast enough.

If `gamma_R` denotes the fraction of active enstrophy-time captured by coercive own-scale cells, then schematically

\[
\mathcal P_{anc,R}
\gtrsim
\gamma_R R.
\]

Finite ancestral palinstrophy therefore requires

\[
\boxed{
\sum_m\gamma_{R_m}R_m<\infty.
}
\]

For a persistent parent-time diffuse carrier, `gamma_R` must be far smaller than order one; on geometric records it must decay beyond the record-linear threshold up to summable corrections.

## 7. Relation to M17-428 and M17-383

M17-428 already showed that

\[
\kappa\sim-r^{-2}
\]

by itself does not imply local palinstrophy coercivity because boundary/doubling terms can be of the same order.

M17-383 separately showed that coefficient-scale thickness does not imply solution-mass retention and introduced the local doubling/frequency firewall.

M17-453 shows why those two firewalls are now the decisive ones for the diffuse branch:

- raw-`H2` is too heavily discounted (`R^-3`);
- coefficient-gradient/D3 is even more heavily discounted (`R^-5`);
- palinstrophy has the favorable `R^-1` ancestry weight and would close the branch immediately if local coercivity held on a nonsummable fraction of the diffuse carrier.

## 8. Updated target

The next high-value question is therefore not another higher-derivative budget.

It is:

\[
\boxed{
\text{Does mesoscopic transverse broadening }\mathfrak A\sim R
\text{ restore enough interior mass/boundary separation to force}
\]
\[
\boxed{
\text{own-scale palinstrophy coercivity on a nonsummable fraction of cells?}
}
\]

If yes, the `R^-1` ancestral ledger becomes decisive.

If no, the remaining escape must be typed as one of:

1. local doubling/frequency decompactification on almost all active cells;
2. boundary-layer mass concentration;
3. coefficient-sign/zero-corridor complexity;
4. chart/interface/genealogy loss.

## 9. Audit verdict

**PASS — the resource priority is now sharply ordered.**

The minimal diffuse-flux scaling evades the `R^-3` and `R^-5` ledgers but cannot tolerate persistent own-scale palinstrophy coercivity. The late CE-H frontier therefore returns to the M17-383/428 local coercivity firewall, now inside a mesoscopically broadened positive-flux carrier.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
