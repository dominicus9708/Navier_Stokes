# Amplitude–Location Genealogy Bridge

Date: 2026-08-25

Status: **LOCAL MATERIAL-PACKET BRIDGE PROVED / REMOTE CENTER-SEPARATION GATE PROVED / REVERSE ANNULAR-TO-ANCESTOR IDENTIFICATION NOT DERIVED / GLOBAL REGULARITY NOT PROVED.**

## 1. Scope and audit correction

The repository already contains the exact scale identity

\[
R_{j,k}^{\mathrm{phys}}=r_{j-k}.
\]

This identifies only a physical radius. It does **not** identify the current age-\(k\) annulus with the material image of the earlier first-hitting maximum packet.

A first draft of this note used global \(L^\infty\) deformation exposure. That statement was correct but too strong for remote genealogy, because first-hitting amplification itself forces an arbitrarily large *global* integrated strain over many generations. The correct genealogy quantity is therefore a deformation/diffusion exposure localized to the transported ancestor packet and its deformation tube.

Throughout let

\[
n=j-k,
\qquad
W_n=\|\omega(t_n)\|_\infty,
\qquad
r_n=\left(\frac{\nu}{W_n}\right)^{1/2},
\]

and let \(x_n\) be a first-hitting maximum point at time \(t_n\).

The imported first-hitting analyticity corridor supplies fixed \(a_0,b_0>0\) such that

\[
\boxed{
|\omega(x,t_n)|\ge b_0W_n
\qquad(x\in B_{a_0r_n}(x_n)).
}
\]

Set

\[
A_n^0:=B_{a_0r_n}(x_n).
\]

---

## 2. Material ancestor packet

Let \(\Phi_{t_n,t}\) be the smooth Lagrangian flow and define

\[
A_n(t)=\Phi_{t_n,t}(A_n^0),
\qquad
z_n(t)=\Phi_{t_n,t}(x_n).
\]

Since \(\nabla\cdot u=0\),

\[
\boxed{
|A_n(t)|=|A_n^0|
=\frac{4\pi}{3}a_0^3r_n^3.
}
\]

**Status: PROVED.**

---

## 3. Local packet exposures

For \(I=[t_n,t]\), define the packet strain exposure

\[
\boxed{
\Sigma_n(I)
:=
\int_I
\sup_{x\in A_n(s)}|S(x,s)|\,ds,
}
\]

and the packet diffusion exposure

\[
\boxed{
\mathcal D_n(I)
:=
\frac{\nu}{W_n}
\int_I
\sup_{x\in A_n(s)}|\Delta\omega(x,s)|\,ds.
}
\]

To control the geometry of the whole packet, let \(H_n(s)\) denote any connected tube containing all line segments joining points of \(A_n(s)\), for example its convex hull, and define

\[
\boxed{
\Lambda_n(I)
:=
\int_I
\sup_{x\in H_n(s)}|\nabla u(x,s)|\,ds.
}
\]

Then \(\Sigma_n(I)\le\Lambda_n(I)\) whenever \(A_n(s)\subset H_n(s)\).

These quantities are Galilean invariant under constant Galilean transformations because they involve derivatives of \(u\) and relative material geometry.

---

## 4. Two-sided amplitude retention on the material packet

Along a trajectory starting in \(A_n^0\), write

\[
a(t)=|\omega(\Phi(a_*,t),t)|.
\]

From

\[
D_t\omega=S\omega+\nu\Delta\omega,
\]

we have

\[
-|S|a-\nu|\Delta\omega|
\le
\frac{d}{dt}a
\le
|S|a+\nu|\Delta\omega|.
\]

Suppose

\[
\Sigma_n(I)\le L,
\qquad
\mathcal D_n(I)\le D.
\]

Because initially

\[
b_0W_n\le a(t_n)\le W_n,
\]

integrating factors give the uniform packet bounds

\[
\boxed{
a(t)
\ge
\left(b_0e^{-L}-D\right)W_n}
\]

and

\[
\boxed{
a(t)
\le
e^L(1+D)W_n.}
\]

In particular, if

\[
D\le\frac{b_0}{2}e^{-L},
\]

then

\[
\boxed{
q_LW_n
\le
|\omega(x,t)|
\le
Q_LW_n
\qquad(x\in A_n(t)),
}
\]

where

\[
q_L:=\frac{b_0}{2}e^{-L},
\qquad
Q_L:=e^L\left(1+\frac{b_0}{2}e^{-L}\right).
\]

Thus a locally quiet ancestor packet retains not only a lower amplitude fraction but also an upper amplitude of the same ancestor order.

**Status: PROVED.**

---

## 5. Coherence radius under local tube deformation

For any two trajectories starting in \(A_n^0\), the line-segment mean-value estimate inside \(H_n(s)\) gives

\[
\frac{d}{dt}|\Phi(a,t)-\Phi(b,t)|
\le
\sup_{H_n(t)}|\nabla u|
|\Phi(a,t)-\Phi(b,t)|.
\]

The inverse-flow estimate gives the corresponding lower Lipschitz bound. Hence, if

\[
\Lambda_n(I)\le L,
\]

then the transported packet is bi-Lipschitz at distortion at most \(e^L\), and in particular

\[
\boxed{
B_{\theta_Lr_n}(z_n(t))
\subset A_n(t),
\qquad
\theta_L:=a_0e^{-L}.
}
\]

Combining Sections 4 and 5, under the quiet local packet/tube conditions

\[
\boxed{
q_LW_n
\le|\omega(x,t)|\le Q_LW_n
\quad
(x\in B_{\theta_Lr_n}(z_n(t))).
}
\]

**Status: PROVED CONDITIONAL on the explicit local tube exposure bound.**

---

## 6. Exact annular contact-to-\(J\) bridge

At descendant stage \(j\), let \(\mathcal A_{j,k}\) be the physical age-\(k\) annulus and

\[
J_{j,k}
=r_n\int_{\mathcal A_{j,k}}|\nabla u(x,t_j)|^2dx,
\]

using the exact ancestor-radius identity.

Define

\[
\boxed{
\chi_{j,k}
:=
\frac{|A_n(t_j)\cap\mathcal A_{j,k}|}{r_n^3}.
}
\]

If the packet lower amplitude satisfies \(|\omega|\ge qW_n\) on the contact set, then pointwise \(|\omega|^2\le2|\nabla u|^2\) gives

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

Therefore a small-\(J\) remote annulus can contain only a small fraction of a quietly retained ancestor packet.

**Status: PROVED.**

---

## 7. Deep radial contact forces an order-one shell cost

Write, up to the fixed cutoff constants,

\[
\mathcal A_{j,k}
=\{x:c_-r_n<|x-X_j|<c_+r_n\},
\qquad0<c_-<c_+.
\]

Under \(\Lambda_n\le L\), if

\[
(c_-+\theta_L)r_n
\le
|z_n(t_j)-X_j|
\le
(c_+-\theta_L)r_n,
\]

then

\[
B_{\theta_Lr_n}(z_n(t_j))
\subset\mathcal A_{j,k}.
\]

The contact fraction has a fixed positive lower bound and therefore

\[
\boxed{
J_{j,k}
\ge
c(a_0,b_0,L,c_\pm)\nu^2.
}
\]

Thus a diffuse shell with \(J_{j,k}/\nu^2\to0\) cannot be a deep annular image of a locally quiet ancestor maximum packet.

**Status: PROVED CONDITIONAL.**

---

## 8. Remote descendant maximum cannot stay inside a quiet ancestor packet

The first-hitting amplitudes obey

\[
W_j=q^kW_n.
\]

Equivalently, with

\[
K_k=q^{k/2},
\]

\[
\boxed{W_j=K_k^2W_n.}
\]

Let \(X_j\) be a current first-hitting maximum point, so

\[
|\omega(X_j,t_j)|=W_j.
\]

If \(X_j\in A_n(t_j)\), the quiet-packet upper bound from Section 4 would imply

\[
K_k^2W_n=W_j\le Q_LW_n.
\]

Hence, whenever

\[
\boxed{K_k^2>Q_L,}
\]

the current maximum point cannot belong to the quietly transported ancestor packet:

\[
\boxed{X_j\notin A_n(t_j).}
\]

Using the coherent inner ball from Section 5,

\[
\boxed{
|X_j-z_n(t_j)|
\ge
\theta_Lr_n
\qquad(K_k^2>Q_L).
}
\]

This is a Galilean-invariant remote center-separation statement. It does not say whether the old packet moved away or the active maximum switched to a different packet; it proves that the two cannot remain the same quiet material core for arbitrarily large age.

**Status: PROVED CONDITIONAL on local packet/tube quietness.**

---

## 9. First-hitting amplification forces global strain exposure

The previous section explains why a *local* genealogy exposure is needed rather than a global one.

Let

\[
M(t)=\|\omega(t)\|_\infty.
\]

For

\[
f=|\omega|^2,
\]

the vorticity equation gives

\[
(\partial_t+u\cdot\nabla)f
=
2\omega\cdot S\omega
+\nu\Delta f
-2\nu|\nabla\omega|^2.
\]

At a spatial maximum of \(f\), the diffusion contribution is nonpositive. Hence the upper Dini derivative obeys

\[
D^+M(t)
\le
\|S(t)\|_\infty M(t).
\]

Integrating from \(t_n\) to \(t_j\),

\[
\log\frac{W_j}{W_n}
\le
\int_{t_n}^{t_j}\|S(t)\|_\infty dt.
\]

Since \(W_j/W_n=q^k=K_k^2\),

\[
\boxed{
\int_{t_n}^{t_j}\|S(t)\|_\infty dt
\ge
k\log q
=2\log K_k.
}
\]

Thus the global deformation exposure necessarily diverges with remote age. If the old material packet remains locally quiet, this required amplification must be carried elsewhere in the flow, naturally producing a center-switch/new-active-region alternative.

**Status: PROVED.**

---

## 10. Correct forward genealogy decomposition

For a remote ancestor packet, one now has the following valid tree.

Either

\[
\boxed{
\Sigma_n(I)>L
\quad\text{or}\quad
\mathcal D_n(I)>\frac{b_0}{2}e^{-L}
\quad\text{or}\quad
\Lambda_n(I)>L,
}
\]

which is a local strain/diffusion/deformation escape,

or the ancestor packet remains a coherent \(O(r_n)\), amplitude-\(O(W_n)\) material packet.

In the quiet case:

- deep annular contact forces \(J_{j,k}\gtrsim\nu^2\);
- small \(J_{j,k}\) forces small material contact fraction;
- for sufficiently remote age, the current maximum lies outside the old coherent packet;
- meanwhile first-hitting amplification requires global strain exposure at least \(2\log K_k\), so the active growth occurs outside the quiet old core.

Therefore

\[
\boxed{
\text{remote ancestor packet}
\Longrightarrow
\begin{cases}
\text{local strain/diffusion/tube deformation},\\
\text{order-one annular }J\text{-contact},\\
\text{radial dephasing + center/packet switch}.
\end{cases}
}
\]

**Status: PROVED as a forward decomposition.**

---

## 11. Consequence for diffuse cubic tails

On a remote subsequence with

\[
J_{j,k}/\nu^2\to0,
\]

if the ancestor packet is locally quiet, then

\[
\chi_{j,k}\to0.
\]

For all sufficiently remote ages it is also distinct from the current maximum packet.

Hence a diffuse cubic tail cannot be interpreted simply as the same first-hitting maximum packet being quietly carried from generation \(j-k\) to generation \(j\) at its matching radius.

It requires at least one of:

1. active local deformation/diffusion of the old packet;
2. loss of annular contact;
3. a new active packet / center switch;
4. shell rebuilding not material-identical to the old maximum packet.

**Status: PROVED within the stated local quiet hypotheses.**

---

## 12. What remains open

The reverse implication

\[
J_{j,k}>0
\stackrel{?}{\Longrightarrow}
\text{the shell descends from the stage }j-k\text{ maximum packet}
\]

remains **NOT DERIVED**.

Likewise, center switching alone has not yet been shown to violate the finite energy ledger. Packets at geometrically separated natural scales may have geometrically summable ordinary energy/enstrophy costs.

The next calculation must therefore test whether repeated center switching can carry the **divergent cubic annular mass**, rather than merely whether several packets can coexist.

---

## 13. Audit table

| Statement | Status |
|---|---|
| Exact ancestor radius identity | PROVED previously |
| Material ancestor volume preservation | PROVED |
| Local packet strain/diffusion control gives two-sided amplitude retention | PROVED |
| Local tube deformation control gives coherent \(O(r_n)\) packet | PROVED CONDITIONAL |
| Material contact fraction forces \(J\)-cost | PROVED |
| Deep annular contact forces \(J\gtrsim\nu^2\) | PROVED CONDITIONAL |
| Remote current maximum cannot remain inside a quiet ancestor packet | PROVED CONDITIONAL |
| First-hitting age \(k\) amplification forces \(\int\|S\|_\infty\ge k\log q\) | PROVED |
| Global exposure can be assumed uniformly quiet for remote age | FALSE |
| Radius matching identifies the same material packet | FALSE |
| Current annular \(J\) automatically comes from the ancestor maximum packet | NOT DERIVED |
| Center switching alone contradicts finite energy | NOT DERIVED |
| Global regularity | UNPROVED |

---

## 14. Updated frontier

The amplitude/location bridge is now localized correctly:

\[
\boxed{
\text{ancestor packet}
\to
\text{local deformation/diffusion}
\lor
J\text{-contact}
\lor
\text{dephasing + center switch}.
}
\]

The next sharp question is

\[
\boxed{
\text{Can repeated center/packet switching support the bounded-}Z\text{ divergent cubic ledger }
\sum_kJ_k^{3/2}=\infty
\text{ while all physical dissipation ledgers remain finite?}
}
\]

That is now the principal genealogy bottleneck on the corrected bounded-\(Z\), recurrent, non-\(L^3\) branch.