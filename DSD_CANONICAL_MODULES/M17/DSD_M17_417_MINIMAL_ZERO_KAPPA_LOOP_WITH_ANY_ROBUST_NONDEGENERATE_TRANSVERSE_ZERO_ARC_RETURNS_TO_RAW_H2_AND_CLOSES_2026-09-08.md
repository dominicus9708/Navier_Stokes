# DSD M17-417 — A minimal `kappa=0` loop with any robust nondegenerate transverse zero arc returns to raw-`H2` and closes

Date: 2026-09-08  
Canonical ID: **M17-417**

Status: **ACTIVE ZERO-LOOP TRANSVERSE DICHOTOMY / REGULAR-ZERO CONDITIONAL CLOSURE / DEGENERATE-GRADIENT REDUCTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-416

On the retained compact loop branch with minimal full omega-limit and the M17-413 geometry, M17-416 reduces every surviving loop state to

\[
\boxed{\kappa_\Gamma\equiv0.}
\]

Because M17-313 gives

\[
D_\xi\kappa=0,
\]

the coefficient gradient is transverse to the vortex direction:

\[
\boxed{\nabla\kappa\perp W.}
\]

The next question is whether the zero loop is transversely regular or degenerate.

## 2. Record-scale nondegenerate transverse zero hypothesis

Let the descendant own-scale be

\[
r_m\asymp R_m^{-1}
\]

inside the parent-normalized record cell.

The natural intrinsic scale at a zero level is the M17-340 gradient scale

\[
\boxed{r_{\nabla\kappa}:=|\nabla\kappa|^{-1/3}.}
\]

Assume there exists one state `z_*` in the minimal omega-limit and one point `s_*` on the loop such that the transverse zero gradient is nondegenerate at the descendant scale:

\[
\boxed{
c_g r_m^{-3}
\le
|\nabla\kappa(s_*,z_*)|
\le
C_g r_m^{-3}.}
\]

Equivalently, in descendant own-scale normalized coordinates,

\[
c_g\le|\nabla\kappa^{norm}|\le C_g.
\]

Assume also the regular loop amplitude is bounded below at that point and the tubular geometry is retained.

Failure of these scale/amplitude/geometric assumptions is kept as an explicit exit.

## 3. One nondegenerate point gives a parent-length fraction arc

In the compact regular loop-state topology, `nabla kappa`, the loop embedding, and the vorticity amplitude vary continuously.

Therefore from one strict nondegenerate point one obtains:

- a state neighborhood `U_g` of `z_*`;
- an arclength interval `I_g` on the loop of fixed parent-normalized length
  \[
  |I_g|\ge\ell_g>0;
  \]
- uniform constants `g_-,g_+,rho_*>0`;

such that throughout `U_g` and on `I_g`,

\[
\boxed{
\kappa=0,
\qquad
g_-r_m^{-3}\le|\nabla\kappa|\le g_+r_m^{-3},
\qquad
\rho\ge\rho_*.
}
\]

Thus one nondegenerate point produces a **fixed positive parent-length fraction** of regular zero arc, not merely one isolated descendant cell.

## 4. Linear number of zero-corridor segments

Partition the fixed arc `I_g` into descendant own-scale subsegments of length `O(r_m)`.

Under the same tubular reach/bounded-overlap hypothesis as M17-413,

\[
\boxed{
N_{x,m}^{zero}
\gtrsim
\frac{\ell_g}{r_m}
\asymp
c\ell_gR_m.
}
\]

Hence the regular zero arc supplies the same missing linear spatial multiplicity as an away-zero parent-length loop.

## 5. M17-409 supplies raw-H2 payment on each zero corridor

M17-409 proves that on a uniformly regular zero corridor, coarea plus a coefficient-gradient ceiling gives

\[
\boxed{
H_{0,\delta}
\ge
c_{0H}A_{\kappa\kappa}(0).
}
\]

On the own-scale normalized zero arc in Sections 2--4, the uniform amplitude floor, transverse gradient lower bound, and fixed tubular geometry give a fixed positive lower bound on the local zero-level diffusion density per normalized segment:

\[
\boxed{
A_{\kappa\kappa}^{seg}(0)
\ge a_*>0.
}
\]

Therefore every selected zero-corridor segment carries

\[
\boxed{
h_{seg}^{norm}\ge h_*>0}
\]

of normalized raw-`H2` corridor charge during one unit own-time, with constants uniform on the robust state neighborhood.

This is exactly the regular-zero counterpart of the positive-flux segment payment used in M17-413.

## 6. Minimality gives syndetic zero-gradient good states

The minimal full omega-limit hypothesis remains in force.

The robust nondegenerate zero-arc condition defines a nonempty relative open state set `U_g`.

By M17-415, visits to `U_g` are syndetic with uniform dwell time, and the original orbit has positive lower asymptotic occupation density in the corresponding good-state set, provided the representation-safe record map persists.

Hence the record occupancy fractions `alpha_m^zero` satisfy

\[
\boxed{
\sum_m\alpha_m^{zero}=\infty.
}
\]

## 7. Space-time count and ancestry contradiction

At each good record,

\[
N_{x,m}^{zero}\gtrsim cR_m.
\]

A good-time fraction `alpha_m^zero` supplies

\[
N_{t,m}^{zero}\gtrsim c\alpha_m^{zero}R_m^2
\]

unit own-time blocks.

Thus the normalized raw-`H2` zero-corridor charge is

\[
H_{m,zero}^{norm}
\gtrsim
c h_*\alpha_m^{zero}R_m^3.
\]

Apply the M17-405 ancestry weight:

\[
\boxed{
R_m^{-3}H_{m,zero}^{norm}
\gtrsim
c h_*\alpha_m^{zero}.
}
\]

Since

\[
\sum_m\alpha_m^{zero}=\infty,
\]

the ancestral raw-`H2` sum diverges, contradicting M17-405.

## 8. Minimal zero-loop dichotomy

Therefore, under the retained compact geometry and record map,

\[
\boxed{
\begin{aligned}
&\Omega_\omega\text{ minimal},\\
&\kappa_\Gamma\equiv0,\\
&\exists\text{ robust own-scale transverse }\nabla\kappa\neq0
\end{aligned}
\Longrightarrow
\text{contradiction}.
}
\]

Hence every surviving minimal zero loop must satisfy the degenerate alternative

\[
\boxed{
\nabla\kappa=0
\quad\text{on the loop throughout the minimal omega-limit},
}
\]

or escape through amplitude/tubular/scale/genealogy/interface loss.

## 9. Scope firewall

The conclusion requires a **record-scale** transverse gradient:

\[
|\nabla\kappa|\asymp r_m^{-3}.
\]

A nonzero gradient whose intrinsic gradient scale is much larger or smaller than the descendant record scale must be reassigned to its true M17-340 scale or routed to coefficient-gradient decompactification.

Thus the theorem does not manufacture a record match from a bare inequality `nabla kappa != 0`.

## 10. Revised compact minimal-loop survivor

Combining M17-416 and M17-417, the retained minimal full-omega-limit loop branch is reduced to

\[
\boxed{
\kappa_\Gamma=0,
\qquad
\nabla\kappa|_\Gamma=0,
}
\]

unless a named geometry/scale/genealogy exit occurs.

This is a **critical coefficient-zero, zero-gradient loop**.

It is much narrower than the original recurrent closed-loop CE-H branch.

## 11. Next target

At such a loop, first-order transverse coefficient information vanishes.

The next audit is finite-order transverse vanishing:

\[
\kappa=0,
\quad
\nabla\kappa=0,
\quad
D^2\kappa\ ?
\]

Because the late CE-H states are analytic on the retained regular branch, one must determine whether a finite transverse jet order produces a higher-order intrinsic scale and another corridor payment, or whether all transverse jets vanish and `kappa` is locally identically zero near the loop.

## 12. DSD audit

The DSD role is a degeneracy-order audit. Regular zero crossing is not a separate terminal branch once the new finite raw-`H2` ancestor is available; the only minimal-loop survivor moves to a higher-order zero.

## 13. Audit verdict

**PASS — regular transverse zero-loop branch conditionally closed.**

The compact minimal loop frontier is now a higher-order coefficient-flatness problem or an explicit geometry/scale/genealogy loss.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]