# Terminal Analytic Window and Dissipation Gate

Date: 2026-08-25

Status: **TAWPG PROVED ON THE EXISTING NON-H/T RECURRENT FIRST-HITTING CORRIDOR / TERMINAL LOCAL-ENSTROPHY CONCENTRATION PAYS A UNIFORM PARABOLIC L2-GRADIENT CHARGE / EULERIAN REMOTE-WITNESS TO TERMINAL-LOCAL-CONCENTRATION IDENTIFICATION STILL OPEN / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

`ANALYTIC_W13_TO_L2_GENEALOGY_BRIDGE_2026-08-25.md` reduced the temporal genealogy problem to the Terminal Analytic Window Propagation Gate (TAWPG): can the pointwise analytic/deformation ceiling available at a first-hitting snapshot be propagated uniformly over a fixed terminal parabolic subwindow?

On the existing non-H/T recurrent first-hitting corridor the answer is yes. The proof uses only:

1. the first-hitting cap before the checkpoint;
2. the same short-time analyticity restart theorem already imported by the repository;
3. the positive lower bound on normalized stage length;
4. the bounded endpoint-enstrophy branch and the existing in-stage enstrophy amplification bound.

The second part of the note then upgrades the local-enstrophy persistence/crossing alternative to a **time-integrated critical L2 gradient charge**.

---

## 2. First-hitting terminal window lies inside the previous stage

Let

\[
W_j=qW_{j-1},
\qquad
r_j=\left(\frac\nu{W_j}\right)^{1/2}.
\]

Write

\[
\tau_{j-1}:=W_{j-1}(t_j-t_{j-1}).
\]

On the existing recurrent non-H/T stage corridor,

\[
\tau_{j-1}\ge\tau_-:=\frac{L_-}{q}>0.
\]

Therefore

\[
W_j(t_j-t_{j-1})
=q\tau_{j-1}
\ge L_-.
\]

Choose once and for all

\[
\boxed{0<\alpha_0<L_-.}
\]

Then

\[
\boxed{
I_j^{an}:=
\left[t_j-\alpha_0W_j^{-1},t_j\right]
\subset[t_{j-1},t_j].
}
\]

Since

\[
W_j^{-1}=\frac{r_j^2}{\nu},
\]

this is a fixed terminal parabolic window:

\[
\boxed{
|I_j^{an}|=\alpha_0\frac{r_j^2}{\nu}.}
\]

Status: **PROVED.**

---

## 3. Restart analyticity at every time in the terminal window

The repository's first-hitting analyticity theorem is used as follows: if the solution is restarted at a time \(a\) with

\[
\|\omega(a)\|_\infty\le W,
\]

then there is a universal \(c_{an}>0\) such that the analytic lifespan is at least

\[
c_{an}W^{-1},
\]

and after any fixed elapsed fraction

\[
\theta_{an}W^{-1},
\qquad 0<\theta_{an}<c_{an},
\]

the spatial analyticity radius is comparable to

\[
\sqrt{\nu\theta_{an}/W}
\]

with a complex vorticity amplitude bounded by a universal multiple of \(W\).

By first hitting,

\[
\boxed{
\|\omega(t)\|_\infty\le W_j
\qquad(t\le t_j).
}
\]

Fix any \(t\in I_j^{an}\). Restart the solution at

\[
a_t=t-\theta_{an}W_j^{-1}.
\]

For all sufficiently late \(j\), \(a_t>0\), and the first-hitting cap gives

\[
\|\omega(a_t)\|_\infty\le W_j.
\]

Applying the same analyticity theorem to every such \(t\) gives uniform constants \(\rho_0,M_0\), independent of \(j\) and \(t\in I_j^{an}\), in the parent variables

\[
y=\frac{x-X}{r_j},
\qquad
\Omega_j(y,t)=\frac{\omega(x,t)}{W_j},
\]

such that

\[
\boxed{
\sup_{t\in I_j^{an}}
\sup_{|\operatorname{Im}y|<\rho_0}
|\Omega_j(y,t)|
\le M_0.
}
\]

Consequently for every fixed derivative order \(m\),

\[
\boxed{
\sup_{t\in I_j^{an}}
\|\nabla_y^m\Omega_j(t)\|_\infty
\le C_m(M_0,\rho_0).
}
\]

This is the terminal-window extension of the checkpoint Cauchy estimate.

Status: **PROVED by repeated application of the already imported restart theorem.**

---

## 4. Uniform terminal-window enstrophy ceiling

The terminal window lies in the previous first-hitting stage \([t_{j-1},t_j]\).

The existing in-stage enstrophy amplification theorem gives, in the parent \(j-1\) normalization,

\[
\frac{r_{j-1}}{\nu^2}\|\omega(t)\|_2^2
\le
Z_*\exp\left(\frac{2L_+}{\sqrt3}\right)
\qquad(t\in[t_{j-1},t_j]).
\]

Since

\[
r_{j-1}=q^{1/2}r_j,
\]

the \(r_j\)-normalized enstrophy satisfies

\[
\boxed{
\widetilde Z_j(t)
:=
\frac{r_j}{\nu^2}\|\omega(t)\|_2^2
\le
q^{-1/2}Z_*
\exp\left(\frac{2L_+}{\sqrt3}\right)
=:Z_{an,+}.
}
\]

Thus the entire terminal analytic window has both a pointwise derivative ceiling and a bounded normalized enstrophy ceiling.

Status: **PROVED on the stated corridor.**

---

## 5. Uniform velocity-gradient ceiling on the terminal window

Let

\[
C_1:=C_1(M_0,\rho_0).
\]

The endpoint-Riesz-safe strain interpolation gives

\[
\|\Sigma\|_\infty
\le
C_I
\|\nabla\Omega\|_\infty^{3/5}
\|\Omega\|_2^{2/5}.
\]

Using Sections 3--4,

\[
\boxed{
\|\Sigma_j(t)\|_\infty
\le
C_I C_1^{3/5}Z_{an,+}^{1/5}
\qquad(t\in I_j^{an}).
}
\]

The antisymmetric part is bounded algebraically by \(\|\Omega_j\|_\infty\le M_0\). Hence

\[
\boxed{
\sup_{t\in I_j^{an}}
\|\nabla U_j(t)\|_\infty
\le
A_{an}<\infty,
}
\]

where one may take

\[
A_{an}
=C_A M_0
+C_I C_1^{3/5}Z_{an,+}^{1/5}.
\]

In physical variables,

\[
\boxed{
\|\nabla u(t)\|_\infty
\le
A_{an}\frac{\nu}{r_j^2}
\qquad(t\in I_j^{an}).
}
\]

Thus TAWPG is established on the existing recurrent non-H/T bounded-Z corridor.

---

## 6. Automatic critical L3-vorticity bound on fixed matching scales

Let \(R\) be a physical radius satisfying

\[
c_-r_j\le R\le c_+r_j
\]

with fixed positive \(c_\pm\). On a ball/shell of volume \(\lesssim R^3\), the first-hitting cap gives

\[
\|\omega\|_{L^3(E)}
\le
|E|^{1/3}W_j
\le C R W_j.
\]

Therefore

\[
q_R:=R\|\omega\|_{L^3(E)}
\le C R^2W_j.
\]

Since \(W_jr_j^2=\nu\),

\[
\boxed{
q_R\le Q_0\nu
}
\]

with \(Q_0\) depending only on the fixed radius ratio and cutoff geometry.

Hence the `large critical L3 vorticity` escape in the local-enstrophy gate is automatically bounded on the fixed matching-scale terminal window. It need not remain a separate branch there.

Status: **PROVED.**

---

## 7. Integrated L2 cost from the cutoff-diffusion channel

Let

\[
G_R(t):=R\int_{B_{4R}}|\nabla u|^2dx.
\]

Suppose the cutoff-diffusion contribution on an interval \(I\subset I_j^{an}\) satisfies

\[
\frac\nu2
\int_I\int |\omega|^2|\Delta\psi_R|dxdt
\ge
\delta\frac{\nu^2}{R}.
\]

Using

\[
|\Delta\psi_R|\le CR^{-2},
\qquad
|\omega|^2\le2|\nabla u|^2,
\]

we obtain

\[
\delta\frac{\nu^2}{R}
\le
C\frac\nu{R^2}
\int_I\int_{A_R^\partial}|\nabla u|^2dxdt.
\]

Thus

\[
\boxed{
\int_I G_R(t)dt
\ge
c\delta\,\nu R^2.
}
\]

Status: **PROVED.**

---

## 8. Integrated L2 cost from relative boundary transport

The local-enstrophy gate gives

\[
|B_R(t)|
\le
CR^{-3}G_R(t)^{1/2}(q_R^\partial(t))^2.
\]

By Section 6,

\[
q_R^\partial\le Q_0\nu.
\]

If

\[
\int_I|B_R(t)|dt
\ge
\delta\frac{\nu^2}{R},
\]

then

\[
\int_I G_R(t)^{1/2}dt
\ge
c\frac{\delta}{Q_0^2}R^2.
\]

For

\[
|I|\le\alpha_0\frac{R^2}{\nu}
\]

(up to the fixed matching-radius ratio), Cauchy-Schwarz gives

\[
\left(\int_I G_R^{1/2}dt\right)^2
\le
|I|\int_I G_Rdt.
\]

Therefore

\[
\boxed{
\int_I G_R(t)dt
\ge
c
\frac{\delta^2}{\alpha_0Q_0^4}
\nu R^2.
}
\]

Status: **PROVED.**

---

## 9. Integrated L2 cost from stretching

The stretching estimate is

\[
|S_R(t)|
\le
R^{-3}g_R(t)(q_R^c(t))^2,
\]

with

\[
g_R(t)=R\|\nabla u\|_{L^3(B_{2R})}.
\]

Section 6 gives

\[
q_R^c\le Q_0\nu.
\]

If

\[
\int_I|S_R(t)|dt
\ge
\delta\frac{\nu^2}{R},
\]

then

\[
\boxed{
\int_I g_R(t)dt
\ge
c\frac{\delta}{Q_0^2}R^2.
}
\]

On the terminal analytic window, Section 5 yields

\[
\|\nabla u\|_\infty
\le
A_{an}\frac\nu{R^2}
\]

up to the fixed radius ratio. Hence

\[
\|\nabla u\|_3^3
\le
\|\nabla u\|_\infty\|\nabla u\|_2^2
\]

becomes

\[
\boxed{
g_R(t)^3\le C A_{an}\nu G_R(t).}
\]

Therefore

\[
\int_I G_Rdt
\ge
\frac{c}{A_{an}\nu}
\int_I g_R^3dt.
\]

By Holder in time,

\[
\int_I g_R^3dt
\ge
\frac{\left(\int_I g_Rdt\right)^3}{|I|^2}.
\]

Using \(|I|\le C\alpha_0R^2/\nu\),

\[
\boxed{
\int_I G_R(t)dt
\ge
c
\frac{\delta^3}{A_{an}\alpha_0^2Q_0^6}
\nu R^2.
}
\]

Thus the former W^{1,3} stretching bottleneck pays a genuine time-integrated L2 deformation charge inside the analytic window.

Status: **PROVED.**

---

## 10. Long persistence also pays the same scale of charge

Suppose the local-enstrophy last-crossing time \(t_c\) satisfies

\[
t_*-t_c\ge\alpha_0\frac{R^2}{\nu}.
\]

Then throughout a final interval of that length,

\[
W_R(t)\ge\varepsilon\frac{\nu^2}{R}.
\]

Since

\[
W_R(t)\le2\int_{B_{2R}}|\nabla u|^2dx,
\]

we have

\[
G_R(t)\ge\frac\varepsilon2\nu^2.
\]

Integrating over the persistent interval gives

\[
\boxed{
\int G_R(t)dt
\ge
c\varepsilon\alpha_0\nu R^2.
}
\]

Status: **PROVED.**

---

## 11. Terminal concentration charge theorem

Assume at a terminal first-hitting checkpoint or matching terminal slice

\[
W_R(t_*)
\ge
2\varepsilon\frac{\nu^2}{R},
\qquad
R\asymp r_j.
\]

Apply the last-crossing split.

- If post-crossing residence is long, Section 10 gives a uniform integrated L2 charge.
- If it is short, the entire positive local-enstrophy crossing occurs inside \(I_j^{an}\). The exact local-enstrophy identity forces cutoff diffusion, relative transport, or stretching; Sections 7--9 show that every one pays a uniform integrated L2 charge.

Therefore there exists

\[
c_{gen}>0
\]

depending only on the fixed corridor/cutoff/analytic constants such that

\[
\boxed{
\frac1{\nu R^2}
\int_{t_* - C R^2/\nu}^{t_*}
R\int_{B_{4R}(X_R(t))}|\nabla u|^2dxdt
\ge c_{gen}.
}
\]

Equivalently,

\[
\boxed{
\text{terminal matching-scale local enstrophy concentration}
\Longrightarrow
\text{uniform parabolic historical L2-gradient charge}.
}
\]

Status: **PROVED on the existing bounded-Z recurrent non-H/T corridor, conditional only on the terminal local concentration hypothesis itself.**

---

## 12. EMGG update

The local causal part of EMGG is now substantially closed:

\[
\boxed{
\text{matching-scale terminal local concentration}
\Longrightarrow
\text{historical L2-gradient/dissipation charge}
\lor H_{remote}\lor T.
}
\]

In particular, the former escapes

- critical L3 vorticity,
- relative boundary transport,
- critical W^{1,3} stretching,
- short-time crossing,

no longer remain naked branches on the terminal analytic window.

The unresolved step is now more geometric:

\[
\boxed{
\text{positive-density Eulerian remote-vorticity witness}
\stackrel{?}{\Longrightarrow}
\text{a matching-scale terminal local concentration label}
\lor H_{remote}\lor T.
}
\]

Call this narrower step the

\[
\boxed{\text{Remote Witness Localization Gate (RWLG)}.}
\]

RWLG is now the active EMGG frontier.

---

## 13. DSD audit

The following channels are kept separate:

- terminal local enstrophy concentration;
- analytic terminal-window pointwise deformation ceiling;
- cutoff-diffusion action;
- relative boundary transport action;
- stretching action;
- integrated L2 gradient charge;
- remote derivative non-tightness;
- turnover/multicore activity.

No arbitrary Eulerian remote witness is identified with a material packet without RWLG.

---

## 14. Audit verdict

### PROVED on the stated corridor

- a fixed terminal parabolic window lies inside the previous first-hitting stage;
- the repository's restart analyticity argument applies uniformly at every time in that window;
- bounded endpoint enstrophy propagates to a uniform terminal-window enstrophy ceiling;
- the velocity gradient has a uniform natural-scale pointwise ceiling on that window;
- critical L3 vorticity is automatically bounded on fixed matching scales;
- cutoff diffusion, relative transport, and stretching each force a time-integrated critical L2 gradient charge;
- long local-enstrophy persistence pays the same type of charge;
- terminal matching-scale local concentration therefore carries a uniform parabolic historical deformation/dissipation charge.

### NOT DERIVED

- RWLG: arbitrary positive-density Eulerian remote witnesses need not yet produce a matching-scale local concentration label;
- closure of H_remote;
- closure of T;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
