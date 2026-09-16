# DSD M19-353 — Uniform transverse log-Sobolev chart control closes all persistent sign-flux thinning by an explicit amplitude-quantile palinstrophy bound

Date: 2026-09-16  
Canonical ID: **M19-353**

Status: **ACTIVE CONDITIONAL THINNING CLOSURE / QUANTILE-CAPACITY THEOREM / TRANSVERSE LOG-SOBOLEV GATE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Why this module is needed

M19-351 conditionally closed fixed-power sign-flux thinning using an abstract logarithmic condenser inequality.

M19-352 showed that bounded global Poincare shape factor \(\Pi\) alone does not certify that small-phase bound.

The present module replaces the abstract condenser statement by a concrete, scale-invariant two-dimensional functional hypothesis on the transverse charts and derives the logarithmic estimate from amplitude quantile sets.

## 2. Uniform transverse log-Sobolev hypothesis

Let \(A=A_z\) be a represented normalized transverse cross-section.

Assume the compact transverse chart class satisfies, uniformly in the record and the section,

\[
\boxed{
\|f-\bar f_A\|_{L^q(A)}
\le
C_{LS}\sqrt q\,|A|^{1/q}
\|\nabla_\perp f\|_{L^2(A)},
\qquad q\ge2.
}
\]

This is scale-invariant in two dimensions.

A uniform bi-Lipschitz/Lipschitz image of one fixed shape-compact reference class would supply such a bound through the standard two-dimensional Moser--Trudinger/Sobolev-q mechanism. M19-353 does **not** claim that M17-449's bounded Poincare factor alone implies it.

Also retain the baseline-size compact alternative

\[
\boxed{|A_z|\le C_AR.}
\]

Failure is transverse-size decompactification.

Finally retain the normalized amplitude ceiling

\[
\boxed{0\le\rho\le M_\rho.}
\]

## 3. Logarithmic two-set average inequality

Let \(E,F\subset A\) have positive relative areas

\[
\delta_E:=|E|/|A|,
\qquad
\delta_F:=|F|/|A|.
\]

For any \(q\ge2\), Holder and Section 2 give

\[
\left|
\fint_E(f-\bar f_A)
\right|
\le
|E|^{-1/q}
\|f-\bar f_A\|_q
\le
C_{LS}\sqrt q\,\delta_E^{-1/q}
\|\nabla f\|_2.
\]

Choose

\[
q_E:=\max\{2,\log(e/\delta_E)\}.
\]

Then \(\delta_E^{-1/q_E}\le e\), hence

\[
\left|
\fint_E f-\bar f_A
\right|
\le
C
\sqrt{\log(e/\delta_E)}
\|\nabla f\|_2.
\]

The same holds for \(F\). Therefore

\[
\boxed{
\left|
\fint_E f-int_F f
\right|^2
\le
C
\left[
\log\frac{e}{\delta_E}
+
\log\frac{e}{\delta_F}
\right]
\int_A|\nabla f|^2dA.
}
\]

This is the exact logarithmic small-set estimate needed below.

## 4. Sign-specific flux-weighted amplitudes

At one good-time section, let \(S\) be the thinning coefficient-sign sector and \(C\) its complement.

Write

\[
\Phi_S=\eta\Phi,
\qquad
\Phi_C=(1-\eta)\Phi.
\]

For the thinning branch assume eventually

\[
0<\eta\le\eta_0<1/2.
\]

Define

\[
\boxed{
a_S(z)
:=
\frac1{\Phi_S}
\int_{A_z\cap S}\rho^2dA,
}
\]

and

\[
\boxed{
a_C(z)
:=
\frac1{\Phi_C}
\int_{A_z\cap C}\rho^2dA.
}
\]

These are flux-probability means of \(\rho\) on the two sectors.

The sign enstrophy floor gives

\[
E_S
=
\Phi_S\int_0^{\ell_R}a_S(z)dz
\ge e_*.
\]

Therefore

\[
\boxed{
\int_0^{\ell_R}a_S(z)dz
\ge
\frac{c}{\eta}.
}
\]

The complementary enstrophy and flux bounds give

\[
\boxed{
\int_0^{\ell_R}a_C(z)dz
\le C.
}
\]

Assume the compact parent-length alternative

\[
\boxed{\ell_R\le C_\ell R.}
\]

## 5. Select the strong-disparity sections

Choose a small fixed \(c_0>0\) and define

\[
D_R
:=
\left\{
 z:
 a_S(z)\ge8a_C(z),
\quad
 a_S(z)\ge\frac{c_0}{\eta R}
\right\}.
\]

The complement of the first condition contributes at most

\[
8\int a_Cdz\le C.
\]

The complement of the second contributes at most

\[
\frac{c_0}{\eta R}\ell_R
\le
\frac{C_\ell c_0}{\eta}.
\]

Choosing \(c_0\) sufficiently small and then taking \(\eta\) below a fixed threshold, Section 4 yields

\[
\boxed{
\int_{D_R}a_S(z)dz
\ge
\frac{c_1}{\eta}.
}
\]

By Cauchy--Schwarz and \(|D_R|\le\ell_R\le C_\ell R\),

\[
\boxed{
\int_{D_R}a_S(z)^2dz
\ge
\frac{c_2}{\eta^2R}.
}
\]

## 6. High-sign and low-complement amplitude quantile sets

Fix \(z\in D_R\).

Define the sign-sector flux probability

\[
dp_S:=\frac{\rho\,dA}{\Phi_S}.
\]

Since

\[
a_S=\mathbb E_{p_S}[\rho]
\]

and \(0\le\rho\le M_\rho\), the high set

\[
\boxed{
H_z
:=
\{x\in A_z\cap S:\rho(x)\ge a_S/2\}
}
\]

has

\[
p_S(H_z)
\ge
\frac{a_S}{2M_\rho}.
\]

Hence its flux and geometric area satisfy

\[
\int_{H_z}\rho dA
\ge
\frac{\Phi_Sa_S}{2M_\rho},
\]

\[
\boxed{
|H_z|
\ge
\frac{\Phi_Sa_S}{2M_\rho^2}.
}
\]

Because \(z\in D_R\),

\[
\Phi_Sa_S
\ge
\eta\Phi_-\frac{c_0}{\eta R}
\ge
\frac{c}{R}.
\]

Thus

\[
|H_z|\ge cR^{-1}.
\]

Using \(|A_z|\le C_AR\),

\[
\boxed{
\delta_H:=|H_z|/|A_z|
\ge cR^{-2}.
}
\]

Now define the complementary flux probability \(p_C\). Since

\[
a_C=\mathbb E_{p_C}[\rho],
\]

Markov gives

\[
p_C\{\rho>2a_C\}\le1/2.
\]

Therefore the low set

\[
\boxed{
L_z
:=
\{x\in A_z\cap C:\rho(x)\le2a_C\}
}
\]

carries at least half of \(\Phi_C\). Using \(a_C\le M_\rho\),

\[
|L_z|
\ge
\frac{\Phi_C}{4M_\rho}
\ge c>0.
\]

Hence

\[
\boxed{
\delta_L:=|L_z|/|A_z|
\ge cR^{-1}.
}
\]

Both relative areas are therefore only polynomially small.

## 7. Logarithmic transverse gradient cost

On \(H_z\),

\[
\rho\ge a_S/2.
\]

On \(L_z\), because \(z\in D_R\),

\[
\rho\le2a_C\le a_S/4.
\]

Thus

\[
\left|
\fint_{H_z}\rho
-
\fint_{L_z}\rho
\right|
\ge
\frac{a_S}{4}.
\]

Apply Section 3 with \(f=\rho\). Sections 6 gives

\[
\log(e/\delta_H)+\log(e/\delta_L)
\le
C\log R.
\]

Therefore

\[
\boxed{
\int_{A_z}|\nabla_\perp\rho|^2dA
\ge
\frac{c}{\log R}a_S(z)^2.
}
\]

Integrating over \(D_R\) and using Section 5,

\[
\boxed{
P_R^{snap}
\ge
\int|\nabla_\perp\rho|^2dx
\ge
\frac{c}{\eta^2R\log R}.
}
\]

Since \(|\nabla\rho|\le|\nabla\Omega|\), this is a genuine palinstrophy lower bound.

## 8. Parent-time ancestry consequence

Suppose the thinning state with flux fraction at most \(\eta_R\) and the Section 2 chart package holds on a fraction \(\gamma_R\) of the parent-time record window of size \(\asymp R^2\).

Then

\[
\int_{J_R}P_Rdt
\ge
c\gamma_RR^2
\frac1{\eta_R^2R\log R}
=
\frac{c\gamma_RR}{\eta_R^2\log R}.
\]

Apply the M17-307 ancestry weight \(R^{-1}\):

\[
\boxed{
\mathcal P_{anc,R}
\ge
\frac{c\gamma_R}{\eta_R^2\log R}.
}
\]

Therefore finite ancestry requires

\[
\boxed{
\sum_m
\frac{\gamma_{R_m}}
{\eta_{R_m}^2\log R_m}
<\infty.
}
\]

For geometric records, \(\log R_m\asymp m\).

If \(\gamma_{R_m}\ge\gamma_*>0\) and \(\eta_{R_m}\to0\), then

\[
\frac{1}{\eta_{R_m}^2\log R_m}
\ge
\frac{1}{\log R_m}
\asymp
\frac1m
\]

for all sufficiently large \(m\), and the series diverges.

Thus

\[
\boxed{
\text{persistent sign-flux thinning is impossible under the uniform transverse log-Sobolev chart package.}
}
\]

This closes **all** thinning rates, not only fixed powers.

## 9. Relation to M19-351

M19-351 assumed a relative condenser inequality abstractly.

M19-353 derives the needed logarithmic cost from three inspectable ingredients:

1. uniform scale-invariant transverse Sobolev-q/Moser--Trudinger control;
2. baseline transverse-size upper bound \(|A_z|\lesssim R\);
3. normalized amplitude ceiling.

Thus the geometry gate is sharpened to

\[
\boxed{
\mathcal T_{LS}^{trans}:
\text{uniform scale-normalized 2D log-Sobolev control on the represented transverse charts.}
}
\]

The M19-351 condenser theorem is recovered as a consequence of this stronger but standard functional chart property.

## 10. What remains OPEN

M17-449 bounded \(\Pi\) alone does not prove \(\mathcal T_{LS}^{trans}\).

The remaining alternatives are therefore

\[
\boxed{
\begin{aligned}
G_{\rm sign\text{-}flux\ thinning}
\Longrightarrow{}&
G_{\rm palinstrophy\ contradiction}\\
&\lor G_{\rm transverse\ log\text{-}Sobolev/chart\ degeneration}\\
&\lor G_{\rm transverse\ size\ excess}\;( |A|/R\to\infty )\\
&\lor G_{\rm super\text{-}parent\ line\ length/folding}\\
&\lor G_{\rm amplitude\ ceiling\ loss}\\
&\lor G_{\rm time\ occupancy\ thinning}\\
&\lor G_{\rm common\ section/genealogy/interface\ loss}.
\end{aligned}
}
\]

The next repository audit should determine whether the retained late-M17 tube/chart compactness already includes a uniform bi-Lipschitz or equivalent normalized Sobolev-chart bound. If yes, persistent sign-flux thinning is no longer an OPEN internal mechanism.

## 11. External-theorem firewall

The logarithmic \(q\)-growth in Section 2 is a standard two-dimensional Sobolev/Moser--Trudinger consequence on a uniformly shape-regular bounded reference class. It is not derived from the Navier--Stokes equation itself.

Therefore its use in the proof architecture requires explicit certification that every retained transverse section belongs, after scale normalization, to a uniform chart class on which the constant \(C_{LS}\) is record-independent.

## 12. Audit verdict

**PASS AS A CONDITIONAL ALL-RATE THINNING CLOSURE.**

The abstract small-phase capacity gate can be replaced by a concrete transverse log-Sobolev chart gate. Under that gate, any material-flux sign population carrying fixed enstrophy cannot thin persistently through the geometric record sequence: the palinstrophy ancestry cost is at least

\[
\boxed{
\mathcal P_{anc,R}
\gtrsim
\frac{\gamma_R}{\eta_R^2\log R}.
}
\]

The remaining question is no longer the scaling calculation; it is whether the late-M17 retained tube geometry certifies the uniform normalized two-dimensional chart inequality.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
