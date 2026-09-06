# DSD M17-300 — Fixed-lag Logarithmic Ancestor Gate extracts a true spectral band or spectral leakage/recharge

Date: 2026-09-06  
Canonical ID: **M17-300**

Status: **FIXED-RESCALED-LAG SPECTRAL ANCESTOR GATE / M17-299 PRODUCES A SHELL-RELEVANT SCALE-COMPARABLE PACKET WITH POLYNOMIAL-IN-R RMS AMPLITUDE, BUT `H2/L2` ALONE DOES NOT JUSTIFY BACKWARD SINGLE-MODE AMPLIFICATION. ON THE PAYER-FREE COMPACT/NO-SUBSCALE CORRIDOR, M17-272 GIVES UNIFORM HIGHER REGULARITY. AFTER MULTIPLYING BY A FIXED BUFFER CUTOFF THAT IS ONE ON THE RAW LAPLACIAN CORE, A UNIFORM H3 BOUND CONTROLS THE HIGH-FOURIER TAIL, WHILE THE RETAINED NONZERO LAPLACIAN CHARGE AND A SMALL LOW-FREQUENCY CUTOFF FORCE A FIXED FREQUENCY ANNULUS TO CARRY A POSITIVE BAND MASS. THE LOCALIZED EQUATION IS HEAT PLUS EXPLICIT COEFFICIENT AND CUTOFF/INTERFACE FORCING. DUHAMEL ON THE FIXED BAND SHOWS: FOR EVERY FIXED RESCALED LAG T, EITHER THE PROJECTED FORCING PAYS A FIXED FRACTION OF THE PRESENT BAND, OR THE ANCESTOR BAND NORM IS AT LEAST `c exp(lambda_-^2 T)`. THIS IS THE FIRST RIGOROUS LOGARITHMIC ANCESTOR GATE; IT DOES NOT YET PASS TO T=T_j->infinity. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Localized scale-comparable packet

Let `V_j(z,tau)` be the own-scale normalized packet on a fixed rescaled cylinder.

Choose nested fixed balls

\[
B_{core}\Subset B_{mid}\Subset B_{out}
\]

and a smooth cutoff

\[
\chi\in C_c^\infty(B_{out}),
\qquad
\chi\equiv1\text{ on }B_{mid}.
\]

Set

\[
\boxed{f_j:=\chi V_j.}
\]

The raw Laplacian core lies inside the plateau of `chi`, so the time-zero retained charge gives

\[
\boxed{
\|\Delta f_j(0)\|_2^2\ge h_0>0
}
\]

after choosing the packet/cutoff geometry with the fixed raw-core margin.

The packet normalization gives

\[
\boxed{\|f_j(0)\|_2\le C_0.}
\]

On the no-higher-subscale compact branch, M17-272 plus interior bootstrapping gives

\[
\boxed{\|f_j(0)\|_{H^3}\le C_3.}
\]

---

## 2. Low and high Fourier tails cannot carry all Laplacian charge

Let

\[
\widehat f_j(\xi)
\]

be the Fourier transform of the compactly supported localized packet.

For low frequencies,

\[
\int_{|\xi|<\lambda_-}|\xi|^4|\widehat f_j|^2d\xi
\le
\lambda_-^4\|f_j\|_2^2.
\]

Choose fixed `lambda_->0` sufficiently small that

\[
\boxed{
\lambda_-^4 C_0^2\le h_0/4.
}
\]

For high frequencies, the H3 bound gives

\[
\int_{|\xi|>\lambda_+}|\xi|^4|\widehat f_j|^2d\xi
\le
\lambda_+^{-2}
\int|\xi|^6|\widehat f_j|^2d\xi
\le
C_3^2\lambda_+^{-2}.
\]

Choose fixed `lambda_+` sufficiently large that

\[
\boxed{C_3^2\lambda_+^{-2}\le h_0/4.}
\]

Therefore the fixed annulus

\[
\boxed{\mathcal B:=\{\lambda_-\le|\xi|\le\lambda_+\}}
\]

carries

\[
\boxed{
\int_{\mathcal B}|\xi|^4|\widehat f_j(\xi,0)|^2d\xi
\ge h_0/2.
}
\]

Since `|xi|<=lambda_+` on the band,

\[
\boxed{
\|P_{\mathcal B}f_j(0)\|_2
\ge c_B>0.
}
\]

This is a true fixed Fourier-band witness, not merely an H2/L2 ratio.

---

## 3. Localized evolution and leakage forcing

Write the packet-scale equation as

\[
\partial_\tau V_j-\Delta V_j
=\mathcal N_j,
\]

where `N_j` contains the scaled drift, strain/reaction, and any explicitly retained non-heat terms.

Then

\[
\partial_\tau f_j-\Delta f_j
=F_j,
\]

with

\[
\boxed{
F_j
=\chi\mathcal N_j
-2\nabla\chi\cdot\nabla V_j
-(\Delta\chi)V_j.
}
\]

The last two terms are supported in the fixed transition annulus of the packet cutoff.

Thus `F_j` exactly separates:

1. scaled ambient/coefficient forcing;
2. cutoff/interface leakage;
3. any non-heat recharge retained in `N_j`.

No cutoff term is silently dropped.

---

## 4. Duhamel on the fixed band

For a fixed rescaled lag `T>0`,

\[
P_{\mathcal B}f_j(0)
=
e^{T\Delta}P_{\mathcal B}f_j(-T)
+
\int_{-T}^{0}
e^{-s\Delta}P_{\mathcal B}F_j(s)ds.
\]

On the band,

\[
\|e^{T\Delta}P_{\mathcal B}g\|_2
\le
e^{-\lambda_-^2T}
\|P_{\mathcal B}g\|_2.
\]

Also

\[
\left\|
\int_{-T}^{0}
e^{-s\Delta}P_{\mathcal B}F_j(s)ds
\right\|_2
\le
\int_{-T}^{0}
 e^{-\lambda_-^2(-s)}
\|P_{\mathcal B}F_j(s)\|_2ds.
\]

Define the band recharge/leakage action

\[
\boxed{
\mathfrak L_j(T)
:=
\int_{-T}^{0}
 e^{-\lambda_-^2(-s)}
\|P_{\mathcal B}F_j(s)\|_2ds.
}
\]

---

## 5. Fixed-lag dichotomy

The present band mass satisfies

\[
\|P_{\mathcal B}f_j(0)\|_2\ge c_B.
\]

Therefore either

\[
\boxed{
\mathfrak L_j(T)\ge c_B/2,
}
\]

which is a fixed band recharge/interface payment, or

\[
\frac{c_B}{2}
\le
e^{-\lambda_-^2T}
\|P_{\mathcal B}f_j(-T)\|_2.
\]

Thus

\[
\boxed{
\|P_{\mathcal B}f_j(-T)\|_2
\ge
\frac{c_B}{2}e^{\lambda_-^2T}.
}
\]

Hence

\[
\boxed{
H_{present\ scale\text{-}comparable\ spectral\ packet}
\Longrightarrow
H_{fixed\text{-}lag\ spectral\ leakage/recharge}
\lor
H_{exponentially\ larger\ ancestor\ band}.
}
\]

---

## 6. Physical-scale translation

The rescaled band frequencies `lambda_-,lambda_+` correspond to physical similarity frequencies

\[
\asymp r_j^{-1}.
\]

A rescaled lag `T` corresponds to similarity time

\[
\Delta\theta=T r_j^2.
\]

Thus the ancestor factor is

\[
\boxed{
e^{\lambda_-^2T}
=e^{c\Delta\theta/r_j^2}.}
\]

This is the rigorous version of the expected heat-frequency backward amplification, but only after a true band has been extracted and only modulo the explicit leakage/recharge action.

---

## 7. Why this does not yet close M17-299

For every **fixed** `T`, M17-254/255 can support the required corridor after payer splitting.

To compare the ancestor band with the parent absolute-amplitude ceiling when the present packet amplitude is only `R^-2 polylog^-1`, one needs a lag of size

\[
T_j\asymp\log R_j
\]

in root rescaled time, or equivalently a physical similarity lag

\[
\boxed{
\Delta\theta_j\asymp r_j^2\log R_j.
}
\]

This lag may be bounded or may diverge depending on the logarithmic carrier scale.

Fixed-T compactness does not automatically justify this growing-lag passage.

The next gate must audit exactly this quantity.

---

## 8. DSD audit

- A true Fourier band is extracted before any heat amplification argument.
- The high-frequency tail is controlled only on the no-subscale/higher-regularity branch.
- The cutoff/interface commutator is included explicitly in `F_j`.
- The theorem is fixed-rescaled-lag; no `T_j->infinity` limit is silently taken.
- Band leakage/recharge is a real branch, not called an error term without budget.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
