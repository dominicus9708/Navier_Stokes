# Proof / verification map

This file separates established identities, DSD bridge definitions, computational checks, external regularity anchors, and unresolved proof targets.

| Item | Current support | Status |
|---|---|---|
| 3D incompressible Navier–Stokes baseline on `R^3` | repository baseline note | NAVIER–STOKES INPUT |
| Gaussian double-curl benchmark is divergence-free | exact SymPy identity | COMPUTATIONAL CHECK / exact symbolic |
| Vorticity formula for benchmark | exact SymPy identity | COMPUTATIONAL CHECK / exact symbolic |
| Pressure Poisson source `-Delta p = Q` | exact SymPy identity | COMPUTATIONAL CHECK / exact symbolic |
| Radial channel at `r=0` is inapplicable, not zero | coordinate definition + typed DSD interpretation | BRIDGE DEFINITION |
| Radial channel away from origin can be defined zero | direct benchmark evaluation | COMPUTATIONAL CHECK |
| `x/y/z` seeds are rotation-equivalent | radial seed construction / coordinate permutation | DERIVED BENCHMARK FACT |
| Fixed-time shell terms `T_E,T_W,T_P,T_Ei` | analytic definitions | BRIDGE DEFINITION |
| Total shell energy isotropic at `r=sqrt(2)` for benchmark | exact angular polynomial identity | COMPUTATIONAL CHECK / exact symbolic |
| Axis-resolved energies remain unequal at `r=sqrt(2)` | closed-form shell averages | COMPUTATIONAL CHECK |
| Enstrophy shell vanishes at `r=sqrt(5/2)` while energy is nonzero | closed-form formulas | COMPUTATIONAL CHECK |
| Quadratic descriptor collision for `u` and `-u` | exact construction | COMPUTATIONAL CHECK |
| `r^2 T_E` scaling covariance | exact Navier–Stokes scaling identity | COMPUTATIONAL CHECK |
| `r^4 T_W` scaling covariance | exact Navier–Stokes scaling identity | COMPUTATIONAL CHECK |
| `r^4 T_P` scaling covariance | whole-space `l=2` pressure inversion + numerical cross-check | COMPUTATIONAL CHECK |
| Centered candidate `D_O` | finite sampling only | CONJECTURE / TARGET |
| All-center descriptor `D_all` | definition only | CONJECTURE / TARGET |
| Velocity-gradient block has `tr S=0` | exact SymPy identity | COMPUTATIONAL CHECK / exact symbolic |
| Benchmark vortex-stretching formula `omega^T S omega` | exact SymPy identity | COMPUTATIONAL CHECK / exact symbolic |
| Signed shell stretching cancels but positive part is nonzero | exact shell integration | COMPUTATIONAL CHECK |
| Global benchmark stretching cancels with `Sigma_+=Sigma_-=992*pi/81` | exact whole-space integration | COMPUTATIONAL CHECK |
| `div R_adv=-Q`, `div R_pres=+Q`, `div R_visc=0` | smooth incompressible identity + exact benchmark check | DERIVED IDENTITY / CHECK |
| Translated benchmark recovers the same special shell about its own center | equal-solid-angle quadrature + exact scaling | COMPUTATIONAL CHECK |
| Same-radius shell about an unrelated fixed origin becomes anisotropic | deterministic quadrature witness | COMPUTATIONAL CHECK |
| Linear superposition of benchmark seeds remains divergence-free | exact symbolic identity | COMPUTATIONAL CHECK / exact symbolic |
| Nonlinear pressure/advection source has nonzero `Q_cross` under superposition | exact symbolic expression + test-point evaluation | COMPUTATIONAL CHECK / exact symbolic |
| DSD off-diagonal dynamic channels are required for nonlinear interactions | bridge interpretation of `Q_cross` | BRIDGE DEFINITION |
| `L^infty_t L^3_x` control implies smoothness in the external endpoint theorem | Escauriaza–Seregin–Šverák (2003) | EXTERNAL REGULARITY ANCHOR |
| DSD critical channel `T_3(t)=int |u|^3` is Navier–Stokes scale invariant | direct scaling calculation | BRIDGE DEFINITION / EXACT SCALING |
| Formal `L^3` balance separates advection cancellation, viscous dissipation, pressure correlation | smooth decaying solution calculation | DERIVED IDENTITY |
| A-priori bound for `sup_t ||u||_3` from DSD channels | none | OPEN PROOF OBLIGATION |
| Non-circular control of pressure correlation `Pi_3` | none | OPEN PROOF OBLIGATION |
| Non-circular control of positive vortex stretching `Sigma_+` | none | OPEN PROOF OBLIGATION |
| Translation-complete extension to arbitrary centers/data | finite covariance witness only | OPEN PROOF OBLIGATION |
| General control of all off-diagonal nonlinear cross couplings | one two-seed witness only | OPEN PROOF OBLIGATION |
| Global a-priori bound for arbitrary admissible initial data | none | OPEN PROOF OBLIGATION |
| DSD route proves global smoothness | none | NOT CLAIMED |

## Failure rule

A candidate route must be downgraded to **FAILED ROUTE** if it is shown to be incompatible with the original incompressible PDE, loses information needed by any proposed regularity implication, or cannot be made translation/rotation complete.
