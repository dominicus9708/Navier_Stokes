# DSD M5-277 — Compactness-Failure Collapse to Existing H/T Exits

Date: 2026-08-30

Parent: `DSD_M5_276_WEAK_L3_NO_H_NO_T_TO_ALBRITTON_BARKER_MASTER_REDUCTION_2026-08-30.md`

Status: **MASTER-TREE PRUNING / `C_fail` IS NOT AN INDEPENDENT THIRD TERMINAL BRANCH ON THE AUDITED FIRST-HITTING TREE / GLOBAL ENSTROPHY ESCAPE DOES NOT BREAK LOCAL COMPACTNESS WHEN MORREY HOLDS / MORREY FAILURE IS THE CAMPANATO/TURNOVER EXIT, CENTER NON-NESTING IS THE CENTER-TURNOVER EXIT, LOSS OF STRONG LOCAL VORTICITY/DERIVATIVE PASSAGE IS AN H EXIT, AND LOSS OF BACKWARD TOWER LENGTH IS ALREADY A RATE H/T EXIT / THEREFORE THE POST-LIOUVILLE MASTER FRONTIER REDUCES TO H OR T / GLOBAL REGULARITY UNPROVED BECAUSE H AND T THEMSELVES ARE NOT YET EXCLUDED.**

---

## 1. Starting frontier

M5-276 reduced every hypothetical singular tower to

\[
\boxed{
H_{freq}
\lor
T_{Campanato}
\lor
C_{fail},
}
\]

where `C_fail` was deliberately left as a catch-all for failure of the complete nontrivial ancient extraction.

The purpose of this note is to audit that catch-all against the compactness work already present in the repository.

---

## 2. Global enstrophy divergence is not a compactness failure

`ANCIENT_LOCAL_COMPACTNESS_FROM_MORREY_WITHOUT_GLOBAL_Z_2026-08-24.md` proved that the global normalized enstrophy

\[
Z_j=\int_{\mathbb R^3}|\Omega_j|^2
\]

need not be uniformly bounded.

On the centered Morrey corridor

\[
\boxed{
\rho^{-1}\int_{B_\rho}|U_j|^2\le M_*
}
\]

and with the first-hitting vorticity cap

\[
\|\Omega_j\|_\infty\le1,
\]

one obtains on every fixed cylinder uniform local bounds for

\[
A,\quad E,\quad C,\quad D.
\]

The mechanism is:

1. Morrey gives local `A`;
2. near/far strain splitting plus the vorticity cap gives local `E`;
3. local Sobolev interpolation gives `C`;
4. local/far pressure splitting gives `D`.

Therefore suitable-solution compactness yields an ancient local solution even if

\[
Z_j\to\infty.
\]

Hence

\[
\boxed{
Z_j\uparrow\infty
\not\Rightarrow C_{fail}.
}
\]

Remote diffuse enstrophy is a rigidity/tail issue, not a local compactness obstruction, as long as the Morrey corridor persists.

---

## 3. Morrey failure is already T/Campanato

The same compactness theorem isolates the only local-energy alternative:

\[
\boxed{
\text{Morrey holds}
\quad\lor\quad
\text{local energy / Campanato corridor fails}.
}
\]

The latter is precisely the turnover/local-energy branch already denoted

\[
\boxed{T_{Campanato}.}
\]

The vorticity non-tightness audit sharpened this further:

\[
V_{remote}
\Longrightarrow
H_{freq}\lor T_{Campanato}.
\]

Thus no additional compactness label is required for failure of local kinetic-energy control.

---

## 4. Center failure is already T_center

The center-nesting theorem defines

\[
\mathfrak T_j
:=
\frac{|X_{j+1}-X_j|}{r_j}.
\]

The non-turnover condition is

\[
\sup_j\mathfrak T_j\le C_T.
\]

Then

\[
|X_*-X_j|\le
\frac{C_T}{1-q^{-1/2}}r_j,
\]

so the first-hitting cores converge to one physical center and the fixed-center ancient rescaling is valid.

Therefore failure of center nesting means

\[
\boxed{
\sup_j\mathfrak T_j=\infty,
}
\]

which by definition is a core-replacement/material-turnover event:

\[
\boxed{C_{center\ fail}\subset T_{center}.}
\]

It is not a third compactness mechanism.

---

## 5. Loss of terminal nontriviality is already H_der

Suitable weak compactness alone gives strong local velocity convergence in the standard subcritical topology, but the first-hitting normalization requires the terminal vorticity witness

\[
|\Omega_\infty(y_*,0)|=1
\]

to survive.

The repository has consistently retained this through the **no-H local derivative compactness** corridor.

If the local derivative/vorticity convergence needed to pass the witness fails, then there exists a fixed normalized cylinder on which the derivative family is not precompact in the retained topology.

This is exactly a derivative concentration/frequency/roughness escape and is typed as

\[
\boxed{H_{der}.}
\]

Hence

\[
\boxed{
C_{nontriviality\ fail}
\subset H_{der}.
}
\]

One must not replace this by a claim that weak suitable convergence preserves pointwise vorticity automatically; it does not.  The correct statement is only that failure of the stronger passage is already an H event.

---

## 6. Pressure does not create an independent compactness branch

Once the fixed center and Morrey local-energy corridor are available, the pressure oscillation on every fixed ball is controlled by the existing near/far decomposition:

\[
P=P_{near}+P_{far}
\]

modulo a time-dependent scalar gauge.

The near part is controlled by local `L^3` velocity and Calderon--Zygmund estimates.

The far part gains one kernel derivative after subtracting a local representative, and the Morrey dyadic series converges.

Therefore

\[
\boxed{
D(R,T)\le C(R,T,M_*).
}
\]

Pressure compactness can fail only if the local-energy/Morrey or centering package has already failed, which is T.

Thus

\[
\boxed{
C_{pressure\ fail}
\subset T_{Campanato}\lor T_{center}.
}
\]

---

## 7. Backward-time completeness is already part of the H/T rate split

The first-hitting tower needs earlier checkpoints to cover arbitrarily long normalized backward times.

On the eventual non-H/non-T rate corridor the repository has

\[
L_-\le L_j\le L_+,
\]

and

\[
\Delta t_j\asymp r_j^2.
\]

Consequently, after stage-`j` normalization, the `m`-generation ancestor lies at backward time of order

\[
q^m,
\]

and the diagonal limit covers

\[
(-\infty,0].
\]

If the normalized stage duration degenerates or escapes the admissible rate corridor, this is already one of the previously typed rate/turnover/derivative exits used to define the eventual no-H/no-T branch.

Hence failure of ancient time completeness is not an additional post-extraction branch.

---

## 8. Exhaustive compactness ledger

The possible failure modes are therefore

\[
\boxed{
\begin{array}{ccl}
\text{global }Z\text{ divergence}
&\longrightarrow&
\text{compactness still holds under Morrey},\\[1mm]
\text{Morrey/local-energy failure}
&\longrightarrow&
T_{Campanato},\\[1mm]
\text{center nesting failure}
&\longrightarrow&
T_{center},\\[1mm]
\text{strong local derivative passage failure}
&\longrightarrow&
H_{der},\\[1mm]
\text{pressure passage failure}
&\longrightarrow&
T_{Campanato}\lor T_{center},\\[1mm]
\text{backward time coverage failure}
&\longrightarrow&
H_{rate}\lor T_{rate}.
\end{array}
}
\]

Thus

\[
\boxed{
C_{fail}\subset H\lor T.
}
\]

---

## 9. Post-Liouville master frontier

Insert this into M5-276:

\[
\text{singular survivor}
\Longrightarrow
H_{freq}\lor T_{Campanato}\lor C_{fail}.
\]

Since

\[
C_{fail}\subset H\lor T,
\]

we obtain the shorter master reduction

\[
\boxed{
\text{hypothetical singular first-hitting tower}
\Longrightarrow
H\lor T.
}
\]

Here `H` is the union of the already typed derivative/frequency/roughness/rate exits and `T` is the union of Campanato/local-energy, material/core replacement, center, pressure/boundary, and rate-turnover exits.

The complete quiet complement is empty by M5-276 + Albritton–Barker.

---

## 10. What this does NOT mean

The statement

\[
\boxed{\text{singularity}\Longrightarrow H\lor T}
\]

is **not** a contradiction.

A true singularity is allowed to have scale-critical derivative-frequency growth or repeated turnover.  Existing genealogy ledgers show that such behavior pays explicit critical actions, but those actions have not yet been proved globally finite.

Therefore the global regularity problem has now moved to exactly two questions:

1. can `H` be absorbed by reselecting a smaller/natural first-hitting core, or must it force a known continuation criterion to diverge in a quantitatively impossible way?
2. can `T` recur indefinitely without violating a scale-critical monotone/coercive quantity or forcing a re-centered first-hitting subsequence back into the quiet corridor?

---

## 11. DSD verdict

### CLOSED

- global enstrophy as an independent compactness prerequisite;
- pressure as an independent compactness escape;
- center drift as an untyped compactness failure;
- terminal witness loss as an untyped event;
- `C_fail` as a third master terminal branch.

### CURRENT MASTER TREE

\[
\boxed{
\text{singular tower}
\Longrightarrow
H\lor T,
\qquad
\text{quiet complement}\Longrightarrow\text{Liouville contradiction}.
}
\]

### OPEN

- closure or absorption of H;
- closure or absorption of T;
- final proof that the H/T classification is exhaustive under every finite-stage reselection convention.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
