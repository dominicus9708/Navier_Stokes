# Proof / verification map

This file separates established identities, DSD bridge definitions, computational checks, and unresolved proof targets.

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
| Bounded DSD descriptor implies a known regularity-sufficient norm | none | OPEN PROOF OBLIGATION |
| Global a-priori bound for arbitrary admissible initial data | none | OPEN PROOF OBLIGATION |
| DSD route proves global smoothness | none | NOT CLAIMED |

## Failure rule

A candidate route must be downgraded to **FAILED ROUTE** if it is shown to be incompatible with the original incompressible PDE, loses information needed by any proposed regularity implication, or cannot be made translation/rotation complete.
