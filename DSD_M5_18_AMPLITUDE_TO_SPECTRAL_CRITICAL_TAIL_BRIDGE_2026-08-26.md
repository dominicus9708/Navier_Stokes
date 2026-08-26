# DSD M5-18 — Amplitude-to-Spectral Critical Tail Bridge

Date: 2026-08-26

Status: **DERIVED SUFFICIENT SPECTRAL FORM OF M5 / EXACT RECOVERY OF THE M5-1 TIME-AVERAGED EXPONENT / UNIFORM SPECTRAL TIGHTNESS REMAINS OPEN / GLOBAL REGULARITY UNPROVED.**

## 1. Physical amplitude defect

Recall

\[
K_L^{phys}(t)
:=
\frac L2\int (|u(x,t)|^2-L^2)_+dx.
\]

M5 asks for uniform smallness of this quantity as `L->infinity`.

Let

\[
E_0:=\sup_{t<T_*}\|u(t)\|_2^2<\infty.
\]

## 2. Low/high Fourier split

Let

\[
u=u_{\le\kappa}+u_{>\kappa}
\]

be a standard smooth Fourier decomposition.

Bernstein gives

\[
\|u_{\le\kappa}\|_\infty
\le
C_B\kappa^{3/2}\|u\|_2
\le
C_B\kappa^{3/2}E_0^{1/2}.
\]

For a velocity threshold `L`, choose

\[
\boxed{
\kappa_L
:=
\left(
\frac{L}{2C_BE_0^{1/2}}
\right)^{2/3}.
}
\]

Then

\[
\|u_{\le\kappa_L}\|_\infty\le L/2.
\]

## 3. High amplitude must come from the high-frequency part

On the set `|u|>L`, write `u=l+h` with `|l|<=L/2` and `h=u_{>\kappa_L}`.

Then

\[
|u|^2
\le
2|h|^2+2|l|^2
\le
2|h|^2+\frac{L^2}{2}.
\]

Hence

\[
(|u|^2-L^2)_+
\le
2|h|^2.
\]

Therefore

\[
\boxed{
K_L^{phys}(t)
\le
L\|P_{>\kappa_L}u(t)\|_2^2.
}
\]

This converts the amplitude defect into a sufficient spectral-tail condition.

## 4. Canonical spectral form

Since

\[
L=2C_BE_0^{1/2}\kappa_L^{3/2},
\]

we obtain

\[
K_L^{phys}(t)
\le
C E_0^{1/2}\kappa_L^{3/2}
\|P_{>\kappa_L}u(t)\|_2^2.
\]

Thus a sufficient M5 theorem is

\[
\boxed{
\lim_{\kappa\to\infty}
\sup_{t_0<t<T_*}
E_0^{1/2}\kappa^{3/2}
\|P_{>\kappa}u(t)\|_2^2
=0.
}
\]

This condition is scale invariant once the scale-breaking global-energy anchor `E_0` is included.

## 5. Recovery of the M5-1 time-average exponent

The high-frequency energy satisfies

\[
\|P_{>\kappa}u\|_2^2
\le
\kappa^{-2}\|\nabla u\|_2^2.
\]

Hence

\[
\int_{t_0}^{T_*}K_L^{phys}(t)dt
\le
L\kappa_L^{-2}
\int_{t_0}^{T_*}\|\nabla u\|_2^2dt.
\]

Because

\[
\kappa_L^{-2}
\asymp
E_0^{2/3}L^{-4/3},
\]

we recover

\[
\boxed{
\int_{t_0}^{T_*}K_L^{phys}(t)dt
\lesssim
E_0^{2/3}L^{-1/3}
\int_{t_0}^{T_*}\|\nabla u\|_2^2dt.
}
\]

This is exactly the exponent found independently in M5-1.

Therefore the amplitude and spectral descriptions are consistent manifestations of the same critical concentration barrier.

## 6. DSD interpretation

The amplitude coordinate and Fourier coordinate are not independent channels:

\[
\boxed{
\text{large velocity amplitude}
\Rightarrow
\text{energy above a corresponding frequency scale},
}
\]

once the low-frequency part is bounded using the finite global energy anchor.

The scale relation is

\[
\boxed{
\kappa_L\asymp
\left(\frac{L}{E_0^{1/2}}\right)^{2/3}.
}
\]

The unusual exponent `2/3` is exactly what converts the ordinary dissipation tail `kappa^{-2}` into the amplitude time-average exponent `L^{-1/3}`.

## 7. What is not proved

The energy inequality gives only time-integrated high-frequency tightness. It does not yield

\[
\sup_t\kappa^{3/2}\|P_{>\kappa}u(t)\|_2^2\to0.
\]

Thus M5-18 does not close the problem. It replaces the open amplitude-tail theorem by an explicit sufficient **spectral critical-tail theorem**.

## 8. Updated target

Future spectral/helical estimates should be judged by whether they improve the quantity

\[
\boxed{
\mathfrak S(\kappa,t)
:=
E_0^{1/2}\kappa^{3/2}
\|P_{>\kappa}u(t)\|_2^2.
}
\]

If `mathfrak S` can be shown uniformly small at sufficiently large `kappa`, M5 closes through the already proved amplitude-tail absorption lemma.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
