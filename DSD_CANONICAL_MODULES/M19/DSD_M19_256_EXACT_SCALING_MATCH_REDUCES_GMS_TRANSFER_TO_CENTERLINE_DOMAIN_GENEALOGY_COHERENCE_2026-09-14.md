# DSD M19-256 — Exact scaling match reduces GMS transfer to centerline/domain/genealogy coherence

Date: 2026-09-14
Status: CONDITIONAL TRANSFER THEOREM + TRACKING-DECOMPACTIFICATION FIREWALL; NOT A CLOSURE THEOREM
Parent: M19-255

## 0. Goal

M19-255 isolated

\[
\mathcal T_{GMS}^{transfer}
\]

as the first gate required to use the certified M17 ancestry/derivative ledgers against the logarithmically divergent GMS payer.

The purpose of M19-256 is to determine whether the obstruction is dimensional/scaling or geometric/genealogical.

The answer is sharp:

\[
\boxed{
\text{the M17 ancestry exponents exactly match Navier--Stokes parabolic scaling.}
}
\]

Therefore the remaining transfer problem is centerline, domain, overlap, and genealogy coherence.

---

## 1. Exact physical parabolic scaling

Around a spacetime point \(z_0=(x_0,t_0)\), define

\[
u^{(r)}(y,s)
=r\,u(x_0+ry,t_0+r^2s),
\]

\[
\omega^{(r)}(y,s)
=r^2\omega(x_0+ry,t_0+r^2s).
\]

For every integer \(k\ge0\),

\[
\nabla_y^k\omega^{(r)}
=r^{k+2}D_x^k\omega.
\]

Since

\[
dy\,ds=r^{-5}dx\,dt,
\]

we obtain the exact identity

\[
\boxed{
\int_{Q_1}|\nabla_y^k\omega^{(r)}|^2dy\,ds
=
r^{2k-1}
\int_{Q_r}|D_x^k\omega|^2dx\,dt.
}
\]

Equivalently,

\[
\boxed{
\int_{Q_r}|D_x^k\omega|^2dx\,dt
=
r^{1-2k}
\int_{Q_1}|\nabla_y^k\omega^{(r)}|^2dy\,ds.
}
\]

This is exactly the M17 ancestry factor

\[
\boxed{r^{1-2k}}.
\]

In particular,

\[
k=1:\quad r^{-1},
\qquad
k=2:\quad r^{-3},
\qquad
k=3:\quad r^{-5}.
\]

Thus there is no hidden exponent mismatch between the M17 derivative ledgers and the physical parabolic windows required by the GMS route.

---

## 2. Consequence for the M19-255 high-frequency estimate

M19-255 gave, at scale \(r\),

\[
r^{-5/3}
\int_{I_r}\|u_{>r^{-1}}\|_{10/3}^{10/3}dt
\lesssim
B_{-1}^{2/3}
\,r^{1/3}
\int_{I_r}\|\nabla\omega\|_2^2dt.
\]

Once an M17 record window and its physical scale \(r\) are identified with the corresponding Galilean parabolic window, the certified \(k=1\) ancestry ledger supplies precisely the correctly scaled palinstrophy currency. No additional scale exponent must be manufactured.

Hence the high-frequency obstruction is not dimensional.

---

## 3. What transfer actually requires

Let \(I_m\) be an M17 record/material time window at physical scale \(r_m\), and let \(X_m(t)\) denote its physical center or the center inherited from the same material genealogy.

For a fixed Galilean velocity \(V\), define the target centerline

\[
a_V(t)=x_0+V(t-t_0)
\]

and the normalized tracking defect

\[
\boxed{
\Theta_m(V)
:=
r_m^{-1}
\sup_{t\in I_m}
|X_m(t)-a_V(t)|.
}
\]

A bounded transfer requires, up to fixed enlargement constants:

1. \(|I_m|\asymp r_m^2\);
2. \(\sup_m\Theta_m(V)<\infty\) for one fixed \(V\);
3. the M17 spatial record domains contain or are uniformly comparable to the required Galilean balls/shells;
4. the mapped windows have the bounded-overlap/nonreuse property used by the certified ancestry ledger;
5. all windows belong to the same physical singular genealogy, with no unrecorded interface/rank/domain exit.

Under these conditions the exact scaling identity in Section 1 transfers the M17 derivative ledger to the GMS dyadic family.

---

## 4. Conditional transfer theorem

Assume there exists a fixed \(V\in\mathbb R^3\) and a scale sequence \(r_m\downarrow0\) satisfying the five coherence conditions above.

Then the M17 palinstrophy ancestry ledger transfers to the same physical Galilean scale family. Consequently

\[
\boxed{
\sum_m
r_m^{-5/3}
\int_{I_m}
\|u_{>r_m^{-1}}\|_{10/3}^{10/3}dt
<\infty.
}
\]

Thus, under transfer coherence,

\[
\boxed{
\text{the high-frequency velocity sector cannot be the source of }
\mathcal P_{GMS}^{log}(V)=\infty.
}
\]

The surviving GMS divergence must be carried by the low-frequency velocity sector, the pressure sector not yet reduced to velocity, or by failure of the transfer-coherence hypotheses themselves.

---

## 5. Tracking decompactification

Failure of centerline coherence for every fixed Galilean frame defines a new typed survivor:

\[
\boxed{
\mathcal E_{track}:
\quad
\forall V\in\mathbb R^3,
\qquad
\limsup_{m\to\infty}\Theta_m(V)=\infty.
}
\]

This is not a wall/cavity phenomenon. It is a whole-space scale-dependent translation/tracking decompactification.

If the record centers arise from a single material curve \(X(t)\), a sufficient scale-wise condition for bounded tracking on \(I_m\) is

\[
\sup_{t\in I_m}|\dot X(t)-V|
\lesssim r_m^{-1},
\]

because \(|I_m|\asymp r_m^2\) then gives displacement \(O(r_m)\). This sufficient condition is intentionally weak and does not by itself produce a common fixed \(V\).

The high-frequency derivative ledgers do not control \(\mathcal E_{track}\) automatically. Translation of the center is a low-frequency/geometric degree of freedom.

---

## 6. Fixed-V firewall

At each scale one may be able to choose an optimizing velocity \(V_m\). That is not enough for M19-254.

The logarithmic Tonelli identity and the singularity necessity statement are formulated for one fixed Galilean centerline. Therefore

\[
\boxed{
\text{scale-wise selectable }V_m
\not\Rightarrow
\text{one fixed }V\text{ with finite }\mathcal P_{GMS}^{log}(V).
}
\]

A compactness, averaging, or coherence theorem is required to extract a single fixed \(V\), or the failure must be retained as \(\mathcal E_{track}\).

---

## 7. Transfer gate after M19-256

The dimensional part of \(\mathcal T_{GMS}^{transfer}\) is closed:

\[
\boxed{
\text{M17 ancestry weight}=\text{exact physical parabolic derivative weight}.
}
\]

The remaining transfer gate is

\[
\boxed{
\mathcal T_{GMS}^{coh}:
\text{fixed-}V\text{ centerline coherence}
+
\text{domain comparability}
+
\text{bounded-overlap genealogy alignment}.
}
\]

Conditional implication:

\[
\boxed{
\mathcal T_{GMS}^{coh}
\Longrightarrow
\text{high-frequency GMS payer finite}.
}
\]

Failure splits into a finite list of typed exits:

\[
\boxed{
\mathcal E_{track}
\lor
\mathcal E_{domain}
\lor
\mathcal E_{overlap}
\lor
\mathcal E_{genealogy}.
}
\]

These exits must not be silently identified with singularity exclusion.

---

## 8. New permanent firewalls

\[
\boxed{
\text{exact scaling-exponent match}
\not\Rightarrow
\text{physical GMS transfer without center/domain/genealogy coherence}.}
\]

\[
\boxed{
\text{bounded high-frequency derivative ledger}
\not\Rightarrow
\text{bounded centerline drift}.}
\]

\[
\boxed{
\text{scale-wise Galilean optimization}
\not\Rightarrow
\text{fixed-frame logarithmic control}.}
\]

---

## 9. Next target

The next calculation should test whether \(\mathcal E_{track}\) can itself be reduced to the existing low-frequency currency \(B_{-1}\), or whether a fixed \(V\) can be extracted from the record-center genealogy by an averaging/compactness argument. In parallel, the weighted Calderón--Zygmund pressure reduction should be audited because, if uniform in the parabolic truncation parameter, it may remove \(\mathcal T_{GMS}^{press}\) as an independent gate.

Global regularity remains unproved.
