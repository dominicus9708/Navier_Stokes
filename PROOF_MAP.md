# Proof / verification map — current audited route

Date: 2026-08-26

This file is the **current proof ledger** for the DSD-assisted 3D incompressible Navier–Stokes project.
Older exploratory routes remain in Git history and dated notes, but they are not independent terminal proof branches unless explicitly listed here.

## Final status

\[
\boxed{\text{GLOBAL REGULARITY OF 3D NAVIER--STOKES REMAINS UNPROVED.}}
\]

The current work has reduced the retained W1 singular corridor to one large weak-critical endpoint and proved one continuation/absorption lemma.
The reverse critical-tail-tightness implication is still open.

Primary references:

- `DSD_NAVIER_STOKES_FINAL_CLOSURE_AUDIT_2026-08-26.md`
- `DSD_W1_CRITICAL_HIGH_AMPLITUDE_TAIL_ABSORPTION_LEMMA_2026-08-26.md`
- `DSD_W1_INTERIOR_BOUNDARY_DECOUPLING_AND_UNIFORM_NO_DEFECT_TARGET_2026-08-26.md`
- `DSD_W1_WEAK_L3_DISTRIBUTION_DEFECT_EQUIVALENCE_2026-08-26.md`
- GitHub Issue #2: `Final endpoint: prove critical K-tail tightness or equivalent pump absorption`

---

## Status vocabulary

- **STANDARD INPUT** — standard Navier–Stokes/Leray/suitable-solution fact used as input.
- **DERIVED IDENTITY** — exact algebra/calculus identity under the stated class.
- **DERIVED LEMMA** — internally proved analytic lemma under stated hypotheses.
- **W1-CONDITIONAL** — proved inside the retained W1 recurrent corridor; not yet a theorem for every possible finite-time singularity.
- **DIAGNOSTIC** — useful structural information but not an independent closure obligation.
- **SUPERSEDED / INVALID SHORTCUT** — explicitly rejected by audit.
- **OPEN MILLENNIUM-LEVEL BRIDGE** — genuinely unresolved implication needed for unconditional closure.
- **FINAL AUDIT REQUIRED** — must be rechecked after the open bridge is solved before any global-regularity claim.

---

# A. Standard problem

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad
\nabla\cdot u=0,
\qquad
x\in\mathbb R^3,
\qquad
\nu>0,
\qquad
f=0.
\]

DSD does not modify this PDE. It is used only to keep domains, state boundaries, channels, limit operations, and causal/representational distinctions explicit.

Status: **STANDARD INPUT**.

---

# B. Retained W1 corridor

The late blow-up analysis uses a recurrent W1 corridor with the previously recorded assumptions and compactness/tail hypotheses.
Inside this corridor the omega-limit contains a compact minimal recurrent set and a nontrivial critical endpoint.

The current proof map does **not** claim, without a final branch-completeness audit, that every conceivable finite-time singularity has already been reduced to W1.
Therefore:

\[
\boxed{
\text{W1 closure} \neq \text{global regularity until upstream branch completeness is re-audited.}
}
\]

Status: **W1-CONDITIONAL REDUCTION**.

---

# C. Endpoint quantity: critical cubic residue

On the retained recurrent W1 endpoint, the audited critical residue is

\[
\boxed{\mathscr R_3>0.}
\]

Its robust general definition is Abel/Mellin in nature, schematically

\[
\mathscr R_3
=
\lim_{\varepsilon\downarrow0}
\varepsilon
\left\langle
\int |U|^{3+\varepsilon}\,dY
\right\rangle_\mu.
\]

The general aperiodic lane must **not** automatically identify this with a pointwise limit of

\[
\lambda^3|\{|U|>\lambda\}|.
\]

That upgrade needs a Tauberian/regular-variation hypothesis.

Status: **W1-CONDITIONAL ENDPOINT + AUDITED TAUBERIAN CAUTION**.

---

# D. Exact boundary coordinate: truncated critical energy

Define

\[
\mathcal E_\lambda(U)
:=
\frac12\int_{\mathbb R^3}(|U|^2-\lambda^2)_+\,dY,
\]

\[
\boxed{
K(U;\lambda)
:=
\lambda\mathcal E_\lambda(U).
}
\]

This coordinate does not require the pointwise weak-`L3` distribution limit.
Invariant averaging on W1 gives

\[
\boxed{
\lim_{\lambda\downarrow0}
\langle K(U;\lambda)\rangle_\mu
=
\frac{\mathscr R_3}{3}>0.
}
\]

Thus the surviving normalized state has a positive critical boundary defect in the exact `K` sense.

Status: **DERIVED W1-CONDITIONAL IDENTITY**.

---

# E. Exact amplitude-state transport

For almost every regular amplitude level,

\[
\boxed{
\partial_s\mathcal E_\lambda
-\frac12\partial_\lambda(\lambda\mathcal E_\lambda)
+\nu D_\lambda
=J_P(\lambda),
}
\]

where `D_lambda>=0` is the thresholded viscous cost and `J_P(lambda)` is the gauge-independent pressure work through the velocity-magnitude level surface.

Equivalently,

\[
\boxed{
\partial_sK
-\frac\lambda2\partial_\lambda K
=
\lambda(J_P-\nu D_\lambda).
}
\]

The amplitude characteristic is

\[
\boxed{\lambda'(s)=-\lambda/2,}
\]

which corresponds exactly to one fixed physical velocity threshold.

Status: **DERIVED IDENTITY**.

---

# F. DSD interior/boundary separation

The current state description is:

### Interior

Finite normalized amplitude/finite-parent structures, including pressure work, `D3` dissipation, amplitude BMO oscillation, direction deformation, vorticity stretching, and strain diagnostics.

### Boundary

The critical `K` defect at normalized amplitude zero/spatial infinity.

### Joint projective boundary

The critical endpoint sits on

\[
\boxed{\lambda |Y|=O(1),}
\]

which is the amplitude-space form of the `1/r` critical geometry.

Therefore the boundary defect is not treated as an ex-nihilo source. It has a describable amplitude-state formation path.

Status: **DSD STRUCTURAL REDUCTION**.

---

# G. Retired terminal branches

The following are retained as diagnostics/internal realization classes but are **not separate final proof obligations**:

- periodic versus aperiodic recurrence;
- `H2` coherent versus derivative-escalating tail behavior;
- middle/top strain subbranches;
- maximum-vorticity contact geometry;
- Bernoulli versus pressure-free vorticity current descriptions;
- turnover/material-export subcases;
- Lamb/Hodge projection descriptions;
- finite-core pressure-pump geometry.

They all feed the same large weak-critical W1 endpoint.

Status: **DIAGNOSTIC / SUBSUMED**.

---

# H. Completed continuation lemma

For a smooth physical solution on `(t0,T*)`, fix `L>0` and split

\[
u=v_L+w_L,
\]

\[
v_L=u\mathbf1_{|u|\le L},
\qquad
w_L=u\mathbf1_{|u|>L}.
\]

The repository proves that there exists a viscosity-dependent threshold `epsilon_nu>0` such that

\[
\boxed{
\sup_{t_0<t<T_*}
\|w_L(t)\|_{L^{3,\infty}}
<\varepsilon_\nu
}
\]

for one finite `L` implies uniform `H1` control and continuation past `T*`.

Thus

\[
\boxed{
\text{small high-amplitude weak-}L^3\text{ tail}
\Longrightarrow
\text{regularity}.
}
\]

Status: **DERIVED LEMMA — COMPLETED**.

Reference: `DSD_W1_CRITICAL_HIGH_AMPLITUDE_TAIL_ABSORPTION_LEMMA_2026-08-26.md`.

---

# I. `K` and the physical high-amplitude tail

Define

\[
K_L^{phys}(t)
:=
\frac L2\int(|u|^2-L^2)_+\,dx.
\]

The Leray/physical correspondence is exact:

\[
\boxed{
K(U(s);L\sqrt{T_*-t})
=
K_L^{phys}(t).
}
\]

The repository also derives quantitative comparison between `K_L^{phys}` and the high-amplitude weak-`L3` distribution tail.
Hence critical `K`-tail tightness is an equivalent/sufficient route into the completed absorption lemma.

Status: **DERIVED LEMMA/IDENTITY**.

---

# J. Single live endpoint bridge

The principal unresolved implication is

\[
\boxed{
\text{finite-energy Navier--Stokes + retained W1/prelimit structure}
\stackrel{?}{\Longrightarrow}
\text{uniform critical high-amplitude tail tightness}.
}
\]

A sufficient form is

\[
\boxed{
\lim_{L\to\infty}
\sup_{t_0<t<T_*}
K_L^{phys}(t)=0
}
\]

on some terminal interval.

Equivalently, it is enough to prove one of:

1. a high-amplitude weak-`L3` tail eventually below the absorption threshold;
2. defect-aware late compactness controlling `K`;
3. pressure-pump absorption on the strict interior amplitude band;
4. a strong-critical upgrade to a known continuation class;
5. direct exclusion of the large weak-critical recurrent W1 ancient class.

Finite `L2` energy and ordinary dissipation alone do not yield this implication.

Status: **OPEN MILLENNIUM-LEVEL BRIDGE**.

Tracked in GitHub Issue #2.

---

# K. Major invalid shortcuts — do not reopen

The following routes were explicitly audited and must not be reused without new hypotheses:

| Shortcut | Audit result |
|---|---|
| Uniform weak-`L3` contradicts logarithmic cubic concentration | False; the two are compatible |
| Similarity-radial current is material turnover | False |
| Periodic omega-limit tail automatically transfers to the original parent on fixed physical annuli | False without a diagonal convergence rate |
| `R3/6` is a new physical power source | False; it is a normalized amplitude-boundary term |
| Large `H2` capacity is the actual reformation action | False |
| Mellin/Abel residue automatically equals `lim lambda^3 N(lambda)` | False without Tauberian regularity |
| Pointwise sign of pressure is physically/gauge invariant | False; use gradients, differences, or level-set work |
| Infinite normalized events automatically violate finite physical energy | False for positive scaling exponent costs |

Status: **SUPERSEDED / INVALID SHORTCUTS**.

---

# L. What would count as completion

### Step 1 — endpoint bridge

Resolve GitHub Issue #2 by proving one valid closure route under the retained hypotheses.

### Step 2 — W1 contradiction

Use that theorem to force

\[
\mathscr R_3=0
\]

or continuation, contradicting the nontrivial W1 endpoint.

### Step 3 — upstream branch-completeness audit

Re-run the route from an arbitrary finite-time blow-up assumption and verify that no singular lane escapes the W1 reduction.

### Step 4 — external theorem audit

Check exact hypotheses, constants, domains, pressure gauges, limit order, compactness topology, and all Tauberian claims.

### Step 5 — only then consider a global claim

Until Steps 1–4 are complete,

\[
\boxed{\text{GLOBAL REGULARITY IS NOT CLAIMED.}}
\]

---

# M. Current one-line proof ledger

\[
\boxed{
\begin{array}{c}
\text{candidate blow-up}\
\Downarrow\quad\text{(upstream completeness still to be finally audited)}\\
\text{retained recurrent W1 corridor}\
\Downarrow\\
\mathscr R_3>0\ \Longleftrightarrow\ \text{positive critical }K\text{ boundary defect}\
\Downarrow\\
\text{large high-amplitude weak-critical tail}\
\Downarrow\\
\textbf{OPEN: prove uniform tail tightness / pump absorption}\
\Downarrow\\
\text{completed }H^1\text{ absorption lemma}\
\Downarrow\\
\text{continuation, hence contradiction to }T_*.
\end{array}
}
\]

This is the only live top-level route in the repository as of 2026-08-26.