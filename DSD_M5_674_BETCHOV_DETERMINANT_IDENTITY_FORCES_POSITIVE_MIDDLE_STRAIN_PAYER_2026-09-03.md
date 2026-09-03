# DSD M5-674 — Betchov determinant identity forces a quantitative positive-middle-strain payer

Date: 2026-09-03

Status: **INTERNAL ALGEBRAIC STRAIN PAYER EXTRACTION / FOR TRACE-FREE STRAIN EIGENVALUES `lambda1>=lambda2>=lambda3`, POSITIVE `-det Sigma` IS POSSIBLE ONLY WHERE `lambda2>0`, AND ON THAT SET `(1/3)lambda2|Sigma|^2 <= -det Sigma <= (1/2)lambda2|Sigma|^2` / THE BETCHOV IDENTITY `Q=-4 int det Sigma` THEREFORE IMPLIES `int lambda2^+ |Sigma|^2 >= Q/2` / SINCE EVERY NONZERO INVARIANT HARD COMPONENT HAS `<Q>>0`, A POSITIVE-MIDDLE-STRAIN POPULATION IS MANDATORY EVEN IF THE VORTICITY MAXIMUM ITSELF IS TOP-ALIGNED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Trace-free strain spectrum

Let

\[
\lambda_1\ge\lambda_2\ge\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0
\]

be the eigenvalues of the similarity strain tensor `Sigma`.

The determinant is

\[
\det\Sigma=\lambda_1\lambda_2\lambda_3.
\]

Because the trace vanishes, `lambda1>=0` and `lambda3<=0`.

---

## 2. Sign of the determinant

If

\[
\lambda_2\le0,
\]

then `lambda2 lambda3>=0`, so

\[
\det\Sigma\ge0.
\]

Therefore

\[
\boxed{
-\det\Sigma>0
\Longrightarrow
\lambda_2>0.
}
\]

Thus positive strain-determinant production can occur only where the middle strain eigenvalue is positive.

---

## 3. Quantitative comparison on lambda2>0

On `lambda2>0`, write

\[
\lambda_1=r\lambda_2,
\qquad
r\ge1,
\]

and hence

\[
\lambda_3=-(r+1)\lambda_2.
\]

Then

\[
-\det\Sigma
=r(r+1)\lambda_2^3.
\]

Also

\[
|\Sigma|^2
=\lambda_1^2+\lambda_2^2+\lambda_3^2
=2(r^2+r+1)\lambda_2^2.
\]

Therefore

\[
\frac{-\det\Sigma}{\lambda_2|\Sigma|^2}
=
\frac{r(r+1)}{2(r^2+r+1)}.
\]

For `r>=1`, this ratio lies between `1/3` and `1/2`.

Hence

\[
\boxed{
\frac13\lambda_2|\Sigma|^2
\le
-\det\Sigma
\le
\frac12\lambda_2|\Sigma|^2
\qquad(\lambda_2>0).
}
\]

---

## 4. Betchov identity

The whole-space strain-vorticity/Betchov identity already used in M5-608 gives

\[
\boxed{
Q
=-4\int_{\mathbb R^3}\det\Sigma\,dy.
}
\]

Split the domain according to the sign of `lambda2`.

On `lambda2<=0`,

\[
-\det\Sigma\le0.
\]

Therefore

\[
\frac14Q
=\int(-\det\Sigma)dy
\le
\int_{\lambda_2>0}(-\det\Sigma)dy.
\]

Using the upper determinant bound,

\[
\frac14Q
\le
\frac12
\int\lambda_2^+|\Sigma|^2dy.
\]

Thus

\[
\boxed{
\int_{\mathbb R^3}
\lambda_2^+|\Sigma|^2dy
\ge
\frac12Q.
}
\]

---

## 5. Invariant mean

Every nonzero invariant CE-H component inherits the exact enstrophy production ledger

\[
\boxed{
\langle Q\rangle
=\frac14\langle E\rangle+\langle P\rangle
>0.
}
\]

Therefore

\[
\boxed{
\left\langle
\int\lambda_2^+|\Sigma|^2dy
\right\rangle
\ge
\frac12\langle Q\rangle
>0.
}
\]

Hence positive middle strain is not an optional geometric feature of the hard survivor.

It is a mandatory recurrent payer.

---

## 6. Coherent packet extraction

The all-order compact hull gives uniform `C^1` bounds for `Sigma` in the fixed active core.

A positive invariant average of

\[
\lambda_2^+|\Sigma|^2
\]

therefore yields, after the usual event thickening and finite-core localization, a positive-frequency family of fixed-radius regions on which

\[
\boxed{
\lambda_2\ge\lambda_{2,*}>0
}
\]

and

\[
\boxed{
|\Sigma|\ge s_*>0.
}
\]

The precise constants depend on the compact-hull caps and the production mean.

This defines a coherent positive-middle-strain payer population.

---

## 7. Relation to vorticity alignment

M5-672 says that the global vorticity maximum must be top- or middle-aligned whenever it pays positive recurrent axial strain.

M5-674 adds a stronger global statement:

Even if that maximum is **top-aligned**, the same hard state must contain another population with

\[
\lambda_2>0.
\]

Thus a purely `one-positive-eigenvalue` top-stretch geometry cannot support the CE-H recurrent production balance.

---

## 8. Relation to known middle-eigenvalue criteria

Known regularity criteria require scale-critical space-time integrability of `lambda2^+`.

The present result gives the opposite necessary hard-core behavior: a Type-I recurrent survivor must carry persistent positive-middle-strain activity, which is consistent with critical logarithmic divergence of those criteria.

Therefore the external theorem does not itself close the branch.

---

## 9. Updated strain frontier

Every CE-H survivor now carries simultaneously:

1. a high-vorticity axial-strain payer with mean at least one at the maximum;
2. a positive-frequency positive-middle-strain packet;
3. the M5-671 spectral-gap compatibility;
4. the M5-624 pressure-viscous compensation requirement at eigenvalue collisions.

Thus top-aligned and middle-aligned dynamics cannot be treated as disjoint global alternatives; positive middle strain is mandatory somewhere in every recurrent state/component.

The next calculation should determine whether the positive-middle-strain packet can be separated indefinitely from the persistent high-vorticity flux network, or whether finite-core Biot--Savart/strain coupling forces a same-component overlap.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
