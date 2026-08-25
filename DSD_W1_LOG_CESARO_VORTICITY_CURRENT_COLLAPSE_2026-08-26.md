# DSD W1 Log-Cesaro Vorticity Current Collapse

Date: 2026-08-26

Status: **PRESSURE-FREE VORTICITY ENDPOINT MADE H2-INDEPENDENT IN LOG-SCALE CESARO FORM / PERSISTENCE VS REFORMATION RETIRED AS A TERMINAL BRANCH SPLIT / ALL W1 SURVIVORS CARRY POSITIVE MEAN VORTICITY CURRENT ACROSS UNBOUNDED LOG SCALE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

Recent work introduced two descriptions of the remote endpoint:

1. a Bernoulli/cubic scale current
\[
\mathcal S_B(R)>0,
\qquad
\mathcal S_B(R)\to \mathscr R_3/6>0,
\]
2. a pressure-free weighted-vorticity current
\[
\mathcal S_\Omega(R)
=
\frac12\partial_{\log R}\bar I(R)
\ge0.
\]

The pointwise limit of the second current was first obtained on an H2-coherent corridor.  H2 escalation was therefore temporarily kept as a possible obstruction to pointwise convergence.

The DSD audit asks whether pointwise convergence is actually needed.

It is not.

The already proved cumulative weighted-vorticity lower bound is enough to force a strictly positive **log-scale Cesaro current** with no H2 assumption.

---

## 2. Pressure-free current identity

Let

\[
\bar I(R)
=
\left\langle
I_R(U)
\right\rangle_\mu
\]

be the invariantly averaged Gaussian/radial first weighted-enstrophy functional used in the pressure-free current note.

The exact invariant scale identity is

\[
\boxed{
\mathcal S_\Omega(R)
=
\frac12\partial_{\log R}\bar I(R).
}
\]

The construction gives

\[
\boxed{
\mathcal S_\Omega(R)\ge0.
}
\]

Thus `bar I` is nondecreasing in logarithmic radius.

---

## 3. H2-independent cumulative lower bound

The localized solenoidal Hardy--curl bridge, together with the W1 Type-I envelope and the Barker--Prange/W1 fixed-radius cubic lower bound, gives

\[
\boxed{
\bar I(R)
\ge
c_I\log R-C_I
}
\]

for all sufficiently large `R`, with one fixed `c_I>0`.

No remote H2 ceiling is used here.

This lower bound is inherited by the W1 omega-limit because the radius `R` is fixed before taking the local smooth limit.

---

## 4. Exact logarithmic integral of the current

Write

\[
\rho=\log R.
\]

For `R_1>R_0`, integrate the exact current identity:

\[
\int_{\log R_0}^{\log R_1}
\mathcal S_\Omega(e^\rho)d\rho
=
\frac12
\left[
\bar I(R_1)-\bar I(R_0)
\right].
\]

Therefore

\[
\boxed{
\int_{\log R_0}^{\log R_1}
\mathcal S_\Omega(e^\rho)d\rho
\ge
\frac{c_I}{2}\log R_1-C.
}
\]

Equivalently, with `R_1=R_0e^L`,

\[
\boxed{
\frac1L
\int_{\log R_0}^{\log R_0+L}
\mathcal S_\Omega(e^\rho)d\rho
\ge
\frac{c_I}{2}-o(1).
}
\]

Hence

\[
\boxed{
\liminf_{L\to\infty}
\frac1L
\int_{\log R_0}^{\log R_0+L}
\mathcal S_\Omega(e^\rho)d\rho
\ge
\frac{c_I}{2}>0.
}
\]

This is the H2-independent endpoint statement.

---

## 5. What H2 coherence adds, and what it does not add

If the shell state is sufficiently coherent, the stronger pointwise statement remains valid:

\[
\mathcal S_\Omega(R)
\to
\mathscr R_\Omega/4>0.
\]

If remote derivative structure is highly noncoherent, the pointwise current may oscillate or concentrate in scale.

However the preceding Cesaro identity shows that such oscillation cannot remove the total critical current. It can only redistribute it:

\[
\boxed{
\text{coherence}
\Rightarrow
\text{smooth positive current},
}

\[
\boxed{
\text{reformation}
\Rightarrow
\text{intermittent/oscillatory positive current},
}

while in both cases

\[
\boxed{
\text{mean log-scale vorticity current}>0.
}
\]

Therefore H2 coherence and H2 reformation are diagnostics of the **regularity of the current in scale**, not independent terminal proof mechanisms.

---

## 6. DSD collapse of the persistence/reformation branch

The corrected actual shell variation

\[
\mathfrak V_{form}
=
\sum_k d_k
\]

remains a useful descriptor.

- if `V_form<infinity`, the shell state itself converges in H1 and the vorticity current has a positive pointwise asymptotic trace;
- if `V_form=infinity`, the shell state is repeatedly re-formed and the current may be redistributed among scales.

But the endpoint proof obligation is the same in either case:

\[
\boxed{
\liminf_{L\to\infty}
\frac1L
\int^{L}
\mathcal S_\Omega\,d\rho
>0.
}
\]

Hence the W1 proof tree no longer needs

\[
H_{2,crit}^{tail}
\quad\text{versus}\quad
H2\text{-coherent}
\]

as a terminal split.

---

## 7. Dual-current W1 endpoint

Every nontrivial W1 survivor now carries simultaneously:

### Velocity/Bernoulli endpoint

\[
\boxed{
\mathcal S_B(R)
\to
\frac{\mathscr R_3}{6}>0.
}
\]

### Pressure-free vorticity endpoint

\[
\boxed{
\liminf_{L\to\infty}
\frac1L
\int_{\rho_0}^{\rho_0+L}
\mathcal S_\Omega(e^\rho)d\rho
>0.
}
\]

These statements require no periodic/aperiodic split and no H2 terminal split.

The same critical memory is simultaneously transported in velocity-cubic and vorticity-weighted channels.

---

## 8. Updated DSD logical chain

The current branch structure can be written without A--E and without H2 persistence/reformation as

\[
\boxed{
\text{hypothetical blow-up}
\Longrightarrow
W1
\Longrightarrow
M_{crit}>0
\Longrightarrow
\begin{cases}
\mathcal S_B(\infty)>0,\\[1mm]
\langle\mathcal S_\Omega\rangle_{\log R}>0.
\end{cases}
}
\]

Remote derivative reformation only changes **how** the second positive current is distributed over scale.

It does not remove the current itself.

---

## 9. Remaining endpoint theorem

The next proof target should therefore not be another H2 branch closure.

It should seek one relation between the two mandatory currents strong enough to contradict an unforced finite-energy prelimit, for example:

\[
\boxed{
\text{a dual-current packing/nonrepeatability inequality}
}
\]

or a corrected monotonicity functional whose scale derivative contains both currents with a favorable sign.

A theorem forcing either current to have zero long-scale mean would contradict the W1 endpoint.

No such theorem has yet been established.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
