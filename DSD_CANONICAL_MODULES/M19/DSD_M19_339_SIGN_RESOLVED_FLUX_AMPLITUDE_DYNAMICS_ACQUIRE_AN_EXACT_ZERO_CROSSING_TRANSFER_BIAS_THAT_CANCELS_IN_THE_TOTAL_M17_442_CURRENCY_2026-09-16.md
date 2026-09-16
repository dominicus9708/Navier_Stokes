# DSD M19-339 — Sign-resolved flux-amplitude dynamics acquire an exact zero-crossing transfer bias that cancels in the total M17-442 currency

Date: 2026-09-16  
Canonical ID: **M19-339**

Status: **ACTIVE SIGN-TRANSFER DYNAMICS / ZERO-CROSSING CURRENT / M17-442 + M17-459 BRIDGE FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Setup

Work on one coherent positive-orientation material-flux family in one fixed own-scale normalization.

Let

\[
q=r^2\rho\ge0
\]

be the normalized amplitude and let \(d\Phi\) be the positive material vorticity-flux measure.

Exact CE-H gives the material laws used in M17-442:

\[
\boxed{
D_tq=(\sigma+\nu\kappa)q,
}
\]

and

\[
\boxed{
\partial_t(d\Phi)=\nu\kappa\,d\Phi.
}
\]

Let

\[
\boxed{h:=D_t\kappa.}
\]

M17-339 gives, in physical variables,

\[
 h=L_\rho\kappa+L_\rho\sigma+\mathcal R_{\rm geom},
\]

but the present derivation initially uses only the material scalar velocity \(h\).

Assume the zero level is regular enough for the distributional differentiation of \(H(\pm\kappa)\) along material labels. Failure is recorded as critical-level/high-jet/interface loss.

## 2. Sign-resolved fluxes

Define

\[
\Phi_+
:=\int H(\kappa)\,d\Phi,
\qquad
\Phi_-
:=\int H(-\kappa)\,d\Phi.
\]

For regular crossings,

\[
D_tH(\kappa)=\delta(\kappa)h,
\qquad
D_tH(-\kappa)=-\delta(\kappa)h.
\]

Define the signed material zero-crossing flux current

\[
\boxed{
C_0^\Phi
:=
\int\delta(\kappa)h\,d\Phi.
}
\]

Then exact differentiation gives

\[
\boxed{
\dot\Phi_+
=
\nu\int_{\{\kappa>0\}}\kappa\,d\Phi
+
C_0^\Phi,
}
\]

and

\[
\boxed{
\dot\Phi_-
=
\nu\int_{\{\kappa<0\}}\kappa\,d\Phi
-
C_0^\Phi.
}
\]

The crossing current is internal exchange: it cancels exactly in the total flux equation,

\[
\boxed{
\dot\Phi_++\dot\Phi_-
=
\nu\int_{\{\kappa\ne0\}}\kappa\,d\Phi,
}
\]

up to any flux measure supported identically on \(\kappa=0\).

## 3. Sign-resolved quadratic currencies

Define

\[
Q_+
:=\int H(\kappa)q\,d\Phi,
\qquad
Q_-
:=\int H(-\kappa)q\,d\Phi.
\]

These are exactly

\[
Q_+=\Phi_+\mathfrak a_+,
\qquad
Q_-=\Phi_-\mathfrak a_-
\]

from M19-338.

Since

\[
D_t(q\,d\Phi)
=(\sigma+2\nu\kappa)q\,d\Phi,
\]

define the amplitude-weighted zero-crossing current

\[
\boxed{
C_0^Q
:=
\int\delta(\kappa)h\,q\,d\Phi.
}
\]

Then

\[
\boxed{
\dot Q_+
=
\int_{\{\kappa>0\}}
(\sigma+2\nu\kappa)q\,d\Phi
+
C_0^Q,
}
\]

and

\[
\boxed{
\dot Q_-
=
\int_{\{\kappa<0\}}
(\sigma+2\nu\kappa)q\,d\Phi
-
C_0^Q.
}
\]

Again the zero-crossing transfer cancels in the total quadratic currency \(Q_++Q_-\). This is why it is invisible in the total M17-442 equation.

## 4. Conditional sign probabilities

When \(\Phi_\pm>0\), define

\[
dp_\pm
:=
\frac{1_{S_\pm}d\Phi}{\Phi_\pm},
\]

and when \(Q_\pm>0\),

\[
d\widehat p_\pm
:=
\frac{1_{S_\pm}q\,d\Phi}{Q_\pm}.
\]

Then

\[
\frac{\dot\Phi_+}{\Phi_+}
=
\nu\langle\kappa\rangle_{p_+}
+
\frac{C_0^\Phi}{\Phi_+},
\]

\[
\frac{\dot Q_+}{Q_+}
=
\langle\sigma+2\nu\kappa\rangle_{\widehat p_+}
+
\frac{C_0^Q}{Q_+},
\]

with the analogous minus formulas carrying the opposite crossing sign.

## 5. Exact sign-resolved amplitude dynamics

Because

\[
\mathfrak a_+=Q_+/\Phi_+,
\]

we obtain

\[
\boxed{
\begin{aligned}
\frac d{dt}\log\mathfrak a_+
={}&
\langle\sigma+2\nu\kappa\rangle_{\widehat p_+}
-
\nu\langle\kappa\rangle_{p_+}\\
&+
\frac{C_0^Q}{Q_+}
-
\frac{C_0^\Phi}{\Phi_+}.
\end{aligned}
}
\]

Likewise

\[
\boxed{
\begin{aligned}
\frac d{dt}\log\mathfrak a_-
={}&
\langle\sigma+2\nu\kappa\rangle_{\widehat p_-}
-
\nu\langle\kappa\rangle_{p_-}\\
&-
\frac{C_0^Q}{Q_-}
+
\frac{C_0^\Phi}{\Phi_-}.
\end{aligned}
}
\]

Thus each sign-resolved collapse is paid by two conceptually distinct mechanisms:

1. within-sign strain/coefficient reweighting;
2. amplitude-biased transfer across \(\kappa=0\).

## 6. Crossing term is an amplitude-bias current

Since \(Q_+=\Phi_+\mathfrak a_+\),

\[
\frac{C_0^Q}{Q_+}
-
\frac{C_0^\Phi}{\Phi_+}
=
\frac{1}{\Phi_+\mathfrak a_+}
\int\delta(\kappa)h
\left(q-\mathfrak a_+\right)d\Phi.
\]

Therefore

\[
\boxed{
\mathcal C_+
:=
\frac{1}{\Phi_+\mathfrak a_+}
\int\delta(\kappa)h(q-\mathfrak a_+)d\Phi
}
\]

is the exact plus-sector crossing bias.

Similarly

\[
\boxed{
\mathcal C_-
:=
-
\frac{1}{\Phi_-\mathfrak a_-}
\int\delta(\kappa)h(q-\mathfrak a_-)d\Phi.
}
\]

A sign transfer that carries exactly the sector-average amplitude produces no direct change in that sector's mean amplitude. Only amplitude-biased sign transfer changes \(\mathfrak a_\pm\) beyond the within-sign dynamics.

## 7. Relation to M17-459 zero current

M17-459 defines the positive codimension-one coefficient-diffusion current

\[
J_0
=
\int\rho^2\delta(\kappa)|\nabla\kappa|^2dx
\ge0.
\]

The present quantities

\[
C_0^\Phi
=
\int\delta(\kappa)h\,d\Phi,
\qquad
C_0^Q
=
\int\delta(\kappa)h q\,d\Phi
\]

are **signed material-line sign-transfer currents**.

They are not identical to \(J_0\). M17-339 gives

\[
h=L_\rho\kappa+L_\rho\sigma+\mathcal R_{\rm geom},
\]

so any theorem connecting \(C_0^\Phi\) or \(C_0^Q\) to \(J_0\) must explicitly transport the weighted diffusion, strain-trace, geometry, line-coordinate, and coarea factors.

Permanent firewall:

\[
\boxed{
C_0^{\Phi,Q}
\ne
J_0
\quad\text{without an additional representation theorem.}
}
\]

## 8. Why the total M17-442 equation misses the sign-transfer mechanism

Adding the plus and minus flux equations cancels \(C_0^\Phi\).

Adding the plus and minus quadratic equations cancels \(C_0^Q\).

Hence the total flux-weighted amplitude \(\mathfrak a_\Phi\) can be analyzed by M17-442 without an explicit crossing term even though the individual sign amplitudes may exchange mass violently.

This yields a new anti-shortcut rule:

\[
\boxed{
\text{small total flux-amplitude drift}
\not\Rightarrow
\text{small sign-resolved transfer activity}.
}
\]

Large opposite sign transfers may cancel in the total currency.

## 9. Updated mixed-sign survivor

Combining M19-337--339,

\[
\boxed{
\begin{aligned}
H_{\rm productive\ mixed\text{-}sign\ survivor}
\Longrightarrow{}&
G_{\rm residence\ segregation}\\
&\lor G_{\rm sign\ flux\text{-}fraction\ thinning}\\
&\lor G_{\rm within\text{-}sign\ strain/coefficient\ reweighting}\\
&\lor G_{\rm amplitude\text{-}biased\ zero\text{-}crossing\ transfer}\\
&\lor G_{\rm zero\text{-}level/high\text{-}jet/representation\ loss}.
\end{aligned}
}
\]

The vague spatial mixed-sign branch is therefore converted into a small set of exact measure-current mechanisms.

## 10. Next target

The highest-value new bridge is now

\[
\boxed{
\mathcal T_{0}^{\Phi\leftrightarrow J}:
\text{compare the signed material sign-transfer current }
C_0^{\Phi,Q}
\text{ with the positive CE-H zero-current }J_0
}
\]

under the regular line-family / zero-tube compactness hypotheses.

If amplitude-biased sign transfer can be forced to pay a non-summable palinstrophy or raw-H2 amount, the mixed-sign branch would narrow further. If not, the result should identify the exact reversible transfer survivor.

## 11. Audit verdict

**PASS — sign-resolved amplitude collapse has an exact evolution law, and its new term is an amplitude-biased signed zero-crossing transfer current.**

This current cancels from the total M17-442 currency and is not automatically the positive M17-459 zero-current. Their comparison is the next theorem gate.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
