# DSD M5-35 — Weighted Pressure Tail Returns to the Large Weak-L3 Endpoint

Date: 2026-08-27

Status: **DERIVED LORENTZ/CALDERON--ZYGMUND REDUCTION / THE M5-34 PRESSURE-TAIL REMAINDER IS CONTROLLED BY THE SAME LARGE WEAK-L3 CRITICAL SIZE ALREADY IDENTIFIED EARLIER / NO NEW UNCONDITIONAL CLOSURE / GLOBAL REGULARITY UNPROVED.**

## 1. Input from M5-34

The threshold-surface estimate gives

\[
|F_P|
\le
\frac\nu2D_3
+
\frac1{2\nu}
\int |V|\,|\Pi|^2dz.
\]

On a positive-residue W1 endpoint,

\[
\langle F_P\rangle
=
\nu\langle D_3\rangle
+
\frac{\mathscr R_3}{6}.
\]

Hence necessarily

\[
\boxed{
\left\langle
\int |V|\,|\Pi|^2dz
\right\rangle
\ge
\nu^2\langle D_3\rangle
+
\frac{\nu\mathscr R_3}{3}.
}
\]

## 2. Critical weak-L3 size

Let

\[
M:=\|V\|_{L^{3,\infty}}.
\]

The established `p=3` dissipation controls the strong `L9` norm:

\[
\|V\|_9^3\lesssim D_3.
\]

Lorentz interpolation between `L^{3,infty}` and `L9` gives

\[
\boxed{
\|V\|_{L^{6,2}}
\lesssim
M^{1/4}D_3^{1/4}.
}
\]

## 3. Pressure estimate

The pressure satisfies

\[
\Pi=R_iR_j(V_iV_j)
\]

up to the scalar gauge.

Lorentz Holder gives

\[
\|V\otimes V\|_{L^{3,1}}
\lesssim
\|V\|_{L^{6,2}}^2.
\]

Calderon--Zygmund boundedness on Lorentz spaces then yields

\[
\boxed{
\|\Pi\|_{L^{3,1}}
\lesssim
M^{1/2}D_3^{1/2}.
}
\]

Since `L^{3,1}` embeds into the Lorentz spaces needed for the square-product estimate,

\[
\||\Pi|^2\|_{L^{3/2,1}}
\lesssim
M D_3.
\]

Pairing with `|V| in L^{3,infty}` gives

\[
\boxed{
\int |V|\,|\Pi|^2dz
\lesssim
M^2D_3.
}
\]

## 4. Necessary large-critical threshold

Combining the lower and upper bounds,

\[
\nu^2\langle D_3\rangle
+
\frac{\nu\mathscr R_3}{3}
\lesssim
M_*^2\langle D_3\rangle,
\]

where `M_*` is the recurrent W1 weak-L3 ceiling/supremum used in the estimate.

Thus

\[
\boxed{
M_*^2
\gtrsim
\nu^2
+
\frac{\nu\mathscr R_3}
{3\langle D_3\rangle}.
}
\]

In particular,

\[
\boxed{M_*\gtrsim\nu.}
\]

This is the same qualitative large weak-critical survivor requirement already obtained from the direct pressure-work estimate, now recovered through the weighted pressure-tail remainder.

## 5. DSD interpretation

The chain

\[
\boxed{
\text{threshold--Hodge commutator}
\to
\text{weighted pressure tail}
\to
\text{large weak-L3 critical size}
}
\]

is now explicit.

Therefore the weighted pressure tail is not a new independent endpoint. Standard Lorentz/CZ estimates route it back to the same large weak-critical class.

This is useful as an audit lock: continuing to estimate the pressure tail only by global Lorentz norms will not prove M5; it simply restates the existing small-tail threshold in another representation.

## 6. What would be genuinely new

A new pressure-tail argument would need information not reducible to the global weak-L3 size, for example

1. a **strictly local/high-threshold** estimate in which only the shrinking high-amplitude tail appears;
2. a geometric cancellation tied to the threshold surface;
3. a time-integrability theorem for `int |V||Pi|^2` stronger than the generic critical scaling permits;
4. a pressure-Poisson estimate exploiting the W1 cross-radius/phase-space structure beyond Calderon--Zygmund boundedness.

None is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
