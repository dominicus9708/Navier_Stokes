# M18-068 — Multi-p amplitude moments are generalized flux-line residence measures, and flux-neutral recycling forces same-line strain segregation or material turnover

**Date:** 2026-09-11  
**Status:** MATERIAL-TUBE / MULTI-MOMENT IDENTIFICATION / GENERALIZED RESIDENCE HIERARCHY / SAME-LINE STRAIN-SEGREGATION ROUTING

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-060--067 develops the recurrent CE-H amplitude moments

\[
M_p=\int_{\mathbb R^3}\rho^pdy,
\qquad p\ge2,
\]

and proves the exact invariant baseline

\[
\mathbb E_p[\sigma+\kappa]
=
c_p
:=1-\frac{3}{2p}.
\]

M18-067 shows that the resulting moment-space hysteresis is strain-driven and does not by itself force a new diffusion payment.

The remaining concrete signed object is the material tube triad of M16-019--022:

\[
D_B\log\rho=\sigma+\kappa-1,
\qquad
D_B\log A=1-\sigma,
\qquad
D_B\log\Phi=\kappa.
\]

The present module identifies these two lines exactly.

The key result is that the global \(p\)-moment is the flux integral of a generalized vortex-line residence factor

\[
\boxed{
L_{p-1}:=\int_\Gamma\rho^{p-1}ds.
}
\]

Moreover, on a flux-neutral recurrent same-lineage tube, recurrence of the generalized residence factor forces

\[
\boxed{
\langle\bar\sigma_{p-1}\rangle=c_p.
}
\]

Thus the full multi-\(p\) baseline hierarchy has an exact material-tube meaning.

Comparing two exponents then forces a positive same-vortex-line amplitude/strain covariance unless flux, generalized residence, or material labels turn over.

## 2. Tube-coordinate disintegration

Work on the active CE-H region \(\rho>0\), where vorticity lines define local oriented tube coordinates.

For an infinitesimal oriented tube label \(\lambda\), let

\[
d\nu_\theta(\lambda):=|d\Phi_\lambda(\theta)|
\]

be the positive absolute vorticity-flux measure, and let \(s\) be arclength along the corresponding instantaneous vortex line segment \(\Gamma_\lambda(\theta)\).

M16-020 gives

\[
dV=dA\,ds
=\frac{d\nu\,ds}{\rho}.
\]

Therefore, for every finite \(p\ge2\),

\[
\begin{aligned}
M_p
&=\int\rho^p\,dV\\
&=\int_\Lambda\int_{\Gamma_\lambda}
\rho^{p-1}ds\,d\nu(\lambda).
\end{aligned}
\]

Define, for every \(m\ge1\),

\[
\boxed{
L_m(\lambda,\theta)
:=
\int_{\Gamma_\lambda(\theta)}\rho^m ds.
}
\]

Then

\[
\boxed{
M_p
=
\int_\Lambda L_{p-1}\,d\nu.
}
\]

For \(p=2\),

\[
L_{p-1}=L_1=L_\rho,
\]

which is exactly the vorticity-weighted line-residence factor of M16-020.

Hence the M18 amplitude-moment hierarchy is precisely a hierarchy of generalized flux-line residence measures.

## 3. Weighted strain and coefficient disintegration

Because CE-H gives

\[
W\cdot\nabla\kappa=0,
\]

\(\kappa\) is constant along each instantaneous vortex line.

Define the generalized line-weighted axial strain

\[
\boxed{
\bar\sigma_m
:=
\frac{\int_\Gamma\sigma\rho^m ds}{L_m}.
}
\]

Then

\[
\boxed{
\int\sigma\rho^p dV
=
\int_\Lambda
\bar\sigma_{p-1}L_{p-1}\,d\nu,
}
\]

and

\[
\boxed{
\int\kappa\rho^p dV
=
\int_\Lambda
\kappa_\lambda L_{p-1}\,d\nu.
}
\]

Thus the \(p\)-weighted net-growth field is a flux-line ensemble average of

\[
\boxed{
\kappa_\lambda+\bar\sigma_{p-1,\lambda}.
}
\]

## 4. Exact generalized line-residence evolution

M16-019 gives the material laws

\[
D_B\rho=(\sigma+\kappa-1)\rho
\]

and

\[
D_B ds
=\left(\sigma+\frac12\right)ds.
\]

For \(m\ge1\),

\[
D_B(\rho^m ds)
=
\left[
 m(\sigma+\kappa-1)
 +\sigma+\frac12
\right]
\rho^m ds.
\]

Integrating along one material vortex-line segment gives

\[
\boxed{
L_m'
=
\left(m\kappa-m+\frac12\right)L_m
+(m+1)\int_\Gamma\sigma\rho^m ds.
}
\]

Hence

\[
\boxed{
D_B\log L_m
=
m\kappa
+(m+1)\bar\sigma_m
-m+\frac12.
}
\]

For \(m=1\), this becomes

\[
D_B\log L_\rho
=
\kappa+2\bar\sigma_\rho-\frac12,
\]

exactly M16-020.

## 5. Tube contribution to the p-moment

The absolute tube flux obeys, as long as the oriented label stays nondegenerate,

\[
D_B\log|\Phi|=\kappa.
\]

Define the tube contribution to \(M_p\) by

\[
\boxed{
E_{p,\lambda}
:=
|\Phi_\lambda|L_{p-1,\lambda}.
}
\]

Then

\[
\begin{aligned}
D_B\log E_{p,\lambda}
&=
\kappa
+(p-1)\kappa
+p\bar\sigma_{p-1}
-(p-1)+\frac12\\
&=
p\left(
\kappa+\bar\sigma_{p-1}
-1+\frac{3}{2p}
\right).
\end{aligned}
\]

Therefore

\[
\boxed{
\frac1pD_B\log E_{p,\lambda}
=
\kappa+\bar\sigma_{p-1}-c_p,
\qquad
c_p=1-\frac{3}{2p}.
}
\]

This is the exact material-tube counterpart of the global M18-060 moment law.

## 6. Flux-neutral recurrent tube baseline

Consider one persistent same-lineage material tube segment satisfying

\[
0<\Phi_-\le|\Phi(\theta)|\le\Phi_+<\infty.
\]

Then

\[
\lim_{T\to\infty}
\frac{\log|\Phi(T)|-\log|\Phi(0)|}{T}=0,
\]

so

\[
\boxed{
\langle\kappa\rangle_{tube}=0.
}
\]

Assume also that for one \(m\ge1\),

\[
0<L_{m,-}\le L_m(\theta)\le L_{m,+}<\infty.
\]

Then the long-time mean logarithmic drift of \(L_m\) vanishes.

The generalized residence equation gives

\[
0
=
m\langle\kappa\rangle
+(m+1)\langle\bar\sigma_m\rangle
-m+\frac12.
\]

Using \(\langle\kappa\rangle=0\),

\[
\boxed{
\langle\bar\sigma_m\rangle
=
\frac{m-1/2}{m+1}
=
1-\frac{3}{2(m+1)}.
}
\]

Set

\[
m=p-1.
\]

Then

\[
\boxed{
\langle\bar\sigma_{p-1}\rangle
=
c_p
=
1-\frac{3}{2p}.
}
\]

Thus the \(p\)-dependent similarity baseline of M18-060--062 is exactly the strain baseline of a flux-neutral recurrent material tube whose \(p\)-residence is recurrent.

## 7. Endpoints of the hierarchy

For \(p=2\),

\[
\boxed{
\langle\bar\sigma_1\rangle
=\frac14,
}
\]

recovering the M16-020/022 \(\rho ds\)-weighted residence baseline.

As \(p\to\infty\),

\[
\boxed{c_p\uparrow1.}
\]

This approaches the persistent active-marker amplitude baseline from M16-022,

\[
\langle\sigma_m\rangle=1,
\]

although no interchange of \(p\to\infty\) with tube/time limits is asserted here.

The correct interpretation is structural:

\[
\boxed{
\text{low-amplitude line residence sees baseline }1/4,
\quad
\text{increasing amplitude concentration shifts the baseline toward }1.
}
\]

## 8. Two-exponent same-line segregation identity

Let

\[
q>p\ge2.
\]

On one vortex line define the \(p\)-line probability measure

\[
\boxed{
 d\pi_{p,\lambda}(s)
 :=
 \frac{\rho^{p-1}ds}{L_{p-1}}.
}
\]

Then

\[
\bar\sigma_{p-1}
=
\mathbb E_{\pi_p}[\sigma].
\]

Since

\[
\rho^{q-1}
=
\rho^{p-1}\rho^{q-p},
\]

we also have

\[
\bar\sigma_{q-1}
=
\frac{
\mathbb E_{\pi_p}[\sigma\rho^{q-p}]
}{
\mathbb E_{\pi_p}[\rho^{q-p}]
}.
\]

Therefore

\[
\boxed{
\bar\sigma_{q-1}-\bar\sigma_{p-1}
=
\frac{
\operatorname{Cov}_{\pi_p}
\left(\sigma,\rho^{q-p}\right)
}{
\mathbb E_{\pi_p}[\rho^{q-p}]
}.
}
\]

This identity is purely linewise.

The coefficient \(\kappa\) does not appear because it is constant along each instantaneous CE-H vortex line.

## 9. Exact recurrent same-line covariance floor

Assume the same material tube is flux-neutral and both generalized residence factors

\[
L_{p-1},
\qquad
L_{q-1}
\]

remain bounded above and away from zero recurrently.

Then Section 6 gives

\[
\langle\bar\sigma_{p-1}\rangle=c_p,
\qquad
\langle\bar\sigma_{q-1}\rangle=c_q.
\]

Subtracting,

\[
\boxed{
\left\langle
\bar\sigma_{q-1}-\bar\sigma_{p-1}
\right\rangle
=
c_q-c_p
=
\delta_{pq}
:=
\frac32\left(\frac1p-\frac1q\right)>0.
}
\]

Using Section 8,

\[
\boxed{
\left\langle
\frac{
\operatorname{Cov}_{\pi_p}
(\sigma,\rho^{q-p})
}{
\mathbb E_{\pi_p}[\rho^{q-p}]
}
\right\rangle
=
\delta_{pq}>0.
}
\]

Hence a flux-neutral same-lineage tube cannot realize the multi-\(p\) recurrent hierarchy with spatially uniform axial strain along its active line.

Higher-amplitude line segments must, on average, sample larger axial strain.

## 10. Positive-density same-line strain heterogeneity

On the compact CE-H hull,

\[
|\sigma|\le S_*.
\]

Thus

\[
\left|
\bar\sigma_{q-1}-\bar\sigma_{p-1}
\right|
\le2S_*.
\]

Since its long-time mean equals \(\delta_{pq}>0\), there exists a positive-density event set on which, for example,

\[
\boxed{
\bar\sigma_{q-1}-\bar\sigma_{p-1}
\ge
\frac{\delta_{pq}}2.
}
\]

At every such event, both weighted means lie between the essential infimum and supremum of \(\sigma\) on the same vortex-line segment.

Therefore

\[
\boxed{
\operatorname*{ess\,osc}_{\Gamma_\lambda}\sigma
\ge
\frac{\delta_{pq}}2.
}
\]

If the relevant line segment remains in a controlled finite core with bounded arclength/geometric carrier constants, the existing M16-022--024 machinery converts this into

\[
\boxed{
\text{same-line axial strain gradient/director deformation}
\lor
\text{marker/sheath/component turnover}.
}
\]

Thus the multi-\(p\) covariance has a direct material-genealogy realization.

## 11. What happens if generalized residence is not recurrent

The conclusion of Section 9 requires recurrence/nondegeneracy of

\[
L_{p-1}
\quad\text{and}\quad
L_{q-1}.
\]

If either loses its upper/lower compactness along the same material label, then one has a genuine material-residence exit:

\[
\boxed{
G_{generalized\ line\ residence\ decompactification}.
}
\]

Possible realizations include

- amplitude depletion on the tracked tube;
- uncontrolled line stretching/length growth;
- active-marker migration;
- tube segmentation or component loss;
- replacement of the material label;
- remote escape.

These must not be hidden by taking logarithmic averages.

## 12. What happens if flux is not neutral

If

\[
|\Phi|
\]

fails to remain bounded above and away from zero on the same recurrent lineage, then

\[
\langle\kappa\rangle
\]

need not vanish.

This is exactly the signed flux branch of M16-021:

\[
\boxed{
G_{flux\ drift/decay/growth}
\to
G_{material\ flux\ replacement/exit}
}
\]

unless a new compensating label enters.

Therefore the correct material split is

\[
\boxed{
\begin{aligned}
\text{multi-p recurrent tube support}
\Longrightarrow{}&
G_{flux\ drift/replacement}\\
&\lor
G_{generalized\ residence\ decompactification}\\
&\lor
G_{same-line\ amplitude/strain\ segregation}.
\end{aligned}
}
\]

## 13. Global material disintegration of the M18 covariance

The preceding same-line theorem can also be written as a global conditional-covariance decomposition.

Factor the joint \(p\)-weighted recurrent measure by state/tube label and line position.

Let

\[
 d\eta_p(Y,\lambda)
 \propto
 L_{p-1,\lambda}(Y)
 \,d\nu_Y(\lambda)\,d\mu(Y),
\]

normalized to a probability measure, and condition along each line with \(\pi_{p,Y,\lambda}\).

Set

\[
w:=\rho^{q-p}.
\]

Then the M18-062 covariance admits the exact total-covariance split

\[
\boxed{
\operatorname{Cov}_{\mathbb P_p}(h,w)
=
C_{line}^{pq}
+
C_{tube}^{pq},
}
\]

where

\[
\boxed{
C_{line}^{pq}
:=
\mathbb E_{\eta_p}
\left[
\operatorname{Cov}_{\pi_p}(h,w)
\right]
}
\]

and

\[
\boxed{
C_{tube}^{pq}
:=
\operatorname{Cov}_{\eta_p}
\left(
\bar h_{p,\lambda},
\frac{L_{q-1,\lambda}}{L_{p-1,\lambda}}
\right).
}
\]

Since \(\kappa\) is constant along each line,

\[
\boxed{
C_{line}^{pq}
=
\mathbb E_{\eta_p}
\left[
\operatorname{Cov}_{\pi_p}(\sigma,\rho^{q-p})
\right].
}
\]

Also

\[
\boxed{
\bar h_{p,\lambda}
=
\kappa_\lambda+ar\sigma_{p-1,\lambda}.
}
\]

Therefore the exact M18-062 positive covariance

\[
\delta_{pq}\mathbb E_p[w]>0
\]

must be carried by at least one of

\[
\boxed{
G_{within\ vortex\ line\ strain/amplitude\ covariance}
\lor
G_{between\ tube/lineage\ concentration\ covariance}.
}
\]

This is a material refinement of the spatial-versus-phase split of M18-064.

## 14. Between-tube branch

The between-tube term is

\[
C_{tube}^{pq}
=
\operatorname{Cov}_{\eta_p}
\left(
\kappa+\bar\sigma_{p-1},
R_{pq}
\right),
\]

where

\[
\boxed{
R_{pq}
:=
\frac{L_{q-1}}{L_{p-1}}.
}
\]

Hence

\[
\boxed{
C_{tube}^{pq}
=
\operatorname{Cov}_{\eta_p}(\kappa,R_{pq})
+
\operatorname{Cov}_{\eta_p}(\bar\sigma_{p-1},R_{pq}).
}
\]

So if the global covariance is not paid by within-line strain heterogeneity, it must be paid by a tube/lineage population in which generalized amplitude concentration \(R_{pq}\) is correlated with either

- tube-wise \(\kappa\), or
- tube-wise line-averaged axial strain.

This is a genuine material-population segregation branch.

It does **not** by itself imply a nonzero mean flux drift because covariance with \(R_{pq}\) is not the same measure as the flux mean of \(\kappa\).

That distinction preserves the M16-020 measure-mismatch firewall.

## 15. Relation to M16-021 negative residence covariance

For \(p=2\),

\[
L_{p-1}=L_1=L_\rho.
\]

M16-021 shows that a negative enstrophy-weighted \(\kappa\) budget can be realized by

\[
\operatorname{Cov}_{\Phi}(\kappa,L_\rho)<0
\]

without mean flux decay.

M18-068 does not contradict this.

The new between-tube variable is instead

\[
R_{2q}
=
\frac{L_{q-1}}{L_1},
\]

which measures concentration **inside** the line residence.

Thus one recurrent survivor may in principle satisfy simultaneously

\[
\operatorname{Cov}_{\Phi}(\kappa,L_1)<0
\]

and

\[
\operatorname{Cov}_{\eta_2}(\kappa,R_{2q})>0.
\]

The physical interpretation is then highly specific:

- negative-\(\kappa\) phases/tubes preferentially carry larger total \(\rho ds\) residence;
- more strongly high-amplitude-concentrated tubes preferentially carry larger \(\kappa\) or larger axial strain.

This is not yet impossible, but it is a much narrower covariance architecture than a generic recharge loop.

## 16. Audit verdict

### Certified

1. The global amplitude moment is exactly
   \[
   M_p=\int L_{p-1}\,d|\Phi|.
   \]
2. Generalized line residence satisfies
   \[
   D_B\log L_m
   =m\kappa+(m+1)\bar\sigma_m-m+\frac12.
   \]
3. A flux-neutral recurrent tube with recurrent \(L_{p-1}\) has
   \[
   \langle\bar\sigma_{p-1}\rangle=c_p.
   \]
4. If the same tube supports recurrent \(p\)- and \(q\)-residence, then
   \[
   \left\langle
   \frac{\operatorname{Cov}_{\pi_p}(\sigma,\rho^{q-p})}
   {\mathbb E_{\pi_p}[\rho^{q-p}]}
   \right\rangle
   =c_q-c_p>0.
   \]
5. Hence flux-neutral same-lineage multi-p recurrence forces positive-density same-vortex-line axial-strain heterogeneity unless generalized residence or labels turn over.
6. The global M18 covariance further splits exactly into within-line strain/amplitude covariance and between-tube concentration covariance.
7. The between-tube branch preserves, rather than bypasses, the M16-020 measure-mismatch firewall.

### Not certified

- that every global recurrent amplitude population is represented by one fixed finite tube family for all time;
- that the between-tube concentration covariance forces mean flux decay;
- that generalized residence is uniformly compact on every surviving material label;
- ancestry closure of the resulting strain-gradient/turnover payments;
- remote/critical roots;
- global regularity.

## 17. Next target

The sharp remaining material branch is the **between-tube covariance**

\[
C_{tube}^{pq}>0.
\]

M18-069 should compare it directly with the M16-021 negative \(\kappa\)--residence covariance at \(p=2\).

The question is whether a flux-neutral tube ensemble can simultaneously maintain

\[
\operatorname{Cov}_{\Phi}(\kappa,L_1)<0
\]

and a fixed positive high-concentration covariance involving

\[
R_{2q}=L_{q-1}/L_1
\]

without forcing either

- a three-population ordering in \((L_1,R_{2q},\kappa)\);
- same-tube strain heterogeneity;
- flux-label replacement;
- or concentration/residence decompactification.

That is now a more constrained and materially interpretable target than the generic moment-loop hysteresis of M18-066--067.
