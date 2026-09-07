# DSD M17-331 — Stationary pure-flux current is nonpositive across kappa-space and splits zero-current into resonant tail or positive-corridor occupancy

Date: 2026-09-08  
Canonical ID: **M17-331**

Status: **ACTIVE FIXED-GENERATION CURRENT IDENTITY**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Fixed-generation scope

By M17-330, the level `kappa=3/2` is not a record-blowdown fixed threshold.  Therefore this module works entirely inside one fixed similarity representation / recurrent hull.

Use the M5-681 stationary pure-material-flux law

\[
\boxed{
\partial_k\overline G(k)=k\,\overline F(k),
}
\]

with

\[
\overline F(k)\ge0.
\]

Assume the retained recurrent population has compact `kappa` support `[k_-,k_+]` and no boundary current:

\[
\overline G(k_-)=\overline G(k_+)=0.
\]

## 2. Exact current formulas

Integrating from the left endpoint gives

\[
\boxed{
\overline G(k)
=
\int_{k_-}^{k}s\,\overline F(s)\,ds.
}
\]

Integrating from the right endpoint gives equivalently

\[
\boxed{
\overline G(k)
=-
\int_k^{k_+}s\,\overline F(s)\,ds.
}
\]

The boundary conditions also force the zero first moment

\[
\boxed{
\int_{k_-}^{k_+}k\,\overline F(k)\,dk=0.
}
\]

## 3. Sign of the stationary current

For `k<=0`,

\[
\overline G(k)
=
\int_{k_-}^{k}s\overline F(s)ds
\le0.
\]

For `k>=0`,

\[
\overline G(k)
=-\int_k^{k_+}s\overline F(s)ds
\le0.
\]

Hence

\[
\boxed{
\overline G(k)\le0
\quad\text{throughout the retained support.}
}
\]

Thus the stationary pure-flux current is everywhere directed toward lower `kappa`; the source term `kF` changes its magnitude but not its sign.

## 4. Exact zero-level balance

At `k=0`,

\[
-\overline G(0)
=
\int_0^{k_+}k\overline F(k)dk
=
\int_{k_-}^{0}(-k)\overline F(k)dk.
\]

M17-314 supplies the lower bound

\[
\boxed{
-\overline G(0)\ge d_{flux}>0.
}
\]

Therefore the positive and negative first moments of the stationary pure-flux distribution are both at least `d_flux`.

## 5. Current at a positive threshold

For any `a>=0`,

\[
\boxed{
-\overline G(a)
=
\int_a^{k_+}k\overline F(k)dk.
}
\]

Subtracting the zero-level identity gives

\[
\boxed{
\overline G(a)-\overline G(0)
=
\int_0^a k\overline F(k)dk.
}
\]

Equivalently,

\[
\boxed{
-\overline G(a)
=
-\overline G(0)
-
\int_0^a k\overline F(k)dk.
}
\]

Thus positive-`kappa` occupancy between `0` and `a` progressively absorbs the magnitude of the downward current.

## 6. The resonant level a=3/2

Set

\[
a=\frac32.
\]

Then

\[
\boxed{
-\overline G\!\left(\frac32\right)
=
\int_{3/2}^{k_+}k\overline F(k)dk.
}
\]

Hence a strict negative current across the resonant level exists **if and only if** the stationary pure-flux distribution carries positive first moment above `3/2`.

The M17-314 zero-level current alone does not force this.

Indeed all positive first moment needed to balance the negative phase could lie in

\[
0<k<\frac32.
\]

## 7. Quantitative half-split

Because

\[
-\overline G(0)\ge d_{flux},
\]

one of the following must hold:

### Branch A — resonant-tail current

\[
\boxed{
-\overline G\!\left(\frac32\right)
\ge\frac12d_{flux}.
}
\]

Then a fixed amount of positive `kappa` first moment lies above the resonant level and the same fixed-generation stationary state has a definite downward crossing current through `kappa=3/2`.

### Branch B — positive corridor occupancy

Otherwise,

\[
-\overline G\!\left(\frac32\right)
<\frac12d_{flux}.
\]

Using the exact difference formula,

\[
\boxed{
\int_0^{3/2}k\overline F(k)dk
\ge\frac12d_{flux}.
}
\]

Since `k<=3/2` in the corridor,

\[
\boxed{
\int_0^{3/2}\overline F(k)dk
\ge\frac13d_{flux}.
}
\]

Thus failure of a resonant-level current forces a fixed pure-flux occupancy in the intermediate positive corridor.

## 8. DSD-theory role

The useful DSD heuristic is channel separation:

- do not treat all positive `kappa` as one state;
- distinguish the intermediate corridor from the super-resonant tail;
- ask which channel actually pays the zero-level directed current.

The canonical result itself is only the exact stationary continuity equation integrated in `k`.

## 9. What is and is not closed

M17-331 proves

\[
\boxed{
H_{zero\ current}
\Longrightarrow
H_{superresonant\ tail/current}
\lor
H_{0<\kappa<3/2\ corridor\ occupancy}.
}
\]

It does **not** prove that the same material label which realizes M17-134's long mean `3/2` must cross either level.

It does **not** identify the fixed-generation `3/2` current as a record-scale-critical ancestry currency; M17-330 forbids that import.

## 10. Next target

The next question is whether M17-134's same-genealogy mean

\[
\langle\kappa\rangle\to\frac32
\]

forces either:

1. genuine super/sub-resonant excursions of that same label, or
2. asymptotic phase locking near `kappa=3/2`.

That is a same-label temporal problem and must not be inferred from the ensemble stationary distribution without an explicit bridge.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
