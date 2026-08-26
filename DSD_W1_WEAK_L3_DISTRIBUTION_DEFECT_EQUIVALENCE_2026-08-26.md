# DSD W1 Weak-L3 Distribution Defect Equivalence

Date: 2026-08-26

Status: **ZERO-AMPLITUDE THRESHOLD DEFECT IDENTIFIED WITH THE LOW-AMPLITUDE `L^{3,INFINITY}` DISTRIBUTION COEFFICIENT / `1/r` LOG-SHELL DENSITY, WEAK-L3 SATURATION, AND `R3/6` BOUNDARY CHARGE SHOWN TO BE THE SAME ENDPOINT OBJECT UP TO FIXED NORMALIZATIONS / GLOBAL REGULARITY UNPROVED.**

## 1. Distribution function

For a W1 state `U`, let

\[
a:=|U|,
\qquad
N(\lambda)
:=
|\{Y:a(Y)>\lambda\}|.
\]

The threshold energy is

\[
\mathcal E_\lambda
=
\frac12\int(a^2-\lambda^2)_+dY.
\]

Since for `a>lambda`,

\[
\frac12(a^2-\lambda^2)
=
\int_\lambda^a \mu\,d\mu,
\]

Fubini/layer-cake gives

\[
\boxed{
\mathcal E_\lambda
=
\int_\lambda^\infty \mu N(\mu)d\mu.
}
\]

---

## 2. Critical weak-L3 model

Suppose the low-amplitude distribution has the critical asymptotic

\[
N(\lambda)
\sim C_3\lambda^{-3}
\qquad(\lambda\downarrow0).
\]

Then

\[
\mathcal E_\lambda
\sim
C_3\int_\lambda \mu^{-2}d\mu
\sim
\frac{C_3}{\lambda},
\]

and hence

\[
\boxed{
\lambda\mathcal E_\lambda
\to C_3.
}
\]

Conversely, under the W1 monotonicity/regular-variation structure supplied by the positive-density critical tail, the Abelian/Tauberian endpoint gives the same coefficient relation.

Thus define the low-amplitude weak-L3 defect coefficient by

\[
\boxed{
\mathscr C_{WL3}
:=
\lim_{\lambda\downarrow0}\lambda^3N(\lambda),
}
\]

whenever the limit exists, or use the corresponding Abelian/Cesaro coefficient when only averaged convergence is available.

---

## 3. Match to the threshold defect

The amplitude-state endpoint theorem gives

\[
\boxed{
\lambda\langle\mathcal E_\lambda\rangle_\mu
\to
\frac{\mathscr R_3}{3}.
}
\]

Therefore the invariant low-amplitude distribution coefficient is

\[
\boxed{
\mathscr C_{WL3}
=
\frac{\mathscr R_3}{3}
}
\]

in the exact-tail/regular-variation regime, and the same identity holds at the level of the Abelian defect coefficient in the general W1 endpoint formulation.

Consequently

\[
\boxed{
\frac{\mathscr R_3}{6}
=
\frac12\mathscr C_{WL3}.
}
\]

---

## 4. Check on the canonical `1/r` model

For

\[
U(Y)=\frac{A}{|Y|}
\]

with isotropic scalar amplitude `A`,

\[
N(\lambda)
=
\frac{4\pi}{3}\left(\frac A\lambda\right)^3,
\]

so

\[
\lambda^3N(\lambda)
=
\frac{4\pi}{3}A^3.
\]

The cubic mass per logarithmic radius is

\[
\mathscr R_3
=4\pi A^3.
\]

Hence

\[
\boxed{
\mathscr C_{WL3}=\mathscr R_3/3,
}
\]

exactly as above.

---

## 5. Relation to the weak-L3 quasi-norm

The Lorentz quasi-norm satisfies, up to the conventional normalization,

\[
\|U\|_{L^{3,\infty}}^3
\asymp
\sup_{\lambda>0}\lambda^3N(\lambda).
\]

Thus

\[
\boxed{
\|U\|_{3,\infty}^3
\gtrsim
\mathscr C_{WL3}
=
\frac{\mathscr R_3}{3}.
}
\]

The W1 endpoint therefore contains a genuinely nonzero weak-L3 defect at the low-amplitude state boundary.

The large weak-L3 core threshold derived separately is stronger in a different direction: it says the survivor must also have a quantitatively large finite-parent contribution, not merely the asymptotic tail coefficient.

---

## 6. Why every fixed prelimit time has zero defect

For the actual finite-energy prelimit at any fixed Leray time `s`,

\[
N_s(\lambda)
\le
\frac{\|U(s)\|_2^2}{\lambda^2}.
\]

Hence

\[
\lambda^3N_s(\lambda)
\le
\lambda\|U(s)\|_2^2
\to0
\qquad(\lambda\downarrow0).
\]

Likewise

\[
\lambda\mathcal E_{\lambda,s}\to0.
\]

But the W1 omega-limit has the nonzero coefficient

\[
\mathscr C_{WL3}=\mathscr R_3/3>0.
\]

Thus the endpoint is a genuine **loss-of-tightness defect** under the noncompact Leray limit.

This is not a contradiction because

\[
\|U(s)\|_2^2
=e^{s/2}\|u(t)\|_2^2
\]

is not uniformly bounded as `s->infinity`.

---

## 7. Fixed physical amplitude levels

Let a fixed physical velocity threshold be `L>0`. The corresponding Leray threshold is

\[
\lambda(s)=Le^{-s/2}.
\]

The distribution functions satisfy

\[
N_U(\lambda(s),s)
=e^{3s/2}N_u(L,t).
\]

Therefore

\[
\boxed{
\lambda(s)^3N_U(\lambda(s),s)
=L^3N_u(L,t).
}
\]

So the amplitude-state characteristic transports exactly the physical superlevel-volume observable `L^3 N_u(L,t)`.

This is the distribution-function version of the moving-threshold cancellation.

---

## 8. Unified endpoint object

At the present W1 resolution the following are equivalent manifestations of one critical defect:

\[
\boxed{
\begin{array}{c}
\text{positive cubic mass per log radius}\[1mm]
\Updownarrow\\[1mm]
\mathscr R_3>0\\[1mm]
\Updownarrow\\[1mm]
K(0+)=\mathscr R_3/3\\[1mm]
\Updownarrow\\[1mm]
\mathscr C_{WL3}=\mathscr R_3/3>0\\[1mm]
\Updownarrow\\[1mm]
\text{nonzero low-amplitude weak-L3 defect}.
\end{array}
}
\]

The endpoint residue `R3/6` is one half of this defect coefficient because of the cubic-energy normalization.

---

## 9. Updated proof target

The final compactness problem can now be stated without reference to a particular tail parametrization:

\[
\boxed{
\text{Can a finite-energy Navier--Stokes prelimit generate a nonzero }L^{3,\infty}
\text{ low-amplitude defect under a recurrent Leray omega-limit?}
}
\]

Every fixed prelimit state has zero defect; the candidate W1 omega-limit has a positive one.

Ruling out this defect would force

\[
\mathscr R_3=0
\]

and close the W1 endpoint. No such no-defect theorem is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
