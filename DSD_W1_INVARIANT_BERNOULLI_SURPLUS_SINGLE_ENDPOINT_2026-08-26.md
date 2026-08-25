# DSD W1 Invariant Bernoulli Surplus: Single Endpoint

Date: 2026-08-26

Status: **INVARIANT SCALE-TIME TRANSPORT REDUCED TO ONE POSITIVE BERNOULLI-SURPLUS FUNCTION / SURPLUS SHOWN TO EQUAL THE SCALE DERIVATIVE OF CRITICAL CUBIC MASS PLUS FINITE-R CONFINEMENT / LARGE-R LIMIT EXACTLY R3/6 / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The Gaussian scale-time equation is

\[
\partial_sE_R
+\frac12\left(1-\frac1{2R^2}\right)\partial_{\log R}E_R
+3\nu D_R
+\frac3{4R^2}E_R
=3F_R,
\]

where

\[
F_R=-\int\phi_R|U|U\cdot\nabla B,
\qquad
B=P+\frac12|U|^2.
\]

This note averages the equation on the invariant W1 measure and isolates the exact scalar obstruction that remains after all previous branch collapses.

---

## 2. Invariant scale ODE

Let mu be an invariant probability measure supported on the nontrivial W1 minimal set. Define

\[
\bar E(R):=\langle E_R\rangle_\mu,
\qquad
\bar D(R):=\langle D_R\rangle_\mu,
\qquad
\bar F(R):=\langle F_R\rangle_\mu.
\]

Invariance removes the time derivative:

\[
\boxed{
\frac16\left(1-\frac1{2R^2}\right)
\partial_{\log R}\bar E(R)
+\nu\bar D(R)
+\frac1{4R^2}\bar E(R)
=\bar F(R).
}
\]

---

## 3. Define the Bernoulli surplus

Set

\[
\boxed{
\mathcal S_B(R)
:=\bar F(R)-\nu\bar D(R).
}
\]

Then exactly

\[
\boxed{
\mathcal S_B(R)
=
\frac16\left(1-\frac1{2R^2}\right)
\partial_{\log R}\bar E(R)
+\frac1{4R^2}\bar E(R).
}
\]

Because phi_R increases with R,

\[
\partial_{\log R}\bar E(R)\ge0.
\]

Also bar E(R)>0 on a nontrivial minimal set. Therefore for every

\[
R>1/\sqrt2,
\]

\[
\boxed{
\mathcal S_B(R)>0.
}
\]

Thus recurrent Bernoulli input is strictly larger than the weighted D3 viscous cost at every Gaussian resolution.

The excess is not an unknown remainder. It is exactly the scale-direction transport of critical cubic mass plus the finite-R confinement term.

---

## 4. Large-scale endpoint

The previous Gaussian Abelian calculation gives

\[
\frac1{R^2}\langle M_R\rangle_\mu
\to4\nu\mathscr R_3,
\]

where

\[
\mathscr R_3=M_{crit}/\log2>0.
\]

Equivalently,

\[
\partial_{\log R}\bar E(R)
\to\mathscr R_3
\]

in the corresponding Abelian/log-window sense. Moreover

\[
R^{-2}\bar E(R)\to0.
\]

Hence

\[
\boxed{
\lim_{R\to\infty}\mathcal S_B(R)
=\frac{\mathscr R_3}{6}>0.
}
\]

Therefore the endpoint residue is precisely the asymptotic Bernoulli surplus after subtracting the entire weighted D3 dissipation.

---

## 5. Integral reconstruction of the critical mass

For R>1/sqrt2, solve the scale ODE for the logarithmic derivative:

\[
\boxed{
\partial_{\log R}\bar E(R)
=
\frac{6}{1-1/(2R^2)}
\left[
\mathcal S_B(R)-\frac1{4R^2}\bar E(R)
\right].
}
\]

Thus the whole invariant critical cubic mass profile can be reconstructed from the Bernoulli surplus.

At large R,

\[
\partial_{\log R}\bar E(R)
=6\mathcal S_B(R)+o(1).
\]

So a positive asymptotic surplus is equivalent to a positive asymptotic cubic mass per log radius.

The two statements

\[
\mathscr R_3>0
\]

and

\[
\lim_{R\to\infty}\mathcal S_B(R)>0
\]

are the same endpoint information in two languages.

---

## 6. DSD interpretation

The former proof tree distinguished

- core replenishment;
- pressure work;
- material crossing;
- periodic/aperiodic recurrence;
- H2-tail escape;
- coherent 1/r conveyor;
- endpoint pressure residue.

After the Gaussian/Bernoulli collapse, all of those are diagnostics of one scalar scale-chain:

\[
\boxed{
\mathcal S_B(R)>0,
\qquad
R>1/\sqrt2.
}
\]

At finite R it is the net critical Bernoulli work left after weighted D3 dissipation.

At large R it becomes the critical log-shell transport rate.

At infinity it equals R3/6.

Hence the final W1 survivor can be described without a branch list:

\[
\boxed{
\text{nontrivial recurrent W1}
\Longrightarrow
\text{positive Bernoulli surplus at every scale with nonzero endpoint limit}.
}
\]

---

## 7. External-theorem audit

Classical stationary backward self-similar Liouville results use a Bernoulli-like maximum principle and strong decay/integrability assumptions. Later results extend stationary-profile nonexistence to broader Lp, Lorentz, and Morrey classes.

Those theorems do not directly eliminate the present time-dependent recurrent weak-L3 endpoint. The degree -1/log-periodic tail leaves an O(1) Bernoulli-like boundary trace at scale infinity, precisely where the stationary maximum-principle mechanism loses the boundary condition needed for immediate triviality.

Thus no external theorem is invoked to close S_B.

---

## 8. Single remaining target

The proof attempt is now reduced to one endpoint rigidity question:

\[
\boxed{
\text{Can a smooth finite-energy prelimit Navier--Stokes trajectory generate}
\\
\text{a nontrivial compact recurrent W1 limit with}
\\
\mathcal S_B(R)>0\text{ for every large R and }
\lim_{R\to\infty}\mathcal S_B(R)=\mathscr R_3/6>0?
}
\]

Any future closure need only prove one of the following equivalent endpoint statements:

1. the Bernoulli surplus must vanish along some unbounded scale sequence;
2. the logarithmic cubic mass derivative must have zero liminf;
3. the critical shell density Mcrit must vanish;
4. the scale-time characteristic cannot sustain linear critical L3 growth;
5. a suitable recurrent Bernoulli maximum/flux principle forces S_B(infinity)=0.

Each would contradict the already proved positive endpoint.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
