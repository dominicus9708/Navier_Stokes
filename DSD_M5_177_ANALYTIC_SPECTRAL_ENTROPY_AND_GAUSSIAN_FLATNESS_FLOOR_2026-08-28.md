# DSD M5-177 — Analytic Spectral Entropy and Gaussian Flatness Floor

Date: 2026-08-28

Status: **P1_B^S ANALYTIC-ENERGY REFINEMENT / UNIFORM CROSS-SECTION ANALYTICITY CONVERTS THE DIRICHLET MEAN INTO A LOGARITHMIC AMPLITUDE BOUND / COMBINED WITH THE GLOBAL M5-175 ENERGY INEQUALITY, ANY NONZERO FLAT FIBER WOULD HAVE TO DECAY AT LEAST LIKE `exp(-c/z)=exp(-c r^2)` IN THE INVARIANT PAIR ENERGY / THIS IS MUCH STRONGER THAN SUPERALGEBRAIC FLATNESS BUT IS NOT BY ITSELF DECLARED A BACKWARD-UNIQUENESS CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Uniform analytic spectral envelope

Use the M5-155 time-analytic scale together with the previously audited scaled-shell spatial analyticity.  After reducing the analytic radius once, fix

\[
\delta>0
\]

and a uniform W1-class constant `M<infinity` such that on the statistical same-tail branch

\[
\boxed{
\|e^{\delta\sqrt A}F(z)\|\le M
}
\]

for all sufficiently small `z`.

Here

\[
A=1-4G^2-\Delta_{S^2}\ge1.
\]

This is an absolute analytic ceiling; it is not divided by the possibly tiny amplitude `||F||`.

---

## 2. Analytic tail estimate

Let

\[
E:=\|F\|^2,
\qquad
N:=\frac{\langle AF,F\rangle}{E}.
\]

For a spectral threshold `L>=1`, split

\[
F=P_{\sqrt A\le L}F+P_{\sqrt A>L}F.
\]

The low part contributes at most

\[
L^2E
\]

to `\langle AF,F\rangle`.

For the high part, the analytic ceiling gives exponentially decaying spectral moments.  In particular, after decreasing `delta` by a fixed factor if needed,

\[
\int_{\sqrt A>L}A\,d\|E_AF\|^2
\le
C_\delta M^2(1+L)^2e^{-2\delta L}.
\]

Hence

\[
N
\le
L^2
+
C_\delta\frac{M^2}{E}(1+L)^2e^{-2\delta L}.
\]

Choose

\[
L
\simeq
\delta^{-1}
\left[
1+\log\left(\frac{M}{\sqrt E}\right)
\right]
\]

with a fixed harmless enlargement to absorb the polynomial factor.  Then

\[
\boxed{
N
\le
C_\delta
\left[
1+\log^2\left(\frac{M^2}{E}\right)
\right].
}
\]

This is the analytic spectral entropy bound.

---

## 3. Amplitude variable

Define

\[
\boxed{
L_E(\tau)
:=
1+\log\left(\frac{M^2}{E(\tau)}\right)
\ge1.
}
\]

Section 2 gives

\[
\boxed{N\le C_\delta L_E^2.}
\]

M5-175 gives

\[
\frac d{d\tau}\log E
\ge
-Cz(1+N).
\]

Therefore

\[
\boxed{
(L_E)_\tau
\le
C_1zL_E^2
}
\]

for a fixed W1/analytic constant `C_1`.

---

## 4. Terminal-zero condition forces Gaussian normal decay

A nonzero flat fiber satisfies

\[
E(\tau)\to0,
\]

hence

\[
L_E(\tau)\to\infty.
\]

Set

\[
Y:=L_E^{-1}.
\]

Then

\[
Y_\tau
=-\frac{(L_E)_\tau}{L_E^2}
\ge
-C_1z.
\]

Since

\[
Y(\infty)=0
\]

and

\[
\int_\tau^\infty z(s)ds=z(\tau),
\]

integration from `tau` to infinity yields

\[
0-Y(\tau)
\ge
-C_1z(\tau).
\]

Thus

\[
\boxed{
Y(\tau)\le C_1z(\tau)
}
\]

and hence

\[
\boxed{
L_E(\tau)
\ge
\frac{c}{z(\tau)}.
}
\]

Therefore

\[
\boxed{
E(\tau)
\le
M^2\exp\left[-\frac{c}{z(\tau)}\right].
}
\]

Because

\[
z=r^{-2},
\]

this is

\[
\boxed{
E(r)\le M^2e^{-cr^2}.
}
\]

Thus any surviving flat statistical fiber is forced into at least a Gaussian-in-radius energy decay class.

---

## 5. Relation to M5-176

M5-176 separately proves

\[
zN\to\infty.
\]

Together with the analytic entropy bound,

\[
N\le C_\delta L_E^2,
\]

we also obtain

\[
\boxed{
\sqrt z\,L_E\to\infty.
}
\]

This is weaker than the Gaussian floor `L_E>=c/z` already obtained in Section 4, but confirms that the mean-superparabolic escape is compatible only with an extremely small amplitude.

---

## 6. DSD audit

### Formation — GREEN

The analytic norm is an existing W1 regularity input and `L_E` is derived from the actual pair energy.

### Axis — GREEN

Analytic spectral radius, normal depth, and pair amplitude remain distinct quantities.

### Static aggregation — GREEN

No frequency-to-amplitude ratio is assumed.  The ratio is derived by a spectral low/high split using the absolute analytic ceiling.

### Dynamics — GREEN

The Gaussian floor follows from the global M5-175 energy differential inequality and the terminal flat condition.

### Cross-audit — GREEN

This does not revive the M5-152 same-norm derivative shortcut and does not assume Gaussian regularity of the solution.  Gaussian **decay of the flat difference** is a consequence, not an input.

---

## 7. Updated frontier

The remaining statistical flat branch must simultaneously satisfy

\[
\boxed{
\begin{aligned}
&zN\to\infty,\\
&E\le M^2e^{-c/z},\\
&\|e^{\delta\sqrt A}F\|\le M.
\end{aligned}
}
\]

The next audit is whether an existing backward-uniqueness/unique-continuation theorem applies to this **Gaussian terminal-normal class** for the actual same-tail relative Navier--Stokes/Stokes system.  If not, the exact Fuchsian system must be pushed one step further to determine whether the Gaussian critical class can be sustained internally.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
