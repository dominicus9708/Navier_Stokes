# DSD M19-257 — Record-to-physical-shell transfer requires scale-comparable bounded reuse, field matching, pressure matching, and root eligibility

Date: 2026-09-15  
Status: **CONDITIONAL TRANSFER THEOREM / INTERFACE AUDIT / NOT A CLOSURE THEOREM**  
Parent: M19-256

## 0. Goal

M19-256 closed the dimensional question: the physical parabolic scaling of the raw-vorticity \(H^2\) quantity is exactly \(r^{-3}\), matching the certified M17 ancestry weight. What remains is not an exponent problem but an interface problem.

The purpose of M19-257 is to state the weakest explicit contract under which the certified M17 record ledger

\[
\sum_m R_m^{-3}H_m^{rec}<\infty
\]

can be transferred to the physical dyadic shells around a hypothetical singular point,

\[
\sum_j r_j^{-3}H_j^{phys}<\infty,
\]

which is the input required by M19-255--256 to make the Galilean logarithmic payer finite.

Global regularity remains unproved.

---

## 1. Physical dyadic shells

Fix a hypothetical singular point \(z_0=(x_0,t_0)\), a constant Galilean velocity \(V\), and dyadic radii

\[
r_j=2^{-j}r_0.
\]

Let

\[
Q_j^V:=Q_{r_j}^V(z_0),
\qquad
A_j^V:=Q_j^V\setminus Q_{j+1}^V.
\]

M19-256 reduces the weighted GMS problem to a physical shell ledger at the raw-\(H^2\) vorticity / \(D^3u\) level. Denote the required nonnegative shell cost by

\[
H_j^{phys}.
\]

The precise localized realization may include cutoff/commutator terms, but the target summability is

\[
\boxed{
\sum_j r_j^{-3}H_j^{phys}<\infty.
}
\]

---

## 2. M17 record ledger

For the retained M17 genealogy, write the certified raw-\(H^2\) record costs as

\[
H_m^{rec}\ge0,
\qquad R_m>0,
\]

with

\[
\boxed{
\sum_m R_m^{-3}H_m^{rec}<\infty.
}
\]

This statement is record/genealogy based. It does **not** by itself assert that arbitrary physical parabolic shells around an arbitrary singular point are covered by the same records.

---

## 3. Exact transfer contract

For every sufficiently large physical shell index \(j\), choose a finite set of records \(\mathcal M(j)\). The following four conditions are sufficient.

### 3.1 Scale comparability

There exists \(\Lambda\ge1\) such that

\[
\boxed{
\Lambda^{-1}r_j\le R_m\le\Lambda r_j,
\qquad m\in\mathcal M(j).
}
\]

This prevents a physical shell at scale \(r_j\) from being paid only by records at parametrically different scales.

### 3.2 Field domination

There exists \(C_{field}<\infty\) such that the physical localized velocity/vorticity cost obeys

\[
\boxed{
H_{j,vel}^{phys}
\le C_{field}\sum_{m\in\mathcal M(j)}H_m^{rec}.
}
\]

This is where localized Biot--Savart/elliptic estimates, cutoffs, and commutator terms must be certified. The identity \(D^2\omega\simeq D^3u\) is an order-counting guide, not by itself a local elliptic estimate.

### 3.3 Pressure domination

The pressure part required by the GMS payer must be controlled without an independent unbudgeted source. Write its shell cost as \(H_{j,p}^{phys}\). Require

\[
\boxed{
H_{j,p}^{phys}
\le C_{press}
\left(
\sum_{m\in\mathcal M(j)}H_m^{rec}
+H_{j,low}^{phys}
\right),
}
\]

where the lower-order term \(H_{j,low}^{phys}\) is already summable from the whole-space finite-energy/localized low-frequency budget. Equivalently one may absorb this term into \(H_j^{phys}\) once its summability is proved.

The natural audit is the local/nonlocal decomposition of

\[
-\Delta p=\partial_i\partial_j(u_i u_j),
\]

with the near field controlled by Calderón--Zygmund and the far field treated as harmonic on the inner shell.

### 3.4 Bounded reuse / overlap

There exists \(N<\infty\) such that every record is used by at most \(N\) physical shells:

\[
\boxed{
\#\{j:m\in\mathcal M(j)\}\le N.
}
\]

This is stronger than saying the M17 record intervals have bounded overlap inside their own genealogy. It is a statement about the new map from physical shells to records.

---

## 4. Algebraic transfer theorem

Assume 3.1--3.4 and that the lower-order physical terms are summable with the same weight. Then

\[
\begin{aligned}
\sum_j r_j^{-3}H_j^{phys}
&\le C
\sum_j\sum_{m\in\mathcal M(j)}r_j^{-3}H_m^{rec}
+
C\sum_jr_j^{-3}H_{j,low}^{phys}\\
&\le C\Lambda^3
\sum_j\sum_{m\in\mathcal M(j)}R_m^{-3}H_m^{rec}
+
C\sum_jr_j^{-3}H_{j,low}^{phys}\\
&\le C\Lambda^3N
\sum_mR_m^{-3}H_m^{rec}
+
C\sum_jr_j^{-3}H_{j,low}^{phys}\\
&<\infty.
\end{aligned}
\]

Therefore

\[
\boxed{
\text{scale-comparable cover}
+\text{field match}
+\text{pressure match}
+\text{bounded reuse}
\Longrightarrow
\text{physical }r^{-3}\text{ raw-H2 ledger}.
}
\]

Combined with M19-255--256,

\[
\boxed{
\mathcal T_{GMS}^{record}
\Longrightarrow
\mathcal P_{GMS}^{log}(V)<\infty.
}
\]

M19-254 says a genuine singular point requires \(\mathcal P_{GMS}^{log}(V)=\infty\) for every fixed \(V\). Hence the entered branch closes if the transfer contract is actually verified.

---

## 5. Root/eligibility gate is logically separate

Even a perfect record-to-shell transfer inside the retained CE-H genealogy does not show that an arbitrary hypothetical singular point enters that genealogy.

Define

\[
\boxed{
\mathcal T_{GMS}^{root}:
\text{the hypothetical singular point enters an M17-eligible retained genealogy
with the hypotheses needed by the raw-H2 ledger}.}
\]

This includes the unresolved `ROOT-CERT`, parent-to-M17 persistence, and branch/interface assumptions. It must not be hidden inside the analytic transfer theorem.

Thus the current whole-space GMS branch decomposes into

\[
\boxed{
\mathcal T_{GMS}^{cover},
\quad
\mathcal T_{GMS}^{field},
\quad
\mathcal T_{GMS}^{press},
\quad
\mathcal T_{GMS}^{root}.
}
\]

Here `cover` includes scale comparability, physical-domain coverage, center coherence, and bounded reuse/nonoverlap.

---

## 6. Relation to M19-256 exit taxonomy

M19-256 typed transfer failure as

\[
\mathcal E_{track}
\lor\mathcal E_{domain}
\lor\mathcal E_{coverage}
\lor\mathcal E_{overlap}
\lor\mathcal E_{genealogy}
\lor\mathcal E_{interface}.
\]

M19-257 reorganizes these failures by proof obligation:

- \(\mathcal T_{GMS}^{cover}\): excludes \(\mathcal E_{track},\mathcal E_{domain},\mathcal E_{coverage},\mathcal E_{overlap}\) at the physical-shell level;
- \(\mathcal T_{GMS}^{field}\): controls the PDE/elliptic content of \(\mathcal E_{interface}\);
- \(\mathcal T_{GMS}^{press}\): controls the nonlocal pressure part of \(\mathcal E_{interface}\);
- \(\mathcal T_{GMS}^{root}\): excludes the relevant \(\mathcal E_{genealogy}\) and upstream branch-entry failure.

This is a decomposition, not a proof that the exits are absent.

---

## 7. New permanent firewalls

\[
\boxed{
\text{matching ancestry exponent }R^{-3}
\not\Rightarrow
\text{physical-shell coverage/control}.
}
\]

\[
\boxed{
\text{bounded overlap inside the record genealogy}
\not\Rightarrow
\text{bounded reuse under the physical-shell cover}.
}
\]

\[
\boxed{
\text{vorticity raw-H2 ledger}
\not\Rightarrow
\text{localized velocity }D^3u\text{ ledger without elliptic cutoff/commutator control}.
}
\]

\[
\boxed{
\text{local velocity transfer}
\not\Rightarrow
\text{weighted pressure transfer}.
}
\]

\[
\boxed{
\text{closure of an M17-eligible CE-H/GMS branch}
\not\Rightarrow
\text{ROOT-CERT or non-CE-H closure}.
}
\]

---

## 8. Next calculation

The most local analytic gate is \(\mathcal T_{GMS}^{field}\). The next module should derive a cutoff-stable elliptic estimate on nested physical balls/cylinders, schematically of the form

\[
\|D^3u\|_{L^2(B_r)}
\lesssim
\|D^2\omega\|_{L^2(B_{2r})}
+r^{-1}\|D\omega\|_{L^2(B_{2r})}
+r^{-2}\|\omega\|_{L^2(B_{2r})}
+r^{-3}\|u\|_{L^2(B_{2r})},
\]

with the exact derivative orders and divergence-free/localization commutators audited before use.

If this estimate survives with lower-order terms already paid by certified ledgers, the field gate can be removed and the pressure gate becomes the next local analytic target.

Global regularity remains unproved.
