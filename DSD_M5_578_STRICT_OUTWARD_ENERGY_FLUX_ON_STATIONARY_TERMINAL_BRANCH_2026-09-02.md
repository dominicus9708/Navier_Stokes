# DSD M5-578 — Strict Outward Energy Flux on the Stationary Terminal Branch

Date: 2026-09-02

Status: **EVERY NONTRIVIAL RECURRENT STATIONARY TERMINAL PROFILE HAS STRICTLY POSITIVE SCALE-NORMALIZED OUTWARD ENERGY FLUX AT EVERY LOG RADIUS. THIS IDENTIFIES AN UNAVOIDABLE TERMINAL ENERGY-DEFECT CHANNEL BUT DOES NOT YET CONTRADICT TYPE-I SINGULARITY FORMATION. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Input from M5-575

For the terminal critical profile

\[
v(x)=r^{-1}A(q,\omega),
\]

the scale-normalized energy flux satisfies

\[
\boxed{
\Phi_E'(q)-\Phi_E(q)
=
\mathcal C_{AC}(q)-\mathcal D_A(q),
}
\]

where

\[
\mathcal C_{AC}
=\int_{S^2}A\cdot C\,d\omega,
\]

and

\[
\boxed{
\mathcal D_A(q)
=
\int_{S^2}
\left[
|(\partial_q-1)A|^2
+|\nabla_{S^2}A|^2
\right]d\omega
\ge0.
}
\]

On the stationary terminal branch,

\[
\boxed{C=0.}
\]

Hence

\[
\boxed{
\Phi_E'-\Phi_E=-\mathcal D_A.
}
\]

---

## 2. Exact bounded solution formula

Multiply by \(e^{-q}\):

\[
\frac d{dq}\left(e^{-q}\Phi_E(q)\right)
=-e^{-q}\mathcal D_A(q).
\]

The compact log-profile hull gives bounded \(\Phi_E\). Therefore

\[
\lim_{Q\to\infty}e^{-Q}\Phi_E(Q)=0.
\]

Integrating from \(q\) to infinity yields

\[
-e^{-q}\Phi_E(q)
=-\int_q^\infty e^{-t}\mathcal D_A(t)dt.
\]

Thus

\[
\boxed{
\Phi_E(q)
=e^q\int_q^\infty e^{-t}\mathcal D_A(t)dt
=
\int_0^\infty e^{-s}\mathcal D_A(q+s)ds.
}
\]

This is an exact representation, not only an averaged identity.

---

## 3. Positivity

Because

\[
\mathcal D_A\ge0,
\]

we immediately obtain

\[
\boxed{
\Phi_E(q)\ge0
\quad\text{for every }q.
}
\]

If \(\Phi_E(q_0)=0\) at some \(q_0\), then the integral representation forces

\[
\mathcal D_A(q)=0
\qquad\text{for a.e. }q\ge q_0.
\]

But \(\mathcal D_A=0\) implies simultaneously

\[
(\partial_q-1)A=0,
\qquad
\nabla_{S^2}A=0.
\]

Hence on that half-line

\[
A(q,\omega)=ce^q
\]

with constant vector \(c\).

The retained log-profile process is bounded/recurrent. Therefore \(c=0\), so

\[
A=0
\]

on the future half-line. By the stationary smooth/analytic continuation in the retained profile class, this collapses the nontrivial recurrent stationary state.

Consequently every nontrivial recurrent stationary terminal profile obeys

\[
\boxed{
\Phi_E(q)>0
\quad\text{for every }q.
}
\]

---

## 4. Ergodic mean

Averaging the stationary identity gives

\[
-\langle\Phi_E\rangle
=-\langle\mathcal D_A\rangle,
\]

so

\[
\boxed{
\langle\Phi_E\rangle
=
\langle\mathcal D_A\rangle
>0.
}
\]

Thus the stationary branch has a strictly positive mean normalized energy current.

---

## 5. Physical energy flux

By definition,

\[
\Phi_E(q)
=r\int_{S_r}J_A\cdot n\,dS.
\]

Therefore the physical energy flux is

\[
\boxed{
\int_{S_r}J_A\cdot n\,dS
=
\frac{1}{r}\Phi_E(\log r).
}
\]

For every nontrivial stationary recurrent terminal profile this has a fixed outward sign.

At large \(r\), it tends to zero like \(1/r\), consistent with the remote energy-flux audit.

At small \(r\), the exact critical terminal trace carries a singular energy current of order \(1/r\) modulated by the recurrent log profile.

This identifies a genuine **terminal energy defect/source channel** at the singular core.

---

## 6. Homogeneous Landau branch

If additionally

\[
\partial_qA=0,
\]

then \(\mathcal D_A\) and \(\Phi_E\) are constant in \(q\). The ODE gives

\[
\boxed{
\Phi_E=\mathcal D_A>0.
}
\]

Thus the Landau-type point-stress defect necessarily carries a positive normalized energy flux paying its stationary dissipation.

---

## 7. Nonhomogeneous stationary log branch

If

\[
\partial_qA\neq0,
\]

then

\[
\boxed{
\Phi_E(q)
=
\int_0^\infty e^{-s}\mathcal D_A(q+s)ds>0.
}
\]

Therefore even if the momentum-stress defect vector

\[
\kappa
\]

were zero, the stationary log-critical profile could not be defect-free in the energy channel.

This is an important separation:

\[
\boxed{
\text{zero net momentum defect}
\not\Rightarrow
\text{zero terminal energy defect}.
}
\]

---

## 8. Why this is still not a contradiction

The terminal trace is singular and has infinite local Dirichlet energy at the core at the critical \(1/r\) scale.

The local energy balance at the terminal singularity may therefore contain a nontrivial limiting defect; the current inheritance package does not prove that this defect must vanish.

Thus one may not conclude

\[
\Phi_E>0
\Longrightarrow
\text{impossible}.
\]

The correct next theorem would be a terminal local-energy defect exclusion/structure result connecting the smooth \(s<0\) ancient flow to its singular \(s=0\) trace.

---

## 9. Refined stationary endpoint

Every nontrivial stationary endpoint now satisfies

\[
\boxed{
\begin{gathered}
C=0,\\
\mathcal F_A\equiv\kappa,\\
\Phi_E(q)>0\ \forall q,\\
\langle\Phi_E\rangle
=
\langle\mathcal D_A\rangle>0.
\end{gathered}
}
\]

Thus the stationary terminal branch requires an unavoidable singular energy-current mechanism, irrespective of whether its net momentum defect vanishes.

Status: **THE STATIONARY HARD BRANCH HAS BEEN SHARPENED TO A STRICT ONE-SIGN ENERGY-DEFECT BRANCH. ITS REMOVAL REQUIRES CONTROL OF TERMINAL LOCAL-ENERGY DEFECTS ACROSS THE SINGULAR TIME. GLOBAL REGULARITY REMAINS UNPROVED.**