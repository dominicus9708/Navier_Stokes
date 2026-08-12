# Critical L3 pressure-rate baseline

Status: **COMPUTATIONAL CHECK + DERIVED SYMMETRY / CRITICAL-L3 RATE**

Checks expected from the committed audit: **10/10**.

## Symmetric seed

Reflection parity gives `Pi3=0` exactly for the single z-axis Gaussian benchmark. The spectral audit at `80^3` gives `Pi3≈2.76e-15`.

## Asymmetric superposition

For the z-seed at the origin plus an x-seed centered at `(-1,0,0)`:

- `48^3`: `Pi3≈6.35132629412`
- `64^3`: `Pi3≈6.37069208506`
- `80^3`: `Pi3≈6.37252492014`
- `96^3`: `Pi3≈6.37091893766`

At `96^3`:

- `T3≈84.8365700225`
- `D3≈664.578015025`
- `Pi3≈6.37091893766`

The relative spread of `Pi3` over `48^3..96^3` is approximately `0.333%`.

The reflection-related x-seed centered at `(1,0,0)` gives `Pi3≈-6.37252492014` at `80^3`.

## Amplitude homogeneity

For fixed spatial shape and positive amplitude `A`:

- `T3(Au)=A^3 T3(u)`
- `D3(Au)=A^3 D3(u)`
- `Pi3(Au)=A^4 Pi3(u)`

For `nu=1`, the representative positive-pressure configuration gives a computational crossover

`A_*≈104.31431031`.

At `A=120`, the corresponding balance predicts

`dT3/dt≈5.18048822849e8 > 0`

at `t=0`.

## Route status

The shortcut “global `L3` is automatically monotone decreasing” is therefore marked **FAILED-ROUTE CANDIDATE / COMPUTATIONAL COUNTEREXAMPLE**, not a rigorous theorem-level counterexample yet.

The retained proof target is a non-circular estimate controlling `Pi3` strongly enough to keep the critical `L3` channel bounded.

## Numerical boundary

Pressure is reconstructed by spectral inversion of `-Delta p=Q` on a large window containing rapidly decaying data. The window is a numerical integration device, not a physical container or a change of the Clay-aligned `R^3` problem.
