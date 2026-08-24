# DSD Ancestor-Epoch Two-Sided Clock Upgrade

Date: 2026-08-25

Status: **PREVIOUSLY CONDITIONAL ANCESTOR EPOCH-SEPARATION LOWER BOUND IS NOW PROVED ON THE NON-H/T RECURRENT CLOCK CORRIDOR / EXACT FINITE-k FORMULA DERIVED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

`ANCESTOR_RADIUS_IDENTITY_AND_WEIGHTED_RETURN_DENSITY_2026-08-25.md` introduced

\[
\Gamma_{j,k}
:=
\frac{\nu(t_j-t_{j-k})}{r_{j-k}^2}
\]

in viscosity-restored notation and correctly audited that upper remaining-time estimates alone do not imply a positive lower bound for `Gamma_{j,k}`.

At that time, a one-step lower epoch separation was left as a missing premise.

The later first-hitting/Leray clock analysis proved the stronger two-sided adjacent-gap estimate on the existing non-H/T recurrent stage corridor. This note feeds that result back into the genealogy ledger.

---

## 2. Imported two-sided adjacent gap

Use

\[
W_j=q^jW_0,
\qquad
r_j^2=\frac\nu{W_j}.
\]

Define the exact adjacent normalized gap

\[
\tau_j
:=
W_j(t_{j+1}-t_j)
=
\frac{\nu(t_{j+1}-t_j)}{r_j^2}.
\]

On the recurrent non-H/T stage corridor,

\[
\boxed{
0<\tau_-
\le
\tau_j
\le
\tau_+<\infty.
}
\]

The existing clock construction gives explicitly

\[
\tau_-\ge\frac{L_-}{q},
\qquad
\tau_+\le L_+.
\]

Therefore the formerly missing one-step lower epoch separation is already available:

\[
\boxed{
 t_{j+1}-t_j
\ge
\tau_-\frac{r_j^2}{\nu}.
}
\]

**Status: PROVED on the stated corridor.**

---

## 3. Exact age-k epoch formula

Let

\[
n=j-k.
\]

Then

\[
t_j-t_n
=
\sum_{h=0}^{k-1}(t_{n+h+1}-t_{n+h}).
\]

Using

\[
t_{m+1}-t_m
=
\tau_m\frac{r_m^2}{\nu}
\]

and

\[
r_{n+h}^2=r_n^2q^{-h},
\]

we obtain the exact identity

\[
\boxed{
\frac{\nu(t_j-t_{j-k})}{r_{j-k}^2}
=
\sum_{h=0}^{k-1}q^{-h}\tau_{j-k+h}.
}
\]

Thus

\[
\boxed{
\Gamma_{j,k}
=
\sum_{h=0}^{k-1}q^{-h}\tau_{j-k+h}.
}
\]

This is a finite ancestor-clock analogue of the remaining-time geometric convolution.

---

## 4. Uniform two-sided epoch comparability

Apply the adjacent bounds termwise:

\[
\tau_-
\sum_{h=0}^{k-1}q^{-h}
\le
\Gamma_{j,k}
\le
\tau_+
\sum_{h=0}^{k-1}q^{-h}.
\]

Hence

\[
\boxed{
\tau_-
\frac{1-q^{-k}}{1-q^{-1}}
\le
\Gamma_{j,k}
\le
\tau_+
\frac{1-q^{-k}}{1-q^{-1}}.
}
\]

For every `k>=1`, this implies in particular

\[
\boxed{
\tau_-
\le
\Gamma_{j,k}
\le
\frac{\tau_+}{1-q^{-1}}.
}
\]

Restoring physical time,

\[
\boxed{
\tau_-\frac{r_{j-k}^2}{\nu}
\le
 t_j-t_{j-k}
\le
\frac{\tau_+}{1-q^{-1}}
\frac{r_{j-k}^2}{\nu}.
}
\]

Thus an age-`k` observation occurs after a time genuinely comparable to one parabolic time of the ancestor scale `r_{j-k}`, uniformly in `k`.

**Status: PROVED.**

---

## 5. Large-age limit

As `k->infinity`, the geometric sum tends to

\[
\frac1{1-q^{-1}}.
\]

Therefore every large-age epoch gap remains inside the fixed interval

\[
\boxed{
\frac{\tau_-}{1-q^{-1}}
\lesssim
\Gamma_{j,k}
\lesssim
\frac{\tau_+}{1-q^{-1}},
}
\]

more precisely with the finite-`k` factors from Section 4.

The important point is that `Gamma_{j,k}` does **not** grow with age `k`.

An old shell is observed after order one of its own ancestor parabolic time, not after `k` ancestor parabolic times.

---

## 6. Relation to the exact ancestor-radius identity

The earlier spatial identity is

\[
\boxed{
R_{j,k}^{\rm phys}
=r_{j-k}.
}
\]

Combining it with the present temporal identity gives the exact parabolic spacetime matching

\[
\boxed{
R_{j,k}^{\rm phys}=r_{j-k},
\qquad
 t_j-t_{j-k}
\asymp
\frac{(R_{j,k}^{\rm phys})^2}{\nu}.
}
\]

This is the strongest scale-only genealogy correspondence available without identifying the shell with a material packet.

---

## 7. Consequence for material-packet tracking

Suppose a material ancestor packet is initialized at stage `n=j-k` with physical radius comparable to `r_n`.

The present theorem says that by the descendant observation time `t_j`, the packet has evolved for a full order-one fraction/multiple of its own parabolic time

\[
\frac{r_n^2}{\nu}.
\]

Therefore the local amplitude-location genealogy bridge can no longer be dismissed on the ground that the ancestor/descendant interval might be arbitrarily shorter than the ancestor natural time.

If the packet fails to retain amplitude/coherence over this interval, it must pay one of the explicitly defined local strain/deformation or diffusion exposures.

If it remains quiet, the forward material-packet theorem produces a coherent descendant packet after a genuine ancestor-scale epoch.

This still does **not** prove that the descendant packet occupies the Eulerian age-`k` shell.

---

## 8. Important limitation: elapsed epoch is not return residence

The theorem gives

\[
t_j-t_{j-k}\asymp r_{j-k}^2/\nu.
\]

It does not say that the material packet spends that entire interval inside the matching Eulerian annulus.

Hence it does not by itself imply a lower bound for the weighted shell return density

\[
\mathfrak R_k
=
\rho_k^{-1}\sum_\ell\tau_{k,\ell}.
\]

The distinction is:

- **epoch gap** = time between ancestor creation and descendant observation;
- **return dwell** = time actually spent in the tracked shell geometry.

The first is now controlled from both sides. The second still requires a material-location / relative-motion argument.

---

## 9. Audit update

The earlier genealogy audit can now be updated as follows.

| Statement | Updated status |
|---|---|
| `R_{j,k}^{phys}=r_{j-k}` | PROVED |
| one-step lower epoch separation on recurrent corridor | **PROVED** |
| `Gamma_{j,k}` exact geometric-sum identity | **PROVED** |
| `Gamma_{j,k}` bounded above and below uniformly in age | **PROVED** |
| age-k observation occurs after one ancestor-scale parabolic epoch up to constants | **PROVED** |
| shell is automatically same material packet | NOT DERIVED |
| elapsed epoch automatically equals shell residence | FALSE / NOT DERIVED |
| weighted return-density lower bound sufficient for cubic contradiction | remains conditional |
| global regularity | UNPROVED |

---

## 10. Updated genealogy frontier

The temporal scale-matching uncertainty has been removed.

The remaining genealogy problem is now purely a **material-location / dwell / replacement** problem:

\[
\boxed{
\text{ancestor packet evolves for }\asymp r_n^2/\nu
\quad\text{and the matching descendant shell is observed}
}
\]

but one must still decide whether

\[
\boxed{
\text{the material descendant actually occupies that shell for sufficient weighted time}
}
\]

or instead pays local deformation, diffusion, center-relative transport, packet replacement, or remote-tail escape.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
