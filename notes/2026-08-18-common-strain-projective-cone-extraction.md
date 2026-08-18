# Common-strain projective cone extraction for a packet ensemble

Date: 2026-08-18

Status: **EXACT FINITE-DIMENSIONAL COVARIANCE LEMMA. A COMMON TRACE-FREE STRAIN CANNOT PRODUCTIVELY AMPLIFY AN ISOTROPIC PACKET ENSEMBLE. ORDER-ONE COMMON-STRAIN EFFICIENCY FORCES A FIXED PROJECTIVE-CONE SUBPOPULATION, AND AFTER ORIENTATION CHOICE A FIXED SIGNED-CONE SUBPOPULATION. GLOBAL REGULARITY NOT PROVED.**

## 1. Packet ensemble covariance

Let packets be indexed by `i`, with positive vorticity-energy weights `e_i` and representative unit directions `xi_i` at the responsible time.  Set

\[
E=\sum_i e_i,
\qquad
w_i=e_i/E,
\]

and define

\[
\boxed{
C_{\rm ens}
=\sum_i w_i\,\xi_i\otimes\xi_i.
}
\]

Then

\[
C_{\rm ens}\succeq0,
\qquad
\operatorname{tr}C_{\rm ens}=1.
\]

Suppose a common mesoscopic symmetric strain `S_L` is approximately constant across the packet set on the responsible block.  Its direct packet stretching is

\[
Q_{\rm common}
=\sum_i e_i\,\xi_i^TS_L\xi_i
=E\operatorname{tr}(S_LC_{\rm ens}).
\]

Because `tr S_L=0`,

\[
Q_{\rm common}
=E\operatorname{tr}\left[
S_L\left(C_{\rm ens}-\frac13I\right)
\right].
\]

Hence

\[
\boxed{
|Q_{\rm common}|
\le
E|S_L|_F
\left\|C_{\rm ens}-\frac13I\right\|_F.
}
\]

## 2. Isotropic packet populations cannot use a common affine amplifier

If

\[
C_{\rm ens}=\frac13I,
\]

then exactly

\[
\boxed{Q_{\rm common}=0.}
\]

Thus a common trace-free strain cannot produce net enstrophy growth of a projectively isotropic ensemble.

More generally, if the common strain supplies a fixed efficiency fraction

\[
Q_{\rm common}
\ge
\alpha E|S_L|_F,
\qquad
\alpha>0,
\]

then necessarily

\[
\boxed{
\left\|C_{\rm ens}-\frac13I\right\|_F
\ge\alpha.
}
\]

Equivalently,

\[
\boxed{
\operatorname{tr}(C_{\rm ens}^2)
\ge
\frac13+\alpha^2.
}
\]

## 3. Preferred projective axis

Let

\[
\lambda_1
=\lambda_{\max}(C_{\rm ens})
\]

and let `e` be a corresponding eigenvector.  Since the eigenvalues are nonnegative and sum to one,

\[
\operatorname{tr}(C_{\rm ens}^2)
\le
\lambda_1\operatorname{tr}C_{\rm ens}
=\lambda_1.
\]

Therefore

\[
\boxed{
\lambda_1
\ge
\frac13+\alpha^2.
}
\]

But

\[
\lambda_1
=\sum_iw_i(\xi_i\cdot e)^2.
\]

Choose

\[
\theta
=\frac13+\frac{\alpha^2}{2}.
\]

Let `p` be the total energy weight of packets satisfying

\[
(\xi_i\cdot e)^2\ge\theta.
\]

Because the complementary packets contribute at most `theta`,

\[
\lambda_1
\le
p+(1-p)\theta.
\]

Hence

\[
\boxed{
p
\ge
\frac{\alpha^2/2}
{2/3-\alpha^2/2}
=:c_\alpha>0.
}
\]

Thus order-one common-strain efficiency extracts a fixed energy fraction in one projective cone.

## 4. Signed cone extraction

The projective cone contains both orientations `+e` and `-e`.  Split it by the sign of `xi_i dot e`.  At least one sign carries half the cone weight.  Therefore a fixed fraction

\[
\boxed{
\ge c_\alpha/2
}
\]

lies in one signed cone and satisfies

\[
|\xi_i\cdot e|
\ge\sqrt\theta.
\]

For thick intense packets, this gives a fixed-sign component of vorticity along `e` on a fixed fraction of the packet population.

Hence a productive common mesoscopic amplifier automatically creates a **signed coherent subpopulation**, even if the full packet ensemble is not coherent.

## 5. Relation to the signed-line defect

The projective cone extraction does not by itself guarantee that each packet has a coherent first moment; projective alignment can coexist with polarity cancellation inside a packet.  The existing exact split

\[
\operatorname{Var}(\Omega)
=D_{\rm proj}+D_{\rm line}
\]

therefore supplies the local complement:

- small `D_proj` + small `D_line` gives a genuinely signed coherent packet;
- small `D_proj` + large `D_line` is a polarity/magnitude-gradient residual branch;
- large `D_proj` is a multi-axis/angular branch.

Thus after local signed-line pruning, the common-strain ensemble contains a fixed signed coherent packet subpopulation or pays residual variance.

## 6. Mesoscopic amplifier versus same-scale amplifier

If a lower-frequency strain field is sufficiently slowly varying across many natural packets, the common-strain lemma applies and extracts a coherent signed subpopulation.  That subpopulation returns to the previously developed coherent-flux/Betchov/material-deformation geometry.

To avoid this extraction, the responsible strain must vary materially from packet to packet.  Spectrally, its active frequency must then approach the packet frequency.  This is consistent with the previously derived sampling bound

\[
R\lesssim C\sqrt{K/N},
\qquad
L=K/R,
\]

which forces the responsible strain frequency `L` toward `K` as multiplicity grows.

Therefore the residual compact wall sharpens from

\[
\text{noncoherent packet replication}
\]

to

\[
\boxed{
\text{same-scale high--high strain--direction correlation}
}
\]

unless a coherent signed subpopulation, polarity defect, or derivative/kernel deformation branch is activated.

Status: **COMMON LOWER-FREQUENCY AMPLIFIER ROUTED TO SIGNED COHERENT SUBPOPULATION / FINAL COMPACT RESIDUAL = SAME-SCALE HIGH-HIGH CORRELATION NETWORK.**