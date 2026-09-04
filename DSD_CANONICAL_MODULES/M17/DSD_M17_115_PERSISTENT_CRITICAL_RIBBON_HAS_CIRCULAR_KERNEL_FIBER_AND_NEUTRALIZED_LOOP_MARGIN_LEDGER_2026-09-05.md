# DSD M17-115 — Persistent critical ribbon has a circular kernel fiber and a neutralized loop-margin ledger

Date: 2026-09-05
Canonical ID: **M17-115**

Status: **INTERNAL CRITICAL-RIBBON PERSISTENCE GATE / M17-114 ISOLATES THE ONLY ANALYTIC ESCAPE FROM A UNIFORM KERNEL-TUBE PEAK-OSCILLATION BOUND: `g=D_xi log rho` MAY CONVERGE TO ZERO IDENTICALLY ALONG A KERNEL FIBER. IF THIS RIBBON PERSISTS MATERIALLY, `D_B g=D_xi(sigma+kappa)=0` MUST HOLD ALONG THE FIBER. FLATNESS GIVES `gamma_k=q`, `D_k q=0`; WITH `D_k xi=0`, A COMPLETE RIBBON FIBER IS A MATERIAL PLANE CIRCLE OF RADIUS `1/|q|`. MATERIAL PERSISTENCE OF `gamma_k=q` FURTHER FORCES `D_k Omega+p Omega+(sigma-sigma_k)q=0`, `Omega=beta_Sigma+r_W`. MOST IMPORTANTLY, THE TRANSVERSE-SECTION THREE-HALVES MARGIN PAYMENT OF M17-107 DOES NOT CARRY OVER TO THE RIBBON. FOR A MATERIAL CLOSED KERNEL LOOP, `D_B log ds=sigma_k+1/2`, `D_B log|J_xi|=sigma_k-1`, AND `D_B N_R2=-(3/2)N_R2+|a|R_R2`; THEREFORE THE HOMOGENEOUS TERMS CANCEL EXACTLY IN THE LOOP INVENTORY `I_rib=oint (N_R2/|J_xi|) ds`, GIVING `dI_rib/dtheta=oint (|a|/|J_xi|)R_R2 ds=(1/|q|)oint R_R2 ds`. A RECURRENT RIBBON REQUIRES ZERO MEAN LOOP RECHARGE, NOT POSITIVE THREE-HALVES RECHARGE. THE RIBBON IS THUS A GENUINELY DIFFERENT RESONANT SURVIVOR AND MUST BE AUDITED SEPARATELY RATHER THAN COUNTED BY THE TRANSVERSE PEAK MEASURE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Critical-ribbon hypothesis

Work on the pure-kernel Rank-2 branch

\[
J_\xi=|J_\xi|k\neq0,
\qquad
D_k\xi=0.
\]

Let

\[
\boxed{g:=D_\xi\log\rho.}
\]

A critical ribbon is a connected kernel segment on which

\[
\boxed{g\equiv0.}
\]

Then automatically

\[
D_k^jg=0
\]

for every `k` derivative along the segment.

M17-114 shows that this is the analytic limit branch arising when the kernel-direction peak zero count is not uniformly finite.

---

## 2. Instantaneous circular kernel geometry

At every point of the ribbon,

\[
g=0,
\qquad
D_kg=0.
\]

M17-099/M17-110 give

\[
\boxed{\gamma_k=q}
\]

and

\[
\boxed{D_kq=0.}
\]

The kernel-frame equations are

\[
D_kk=\gamma_k n,
\qquad
D_kn=-\gamma_k k,
\]

so on the ribbon

\[
\boxed{
D_kk=q n,
\qquad
D_kn=-q k,
\qquad
D_kq=0.
}
\]

Because `D_k xi=0`, the director `xi` is constant along the kernel curve and the curve lies in a fixed plane normal to `xi`.

Full Rank 2 at `g=0` requires

\[
q\neq0.
\]

Therefore a complete connected ribbon fiber is a plane circle of radius

\[
\boxed{R_k=|q|^{-1}.}
\]

A local ribbon is correspondingly a circular arc.

---

## 3. Material persistence of g=0

At a peak/critical point M17-040 gives

\[
D_Bg=D_\xi(\sigma+\kappa).
\]

For the same material points of the ribbon to remain critical,

\[
D_Bg=0.
\]

Hence persistent ribbon geometry requires

\[
\boxed{
D_\xi(\sigma+\kappa)=0
}
\]

at every point of the ribbon.

This is stronger than the generic fold branch, where this quantity is nonzero and unfolds the tangency.

---

## 4. Exact commutator along the kernel direction

M17-033 gives the material rotation of the transverse frame

\[
D_Bk=\Omega n,
\qquad
D_Bn=-\Omega k,
\]

where

\[
\boxed{\Omega:=\beta_\Sigma+r_W.}
\]

Also

\[
D_kB
=\left(\sigma_k+\frac12\right)k
+\Omega n.
\]

For any scalar `f`, the frame-rotation terms cancel in the directional commutator, giving

\[
\boxed{
D_B(D_kf)
=D_k(D_Bf)
-\left(\sigma_k+\frac12\right)D_kf.
}
\]

This is the kernel analogue of the previously used `xi`-direction commutator.

---

## 5. Material law for kernel-fiber curvature gamma_k

Start from

\[
D_kk=\gamma_kn.
\]

Differentiate materially.
Using

\[
D_Bk=\Omega n
\]

and

\[
D_kB=(\sigma_k+1/2)k+\Omega n,
\]

a direct Euclidean commutator calculation gives

\[
\boxed{
D_B\gamma_k
=D_k\Omega
-\left(\sigma_k+\frac12\right)\gamma_k.
}
\]

---

## 6. Material law for q

Write

\[
b=D_\xi\xi=p k+q n.
\]

M17-031/M17-033 give

\[
D_Bb
=-\left(\sigma+\frac12\right)b.
\]

Resolving in the rotating `(k,n)` frame gives

\[
\boxed{
D_Bq
=-\left(\sigma+\frac12\right)q
-p\Omega.
}
\]

---

## 7. Persistence of the curvature resonance

The ribbon requires

\[
\gamma_k=q
\]

for all material time.
Therefore

\[
D_B(\gamma_k-q)=0.
\]

Use Sections 5--6 and set `gamma_k=q`:

\[
0
=D_k\Omega
-\left(\sigma_k+\frac12\right)q
+\left(\sigma+\frac12\right)q
+p\Omega.
\]

Hence

\[
\boxed{
D_k\Omega
+p\Omega
+(\sigma-\sigma_k)q
=0.
}
\]

This is the first nontrivial material connection compatibility of the persistent circular ribbon.

---

## 8. Material line element on the kernel circle

Let `ds` be arclength on a material kernel line.
Its tangent is `k`.

The material stretching rate is

\[
D_B\log ds
=k\cdot(\nabla B)k
=\sigma_k+\frac12.
\]

Thus

\[
\boxed{
D_B ds
=\left(\sigma_k+\frac12\right)ds.
}
\]

The director-area magnitude satisfies

\[
\boxed{
D_B\log|J_\xi|
=\sigma_k-1.
}
\]

---

## 9. Margin law on the material ribbon

At every ribbon point assume a retained line maximum

\[
C=D_\xi g<0
\]

with positive sub-Riccati margin

\[
\mathcal M_{R2}>0.
\]

Define

\[
N:=N_{R2}=|a|\mathcal M_{R2}>0.
\]

M17-080 gives at the material peak point

\[
\boxed{
D_BN
=-\frac32N
+|a|\mathcal R_{R2}.
}
\]

No `alpha_J` section slide is needed because the entire material kernel fiber remains inside the critical ribbon by hypothesis.

---

## 10. Natural loop inventory and exact homogeneous cancellation

For a complete material ribbon circle define

\[
\boxed{
\mathscr I_{rib}
:=\oint
\frac{N}{|J_\xi|}\,ds.
}
\]

Differentiate a material line integral:

\[
\frac d{d\theta}\mathscr I_{rib}
=
\oint
\left[
D_B\left(\frac{N}{|J_\xi|}\right)
+\left(\sigma_k+\frac12\right)
\frac{N}{|J_\xi|}
\right]ds.
\]

Now

\[
D_B\left(\frac{N}{|J_\xi|}\right)
=
-\left(\sigma_k+\frac12\right)
\frac{N}{|J_\xi|}
+
\frac{|a|}{|J_\xi|}\mathcal R_{R2}.
\]

The homogeneous terms cancel exactly, giving

\[
\boxed{
\frac d{d\theta}\mathscr I_{rib}
=
\oint
\frac{|a|}{|J_\xi|}
\mathcal R_{R2}\,ds.
}
\]

Thus the pointwise `3/2` damping is exactly neutralized by the material line stretching and inverse director-area density in the complete-loop inventory.

---

## 11. Simplify by the peak frame

At `g=0`,

\[
a=rk,
\qquad
b=pk+qn.
\]

Therefore

\[
|a|=|r|
\]

and

\[
|J_\xi|
=|a\times b|
=|rq|.
\]

Hence

\[
\boxed{
\frac{|a|}{|J_\xi|}
=\frac1{|q|}.
}
\]

Because `D_kq=0` on the ribbon, `|q|` is constant around each kernel circle.

Thus

\[
\boxed{
\mathscr I_{rib}
=\frac1{|q|}\oint\mathcal M_{R2}\,ds,
}
\]

and

\[
\boxed{
\frac d{d\theta}\mathscr I_{rib}
=\frac1{|q|}\oint\mathcal R_{R2}\,ds.
}
\]

---

## 12. Recurrent ribbon law

If a complete material critical ribbon is recurrent with bounded positive loop inventory, then its long-time mean drift vanishes and

\[
\boxed{
\left\langle
\frac1{|q|}
\oint\mathcal R_{R2}\,ds
\right\rangle
=0.
}
\]

This is **not** the transverse section law

\[
\langle\text{recharge}\rangle
=\frac32\langle\text{positive margin}\rangle.
\]

The circular ribbon has a different geometric measure that neutralizes the homogeneous three-halves damping.

---

## 13. DSD interpretation

The analytic oscillation limit changes the descriptor support:

\[
\boxed{
\text{transverse isolated peak intersections}
\to
\text{critical ribbon tangent to }J_\xi.
}
\]

Accordingly the natural measure changes from a director-area **cross-section** measure to a material **loop-per-flux** measure.

The disappearance of the `3/2` payment is therefore not a contradiction in previous modules; it is a measure/geometry transition.

---

## 14. DSD audit

### Audit A — applying M17-107's transverse `3/2` recharge law at `D_k g=0` ribbon
Rejected.

### Audit B — counting a continuum of ribbon points as infinitely many independent peaks
Rejected. They belong to one tangent kernel fiber geometry.

### Audit C — claiming local circular arc implies a complete material circle
Restricted: the loop inventory applies only when the ribbon condition extends around a complete connected kernel fiber.

### Audit D — treating zero mean loop recharge as a contradiction
Rejected. It is a compatibility condition.

### Audit E — proof status
The critical ribbon is sharply classified and has its own exact recurrence ledger, but it remains a genuine survivor.

---

## 15. Updated Rank-2 analytic frontier

Away from critical ribbons, analytic compactness supplies a finite peak-total-variation bound and the positive transverse `3/2` recharge ledger.

At the ribbon limit,

\[
\boxed{
\begin{aligned}
&g\equiv0\text{ along a }k\text{-fiber},\\
&k\text{-fiber is circular},\\
&D_\xi(\sigma+\kappa)=0,\\
&D_k\Omega+p\Omega+(\sigma-\sigma_k)q=0,\\
&\left\langle|q|^{-1}\oint\mathcal R_{R2}ds\right\rangle=0.
\end{aligned}
}
\]

The next high-value question is whether a complete circular kernel fiber with a material constant director and full Rank 2 is compatible with the global Euclidean embedding / finite-energy topology of the retained hard branch, or whether such fibers necessarily organize into a forbidden foliation or an allowed toroidal/Hopf-like geometry.

This is the **Circular Kernel Fiber Topology Gate (CKFTG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
