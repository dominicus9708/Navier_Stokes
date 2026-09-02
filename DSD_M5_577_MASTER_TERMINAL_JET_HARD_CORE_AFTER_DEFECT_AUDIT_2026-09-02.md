# DSD M5-577 — Master Terminal-Jet Hard Core after Defect Audit

Date: 2026-09-02

Status: **MASTER CONSOLIDATION OF M5-569–M5-576. THE FINAL TAIL PROBLEM IS NOW A TWO-BRANCH TERMINAL-JET PROBLEM: STATIONARY DEFECT OR DYNAMIC PARABOLIC PAYER. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Terminal representation

After the remote-tail/scattering reduction, every retained hard state has

\[
\boxed{
u(x,s)
=
r^{-1}A(q,\omega)
+(-s)r^{-3}C(q,\omega)
+O(s^2r^{-5}),
}
\]

with

\[
q=\log r,
\qquad
\omega=x/r.
\]

The leading terminal trace is

\[
\boxed{u_0(x)=r^{-1}A(q,\omega).}
\]

Its leading vorticity is

\[
\boxed{\omega_0(x)=r^{-2}B_A(q,\omega).}
\]

---

## 2. Exact criticality package

The retained nontrivial branch obeys

\[
\boxed{
A\notin L^3(dq\,d\omega),
}
\]

while finite enstrophy and \(L^6\) remain compatible because

\[
\int_{r>R}|\omega_0|^2\lesssim R^{-1},
\qquad
\int_{r>R}|u_0|^6\lesssim R^{-3}.
\]

Moreover

\[
\boxed{
A\neq0
\Longrightarrow
B_A\neq0,
}
\]

so every hard critical terminal trace has a nonzero \(r^{-2}\) terminal-vorticity mode.

This mode blocks the classical zero-final-vorticity backward-uniqueness closure.

---

## 3. Ergodic log-radius factor

The tail map is equivariant:

\[
A_{\sigma_tY}(q,\omega)
=
A_Y(q-t/2,\omega).
\]

The invariant similarity-hull measure therefore induces a translation-invariant ergodic measure on terminal log profiles.

On every nontrivial hard ergodic component,

\[
\boxed{
\frac1L\int_0^L\int_{S^2}|A|^3
\to c_3>0,
}
\]

and

\[
\boxed{
\frac1L\int_0^L\int_{S^2}|B_A|^2
\to c_\omega>0.
}
\]

Hence

\[
\boxed{
\int_{1<r<R}r|\omega_0|^2dx
\sim c_\omega\log R
}
\]

in ergodic mean.

The tail is therefore a positive-density stationary critical process, not a sparse shell sequence.

---

## 4. First parabolic terminal jet

The leading profile is not autonomous.

The exact first coefficient is

\[
\boxed{
C
=\mathcal R_{stat}[A,P]
=-\mathcal L_{-1}A
+\mathcal N(A)
+\mathcal G_{-2}P.
}
\]

Thus \(C\) is the stationary Navier-Stokes residual of the leading \(1/r\) trace.

Any argument treating \(A\) as stationary without proving \(C=0\) is invalid.

---

# BRANCH S — Stationary terminal trace

## 5. Definition

\[
\boxed{C=0.}
\]

Then the critical leading field solves stationary NS on the exterior/log-cylinder class.

Its momentum-stress flux

\[
\mathcal F_A(q)
\]

is constant:

\[
\boxed{\mathcal F_A(q)\equiv\kappa.}
\]

### S1. Continuously homogeneous

If

\[
\boxed{\partial_qA=0,}
\]

then the profile is \((-1)\)-homogeneous. Known classification reduces it to a Landau solution.

A nontrivial survivor therefore has

\[
\boxed{\kappa\neq0,}
\]

i.e. a terminal point-force/stress defect.

This is not yet contradicted by unforcedness for \(s<0\). The relative momentum can obey

\[
\boxed{
M_{rel}'(s)=\kappa,
\qquad
M_{rel}(s)-M_{rel}(s_0)=\kappa(s-s_0),
}
\]

which has exactly the allowed Type-I \(L^1\) growth scale \(O(|s|)\).

Therefore the required closure is a genuine **terminal defect-measure exclusion theorem**.

### S2. Log-radius-dependent stationary

If

\[
\boxed{\partial_qA\neq0,}
\]

then the stationary exterior critical field may be log-periodic or aperiodic recurrent.

It still has

\[
\mathcal F_A(q)\equiv\kappa,
\]

but a complete classification is not currently available at the required generality.

Thus this is a distinct stationary log-critical endpoint.

---

# BRANCH J — Genuinely parabolic terminal jet

## 6. Definition

\[
\boxed{C\neq0.}
\]

The first residual is dynamically absorbed by the \((-s)/r^3\) terminal correction.

### J1. Momentum projection

The exact stress-flux identity is

\[
\boxed{
\mathcal F_A'(q)
=-m_C(q),
}
\]

where

\[
m_C(q)=\int_{S^2}C(q,\omega)d\omega.
\]

Recurrence gives

\[
\boxed{\langle m_C\rangle=0.}
\]

Hence no persistent one-sign net-force residual is allowed.

The surviving residual lies in oscillatory net-force and spherical-mean-zero channels.

### J2. Energy projection

Define the log-cell dissipation

\[
\mathcal D_A(q)
=
\int_{S^2}
\left[
|(\partial_q-1)A|^2
+|\nabla_{S^2}A|^2
\right]d\omega
\ge0.
\]

Let \(\Phi_E(q)\) be the scale-normalized radial energy flux and

\[
\mathcal C_{AC}(q)
=\int_{S^2}A\cdot C\,d\omega.
\]

Then

\[
\boxed{
\Phi_E'-\Phi_E
=\mathcal C_{AC}-\mathcal D_A.
}
\]

Invariant averaging yields

\[
\boxed{
\langle\mathcal D_A\rangle
=
\langle\Phi_E\rangle
+
\langle\mathcal C_{AC}\rangle.
}
\]

Therefore positive critical dissipation has exactly two currently unresolved payers:

1. scale-normalized energy flux;
2. parabolic residual correlation \(A\cdot C\).

Neither has a fixed sign under the present inherited package.

---

## 7. Master endpoint

The final terminal-tail hard core is now

\[
\boxed{
E_{terminal}^{hard}
=
S_{Landau\ defect}
\lor
S_{stationary\ log}
\lor
J_{dynamic\ payer}.
}
\]

More explicitly,

\[
\boxed{
\begin{array}{ll}
S_{Landau\ defect}:&
C=0,\ \partial_qA=0,\ \kappa\neq0;
\\[1mm]
S_{stationary\ log}:&
C=0,\ \partial_qA\neq0,\ \mathcal F_A\equiv\kappa;
\\[1mm]
J_{dynamic\ payer}:&
C\neq0,\ \langle m_C\rangle=0,\
\langle\mathcal D_A\rangle
=\langle\Phi_E\rangle+\langle A\cdot C\rangle.
\end{array}
}
\]

---

## 8. Highest-value next steps

### Target T1 — terminal defect exclusion

Show that a smooth unforced Type-I ancient solution cannot create

\[
\kappa\delta_0
\]

in the stationary residual of its terminal critical trace.

A successful theorem would close \(S_{Landau\ defect}\).

### Target T2 — stationary log-profile rigidity

Classify stationary critical exterior fields with recurrent/log-periodic \(A(q,\omega)\) and bounded regular log-cylinder profile.

A rigidity theorem reducing them to the homogeneous Landau class would collapse \(S_{stationary\ log}\) into T1.

### Target T3 — dynamic payer elimination

For \(J_{dynamic\ payer}\), prove one or both of

\[
\langle\Phi_E\rangle=0,
\qquad
\langle A\cdot C\rangle=0,
\]

or convert either nonzero payer into an already excluded turnover/remote/derivative branch.

If both vanished, then

\[
\langle\mathcal D_A\rangle=0,
\]

forcing the terminal profile into the kernel of the log/angular dissipation and dramatically collapsing the endpoint.

---

## 9. Proof status

No branch above has yet been fully eliminated.

The new gain is structural:

\[
\boxed{
\text{infinite critical tail}
\Longrightarrow
\text{ergodic terminal profile}
\Longrightarrow
\text{first terminal jet}
\Longrightarrow
\text{three explicit hard endpoints}.
}
\]

Status: **GLOBAL REGULARITY REMAINS UNPROVED. THE NEXT MAIN BOTTLENECKS ARE TERMINAL DEFECT CREATION, STATIONARY LOG-PROFILE RIGIDITY, AND THE TWO DYNAMIC ENERGY PAYERS.**