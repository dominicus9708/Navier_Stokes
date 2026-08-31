# DSD M5-388 — Uniform weak-L3 export conveyor: Albritton–Barker scope transfer

Date: 2026-08-31

Status: **THE 2026-08-25 BARKER--PRANGE WEAK-L3 CLOSURE WAS CORRECTLY WITHDRAWN, BUT THE LATER M5-276 ALBRITTON--BARKER ANCIENT-LIOUVILLE ARGUMENT IS STRICTLY STRONGER / IN M5-276 THE NO-H/NO-T SHELL HYPOTHESES ARE USED TO DERIVE THE UNIFORM `L^{3,infinity}` BOUND, NOT AS INDEPENDENT HYPOTHESES OF THE LIOUVILLE STEP / THEREFORE ON ANY COMPLETE REALIZED FIRST-HITTING W1 ORBIT WHERE UNIFORM WEAK-L3 IS ALREADY GIVEN DIRECTLY, THE SAME GLOBAL-RG ANCIENT RECONSTRUCTION, VORTICITY-CAP MILDNESS BRIDGE, TERMINAL-TRACE ARGUMENT, AND ALBRITTON--BARKER THEOREM FORCE THE ANCIENT SOLUTION TO VANISH / COMBINED WITH `W2 -> H_freq`, THE FORMED-ANCESTRY NO-H PERMANENT-EXPORT CONVEYOR HAS NO SURVIVING WEAK-CRITICAL BRANCH / GLOBAL REGULARITY REMAINS UNPROVED BECAUSE H AND FAILURE OF THE COMPLETE FORMED-ANCESTRY/COMPACT-ORBIT PACKAGE REMAIN.**

---

## 1. Purpose

M5-387 reduced the formed-ancestry no-H permanent-export branch to a realized nonstationary critical conveyor carrying a positive-density Navier--Stokes residual.

The natural endpoint split is

\[
\boxed{
W_1:\ \sup_s\|V(s)\|_{L^{3,\infty}}<\infty
}
\]

or

\[
\boxed{
W_2:\ \|V(s_j)\|_{L^{3,\infty}}\to\infty.
}
\]

The 2026-08-25 endpoint audit correctly withdrew an earlier Barker--Prange-based attempt to close `W1`. The present question is whether the later M5-276 Albritton--Barker theorem changes that conclusion on the **complete realized W1 corridor**.

It does.

---

## 2. Preserve the 2026-08-25 correction

The old incorrect route compared a Type-I lower bound on

\[
\int |u|^3
\]

with a weak-L3 upper bound and mistakenly treated the logarithmic growth as a contradiction at the norm level.

The corrected audit showed both cubic-mass estimates have the same logarithmic order.

Therefore the implication

\[
\text{uniform weak-}L^3
\Longrightarrow
\text{regularity}
\]

is **not** available from Barker--Prange alone.

M5-388 does not revive that argument.

---

## 3. The later M5-276 theorem uses a different mechanism

M5-276 imports Albritton--Barker, *On local Type I singularities of the Navier--Stokes equations and Liouville theorems*, Theorem 4.1.

In the formulation used by the repository, the theorem requires a mild ancient solution `U` with

\[
\|U(\tau_k)\|_{L^{3,\infty}}\le M
\]

along a sequence

\[
\tau_k\to-\infty,
\]

and a terminal trace sufficiently close in

\[
\dot B^{-1}_{\infty,\infty}
\]

to the subspace

\[
\mathbb B
=
\{f:\ f(\lambda\cdot)\to0\text{ in }\mathcal D'\}.
\]

M5-276 proves something stronger on the realized corridor: the terminal trace itself lies in `mathbb B`, so the distance is zero.

The theorem then gives

\[
\boxed{U\equiv0.}
\]

---

## 4. Audit where no-H/no-T enters M5-276

M5-276 begins with shell quantities

\[
E_1(R)=R\int_{A_R^*}|\nabla V|^2,
\]

\[
\mathfrak C_A(R)
=R^{-1}\int_{A_R^*}|V-(V)_{A_R^*}|^2,
\]

and localized derivative ratio

\[
\Gamma_R
=
\frac{R\|\nabla f_R\|_2}{\|f_R\|_2}.
\]

Its no-H/no-T assumptions

\[
\Gamma_R\le\Gamma_*,
\qquad
\mathfrak C_A(R)\le C_T
\]

are used to derive

\[
\boxed{
\sup_s\|V(s)\|_{L^{3,\infty}}\le M_*.
}
\]

After this point, the Albritton--Barker application uses the following formed inputs:

1. complete realized W1 orbit and global RG reconstruction;
2. uniform weak-L3 bound;
3. first-hitting vorticity cap on fixed negative-time slabs;
4. actual terminal distributional trace.

It does **not** use `T_Campanato=0` as an independent hypothesis of the external Liouville theorem.

Therefore if item 2 is supplied directly by the branch definition `W1`, the no-T derivation of item 2 is unnecessary.

This is the central scope-transfer observation.

---

## 5. Global RG ancient reconstruction is available on the complete realized orbit

M5-274 defines, for every `rho>0`,

\[
\boxed{
\mathscr R_\rho(T_V)(Y)
=
\rho^{-1/2}
\bigl(S(-\log\rho)V\bigr)(\rho^{-1/2}Y).
}
\]

With

\[
\tau=-\rho<0,
\qquad
U(Y,\tau)=\mathscr R_{-\tau}(T)(Y),
\]

this is an ancient smooth Navier--Stokes solution on

\[
\mathbb R^3\times(-\infty,0).
\]

The algebraic global-`rho` extension uses the **complete recurrent W1 orbit**; it does not require the later no-T weak-L3 derivation.

Thus the current realized export conveyor lies in the same reconstruction class as long as the complete W1/realized-tail package is retained.

---

## 6. Direct W1 gives the ancient weak-critical bound

Assume

\[
\boxed{
\sup_{h\in\mathbb R}
\|S(h)V\|_{L^{3,\infty}}
\le M_*.
}
\]

The Lorentz `L^{3,infinity}` norm is invariant under Navier--Stokes scaling.

Hence the exact reconstruction gives

\[
\boxed{
\|U(\tau)\|_{L^{3,\infty}}
=
\|S(-\log(-\tau))V\|_{L^{3,\infty}}
\le M_*
\qquad\forall\tau<0.
}
\]

Therefore the Albritton--Barker backward-sequence hypothesis holds for every sequence `tau_k -> -infinity`.

No spatial tightness of the material ancestry is needed for this critical-norm identity.

---

## 7. Mildness still follows from weak-L3 plus the first-hitting vorticity cap

M5-276 uses the first-hitting ancient vorticity cap to obtain, on every fixed slab

\[
-B\le\tau\le-A<0,
\]

a finite global bound

\[
\|\Xi(\tau)\|_\infty\le K_{A,B},
\qquad
\Xi=\nabla\times U.
\]

Uniform weak-L3 gives a uniform local `L2` velocity bound on unit balls.

Interior div-curl estimates first give local `W^{1,2}` and `L6`, then `W^{1,6}`, hence a global `L-infinity` bound on each fixed negative-time slab.

Therefore the smooth ancient solution belongs to the mild/Duhamel class required by Albritton--Barker.

Again, this step requires the formed first-hitting vorticity cap and weak-L3, not the absence of export as a material event.

---

## 8. Terminal trace is in the Albritton--Barker subspace

The realized RG/Fuchsian package supplies the actual terminal distributional trace

\[
U(\tau)\to T
\quad\text{in }\mathcal D'
\quad(\tau\uparrow0).
\]

Uniform boundedness in `L^{3,infinity}` passes to the trace in the Lorentz weak-star topology:

\[
\boxed{
T\in L^{3,\infty}.
}
\]

The standard embedding gives

\[
L^{3,\infty}\hookrightarrow
\dot B^{-1}_{\infty,\infty}.
\]

For every test function `phi`, Lorentz Holder and scaling give

\[
|\langle T(\lambda\cdot),\phi\rangle|
\lesssim
\lambda^{-1}
\|T\|_{L^{3,\infty}}
\|\phi\|_{L^{3/2,1}}
\to0.
\]

Thus

\[
\boxed{T\in\mathbb B}
\]

and

\[
\boxed{
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}(T,\mathbb B)=0.
}
\]

---

## 9. Apply Albritton--Barker

The ancient reconstruction now satisfies all imported hypotheses:

1. mild ancient solution;
2. uniform `L^{3,infinity}` bound along a backward sequence;
3. terminal trace in `mathbb B` with distance zero.

Therefore

\[
\boxed{U\equiv0.}
\]

But at `rho=1`,

\[
U(-1)=\mathscr R_1(T)=V,
\]

and the first-hitting/checkpoint construction retains a nonzero vorticity witness.

Contradiction.

Hence

\[
\boxed{
W_1
+
\text{complete realized first-hitting W1 orbit}
\Longrightarrow
\bot.
}
\]

This is a Liouville contradiction, not a Barker--Prange endpoint contradiction.

---

## 10. The W2 branch is already H/T

The corrected weak-critical audit and its later derivative-frequency refinement prove

\[
\boxed{
W_2
\Longrightarrow
T_{Campanato}
\lor
H_{freq}.
}
\]

On the bounded-Campanato/no-H formed corridor this becomes

\[
\boxed{W_2\Longrightarrow H_{freq}.}
\]

Equivalently, uniform annular critical H1 control implies weak-L3, while weak-L3 escalation forces annular critical-H1 escalation and, after the localized derivative-ratio comparison, derivative-frequency H.

Therefore the weak-critical dichotomy on the current no-H formed corridor is exhausted:

\[
\boxed{
W_1\to\bot,
\qquad
W_2\to H_{freq}.
}
\]

---

## 11. Consequence for the M5-387 residual-active export conveyor

M5-387 retained

\[
T_{export,+freq}
\to
R_{tail,+dens}
\]

as the formed no-H permanent-export survivor.

Split this survivor by weak-L3 behavior.

### Uniform coefficient

If

\[
\sup_s\|V(s)\|_{L^{3,\infty}}<\infty,
\]

Sections 5--9 close the complete realized branch by Albritton--Barker.

### Escalating coefficient

If the weak-L3 norm is unbounded, the branch returns to

\[
H_{freq}
\lor
T_{Campanato}.
\]

Thus on the no-H bounded-Campanato/formed-ancestry corridor,

\[
\boxed{
T_{export,+freq}
\text{ has no surviving complete realized weak-critical endpoint.}
}

The residual-active label is therefore not a final leaf there.

---

## 12. DSD scope firewall

This closure has a precise scope.

It requires the **complete realized first-hitting W1 package**:

- complete eternal Leray orbit from compactness/recurrent extraction;
- realized canonical tail and global `rho>0` reconstruction;
- first-hitting vorticity cap;
- actual terminal distributional trace;
- uniform weak-L3 for `W1`.

If the ancestry/compactness process fails before this complete realized object is formed, M5-388 does not silently reconstruct it.

That failure remains

\[
\boxed{
T_{\rm descriptive/ancestry/compactness\ nonformation}.
}
\]

Likewise the derivative-frequency branch `H_freq` is not closed merely because `W2` routes to it.

---

## 13. Updated master frontier

On the **formed complete W1 corridor**, the previous no-H permanent-export survivor is removed:

\[
\boxed{
\text{complete formed no-H branch}
\Longrightarrow
\bot.
}
\]

Accordingly the global proof tree sharpens to

\[
\boxed{
\text{hypothetical singular cascade}
\Longrightarrow
H_{\rm freq/cap}
\lor
T_{\rm ancestry/compactness\ nonformation}.
}
\]

Here `T_nonformation` means failure of the compact/recurrent/realized-tail package needed to reach the complete ancient W1 object, not ordinary bounded-spatial microshape or return/export, which have been reduced in M5-383--387.

---

## 14. Audit verdict

### CLOSED ON THE COMPLETE REALIZED CORRIDOR

\[
\boxed{
W_1:\ \sup_s\|V(s)\|_{L^{3,\infty}}<\infty
\Longrightarrow
U\equiv0
\Longrightarrow
\text{contradiction with the first-hitting witness}.
}
\]

### ROUTED

\[
\boxed{
W_2\Longrightarrow H_{freq}\lor T_{Campanato}.
}
\]

### REMOVED AS A FINAL FORMED NO-H LEAF

- uniform weak-L3 permanent-export conveyor;
- residual-active export conveyor on the complete realized W1 orbit.

### STILL OPEN

- derivative/frequency/capacity H itself;
- failure to form the complete compact/recurrent realized W1 ancient object;
- any compactness/ancestry escape occurring before the M5-274/M5-276 package applies;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
