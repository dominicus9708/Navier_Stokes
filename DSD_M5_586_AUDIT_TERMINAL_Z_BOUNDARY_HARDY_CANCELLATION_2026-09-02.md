# DSD M5-586 — Audit: Terminal z-Boundary Hardy Cancellation

Date: 2026-09-02

Status: **POSITIVE TERMINAL VORTICITY DENSITY DOES NOT CREATE AN EXTRA z=0 ENSTROPHY-FLUX OBSTRUCTION. THE LEADING BOUNDARY TERMS CANCEL EXACTLY AND THE NEXT TERM IS JUST THE LOCAL WEDGE ODE. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Localized wedge enstrophy ledger

M5-585 gives, for \(0<z_1<z_2\),

\[
\frac12\int_{z_1}^{z_2}z^{1/2}
(\mathscr P_\omega-\mathscr Q_\omega)dz
=
\frac12[z^{1/2}\mathscr K_\omega]_{z_1}^{z_2}
+[z^{3/2}\mathscr J_\omega]_{z_1}^{z_2}
-
\frac14\int_{z_1}^{z_2}z^{-1/2}\mathscr K_\omega dz.
\]

The natural question was whether the positive terminal vorticity density from M5-571 forces a nonzero one-sign boundary charge as \(z_1\downarrow0\).

---

## 2. Terminal expansions

On the regular terminal-jet class,

\[
G(z,q,\omega)
=B_A(q,\omega)+zB_1(q,\omega)+O(z^2).
\]

Hence the q-averaged spherical enstrophy density has

\[
\boxed{
\mathscr K_\omega(z)
=K_0+K_1z+O(z^2),
}
\]

where

\[
K_0
=
\frac12
\left\langle
\int_{S^2}|B_A|^2d\omega
\right\rangle
>0
\]

on the hard ergodic component.

Likewise write

\[
\boxed{
\mathscr J_\omega(z)
=J_0+J_1z+O(z^2),
}
\]

and

\[
\boxed{
\mathscr P_\omega(z)-\mathscr Q_\omega(z)
=S_0+O(z).
}
\]

---

## 3. The apparent sqrt(epsilon) boundary charge

Set \(z_1=0\), \(z_2=\varepsilon\).

The first boundary term is

\[
\frac12\varepsilon^{1/2}\mathscr K_\omega(\varepsilon)
=
\frac12K_0\varepsilon^{1/2}
+O(\varepsilon^{3/2}).
\]

The weighted enstrophy term is

\[
-\frac14\int_0^\varepsilon
z^{-1/2}\mathscr K_\omega(z)dz
=
-\frac14
\left[
2K_0\varepsilon^{1/2}
+O(\varepsilon^{3/2})
\right].
\]

Therefore

\[
\boxed{
\frac12K_0\varepsilon^{1/2}
-
\frac12K_0\varepsilon^{1/2}
=0.
}
\]

The positive terminal vorticity density cancels exactly at leading order.

This is the same critical Hardy mechanism repeatedly encountered in the remote tail.

---

## 4. First nonzero order

Expand one order further:

\[
\frac12\varepsilon^{1/2}\mathscr K_\omega(\varepsilon)
-
\frac14\int_0^\varepsilon z^{-1/2}\mathscr K_\omega dz
=
\boxed{
\frac13K_1\varepsilon^{3/2}
+O(\varepsilon^{5/2}).
}
\]

The flux boundary contributes

\[
\boxed{
\varepsilon^{3/2}\mathscr J_\omega(\varepsilon)
=J_0\varepsilon^{3/2}+O(\varepsilon^{5/2}).
}
\]

The left side of the localized ledger is

\[
\frac12\int_0^\varepsilon z^{1/2}
(S_0+O(z))dz
=
\boxed{
\frac13S_0\varepsilon^{3/2}
+O(\varepsilon^{5/2}).
}
\]

Equating coefficients gives

\[
\boxed{
K_1+3J_0=S_0.
}
\]

Since

\[
S_0
=
\mathscr P_\omega(0)-\mathscr Q_\omega(0),
\]

this is exactly the \(z=0\) value of M5-585's differential equation:

\[
\boxed{
\mathscr K_\omega'(0)
+3\mathscr J_\omega(0)
=
\mathscr P_\omega(0)-\mathscr Q_\omega(0).
}
\]

Thus the first nonzero boundary asymptotic contains no independent extra condition.

---

## 5. Explicit terminal enstrophy flux

At \(z=0\), let

\[
K_A(q,\omega)=\frac12|B_A|^2.
\]

The radial wedge enstrophy flux is

\[
(\mathcal J_\omega)_r
=
K_AF_r-(\mathfrak D-4)K_A.
\]

At the terminal boundary,

\[
\mathfrak D=\partial_q,
\qquad
F=A,
\]

so

\[
\boxed{
(\mathcal J_\omega)_r(0,q,\omega)
=
K_AA_r
-\partial_qK_A
+4K_A.
}
\]

After q-averaging,

\[
\boxed{
J_0
=
\left\langle
\int_{S^2}(K_AA_r+4K_A)d\omega
\right\rangle,
}
\]

because the total q derivative averages to zero.

The \(4K_A\) term is positive, but the advective contribution \(K_AA_r\) has no fixed sign under the current Type-I bounds. Therefore even the terminal enstrophy-flux coefficient is not known to be one-sign.

---

## 6. DSD anti-proof conclusion

The implication

\[
c_\omega>0
\Longrightarrow
\text{nonzero one-sign z=0 enstrophy defect}
\]

is false.

Critical homogeneity produces an exact cancellation between:

- the endpoint enstrophy term;
- the integrated weighted enstrophy term.

The remaining \(O(\varepsilon^{3/2})\) coefficient is already encoded in the local wedge ODE.

Thus the terminal boundary contains no additional hidden contradiction at this order.

---

## 7. Updated localization target

Since both the full \(z\)-integral and the infinitesimal \(z\downarrow0\) limit close exactly, any new enstrophy rigidity must arise at **finite nonzero wedge depth**:

\[
\boxed{
z\sim O(1)}
\]

or on an intermediate interval

\[
\boxed{0<z_1<z_2<\infty.}
\]

This is precisely the region connecting the terminal critical tail to the Type-I recurrent core.

The next efficient step is to identify a scale-invariant depth \(z_*\) or interval on which the positive similarity production \(\langle Q\rangle>0\) and the terminal positive densities force a nontrivial flux crossing. That crossing can then be compared with the earlier material-lineage/dual-flux constraints.

Status: **THE z=0 ENSTROPHY BOUNDARY HAS BEEN AUDITED AND DOES NOT CLOSE THE PROOF. THE REMAINING LEVER IS FINITE-DEPTH TRANSPORT BETWEEN TERMINAL TAIL AND RECURRENT CORE. GLOBAL REGULARITY REMAINS UNPROVED.**