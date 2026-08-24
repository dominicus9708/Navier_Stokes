# DSD core-tail static compatibility / dynamic maintenance audit

Date: 2026-08-25

Status: **STATIC CORE+PASSIVE-TAIL COMPATIBILITY WITNESS CONSTRUCTED / CURRENT FUNCTION-SPACE LEDGERS DO NOT CONTRADICT THE 1/r TAIL / CORE-TAIL COEXISTENCE IS NOT A PRIMITIVE CONTRADICTION / DYNAMIC CRITICAL-TAIL MAINTENANCE REMAINS OPEN / GLOBAL REGULARITY UNPROVED.**

This note audits the Core--Tail Renormalized Compatibility Gate (CTRCG) after the parabolic-renormalization correction.

The purpose is to decide whether the mere coexistence of an order-one recurrent normalized core and a global non-L3 critical tail is already contradictory to the currently formed channels.

It is not. A concrete divergence-free static witness realizes exactly the critical functional behavior that the existing ancient-tail ledger permits.

The witness is **not** asserted to solve Navier--Stokes. It is a countermodel only to an attempted logical implication from the present norm/decoupling assumptions to contradiction.

## 1. A divergence-free 1/r critical tail

Fix a constant vector `a in R^3`, a radius `R0>0`, and a smooth radial cutoff `chi(r)` satisfying

\[
\chi(r)=0\quad(r\le R_0),
\qquad
\chi(r)=1\quad(r\ge2R_0).
\]

Define

\[
\boxed{
U_T(x)
:=
\chi(|x|)\frac{a\times x}{|x|^2}.
}
\]

Because `a x x` is tangent to spheres and `chi(r)/r^2` is radial,

\[
\nabla\left(\frac{\chi(r)}{r^2}\right)
\cdot(a\times x)=0.
\]

Also

\[
\nabla\cdot(a\times x)=0.
\]

Therefore

\[
\boxed{\nabla\cdot U_T=0.}
\]

Status: **PROVED.**

## 2. Critical pointwise decay

For `r>=2R0`,

\[
U_T(x)=\frac{a\times x}{r^2}.
\]

Hence

\[
|U_T(x)|\le \frac{|a|}{r},
\]

and on an angular subset of every sphere having fixed positive surface fraction,

\[
|U_T(x)|\ge c\frac{|a|}{r}.
\]

Differentiation gives

\[
\boxed{
|\nabla U_T(x)|\asymp\frac{|a|}{r^2}
}
\]

away from the finite transition annulus, and therefore

\[
|\Omega_T(x)|=|\nabla\times U_T(x)|\lesssim\frac{|a|}{r^2}.
\]

Thus the tail has exactly the borderline velocity decay identified by the ancient-shell route.

## 3. The tail is outside L3 but inside L6

For the cubic norm, use the positive angular-fraction lower bound:

\[
\int_{|x|>2R_0}|U_T|^3dx
\gtrsim
|a|^3\int_{2R_0}^{\infty}\frac{r^2}{r^3}dr
=
|a|^3\int_{2R_0}^{\infty}\frac{dr}{r}
=\infty.
\]

Therefore

\[
\boxed{U_T\notin L^3(\mathbb R^3).}
\]

On the other hand,

\[
\int_{|x|>2R_0}|U_T|^6dx
\lesssim
|a|^6\int_{2R_0}^{\infty}r^{-4}dr
<\infty.
\]

Hence

\[
\boxed{U_T\in L^6(\mathbb R^3).}
\]

This exactly matches the gap used by the ancient L3-tail survivor.

Status: **PROVED.**

## 4. Finite Dirichlet energy and finite tail enstrophy

Since

\[
|\nabla U_T|\lesssim |a|r^{-2},
\]

we have

\[
\int_{|x|>2R_0}|\nabla U_T|^2dx
\lesssim
|a|^2\int_{2R_0}^{\infty}r^{-2}dr
\lesssim
\frac{|a|^2}{R_0}.
\]

The cutoff region contributes another finite quantity of the same scaling order. Thus

\[
\boxed{
\|\nabla U_T\|_2^2
\lesssim
\frac{|a|^2}{R_0}.
}
\]

Likewise

\[
\boxed{
\|\Omega_T\|_2^2
\lesssim
\frac{|a|^2}{R_0}.
}
\]

Therefore the non-L3 tail is completely compatible with finite normalized Dirichlet/enstrophy content.

This is the static version of the shell ledger

\[
\sum_ke_k<\infty,
\qquad
\sum_k(R_ke_k)^{3/2}=\infty.
\]

## 5. Exact dyadic shell scaling

Let

\[
A_R=\{R<|x|<2R\},
\qquad R\ge2R_0,
\]

and define

\[
e_R:=\int_{A_R}|\nabla U_T|^2dx.
\]

The pointwise two-sided decay on a positive angular fraction gives

\[
\boxed{
e_R\asymp\frac{|a|^2}{R}.}
\]

Hence the weighted Dirichlet number

\[
J_R:=Re_R
\]

satisfies

\[
\boxed{J_R\asymp |a|^2.}
\]

For dyadic radii `R_k=2^kR0`, therefore

\[
\boxed{
\sum_ke_{R_k}<\infty,
\qquad
\sum_kJ_{R_k}^{3/2}=\infty.
}
\]

This realizes the exact critical-shell pattern of the repository's non-L3 ancient survivor.

Status: **PROVED.**

## 6. The critical tail can be arbitrarily weak at the core

The tail vorticity obeys

\[
|\Omega_T(y)|\lesssim |a||y|^{-2}
\qquad(|y|\ge R_0).
\]

The strain at a core point is a Calderon--Zygmund transform of vorticity. At the origin, using only the absolute kernel bound,

\[
\begin{aligned}
|S_T(0)|
&\lesssim
\int_{|y|>R_0}\frac{|\Omega_T(y)|}{|y|^3}dy\\
&\lesssim
|a|\int_{R_0}^{\infty}r^{-3}dr.
\end{aligned}
\]

Therefore

\[
\boxed{
|S_T(0)|
\lesssim
\frac{|a|}{R_0^2}.
}
\]

The same estimate holds uniformly on any fixed core ball `B_M` once `R0>>M`, with only a changed constant.

Thus the tail may carry infinite global L3 mass while its direct strain action on a fixed normalized active core tends to zero as the tail is moved outward.

Status: **PROVED as a static remote-coupling estimate.**

## 7. Remote pressure-Hessian influence is also small

The pressure source generated purely by the tail is schematically quadratic in the gradient,

\[
|f_T|
=|\partial_iU_{T,j}\partial_jU_{T,i}|
\lesssim
|a|^2r^{-4}.
\]

A pressure Hessian uses a kernel of order `|y|^{-3}`. Hence on a fixed core,

\[
|\nabla^2P_T|
\lesssim
\int_{|y|>R_0}
|y|^{-3}|f_T(y)|dy
\lesssim
|a|^2\int_{R_0}^{\infty}r^{-5}dr.
\]

Therefore

\[
\boxed{
|\nabla^2P_T|_{core}
\lesssim
\frac{|a|^2}{R_0^4}.
}
\]

The cross pressure source between a compact core and a tail that vanishes on a neighborhood of that core requires separate localization, but no purely tail-generated order-one pressure Hessian is forced by the non-L3 shell stack itself.

## 8. Static core-tail superposition

Let `U_C` be any smooth compactly supported divergence-free core contained in `B_{R0/2}`.

Then

\[
U=U_C+U_T
\]

is divergence-free and satisfies

\[
U=U_C
\qquad\text{on }B_{R0}.
\]

Hence every finite local descriptor supported inside `B_{R0}` is exactly unchanged by the addition of `U_T`, while globally

\[
U\notin L^3,
\qquad
U\in L^6,
\qquad
\nabla U\in L^2.
\]

Moreover the tail can be moved to arbitrarily large `R0`, making its direct nonlocal strain/pressure influence on the fixed core arbitrarily small.

Again, this superposition is **not** asserted to be a Navier--Stokes solution.

Its role is logical:

\[
\boxed{
\text{local core recurrence}
+
\text{global non-L3 finite-Dirichlet tail}
+
\text{small instantaneous core coupling}
\not\Longrightarrow
\text{contradiction from the current static channels}.
}
\]

Status: **PROVED AS A FUNCTIONAL COMPATIBILITY COUNTERMODEL.**

## 9. DSD audit of CTRCG

The original Core--Tail Renormalized Compatibility Gate asked whether an order-one recurrent active core could coexist with a global critical tail escaping the available Liouville class.

The present witness shows that **coexistence itself is too weak a target**.

DSD separates the channels:

1. local core field;
2. global tail integrability defect;
3. weighted tail Dirichlet stack;
4. instantaneous remote strain coupling;
5. instantaneous remote pressure coupling;
6. actual Navier--Stokes spacetime evolution maintaining all of the above.

The first five channels can be made mutually compatible at a single time. Therefore only the sixth can still supply a contradiction.

Thus CTRCG is reclassified:

\[
\boxed{
\text{CTRCG is not a primitive static contradiction gate.}
}
\]

## 10. Critical local-energy scaling is also neutral

The `1/r` tail is critical not only for L3 and Dirichlet shell weighting.

On a shell `A_R`,

\[
\int_{A_R}|U_T|^2dx
\asymp
|a|^2R.
\]

The shell dissipation rate is

\[
\int_{A_R}|\nabla U_T|^2dx
\asymp
\frac{|a|^2}{R}.
\]

Over its natural parabolic time `R^2`, the dissipative cost is

\[
R^2\cdot\frac{|a|^2}{R}
\asymp
|a|^2R,
\]

which is exactly the same order as the shell kinetic energy.

Likewise a cubic advective energy flux has the dimensional size

\[
R^2\cdot(R^{-1})^3
\asymp
R^{-1},
\]

the same order as the instantaneous shell dissipation.

Therefore the local-energy equation is also scale-neutral at the `1/r` tail.

A successful closure cannot come merely from saying that a critical shell dissipates energy or requires flux; both terms live at the same scaling order.

Status: **PROVED AS A SCALING AUDIT.**

## 11. Corrected dynamic gate

The primitive question is now dynamical:

\[
\boxed{
\text{Can an unforced 3D Navier--Stokes ancient survivor maintain a non-L3}\
\text{finite-Dirichlet critical tail of essentially 1/r shell scaling while a}\
\text{nontrivial recurrent active core remains locally bounded and the direct}\
\text{tail-to-core coupling stays asymptotically passive?}
}
\]

Call this the **Dynamic Critical-Tail Maintenance Gate (DCTMG)**.

A successful closure must provide information beyond the current static norms. Candidate mechanisms are:

- a Liouville theorem allowing the non-L3 but finite-Dirichlet critical tail;
- a quantitative local-energy flux defect showing that the critical shell stack cannot be maintained through the ancient time direction;
- a stress/momentum-flux identity forcing a non-summable core or interface action;
- a genuine tail-to-core exchange theorem derived from the PDE rather than assumed from genealogy;
- a subcritical improvement of the 1/r tail on a cubic-divergent subset.

## 12. External-theory boundary used in the audit

The relevant known ancient-solution rigidity result used elsewhere in the repository is the Albritton--Barker theorem: a mild ancient solution bounded in global `L3` along a backward sequence is trivial.

That theorem does not apply to the witness class above because the global `L3` norm is precisely the channel that diverges.

General three-dimensional bounded ancient-solution Liouville rigidity is not currently available in a form that automatically removes this survivor.

Therefore no external theorem is imported here to close DCTMG.

## 13. Audit verdict

### PROVED

- an explicit divergence-free `1/r` tail exists with `U notin L3`, `U in L6`, and `grad U in L2`;
- its dyadic shell stack satisfies `e_k ~ R_k^{-1}`, `J_k ~ 1`, hence `sum e_k < infinity` but `sum J_k^{3/2}=infinity`;
- its tail vorticity is square-integrable;
- moving the tail outward makes its direct strain influence on a fixed core `O(R0^{-2})` and pure-tail pressure-Hessian influence `O(R0^{-4})`;
- a compact divergence-free core can therefore coexist with all current static tail channels without logical contradiction;
- the `1/r` local-energy balance is scale-neutral.

### PRUNED / CORRECTED

- `recurrent core + non-L3 critical tail` by itself as a contradiction target;
- energy/Dirichlet finiteness alone as an exclusion of the critical tail;
- instantaneous remote coupling alone as an exclusion of the critical tail.

### NOT DERIVED

- an actual Navier--Stokes ancient solution with the static witness form;
- persistence/maintenance of the passive critical tail under the PDE;
- DCTMG;
- contradiction to the bounded-Z singular branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
