# DSD M19-082 — Center-witness concentration compactness splits into core observability, annular critical escape, or log-scale diffuse escape

Date: 2026-09-12

Status: **CENTER-WITNESS CONCENTRATION-COMPACTNESS / FAILURE OF A UNIFORM CORE MASS FLOOR DOES NOT AUTOMATICALLY PRODUCE ONE CLEAN MOVING PACKET / A NORMALIZED COMPLETE CENTER WITNESS HAS THREE SAFE LARGE-RADIUS SCENARIOS: A FIXED CORE RETAINS POSITIVE MASS, A DYADIC ANNULUS RETAINS POSITIVE MASS WHILE ITS RADIUS ESCAPES, OR THE MASS BECOMES DIFFUSE ACROSS AN INCREASING NUMBER OF LOG-RADIUS SHELLS / THE ANNULAR BRANCH CAN BE BLOWN DOWN TO THE EXISTING CRITICAL SCATTERING TRANSPORT PROBLEM PROVIDED A SCALE-MATCHED DERIVATIVE BOUND HOLDS; FAILURE OF THAT BOUND IS A HIGH-FREQUENCY EXIT / THE LOG-DIFFUSE BRANCH IS GENUINELY DISTINCT AND MUST NOT BE SILENTLY IDENTIFIED WITH ONE-PACKET SCATTERING / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Normalized weighted mass measure

Let \(W(\theta)\) be a nonzero bounded complete rotation-transverse linearized witness.

Use the radial A2 weight

\[
w(y)=(1+\kappa|y|^2)^{-a/2},
\qquad 1<a<3.
\]

Assume the weighted energy is nonzero at the selected times and define the probability measure

\[
\boxed{
 d\mu_\theta(y)
:=
\frac{|W(y,\theta)|^2w(y)\,dy}{E_w(\theta)},
\qquad
E_w(\theta)=\int|W|^2w\,dy.
}
\]

Then

\[
\mu_\theta(\mathbb R^3)=1.
\]

The common-core observability target would be

\[
\boxed{
\exists K<\infty,\ c_K>0:
\mu_\theta(B_K)\ge c_K
}
\]

on the relevant recurrent time set.

---

## 2. Exact negation of a uniform core floor

If no such uniform core floor exists, then for every integer \(n\) one can select a time \(\theta_n\) such that

\[
\boxed{
\mu_{\theta_n}(B_n)<\frac1n.
}
\]

Hence for every fixed \(K\),

\[
\boxed{
\mu_{\theta_n}(B_K)\to0.
}
\]

So failure of observability produces a full radial-escape sequence in the weighted mass measure.

This part is an exact logical dichotomy:

\[
\boxed{
\text{uniform core floor}
\quad\lor\quad
\text{there exists a full radial-escape time sequence}.
}
\]

---

## 3. Dyadic log-radius decomposition of an escape time

For \(j\in\mathbb Z\), define dyadic annuli

\[
A_j:=\{2^j<|y|<2^{j+1}\}.
\]

At each selected escape time \(\theta_n\), set

\[
m_{j,n}:=\mu_{\theta_n}(A_j).
\]

Then

\[
\sum_jm_{j,n}=1.
\]

Since the mass inside every fixed ball vanishes, the active indices must drift to

\[
j\to+\infty.
\]

Now define

\[
M_n:=\sup_jm_{j,n}.
\]

There are two genuinely different escape cases.

---

## 4. Annular packet branch

If

\[
\boxed{
\limsup_{n\to\infty}M_n>0,
}
\]

then after a subsequence there exist \(\eta>0\) and indices \(j_n\to\infty\) such that

\[
\boxed{
m_{j_n,n}\ge\eta.}
\]

Let

\[
R_n:=2^{j_n}\to\infty.
\]

Thus a fixed positive fraction of the normalized weighted mass sits in one moving fixed-ratio annulus

\[
A_{R_n}=\{R_n<|y|<2R_n\}.
\]

This is the clean one-packet escape branch.

---

## 5. Log-scale diffuse branch

If instead

\[
\boxed{
M_n=\sup_jm_{j,n}\to0,
}
\]

then no single dyadic annulus carries a fixed positive fraction of the witness mass.

Since the total mass is one, it must be distributed over an increasing number of log-radius shells.

Symbolically,

\[
\boxed{
\text{radial escape}
+\sup_jm_{j,n}\to0
\Longrightarrow
\text{log-scale diffuse escape}.
}
\]

This is analogous to the vanishing/diffuse branch in concentration-compactness.

It cannot be replaced by an annular packet without an additional inverse inequality.

---

## 6. Correct trichotomy

Combining the previous sections gives the safe center-witness classification

\[
\boxed{
\begin{aligned}
\text{normalized complete center witness}
\Longrightarrow{}&
\mathcal C_{core}\\
&\lor\mathcal C_{annular}\\
&\lor\mathcal C_{log\text{-}diffuse},
\end{aligned}
}
\]

where

\[
\mathcal C_{core}:
\exists K,c>0\text{ with positive recurrent core mass},
\]

\[
\mathcal C_{annular}:
\exists R_n\to\infty\text{ with one shell mass }\ge\eta,
\]

and

\[
\mathcal C_{log\text{-}diffuse}:
\text{all fixed-shell fractions vanish while the total mass escapes}.
\]

---

## 7. Natural annular blow-down normalization

On \(A_{R_n}\), the weight satisfies

\[
w(y)\asymp R_n^{-a}.
\]

Define

\[
\boxed{
V_n(z)
:=R_n^{(3-a)/2}W(R_nz,\theta_n),
\qquad 1<|z|<2.
}
\]

Then

\[
\int_{1<|z|<2}|V_n(z)|^2|z|^{-a}dz
\asymp
\int_{A_{R_n}}|W|^2w\,dy.
\]

After dividing by the shell mass if necessary, the annular packet can be normalized to have order-one fixed-annulus L2 mass.

---

## 8. Derivative scaling creates a second branch inside annular escape

The rescaled derivative obeys

\[
\nabla_zV_n
=R_n^{(5-a)/2}\nabla_yW(R_nz,\theta_n).
\]

Hence

\[
\boxed{
\int_{A_{R_n}}|\nabla W|^2w\,dy
\asymp
R_n^{-2}
\int_{1<|z|<2}|\nabla V_n|^2|z|^{-a}dz.
}
\]

Therefore fixed-annulus H1 compactness requires the scale-matched bound

\[
\boxed{
R_n^2
\frac{
\int_{A_{R_n}}|\nabla W|^2w\,dy
}{
\int_{A_{R_n}}|W|^2w\,dy
}
\lesssim1.
}
\]

If this fails, the escaping annular witness carries a growing normalized derivative frequency.

Thus

\[
\boxed{
\mathcal C_{annular}
\Longrightarrow
\mathcal C_{annular}^{critical\ frequency}
\lor
\mathcal C_{annular}^{high\ frequency}.
}
\]

The second branch reconnects to the already familiar remote derivative/frequency escalation family.

---

## 9. Critical-frequency annular escape reconnects to scattering transport

Assume the scale-matched derivative ratio is bounded and that the background lies in the controlled passive spectator corridor.

Then, after fixed-annulus extraction, the rescaled perturbations have a nonzero local limit.

Along the outward dilation characteristic

\[
R(\tau)=R_ne^{\tau/2},
\]

the exact spectator equation carries nonlinear/pressure/viscous residuals with the same \(R_n^{-2}e^{-\tau}\) suppression that produced M5-563 and M19-069.

For the linearized perturbation, after normalization, the limiting leading equation is therefore the pure critical dilation transport law.

Equivalently the limit has the formal form

\[
\boxed{
W_{lim}(y,\theta)
=r^{-1}B(\log r-\theta/2,\omega)
}
\]

subject to the leading divergence constraint, up to normalization convention.

Thus the critical-frequency annular escape branch rejoins the M19-068 formal tail center and M19-069 scattering-realizability problem.

This statement is conditional on the spectator residual and scale-matched compactness assumptions; it is not an exact construction of a Navier--Stokes center mode.

---

## 10. Why the log-diffuse branch is not already covered

If

\[
\sup_jm_{j,n}\to0,
\]

then every fixed-ratio annulus contains vanishing normalized mass.

Normalizing any one annulus requires amplification factors tending to infinity, and the corresponding derivative/residual bounds need not survive.

Therefore one cannot automatically extract one nonzero critical packet.

The log-diffuse branch may represent:

1. a very broad q-profile;
2. an increasing number of weak critical packets;
3. scale-cascade delocalization;
4. derivative-frequency spread across log radius.

It requires its own inverse estimate or entropy/moment control.

---

## 11. Relation to M19-081 escape sequence

The explicit M19-081 family

\[
W_R=R^{(a-1)/2}R^{-1}F(y/R)
\]

belongs to the annular critical-frequency branch:

- one moving annulus carries essentially all mass;
- the scale-matched derivative ratio stays order one;
- its fixed-annulus renormalization is exactly \(F\).

Thus M19-081 is a concrete functional model of \(\mathcal C_{annular}^{critical\ frequency}\).

---

## 12. Revised center theorem architecture

The center-rigidity problem now splits into three distinct PDE tasks:

\[
\boxed{
\begin{array}{ll}
\mathcal C_{core}:&
\text{prove a local recurrent linear Liouville theorem on a common core};\\[1mm]
\mathcal C_{annular}^{critical}:&
\text{exclude interior realization of the formal aperiodic scattering center};\\[1mm]
\mathcal C_{log\text{-}diffuse}:&
\text{prove an inverse/log-scale concentration estimate or classify diffuse escape}.
\end{array}
}
\]

High-frequency annular escape is routed to the derivative-frequency branch rather than counted as a new center mechanism.

---

## 13. Next calculation

The least understood branch is now \(\mathcal C_{log\text{-}diffuse}\).

M19-083 should test whether the weighted first log-radius moment or an entropy of the dyadic shell distribution

\[
\{m_{j,n}\}_j
\]

has a controlled evolution under the linearized similarity equation.

A uniform moment/entropy bound would prevent mass from spreading over arbitrarily many q-shells and force an annular packet; failure would identify the exact new scale-diffusion payer.
