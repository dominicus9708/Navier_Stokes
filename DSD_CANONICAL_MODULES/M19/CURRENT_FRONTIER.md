# M19 Current Frontier

**Date:** 2026-09-14  
**Current tip:** **M19-256**  
**Status:** ACTIVE CALCULATION / WHOLE-SPACE TRANSPARENT MOVING-SPHERE + GALILEAN WEIGHTED-PAYER FRONTIER / TRANSFER-COHERENCE + LOW-FREQUENCY + PRESSURE GATES OPEN / APERIODIC SIGNED FRONTIER OPEN / FINAL ROOT-PROOF CERTIFICATION OPEN

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Canonical policy

M18 remains the frozen audit/reduction family. M19 is the active calculation/closure family. Detailed derivations remain in numbered modules; this file records current theorem obligations and scope firewalls.

## 2. Global proof tree remains open

`ROOT-CERT` is unfinished. Historical non-CE-H roots

\[
CP\!-\!E,\quad CP\!-\!S,\quad CE\!-\!T,\quad Migration
\]

remain unresolved, together with parent-to-late-branch alignment/nonreuse and final beginning-to-end independent audit.

The aperiodic recurrent-hard branch still has

\[
\boxed{\mathcal T_{aper}^{signed}}
\]

OPEN.

## 3. Historical cavity branch is auxiliary — M19-211--252

M19-211--252 remain valid inside their stated no-slip cavity hypotheses. M19-253 permanently corrected their whole-space interpretation:

\[
\boxed{\text{no-slip cavity exclusion}\not\Rightarrow\text{whole-space transparent-sphere exclusion}.}
\]

Wall shear, the \(\nu/R\) no-slip layer, wall impedance, and frozen no-slip determinants are auxiliary diagnostics, not direct Clay-(A) closure conditions.

## 4. M19-253 — transparent moving observation sphere

The active geometric object is

\[
\Omega_R(t)=B_R(X(t))\subset\mathbb R^3,
\qquad S_R(t)=\partial B_R(X(t)),
\]

with no material wall condition. For \(e=|u|^2/2\),

\[
\frac d{dt}\int_{\Omega_R(t)}e
+\nu\int_{\Omega_R(t)}|\nabla u|^2
=
-\int_{S_R(t)}
\left[e(u-\dot X)\cdot n+p\,u\cdot n-\nu\partial_ne\right]dS.
\]

At singular scales the preferred primitive is a smooth moving cutoff or constant-velocity Galilean parabolic cylinder.

For

\[
Q_r^V(z_0)=\{t_0-r^2<t<t_0,\ |x-x_0-V(t-t_0)|<r\},
\]

standard one-scale epsilon regularity and exact Galilean covariance give

\[
\boxed{
z_0\text{ singular}
\Longrightarrow
\forall V,\ \forall r\ll1,
\quad C_V(r)+D_V(r)\ge\varepsilon_*.
}
\]

This is a reformulation of standard epsilon regularity, not a new epsilon theorem.

## 5. M19-254 — logarithmically divergent critical payer

Finite energy yields

\[
u\in L_t^\infty L_x^2\cap L_t^2\dot H_x^1,
\qquad
u\in L_{x,t}^{10/3},
\qquad
p\in L_{x,t}^{5/3}.
\]

The singularity floor implies

\[
F_V(r)=\int_{Q_r^V}(|u-V|^{10/3}+|p|^{5/3})
\ge c\varepsilon_*^{10/9}r^{5/3}.
\]

Unweighted costs remain geometrically summable, so this alone is not a contradiction. But with

\[
\rho_V(x,t)=\max(|x-x_0-V(t-t_0)|,\sqrt{t_0-t}),
\]

Tonelli gives the necessary singularity payer

\[
\boxed{
\mathcal P_{GMS}^{log}(V)
:=
\int_{Q_{r_0}^V(z_0)}
\frac{|u-V|^{10/3}+|p|^{5/3}}{\rho_V^{5/3}}\,dxdt
=\infty
}
\]

for every fixed constant \(V\).

## 6. M19-255 — frequency split of the GMS payer

At scale \(r\), write

\[
u=u_{\le r^{-1}}+u_{>r^{-1}}.
\]

The high-frequency sector satisfies

\[
\boxed{
\|u_{>r^{-1}}\|_{10/3}^{10/3}
\lesssim
r^2\|u\|_2^{4/3}\|\nabla\omega\|_2^2.
}
\]

Hence

\[
\boxed{
r^{-5/3}\int_{I_r}\|u_{>r^{-1}}\|_{10/3}^{10/3}dt
\lesssim
B_{-1}^{2/3}r^{1/3}\int_{I_r}\|\nabla\omega\|_2^2dt.
}
\]

A correctly transferred M17 palinstrophy ancestry ledger is therefore sufficient for high-frequency GMS summability.

The low-frequency sector does not close from energy alone:

\[
\|u_{\le r^{-1}}\|_{10/3}\lesssim r^{-3/5}\|u\|_2.
\]

A fixed Galilean velocity removes only one constant drift, not the general low-frequency tail.

Pressure is potentially reducible through weighted Calderón--Zygmund theory, but uniform parabolic truncation/localization and nonlocal far-field pressure remain to be certified.

Thus

\[
\boxed{
\mathcal T_{GMS}^{weight}
\Leftarrow
\mathcal T_{GMS}^{transfer}
+\mathcal T_{GMS}^{low}
+\mathcal T_{GMS}^{press}.
}
\]

## 7. M19-256 — exact ancestry scaling match

For

\[
\omega^{(r)}(y,s)=r^2\omega(x_0+ry,t_0+r^2s),
\]

one has exactly

\[
\boxed{
\int_{Q_r}|D_x^k\omega|^2dxdt
=
r^{1-2k}
\int_{Q_1}|\nabla_y^k\omega^{(r)}|^2dyds.
}
\]

Therefore the M17 ancestry factors

\[
r^{1-2k}
\]

are exactly the physical parabolic derivative weights: \(r^{-1}\) for \(k=1\), \(r^{-3}\) for \(k=2\), and \(r^{-5}\) for \(k=3\).

There is no exponent mismatch. The remaining transfer problem is geometric/genealogical.

For an M17 record center \(X_m(t)\), define

\[
\Theta_m(V)=r_m^{-1}\sup_{t\in I_m}
|X_m(t)-x_0-V(t-t_0)|.
\]

If for one fixed \(V\), \(\sup_m\Theta_m(V)<\infty\), the time windows satisfy \(|I_m|\asymp r_m^2\), the spatial domains are uniformly comparable, bounded overlap holds, and the same physical genealogy persists, then the M17 derivative ledgers transfer to the GMS family and the high-frequency GMS velocity payer is finite.

Failure of fixed-frame center coherence defines

\[
\boxed{
\mathcal E_{track}:
\forall V,\quad \limsup_{m\to\infty}\Theta_m(V)=\infty.
}
\]

The remaining transfer gate is

\[
\boxed{
\mathcal T_{GMS}^{coh}:
\text{fixed-}V\text{ centerline coherence}
+\text{domain comparability}
+\text{bounded-overlap genealogy alignment}.
}
\]

Failure splits into

\[
\boxed{
\mathcal E_{track}
\lor\mathcal E_{domain}
\lor\mathcal E_{overlap}
\lor\mathcal E_{genealogy}.
}
\]

## 8. Permanent firewalls through M19-256

\[
\boxed{\text{unweighted finite spacetime integrability}\not\Rightarrow\text{finite critical weighted GMS payer}},
\]
\[
\boxed{\text{high-frequency derivative control}\not\Rightarrow\text{low-frequency GMS tightness}},
\]
\[
\boxed{\text{M17 derivative strength}\not\Rightarrow\text{GMS transfer without center/domain/genealogy coherence}},
\]
\[
\boxed{\text{exact ancestry scaling match}\not\Rightarrow\text{physical transfer}},
\]
\[
\boxed{\text{scale-wise selectable }V_m\not\Rightarrow\text{one fixed }V\text{ controlling }\mathcal P_{GMS}^{log}},
\]
\[
\boxed{|x-a|^{-5/3}\in A_{5/3}\not\Rightarrow\text{localized moving-pressure closure without uniform weighted-CZ audit}}.
\]

## 9. Live theorem complex and next target

Whole-space moving-observation branch:

\[
\boxed{
\mathcal T_{GMS}^{coh},\quad
\mathcal T_{GMS}^{low},\quad
\mathcal T_{GMS}^{press}
}
\]

OPEN, with high-frequency velocity conditionally closed once \(\mathcal T_{GMS}^{coh}\) is established.

The next calculation is to test whether \(\mathcal E_{track}\) can be reduced to the existing low-frequency currency \(B_{-1}\), or whether a single fixed Galilean velocity can be extracted from the record-center genealogy. In parallel, audit whether uniform weighted Calderón--Zygmund estimates remove \(\mathcal T_{GMS}^{press}\) as an independent gate.

Aperiodic \(\mathcal T_{aper}^{signed}\), non-CE-H roots, `ROOT-CERT`, and the final independent audit remain OPEN. Global regularity remains unproved.
