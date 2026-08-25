# DSD W1 Gaussian Scale Chain and Endpoint Residue

Date: 2026-08-26

Status: **ONE-PARAMETER GAUSSIAN CRITICAL LEDGER DERIVED / CORE BERNOULLI REPLENISHMENT CONTINUED TO ARBITRARY LERAY RADIUS / GAUSSIAN CONFINEMENT MOMENT SHOWN TO CONVERGE TO THE EXISTING CRITICAL RESIDUE R3/6 / CORE AND REMOTE ENDPOINT IDENTIFIED AS ONE ABELIAN SOURCE CHAIN / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The fixed Gaussian p=3 note collapsed the former A--E endgame to one scale-critical Bernoulli replenishment functional. The next question is whether the finite Gaussian core and the already known remote critical-shell residue are actually two separate mechanisms.

They are not.

At p=3 the critical cancellation allows a whole family of Gaussian weights with increasing radius. The resulting exact identities interpolate continuously between finite-core Bernoulli work and the remote weak-L3 endpoint. The apparently remote residue emerges as the large-radius limit of one positive Gaussian confinement term.

---

## 2. Gaussian family indexed by radius

For R>0 define

\[
a_R:=\frac1{8\nu R^2},
\qquad
\phi_R(Y):=\exp\!\left(-\frac{|Y|^2}{8\nu R^2}\right).
\]

Set

\[
E_{3,R}:=\int\phi_R|U|^3dY,
\]

\[
D_{3,R}:=\int\phi_R\left[
|U||\nabla U|^2
+|U|^{-1}\sum_j(U\cdot\partial_jU)^2
\right]dY,
\]

and

\[
M_{3,R}:=\int |Y|^2\phi_R|U|^3dY.
\]

The Bernoulli scalar is

\[
B=P+\frac12|U|^2.
\]

Define the Gaussian Bernoulli source

\[
\boxed{
\mathcal F_{B,R}
:=-\int\phi_R|U|U\cdot\nabla B\,dY.
}
\]

---

## 3. Exact scale-R critical identity

The general weighted p=3 identity is

\[
\frac13E_{3,R}'
+\nu D_{3,R}
+\int\left[
2a_R\nu+
\frac{a_R}{3}(1-4a_R\nu)|Y|^2
\right]\phi_R|U|^3dY
=\mathcal F_{B,R}.
\]

Since

\[
2a_R\nu=\frac1{4R^2}
\]

and

\[
\frac{a_R}{3}(1-4a_R\nu)
=
\frac1{24\nu R^2}
\left(1-\frac1{2R^2}\right),
\]

we obtain

\[
\boxed{
\frac13E_{3,R}'
+\nu D_{3,R}
+\frac1{4R^2}E_{3,R}
+\frac1{24\nu R^2}
\left(1-\frac1{2R^2}\right)M_{3,R}
=\mathcal F_{B,R}.
}
\]

For

\[
R>\frac1{\sqrt2},
\]

all nondifferential terms on the left are nonnegative.

Thus the fixed-core Gaussian replenishment note is only the R=1 member of an entire scale chain.

---

## 4. Invariant-measure scale chain

Let mu be the invariant probability measure already constructed on the W1 recurrent class. Averaging gives for every R>1/sqrt(2)

\[
\boxed{
\langle\mathcal F_{B,R}\rangle_\mu
=
\nu\langle D_{3,R}\rangle_\mu
+\frac1{4R^2}\langle E_{3,R}\rangle_\mu
+\frac1{24\nu R^2}
\left(1-\frac1{2R^2}\right)
\langle M_{3,R}\rangle_\mu.
}
\]

Hence the recurrent Bernoulli source is positive at every finite Gaussian scale for which the state is nontrivial.

The question is what this identity becomes as R tends to infinity.

---

## 5. Log-radius critical density

Let

\[
Q_3(r,U):=r\int_{|Y|=r}|U|^3dS.
\]

After invariant averaging define

\[
\bar Q_3(r):=\langle Q_3(r,U)\rangle_\mu.
\]

With rho=log r, the cubic shell measure is

\[
\langle |U|^3dY\rangle_\mu
=\bar Q_3(e^\rho)d\rho.
\]

The already proved critical-shell limit is

\[
M_\mu(R)
:=\left\langle\int_{R<|Y|<2R}|U|^3dY\right\rangle_\mu
\longrightarrow M_{crit}>0.
\]

Equivalently, for L=log 2,

\[
\int_x^{x+L}\bar Q_3(e^\rho)d\rho
\longrightarrow M_{crit}
\qquad(x\to\infty).
\]

Define the critical log-density

\[
\boxed{
\mathscr R_3:=\frac{M_{crit}}{\log2}.
}
\]

This is the same endpoint residue already obtained from the Abelian p-downarrow-3 calculation.

---

## 6. Gaussian moment is an Abelian log-radius average

Consider

\[
\frac1{R^2}\langle M_{3,R}\rangle_\mu.
\]

Set

\[
r=Re^x.
\]

Since d rho=dx,

\[
\frac1{R^2}\langle M_{3,R}\rangle_\mu
=
\int_{-\infty}^{\infty}
K_\nu(x)
\bar Q_3(Re^x)\,dx,
\]

where

\[
\boxed{
K_\nu(x):=e^{2x}\exp\!\left(-\frac{e^{2x}}{8\nu}\right).
}
\]

The kernel is positive and integrable. Its total mass is exactly

\[
\begin{aligned}
\int_{-\infty}^{\infty}K_\nu(x)dx
&=\int_0^\infty
r_*^2e^{-r_*^2/(8\nu)}\frac{dr_*}{r_*}\\
&=\int_0^\infty r_*e^{-r_*^2/(8\nu)}dr_*\\
&=\boxed{4\nu}.
\end{aligned}
\]

Because fixed-length log-window averages of bar Q_3 converge to the constant mean R3 and the W1 shell bounds give translation-boundedness, the standard Abelian convolution argument yields

\[
\boxed{
\frac1{R^2}\langle M_{3,R}\rangle_\mu
\longrightarrow
4\nu\mathscr R_3.
}
\]

This is the key scale-chain limit.

---

## 7. The Gaussian confinement term becomes exactly R3/6

Multiply the preceding limit by the coefficient in the exact ledger:

\[
\frac1{24\nu R^2}
\left(1-\frac1{2R^2}\right)
\langle M_{3,R}\rangle_\mu.
\]

Therefore

\[
\boxed{
\frac1{24\nu R^2}
\left(1-\frac1{2R^2}\right)
\langle M_{3,R}\rangle_\mu
\longrightarrow
\frac{\mathscr R_3}{6}.
}
\]

The previously remote critical residue is thus the large-radius limit of a positive Gaussian confinement moment. It is not an unrelated second source.

---

## 8. The other two left-hand terms

### Weighted D3

Since phi_R increases pointwise to one as R tends to infinity and D3 is integrable on the W1 invariant class,

\[
\boxed{
\langle D_{3,R}\rangle_\mu
\longrightarrow
\langle D_3\rangle_\mu.
}
\]

### Gaussian cubic mass divided by R^2

The W1 critical shell bound gives at most logarithmic growth of E_{3,R}:

\[
\langle E_{3,R}\rangle_\mu=O(1+\log R).
\]

Hence

\[
\boxed{
\frac1{4R^2}\langle E_{3,R}\rangle_\mu
\longrightarrow0.
}
\]

---

## 9. Large-radius source limit

Combining Sections 7 and 8 in the invariant Gaussian identity gives

\[
\boxed{
\lim_{R\to\infty}
\langle\mathcal F_{B,R}\rangle_\mu
=
\nu\langle D_3\rangle_\mu
+\frac{\mathscr R_3}{6}.
}
\]

But the repository already proved independently from the p-downarrow-3 global Leray identity that

\[
\boxed{
\lim_{p\downarrow3}
\langle\Pi_p\rangle
=
\nu\langle D_3\rangle_\mu
+\frac{\mathscr R_3}{6}.
}
\]

Therefore the two regularizations agree:

\[
\boxed{
\lim_{R\to\infty}
\langle\mathcal F_{B,R}\rangle_\mu
=
\lim_{p\downarrow3}
\langle\Pi_p\rangle.
}
\]

This is a nontrivial cross-audit of the endpoint calculation.

The weak-L3 radial residue and the finite-core Gaussian Bernoulli replenishment are two scale resolutions of the same critical source.

---

## 10. DSD source-chain interpretation

The former picture was

\[
\text{finite recurrent core replenishment}
\quad+\quad
\text{remote critical shell residue}.
\]

The Gaussian scale family replaces it by one chain

\[
\boxed{
\mathcal F_{B,R}
\qquad
1\lesssim R<\infty.
}
\]

At finite R it measures the Bernoulli-gradient action needed to maintain a nontrivial recurrent state inside the Gaussian resolution R.

As R grows, the Gaussian moment samples more and more of the critical 1/r memory.

At R=infinity its confinement contribution converges exactly to R3/6.

Thus

\[
\boxed{
\text{core replenishment}
\longleftrightarrow
\text{critical log-shell memory}
}
\]

is not merely a qualitative routing statement; both occur in one exact one-parameter identity.

---

## 11. Relation to H2 and coherent conveyor endpoints

The Gaussian scale-chain identity itself does not require the remote H2 quantity to be bounded.

If the remote field is scale coherent, the critical shell density is represented by the previously constructed 1/r log-radius conveyor.

If scale coherence fails, the existing H1/Campanato/H2 audit identifies derivative-subscale activity.

These are therefore two geometric realizations of how the same large-R Gaussian source chain is organized, not separate primary sources.

The proof-management endpoint is now the rigidity of the single scale family F_{B,R}.

---

## 12. Remaining question

The new target is sharper than the previous A--E list:

\[
\boxed{
\text{Can an unforced finite-energy Navier--Stokes blow-up corridor support}
\\
\text{a nontrivial recurrent W1 limit for which the positive critical Gaussian}
\\
\text{Bernoulli source persists continuously from finite R to R=infinity,}
\\
\text{with limiting value }\nu\langle D_3\rangle+\mathscr R_3/6>0?
}
\]

A contradiction must now come from a rigidity, monotonicity, or prelimit-transfer property of this one scale-chain functional, not from separately excluding strain locking, contact degeneracy, periodicity, aperiodicity, pressure infinity, or H2-tail geometry.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
