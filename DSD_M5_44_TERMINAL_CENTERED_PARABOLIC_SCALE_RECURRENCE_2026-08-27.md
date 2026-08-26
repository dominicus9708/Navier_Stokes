# DSD M5-44 — Terminal-Centered Parabolic Scale Recurrence

Date: 2026-08-27

Status: **DERIVED FROM MINIMAL/RECURRENT COMPLETE W1 ANCESTRY / THE PUMP-TO-DEFECT ANCIENT CELL IS RECURRENT UNDER TERMINAL-CENTERED NAVIER--STOKES SCALING / PERIODIC W1 GIVES DSS, APERIODIC W1 GIVES SCALE-APERIODIC RECURRENCE / GLOBAL REGULARITY UNPROVED.**

## 1. Pump-to-defect cell

Let

\[
\sigma_*:=\lambda_c^2.
\]

M5-41 gives

\[
V_*(z,\sigma)
=
(\sigma_*-\sigma)^{-1/2}
U^\#\!\left(
\frac z{\sqrt{\sigma_*-\sigma}},
\log\frac{\sigma_*}{\sigma_*-\sigma}
\right),
\qquad
\sigma<\sigma_*.
\]

Define

\[
\eta(\sigma)
:=\log\frac{\sigma_*}{\sigma_*-\sigma}.
\]

Then `eta -> +infinity` as `sigma -> sigma_*`.

---

## 2. Recurrence of the complete W1 orbit

Because `U^#` belongs to a compact minimal recurrent W1 set, there exists a sequence

\[
h_n\to\infty
\]

such that the time translates return:

\[
\boxed{
U^\#(Y,\eta+h_n)
\to
U^\#(Y,\eta)
}
\]

on compact `(Y,eta)` sets after subsequence selection.

For a periodic W1 orbit, `h_n` may be integer multiples of one exact period. For an aperiodic minimal orbit, only recurrence is asserted.

---

## 3. Terminal-centered Navier--Stokes scaling

Define the scaling operator

\[
\boxed{
(\mathcal R_hV)(z,\sigma)
:=
e^{-h/2}
V\!\left(
 e^{-h/2}z,
 \sigma_*-e^{-h}(\sigma_*-\sigma)
\right).
}
\]

This is exactly the Navier--Stokes parabolic scaling centered at the terminal spacetime point `(0,sigma_*)`.

The remaining time transforms as

\[
\sigma_*-\sigma
\mapsto
 e^{-h}(\sigma_*-\sigma),
\]

and the spatial scale transforms by the square root factor `e^{-h/2}`.

---

## 4. Exact relation to W1 time translation

Let

\[
\sigma_h
:=
\sigma_*-e^{-h}(\sigma_*-\sigma).
\]

Then

\[
\sigma_*-\sigma_h
=e^{-h}(\sigma_*-\sigma),
\]

so

\[
\eta(\sigma_h)
=\eta(\sigma)+h.
\]

Also

\[
\frac{e^{-h/2}z}
{\sqrt{\sigma_*-\sigma_h}}
=
\frac z{\sqrt{\sigma_*-\sigma}}.
\]

Substituting into the inverse-Leray formula gives exactly

\[
\boxed{
(\mathcal R_hV_*)(z,\sigma)
=
(\sigma_*-\sigma)^{-1/2}
U^\#\!\left(
\frac z{\sqrt{\sigma_*-\sigma}},
\eta(\sigma)+h
\right).
}
\]

Thus terminal-centered parabolic scaling of `V_*` is exactly time translation of its W1 ancestor.

---

## 5. Scale recurrence

Apply the recurrent sequence `h_n`:

\[
\boxed{
\mathcal R_{h_n}V_*
\longrightarrow
V_*
}
\]

locally smoothly on compact subsets strictly before `sigma_*`, in the topology inherited from W1 compactness.

Therefore the same ancient-to-terminal cell reappears at arbitrarily smaller parabolic scales near the terminal point.

This is stronger than merely saying that high-amplitude events occur at arbitrarily large physical thresholds.

---

## 6. Periodic versus aperiodic cases

### Periodic W1

If `U^#` has period `S`, then

\[
\mathcal R_SV_*=V_*
\]

exactly. Hence `V_*` is backward discretely self-similar about `(0,sigma_*)` with scale factor

\[
e^{-S/2}.
\]

### Aperiodic minimal W1

There is no exact period, but there are return times `h_n` with

\[
\mathcal R_{h_n}V_*\to V_*.
\]

Thus the correct description is **scale-aperiodic recurrence**, not DSS.

The two cases are therefore unified as recurrence of one terminal-centered scaling flow.

---

## 7. Pump replication

The anchor `sigma=0` is a positive finite-amplitude pump event.

Under the scaling return `R_{h_n}`, its image occurs at a later time closer to the terminal point and at spatial scale `e^{-h_n/2}` with amplitude scale `e^{h_n/2}`.

Therefore recurrence forces the **normalized pump geometry** to reappear at an infinite sequence of nested physical scales.

This is the same cascade phenomenon previously inferred from W1 recurrence, now represented exactly inside one Navier--Stokes spacetime solution.

---

## 8. Compatibility with the static tail

M5-42 shows that the leading `1/r` far field is static.

The terminal scaling recurrence therefore acts on a solution that simultaneously has

\[
\boxed{
\text{static weak-critical far-field memory}
}

and

\[
\boxed{
\text{recurrent time-dependent interior pump geometry}.
}
\]

These are not separate solutions; they are two layers of the same pump-to-defect cell.

---

## 9. Relation to known asymptotically DSS rigidity

Existing nonexistence results for backward self-similar or asymptotically discretely self-similar solutions typically require stronger integrability/decay hypotheses than the present weak-`L^3`, `1/r` tail allows.

Thus scale recurrence by itself does not close the W1 survivor.

The new endpoint is sharper:

\[
\boxed{
\text{exclude a weak-critical, static-tail, terminal-scale-recurrent ancient-to-terminal cell with a positive pump event.}
}
\]

---

## 10. Updated target

A successful next step could be one of:

1. a rigidity theorem for terminal-scale-recurrent cells with static `1/r` ancestry;
2. a proof that the pump/Hodge formation action cannot be recurrent under `R_h` while the far tail stays static;
3. a tail-renormalized strong-`L^3` quantity that is preserved under the terminal scaling returns;
4. or a same-trajectory flux monotonicity under the scaling flow.

No such contradiction is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
