# DSD M19-269 — Residual payer forces an interior wedge-energy maximum and positive weighted-flux derivative, but not global monotonicity

Date: 2026-09-15  
Canonical ID: **M19-269**  
Status: **ACTIVE SIGNED-WEDGE AUDIT / INTERIOR ENERGY MAXIMUM FORCED / LOCAL POSITIVE FLUX-DERIVATIVE CERTIFIED / GLOBAL MONOTONE CLOSURE FAILS / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Residual-payer input

On the M19-267 residual branch,

\[
\boxed{
\mathscr E'(0)
=
\left\langle\int_{S^2}A\cdot C\,d\omega\right\rangle
\ge
\frac{c_3}{2M_A}
=:\delta_E>0.
}
\]

The terminal wedge energy itself is

\[
\mathscr E(0)
=
\frac12
\left\langle\int_{S^2}|A|^2d\omega\right\rangle
=
\frac12c_2,
\]

with

\[
\boxed{
\mathscr E(0)
\ge
\frac{c_3}{2M_A}>0.
}
\]

Thus the mean scale-normalized energy initially rises as the wedge is entered from \(z=0\).

---

## 2. Deep-wedge decay

Recall the exact relation between wedge and similarity variables:

\[
|y|=z^{-1/2},
\qquad
F(z,q,\omega)=z^{-1/2}U(y,\theta).
\]

As

\[
z\to\infty,
\]

the similarity radius tends to the smooth center

\[
|y|\to0.
\]

On the retained smooth compact similarity class, \(U\) remains uniformly bounded at bounded \(y\). Hence

\[
|F|=O(z^{-1/2}),
\]

and therefore

\[
\boxed{
\mathscr E(z)=O(z^{-1})\to0
\qquad(z\to\infty).
}
\]

So the energy starts positive, initially increases, but ultimately tends to zero.

---

## 3. A positive interior maximum is forced

Because

\[
\mathscr E'(0)>0,
\]

there exists \(z_1>0\) such that

\[
\mathscr E(z_1)>\mathscr E(0).
\]

Because

\[
\mathscr E(z)\to0,
\]

continuity implies that \(\mathscr E\) attains a global maximum at some finite

\[
\boxed{z_E\in(0,\infty).}
\]

Moreover,

\[
\boxed{
\mathscr E(z_E)>\mathscr E(0)
\ge
\frac{c_3}{2M_A},
}
\]

and

\[
\boxed{
\mathscr E'(z_E)=0.
}
\]

This is a genuinely finite-depth consequence of the residual-payer sign.

---

## 4. Dissipation has a quantitative floor at an energy extremum

The wedge dissipation is

\[
\mathscr D(z)
=
\left\langle
\int_{S^2}
\left[
|(\mathfrak D-1)F|^2
+|\nabla_{S^2}F|^2
\right]d\omega
\right\rangle_q,
\]

with

\[
\mathfrak D=\partial_q-2z\partial_z.
\]

At fixed \(z\), write

\[
X:=\partial_qF-2z\partial_zF.
\]

Then

\[
|(\mathfrak D-1)F|^2
=|X-F|^2.
\]

Under the invariant \(q\)-mean,

\[
\left\langle\int_{S^2}F\cdot\partial_qF\,d\omega\right\rangle_q=0.
\]

Also

\[
\mathscr E'(z)
=
\left\langle\int_{S^2}F\cdot\partial_zF\,d\omega\right\rangle_q.
\]

Therefore

\[
\begin{aligned}
\left\langle\int|X-F|^2\right\rangle
&=
\left\langle\int|X|^2\right\rangle
+
\left\langle\int|F|^2\right\rangle
+4z\mathscr E'(z).
\end{aligned}
\]

At the interior maximum \(z_E\),

\[
\mathscr E'(z_E)=0,
\]

so

\[
\boxed{
\mathscr D(z_E)
=
2\mathscr E(z_E)
+
\left\langle\int_{S^2}
|\partial_qF-2z_E\partial_zF|^2d\omega
\right\rangle
+
\left\langle\int_{S^2}|\nabla_{S^2}F|^2d\omega\right\rangle.
}
\]

Hence

\[
\boxed{
\mathscr D(z_E)
\ge
2\mathscr E(z_E)
>
\frac{c_3}{M_A}
=:d_*>0.
}
\]

Thus the interior energy maximum carries a fixed positive wedge-dissipation floor.

---

## 5. Exact flux derivative at the maximum

M5-583 gives

\[
\boxed{
\mathscr E'
+2z\mathscr J'
+\mathscr J
=
\mathscr D.
}
\]

At \(z=z_E\),

\[
\mathscr E'(z_E)=0,
\]

so

\[
\boxed{
2z_E\mathscr J'(z_E)
+
\mathscr J(z_E)
=
\mathscr D(z_E)
>
\frac{c_3}{M_A}.
}
\]

Introduce the weighted flux

\[
\boxed{
\mathscr G(z):=\sqrt z\,\mathscr J(z).
}
\]

Then

\[
\mathscr G'(z)
=
\frac{\mathscr J+2z\mathscr J'}{2\sqrt z}
=
\frac{\mathscr D-\mathscr E'}{2\sqrt z}.
\]

At the maximum,

\[
\boxed{
\mathscr G'(z_E)
=
\frac{\mathscr D(z_E)}{2\sqrt{z_E}}
>
\frac{c_3}{2M_A\sqrt{z_E}}
>0.
}
\]

Therefore the residual payer forces a strictly increasing weighted radial-energy-flux observable at at least one finite wedge depth.

---

## 6. Why this is not the required recurrent signed drift

The new sign is a derivative in **wedge depth** \(z\), not in the recurrent log-radius/time coordinate \(q\).

The endpoints satisfy, under the retained regularity,

\[
\sqrt z\,\mathscr J(z)\to0
\qquad(z\downarrow0)
\]

because \(\mathscr J(0)\) is finite, and the smooth-center asymptotics give

\[
\sqrt z\,\mathscr J(z)\to0
\qquad(z\to\infty).
\]

Thus

\[
\boxed{
\mathscr G(0)=0,
\qquad
\mathscr G(\infty)=0.
}
\]

A derivative that is strictly positive at \(z_E\) must therefore be compensated by negative derivative somewhere else unless \(\mathscr G\) is identically zero, which it is not at the certified positive-derivative point.

Using

\[
\mathscr G'
=
\frac{\mathscr D-\mathscr E'}{2\sqrt z},
\]

any compensating negative region obeys

\[
\boxed{
\mathscr E'(z)>\mathscr D(z)\ge0.
}
\]

Thus the full wedge itself contains a compensating recharge/transport channel.

There is no globally one-way \(z\)-monotonicity.

---

## 7. Signed-observable firewall

The desired M5-598/M18 signed mechanism requires a bounded recurrent state observable whose generator has a strict one-way sign under the invariant **recurrent dynamics**.

The present quantity

\[
\mathscr G(z)=\sqrt z\,\mathscr J(z)
\]

fails that criterion for two independent reasons:

1. \(z\) is a scale-invariant depth coordinate, not the recurrent translation coordinate;
2. its two endpoint values agree, so any positive derivative is necessarily compensated elsewhere.

Therefore

\[
\boxed{
\mathscr G'(z_E)>0
\not\Rightarrow
\mathcal T_{aper}^{signed}.
}
\]

It is a finite-depth transport certificate, not a recurrent monotone contradiction.

---

## 8. Relation to the finite-depth enstrophy shell

M5-587 independently forces a finite depth \(z_*\) at which

\[
\mathscr Q_\omega(z_*)-\mathscr P_\omega(z_*)>0.
\]

M19-269 now forces, on the residual-payer branch, a finite depth \(z_E\) at which

\[
\mathscr G'(z_E)>0
\]

and

\[
\mathscr D(z_E)>d_*.
\]

Nothing presently proves

\[
z_E=z_*
\]

or even a fixed overlap between their neighborhoods.

Therefore the energy and enstrophy finite-depth witnesses must not be silently merged into one same-event contradiction.

Any such merger needs a new overlap/compactness theorem.

---

## 9. Verdict

The residual-payer sign does produce new finite-depth structure:

\[
\boxed{
\mathscr E'(0)>0
\Longrightarrow
\exists z_E>0:
\begin{cases}
\mathscr E'(z_E)=0,\\
\mathscr D(z_E)>c_3/M_A,\\
\mathscr G'(z_E)>0.
\end{cases}
}
\]

But the weighted flux returns to the same zero endpoint and must admit compensation.

Thus the attempted signed-depth closure fails:

\[
\boxed{
\text{residual terminal sign}
\Longrightarrow
\text{finite-depth signed flux event}
\not\Longrightarrow
\text{global monotone/recurrent contradiction}.
}
\]

The result is still useful because it sharply localizes where residual energy must be re-routed inside the wedge.

---

## 10. Updated frontier

The terminal-tail route is now reduced to three genuinely new possibilities only:

\[
\boxed{
\mathcal T_{tail}^{energy-defect}
\lor
\mathcal T_{aper}^{signed}
\lor
\mathcal T_{tail}^{rigidity/overlap}.
}
\]

The last term includes a possible theorem forcing the independently obtained finite-depth energy and enstrophy witnesses into the same compact region/event and deriving an exact PDE incompatibility there.

Absent such a theorem, another unsigned finite-depth payer calculation will not close the proof.

Global 3D Navier--Stokes regularity remains unproved.
