# DSD M5-587 — Forced Finite-Depth Enstrophy Production Shell

Date: 2026-09-02

Status: **EVERY NONTRIVIAL HARD ERGODIC TERMINAL-VORTICITY BRANCH FORCES AT LEAST ONE FINITE WEDGE DEPTH / SIMILARITY RADIUS WHERE TIME-AVERAGED VORTEX STRETCHING STRICTLY EXCEEDS VORTICITY-GRADIENT DISSIPATION BY THE LOCAL DAMPING AMOUNT. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Start from the averaged wedge enstrophy ODE

M5-585 gives

\[
\boxed{
\mathscr K_\omega'
+2z\mathscr J_\omega'
+3\mathscr J_\omega
=
\mathscr P_\omega-\mathscr Q_\omega.
}
\]

Here

\[
\mathscr K_\omega\ge0
\]

is q-averaged spherical vorticity-enstrophy density,

\[
\mathscr P_\omega\ge0
\]

is vorticity-gradient dissipation, and \(\mathscr Q_\omega\) is vortex-stretching production.

---

## 2. Define the finite-depth boundary functional

Motivated by the weighted integration in M5-585, define

\[
\boxed{
\mathscr Y_\omega(z)
:=
\frac12z^{1/2}\mathscr K_\omega(z)
+z^{3/2}\mathscr J_\omega(z).
}
\]

Differentiate:

\[
\begin{aligned}
\mathscr Y_\omega'
&=
\frac14z^{-1/2}\mathscr K_\omega
+\frac12z^{1/2}\mathscr K_\omega'
+\frac32z^{1/2}\mathscr J_\omega
+z^{3/2}\mathscr J_\omega'.
\end{aligned}
\]

Using the wedge ODE,

\[
\frac12z^{1/2}
(\mathscr K_\omega'
+2z\mathscr J_\omega'
+3\mathscr J_\omega)
=
\frac12z^{1/2}
(\mathscr P_\omega-\mathscr Q_\omega).
\]

Therefore

\[
\boxed{
\mathscr Y_\omega'(z)
=
\frac14z^{-1/2}\mathscr K_\omega(z)
+
\frac12z^{1/2}
[\mathscr P_\omega(z)-\mathscr Q_\omega(z)].
}
\]

---

## 3. Terminal behavior

M5-571 gives a positive terminal vorticity density

\[
\boxed{
\mathscr K_\omega(0)=K_0>0.
}
\]

M5-586 gives regular expansions at \(z=0\), so

\[
\mathscr Y_\omega(z)
=
\frac12K_0z^{1/2}
+O(z^{3/2}).
\]

Hence

\[
\boxed{
\mathscr Y_\omega(z)>0
\quad\text{for all sufficiently small }z>0.
}
\]

Also

\[
\boxed{
\mathscr Y_\omega(0)=0.
}
\]

---

## 4. Deep-core behavior

As \(z\to\infty\), the similarity radius

\[
|y|=z^{-1/2}
\]

tends to the smooth Type-I center.

Because

\[
W=zG
\]

remains smooth/bounded there,

\[
G=O(z^{-1}),
\]

so

\[
\mathscr K_\omega=O(z^{-2}).
\]

Therefore

\[
\frac12z^{1/2}\mathscr K_\omega
=O(z^{-3/2})\to0.
\]

The wedge enstrophy flux has the corresponding smooth-center decay, giving

\[
z^{3/2}\mathscr J_\omega(z)\to0.
\]

Hence

\[
\boxed{
\lim_{z\to\infty}\mathscr Y_\omega(z)=0.
}
\]

---

## 5. Existence of a positive interior maximum

We now have

\[
\mathscr Y_\omega(0)=0,
\]

\[
\mathscr Y_\omega(z)>0
\quad\text{for small }z>0,
\]

and

\[
\mathscr Y_\omega(z)\to0
\quad(z\to\infty).
\]

By continuity, \(\mathscr Y_\omega\) has a positive maximum at some finite

\[
\boxed{z_*\in(0,\infty).}
\]

At that point,

\[
\boxed{\mathscr Y_\omega'(z_*)=0.}
\]

Moreover

\[
\boxed{\mathscr K_\omega(z_*)>0.}
\]

Indeed, if \(\mathscr K_\omega(z_*)=0\), nonnegativity and smoothness force the local first derivative of the spherical enstrophy density to vanish there; the enstrophy flux also vanishes, giving \(\mathscr Y_\omega(z_*)=0\), contradicting positivity of the maximum.

---

## 6. Exact finite-depth production surplus

Set \(\mathscr Y_\omega'(z_*)=0\). Then

\[
0
=
\frac14z_*^{-1/2}\mathscr K_\omega(z_*)
+rac12z_*^{1/2}
[\mathscr P_\omega(z_*)-\mathscr Q_\omega(z_*)].
\]

Therefore

\[
\boxed{
\mathscr Q_\omega(z_*)
-
\mathscr P_\omega(z_*)
=
\frac{\mathscr K_\omega(z_*)}{2z_*}
>0.
}
\]

Thus there exists a finite wedge depth where mean vortex stretching strictly dominates mean vorticity-gradient dissipation.

This is stronger than merely knowing the global integral \(\langle Q\rangle>0\).

---

## 7. Similarity-sphere formulation

Let

\[
\rho_*=z_*^{-1/2}.
\]

Recall

\[
W=zG,
\]

and

\[
\nabla_yU=z\,\mathbb G_F.
\]

Therefore on a fixed similarity sphere,

\[
W\cdot\Sigma_UW
=z^3\mathcal Q_F,
\]

\[
|\nabla_yW|^2
=z^3\mathcal P_G,
\]

and

\[
|W|^2=2z^2K.
\]

Multiplying the finite-depth equality by \(z_*^3\) gives the time/q-averaged sphere identity

\[
\boxed{
\left\langle
\int_{S_{\rho_*}}
W\cdot\Sigma_UW\,dS_y
\right\rangle
-
\left\langle
\int_{S_{\rho_*}}
|\nabla_yW|^2\,dS_y
\right\rangle
=
\frac14
\left\langle
\int_{S_{\rho_*}}|W|^2\,dS_y
\right\rangle
>0,
}
\]

up to the common positive geometric sphere factor already absorbed consistently in the wedge definitions.

Equivalently,

\[
\boxed{
\langle Q_{sphere}(\rho_*)\rangle
=
\langle P_{sphere}(\rho_*)\rangle
+rac14\langle E_{sphere}(\rho_*)\rangle.
}
\]

---

## 8. New structural marker

Define a **finite-depth production shell** as a similarity radius satisfying

\[
\boxed{
\langle Q_{sphere}\rangle
-
\langle P_{sphere}\rangle
=
\frac14\langle E_{sphere}\rangle>0.
}
\]

M5-587 proves that every nontrivial hard terminal-vorticity branch contains at least one such shell.

Thus the final survivor must possess not only:

- a recurrent core;
- a positive-density critical terminal trace;
- persistent material/dual-flux lineages;

but also a finite similarity radius where stretching has a strict time-averaged local surplus over diffusion.

---

## 9. Why this is not yet a contradiction

The identity is perfectly compatible with a recurrent Type-I flow if the finite-depth shell continuously receives enough stretching production.

It does not force secular growth because radial enstrophy transport can redistribute the produced vorticity.

The gain is localization, not closure.

The next high-value step is to compare this forced production shell with the M5-487/M5-491 directional decomposition and the persistent dual-flux pair:

\[
Q=\int\rho^2\sigma,
\]

\[
P=P_{mag}+P_{dir}.
\]

At \(z_*\), one can ask whether the strict surplus must be paid predominantly by axial stretching on the persistent dual pair or whether radial/magnitude channels can absorb it. That produces a finite-depth version of the earlier tilt/tension dichotomy.

Status: **A FINITE-DEPTH STRETCHING-DOMINANT SHELL IS NOW FORCED ON EVERY HARD ERGODIC TERMINAL-VORTICITY BRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**