# Proof / verification map

This file separates established identities, DSD bridge definitions, computational checks, external regularity anchors, failed-route candidates, and unresolved proof targets.

| Item | Current support | Status |
|---|---|---|
| 3D incompressible Navier–Stokes baseline on `R^3` | repository baseline note | NAVIER–STOKES INPUT |
| Gaussian double-curl benchmark is divergence-free | exact SymPy identity | COMPUTATIONAL CHECK / exact symbolic |
| Vorticity formula for benchmark | exact SymPy identity | COMPUTATIONAL CHECK / exact symbolic |
| Pressure Poisson source `-Delta p = Q` | exact SymPy identity | COMPUTATIONAL CHECK / exact symbolic |
| Radial channel at `r=0` is inapplicable, not zero | coordinate definition + typed DSD interpretation | BRIDGE DEFINITION |
| Radial channel away from origin can be defined zero | direct benchmark evaluation | COMPUTATIONAL CHECK |
| `x/y/z` seeds are rotation-equivalent | coordinate permutation | DERIVED BENCHMARK FACT |
| Fixed-time shell terms `T_E,T_W,T_P,T_Ei` | analytic definitions | BRIDGE DEFINITION |
| Total shell energy isotropic at `r=sqrt(2)` while axis energies remain unequal | exact angular/shell formulas | COMPUTATIONAL CHECK / exact symbolic |
| Enstrophy shell vanishes at `r=sqrt(5/2)` while energy is nonzero | closed-form formulas | COMPUTATIONAL CHECK |
| Quadratic descriptor collision for `u` and `-u` | exact construction | COMPUTATIONAL CHECK |
| `r^2 T_E`, `r^4 T_W`, `r^4 T_P` scaling covariance | exact scaling + pressure inversion check | COMPUTATIONAL CHECK |
| Centered candidate `D_O` | finite sampling only | CONJECTURE / TARGET |
| All-center descriptor `D_all` | definition only | CONJECTURE / TARGET |
| Velocity-gradient block has `tr S=0` | exact identity | COMPUTATIONAL CHECK / exact symbolic |
| Benchmark vortex-stretching formula `omega^T S omega` | exact identity | COMPUTATIONAL CHECK / exact symbolic |
| Signed stretching cancels while positive/negative parts are nonzero | exact shell/whole-space integration | COMPUTATIONAL CHECK |
| Benchmark `Sigma_+=Sigma_-=992*pi/81` | exact whole-space integration | COMPUTATIONAL CHECK |
| `div R_adv=-Q`, `div R_pres=+Q`, `div R_visc=0` | incompressible identity + exact benchmark check | DERIVED IDENTITY / CHECK |
| Translated benchmark recovers its special shell about the translated center | deterministic quadrature + scaling | COMPUTATIONAL CHECK |
| Same-radius shell about an unrelated fixed origin becomes anisotropic | deterministic quadrature | COMPUTATIONAL CHECK |
| Linear benchmark superposition remains divergence-free | exact symbolic identity | COMPUTATIONAL CHECK / exact symbolic |
| Nonlinear source has nonzero `Q_cross` under superposition | exact symbolic expression + point evaluation | COMPUTATIONAL CHECK / exact symbolic |
| DSD off-diagonal dynamic channels required for nonlinear interactions | interpretation of `Q_cross` | BRIDGE DEFINITION |
| Vorticity-direction factorization `sigma=|omega|^2 gamma` with `gamma=xi^T S xi` | exact spectral identity | DERIVED IDENTITY |
| Benchmark `gamma=4 z exp(-|x|^2)` where `|omega|>0` | exact symbolic identity | COMPUTATIONAL CHECK / exact symbolic |
| `xi`/alignment undefined where `|omega|=0`, despite removable quotient extension | typed bridge | BRIDGE DEFINITION |
| `gamma=sum_i lambda_i (xi·e_i)^2`, alignment weights sum to one | eigenframe identity + samples | DERIVED IDENTITY / CHECK |
| Benchmark direction variation `|grad xi|^2=1/(x^2+y^2)` | exact symbolic identity | COMPUTATIONAL CHECK / exact symbolic |
| Magnitude-weighted variation cancels axis singularity | exact identity and whole-space integral | COMPUTATIONAL CHECK / exact symbolic |
| Constantin–Fefferman vorticity-direction regularity line | Constantin–Fefferman (1993) | EXTERNAL REGULARITY ANCHOR |
| Stretching of a two-seed sum is not the sum of self stretchings | exact expansion | DERIVED IDENTITY |
| Exact benchmark cross-stretching reverses the sign predicted by self terms at `(1/4,1/2,0)` | exact analytic witness | COMPUTATIONAL CHECK / exact symbolic |
| DSD off-diagonal stretching blocks are required | sign-reversal witness | BRIDGE REQUIREMENT |
| `L^infty_t L^3_x` control implies smoothness in the endpoint theorem | Escauriaza–Seregin–Šverák (2003) | EXTERNAL REGULARITY ANCHOR |
| `T_3(t)=int |u|^3` is Navier–Stokes scale invariant | direct scaling | BRIDGE DEFINITION / EXACT SCALING |
| Smooth `L^3` balance: advection cancels, viscosity dissipates, pressure correlation remains | direct calculation | DERIVED IDENTITY |
| Symmetric single seed has `Pi3=0` by reflection parity | exact parity + numerical audit | DERIVED IDENTITY / CHECK |
| Asymmetric two-seed benchmarks produce positive and negative `Pi3` | FFT pressure audit, multiple resolutions | COMPUTATIONAL CHECK |
| `Pi3` positive benchmark stable over `48^3..96^3` with ~0.33% spread | deterministic convergence table | COMPUTATIONAL CHECK |
| Fixed-shape amplitude laws `T3,D3~A^3`, `Pi3~A^4` | exact homogeneity | DERIVED IDENTITY |
| Unconditional monotone decay of global `L3` | amplified positive-`Pi3` benchmark predicts positive initial rate | FAILED-ROUTE CANDIDATE / needs rigorous certification |
| Shell-to-ball coarea reconstruction | Euclidean coarea + exact benchmark integrals | DERIVED IDENTITY / CHECK |
| Whole kinetic energy/enstrophy recovered from shell family | exact symbolic radial integration | COMPUTATIONAL CHECK / exact symbolic |
| Local parabolic `C_u`, `C_p`, `E_grad` bridge quantities are scale invariant | exact scaling bookkeeping | BRIDGE DEFINITION / EXACT SCALING |
| CKN partial regularity of suitable weak solutions | Caffarelli–Kohn–Nirenberg (1982) | EXTERNAL REGULARITY ANCHOR |
| Scaled local norms can serve as local regularity gates | later published interior criteria | EXTERNAL REGULARITY ANCHOR |
| Local kinetic-energy shell budget separates `F_adv,F_p,F_visc,D_r` | exact local energy identity | DERIVED IDENTITY |
| Symmetric benchmark has `F_adv=F_p=0` on centered spheres | exact parity | COMPUTATIONAL CHECK / exact symbolic |
| Symmetric benchmark viscous flux is outward for every `r>0` | exact positive formula | COMPUTATIONAL CHECK / exact symbolic |
| Asymmetric two-seed shell budget has nonzero signed advection/pressure flux | two-resolution spectral/volume audit | COMPUTATIONAL CHECK |
| Asymmetric pressure shell flux changes sign with radius | `N=64,80` deterministic audit | COMPUTATIONAL CHECK |
| One-way outward advective/pressure redistribution on every sphere | asymmetric sign witness | FAILED-ROUTE CANDIDATE |
| A-priori bound for `sup_t ||u||_3` from DSD channels | none | OPEN PROOF OBLIGATION |
| Non-circular control of pressure correlation `Pi3` | none | OPEN PROOF OBLIGATION |
| Non-circular control of positive vortex stretching / alignment channels | none | OPEN PROOF OBLIGATION |
| Translation-complete extension to arbitrary centers/data | finite covariance witness only | OPEN PROOF OBLIGATION |
| General control of all off-diagonal nonlinear cross couplings | finite two-seed witnesses only | OPEN PROOF OBLIGATION |
| Force an established local regularity gate at every candidate singular point/scale | geometry/scaling bridge only | OPEN PROOF OBLIGATION |
| Global a-priori bound for arbitrary admissible initial data | none | OPEN PROOF OBLIGATION |
| DSD route proves global smoothness | none | NOT CLAIMED |

## Failure rule

A candidate route is marked **FAILED-ROUTE CANDIDATE** when a stable computational witness contradicts it but rigorous certification is still missing. It is promoted to **FAILED ROUTE** only after analytic or certified numerical exclusion.

Any route incompatible with the original incompressible PDE, dependent on a preferred origin, or discarding information needed for a proposed regularity implication must be rejected or repaired before use in a proof.
