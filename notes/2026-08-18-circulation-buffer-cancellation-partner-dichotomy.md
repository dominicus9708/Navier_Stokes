# Circulation buffer versus same-scale signed partner dichotomy

Date: 2026-08-18

Status: **DERIVED LOCAL FLUX DICHOTOMY COMPLEMENTING THE MATERIAL-LINEAGE FREQUENCY CEILING. IF THE CLEAN CIRCULATION ANNULUS NEEDED FOR THE TUBE ENERGY LOWER BOUND FAILS, THE CANCELLATION ITSELF FORCES A NATURAL-SCALE OPPOSITE-SIGNED VORTICITY PARTNER WITH THE USUAL ENSTROPHY PRICE. GLOBAL REGULARITY NOT PROVED.**

## 1. Core flux

Consider a signed-coherent natural tube cross-section of radius

\[
r\asymp K^{-1}
\]

with vorticity flux / circulation

\[
\Gamma(r)\ge\gamma_0>0.
\]

For a concentric loop of radius `rho`, let `Gamma(rho)` denote the circulation around the loop, equivalently the total vorticity flux through the enclosed cross-section by Stokes.

## 2. Clean buffer case

If

\[
|\Gamma(\rho)|\ge\gamma_0/2
\qquad
\text{for all }r\le\rho\le2r,
\]

then Cauchy--Schwarz on the loops and radial integration gives a kinetic-energy lower bound proportional to the tube length.  This is the clean-buffer hypothesis used in the material-circulation lineage ceiling

\[
K_1\lesssim CK_0^{3/2}.
\]

## 3. Cancellation case

Suppose instead there exists `rho_* in [r,2r]` such that

\[
|\Gamma(\rho_*)|<\gamma_0/2.
\]

Then the annular vorticity flux between the core loop and `rho_*` has magnitude at least `gamma0/2` and must oppose the core signed flux.

Let `A` be that two-dimensional annulus.  Its area satisfies `|A| <= C r^2`.  Hence

\[
\left|\int_A\omega\cdot n\,dA\right|^2
\le
|A|\int_A|\omega|^2dA.
\]

Therefore

\[
\boxed{
\int_A|\omega|^2dA
\gtrsim
\frac{\gamma_0^2}{r^2}.
}
\]

Over a natural longitudinal segment of length comparable to `r`, this gives the three-dimensional enstrophy price

\[
\boxed{
E_{\omega,\rm partner}
\gtrsim
\frac{\gamma_0^2}{r}
\asymp
\gamma_0^2K.
}
\]

This is precisely the natural dangerous-packet enstrophy scale.

## 4. Structural interpretation

The failure of the circulation buffer is therefore not a loophole in the tube-energy argument.  It creates a same-scale neighboring vorticity structure carrying enough opposite signed flux to cancel a fixed fraction of the core circulation.

Depending on its geometry, this returns to

- signed-line / polarity defect;
- projective partner-angle defect;
- non-affine same-scale strain;
- reach-collapse / close-pair concentration.

Thus the material-lineage branch is

\[
\boxed{
\text{clean circulation buffer}
\Rightarrow K_1\lesssim CK_0^{3/2}
}
\]

or

\[
\boxed{
\text{buffer cancellation}
\Rightarrow
\text{same-scale signed/projective partner packet}.
}
\]

## 5. Limitation

The partner packet may itself participate in the source-active heterochiral network and is not forbidden.  The result closes only the possibility that circulation-annulus failure makes the lineage energy lower bound disappear without creating another priced structure.

Status: **CLEAN BUFFER OR NATURAL-SCALE OPPOSITE-SIGNED PARTNER / MATERIAL-LINEAGE COMPLEMENT CLOSED INTO THE SAME-SCALE NETWORK / GLOBAL REGULARITY NOT PROVED.**