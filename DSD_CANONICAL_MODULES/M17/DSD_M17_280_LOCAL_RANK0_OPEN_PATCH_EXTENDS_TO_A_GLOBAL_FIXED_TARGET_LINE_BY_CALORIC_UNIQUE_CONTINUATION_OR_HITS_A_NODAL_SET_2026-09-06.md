# DSD M17-280 — A local Rank-0 open patch extends to a global fixed target line by caloric unique continuation, or the scalar amplitude hits a nodal set

Date: 2026-09-06  
Canonical ID: **M17-280**

Status: **LOCAL-TO-GLOBAL RANK-0 EXTENSION GATE / THE M17-269--279 FRONTIER LEFT ONE LOWER-RANK RESIDUAL: M17-275 CLOSES ONLY A GLOBAL ENTIRE POSITIVE RANK-0 TANGENT, WHILE M17-273/278 CAN PRODUCE A MERELY LOCAL RANK-0 PATCH. ON A RAW HEAT TANGENT, HOWEVER, A RANK-0 OPEN PATCH HAS A CONSTANT DIRECTOR `xi_0`. EVERY CONSTANT TARGET COMPONENT `eta·V` WITH `eta PERP xi_0` SOLVES THE SCALAR HEAT EQUATION AND VANISHES ON A NONEMPTY OPEN SPACETIME SET. INTERIOR ANALYTICITY / UNIQUE CONTINUATION FOR CALORIC FUNCTIONS FORCES THOSE ORTHOGONAL COMPONENTS TO VANISH ON THE ENTIRE CONNECTED TANGENT DOMAIN. THUS THE WHOLE TANGENT LIES IN ONE FIXED TARGET LINE: `V=b xi_0`. DIVERGENCE-FREE GIVES `D_{xi_0}b=0`, SO `b` IS A TWO-DIMENSIONAL SCALAR ANCIENT HEAT SOLUTION. IF `b` NEVER VANISHES, ITS SIGN IS GLOBAL AND M17-275 APPLIES AFTER POSSIBLY REVERSING `xi_0`; IF `b` VANISHES, THAT IS THE EXPLICIT NODAL EXIT. THEREFORE A LOCAL RANK-0 OPEN PATCH DOES NOT REMAIN AN INDEPENDENT EXTENSION RESIDUAL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Local Rank-0 patch

Let `V` be the entire raw heat tangent obtained on the payer-free compact branch.

Assume there exists a nonempty connected open spatial patch

\[
U\subset\mathbb R^3
\]

on which

\[
\boxed{D\xi=0}
\]

and

\[
V\ne0.
\]

Because M17-260 gives

\[
\partial_\tau\xi=0,
\]

the same director is present through the ancient time interval wherever the patch remains active.

On `U`,

\[
\boxed{\xi\equiv\xi_0}
\]

for one constant unit vector.

---

## 2. Orthogonal target components vanish locally

Choose two constant orthonormal vectors

\[
\eta_1,\eta_2\perp\xi_0.
\]

Define scalar components

\[
\boxed{u_m:=\eta_m\cdot V.}
\]

Because `V` solves

\[
\partial_\tau V=\Delta V,
\]

each component satisfies

\[
\boxed{
\partial_\tau u_m=\Delta u_m.
}
\]

On the Rank-0 patch,

\[
V=a\xi_0,
\]

so

\[
\boxed{u_m=0}
\]

on a nonempty open spacetime subset.

---

## 3. Caloric unique continuation

Interior caloric solutions are real analytic in the spatial variables and time on every compact interior cylinder.

Therefore a scalar caloric function that vanishes on a nonempty open subset of a connected caloric domain vanishes identically on that connected domain.

Hence

\[
\boxed{u_1\equiv u_2\equiv0.}
\]

Thus

\[
\boxed{
V=b\xi_0
}
\]

globally on the connected entire tangent domain for one real scalar ancient caloric function `b`.

This conclusion concerns the fixed **target line** `R xi_0`; the scalar coefficient may still change sign by passing through zero.

---

## 4. Divergence-free reduction

The tangent is divergence free:

\[
0=\nabla\cdot V
=\xi_0\cdot\nabla b.
\]

Therefore

\[
\boxed{D_{\xi_0}b=0.}
\]

After rotating coordinates so that

\[
\xi_0=e_3,
\]

we obtain

\[
\boxed{b=b(x_1,x_2,\tau)}
\]

and

\[
\boxed{
\partial_\tau b=\Delta_\perp b.
}
\]

---

## 5. No-zero branch

Suppose

\[
\boxed{b(x,\tau)\ne0}
\]

for the entire connected ancient domain.

By continuity and connectedness, `b` has one fixed sign.
After replacing

\[
(\xi_0,b)
\mapsto
(-\xi_0,-b)
\]

if necessary, assume

\[
\boxed{b>0.}
\]

Then the global positive ancient Rank-0 theorem M17-275 applies.
It gives

\[
K=\partial_\tau\log b\ge0,
\]

which is incompatible with the retained critical sign-balanced `K` survivor.

Thus the global no-zero Rank-0 line branch closes.

---

## 6. Zero branch

If instead there exists

\[
(x_*,\tau_*)
\]

with

\[
\boxed{b(x_*,\tau_*)=0,}
\]

then

\[
V(x_*,\tau_*)=0.
\]

The director is undefined there.
This is precisely the explicit

\[
\boxed{G_{nodal/amplitude\ degeneration}}
\]

branch already retained throughout M17.

No attempt is made to continue a fixed orientation through the zero.

---

## 7. Correct local Rank-0 conclusion

Therefore

\[
\boxed{
H_{local\ Rank0\ open\ patch}
\Longrightarrow
H_{global\ fixed\ target\ line}
\Longrightarrow
\bot
\lor
G_{nodal/amplitude\ degeneration}
}
\]

on the critical sign-balanced `K` survivor.

More compactly,

\[
\boxed{
H_{local\ Rank0\ open\ patch}
\Longrightarrow
G_{nodal/amplitude\ degeneration}
}
\]

because the no-node continuation is closed by M17-275.

---

## 8. Scope firewall

The unique-continuation step requires a genuine nonempty open Rank-0 spacetime patch of the raw heat tangent.

A rank drop occurring only on a measure-zero set, isolated point, or vanishing microcarrier is not upgraded to this theorem.
Those cases remain in the strict-subscale/rank-interface ledger.

The theorem also does not claim that the original nonlinear vorticity has globally constant direction; it concerns the extracted raw heat tangent.

---

## 9. DSD audit

- Target-line continuation is derived from scalar caloric unique continuation, not from director continuity across zeros.
- Scalar sign change is allowed only through an explicit node.
- M17-275 is imported only on the global no-zero positive branch.
- Measure-zero rank degeneration remains distinct from an open Rank-0 patch.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
