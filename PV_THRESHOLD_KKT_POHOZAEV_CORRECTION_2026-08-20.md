# KKT-Corrected Pohozaev Balance for the First-Hitting Threshold Maximizer — 2026-08-20

Overall status: **EXACT FORMAL KKT HOMOGENEITY BALANCE — GLOBAL REGULARITY NOT PROVED.**

This note corrects the smooth fixed-amplitude Pohozaev identity by including the active first-hitting constraint `||omega||_infty <= 1`.

---

## 1. Vorticity operator and its adjoint

For a strain field in the whole-space strain constraint class,

\[
\omega=\mathcal B S,
\qquad
\mathcal B S
=\nabla\times[-2\operatorname{div}(-\Delta)^{-1}S].
\]

For a smooth vector test field `f`, integration by parts gives

\[
\boxed{
\mathcal B^*f
=2(-\Delta)^{-1}\operatorname{sym}\nabla(\nabla\times f).
}
\]

This field is symmetric and trace free because `div curl f = 0`.

Thus the formal first-hitting KKT equation can be written

\[
P_{st}\left[
\mathcal E_N
-2\Lambda\Delta^2S
-2\alpha S
-2\beta|x|^2S
\right]
=\mathcal B^*\boldsymbol\mu,
\]

where the vector measure `boldsymbol mu` is supported on the contact set

\[
\mathcal M=\{x:|\omega(x)|=1\}.
\]

---

## 2. KKT reaction scalar

Define the total contact reaction

\[
\boxed{
\Gamma_K
:=\langle\boldsymbol\mu,\omega\rangle.
}
\]

For the standard outward normal-cone sign convention of the active constraint this quantity is nonnegative:

\[
\Gamma_K\ge0.
\]

The rigorous construction of `boldsymbol mu` from a finite-p approximation remains part of the KKT program; the homogeneity calculation below is exact once such a multiplier exists.

---

## 3. Amplitude variation

Under pure amplitude scaling

\[
S_c=cS,
\]

one has

\[
N(cS)=c^3N,
\qquad
H(cS)=c^2H,
\qquad
E(cS)=c^2E,
\qquad
M(cS)=c^2M,
\]

and, because `mathcal B` is linear,

\[
\|\omega_c\|_\infty=c\|\omega\|_\infty.
\]

At the active first-hitting cap `||omega||_infty=1`, the KKT contribution to the amplitude derivative is `Gamma_K`.

Stationarity therefore gives

\[
3N-2\Lambda H-2\alpha E-2\beta M-\Gamma_K=0.
\]

Since `Lambda H=N`,

\[
\boxed{
N-2\alpha E-2\beta M=\Gamma_K.
}
\]

Equivalently,

\[
\boxed{
\alpha E+\beta M=\frac{N-\Gamma_K}{2}.
}
\]

---

## 4. Coordinate-dilation variation

Now use

\[
S_b(x)=S(bx).
\]

The strain/vorticity reconstruction operator `mathcal B` has order zero, so

\[
\omega_b(x)=\omega(bx)
\]

and therefore

\[
\boxed{
\|\omega_b\|_\infty=\|\omega\|_\infty.
}
\]

Thus the active first-hitting constraint makes **no KKT contribution** to coordinate dilation.

The remaining scaling laws are

\[
N(S_b)=b^{-1}N,
\quad
H(S_b)=bH,
\quad
E(S_b)=b^{-3}E,
\quad
M(S_b)=b^{-5}M.
\]

Stationarity gives

\[
-N-\Lambda H+3\alpha E+5\beta M=0,
\]

hence

\[
\boxed{
3\alpha E+5\beta M=2N.
}
\]

---

## 5. Exact corrected Pohozaev balance

Let

\[
A=\alpha E,
\qquad
B=\beta M.
\]

The two equations are

\[
A+B=\frac{N-\Gamma_K}{2},
\]

\[
3A+5B=2N.
\]

Solving gives

\[
\boxed{
\alpha E
=\frac{N-5\Gamma_K}{4},
}
\]

\[
\boxed{
\beta M
=\frac{N+3\Gamma_K}{4}.
}
\]

When `Gamma_K=0`, this reduces to the smooth-slice identity

\[
\alpha E=\beta M=N/4.
\]

---

## 6. Interpretation

The first-hitting contact reaction does not alter the spatial-dilation balance because the `L^infinity` vorticity cap is invariant under coordinate dilation. It does alter the amplitude balance.

As `Gamma_K` increases,

- the effective amplitude multiplier `alpha E` decreases;
- the spatial confinement multiplier `beta M` increases.

Thus strong contact with the maximum-vorticity constraint pushes the variational balance toward stronger moment confinement rather than allowing free spatial broadening.

If

\[
\Gamma_K>N/5,
\]

then `alpha` becomes negative on a fixed positive-energy slice. This is not by itself a contradiction, because `alpha` is an equality-constraint multiplier, but it identifies a distinct contact-dominated regime that can be analyzed separately.

---

## 7. Applying -Delta to the KKT equation

Because

\[
\mathcal B^*\boldsymbol\mu
=2(-\Delta)^{-1}\operatorname{sym}\nabla(\nabla\times\boldsymbol\mu),
\]

applying `-Delta` formally gives a local distributional contact source

\[
\boxed{
-\Delta\mathcal B^*\boldsymbol\mu
=2\operatorname{sym}\nabla(\nabla\times\boldsymbol\mu).
}
\]

Thus the only singular forcing in the sixth-order differentiated threshold equation is supported on the maximum-vorticity contact set. Away from that set the maximizer obeys the homogeneous nonlinear eigen-equation.

---

## 8. Next split

The KKT maximizer now has two natural regimes:

1. **weak-contact regime:** `Gamma_K/N` is bounded away from its large-contact range; the smooth H1 efficiency/Pohozaev structure dominates;
2. **contact-dominated regime:** a fixed fraction of the cubic H1 production is balanced by the `L^infinity` vorticity reaction, forcing large `beta M` and concentrating the remaining obstruction on the geometry of the contact set.

The next useful calculation is therefore to combine the contact-set maximum identities

\[
\nabla|\omega|=0,
\qquad
\Delta|\omega|\le0,
\]

with the KKT source and the first-hitting stretching condition at `|omega|=1`.

Status: **THE ACTIVE FIRST-HITTING CONSTRAINT MODIFIES THE POHOZAEV BALANCE IN A CONTROLLED WAY. THE EXACT FORMAL RELATIONS ARE alpha E=(N-5 Gamma_K)/4 AND beta M=(N+3 Gamma_K)/4. THE CONTACT REACTION AFFECTS AMPLITUDE BALANCE BUT NOT COORDINATE-DILATION BALANCE. GLOBAL REGULARITY REMAINS UNPROVED.**