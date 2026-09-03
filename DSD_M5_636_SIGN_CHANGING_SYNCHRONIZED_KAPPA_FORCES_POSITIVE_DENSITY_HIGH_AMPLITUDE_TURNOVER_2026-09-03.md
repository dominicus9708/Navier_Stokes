# DSD M5-636 — Sign-changing synchronized kappa forces positive-density high-amplitude turnover

Date: 2026-09-03

Status: **INTERNAL RELABELING + MAXIMUM BARRIER CLOSURE / WHEN THE SYNCHRONIZED PERSISTENT LEVEL HAS `c_*(theta)>0`, M5-634 FORCES EVERY GLOBAL VORTICITY MAXIMUM ONTO A LEVEL `kappa_max<=0<c_*`, STRICTLY BELOW THE PERSISTENT LEVEL. UNDER THE SAME RELABELING ODE, M5-629 EXCLUDES ANY GENUINELY DISTINCT LOWER LEVEL FROM SUPPORTING ANOTHER BOUNDED NONDEGENERATE PERSISTENT FIXED-FLUX LINEAGE. THEREFORE EVERY POSITIVE `c_*` PHASE IS ACCOMPANIED BY A NONPERSISTENT/TURNOVER HIGH-AMPLITUDE POPULATION. SINCE A NONTRIVIAL ZERO-MEAN `c_*` HAS A POSITIVE SET OF POSITIVE MEASURE, THE SIGN-CHANGING SAME-LEVEL COVARIANCE BRANCH FORCES POSITIVE-DENSITY HIGH-AMPLITUDE TURNOVER. THE ONLY RELABELING NO-TURNOVER SYNCHRONIZED POSSIBILITY LEFT IS `c_* identically 0`. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Positive synchronized phase

On the relabeling branch,

\[
\kappa_{persistent}=c_*(\theta),
\qquad
\langle c_*\rangle=0.
\]

Assume at one recurrent time

\[
\boxed{c_*(\theta)>0.}
\]

---

## 2. Location of the global vorticity maximum

Let `y_max(theta)` be a point where

\[
\rho(y,\theta)=|W(y,\theta)|
\]

attains its global maximum.

The inherited decay and smoothness guarantee existence of such a maximum for a nonzero state.

M5-634 gives at every positive local maximum

\[
\boxed{
\kappa(y_{max},\theta)
\le
-|\nabla\xi(y_{max},\theta)|^2
\le0.
}
\]

Define

\[
\kappa_{max}(\theta):=\kappa(y_{max},\theta).
\]

Then during a positive persistent phase,

\[
\boxed{
\kappa_{max}(\theta)
\le0
<c_*(\theta).
}
\]

Thus the maximum lies on a genuinely lower kappa level.

---

## 3. Ordered lower level cannot be another persistent fixed-flux lineage

M5-628--629 apply to all level histories governed by the same scalar relabeling equation

\[
D_B\kappa=f(\kappa,\theta).
\]

ODE uniqueness preserves strict level order.

A distinct recurrent level remaining below the synchronized zero-mean level has strictly negative time-mean kappa and therefore cannot support a bounded nondegenerate fixed-flux lineage indefinitely.

Hence the level carrying the global maximum during `c_*>0` cannot be another persistent fixed-flux member of the same finite network.

Symbolically,

\[
\boxed{
\kappa_{max}<c_*
\Longrightarrow
\text{maximum-carrying level is nonpersistent/turnover}.
}
\]

---

## 4. Positive-density consequence

If `c_*` is not zero almost everywhere, zero invariant mean implies

\[
\mu\{c_*>0\}>0.
\]

At every such time, the amplitude maximum is carried by a nonpersistent lower-level population.

Therefore

\[
\boxed{
 c_*\not\equiv0
\Longrightarrow
T_{max}^{+density}.
}
\]

Here `T_max^{+density}` denotes positive-density turnover/replacement of the high-amplitude vorticity population.

This is stronger than the M5-635 statement of mere ridge detachment.

---

## 5. Relation to the M5-630 covariance branch

M5-632 showed that

\[
\langle c_*E_*\rangle<0
\]

is the same balance as a positive weighted stretching surplus.

M5-636 now shows that if the zero-mean synchronized level changes sign, the positive phases necessarily lose the amplitude maximum to a nonpersistent lower level.

Thus the phase covariance is physically/geometrically realized through

\[
\boxed{
\text{persistent flux skeleton}
+
\text{positive-density high-amplitude sheath turnover}.
}
\]

The covariance is no longer an abstract same-measure loophole.

---

## 6. Remaining no-turnover relabeling branch

To avoid the high-amplitude turnover conclusion inside the relabeling class, one must have

\[
\boxed{c_*(\theta)\equiv0.}
\]

Thus the relabeling frontier is reduced to

\[
\boxed{
R_{relabel}
\Longrightarrow
Z_{\kappa=0}^{persistent}
\lor
T_{max}^{+density}.
}
\]

The first branch has exactly constant material vorticity flux on every synchronized persistent line/surface.

The second branch is a genuine turnover branch and should be merged with the existing finite-memory replacement/migration ledger.

---

## 7. Firewall

The maximum-carrying kappa level at different times need not correspond to one fixed material label.

That is precisely why the conclusion is turnover/nonpersistence rather than a statement about one label's trajectory.

M5-636 also does not claim that positive-density turnover is itself a contradiction; previous audits show that viscous/diffusive replacement can in principle support recurrent Eulerian structure.

The value of the step is the elimination of a nontrivial **no-turnover sign-changing synchronized branch**.

---

## 8. Next target

Study the only synchronized relabeling no-turnover survivor

\[
\boxed{c_*\equiv0.}
\]

Combine:

- exact constant material flux;
- M5-621 curvature decay on a fixed flux label;
- the M5-618 uniform non-Beltrami defect;
- M5-619 transverse-magnitude/curvature split;
- the zero-kappa maximum flatness condition.

This should determine whether the persistent zero-level spine must be surrounded by a mandatory transverse-magnitude sheath or can support another recurrent curvature mechanism.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]