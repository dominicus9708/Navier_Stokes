# DSD M19-261 — Raw-H2 is CE-H independent, but fixed-parent ancestry does not supply physical H3 without a base-scale gain

Date: 2026-09-15  
Canonical ID: **M19-261**  
Status: **ACTIVE CORRECTION / CE-H DEPENDENCY REMOVAL / BASE-SCALE AMPLIFICATION FIREWALL / GMS H3 TRANSFER NOT YET CERTIFIED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-260 corrected the historical M17 record radius semantics by separating

\[
r_j\downarrow0
\]

(the first-hitting physical base scale) from

\[
K_k\asymp q^{k/2}\uparrow\infty
\]

(the backward record blow-down factor), with composite physical radius

\[
\rho_{j,k}=r_jK_k=r_{j-k}.
\]

The next audit asks two questions:

1. Does the M17 raw-H2 resource require exact CE-H at every record?
2. Does the finite M17 fixed-parent raw-H2 ledger imply the physical \(D^3u\in L^2\) input used by M19-255?

The answers are respectively **no** and **no without an additional base-scale gain**.

---

## 2. M17-404 is not a CE-H theorem

M17-404 begins with the first-generation ancient Navier--Stokes element from M5-474--477.

Its inputs are:

\[
\|V(\tau)\|_\infty\lesssim(-\tau)^{-1/2},
\]

\[
\|\Omega(\tau)\|_\infty\lesssim(-\tau)^{-1},
\qquad
\|\Omega(\tau)\|_2^2\lesssim(-\tau)^{-1/2},
\]

and

\[
\int_{-\infty}^{0}\|\nabla\Omega(\tau)\|_2^2d\tau<\infty.
\]

Writing

\[
\partial_\tau\Omega-\Delta\Omega
=-V\cdot\nabla\Omega+S\Omega
=:F,
\]

M17-404 uses a standard forced-heat H1 estimate to prove

\[
\boxed{
\int_{-\infty}^{0}\|\Delta\Omega(\tau)\|_2^2d\tau<\infty.
}
\]

No identity

\[
\Delta\Omega=\kappa\Omega
\]

is used in this proof.

Therefore the true raw-H2 resource is a **general first-generation ancient PDE resource on the bounded Type-I ratchet lane**, not an intrinsically CE-H resource.

---

## 3. M17-405 is likewise a fixed-parent scaling ledger

For record blow-down factors \(K_k\) and a fixed normalized annulus

\[
I=[-b,-a]\Subset(-\infty,0),
\]

M17-405 uses the exact identity

\[
\boxed{
K_k^{-3}
\int_I\|\Delta\Omega_k(s)\|_2^2ds
=
\int_{K_k^2I}\|\Delta\Omega(t)\|_2^2dt.
}
\]

Because the ancestral windows \(K_k^2I\) have bounded overlap,

\[
\boxed{
\sum_k
K_k^{-3}
\int_I\|\Delta\Omega_k(s)\|_2^2ds
<\infty.
}
\]

Again, this conclusion does not require exact CE-H.

Hence the M19-260 provisional requirement that every GMS transfer record retain late exact CE-H was stronger than necessary for the raw-H2 route.

---

## 4. CE-H subsequence gap is removed from the raw-H2 GMS gate

M5-599 globalizes CE-H on the extracted ancient solution, and M17-232 correctly warns that derivative re-extraction/mean subtraction does not create new homogeneous CE-H solutions.

Those facts remain important for the CE-H rigidity program.

However the GMS/raw-H2 route uses the independent M17-404--405 resource.

Therefore

\[
\boxed{
\mathcal T_{GMS}^{rawH2}
\text{ does not require exact CE-H inheritance at every selected scale.}
}
\]

Any `CE-H subsequence ancestry-gap` remains a CE-H-branch issue, but it is removed as a primitive condition for transferring the M17-404--405 raw-H2 resource.

---

## 5. The remaining problem is more basic: the first-hitting base scale

Let \(h_{j,k}\) denote the normalized raw-H2 charge of an age-\(k\) record viewed from first-hitting base stage \(j\).

Inside the stage-normalized parent, the backward-record pullback contributes

\[
K_k^{-3}h_{j,k}.
\]

But returning the stage-normalized parent to the original physical variables contributes an additional factor

\[
r_j^{-3}.
\]

Therefore the actual physical raw-H2 / \(D^3u\) cost is

\[
\boxed{
Q_{j,k}^{phys}
=
r_j^{-3}K_k^{-3}h_{j,k}
=
(r_jK_k)^{-3}h_{j,k}
=
r_{j-k}^{-3}h_{j,k}.
}
\]

This additional \(r_j^{-3}\) factor is not present in the fixed-parent M17-405 summability statement.

---

## 6. Exact firewall against the unsafe transfer

M17-405 gives schematically, for one fixed ancient parent,

\[
\boxed{
\sum_kK_k^{-3}h_k<\infty.
}
\]

Multiplying the same ledger by the physical base conversion gives only

\[
\sum_kQ_{j,k}^{phys}
=
r_j^{-3}
\sum_kK_k^{-3}h_{j,k}.
\]

Even if the normalized-parent sum is bounded uniformly by a constant \(C\), this yields at best

\[
\boxed{
\sum_kQ_{j,k}^{phys}
\lesssim Cr_j^{-3},
}
\]

which diverges as

\[
r_j\downarrow0.
\]

Thus

\[
\boxed{
\text{finite fixed-parent ancestral raw-H2 budget}
\not\Rightarrow
\text{finite physical }D^3u\text{ budget near the singular time}.
}
\]

This is the base-scale amplification firewall.

---

## 7. Relation to M17-404 tail decay

M17-404 proves on a backward dyadic annulus

\[
[-2T,-T]
\]

the tail estimate

\[
\int_{-2T}^{-T}\|\Delta\Omega\|_2^2dt
\lesssim T^{-3/2}.
\]

For a record scale

\[
K^2\asymp T,
\]

this is exactly

\[
T^{-3/2}\asymp K^{-3}.
\]

After blowing the annulus to unit scale, the normalized record raw-H2 charge can therefore remain order one.

This is consistent with M17-405 and confirms that the ancient tail decay precisely pays the **record** factor \(K^{-3}\); it does not produce an extra factor capable of paying the independent fine-base factor \(r_j^{-3}\).

---

## 8. Correct physical transfer requirement

For target physical shell index

\[
n=j-k,
\qquad
\rho_{j,k}=r_n,
\]

a diagonal family \((j_n,k_n)\) would have physical charge

\[
Q_n^{phys}
=
r_n^{-3}h_{j_n,k_n}.
\]

To obtain the physical H3 input required by the M19-255 route through bounded-overlap annular windows, one needs a condition of the form

\[
\boxed{
\mathcal T_{GMS}^{base-gain}:
\qquad
\sum_n r_n^{-3}h_{j_n,k_n}<\infty.
}
\]

Equivalently, the normalized charges must have enough genuine decay in the original physical scale to compensate the \(r_n^{-3}\) derivative amplification.

M17-404--405 do not prove this.

They permit order-one normalized record charges because

\[
\sum_kK_k^{-3}<\infty.
\]

---

## 9. M19-255 remains correct but is a stronger endpoint than the current ancestry resource supplies

M19-255 proves the valid implication

\[
D^3u\in L^2_{x,t}
\Longrightarrow
u\in L^6_{x,t},
\qquad
p\in L^3_{x,t},
\qquad
\mathcal P_{GMS}^{log}(V)<\infty.
\]

Together with M19-254 this excludes a singular point.

The audit correction is not to retract this implication.

The correction is:

\[
\boxed{
\text{M17-404--405 alone do not establish its physical }D^3u\in L^2\text{ premise}.
}
\]

Therefore M19-255 is a valid terminal regularity gate, not yet a consequence of the certified M17 ancestry ledger.

---

## 10. Revised GMS transfer complex

The raw-H2 route should now be written as

\[
\boxed{
\mathcal T_{GMS}^{base-gain}
+
\mathcal T_{GMS}^{physical-incidence}
+
\mathcal T_{GMS}^{repr}
+
\mathcal T_{GMS}^{root}.
}
\]

Here:

- `base-gain` pays the missing original fine-scale derivative amplification;
- `physical-incidence` places the paid resource in the actual Galilean neighborhood of the candidate singularity with the required time coverage;
- `repr` certifies same-field whole-space representation or prices cutoffs/interfaces;
- `root` certifies entry from an arbitrary hypothetical singularity into the bounded Type-I ratchet/ancient-resource corridor.

The previous `diag-AC` bookkeeping remains useful for composing two scales, but it is not by itself enough: diagonal scale matching does not create the missing base-scale decay.

---

## 11. Relation to the CE-H program

The CE-H program remains independently valuable.

M5-599 gives a global double-eigenline ancient class on that branch, while M17-127 and later modules derive exact material genealogy, coefficient, sign and geometry identities.

Those structures may still provide a **new mechanism that forces the required base-scale gain**, or may close CE-H by an entirely different rigidity contradiction.

But until such a mechanism is proved, the raw-H2 budget must not be promoted to physical H3 integrability merely because it was discovered inside the CE-H research chain.

---

## 12. Permanent firewalls after M19-261

\[
\boxed{
\text{raw-H2 finite ancestral budget}
\neq
\text{CE-H-specific theorem}.
}
\]

\[
\boxed{
\text{record blow-down discount }K^{-3}
\neq
\text{physical fine-scale gain }r^3.
}
\]

\[
\boxed{
\text{two-scale exponent identity}
\neq
\text{uniform physical H3 summability}.
}
\]

\[
\boxed{
\text{diagonal radius matching}
\neq
\text{base-scale derivative payment}.
}
\]

\[
\boxed{
\text{M19-255 terminal implication remains valid}
\neq
\text{its premise has been derived}.
}
\]

\[
\boxed{
\text{conditional branch reductions}
\neq
\text{global 3D Navier--Stokes regularity}.
}
\]

---

## 13. Immediate next target

The next calculation should no longer ask whether exact CE-H is present on every first-hitting record.

Instead audit whether any already-certified first-hitting/energy/critical-tail quantity can supply a **physical base-scale gain** strong enough to replace

\[
r_n^{-3}h_n
\]

by a summable quantity.

Three candidate mechanisms are now sharply separated:

1. **direct physical-budget route:** derive a genuine original-variable finite parent budget of derivative order three or an equivalent scale-weighted form;
2. **critical-smallness route:** avoid full physical H3 summability and prove that some scale-invariant normalized quantity becomes small on an admissible sequence, enough for standard epsilon regularity;
3. **CE-H rigidity route:** use the exact double-eigenline/sign/genealogy system to force additional decay in normalized raw-H2 charge or obtain a contradiction without passing through physical H3.

If none supplies an \(r^3\)-level compensation, retain the base-scale amplification as an explicit ancestry-conversion survivor rather than hiding it inside `transfer`.

Global 3D Navier--Stokes regularity remains unproved.
