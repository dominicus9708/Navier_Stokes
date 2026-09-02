# DSD M5-584 — Ergodic q-Averaged Wedge Momentum Law

Date: 2026-09-02

Status: **THE ZERO-MEAN FIRST-JET NET-FORCE CONDITION IS THE z=0 BOUNDARY VALUE OF AN EXACT WEDGE MOMENTUM-TRANSPORT LAW. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Exact momentum conservation

The smooth ancient solution satisfies

\[
\partial_su=\nabla\cdot\mathbb T,
\]

with

\[
\mathbb T
=
\nabla u+(\nabla u)^T-u\otimes u-pI.
\]

In wedge variables,

\[
u=r^{-1}F,
\qquad p=r^{-2}H,
\]

so the stress has the critical form

\[
\boxed{
\mathbb T(x,s)
=r^{-2}\mathbb T_F(z,q,\omega).
}
\]

Also

\[
\boxed{
\partial_su
=-r^{-3}\partial_zF.
}
\]

---

## 2. Sphere-integrated velocity and stress flux

Define the spherical velocity moment

\[
\boxed{
\mathcal M(z,q)
:=
\int_{S^2}F(z,q,\omega)d\omega
}
\]

and the scale-normalized momentum-stress flux

\[
\boxed{
\mathcal F(z,q)
:=
\int_{S^2}\mathbb T_F(z,q,\omega)e_r\,d\omega.
}
\]

Because

\[
dS_x=r^2d\omega,
\]

\(\mathcal F\) is exactly the physical stress flux through \(S_r\):

\[
\int_{S_r}\mathbb Tn\,dS
=\mathcal F(z,q).
\]

---

## 3. Exact wedge sphere-momentum identity

At fixed physical time \(s\), differentiate the physical stress flux with respect to radius.

By the divergence theorem,

\[
\frac d{dr}
\int_{S_r}\mathbb Tn\,dS
=
\int_{S_r}\partial_su\,dS.
\]

The right side is

\[
\int_{S_r}\partial_su\,dS
=
-r^{-1}\int_{S^2}\partial_zF\,d\omega
=
-r^{-1}\partial_z\mathcal M.
\]

Since at fixed \(s\),

\[
r\partial_r=\mathfrak D
=\partial_q-2z\partial_z,
\]

we obtain

\[
\boxed{
\mathfrak D\mathcal F
=-\partial_z\mathcal M.
}
\]

Equivalently,

\[
\boxed{
(\partial_q-2z\partial_z)\mathcal F
=-\partial_z\mathcal M.
}
\]

This is an exact vector identity.

---

## 4. q-ergodic averaging

Let bars denote invariant \(q\)-means:

\[
\overline{\mathcal M}(z)
:=\langle\mathcal M(z,q)\rangle_q,
\]

\[
\overline{\mathcal F}(z)
:=\langle\mathcal F(z,q)\rangle_q.
\]

Stationarity gives

\[
\langle\partial_q\mathcal F\rangle_q=0.
\]

Therefore

\[
-2z\overline{\mathcal F}'(z)
=-\overline{\mathcal M}'(z),
\]

so

\[
\boxed{
\overline{\mathcal M}'(z)
=
2z\overline{\mathcal F}'(z).
}
\]

This is the q-averaged wedge momentum law.

---

## 5. Terminal boundary condition

At \(z=0\),

\[
F(0,q,\omega)=A(q,\omega),
\]

and

\[
\partial_zF(0,q,\omega)=C(q,\omega).
\]

Hence

\[
\boxed{
\overline{\mathcal M}'(0)
=
\left\langle
\int_{S^2}C(q,\omega)d\omega
\right\rangle.
}
\]

But the averaged wedge law gives

\[
\boxed{
\overline{\mathcal M}'(0)=0.
}
\]

Therefore

\[
\boxed{
\left\langle
\int_{S^2}C\,d\omega
\right\rangle=0,
}

exactly recovering M5-574's first-jet net-force cancellation.

Thus that cancellation is a genuine boundary condition imposed by full wedge momentum transport.

---

## 6. Pointwise terminal recovery

Before q-averaging, setting \(z=0\) in

\[
\mathfrak D\mathcal F=-\partial_z\mathcal M
\]

gives

\[
\partial_q\mathcal F(0,q)
=-\int_{S^2}C(q,\omega)d\omega.
\]

This is exactly M5-574's terminal stress-flux derivative law

\[
\boxed{
\mathcal F_A'(q)=-m_C(q).
}
\]

So both the pointwise and mean terminal identities are contained in the wedge momentum equation.

---

## 7. Alternative integrated form

From

\[
\overline{\mathcal M}'=2z\overline{\mathcal F}',
\]

we have

\[
\frac d{dz}
\left(
\overline{\mathcal M}-2z\overline{\mathcal F}
\right)
=-2\overline{\mathcal F}.
\]

Thus

\[
\boxed{
\left(
\overline{\mathcal M}-2z\overline{\mathcal F}
\right)'
=-2\overline{\mathcal F}.
}
\]

If a sign or endpoint condition for the mean stress flux can be obtained, this becomes a monotonicity relation.

At present no such general sign is inherited.

---

## 8. Relation to the stationary terminal defect

On a stationary terminal profile \(C=0\), the terminal stress flux is constant in \(q\):

\[
\mathcal F(0,q)=\kappa.
\]

The wedge law shows that this is merely the \(z=0\) boundary value of the stress-flux field \(\mathcal F(z,q)\) that connects the terminal defect to the Type-I core.

Therefore the Landau/stationary stress defect should be viewed as a boundary momentum-flux datum for the wedge problem rather than an isolated distributional artifact.

---

## 9. Combined reduced system

Together with M5-583, the q-averaged wedge hard core now carries

\[
\boxed{
\mathscr E'
+2z\mathscr J'
+\mathscr J
=\mathscr D\ge0,
}

and

\[
\boxed{
\overline{\mathcal M}'
=2z\overline{\mathcal F}'.
}
\]

The terminal conditions are

\[
\boxed{
\mathscr E'(0)
=\langle A\cdot C\rangle,
}
\]

\[
\boxed{
\overline{\mathcal M}'(0)=0,
}
\]

with positive terminal critical densities from M5-571/M5-580.

The next target is the vorticity/enstrophy wedge law, because vortex stretching is the remaining nonlinear channel with a signed average production \(\langle Q\rangle>0\) inherited from the similarity hull.

Status: **ENERGY AND MOMENTUM HAVE BOTH BEEN REDUCED TO z-TRANSPORT LAWS AFTER q-AVERAGING. THE NEXT NATURAL EQUATION IS THE q-AVERAGED WEDGE ENSTROPHY/VORTICITY BALANCE. GLOBAL REGULARITY REMAINS UNPROVED.**