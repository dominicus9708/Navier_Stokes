# DSD M19-256 — Exact scaling match reduces GMS transfer to centerline/domain/coverage/genealogy coherence

Date: 2026-09-14
Status: CONDITIONAL TRANSFER-CLOSURE THEOREM + TRACKING/COVERAGE FIREWALL; NOT GLOBAL CLOSURE
Parent: M19-255

## 0. Goal

Corrected M19-255 shows that physical

\[
D^3u\in L^2_{x,t}
\]

on the required Galilean neighborhood implies

\[
u\in L^6_{x,t},\qquad p\in L^3_{x,t},\qquad \mathcal P_{GMS}^{log}(V)<\infty,
\]

contradicting the M19-254 singularity necessity.

Thus the only analytic bridge left on this lane is to transfer the certified M17 raw-H2 ancestry currency to the same physical neighborhood.

---

## 1. Exact Navier--Stokes parabolic scaling

Around \(z_0=(x_0,t_0)\), define

\[
u^{(r)}(y,s)=r\,u(x_0+ry,t_0+r^2s),
\]

\[
\omega^{(r)}(y,s)=r^2\omega(x_0+ry,t_0+r^2s).
\]

For every integer \(k\ge0\),

\[
\nabla_y^k\omega^{(r)}=r^{k+2}D_x^k\omega,
\qquad dy\,ds=r^{-5}dx\,dt.
\]

Therefore

\[
\boxed{
\int_{Q_1}|\nabla_y^k\omega^{(r)}|^2dy\,ds
=
r^{2k-1}
\int_{Q_r}|D_x^k\omega|^2dx\,dt,
}
\]

or equivalently

\[
\boxed{
\int_{Q_r}|D_x^k\omega|^2dx\,dt
=
r^{1-2k}
\int_{Q_1}|\nabla_y^k\omega^{(r)}|^2dy\,ds.
}
\]

The M17 ancestry factor \(r^{1-2k}\) is therefore exactly the physical parabolic derivative weight.

In particular,

\[
k=1:\ r^{-1},\qquad
k=2:\ r^{-3},\qquad
k=3:\ r^{-5}.
\]

For the M19-255 threshold, \(k=2\) on vorticity is the relevant case because

\[
D^2\omega\simeq D^3u.
\]

Thus the M17 \(r^{-3}\) raw-H2 ancestry weight has exactly the exponent required for physical \(D^3u\)-energy after rescaling.

---

## 2. What is now closed and what is not

The dimensional/scaling part of \(\mathcal T_{GMS}^{transfer}\) is closed:

\[
\boxed{
\text{M17 raw-H2 ancestry exponent}
=
\text{physical }D^3u\text{ parabolic transfer exponent}.}
\]

There is no missing power of \(r\).

Therefore a failure of transfer cannot be blamed on dimensional mismatch. It must occur through physical placement/coverage or genealogy.

---

## 3. Physical coherence conditions

Let \(I_m\) and \(\mathcal R_m(t)\) denote the physical time window and spatial record domain corresponding to an M17 raw-H2 record at scale \(r_m\downarrow0\).

To infer the physical estimate needed by M19-255, it is sufficient to certify a fixed Galilean cylinder/neighborhood \(Q_{r_0}^V(z_0)\) with a dyadic decomposition such that:

1. **time-scale coherence:** \(|I_m|\asymp r_m^2\);
2. **domain coverage:** the required Galilean dyadic shell/window at scale \(r_m\) is contained in a fixed enlargement of \(\mathcal R_m\), or is covered by uniformly finitely many certified record domains;
3. **bounded overlap/nonreuse:** physical points/events are charged only with the multiplicity allowed by the M17 ledger;
4. **same genealogy/representation:** the normalized raw-H2 record being pulled back belongs to the same physical singular genealogy and no unrecorded interface/rank/domain transition occurs;
5. **center coherence when moving record centers are used:** their displacement from one fixed Galilean centerline remains \(O(r_m)\).

The fifth condition is not needed as a separate axiom if domain coverage is already certified in a center-independent way; it is an explicit diagnostic when the M17 records are material/moving-centered.

---

## 4. Centerline diagnostic

If the M17 physical record is centered at \(X_m(t)\), define for fixed \(V\)

\[
a_V(t)=x_0+V(t-t_0),
\]

\[
\boxed{
\Theta_m(V)
:=r_m^{-1}\sup_{t\in I_m}|X_m(t)-a_V(t)|.
}
\]

Uniform boundedness of \(\Theta_m(V)\) gives scale-compatible center placement after a fixed spatial enlargement.

Failure for every fixed frame is the typed exit

\[
\boxed{
\mathcal E_{track}:
\forall V\in\mathbb R^3,
\quad
\limsup_{m\to\infty}\Theta_m(V)=\infty.
}
\]

Scale-dependent choices \(V_m\) do not replace a fixed-frame coverage theorem:

\[
\boxed{
\text{scale-wise }V_m
\not\Rightarrow
\text{one fixed Galilean neighborhood carrying the transferred raw-H2 bound}.}
\]

---

## 5. Conditional transfer-closure theorem

Assume the M17 \(r_m^{-3}\) raw-H2 ancestry ledger is representation-safe and the physical coherence conditions of Section 3 hold for a Galilean neighborhood of \(z_0\).

The exact scaling identity gives

\[
\int_{Q_{r_0}^V(z_0)}|D^2\omega|^2dxdt<\infty
\]

(up to the certified finite overlap and fixed-enlargement constants). Hence

\[
D^3u\in L^2(Q_{r_0}^V).
\]

M19-255 then yields

\[
u\in L^6(Q_{r_0}^V),
\qquad
p\in L^3(Q_{r_0}^V),
\]

and therefore

\[
\boxed{\mathcal P_{GMS}^{log}(V)<\infty.}
\]

But M19-254 requires \(\mathcal P_{GMS}^{log}(V)=\infty\) at every genuine singular point. Therefore

\[
\boxed{
\mathcal T_{GMS}^{coh}
+\text{certified M17 raw-H2 ledger}
\Longrightarrow
\text{no singularity on this entered branch}.}
\]

This is a conditional closure of the analytic GMS branch, not yet a global Navier--Stokes proof.

---

## 6. Exact remaining transfer exits

The residual bridge is now typed as

\[
\boxed{
\mathcal T_{GMS}^{coh}:
\text{physical domain coverage}
+\text{bounded overlap/nonreuse}
+\text{same genealogy/representation}
+\text{center coherence when required}.}
\]

Failure must be recorded as one of

\[
\boxed{
\mathcal E_{track}
\lor
\mathcal E_{domain}
\lor
\mathcal E_{coverage}
\lor
\mathcal E_{overlap}
\lor
\mathcal E_{genealogy}
\lor
\mathcal E_{interface}.
}
\]

These exits are not contradictions. They are the only remaining ways, on this lane, for the already-certified raw-H2 currency to fail to reach the physical GMS neighborhood.

---

## 7. Permanent firewalls

\[
\boxed{
\text{exact scaling match}
\not\Rightarrow
\text{domain coverage}.}
\]

\[
\boxed{
\text{finite normalized/ancestral raw-H2 ledger}
\not\Rightarrow
\text{physical neighborhood }D^3u\in L^2
\text{ without representation-safe transfer}.}
\]

\[
\boxed{
\text{conditional closure of the entered GMS branch}
\not\Rightarrow
\text{ROOT-CERT or closure of non-CE-H roots}.}
\]

---

## 8. Next target

The next calculation should audit the existing M17 record construction itself against the six transfer exits above. Highest priority:

\[
\boxed{
\text{Does the certified raw-H2 ancestry ledger actually cover a full shrinking physical neighborhood of the candidate singular point, with bounded multiplicity?}
}
\]

If yes, M19-254--256 close this entered whole-space branch immediately. If not, the first failing transfer exit becomes the next explicit survivor to analyze.

Global regularity remains unproved.
