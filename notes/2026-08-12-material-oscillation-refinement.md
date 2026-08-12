# Mean-centered material oscillation refinement

Date: 2026-08-12

Status: **ROUTE REFINEMENT / DERIVED IDENTITY + OPEN PROOF OBLIGATION**.

## 1. Why the point-centered all-scale candidate is rejected

The point-centered material channel

\[
C_{\rm rel}^{\rm point}(a,\ell,t)
=
\ell^{-1}\int_{B_\ell(a)}
|u(\Phi_t(b),t)-u(\Phi_t(a),t)|^2db
\]

is useful for following the relation between a distinguished center particle and its neighborhood.

It is not a good quantity for

\[
\sup_{\ell>0}
\]

on the whole-space problem.  For a localized velocity field with a nonzero center velocity, a very large material cell contains a huge region where the velocity is close to zero while the subtracted center velocity remains nonzero.  The resulting point-centered term can grow with the artificial choice of the distinguished center.

Therefore the proposed all-scale proof target based directly on `sup_ell C_rel^point` is **REJECTED / REPAIRED**, not retained.

## 2. Material mean and internal oscillation

Define the material-cell mean velocity

\[
\bar U(a,\ell,t)
=
\frac{1}{|B_\ell|}
\int_{B_\ell(a)}u(\Phi_t(b),t)db.
\]

Because `J=1`, this is also the volume average over the current material cell.

Define

\[
W(b,t)=u(\Phi_t(b),t)-\bar U(a,\ell,t)
\]

and the scale-critical oscillation channel

\[
\boxed{
C_{\rm osc}(a,\ell,t)
=
\ell^{-1}
\int_{B_\ell(a)}|W(b,t)|^2db.
}
\]

This quantity removes the bulk translation of the **whole tracked material cell**, not just the motion of one chosen center particle.

## 3. Exact point/mean channel decomposition

For the center-particle velocity

\[
U_c(t)=u(\Phi_t(a),t),
\]

the variance identity gives

\[
\int|u-U_c|^2db
=
\int|u-\bar U|^2db
+|B_\ell|\,|\bar U-U_c|^2.
\]

Hence

\[
\boxed{
C_{\rm rel}^{\rm point}
=C_{\rm osc}+C_{\rm drift}
}
\]

with

\[
C_{\rm drift}
=
\ell^{-1}|B_\ell|\,|\bar U-U_c|^2.
\]

Both channels are Navier--Stokes scale invariant, but they describe different information:

- `C_osc`: internal velocity variation of the cell;
- `C_drift`: distinguished center particle versus cell-mean drift.

They must not be collapsed.

## 4. Large scales are automatically controlled

The material mean minimizes the `L^2` deviation, so

\[
\int_{B_\ell(a)}|W|^2db
\le
\int_{B_\ell(a)}|u(\Phi_t(b),t)|^2db.
\]

Using `J=1`,

\[
\int_{B_\ell(a)}|u(\Phi_t(b),t)|^2db
=
\int_{\Omega_\ell^{\rm mat}(a,t)}|u(x,t)|^2dx
\le
\|u(t)\|_2^2.
\]

For the smooth unforced problem,

\[
\|u(t)\|_2^2\le\|u_0\|_2^2.
\]

Therefore

\[
\boxed{
C_{\rm osc}(a,\ell,t)
\le
\frac{\|u_0\|_2^2}{\ell}.
}
\]

Consequently

\[
\sup_a C_{\rm osc}(a,\ell,t)\to0
\qquad (\ell\to\infty).
\]

This is exactly the desired separation: **the infinite size of the total fluid is not the dangerous part; only finite and shrinking local material scales require new control.**

## 5. Exact material oscillation balance

The material mean acceleration is

\[
\dot{\bar U}
=
\overline{-\nabla p+\nu\Delta u}.
\]

Therefore

\[
\dot W
=-\left(\nabla p-\overline{\nabla p}\right)
+\nu\left(\Delta u-\overline{\Delta u}\right)
\]

along the material labels.

Define

\[
P_{\rm osc}
=
\ell\int W\cdot
\left(\nabla p-\overline{\nabla p}\right)db,
\]

\[
V_{\rm osc}
=
\nu\ell\int W\cdot
\left(\Delta u-\overline{\Delta u}\right)db.
\]

Then

\[
\boxed{
\ell^2\partial_t C_{\rm osc}
=-2P_{\rm osc}+2V_{\rm osc}.
}
\]

All three quantities `C_osc`, `P_osc`, and `V_osc` are invariant under the Navier--Stokes parabolic scaling when the material label and radius are scaled together.

## 6. Smooth small-scale asymptotic

For a smooth solution,

\[
\Phi_t(a+y)-\Phi_t(a)=F(a,t)y+o(|y|)
\]

and the mean of the linear term over the centered reference ball is zero. Thus

\[
\boxed{
C_{\rm osc}(a,\ell,t)
=
\frac{4\pi}{15}\ell^4
\| (\nabla u)(\Phi_t(a),t)F(a,t)\|_F^2
+o(\ell^4).
}
\]

So `C_osc -> 0` as `ell -> 0` at every smooth point.

A prospective singular concentration must therefore prevent this small-scale decay, or make another coupled critical channel diverge.

## 7. Revised DSD proof block

The material/local DSD block is refined to

\[
\mathcal M_{\rm osc}(a,\ell,t)=
\left(
C_{\rm osc},
C_{\rm drift},
P_{\rm osc},
V_{\rm osc},
\chi=-\lambda_1,
\lambda_2^+,
\Delta_{\rm shape},
\omega,\text{alignment},\ldots
\right).
\]

The first serious target is now a **finite/small-scale** estimate, not an uncontrolled whole-scale point-centered supremum.

A successful route still has to prove that boundedness of an appropriate time-space version of these channels forces a known regularity gate or directly excludes blow-up.

Status: **OPEN PROOF OBLIGATION**.
