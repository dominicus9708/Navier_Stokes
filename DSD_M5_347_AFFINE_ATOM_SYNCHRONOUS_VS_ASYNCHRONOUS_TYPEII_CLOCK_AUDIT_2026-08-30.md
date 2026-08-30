# DSD M5-347 — Affine-Atom Synchronous vs Asynchronous Type-II Clock Audit

Date: 2026-08-30

Status: **AFFINE 1/5 SHIELD SCALING CONVERTED INTO A VELOCITY TYPE-II CLOCK / ATOM BRANCH SPLIT INTO SYNCHRONOUS TYPE-II OR OFF-LINEAGE/ASYNCHRONOUS TURNOVER / GLOBAL REGULARITY UNPROVED.**

## 1. First-hitting normalization

Let `r_j -> 0` be the physical natural length at a first-hitting/atom stage. Use

\[
U_j(Y)=r_j u(X_j+r_jY,t_j).
\]

Then

\[
\Omega_j=r_j^2\omega,
\]

and the point-picked active core has order-one normalized vorticity.

The saturated affine-shield benchmark has normalized radius

\[
\boxed{
R_{{\rm scr},j}\asymp r_j^{-1/5}.
}
\]

Equivalently its physical radius is

\[
d_{{\rm scr},j}=r_jR_{{\rm scr},j}\asymp r_j^{4/5}.
\]

## 2. Velocity amplitude forced by an affine shield

An order-one affine normalized gradient on a ball of radius `R_scr` gives a relative velocity difference

\[
|U_j(Y_1)-U_j(Y_2)|\gtrsim R_{{\rm scr},j}
\]

for suitable points in the shield.

A common translation cannot hide this difference: at least one of the two absolute velocities has size at least half the difference. Therefore

\[
\|U_j(t_j)\|_\infty\gtrsim R_{{\rm scr},j}.
\]

Returning to physical variables,

\[
\boxed{
\|u(t_j)\|_\infty
\gtrsim
r_j^{-1}R_{{\rm scr},j}
\asymp r_j^{-6/5}.
}
\]

## 3. Terminal clock

Write

\[
a_j:=T_*-t_j,
\qquad
\Theta_j:=\frac{a_j}{r_j^2}.
\]

Since the active vorticity scale is `|omega| ~ r_j^{-2}`, `Theta_j` is also the local vorticity Type-I clock product up to fixed constants.

The velocity Type-II indicator at the atom time satisfies

\[
\begin{aligned}
\sqrt{a_j}\,\|u(t_j)\|_\infty
&\gtrsim
\sqrt{a_j}\,r_j^{-6/5}\\
&=
(r_j\sqrt{\Theta_j})r_j^{-6/5}.
\end{aligned}
\]

Hence

\[
\boxed{
\sqrt{T_*-t_j}\,\|u(t_j)\|_\infty
\gtrsim
r_j^{-1/5}\Theta_j^{1/2}.
}
\]

Define the synchronous atom-clock descriptor

\[
\boxed{
\mathfrak T_{atom,j}
:=r_j^{-1/5}\Theta_j^{1/2}.
}
\]

## 4. Synchronous branch

If

\[
\limsup_j\mathfrak T_{atom,j}=\infty,
\]

then the atom lineage itself realizes velocity Type-II growth.

Equivalently, any power-law clock

\[
\Theta_j\gg r_j^{2/5}
\]

forces synchronous Type-II at the affine-shield times.

This is the branch in which the spatial `1/5` shield and the terminal clock are directly locked.

## 5. Asynchronous branch

Suppose instead that

\[
\sup_j\mathfrak T_{atom,j}<\infty.
\]

Then the affine atom times themselves obey a Type-I-sized velocity indicator.

But M5-346 plus Leslie--Shvydkoy imply that an endpoint atom cannot coexist with a uniform velocity-Type-I bound on the entire preterminal tail. Therefore there must exist other times `s_j -> T_*` such that

\[
\boxed{
\sqrt{T_*-s_j}\,\|u(s_j)\|_\infty\to\infty.
}
\]

These Type-II excursions are not synchronized with the atom snapshots.

Formation-wise there are then two possibilities:

1. the large-velocity event occurs in the same spatial lineage, forcing a strong temporal reformation/turnover between the atom state and the burst state;
2. it occurs in a different spatial lineage, producing a remote competing active structure.

Both belong to the existing dynamic-turnover / remote-H frontier rather than the quiet affine-atom leaf.

Thus

\[
\boxed{
\text{affine atom}
\Longrightarrow
\text{synchronous Type-II atom clock}
\ \lor\
T_{async/remote}.
}
\]

## 6. Axis-property interpretation

The synchronous branch carries simultaneously

- the dual-hyperbolic parent strain from M5-343--345;
- the affine spatial scale `R_scr ~ r^{-1/5}`;
- the clock `Theta`;
- the Type-II descriptor `r^{-1/5}sqrt(Theta)`.

This gives a two-axis formation coordinate

\[
\boxed{
(R_{scr},\Theta)
}
\]

instead of treating space concentration and time compression separately.

## 7. Firewall

The existence of an atom does **not** imply that the atom times themselves must be the times at which the Type-II `L^infty` indicator diverges.

That synchronization is an additional branch condition.

If synchronization fails, the resulting off-time/off-lineage Type-II excursion must be retained as a turnover/remote branch rather than silently identified with the atom core.

## 8. Audit verdict

### PROVED

- saturated affine shield forces `||u(t_j)||_infty >= c r_j^{-6/5}`;
- the atom-time Type-II indicator is bounded below by `c r_j^{-1/5} sqrt(Theta_j)`;
- atom branch splits exhaustively into synchronous Type-II or asynchronous/off-lineage Type-II turnover.

### OPEN

- exclusion of the synchronous Type-II dual-hyperbolic core;
- quantitative cost of asynchronous reformation;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]