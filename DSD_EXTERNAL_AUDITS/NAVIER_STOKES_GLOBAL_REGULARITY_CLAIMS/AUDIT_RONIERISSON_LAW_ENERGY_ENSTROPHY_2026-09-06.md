# DSD Audit — “Ronierisson's Law” Energy/Enstrophy Regularity Claim

Date: 2026-09-06
Source: *Global Regularity of Three-Dimensional Navier-Stokes Equations via Energy and Enstrophy Estimates*, DOI 10.5281/zenodo.15226722, Apr 2025.
Audit status: **CONCLUSION REINTRODUCED AS A LAW / DIRECT CIRCULARITY IF USED AS PROOF INPUT**

## 1. Public statement

The abstract introduces “Ronierisson's Law,” described as the observation:

> all fluids with smooth initial conditions remain smooth forever, controlled by viscosity and pressure.

The paper then says this law provides the mathematical tool leading to refined energy/entropy estimates and global regularity.

## 2. DSD proposition identity audit

Let

\[
P:=\text{“every smooth divergence-free finite-energy datum generates a global smooth NSE solution.”}
\]

The Clay regularity problem asks whether `P` is true.

If the new law is itself the assertion

\[
\boxed{P},
\]

then using the law to prove `P` has logical form

\[
P\Rightarrow P.
\]

This is valid as a tautological implication but supplies no proof of the premise.

Renaming a conjectured property as a “law” does not change its proof status.

## 3. How a noncircular version could exist

The law would become useful if replaced by an independently proved quantitative statement, e.g.

\[
\frac d{dt}X(t)+D(t)\le F(E_0,\nu)X(t)
\]

with an integrable/data-controlled coefficient strong enough to prevent blow-up.

Then the proof obligation would be the derivation of that inequality from the NSE, not the verbal assertion of perpetual smoothness.

## 4. Pressure/viscosity statement

Viscosity dissipates kinetic energy, but the standard 3D difficulty is that vortex stretching can amplify enstrophy/higher norms. Pressure enforces incompressibility and is nonlocal; it is not known to provide a universal sign-definite damping of all higher norms.

Thus saying “viscosity and pressure control smoothness” is the desired mechanism to prove, not an established universal estimate.

## 5. DSD verdict

If the public law is used as an assumption/input with the quoted meaning, the proof is circular:

\[
\boxed{
\text{global smoothness is assumed under a new name and then concluded.}
}
\]

Any independent energy/entropy estimates in the manuscript should be assessed separately, but they must close the regularity theorem without invoking the law in its conclusion-equivalent form.

Global regularity remains unproved.
