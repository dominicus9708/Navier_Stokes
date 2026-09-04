# DSD M17-077 — Frozen-angle compensation margin has constant three-halves damping and an exact moving recharge law

Date: 2026-09-04
Canonical ID: **M17-077**

Status: **INTERNAL FROZEN-ANGLE COMPENSATION-MARGIN GATE / ON AN `n`-TANGENT FROZEN-ANGLE LINE MAXIMUM, M17-074 GIVES `D_n q=2q^2-C-p chi_k`, WITH `C=D_xi g<0`; HENCE THE SIGNED RICCATI MARGIN IS `M_FA:=p chi_k+C`, SO `D_nq=2q^2-M_FA` AND SUB-RICCATI ESCAPE REQUIRES `M_FA>0`. TO DIFFERENTIATE THIS WITHOUT EXTENDING THE CRITICAL IDENTITY `p=m/r` OFF THE MAXIMUM, DEFINE FULL FIELDS `Y:=m chi_k`, `r:=a·k`, AND `Mhat:=Y/r+C`; ONLY ON `g=0` DOES `Mhat=M_FA`. THE EXACT MATERIAL LAWS GIVE `D_B(Y/r)=p D_k(sigma_n-sigma)+(sigma_n-1)p chi_k` AT THE MAXIMUM AND `D_B C=D_xi^2(sigma+kappa)-2(sigma+1/2)C`. THEREFORE THE MOVING MAXIMUM MARGIN OBEYS `D_max M_FA=(sigma_n-1)M_FA+pS_k+L_2-(sigma-sigma_k)C+v_rel D_xi Mhat`. MULTIPLYING BY THE FULL JET MAGNITUDE `|a|`, WHOSE MATERIAL MULTIPLIER IS `-(sigma_n+1/2)`, REMOVES THE LAST STRAIN EXPONENT: `N_FA:=|a|Mhat` SATISFIES ON THE MOVING MAXIMUM `D_max N_FA=-(3/2)N_FA+|a|[pS_k+L_2-(sigma-sigma_k)C]+v_rel D_xi N_FA`. THUS THE ACTUAL POSITIVE RICCATI-ESCAPE MARGIN HAS THE SAME EXACT THREE-HALVES HOMOGENEOUS DAMPING AS M17-076. A RECURRENT POSITIVE MARGIN REQUIRES A SPECIFIC THREE-CHANNEL HIGHER-JET RECHARGE PLUS MOVING-LABEL TRANSPORT. NO SIGN THEOREM CONTROLS THAT COMBINED SOURCE, SO THIS SUBBRANCH REACHES A SHARP HIGHER-JET SIGN FIREWALL RATHER THAN A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. n-tangent frozen-angle maximum

Work on the frozen-angle pure-kernel Rank-2 branch at a regular linewise amplitude maximum

\[
\boxed{
g=D_\xi\log\rho=0,
\qquad
C:=D_\xi g<0.}
\]

Assume additionally that the maximum surface is instantaneously `n`-tangent:

\[
\boxed{D_ng=0.}
\]

M17-074 gives

\[
\boxed{
D_nq=2q^2-C-p\chi_k,
}
\]

where

\[
\chi_k=D_k\log|s|,
\qquad
s=m/|a|^2.
\]

---

## 2. Signed Riccati compensation margin

Define on the maximum

\[
\boxed{
\mathcal M_{FA}:=p\chi_k+C.
}
\]

Then

\[
\boxed{
D_nq=2q^2-\mathcal M_{FA}.
}
\]

Therefore:

\[
\boxed{
\mathcal M_{FA}<0
\Longrightarrow
D_nq>2q^2,
}
\]

\[
\boxed{
\mathcal M_{FA}=0
\Longrightarrow
D_nq=2q^2,
}
\]

and

\[
\boxed{
\mathcal M_{FA}>0
\Longrightarrow
D_nq<2q^2.
}
\]

A complete `n`-tangent maximum component that keeps

\[
\mathcal M_{FA}\le0
\]

is therefore subject to the reciprocal Riccati obstruction of M17-048.

The only local escape is to make the margin positive before the focal distance or leave through rank/critical/interface degeneration.

---

## 3. Full-field extension required for differentiation

At the maximum write

\[
a=rk,
\qquad
b=pk+qn.
\]

The critical identity

\[
p=\frac mr
\]

holds only after `g=0` has been imposed and must not be differentiated as a neighborhood identity.

Define instead the full scalar fields

\[
\boxed{r:=a\cdot k,}
\]

\[
\boxed{Y:=m\chi_k,}
\]

and, where `r!=0`,

\[
\boxed{
\widehat{\mathcal M}_{FA}:=\frac Yr+C.
}
\]

Only on the line maximum, where `a=rk` and `m=pr`, do we identify

\[
\boxed{
\widehat{\mathcal M}_{FA}
=\mathcal M_{FA}=p\chi_k+C.
}
\]

All derivatives below are taken on the full fields first and only then evaluated at the maximum.

---

## 4. Material law for Y=m chi_k

M17-041 gives

\[
D_Bm=(\sigma_k-1)m.
\]

M17-075 gives

\[
D_B\chi_k
=S_k-\left(\sigma_k+\frac12\right)\chi_k,
\]

where

\[
\boxed{S_k:=D_k(\sigma_n-\sigma).}
\]

Hence

\[
\begin{aligned}
D_BY
&=(D_Bm)\chi_k+mD_B\chi_k\\
&=(\sigma_k-1)Y+mS_k
-\left(\sigma_k+\frac12\right)Y.
\end{aligned}
\]

Therefore

\[
\boxed{
D_BY=mS_k-\frac32Y.
}
\]

This is another exact constant-damping product law.

---

## 5. Material law for r=a dot k at the maximum

The full scalar is

\[
r=a\cdot k.
\]

M17-033 gives

\[
D_Ba=-\left(\sigma_n+\frac12\right)a
\]

and

\[
D_Bk=(\beta_\Sigma+r_W)n.
\]

Thus

\[
D_Br
=-\left(\sigma_n+\frac12\right)r
+(\beta_\Sigma+r_W)(a\cdot n).
\]

At the line maximum

\[
a\cdot n=t=-g=0,
\]

so

\[
\boxed{
D_Br
=-\left(\sigma_n+\frac12\right)r
}
\]

when evaluated on the maximum.

This step uses the full field `r=a·k` and does not assume `a=rk` off the critical set.

---

## 6. Material law for Y/r

At the maximum,

\[
\begin{aligned}
D_B\left(\frac Yr\right)
&=\frac{D_BY}{r}
-\frac Yr\frac{D_Br}{r}\\
&=\frac{m}{r}S_k
-\frac32\frac Yr
+\left(\sigma_n+\frac12\right)\frac Yr.
\end{aligned}
\]

Since on the maximum

\[
\frac mr=p,
\qquad
\frac Yr=p\chi_k,
\]

we obtain

\[
\boxed{
D_B\left(\frac Yr\right)
=pS_k+(\sigma_n-1)p\chi_k.
}
\]

---

## 7. Material law for C

M17-049 gives at `g=0`

\[
\boxed{
D_BC
=L_2-2\left(\sigma+\frac12\right)C,
}
\]

where

\[
\boxed{
L_2:=D_\xi^2(\sigma+\kappa).
}
\]

This is the line-curvature recharge channel of the maximum.

---

## 8. Material law for the unweighted margin

Add Sections 6--7:

\[
D_B\mathcal M_{FA}
=pS_k
+(\sigma_n-1)p\chi_k
+L_2
-2\left(\sigma+\frac12\right)C.
\]

Use

\[
p\chi_k=\mathcal M_{FA}-C.
\]

Then

\[
\begin{aligned}
D_B\mathcal M_{FA}
={}&(\sigma_n-1)\mathcal M_{FA}
+pS_k+L_2\\
&-\left(\sigma_n+2\sigma\right)C.
\end{aligned}
\]

Trace-free strain gives

\[
\sigma+\sigma_k+\sigma_n=0,
\]

hence

\[
\sigma_n+2\sigma=\sigma-\sigma_k.
\]

Therefore

\[
\boxed{
D_B\mathcal M_{FA}
=(\sigma_n-1)\mathcal M_{FA}
+pS_k+L_2
-(\sigma-\sigma_k)C
}
\]

when evaluated at the maximum.

---

## 9. Moving-maximum law for the margin

The moving critical point derivative is

\[
D_{max}=D_B+v_{rel}D_\xi,
\]

with

\[
\boxed{
v_{rel}
=-\frac{D_\xi(\sigma+\kappa)}{C}.
}
\]

Because the differentiated object is the full extension `Mhat_FA`, the exact moving law is

\[
\boxed{
\begin{aligned}
D_{max}\mathcal M_{FA}
={}&(\sigma_n-1)\mathcal M_{FA}
+pS_k+L_2\\
&-(\sigma-\sigma_k)C
+v_{rel}D_\xi\widehat{\mathcal M}_{FA}.
\end{aligned}
}
\]

No critical-set identity is differentiated off the critical set.

---

## 10. Weight by |a| and obtain constant three-halves damping

The full jet magnitude obeys exactly

\[
\boxed{
D_B|a|
=-\left(\sigma_n+\frac12\right)|a|.
}
\]

Define the full weighted margin

\[
\boxed{
N_{FA}:=|a|\,\widehat{\mathcal M}_{FA}.
}
\]

On the maximum,

\[
N_{FA}=|a|\mathcal M_{FA}.
\]

Since `|a|>0`, `N_FA` has exactly the same sign as the Riccati margin.

Differentiate along the moving maximum:

\[
D_{max}N_{FA}
=(D_{max}|a|)\mathcal M_{FA}
+|a|D_{max}\mathcal M_{FA}.
\]

Using

\[
D_{max}|a|
=-\left(\sigma_n+\frac12\right)|a|
+v_{rel}D_\xi|a|,
\]

and Section 9, the `sigma_n` terms cancel pointwise:

\[
\boxed{
\begin{aligned}
D_{max}N_{FA}
={}&-\frac32N_{FA}\\
&+|a|\Big[
 pS_k+L_2-(\sigma-\sigma_k)C
\Big]\\
&+v_{rel}D_\xi N_{FA}.
\end{aligned}
}
\]

Equivalently,

\[
\boxed{
D_{max}N_{FA}
-v_{rel}D_\xi N_{FA}
+\frac32N_{FA}
=|a|\Big[
 pD_k(\sigma_n-\sigma)
+D_\xi^2(\sigma+\kappa)
-(\sigma-\sigma_k)C
\Big].
}
\]

Thus the actual Riccati-escape margin has exact homogeneous damping `3/2`.

---

## 11. Recurrent positive-margin recharge law

Assume the moving maximum remains on a uniformly positive recurrent compensation branch

\[
0<c_N\le N_{FA}\le C_N<\infty.
\]

Divide Section 10 by `N_FA` and average along the moving maximum:

\[
\boxed{
\left\langle
\frac{
 pS_k+L_2-(\sigma-\sigma_k)C
}{\mathcal M_{FA}}
+v_{rel}D_\xi\log|N_{FA}|
\right\rangle_{max}
=\frac32.
}
\]

This is the exact **moving compensation-margin recharge law**.

The three local recharge channels are

\[
\boxed{
 pD_k(\sigma_n-\sigma),
\qquad
D_\xi^2(\sigma+\kappa),
\qquad
-(\sigma-\sigma_k)C.
}
\]

The fourth channel is the moving-label transport

\[
\boxed{
v_{rel}D_\xi\log|N_{FA}|.}
\]

---

## 12. Persistent n-tangency supplies an additional compatibility, not a sign

The `n`-tangent condition is

\[
A_g:=D_ng=0.
\]

M17-049 gives

\[
D_BA_g
=D_nD_\xi(\sigma+\kappa)
-2\beta_\Sigma D_kg
+(\sigma_k-1)A_g.
\]

Therefore persistence of `A_g=0` along the moving maximum additionally requires

\[
\boxed{
D_nD_\xi(\sigma+\kappa)
-2\beta_\Sigma D_kg
+v_{rel}D_\xi A_g
=0.
}
\]

This is a genuine extra higher-jet compatibility condition, but it does not determine the sign of the Section-10 recharge source.

---

## 13. Sign audit of the recharge source

The combined source

\[
\boxed{
\mathscr R_{FA}
:=
 pD_k(\sigma_n-\sigma)
+D_\xi^2(\sigma+\kappa)
-(\sigma-\sigma_k)C
}
\]

has no universal sign from the currently retained equations:

- `p` is signed;
- `D_k(sigma_n-sigma)` is signed;
- `D_xi^2(sigma+kappa)` is signed;
- `sigma-sigma_k` is signed;
- `C<0`, but that fixes only the last factor, not the whole term.

The n-tangency persistence equation involves a different mixed derivative and strain-shear channel and does not close this sign.

Hence the route

\[
\text{constant damping}
\Longrightarrow
\text{margin must fail}
\]

is not justified without a new sign/coercivity theorem.

---

## 14. DSD interpretation

The local frozen-angle survivor has now been reduced through the chain

\[
\boxed{
\text{shear}
\to
\chi_k
\to
Z_k
\to
\mathcal M_{FA}
\to
N_{FA}.
}
\]

Two apparently different objects now share the same structural rate:

\[
\boxed{
D_BZ_k+\frac32Z_k=\text{recharge},
}
\]

and

\[
\boxed{
D_{max}N_{FA}-v_{rel}D_\xi N_{FA}
+\frac32N_{FA}=\text{recharge}.
}
\]

The `3/2` rate is therefore a recurring Rank-2 structural signature of the pure-kernel resonant geometry.

---

## 15. DSD audit

### Audit A — differentiating p=m/r as a neighborhood identity
Avoided. `Y/r` is differentiated as a full field and only then specialized.

### Audit B — treating N_FA as a new invariant
Rejected. It is a weighted signed margin, not a conserved charge.

### Audit C — using same-marker strain means on a moving maximum
Avoided. The `3/2` damping is obtained pointwise before averaging.

### Audit D — ignoring n-tangency persistence
Avoided. It is stated as a separate exact higher-jet compatibility.

### Audit E — claiming the combined recharge source has a sign
Rejected. No such theorem is presently available.

### Audit F — proof status
The n-tangent frozen-angle maximum is reduced to a positive constant-damped margin with explicit higher-jet recharge, but remains open.

---

## 16. Updated n-tangent frozen-angle frontier

A complete recurrent n-tangent frozen-angle maximum survivor must keep

\[
\boxed{N_{FA}>0}
\]

and simultaneously satisfy

\[
\boxed{
D_{max}N_{FA}
=-\frac32N_{FA}
+|a|\mathscr R_{FA}
+v_{rel}D_\xi N_{FA},
}
\]

with

\[
\boxed{
\mathscr R_{FA}
=pD_k(\sigma_n-\sigma)
+D_\xi^2(\sigma+\kappa)
-(\sigma-\sigma_k)C,
}
\]

plus the n-tangency persistence condition of Section 12.

Thus the branch is no longer an arbitrary shear escape; it is a tightly specified higher-jet recharge problem.

---

## 17. Next target

The next useful question is whether the source `R_FA` is genuinely independent of the weighted-harmonic stress equations and the negative-`kappa` maximum payer from M17-027, or whether those identities force a sign/coercive average.

If that coupling still leaves the source signed, the n-tangent frozen-angle branch has reached a genuine higher-jet sign firewall and the highest-value move is to compare it with the orthogonal mixed-Hessian survivor rather than continue blind differentiation.

This is the **Frozen-Angle Recharge–Payer Coupling Gate (FARPCG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
