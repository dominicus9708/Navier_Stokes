# DSD M17-135 — Long-time resonance is same-carrier only; fresh low-amplitude strong-director ribbon cascade is the current firewall

Date: 2026-09-05  
Canonical ID: **M17-135**

Status: **AUDIT CORRECTION / M17-134 LONG-TIME RESONANT MEANS ARE CONDITIONAL ON SAME-CARRIER ENDPOINT GENEALOGY AND MUST NOT BE TRANSFERRED TO THE FRESH-CARRIER POPULATION. A SCALE-CONSISTENT LOW-AMPLITUDE, ORDER-ONE DIRECTOR-FLUX RIBBON STACK REMAINS COMPATIBLE WITH THE CURRENT UNWEIGHTED ENERGY/PALINSTROPHY LEDGERS. THIS IS A FIREWALL MODEL, NOT AN EXACT NAVIER–STOKES SOLUTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Scope of the correction

M17-134 derived, under endpoint comparability along one pure-kernel material carrier over the remote stage gap,

\[
\Delta\theta_{j,k}
=\theta_j-\theta_{j-k}
=2\log K_k,
\]

and

\[
D_B\log|J_\xi|=\sigma_k-1,
\]

that

\[
\langle\sigma_k\rangle_{j-k:j}
=1+O((\log K_k)^{-1}).
\]

With additional endpoint comparability of the two director jets and normalized amplitude, it gave the conditional mean frame

\[
\boxed{
(\langle\sigma\rangle,
\langle\sigma_k\rangle,
\langle\sigma_n\rangle;
\langle\kappa\rangle)
=
\left(-\frac12,1,-\frac12;\frac32\right)
+O((\log K_k)^{-1}).
}
\]

The derivation itself is valid under those genealogy hypotheses.

The audit question is whether this is a constraint on the actual remote ribbon survivor.

---

## 2. M17-117/120 prevent promotion to a fresh-carrier population law

For the uniformly compact, nondegenerate complete-ribbon class, M17-117 gives a uniform finite similarity-time residence bound

\[
\boxed{\Delta\theta_{\rm carrier}\le\tau_*<\infty.}
\]

M17-120 further gives a uniformly finite first-hitting-stage multiplicity for any one material loop in that compact class.

For remote age `k`,

\[
\Delta\theta_{j,k}=2\log K_k\to\infty.
\]

Hence, once

\[
2\log K_k>\tau_*,
\]

one material loop cannot remain continuously inside the compact ribbon class throughout the entire ancestor-to-descendant interval.

More generally, the finite stage-multiplicity result prevents an infinite recurrent stage sequence from being serviced by one material loop.

Therefore the actual remote survivor is necessarily a **fresh-carrier population problem** unless it exits the compact/nondegenerate ribbon hypotheses.

Consequently,

\[
\boxed{
\text{M17-134 long-time mean resonance}
\not\Rightarrow
\text{fresh-carrier population mean resonance}.
}
\]

The fresh carrier entering at stage `j` need not inherit the strain exposure of the carrier present at stage `j-k`.

---

## 3. Correct branch split

The remote complete-ribbon branch must be written as

\[
\boxed{
R_{2,\rm ribbon}^{remote}
\Longrightarrow
T_{\rm boundary/rank/geometry}
\ \lor\
F_{\rm fresh}^{lowamp,strongdir}.
}
\]

Here `T_boundary/rank/geometry` collects exits from the uniformly compact, nondegenerate complete-ribbon class.

The fresh branch means that successive remote stages are serviced by different material loops while the Eulerian ribbon geometry remains recurrent or recurrent in distribution.

No same-marker integral over `2 log K_k` is automatically available on this branch.

---

## 4. Scale-consistent fresh-ribbon firewall

M17-133 showed that if a uniformly nondegenerate complete ribbon carries a fixed fraction of an age-`k` shell's vorticity enstrophy, then its director-area tube flux cannot decay like `K_k^{-1}`; instead

\[
\boxed{\Phi_k\ge c_\Phi>0.}
\]

A scale-consistent low-amplitude model is therefore

\[
\boxed{
\Phi_k\asymp1,
\qquad
|J_\xi|\asymp1,
\qquad
L_k\asymp1,
\qquad
\rho_k^2\asymp K_k^{-1}.
}
\]

Assume the ribbon occupies similarity volume `V_k\asymp1`.
Then

\[
E_{k,\rm rib}^\omega
:=\int_{\mathcal T_k}|W|^2dy
\asymp
\rho_k^2V_k
\asymp K_k^{-1}.
\]

The scale-critical weighted vorticity shell number is

\[
J_{k,\rm rib}^\omega
:=K_kE_{k,\rm rib}^\omega,
\]

so

\[
\boxed{J_{k,\rm rib}^\omega\asymp1.}
\]

Therefore

\[
\boxed{
\sum_k(J_{k,\rm rib}^\omega)^{3/2}=\infty,
}
\]

while ordinary enstrophy remains summable because the first-hitting scale ratio is geometric:

\[
\boxed{
\sum_kE_{k,\rm rib}^\omega
\asymp
\sum_kK_k^{-1}<\infty.
}
\]

Thus the critical weighted stack can diverge without ordinary enstrophy divergence.

---

## 5. Ordinary palinstrophy is also compatible with this scaling

Write

\[
W=\rho\xi.
\]

Then

\[
|\nabla W|^2
=|\nabla\rho|^2+\rho^2|\nabla\xi|^2.
\]

On a uniformly scaled ribbon profile assume the normalized geometry and normalized amplitude profile have `O(1)` first derivatives:

\[
|\nabla\xi|\lesssim1,
\qquad
|\nabla\rho|\lesssim\rho_k.
\]

Then

\[
\int_{\mathcal T_k}|\nabla W|^2dy
\lesssim
\rho_k^2V_k
\asymp K_k^{-1}.
\]

Hence

\[
\boxed{
\sum_k\int_{\mathcal T_k}|\nabla W|^2dy<\infty.
}
\]

This is consistent with M17-131: positive director-area flux has a palinstrophy cost, but that unweighted cost can be geometrically summable when the vorticity amplitude decays.

---

## 6. Elliptic amplitude homogeneity is the local firewall

The CE-H elliptic equation is

\[
\Delta W=\kappa W.
\]

If a nonzero profile `V` satisfies

\[
\Delta V=\kappa V,
\]

then for every scalar `epsilon>0`,

\[
W_\epsilon:=\epsilon V
\]

satisfies the same equation with the same scalar potential `kappa`:

\[
\Delta W_\epsilon=\kappa W_\epsilon.
\]

Where `V!=0`,

\[
\xi_\epsilon
=\frac{W_\epsilon}{|W_\epsilon|}
=\frac{V}{|V|},
\]

so the director geometry and

\[
J_\xi
\]

are unchanged by amplitude scaling.

Choosing

\[
\epsilon_k\asymp K_k^{-1/2}
\]

produces exactly the firewall scaling

\[
\rho_k^2\asymp K_k^{-1}
\]

without weakening the local director-area geometry.

Therefore

\[
\boxed{
\rho_k\to0
\quad\not\Rightarrow\quad
J_\xi\to0
}
\]

at the elliptic CE-H level.

---

## 7. This is not an exact Navier–Stokes construction

The amplitude-rescaled elliptic profile is only a compatibility model.

It does **not** by itself produce a solution of the full coupled system because the following remain coupled nonlocally or dynamically:

1. `U` is determined from vorticity by Biot–Savart/incompressibility;
2. the strain eigenline relation must hold;
3. `kappa` is not an externally prescribed potential;
4. pressure and the global STF channels remain coupled;
5. fresh carriers must be produced and transported consistently in time;
6. the surrounding shell velocity field must satisfy the M5 critical-tail constraints.

Thus this module establishes a firewall against an invalid amplitude-only exclusion, not existence of a singular solution.

---

## 8. DSD audit

### Audit A — use M17-134 resonance on every remote ribbon stage

Rejected.
The long-time average is a same-carrier genealogy statement.
Fresh material loops do not inherit the previous loop's integrated strain exposure.

### Audit B — order-one director flux forces order-one vorticity amplitude

Rejected.
The elliptic equation is homogeneous in `W`; normalized director geometry can stay fixed while amplitude tends to zero.

### Audit C — divergent critical ribbon stack contradicts finite enstrophy

Rejected.
The firewall scaling gives

\[
J_k^\omega\asymp1,
\qquad
E_k^\omega\asymp K_k^{-1},
\]

so the critical stack diverges while ordinary enstrophy is summable.

### Audit D — ordinary palinstrophy closes the branch

Rejected under the uniformly scaled profile model.
Its ribbon contribution is also `O(K_k^{-1})` and summable.

### Audit E — this firewall realizes the full non-`L^3` Navier–Stokes tail

Not established.
Divergence of the weighted Dirichlet/vorticity stack is only a necessary condition for non-`L^3`; it is not a sufficient condition.
This becomes the next audit gate.

---

## 9. Updated frontier

The fixed-fraction, uniformly nondegenerate remote ribbon branch is now narrowed to

\[
\boxed{
\begin{gathered}
\Phi_k\gtrsim1,\\
\rho_k^2\lesssim K_k^{-1}\ \text{on the critical cheap-stack scale},\\
J_{k,\rm rib}^\omega\asymp1,\\
\text{fresh material carriers required across remote stages}.
\end{gathered}
}
\]

The next question is no longer a same-marker strain-decoupling question.
It is a **population plus cubic-tail capture question**:

\[
\boxed{
\text{Can infinitely many fresh low-amplitude, order-one-}J_\xi\text{ ribbons}
\text{ coexist with the actual non-}L^3\text{ velocity tail under full CE-H/NS coupling?}
}
\]

The immediate next audit must distinguish

\[
\boxed{
\text{divergent weighted vorticity/Dirichlet stack}
}
\]

from

\[
\boxed{
\text{divergent cubic velocity mass}.
}
\]

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
