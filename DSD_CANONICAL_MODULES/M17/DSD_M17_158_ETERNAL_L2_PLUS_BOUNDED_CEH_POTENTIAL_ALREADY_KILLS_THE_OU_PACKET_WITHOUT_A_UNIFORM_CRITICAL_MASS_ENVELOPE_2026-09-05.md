# DSD M17-158 — Eternal L2 plus bounded CE-H potential already kills the OU packet

Date: 2026-09-05  
Canonical ID: **M17-158**

Status: **OU GATE STRENGTHENED / M17-156 USED A UNIFORM TWO-SIDED CRITICAL MASS ENVELOPE TO FORCE AN ETERNAL `L2` OU LIMIT TO VANISH. THAT ENVELOPE IS STRONGER THAN NECESSARY. IF FOR EVERY FIXED FINITE LAG THE AMPLITUDE-NORMALIZED REMOTE PACKET MASS REMAINS UNIFORMLY FINITE ALONG THE EXTRACTING SEQUENCE, THEN THE M17-155 LIMIT IS `L2` AT EVERY REAL OU TIME, WITH NO UNIFORM-IN-TIME MASS RATE ASSUMPTION. IF THE BOUNDED CE-H POTENTIAL `|kappa|<=K0` ALSO PASSES TO THE LIMIT, THEN `Delta V=kappa_infty V` GIVES THE UNIFORM SPECTRAL RATIO `||grad V||_2^2 <= K0||V||_2^2` AT EVERY TIME. THE EXACT BACKWARD OU FOURIER PROPAGATOR MULTIPLIES THIS RATIO BY `e^T`; AN EXPONENTIALLY TILTED FOURIER MEASURE OF ANY NONZERO `L2` FUNCTION CANNOT HAVE ITS SECOND MOMENT DECAY LIKE `e^-T`. HENCE THE ONLY ETERNAL `L2` BOUNDED-POTENTIAL OU PACKET IS ZERO, CONTRADICTING THE NORMALIZATION. THE SURVIVING MASS EXIT IS THEREFORE STRONGER: SOME FIXED FINITE LAG MUST HAVE UNBOUNDED NORMALIZED PACKET-MASS RATIO, OR THE BOUNDED-POTENTIAL/RELATIVE-THICK/QUIET HYPOTHESES MUST FAIL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Replace the global critical envelope by finite-lag comparability

Use the M17-155 packets `V_j` normalized at time zero.

Instead of M17-156's single global constant `C_Q`, assume only:

> for every fixed `T<infinity`, there is `C_T<infinity` such that along the extracting sequence

\[
\boxed{
\sup_{|\tau|\le T}
\frac{E_j(\tau)}{E_j(0)}
\le C_T.
}
\]

The constant may grow arbitrarily fast with `T`.

This assumption is strictly weaker than

\[
E_j(\tau)\le C_Qe^{-\tau/2}E_j(0).
\]

---

## 2. Eternal L2 limit

For each fixed `T`, the finite-lag mass bound gives a uniform global `L2` bound on the translated normalized packets over `|tau|<=T`.

Diagonal compactness therefore yields an eternal limit

\[
V(z,\tau),
\qquad
\tau\in\mathbb R,
\]

satisfying

\[
\boxed{
\partial_\tau V
=\Delta V-\frac12z\cdot\nabla V-V,
}
\]

and

\[
\boxed{
V(\tau)\in L^2(\mathbb R^3)
\quad\forall\tau\in\mathbb R.
}
\]

No uniform rate in `tau` is assumed.

Also

\[
|V(0,0)|=1.
\]

---

## 3. Pass the bounded CE-H potential to the limit

Assume the M17-133 bounded-potential branch on the expanding remote packet shells:

\[
\boxed{|\kappa_j|\le K_0.}
\]

After subsequence extraction,

\[
\kappa_j\overset{*}{\rightharpoonup}\kappa_\infty
\quad\text{in }L^\infty_{loc},
\]

with

\[
|\kappa_\infty|\le K_0.
\]

Because

\[
\Delta V_j=\kappa_jV_j,
\]

local compactness passes the equation to

\[
\boxed{
\Delta V
=\kappa_\infty V
}
\]

for every real `tau`.

---

## 4. Bounded potential gives a uniform frequency-second-moment ratio

Since `V(tau) in L2` and `kappa_infty in L-infinity`, standard cutoff integration by parts gives

\[
\int|\nabla V|^2
=-\int\kappa_\infty|V|^2.
\]

Therefore

\[
\boxed{
\|\nabla V(\tau)\|_2^2
\le
K_0\|V(\tau)\|_2^2
\qquad\forall\tau.
}
\]

By Plancherel,

\[
\boxed{
\frac{
\int|\xi|^2|\widehat V(\xi,\tau)|^2d\xi
}{
\int|\widehat V(\xi,\tau)|^2d\xi
}
\le K_0.
}
\]

---

## 5. Backward OU evolution of the spectral ratio

Let `T>0` and define

\[
a_T:=e^T-1.
\]

M17-156 gives

\[
\|V(-T)\|_2^2
=e^{T/2}I_T,
\]

where

\[
I_T
:=
\int
 e^{2a_T|\xi|^2}
|\widehat V(\xi,0)|^2d\xi.
\]

Similarly,

\[
\boxed{
\|\nabla V(-T)\|_2^2
=e^{3T/2}J_T,
}
\]

where

\[
J_T
:=
\int
 |\xi|^2
 e^{2a_T|\xi|^2}
|\widehat V(\xi,0)|^2d\xi.
\]

Thus

\[
\boxed{
\frac{\|\nabla V(-T)\|_2^2}{\|V(-T)\|_2^2}
=
e^T\frac{J_T}{I_T}.
}
\]

Bounded CE-H potential therefore forces

\[
\boxed{
\frac{J_T}{I_T}
\le K_0e^{-T}
\to0.
}
\]

---

## 6. Exponential Fourier tilting cannot drive a nonzero spectrum to zero frequency

Suppose `V(0)` is nonzero in `L2`.
Then there exists `delta>0` such that

\[
\int_{|\xi|\ge\delta}
|\widehat V(\xi,0)|^2d\xi>0.
\]

Split frequency space into

\[
B_{\delta/2}
\quad\text{and}\quad
\{|\xi|\ge\delta\}.
\]

Under the weight

\[
e^{2a_T|\xi|^2},
\]

the outer set receives at least the factor

\[
e^{2a_T\delta^2},
\]

while the inner ball receives at most

\[
e^{a_T\delta^2/2}.
\]

Their ratio therefore grows like

\[
e^{(3/2)a_T\delta^2}
\to\infty.
\]

Consequently, for all sufficiently large `T`, a positive fraction of the exponentially tilted mass lies outside `B_{delta/2}`.
Hence

\[
\boxed{
\frac{J_T}{I_T}
\ge c\delta^2>0
}
\]

for large `T`.

This contradicts

\[
J_T/I_T\le K_0e^{-T}.
\]

Therefore

\[
\boxed{V(0)=0.}
\]

---

## 7. Contradiction and strengthened branch closure

But M17-155 normalized the packet so that

\[
|V(0,0)|=1.
\]

Hence

\[
\boxed{
R_{2,ribbon}^{relative-thick,quiet,bounded-\kappa,finite-lag-L2}
\Longrightarrow\bot.
}
\]

The surviving mass branch is now sharper than in M17-156:

\[
\boxed{
G_{mass}^{strong}
:
\exists T_0<\infty
\text{ such that }
\frac{E_j(\pm T_0)}{E_j(0)}
\to\infty
}
\]

along every attempted OU-extracting subsequence, unless another hard exit occurs.

---

## 8. DSD audit

1. No uniform critical rate in `tau` is used.
2. `L2` at each time is essential; a merely local eternal OU solution is not covered.
3. Bounded `kappa` must hold on expanding packet regions strongly enough to pass `Delta V=kappa V` globally in the limit.
4. The spectral-ratio proof uses the scalar CE-H potential relation, not ordinary OU energy alone.
5. If finite-lag mass ratios diverge, that is retained as a genuine strong forgetting/import branch and is not called a contradiction.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
