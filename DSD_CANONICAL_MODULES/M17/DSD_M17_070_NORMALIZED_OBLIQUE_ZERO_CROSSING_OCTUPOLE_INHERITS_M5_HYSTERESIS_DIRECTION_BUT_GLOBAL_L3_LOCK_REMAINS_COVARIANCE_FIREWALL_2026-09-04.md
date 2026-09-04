# DSD M17-070 — The normalized oblique zero-crossing octupole inherits the M5 hysteresis direction, but the global l=3 lock remains a covariance firewall

Date: 2026-09-04
Canonical ID: **M17-070**

Status: **INTERNAL OGLHG ORIENTATION BRIDGE / M17-067 SHOWS THAT EVERY SPATIALLY REGULAR GENUINE-OBLIQUE KAPPA-ZERO EVENT HAS `kappa_3 != 0` AND A NONZERO LOCAL PAYER OCTUPOLE `o_loc = eps sqrt(2)/15 kappa_3 A_* sin(2 vartheta)`, WITH `A_*=|p||Q|_F^2>0`. ON A RETAINED RECURRENT SUBBRANCH WHERE `kappa_3` NEVER VANISHES, ITS SIGN IS MATERIAL-INVARIANT, WHILE `vartheta` IS ALREADY FROZEN. THEREFORE THE AMPLITUDE-NORMALIZED CROSSING OCTUPOLE `omega_oct := o_loc/(A_* |kappa_3|)` IS A CONSTANT SIGNED MATERIAL ORIENTATION. ITS AMPLIFICATION-WEIGHTED KAPPA-ZERO CURRENT IS EXACTLY `omega_oct G_Phi(0)`, SO THE M5-685 SIGN `mean G_Phi(0)<0` TRANSFERS WITHOUT A COVARIANCE LOSS TO THIS NORMALIZED LOCAL l=3 ORIENTATION. HOWEVER THE ACTUAL GLOBAL PRESSURE LOCK SCALAR `m_3` IS NOT EQUAL TO `omega_oct`; M17-068 GIVES `m_3=v_vartheta-n_vartheta`, AND M17-069 SHOWS THAT ITS CROSSING CURRENT REQUIRES `Cov_nu0(m_3,sgn h)`. THE ZERO-SURFACE KINEMATICS ALSO GIVE `h=kappa_3(B_3-V_{0,3})`, SO THE SIGN OF `h` IS A RELATIVE ZERO-SURFACE CROSSING DIRECTION, NOT A SIGN LAW FOR `kappa_3`. THUS SCALAR HYSTERESIS DOES CONTROL ONE NORMALIZED LOCAL OCTUPOLE ORIENTATION, BUT NO EXACT LOCAL-TO-GLOBAL IDENTIFICATION YET TRANSFERS THAT SIGN TO THE PRESSURE l=3 LOCK. THIS IS A PRECISE COVARIANCE FIREWALL, NOT A PROOF / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Regular genuine-oblique zero crossing

At a marked regular nodal event with

\[
\kappa=0,
\]

M17-067 gives, on genuine obliquity,

\[
\boxed{
\mathfrak o_{loc}
=\varepsilon_E\frac{\sqrt2}{15}
\kappa_3A_*\sin2\vartheta,
}
\]

where

\[
\boxed{A_*:=P|Q|_F^2>0.}
\]

Spatial regularity of the kappa-zero level is equivalent here to

\[
\boxed{\kappa_3\neq0}
\]

because

\[
\nabla_h\kappa=0.
\]

---

## 2. Sign of kappa_3 is frozen on the nonzero-gradient recurrent subbranch

M17-064 separates the genuine-oblique branch into

1. a uniformly nonzero-gradient class;
2. a `kappa_3=0` turnover/degenerate class.

On the first class assume

\[
0<c_3\le|\kappa_3|.
\]

Continuity then implies that

\[
\boxed{\operatorname{sgn}\kappa_3}
\]

cannot change along the retained material marker.

The slant/Hessian angle is already materially frozen:

\[
\boxed{D_B\vartheta=0.}
\]

Hence

\[
\boxed{
\operatorname{sgn}(\kappa_3\sin2\vartheta)
}
\]

is a material invariant on this subbranch.

---

## 3. Define the normalized crossing-octupole orientation

At `kappa=0` define

\[
\boxed{
\omega_{oct}
:=\frac{\mathfrak o_{loc}}{A_*|\kappa_3|}.
}
\]

Using Section 1,

\[
\boxed{
\omega_{oct}
=\varepsilon_E\frac{\sqrt2}{15}
\operatorname{sgn}(\kappa_3)\sin2\vartheta.
}
\]

Every factor on the right is constant on the uniformly nonzero-gradient material subbranch.
Therefore

\[
\boxed{D_B\omega_{oct}=0}
\]

between turnover/interface events.

This is a normalized angular orientation, not the physical octupole amplitude.

---

## 4. Lift the normalized orientation into the M5 crossing current

M5-685 uses

\[
G_\Phi(0,\theta)
=\int ha\,\delta(\kappa)d\mu_0.
\]

Define the corresponding normalized-octupole crossing current

\[
\boxed{
G_{\omega}(0,\theta)
:=\int\omega_{oct}\,ha\,\delta(\kappa)d\mu_0.
}
\]

On a coherent recurrent subensemble with the same frozen `omega_oct`, it factors out:

\[
\boxed{
G_{\omega}(0,\theta)
=\omega_{oct}\,G_\Phi(0,\theta).
}
\]

Consequently M5-685's surviving condition

\[
\boxed{
\overline{G_\Phi(0)}<0
}
\]

implies

\[
\boxed{
\operatorname{sgn}\overline{G_\omega(0)}
=-\operatorname{sgn}\omega_{oct}
}
\]

whenever `omega_oct != 0`.

Thus the scalar hysteresis bias does transfer exactly to the **normalized local octupole orientation**.

---

## 5. Caveat for an ensemble containing both orientation classes

If the label ensemble contains material subpopulations with opposite values of

\[
\operatorname{sgn}(\kappa_3\sin2\vartheta),
\]

then `omega_oct` cannot be factored out of the full ensemble integral.
The correct procedure is to decompose the ensemble into its frozen orientation classes first.

Within each class the factorization of Section 4 is exact.
Across classes an additional population-weight cancellation is possible.

This is a DSD branch decomposition, not a technical nuisance.

---

## 6. Actual local octupole amplitude does not factor from the hysteresis current

The physical crossing octupole is

\[
\mathfrak o_{loc}=\omega_{oct}A_*|\kappa_3|.
\]

Its current is

\[
\int\mathfrak o_{loc}ha\delta(\kappa)d\mu_0
=\omega_{oct}
\int A_*|\kappa_3|ha\delta(\kappa)d\mu_0.
\]

The positive magnitude

\[
A_*|\kappa_3|
\]

can correlate with upward/downward crossings.
Therefore M5-685 does **not** determine the sign of the unnormalized octupole current without an additional amplitude/crossing correlation law.

Only the normalized orientation current factors exactly.

---

## 7. Zero-surface kinematics explain why h and kappa_3 signs are independent

At a spatially regular zero event, the implicit-function theorem gives a local moving `kappa=0` surface.
Let its local velocity be `V_0`.
Along the moving zero surface,

\[
\partial_\theta\kappa+V_0\cdot\nabla\kappa=0.
\]

For the material drift `B`,

\[
h=D_B\kappa
=\partial_\theta\kappa+B\cdot\nabla\kappa.
\]

Subtracting gives

\[
\boxed{
h=(B-V_0)\cdot\nabla\kappa.}
\]

On the semilinear nodal branch

\[
\nabla\kappa=\kappa_3e_3,
\]

so

\[
\boxed{
h=\kappa_3(B_3-V_{0,3}).}
\]

Equivalently,

\[
\boxed{
V_{0,3}-B_3=-\frac h{\kappa_3}.
}
\]

Thus the sign ratio

\[
\operatorname{sgn}(h/\kappa_3)
\]

is the signed relative crossing velocity of the zero surface and material marker.
There is no reason from kinematics alone for it to be fixed.

This explains why M5's downward/upward crossing sign `sgn h` cannot be replaced by `sgn kappa_3`.

---

## 8. Regular zero-root formula gives the same absence of a sign lock

M17-013 gives, at a regular zero root of

\[
\kappa=F_q,
\]

\[
\boxed{
h=F_{qq}V_{rel}.}
\]

In the nodal gauge,

\[
\kappa_3=F_{q3}
\]

because `q_3=0`.

Hence

\[
\boxed{
\frac h{\kappa_3}
=\frac{F_{qq}V_{rel}}{F_{q3}}
}
\]

whenever `kappa_3 != 0`.

None of the presently established semilinear identities fixes the sign of the three factors on the right.
The zero-surface kinematic conclusion is therefore consistent with the reduced-label description.

---

## 9. Local Poisson pressure tax also has no hysteresis sign

M17-068 gives

\[
\boxed{
\mathfrak n_\vartheta
=-\varepsilon_E\frac{3\sqrt2}{5}
\lambda G_qP(\operatorname{tr}Q)\sin2\vartheta.
}
\]

At a regular zero root,

\[
h=F_{qq}V_{rel}.
\]

Therefore

\[
\boxed{
\mathfrak n_\vartheta h
=-\varepsilon_E\frac{3\sqrt2}{5}
\lambda G_qP(\operatorname{tr}Q)
F_{qq}V_{rel}\sin2\vartheta.
}
\]

The current theory supplies no universal sign for

\[
\lambda,
\quad
G_q,
\quad
\operatorname{tr}Q,
\quad
F_{qq},
\quad
V_{rel}.
\]

Thus even the explicit local pressure tax cannot by itself determine

\[
\operatorname{Cov}_{\nu_0}(\mathfrak n_\vartheta,\operatorname{sgn}h).
\]

---

## 10. Why the normalized local orientation does not solve the global pressure lock

M17-069 identifies the actual missing global bridge as

\[
\boxed{
\operatorname{Cov}_{\nu_0}(m_3,\operatorname{sgn}h),
}
\]

with

\[
\boxed{
m_3=\mathfrak v_\vartheta-\mathfrak n_\vartheta.}
\]

The newly fixed local orientation is

\[
\omega_{oct}
=\varepsilon_E\frac{\sqrt2}{15}
\operatorname{sgn}(\kappa_3)\sin2\vartheta.
\]

There is no established identity

\[
m_3=C\omega_{oct}
\]

or even a sign law

\[
\operatorname{sgn}m_3=\operatorname{sgn}\omega_{oct}.
\]

Indeed `m_3` is generated by the whole-space STF pressure-source production/relative-transport architecture, whereas `omega_oct` is only the normalized orientation of one local payer-density jet.

Therefore the exact M5-to-local orientation bridge does not close the local-to-global step.

---

## 11. DSD interpretation

OGLHG now contains two consecutive maps:

\[
\boxed{
\text{M5 scalar crossing bias}
\longrightarrow
\text{normalized local octupole orientation}
}
\]

which is exact on each frozen orientation class, followed by

\[
\boxed{
\text{local octupole orientation}
\dashrightarrow
\text{global pressure }m_3
}
\]

for which no sign-preserving map has been proved.

The broken arrow is the genuine remaining firewall.

---

## 12. DSD audit

### Audit A — saying scalar hysteresis has no angular consequence at all
Corrected.
It does control the normalized local crossing-octupole orientation current on a fixed orientation class.

### Audit B — using that normalized result for the physical octupole amplitude
Rejected.
The amplitude `A_*|kappa_3|` introduces another crossing correlation.

### Audit C — assuming sign h equals sign kappa_3
Rejected by the exact zero-surface relative-velocity identity.

### Audit D — assuming the explicit Poisson tax has a fixed h-correlation
Rejected; its signed factorization contains several uncontrolled terms.

### Audit E — identifying normalized local payer orientation with global pressure l=3
Rejected as a descriptor substitution.

### Audit F — proof status
OGLHG has reached a precise local-to-global covariance firewall, not a contradiction.

---

## 13. Updated Rank-1 OGLHG result

On each uniformly nonzero-`kappa_3` frozen-orientation subbranch,

\[
\boxed{
\overline{G_\omega(0)}
=\omega_{oct}\,\overline{G_\Phi(0)},
\qquad
\overline{G_\Phi(0)}<0.
}
\]

Thus the normalized local angular orientation inherits the M5 hysteresis direction exactly.

But the global DSAIG lock still requires

\[
\boxed{
G_3(0)
=\int m_3ha\delta(\kappa)d\mu_0
}
\]

with unconstrained joint covariance.

Therefore Rank-1 is now reduced to

\[
\boxed{
R_{principal}^{scalar-lock}
\ \lor\
R_{oblique}^{local/global-covariance}
\ \lor\
T_{gradient/rank/interface}.
}
\]

---

## 14. Next target

Further differentiation of the existing oblique local equations does not presently supply a sign for `m_3`, because the global STF pressure moment contains independent source-production and relative-transport channels.

The highest-value next move is therefore one of two options:

1. derive a genuinely new local-to-global conservation/monotonicity law for the STF `l=3` pressure moment;
2. return to the intrinsic surviving Rank-2 director geometry, where several complete subbranches are already closed and the remaining anisotropic pure-kernel/interface class has not yet been reduced to an equally sharp covariance firewall.

Under the current audit, option 2 is the better branch-pruning continuation unless a new conserved `l=3` quantity is found.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
