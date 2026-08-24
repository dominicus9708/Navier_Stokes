# Amplitude–Location Genealogy Bridge

Date: 2026-08-25

Status: **FORWARD MATERIAL-PACKET BRIDGE PROVED / REVERSE ANNULAR-TO-ANCESTOR IDENTIFICATION NOT DERIVED / RADIAL DEPHASING ISOLATED / GLOBAL REGULARITY NOT PROVED.**

## 1. Scope and purpose

The repository already contains the exact scale identity

\[
R_{j,k}^{\mathrm{phys}}=r_{j-k},
\]

where the age-\(k\) annulus at first-hitting stage \(j\) has the same physical radius as the distinguished natural scale at the earlier stage \(n=j-k\).

That identity is purely a radius identity. It does **not** imply that the current annular packet is the same material packet that occupied the earlier maximum-centered core.

This note derives the strongest forward statement that is available without assuming such an identification.

Throughout Sections 2–7 let

\[
n=j-k,
\qquad
W_n=\|\omega(t_n)\|_\infty,
\qquad
r_n=\left(\frac{\nu}{W_n}\right)^{1/2}.
\]

Let \(x_n\) be a first-hitting maximum point at time \(t_n\). The imported first-hitting analyticity corridor gives fixed constants \(a_0,b_0>0\) such that

\[
\boxed{
|\omega(x,t_n)|\ge b_0W_n
\qquad
(x\in B_{a_0r_n}(x_n)).
}
\]

Call this initial occupied ball \(A_n^0\).

---

## 2. Material transport of the occupied ancestor ball

Let \(\Phi_{t_n,t}\) be the smooth Lagrangian flow map before the hypothetical first singular time:

\[
\frac{d}{dt}\Phi_{t_n,t}(a)
=u(\Phi_{t_n,t}(a),t),
\qquad
\Phi_{t_n,t_n}(a)=a.
\]

Define

\[
A_n(t):=\Phi_{t_n,t}(A_n^0),
\qquad
z_n(t):=\Phi_{t_n,t}(x_n).
\]

Because \(\nabla\cdot u=0\), the flow is volume preserving:

\[
\boxed{
|A_n(t)|=|A_n^0|
=\frac{4\pi}{3}a_0^3r_n^3.
}
\]

This is exact for every smooth pre-singular interval.

**Status: PROVED.**

---

## 3. Amplitude retention under strain and diffusion exposure

Along any material trajectory, the vorticity equation is

\[
D_t\omega=S\omega+\nu\Delta\omega,
\]

where \(S=(\nabla u+\nabla u^T)/2\).

At points where \(\omega\ne0\), with \(a(t)=|\omega(\Phi(a_0,t),t)|\),

\[
\frac{d}{dt}a(t)
\ge
-\|S(t)\|_{L^\infty}a(t)
-\nu\|\Delta\omega(t)\|_{L^\infty}.
\]

For an interval \(I=[t_n,t]\), define the dimensionless exposures

\[
\Lambda_I
:=
\int_{t_n}^{t}\|\nabla u(s)\|_{L^\infty}\,ds,
\]

and

\[
\mathcal D_I
:=
\frac{\nu}{W_n}
\int_{t_n}^{t}\|\Delta\omega(s)\|_{L^\infty}\,ds
=
r_n^2
\int_{t_n}^{t}\|\Delta\omega(s)\|_{L^\infty}\,ds.
\]

Since \(\|S\|_\infty\le\|\nabla u\|_\infty\), the integrating-factor inequality gives

\[
\boxed{
\frac{a(t)}{W_n}
\ge
e^{-\Lambda_I}
\left(
\frac{a(t_n)}{W_n}
-e^{\Lambda_I}\mathcal D_I
\right).
}
\]

Therefore, if

\[
\Lambda_I\le L,
\qquad
\mathcal D_I\le \frac{b_0}{2}e^{-L},
\]

then every trajectory starting in \(A_n^0\) obeys

\[
\boxed{
|\omega(\Phi(a,t),t)|
\ge
q_LW_n,
\qquad
q_L:=\frac{b_0}{2}e^{-L}>0.
}
\]

Thus a fixed fraction of the ancestor amplitude survives unless either integrated pointwise deformation or integrated normalized vorticity-Laplacian exposure becomes large.

**Status: PROVED.**

---

## 4. Coherence radius under bounded deformation

For two material trajectories,

\[
\frac{d}{dt}|\Phi(a,t)-\Phi(b,t)|
\le
\|\nabla u(t)\|_\infty
|\Phi(a,t)-\Phi(b,t)|.
\]

Gronwall yields

\[
|\Phi(a,t)-\Phi(b,t)|
\le e^{\Lambda_I}|a-b|.
\]

Applying the same estimate to the inverse flow gives the lower bi-Lipschitz bound

\[
|\Phi(a,t)-\Phi(b,t)|
\ge e^{-\Lambda_I}|a-b|.
\]

Consequently the transported image of the initial ball contains a definite ball around the transported ancestor center:

\[
\boxed{
B_{\rho_I}(z_n(t))
\subset A_n(t),
\qquad
\rho_I=a_0e^{-\Lambda_I}r_n.
}
\]

In particular, on \(\Lambda_I\le L\),

\[
\rho_I\ge a_0e^{-L}r_n.
\]

Combining with Section 3, if deformation and diffusion are quiet then

\[
\boxed{
|\omega(x,t)|\ge q_LW_n
\quad
(x\in B_{a_0e^{-L}r_n}(z_n(t))).
}
\]

This is a genuine material occupied packet at the ancestor natural scale.

**Status: PROVED.**

---

## 5. Contact fraction gives an exact annular \(J\)-cost

At descendant stage \(j\), let \(\mathcal A_{j,k}\) be the physical age-\(k\) annulus used in the definition

\[
J_{j,k}
=
R_{j,k}^{\mathrm{phys}}
\int_{\mathcal A_{j,k}}|\nabla u(x,t_j)|^2dx.
\]

The ancestor-radius identity gives

\[
R_{j,k}^{\mathrm{phys}}=r_n.
\]

Define the normalized material contact fraction

\[
\boxed{
\chi_{j,k}
:=
\frac{
|A_n(t_j)\cap\mathcal A_{j,k}|
}{r_n^3}.
}
\]

Suppose amplitude retention gives

\[
|\omega|\ge qW_n
\]

on the intersecting portion. Since pointwise

\[
|\omega|^2\le2|\nabla u|^2,
\]

we obtain

\[
\begin{aligned}
J_{j,k}
&\ge
\frac{r_n}{2}
\int_{A_n(t_j)\cap\mathcal A_{j,k}}|\omega|^2dx\\
&\ge
\frac{q^2}{2}
r_nW_n^2
|A_n(t_j)\cap\mathcal A_{j,k}|.
\end{aligned}
\]

Using \(W_n=\nu/r_n^2\),

\[
\boxed{
J_{j,k}
\ge
\frac{q^2}{2}\nu^2\chi_{j,k}.
}
\]

Equivalently,

\[
\boxed{
\chi_{j,k}
\le
\frac{2J_{j,k}}{q^2\nu^2}.
}
\]

This is the precise amplitude-location bridge: retained material overlap with the descendant shell cannot be large while the shell amplitude \(J_{j,k}\) is small.

**Status: PROVED.**

---

## 6. Deep radial contact forces order-one shell amplitude

Write the shell geometrically as a fixed-ratio annulus

\[
\mathcal A_{j,k}
=\{x:c_-r_n<|x-X_j|<c_+r_n\},
\qquad
0<c_-<c_+,
\]

up to the fixed cutoff-core constants used by the repository.

On the quiet corridor \(\Lambda_I\le L\), set

\[
\theta_L:=a_0e^{-L},
\qquad
\rho_L=\theta_Lr_n.
\]

If the transported ancestor center satisfies the deep-contact condition

\[
\boxed{
(c_-+\theta_L)r_n
\le
|z_n(t_j)-X_j|
\le
(c_+-\theta_L)r_n,
}
\]

then

\[
B_{\rho_L}(z_n(t_j))\subset\mathcal A_{j,k}.
\]

The contact fraction is therefore at least

\[
\chi_{j,k}\ge \frac{4\pi}{3}\theta_L^3.
\]

Together with the amplitude-retention bound \(q=q_L\),

\[
\boxed{
J_{j,k}
\ge
c(a_0,b_0,L,c_\pm)\,\nu^2.
}
\]

Hence a shell with

\[
J_{j,k}/\nu^2\to0
\]

cannot be the deep annular intersection of a quietly transported ancestor maximum packet.

**Status: PROVED CONDITIONAL only on the explicit quiet-exposure and deep-contact hypotheses.**

---

## 7. Forward genealogy escape theorem

For the ancestor occupied first-hitting packet over \(I=[t_n,t_j]\), fix a deformation threshold \(L>0\).

At least one of the following must occur:

### A. Large deformation exposure

\[
\boxed{
\Lambda_I
=
\int_I\|\nabla u\|_\infty dt
>L.
}
\]

### B. Large normalized diffusion/derivative exposure

\[
\boxed{
\mathcal D_I
=
\frac{\nu}{W_n}
\int_I\|\Delta\omega\|_\infty dt
>
\frac{b_0}{2}e^{-L}.
}
\]

### C. Coherent amplitude-retaining material packet survives

There exists

\[
B_{a_0e^{-L}r_n}(z_n(t_j))
\subset A_n(t_j)
\]

on which

\[
|\omega|\ge q_LW_n.
\]

In branch C, either:

1. the packet has nontrivial contact with \(\mathcal A_{j,k}\), in which case
   \[
   J_{j,k}\ge \frac{q_L^2}{2}\nu^2\chi_{j,k};
   \]
2. or its contact fraction is small, which is a **radial/location dephasing event** relative to the current age-\(k\) shell.

Thus

\[
\boxed{
\text{ancestor first-hitting occupied packet}
\Longrightarrow
\begin{cases}
\text{large strain/deformation exposure},\\
\text{large diffusion/fixed-derivative exposure},\\
\text{annular }J\text{-cost},\\
\text{radial/location dephasing}.
\end{cases}
}
\]

**Status: PROVED as a forward conditional genealogy decomposition.**

---

## 8. Important consequence for diffuse cubic tails

Suppose along a remote-shell subsequence

\[
J_{j,k}/\nu^2\to0.
\]

If both deformation and diffusion exposures remain uniformly quiet, then the ancestor packet retains a fixed amplitude and a fixed \(r_n^3\)-scale volume.

Section 5 then forces

\[
\boxed{
\chi_{j,k}\to0.
}
\]

Therefore a diffuse small-\(J\) shell cannot be identified with a quietly transported first-hitting maximum packet occupying a fixed fraction of that annulus.

This is a useful negative identification result:

\[
\boxed{
J_{j,k}\to0
+\text{quiet ancestor transport}
\Longrightarrow
\text{material genealogy dephases from the annulus}.
}
\]

Hence the non-\(L^3\) cubic tail, if carried by amplitudes tending to zero, must be generated by one or more of:

- loss of material amplitude through strain/diffusion exposure;
- migration away from the annular location;
- replacement by a different packet / center switch;
- non-material rebuilding of shell structure.

It cannot simply be the same maximum-centered ancestor packet sitting quietly at its matching scale.

**Status: PROVED within the explicit quiet-exposure hypothesis.**

---

## 9. What is still not derived

The reverse implication

\[
\boxed{
J_{j,k}>0
\stackrel{?}{\Longrightarrow}
\text{the shell comes from the stage }j-k\text{ maximum packet}
}
\]

is **NOT DERIVED**.

The exact radius identity does not supply this reverse material identification.

Likewise, the present calculation does not prove that radial dephasing has a large ordinary energy cost. A current first-hitting center may switch to a different packet, and absolute translation is Galilean-dependent.

The correct next object is therefore not an absolute center displacement. It is a Galilean-invariant dichotomy between

1. **transport dephasing of the same packet**, which should force integrated relative deformation; and
2. **center/packet switching**, which creates multiplicity of occupied critical packets and should be charged through a packing/time-overlap ledger.

---

## 10. Audit table

| Statement | Status |
|---|---|
| Ancestor first-hitting analytic core contains an \(O(r_n)\) occupied ball | PROVED by imported analyticity corridor |
| Material flow preserves its volume | PROVED |
| Quiet strain + quiet Laplacian exposure retain a fixed vorticity fraction | PROVED |
| Bounded integrated \(\|\nabla u\|_\infty\) keeps an \(O(r_n)\) coherent material ball | PROVED |
| Contact fraction \(\chi\) forces \(J\ge(q^2/2)\nu^2\chi\) | PROVED |
| Deep annular contact forces \(J\gtrsim\nu^2\) | PROVED CONDITIONAL |
| Small \(J\) + quiet transport forces vanishing ancestor/shell overlap | PROVED |
| Radius matching alone identifies the same material packet | FALSE |
| Current annular \(J\) automatically comes from the ancestor maximum packet | NOT DERIVED |
| Radial dephasing automatically contradicts finite energy | NOT DERIVED |
| Global regularity | UNPROVED |

---

## 11. Updated frontier

The amplitude/location problem is no longer an undifferentiated missing arrow.

The forward material bridge is now explicit:

\[
\boxed{
\text{ancestor occupied packet}
\to
\text{strain}
\lor
\text{diffusion/derivative}
\lor
J\text{-contact}
\lor
\text{location dephasing}.
}
\]

The unresolved genealogy problem is concentrated in

\[
\boxed{
\text{location dephasing}
\quad\text{and}\quad
\text{packet/center switching}.
}
\]

These must be handled Galilean-invariantly; absolute center motion by itself is not a legitimate contradiction mechanism.