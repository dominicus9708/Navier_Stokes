# DSD M17-072 — Tilt-compensation strength shares the stretch strain multiplier and reduces to a strain-free gradient ratio

Date: 2026-09-04
Canonical ID: **M17-072**

Status: **INTERNAL TILT COMPENSATION PERSISTENCE GATE / M17-071 SHOWS THAT A TILTED ORTHOGONAL-STRETCH MAXIMUM BECOMES SUB-RICCATI ALONG ITS TRUE SURFACE TANGENT ONLY IF `A D_xi q < -C^2`, WHERE `A=D_n g`, `C=D_xi g<0`, AND `g=D_xi log rho`. DEFINE THE POSITIVE COMPENSATION STRENGTH `R_comp := -A L/C^2`, `L:=D_xi q`, SO SURVIVAL REQUIRES `R_comp>1`. USING THE CORRECTED M17-049 STRAIN-SHEAR NOTATION `beta_Sigma=n·Sigma k`, THE EXACT CRITICAL-POINT LAWS ARE `D_B A=(sigma_k-1)A+S_A`, `D_B C=-2(sigma+1/2)C+S_C`, AND A NEW AUDITED LAW `D_B L=-2(sigma+1/2)L+S_L`, WITH `S_A=D_nD_xi(sigma+kappa)-2 beta_Sigma D_k g`, `S_C=D_xi^2(sigma+kappa)`, AND `S_L=-q D_xi sigma-(beta_Sigma+r_W)(q/r)C`. THE HOMOGENEOUS MULTIPLIERS CANCEL TO `D_B log R_comp=(sigma-sigma_n)+F_comp`. THIS IS EXACTLY THE SAME MULTIPLICATIVE STRAIN CHANNEL AS THE ORTHOGONAL STRETCH RATIO AND THE TILT ITSELF. MOREOVER `R_comp=|Theta| Lambda` ON THE COMPENSATED SIGN CLASS, WHERE `Lambda:=|D_xi q/D_xi g|` HAS A STRAIN-FREE MATERIAL LAW. THUS A RECURRENT COMPENSATED MAXIMUM MUST MAINTAIN `R_comp>1` ENTIRELY THROUGH EXPLICIT CRITICAL-JET RECHARGE AFTER COMMON STRAIN DRIFT IS FACTORED OUT. NO SIGN CONTRADICTION FOLLOWS YET; THE SURVIVOR IS REDUCED TO A FINITE SOURCE LEDGER / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Compensated tilted maximum class

Use the M17-071 regular maximum notation

\[
\boxed{
g:=D_\xi\log\rho,}
\]

\[
\boxed{g=0,
\qquad
C:=D_\xi g<0,}
\]

and

\[
\boxed{A:=D_ng.}
\]

Let

\[
\boxed{L:=D_\xi q.}
\]

M17-071 proves that sub-Riccati tangent compensation requires

\[
\boxed{A L<-C^2.}
\]

Hence on the retained compensated class,

\[
A\neq0,
\qquad
L\neq0,
\qquad
C\neq0.
\]

Define

\[
\boxed{
\mathcal R_{comp}
:=-\frac{AL}{C^2}>1.
}
\]

---

## 2. Corrected material law for A

M17-049, after the symbol-collision audit, gives

\[
\boxed{
D_BA
=(\sigma_k-1)A+\mathcal S_A,
}
\]

with

\[
\boxed{
\mathcal S_A
:=D_nD_\xi(\sigma+\kappa)
-2\beta_\Sigma D_kg,
}
\]

where

\[
\boxed{
\beta_\Sigma:=n\cdot\Sigma k
}
\]

is the transverse **strain shear**.

No frame-connection coefficient is substituted for `beta_Sigma`.

---

## 3. Material law for C

M17-049 also gives

\[
\boxed{
D_BC
=-2\left(\sigma+\frac12\right)C
+\mathcal S_C,
}
\]

where

\[
\boxed{
\mathcal S_C
:=D_\xi^2(\sigma+\kappa).
}
\]

Thus `C` has homogeneous multiplier

\[
-2\sigma-1.
\]

---

## 4. Derive the material law for q without differentiating cross alignment off the critical set

At a general nearby point of the orthogonal pure-kernel branch write

\[
\boxed{
b=(\xi\cdot\nabla)\xi=p\,k+q\,n.}
\]

M17-033 gives the exact vector law

\[
\boxed{
D_Bb
=-\left(\sigma+\frac12\right)b.
}
\]

The transverse material frame rotates by

\[
\boxed{
D_Bk=\omega_m n,
\qquad
D_Bn=-\omega_m k,
}
\]

with

\[
\boxed{
\omega_m:=\beta_\Sigma+r_W.
}
\]

Differentiate

\[
b=pk+qn.
\]

Matching `k,n` components gives the general scalar laws

\[
\boxed{
D_Bp
=-\left(\sigma+\frac12\right)p
+q\omega_m,
}
\]

\[
\boxed{
D_Bq
=-\left(\sigma+\frac12\right)q
-p\omega_m.
}
\]

These are valid before imposing the critical cross alignment.

---

## 5. Compute D_B L at the critical point

For any scalar `f`, because `D_B xi=0` and

\[
(\xi\cdot\nabla)B
=\left(\sigma+\frac12\right)\xi,
\]

we have

\[
\boxed{
D_B(D_\xi f)
=D_\xi(D_Bf)
-\left(\sigma+\frac12\right)D_\xi f.
}
\]

Apply this to `q`:

\[
D_BL
=D_\xi(D_Bq)
-\left(\sigma+\frac12\right)L.
\]

Use the general `D_Bq` law from Section 4:

\[
\begin{aligned}
D_BL
={}&-qD_\xi\sigma
-2\left(\sigma+\frac12\right)L\\
&-\omega_mD_\xi p
-pD_\xi\omega_m.
\end{aligned}
\]

Only now impose the critical conditions.
M17-047 gives at `g=0`

\[
p=0
\]

and from the general orthogonality relation

\[
p=\frac{gq}{r}
\]

we obtain

\[
\boxed{
D_\xi p
=\frac qr C.
}
\]

Therefore

\[
\boxed{
D_BL
=-2\left(\sigma+\frac12\right)L
+\mathcal S_L,
}
\]

with

\[
\boxed{
\mathcal S_L
:=-qD_\xi\sigma
-\omega_m\frac qr C.
}
\]

Equivalently,

\[
\boxed{
\mathcal S_L
=-qD_\xi\sigma
-(\beta_\Sigma+r_W)\frac qr C.
}
\]

This derivation avoids differentiating the cross-aligned relation `p=0` as though it held in a neighborhood.

---

## 6. Exact material law for the compensation strength

Since

\[
\mathcal R_{comp}
=-\frac{AL}{C^2}>0,
\]

we have

\[
D_B\log\mathcal R_{comp}
=
\frac{D_BA}{A}
+
\frac{D_BL}{L}
-2\frac{D_BC}{C}.
\]

Insert Sections 2--5.
The homogeneous part is

\[
(\sigma_k-1)
+(-2\sigma-1)
-2(-2\sigma-1).
\]

This simplifies to

\[
\sigma_k+2\sigma.
\]

Using

\[
\sigma+\sigma_k+\sigma_n=0,
\]

we obtain

\[
\boxed{
\sigma_k+2\sigma
=\sigma-\sigma_n.
}
\]

Therefore

\[
\boxed{
D_B\log\mathcal R_{comp}
=(\sigma-\sigma_n)
+\mathcal F_{comp},
}
\]

where

\[
\boxed{
\mathcal F_{comp}
:=
\frac{\mathcal S_A}{A}
+
\frac{\mathcal S_L}{L}
-2\frac{\mathcal S_C}{C}.
}
\]

This is the central TCPG law.

---

## 7. Expanded compensation-source ledger

Substituting the source definitions gives

\[
\boxed{
\begin{aligned}
\mathcal F_{comp}
={}&
\frac{D_nD_\xi(\sigma+\kappa)-2\beta_\Sigma D_kg}{A}\\
&+\frac{-qD_\xi\sigma-(\beta_\Sigma+r_W)(q/r)C}{L}\\
&-2\frac{D_\xi^2(\sigma+\kappa)}{C}.
\end{aligned}
}
\]

Thus the independent recharge channels are finite and explicit:

1. mixed `n-xi` curvature of `sigma+kappa`;
2. strain-shear coupling to `D_k g`;
3. vortex-direction strain gradient;
4. material transverse frame rotation acting through the off-critical `p` slope;
5. second vortex-direction curvature of `sigma+kappa`.

No universal sign is visible.

---

## 8. Same multiplicative drift as stretch anisotropy

M17-037 gives the orthogonal stretch ratio

\[
\boxed{
\mathcal R_s:=\frac{|a|}{|b|}
}
\]

with

\[
\boxed{
D_B\log\mathcal R_s
=\sigma-\sigma_n.
}
\]

Therefore

\[
\boxed{
D_B\log
\left(
\frac{\mathcal R_{comp}}{\mathcal R_s}
\right)
=\mathcal F_{comp}.
}
\]

The common strain drift cancels exactly.

Hence the compensation strength is not a third independent strain-amplified scalar.
Its independent dynamics is entirely in the explicit critical-jet source ledger `F_comp`.

---

## 9. Factor compensation into tilt and a strain-free gradient ratio

M17-049 defines

\[
|\Theta|=\frac{|A|}{|C|}.
\]

On the compensated sign class `AL<0`,

\[
\mathcal R_{comp}
=\frac{|A||L|}{C^2}.
\]

Define

\[
\boxed{
\Lambda
:=\left|\frac{L}{C}\right|
=\left|\frac{D_\xi q}{D_\xi g}\right|.
}
\]

Then

\[
\boxed{
\mathcal R_{comp}
=|\Theta|\Lambda.
}
\]

The sub-Riccati survival condition becomes

\[
\boxed{
|\Theta|\Lambda>1
}
\]

plus the opposing-sign condition

\[
\boxed{AL<0.}
\]

---

## 10. Lambda has no homogeneous strain multiplier

Because `L` and `C` have the same homogeneous multiplier

\[
-2\left(\sigma+\frac12\right),
\]

their ratio cancels it exactly:

\[
\boxed{
D_B\log\Lambda
=
\frac{\mathcal S_L}{L}
-
\frac{\mathcal S_C}{C}.
}
\]

Thus

\[
\boxed{
\Lambda
=\left|\frac{D_\xi q}{D_\xi^2\log\rho}\right|
}
\]

is a **strain-free critical gradient-ratio descriptor**.

This is the cleanest independent quantity exposed by TCPG.

---

## 11. Relation to the tilt forcing of M17-049

M17-049 has

\[
D_B\log|\Theta|
=(\sigma-\sigma_n)+\mathcal F_{crit}^{(2)},
\]

where

\[
\boxed{
\mathcal F_{crit}^{(2)}
=
\frac{\mathcal S_A}{A}
-
\frac{\mathcal S_C}{C}.
}
\]

Therefore

\[
\begin{aligned}
\mathcal F_{comp}-\mathcal F_{crit}^{(2)}
&=
\frac{\mathcal S_L}{L}
-
\frac{\mathcal S_C}{C}\\
&=D_B\log\Lambda.
\end{aligned}
\]

This exactly matches

\[
\mathcal R_{comp}=|\Theta|\Lambda.
\]

The consistency is an internal cross-audit of the calculation.

---

## 12. Moving-maximum derivative

The line maximum moves relative to material labels with M17-040 speed

\[
\boxed{
 v_{rel}
=-\frac{D_\xi(\sigma+\kappa)}{C}.
}
\]

Define

\[
D_{max}:=D_B+v_{rel}D_\xi.
\]

Then

\[
\boxed{
D_{max}\log\mathcal R_{comp}
=(\sigma-\sigma_n)+\mathcal F_{comp}
+v_{rel}D_\xi\log\mathcal R_{comp}.
}
\]

Likewise

\[
\boxed{
D_{max}\log\Lambda
=
\frac{\mathcal S_L}{L}
-
\frac{\mathcal S_C}{C}
+v_{rel}D_\xi\log\Lambda.
}
\]

Thus recurrence of the **moving critical network** requires a balance including the spatial advection of these ratios, not merely zero mean of their material source terms.

---

## 13. Recurrent compensated maximum obligation

A uniformly regular recurrent compensated maximum network must keep

\[
\boxed{
\mathcal R_{comp}>1
}
\]

without allowing

\[
A=0,
\quad
L=0,
\quad
C=0,
\quad
q=0,
\quad
r=0
\]

on the retained full-rank nondegenerate class.

Since the common strain multiplier is already shared with `R_s` and `Theta`, persistence of the strict inequality is controlled by

\[
\boxed{
\mathcal F_{comp}
+v_{rel}D_\xi\log\mathcal R_{comp}
}
\]

relative to the recurrent stretch drift.

No sign theorem for this combined recharge has yet been obtained.

---

## 14. DSD analysis

Three apparently different Rank-2 escape descriptors now share one multiplicative channel:

\[
\boxed{
\mathcal R_s,
\qquad
|\Theta|,
\qquad
\mathcal R_{comp}.
}
\]

All carry

\[
\sigma-\sigma_n.
\]

Their differences are entirely in explicit higher-jet sources.

The genuinely new normalized descriptor is

\[
\boxed{
\Lambda
=|D_\xi q/D_\xi g|,
}
\]

whose material law is strain free.

---

## 15. DSD audit

### Audit A — reusing the invalid beta substitution from the old M17-049
Avoided. `beta_Sigma` is kept distinct from every frame-connection coefficient.

### Audit B — differentiating p=0 off the critical set
Avoided. The general `p` equation and the general identity `p=gq/r` are differentiated before setting `g=p=0`.

### Audit C — treating the critical point as material
Rejected. The `D_max` correction is retained.

### Audit D — claiming R_comp>1 is automatically invariant
Rejected. Its explicit source ledger can drive it through the threshold.

### Audit E — claiming the common strain drift creates three independent recurrence costs
Rejected. It is the same descriptor channel in three normalizations.

### Audit F — proof status
The compensated tilted maximum is reduced to a finite higher-jet recharge system but remains open.

---

## 16. Updated Rank-2 compensated-maximum frontier

\[
\boxed{
R_{max}^{compensated}
\Longrightarrow
R_{max}^{\mathcal R_{comp}>1,\,\Lambda\text{-recharged}}
\ \lor\
T_{A/L/C/q/r=0}
\ \lor\
I_{crit/rank/interface}.
}
\]

The remaining hard scalar is now the strain-free gradient ratio

\[
\boxed{
\Lambda
=\left|\frac{D_\xi q}{D_\xi^2\log\rho}\right|.
}
\]

---

## 17. Next target

The next highest-value calculation is to test whether Euclidean flatness and the weighted-harmonic line law impose a direct spatial equation for `Lambda` on the maximum sheet.

If no sign/monotonicity appears, the compensated maximum network will have reached a higher-jet recharge firewall analogous to the Rank-1 OGLHG covariance firewall.

This is the **Critical Gradient-Ratio Flatness Gate (CGRFG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
