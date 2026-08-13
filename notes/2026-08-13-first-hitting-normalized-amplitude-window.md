# First-hitting normalization gives a uniform vorticity-amplitude window

Date: 2026-08-13

Status: **EXACT CHECKPOINT NORMALIZATION + BOUNDED-ENSTROPHY LOCAL-DRIFT CONSEQUENCES**.

The amplification checkpoints should be chosen as **first hitting times** of geometric vorticity levels.  Then normalization by the *later* checkpoint fixes not only the endpoint maximum but the entire preceding amplification interval below unit vorticity amplitude.

---

## 1. First hitting times

Fix `q>1` and a base level `W_*`.  On the smooth lifespan define

\[
\boxed{
t_j
=\inf\{t:\|\omega(t)\|_\infty=q^jW_*\}.
}
\]

For a hypothetical finite-time blowup with `||omega||_infty -> infinity`, all sufficiently large `j` are defined and

\[
t_j\uparrow T^*.
\]

By the first-hitting definition,

\[
\boxed{
\|\omega(t)\|_\infty
\le W_{j+1}:=q^{j+1}W_*
\quad
\text{for }t\in[t_j,t_{j+1}].
}
\]

At the right endpoint,

\[
\|\omega(t_{j+1})\|_\infty=W_{j+1}.
\]

---

## 2. Normalize by the later checkpoint

Set

\[
r_{j+1}=W_{j+1}^{-1/2}
\]

and choose a maximum-vorticity center `x_{j+1}` at the final time.  Define

\[
y=\frac{x-x_{j+1}}{r_{j+1}},
\qquad
s=W_{j+1}(t-t_{j+1}),
\]

\[
\Omega_{j+1}(y,s)
=W_{j+1}^{-1}
\omega(x_{j+1}+r_{j+1}y,t).
\]

Then on the whole backward amplification interval

\[
I_{j+1}
=
[-\Sigma_j,0],
\qquad
\Sigma_j=W_{j+1}(t_{j+1}-t_j),
\]

we have the exact amplitude bound

\[
\boxed{
\|\Omega_{j+1}(s)\|_{L^\infty(\mathbb R^3)}
\le1
\quad(s\in I_{j+1}).
}
\]

At `s=0`,

\[
\boxed{
\|\Omega_{j+1}(0)\|_\infty=1.
}
\]

At the left checkpoint,

\[
\|\Omega_{j+1}(-\Sigma_j)\|_\infty=1/q.
\]

Thus the entire amplification event is represented inside a fixed amplitude range `[1/q,1]` rather than by a diverging maximum.

---

## 3. Relation to the previous duration channel

The earlier normalization used

\[
\sigma_j=W_j(t_{j+1}-t_j).
\]

The later-checkpoint normalized duration is

\[
\boxed{
\Sigma_j
=W_{j+1}(t_{j+1}-t_j)
=q\sigma_j.
}
\]

Hence the amplification-time noncollapse result

\[
\sigma_j\ge\sigma_*>0
\]

immediately gives

\[
\boxed{
\Sigma_j\ge q\sigma_*>0.
}
\]

---

## 4. Add a bounded normalized-global-enstrophy branch

Define the window enstrophy channel

\[
\boxed{
\mathfrak E_j
=
\sup_{s\in I_{j+1}}
\|\Omega_{j+1}(s)\|_2^2.
}
\]

Split the route into

\[
\boxed{
\mathfrak E_j\to\infty
}
\]

(global normalized-enstrophy concentration) or a subsequence with

\[
\boxed{
\mathfrak E_j\le M_E.
}
\]

On the bounded branch, interpolation with `||Omega||_infty<=1` gives every finite `p>=2`:

\[
\boxed{
\|\Omega(s)\|_p
\le
\|\Omega\|_2^{2/p}
\|\Omega\|_\infty^{1-2/p}
\le
M_E^{1/p}.
}
\]

---

## 5. Strain/velocity-gradient bounds in every finite `Lp`

The velocity gradient/strain is a zero-order singular-integral transform of vorticity.  Therefore for every fixed

\[
1<p<\infty,
\]

\[
\boxed{
\|\nabla U(s)\|_p
+\|S_U(s)\|_p
\le
C_p\|\Omega(s)\|_p
\le
C_pM_E^{1/p}.
}
\]

The Riesz transform does not provide an `L-infinity -> L-infinity` estimate; no such claim is made.

---

## 6. Local mean-frame drift bound

Fix a normalized ball `B_R` and choose `p>3`.  By local Poincare--Morrey,

\[
\boxed{
\|U-(U)_{B_R}\|_{L^\infty(B_R)}
\le
C_{p,R}\|\nabla U\|_{L^p(B_R)}
\le
C_{p,R}M_E^{1/p}.
}
\]

Thus after subtracting the spatial mean velocity -- or equivalently using the already-derived mean-flow moving frame -- the local drift is uniformly bounded on every fixed normalized ball.

This eliminates arbitrary Galilean transport from the local parabolic bookkeeping.

---

## 7. Uniform local stretching-source bound

Because

\[
\|\Omega\|_\infty\le1,
\]

we have

\[
\|\Omega\|_4^2
\le
\|\Omega\|_\infty\|\Omega\|_2
\le
M_E^{1/2}.
\]

Also

\[
\|S_U\|_2\le C\|\Omega\|_2\le C M_E^{1/2}.
\]

Therefore, globally and hence on any local cutoff,

\[
\boxed{
\left|
\int\Omega\cdot S_U\Omega dy
\right|
\le
\|S_U\|_2\|\Omega\|_4^2
\le
C M_E.
}
\]

Thus the normalized vortex-stretching source is uniformly bounded in time on the bounded-`M_E` first-hitting branch.

---

## 8. Cutoff transport/buffer terms are also bounded on fixed balls

For a fixed cutoff `chi` on `B_R`, the mean-frame velocity bound and `||Omega||_2^2<=M_E` give

\[
\boxed{
|T_\chi(s)|
\le
C_{R,p}M_E^{1+1/p}
}
\]

schematically, and

\[
\boxed{
|B_\chi(s)|
\le
C_R\nu M_E.
}
\]

Hence the total local enstrophy growth channel

\[
G_\chi=Q_\chi+T_\chi+B_\chi
\]

satisfies a uniform-in-time bound

\[
\boxed{
\|G_\chi\|_{L^\infty(I_{j+1})}
\le
C(M_E,R,p,\nu).
}
\]

---

## 9. Stronger temporal-persistence consequence

Suppose a fixed local enstrophy rise

\[
\Delta e>0
\]

occurs between an earlier normalized time and the terminal dangerous state.  Since

\[
\frac12E_\chi'\le G_\chi,
\]

the `L-infinity` source bound gives directly

\[
\boxed{
\Delta s
\ge
\frac{\Delta e}
{2C(M_E,R,p,\nu)}.
}
\]

Thus on the bounded normalized-global-enstrophy first-hitting branch, dangerous local enstrophy cannot appear in a vanishing time layer.

This improves the earlier generic `L^p`, `p>1`, temporal-concentration gate.

---

## 10. New use in compactness

The first-hitting window provides three fixed features on the bounded branch:

1. vorticity amplitude `||Omega||_infty<=1`;
2. a noncollapsing normalized time interval;
3. finite-`Lp` strain bounds and bounded local mean-frame drift.

These are strong inputs for interior parabolic compactness/regularity.  A next target is to determine whether the buffered V2 bound used previously can be **derived** on a shorter interior subwindow from these amplitude/enstrophy/drift bounds, or whether failure produces a genuinely separate second-derivative concentration branch.

No such automatic V2 estimate is claimed yet.

Status: **FIRST-HITTING AMPLITUDE WINDOW CLOSED / INTERIOR V2 BOOTSTRAP NEXT**.
