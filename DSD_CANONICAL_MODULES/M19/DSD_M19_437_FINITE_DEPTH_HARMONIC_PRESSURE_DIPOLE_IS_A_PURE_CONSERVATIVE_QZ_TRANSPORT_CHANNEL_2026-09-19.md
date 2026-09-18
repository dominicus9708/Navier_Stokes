# M19-437 — The finite-depth harmonic pressure dipole is a pure conservative q-z transport channel in the wedge energy ledger

Date: 2026-09-19  
Canonical ID: **M19-437**  
Status: **FINITE-DEPTH DIPOLE ENERGY IDENTITY / FOR A HARMONIC PRESSURE-DIPOLE COEFFICIENT SATISFYING D a=0, ITS RADIAL ENERGY-FLUX TERM PLUS ITS MOMENTUM-EQUATION WORK IS EXACTLY D OF ONE FIRST-MOMENT OBSERVABLE / AFTER q-AVERAGING THE DIPOLE CONTRIBUTION IS PURE z-TRANSPORT, NOT A SOURCE OR DISSIPATIVE PAYER / THE M19-436 TERMINAL q-COBOUNDARY IS THE z=0 LIMIT / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Finite-depth dipole sector

Let

\[
H_{dip}(z,q,\omega)
=
a(z,q)\cdot\omega
\]

with

\[
\boxed{
\mathfrak Da
=
(\partial_q-2z\partial_z)a
=
0
}
\]

as established in M19-435.

Then

\[
\boxed{
\mathfrak G_2H_{dip}
=
W_a
=
a-3(a\cdot\omega)\omega.
}
\]

## 2. First radial moment of the wedge velocity

Define

\[
\boxed{
M_F(z,q)
:=
\int_{S^2}
F_r(z,q,\omega)\,\omega,d\omega.
}
\]

Also define

\[
T_F
:=
\int_{S^2}F_T,d\omega,
\]

and

\[
N_F
:=
\int_{S^2}F,d\omega
=
M_F+T_F.
\]

## 3. Wedge incompressibility moment identity

M5-582 gives

\[
(\mathfrak D+1)F_r
+
\operatorname{div}_{S^2}F_T
=
0.
\]

Multiply by \(\omega\) and integrate.

Using

\[
\int
\omega\operatorname{div}_SF_T
=
-T_F,
\]

we obtain

\[
\mathfrak DM_F+M_F-T_F=0.
\]

Therefore

\[
\boxed{
T_F
=
\mathfrak DM_F+M_F,
}
\]

and

\[
\boxed{
N_F
=
\mathfrak DM_F+2M_F.
}
\]

## 4. Dipole contribution to the radial energy current

The pressure part of the normalized wedge radial energy current is

\[
H F_r.
\]

Hence the dipole contribution is

\[
\boxed{
\Gamma_{dip}(z,q)
:=
\int_{S^2}
H_{dip}F_r,d\omega
=
a\cdot M_F.
}
\]

Define its invariant q-average

\[
\boxed{
\mathscr J_{dip}(z)
:=
\langle\Gamma_{dip}(z,q)\rangle_q.
}
\]

## 5. Dipole pressure work in the wedge momentum equation

Pair the dipole pressure gradient with F:

\[
\begin{aligned}
W_{dip}(z,q)
&:=
\int_{S^2}
F\cdot\mathfrak G_2H_{dip}
,d\omega
\\
&=
\int
F\cdot
[a-3(a\cdot\omega)\omega]
,d\omega
\\
&=
a\cdot N_F
-
3a\cdot M_F.
\end{aligned}
\]

Insert

\[
N_F
=
\mathfrak DM_F+2M_F.
\]

Then

\[
\boxed{
W_{dip}
=
a\cdot
(\mathfrak DM_F-M_F).
}
\]

## 6. Exact q-z coboundary identity

Add the radial-flux contribution:

\[
\begin{aligned}
W_{dip}
+
\Gamma_{dip}
&=
a\cdot\mathfrak DM_F.
\end{aligned}
\]

Since

\[
\mathfrak Da=0,
\]

the product rule gives

\[
\boxed{
W_{dip}
+
\Gamma_{dip}
=
\mathfrak D
(a\cdot M_F).
}
\]

Thus the finite-depth harmonic dipole is again an exact derivative contribution.

At z=0,

\[
\mathfrak D\to\partial_q,
\]

and this becomes exactly M19-436.

## 7. q-average converts it to pure depth transport

Take the invariant q-mean at fixed z.

For any bounded recurrent observable X,

\[
\langle\partial_qX\rangle_q=0.
\]

Therefore

\[
\langle\mathfrak DX\rangle_q
=
-2z
\frac d{dz}
\langle X\rangle_q.
\]

Apply this to

\[
X=a\cdot M_F.
\]

Then

\[
\boxed{
\langle W_{dip}\rangle_q
+
\mathscr J_{dip}(z)
=
-2z
\mathscr J_{dip}'(z).
}
\]

Equivalently,

\[
\boxed{
\langle W_{dip}\rangle_q
=
-
\left[
2z\mathscr J_{dip}'(z)
+
\mathscr J_{dip}(z)
\right].
}
\]

This is exactly the pressure-work/radial-flux cancellation pattern required by the q-averaged wedge energy law.

## 8. Dipole does not create energy

The total wedge energy equation is

\[
\mathscr E'
+
2z\mathscr J'
+
\mathscr J
=
\mathscr D.
\]

The harmonic dipole contributes to \(\mathscr E'\) through pressure work and to \(\mathscr J\) through radial pressure transport.

Section 7 shows those two appearances cancel as an exact transport identity.

Therefore

\[
\boxed{
\text{harmonic pressure dipole}
\neq
\text{energy source}.
}
\]

It only redistributes energy in the q-z geometry.

## 9. No dissipative charge is attached to the dipole

The dipole sector contains no positive term analogous to

\[
\mathscr D
\]

or

\[
\mathscr P_\omega.
\]

Its contribution is signed and conservative.

Hence one must not charge a recurring dipole event as a new unsigned physical payer.

This would double-count transport as production.

## 10. Consequence for the finite-depth overlap firewall

M19-433--435 show that the dipole is invisible to vorticity.

M19-437 now shows that it is also source-free in the energy ledger.

Therefore the dipole can modify the **phase and radial location of energy transport** without generating either

- vorticity production;
- or positive energy dissipation.

This explains precisely how it can obstruct a naive energy-to-enstrophy overlap theorem.

## 11. Quotient interpretation

Define the dipole pressure current

\[
\mathscr J_{dip}.
\]

Then the physically productive part of the energy-current structure should be studied modulo this conservative current.

Schematically,

\[
\boxed{
\mathscr J
=
\mathscr J_{dip}
+
\mathscr J_{prod}.
}
\]

The dipole satisfies its own exact work-current identity.

Any contradiction must therefore involve

\[
\mathscr J_{prod},
\]

not merely the sign or variation of the total current.

## 12. Remaining dynamic degree

The coefficient \(a(s)\) remains a three-dimensional physical-time cocycle.

M19-437 does not force it to be constant in s or to vanish.

But its possible influence is now sharply limited:

\[
\boxed{
Z_{dip}^{3D-time}
=
\text{finite-dimensional conservative transport phase}.
}
\]

It is not an independent positive resource.

## 13. Next target

The next useful step is to compare the dipole cocycle with the whole-space pressure representation of the finite prelimit sequence.

A nonzero critical \(r^{-2}\) dipole in the blow-up limit cannot be produced by a uniformly tight compact Reynolds stress, whose pressure contribution is only \(r^{-3}\).

Thus one should compute the exact critical stress-tail growth needed to sustain

\[
a(s)\neq0.
\]

If that growth is merely the already unavoidable \(O(R)\) energy/stress growth of a \(1/r\) tail, the dipole remains a critical firewall.

If it requires an additional anisotropic moment beyond that baseline, a new rigidity gate may appear.

\[
\boxed{\text{M19-437 COMPLETE; THE FINITE-DEPTH HARMONIC PRESSURE DIPOLE IS PURE CONSERVATIVE q-z TRANSPORT.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
