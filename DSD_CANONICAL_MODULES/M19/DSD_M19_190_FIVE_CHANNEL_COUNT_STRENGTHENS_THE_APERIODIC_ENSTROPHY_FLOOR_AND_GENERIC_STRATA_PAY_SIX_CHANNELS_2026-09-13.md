# M19-190 — Five-channel count strengthens the aperiodic enstrophy floor and generic strata pay six channels

**Date:** 2026-09-13  
**Status:** ACTIVE CALCULATION / QUANTITATIVE THRESHOLD IMPROVEMENT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. General M-channel Young reduction

For total observable hard-channel count `M`, the clean `a=2` averaged inequality is

\[
\frac14+\nu x
\le
M^{-2/5}\mathfrak A x^{3/5}
+M^{-1/6}\mathfrak B_2x^{1/4}.
\]

With

\[
\mathfrak A\le K_AZ_+^{7/20}\Pi^{3/20},
\qquad
\mathfrak B_2\le K_B\Pi^{1/2},
\qquad
\Pi=\overline P_U,
\]

split `nu x` equally and use the exact concave Young maxima.

The local coefficient becomes

\[
\boxed{
K_1^{(M)}
=
\frac25\left(\frac35\right)^{3/2}
2^{3/2}M^{-1}K_A^{5/2}.
}
\]

The nonlocal coefficient becomes

\[
\boxed{
K_2^{(M)}
=
\frac34\,2^{-1/3}M^{-2/9}K_B^{4/3}.
}
\]

Hence

\[
\boxed{
K_1^{(M)}\nu^{-3/2}Z_+^{7/8}\Pi^{3/8}
+
K_2^{(M)}\nu^{-1/3}\Pi^{2/3}
<\frac14
\Longrightarrow
\text{no }M\text{-channel neutral hard family}.
}
\]

## 2. Insert the recurrent background enstrophy bound

M19-187 gives

\[
\Pi\le C_E^4\nu^{-4}Z_+^3.
\]

Thus define

\[
\boxed{
K_*^{(M)}
:=
K_1^{(M)}C_E^{3/2}
+
K_2^{(M)}C_E^{8/3}.
}
\]

Then

\[
\boxed{
K_*^{(M)}\frac{Z_+^2}{\nu^3}<\frac14
\Longrightarrow
\text{no }M\text{-channel hard family}.
}
\]

## 3. Universal aperiodic threshold uses M=5

M19-189 proves that genuinely aperiodic quotient recurrence in a nonzero state requires at least

\[
M=5
\]

observable hard channels.

Therefore

\[
\boxed{
K_*^{(5)}\frac{Z_+^2}{\nu^3}<\frac14
\Longrightarrow
\text{genuinely aperiodic quotient recurrence is impossible}.
}
\]

Equivalently, every genuinely aperiodic survivor must satisfy

\[
\boxed{
\frac{Z_+^2}{\nu^3}
\ge
\frac1{4K_*^{(5)}}.
}
\]

Since

\[
K_1^{(5)}\propto5^{-1},
\qquad
K_2^{(5)}\propto5^{-2/9},
\]

this is strictly stronger than the M19-187 three-channel floor.

## 4. Generic rotational stratum uses M=6

If the rotational stabilizer is discrete, then

\[
\dim(SO(3)\cdot U)=3.
\]

Aperiodic quotient dynamics needs two additional directions and the time tangent is independent of rotations. Hence

\[
M\ge3+1+2=6.
\]

Thus the generic-stratum threshold is

\[
\boxed{
K_*^{(6)}\frac{Z_+^2}{\nu^3}<\frac14
\Longrightarrow
\text{generic-stratum aperiodic recurrence is impossible}.
}
\]

Only the axisymmetric-isotropy stratum needs the universal `M=5` constant.

## 5. Monotonicity in channel count

Both pieces of `K_*^{(M)}` decrease strictly with `M`:

\[
M^{-1},
\qquad
M^{-2/9}.
\]

Hence additional exact neutral symmetry channels help the exclusion estimate rather than weaken it.

This reflects the basic mechanism:

\[
\boxed{
\text{damping demand grows linearly in }M,
\quad
\text{collective compensation grows sublinearly in }M.
}
\]

## 6. Status

The improvement raises the quantitative floor on aperiodic recurrence, but M18-042 still supplies only boundedness, not the required universal smallness of `Z_+^2/nu^3`.

Thus the large-but-finite enstrophy branch remains open.

---

\[
\boxed{\text{M19-190: APERIODICITY PAYS A FIVE-CHANNEL ENSTROPHY FLOOR, AND GENERIC STRATA PAY SIX.}}
\]
