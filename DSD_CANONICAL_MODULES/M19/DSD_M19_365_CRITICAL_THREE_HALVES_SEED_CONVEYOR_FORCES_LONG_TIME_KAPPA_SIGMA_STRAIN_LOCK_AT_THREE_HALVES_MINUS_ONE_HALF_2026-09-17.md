# DSD M19-365 — Critical three-halves seed conveyor forces a long-time kappa/sigma strain lock at (3/2,-1/2)

Date: 2026-09-17  
Canonical ID: **M19-365**

Status: **ACTIVE CRITICAL-SEED LOCK / LONG-TIME COEFFICIENT-STRAIN BALANCE / SHARP SURVIVOR AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-361--364 and M5-621

For a dormant material seed label that becomes an order-one curvature carrier at late similarity time \(\theta_j\), write

\[
T_j:=\theta_j-\theta_0\to\infty.
\]

M19-361 gives the necessary flux-amplification exposure

\[
\boxed{
\int_{\theta_0}^{\theta_j}\kappa_j\,d\theta
\ge \frac32T_j-C_\kappa.
}
\]

On exact CE-H, M5-621 supplies

\[
\boxed{D_B\log\rho=\sigma+\kappa-1,}
\]

\[
\boxed{D_B\log|\mathcal K|=-\sigma-\frac12,}
\]

and hence

\[
\boxed{D_B\log Z_{curv}=\kappa-\frac32,}
\qquad
Z_{curv}:=\rho|\mathcal K|.
\]

The material flux law is

\[
\boxed{D_B\log|\phi|=\kappa.}
\]

M19-362--364 show that the borderline \(\kappa=3/2\) scaling is compatible with finite dormant volume/flux/enstrophy at the level of resource scaling. The present module asks what additional strain history is required if the dormant seed itself remains in a compact nondegenerate CE-H packet class.

## 2. Compact seed-amplitude hypothesis

Assume the selected dormant-to-active material seed remains in a compact amplitude window

\[
\boxed{0<\rho_-\le \rho_j(\theta)\le \rho_+<\infty}
\]

through the relevant preactivation interval, or more generally that its endpoint amplitude ratio is uniformly bounded:

\[
\boxed{
\left|\log\frac{\rho_j(\theta_j)}{\rho_j(\theta_0)}\right|
\le C_\rho.
}
\]

This is the exact hypothesis needed for a long-time average statement. Failure is an explicit amplitude/nodal/decompactification exit.

Integrating the amplitude law gives

\[
\log\frac{\rho_j(\theta_j)}{\rho_j(\theta_0)}
=
\int_{\theta_0}^{\theta_j}(\sigma_j+\kappa_j-1)\,d\theta.
\]

Therefore

\[
\boxed{
\left|
\int_{\theta_0}^{\theta_j}(\sigma_j+\kappa_j-1)\,d\theta
\right|
\le C_\rho.
}
\]

## 3. Long-time strain consequence

Rearranging,

\[
\int_{\theta_0}^{\theta_j}\sigma_j\,d\theta
=
T_j
-
\int_{\theta_0}^{\theta_j}\kappa_j\,d\theta
+O(1).
\]

Using the M19-361 lower bound on the kappa exposure,

\[
\boxed{
\int_{\theta_0}^{\theta_j}\sigma_j\,d\theta
\le
-\frac12T_j+C.
}
\]

Hence

\[
\boxed{
\limsup_{j\to\infty}
\frac1{T_j}
\int_{\theta_0}^{\theta_j}\sigma_j\,d\theta
\le -\frac12.
}
\]

Thus any compact-amplitude late seed capable of the required three-halves flux amplification must experience asymptotically nonpositive longitudinal strain with mean at most \(-1/2\).

This already rules out a persistently extensional seed axis with positive mean \(\sigma\).

## 4. Curvature compactness supplies the opposite inequality

Assume in addition that the same dormant-to-active seed remains in a compact nondegenerate curvature window at the two endpoints, equivalently

\[
\boxed{
\left|\log\frac{|\mathcal K_j(\theta_j)|}{|\mathcal K_j(\theta_0)|}\right|
\le C_K.
}
\]

Integrating

\[
D_B\log|\mathcal K|=-\sigma-\frac12
\]

gives

\[
\left|
-\int_{\theta_0}^{\theta_j}\sigma_j\,d\theta
-\frac12T_j
\right|
\le C_K.
\]

Therefore

\[
\boxed{
\frac1{T_j}
\int_{\theta_0}^{\theta_j}\sigma_j\,d\theta
=
-\frac12+O(T_j^{-1}).
}
\]

Substituting into the amplitude identity then gives

\[
\boxed{
\frac1{T_j}
\int_{\theta_0}^{\theta_j}\kappa_j\,d\theta
=
\frac32+O(T_j^{-1}).
}
\]

Hence the fully compact critical seed branch has the exact long-time lock

\[
\boxed{
(\bar\kappa_j,\bar\sigma_j)
\longrightarrow
\left(\frac32,-\frac12\right).
}
\]

## 5. Equivalent curvature-amplitude derivation

The same conclusion follows from

\[
D_B\log Z_{curv}=\kappa-\frac32.
\]

If

\[
0<z_-\le Z_{curv}(\theta_0),Z_{curv}(\theta_j)\le z_+<\infty,
\]

then

\[
\int_{\theta_0}^{\theta_j}
\left(\kappa_j-\frac32\right)d\theta
=O(1),
\]

so

\[
\boxed{
\bar\kappa_j=\frac32+O(T_j^{-1}).
}
\]

If amplitude is also compact, the amplitude law then forces

\[
\boxed{
\bar\sigma_j=-\frac12+O(T_j^{-1}).
}
\]

Thus the lock is not an artifact of separately assuming both amplitude and curvature compactness; compact curvature amplitude plus compact vorticity amplitude already suffices.

## 6. Material packet enstrophy density is exactly critical

In backward similarity variables the material velocity is

\[
B=U+\frac12y,
\qquad
\nabla\cdot B=\frac32.
\]

A material volume element therefore obeys

\[
D_B\log dV=\frac32.
\]

Since

\[
D_B\log\rho^2=2(\sigma+\kappa-1),
\]

one material enstrophy element satisfies

\[
\boxed{
D_B\log(\rho^2dV)
=2\sigma+2\kappa-\frac12.
}
\]

At the critical lock

\[
(\kappa,\sigma)=\left(\frac32,-\frac12\right),
\]

the right side is

\[
-1+3-\frac12=\frac32.
\]

Thus

\[
\boxed{
D_B\log(\rho^2dV)=\frac32
}
\]

at the critical lock.

Consequently a base seed with enstrophy of size \(e^{-3T/2}\) can reach order-one packet enstrophy after time \(T\). This exactly matches the M19-362 scaling witness.

Therefore the packet-enstrophy evolution does **not** close the critical conveyor; it confirms that the three-halves resource scaling is dynamically self-consistent at the level of the exact CE-H transport laws.

## 7. Flux-normalized packet enstrophy is neutral at the lock

Because

\[
D_B\log|\phi|=\kappa,
\]

we have

\[
D_B\log\frac{\rho^2dV}{|\phi|}
=
2\sigma+\kappa-\frac12.
\]

At the critical lock,

\[
2\left(-\frac12\right)+\frac32-\frac12=0.
\]

Hence

\[
\boxed{
D_B\log\frac{\rho^2dV}{|\phi|}=0
}
\]

in the exact locked model.

This gives a second consistency check: material packet enstrophy and material flux amplify at precisely the same exponential rate on the critical seed conveyor.

## 8. Incompressibility fixes only the transverse trace

Since \(\operatorname{tr}\Sigma=0\) and \(\xi\) is the longitudinal strain eigenvector with eigenvalue \(\sigma\), the two transverse strain eigenvalues satisfy

\[
\lambda_2+\lambda_3=-\sigma.
\]

At the lock,

\[
\boxed{
\overline{\lambda_2+\lambda_3}\to\frac12.
}
\]

This is not contradictory. It describes longitudinal compression accompanied by net transverse expansion.

The exact split between \(\lambda_2\) and \(\lambda_3\) may remain anisotropic. The local algebra is compatible with regular Burgers-like/axisymmetric geometries and therefore must not be declared impossible without a global ancient/recurrent theorem.

## 9. Relation to M5-622

M5-622 shows that the transverse logarithmic magnitude gradient

\[
G=P_\perp\nabla\log\rho
\]

obeys

\[
D_BG
=P_\perp\nabla(\sigma+\kappa)-L_\perp^TG.
\]

At the critical scalar lock,

\[
\overline{\sigma+\kappa}\to1.
\]

But this controls only the time average along one material label; it does not force

\[
P_\perp\nabla(\sigma+\kappa)=0.
\]

Therefore the next genuine distinction is:

\[
\boxed{
\text{critical scalar lock}
+
\begin{cases}
\text{persistent cross-line forcing }P_\perp\nabla(\sigma+\kappa),\\
\text{or asymptotically homogeneous Burgers-like transverse deformation.}
\end{cases}
}
\]

The first may carry a new spatial derivative cost; the second is a sharp regular-geometry firewall.

## 10. Updated critical seed branch

The M19-364 stationary seed conveyor is therefore sharpened to

\[
\boxed{
\begin{aligned}
G_{seed}^{3/2}
\Longrightarrow{}&
G_{(\bar\kappa,\bar\sigma)\to(3/2,-1/2)}\\
&\lor G_{amplitude/nodal\ loss}\\
&\lor G_{curvature\ degeneration}\\
&\lor G_{representation/genealogy\ loss}.
\end{aligned}
}
\]

On the fully compact lane, the locked pair is not itself a contradiction. It is a new sharp endpoint.

## 11. Preferred next theorem gate

The next target should no longer be merely

\[
\bar\kappa<\frac32-\varepsilon.
\]

The stronger and more geometrically informative target is

\[
\boxed{
\mathcal T_{lock}^{trans}:
\text{show that a positive-density family of long seed lineages with }
(\bar\kappa,\bar\sigma)\to(3/2,-1/2)
}
\]

must either produce a nonsummable cross-line forcing/gradient cost or collapse into a globally classifiable Burgers-like/axisymmetric regular ancient geometry.

This target directly uses the exact CE-H transport laws and respects the axisymmetric no-swirl firewall.

## 12. Audit verdict

**PASS — the critical three-halves conveyor forces a sharp longitudinal strain lock rather than an immediate contradiction.**

On a nondegenerate compact seed lineage, late activation requires

\[
\bar\kappa\to\frac32,
\qquad
\bar\sigma\to-\frac12.
\]

At this lock the material enstrophy element grows at exactly the same \(e^{3T/2}\) rate needed to amplify an exponentially small base seed to order one, and flux-normalized packet enstrophy is neutral. Thus the known exact transport laws certify the criticality of the M19-362--364 witness instead of closing it.

The next unresolved structure is transverse: persistent forcing of \(P_\perp\nabla(\sigma+\kappa)\) versus an asymptotically homogeneous Burgers-like transverse-deformation endpoint.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
