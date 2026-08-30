# DSD M5-334 — Compressive-Strain Three-Sector / Determinant–Planar Fork

Date: 2026-08-30

Status: **ATOM-SELECTED COMPRESSIVE ACTION SPLIT INTO POSITIVE-MIDDLE, NEGATIVE-MIDDLE, OR SPECTRALLY PLANAR SECTORS / NEGATIVE-MIDDLE ACTION IS ENSTROPHY-DESTRUCTIVE AND REQUIRES COMPENSATING POSITIVE DETERMINANT PRODUCTION / ONLY THE NEAR-PLANAR SECTOR CAN CARRY LARGE COMPRESSION WITH SMALL DETERMINANT / GLOBAL REGULARITY UNPROVED.**

## 1. Setup

From M5-333, an endpoint energy atom forces

\[
\int^{T_*}\|S_-(t)\|_3^2dt=\infty.
\]

Let

\[
\lambda_1\ge\lambda_2\ge\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0.
\]

Fix a small spectral threshold `0<delta<1` and split space-time into

\[
\mathcal E_+(\delta)=\{\lambda_2\ge\delta|S|\},
\]

\[
\mathcal E_-(\delta)=\{\lambda_2\le-\delta|S|\},
\]

and

\[
\mathcal E_0(\delta)=\{|\lambda_2|<\delta|S|\}.
\]

These are respectively the two-positive/one-negative productive sector, the one-positive/two-negative compressive sector, and the near-planar spectral sector.

## 2. Middle eigenvalue is the eigenvalue nearest zero

For a nonzero symmetric trace-free `3x3` matrix,

\[
\boxed{
|\lambda_2|=\min_i|\lambda_i|.
}
\]

Moreover

\[
\boxed{
\lambda_1(-\lambda_3)\ge\frac13|S|^2.
}
\]

Indeed, if `lambda_2>=0`, write `lambda_2=x lambda_1`, `0<=x<=1`; if `lambda_2<0`, apply the same calculation to `-S`.

Hence

\[
\boxed{
|\det S|
=\lambda_1(-\lambda_3)|\lambda_2|
\ge\frac13|S|^2|\lambda_2|.
}
\]

Therefore on either nondegenerate sign sector,

\[
\boxed{
|\det S|\ge\frac\delta3|S|^3.
}
\]

Thus large strain with small determinant is possible only on the near-planar sector `E_0(delta)`.

## 3. Productive sector `E_+`

On `E_+(delta)`,

\[
\lambda_2^+\ge\delta|S|.
\]

Also the negative spectral part is the one-dimensional `lambda_3` direction and

\[
|S_-|\lesssim |S|\le\delta^{-1}\lambda_2^+.
\]

Hence if a fixed positive fraction of the atom-forced compressive `L_t^2L_x^3` action lies in `E_+(delta)`, then

\[
\boxed{
\int^{T_*}\|\lambda_2^+(t)\|_3^2dt=\infty.
}
\]

This is exactly the standard positive-middle critical strain channel already present in the repository.

It is a necessary critical action, not yet a contradiction.

## 4. Negative-middle sector `E_-`

On `E_-(delta)`,

\[
\det S>0,
\]

so this sector contributes negatively to enstrophy production because

\[
Q=\int\omega\cdot S\omega=-4\int\det S.
\]

Define

\[
Q_+(t)=4\int_{\{\lambda_2>0\}}|\det S|dx,
\qquad
Q_-(t)=4\int_{\{\lambda_2<0\}}|\det S|dx.
\]

Then

\[
\boxed{Q=Q_+-Q_-.}
\]

If the atom compressive action on `E_-(delta)` diverges, set

\[
f_-(t)=\|S\mathbf 1_{E_-(\delta)}\|_3.
\]

Since the terminal interval has finite length,

\[
\int f_-^2dt=\infty
\quad\Longrightarrow\quad
\int f_-^3dt=\infty.
\]

The determinant lower bound gives

\[
\boxed{
\int^{T_*}Q_-(t)dt=\infty.
}
\]

But the exact enstrophy identity gives, for every `T<T_*`,

\[
\int_{t_0}^{T}Q_+dt
=\int_{t_0}^{T}Q_-dt
+\frac12[Z(T)-Z(t_0)]
+\nu\int_{t_0}^{T}Pdt.
\]

Therefore

\[
\boxed{
\int^{T_*}Q_-dt=\infty
\Longrightarrow
\int^{T_*}Q_+dt=\infty.
}
\]

So a large negative-middle atom payer cannot act alone: it forces an equally nonintegrable compensating positive-determinant production channel somewhere in the parent flow.

This is a **bipolar compensation structure**, not yet a contradiction.

## 5. Near-planar sector `E_0`

On

\[
|\lambda_2|<\delta|S|,
\]

trace-freeness implies

\[
\lambda_1\simeq-\lambda_3\simeq\frac{|S|}{\sqrt2}
\]

up to `O(delta)` relative errors, while

\[
|\det S|\lesssim\delta|S|^3.
\]

Thus this sector is close to the planar-hyperbolic matrix

\[
\operatorname{diag}(a,0,-a).
\]

It is the only sector where very large compressive strain can be almost invisible to the determinant/Betchov production ledger.

This reproduces, at the spectral level, the exact affine anti-model previously identified in the axis audit.

## 6. Formation reduction

The atom branch now has the exact structural fork

\[
\boxed{
\text{atom compressive action}
\Longrightarrow
\begin{cases}
H_{\lambda_2^+},\\
C_{\det\text{-}bipolar},\\
H_{\rm planar}.
\end{cases}
}
\]

where

- `H_{lambda_2+}` is the existing positive-middle critical action;
- `C_det-bipolar` is simultaneous nonintegrable negative and positive determinant production;
- `H_planar` is near-rank-two planar hyperbolic compression.

The next axis calculation should target `H_planar`, because it is the unique determinant-degenerate large-strain survivor.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
