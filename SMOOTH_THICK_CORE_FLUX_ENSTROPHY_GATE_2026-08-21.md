# Smooth Thick-Core Flux / Enstrophy Gate — 2026-08-21

Status: **SMOOTH FINITE-STAGE CLOSURE CRITERION / GLOBAL REGULARITY NOT PROVED.**

This note stays entirely on the pre-singular smooth first-hitting track. It combines the endpoint Taylor-thick vorticity cylinder, the exact material-vorticity-flux identity, the distortion-aware material-tube coarea lemma, and the exact dynamically normalized enstrophy ledger.

## 1. Endpoint Taylor cylinder

At a record first-hitting endpoint let

\[
\|\Omega\|_\infty=1,
\qquad
\Omega(0)=\xi,
\qquad |\xi|=1,
\]

and assume the normalized Hessian bound

\[
\|\nabla^2\Omega\|_\infty\le K_{2,+}.
\]

Because \(\nabla(\xi\cdot\Omega)(0)=0\), Taylor gives

\[
\xi\cdot\Omega(y)
\ge
1-\frac{K_{2,+}}2|y|^2.
\]

Set

\[
r_0=K_{2,+}^{-1/2}.
\]

On the cylinder

\[
|z|\le r_0/2,
\qquad
|y_\perp|\le r_0/2,
\]

we have \(|y|^2\le r_0^2/2\), hence

\[
\boxed{\xi\cdot\Omega\ge\frac34.}
\]

Every transverse disk in this cylinder therefore carries normalized signed vorticity flux

\[
\boxed{
\Phi_*
\ge
\frac34\pi\left(\frac{r_0}{2}\right)^2
=
\frac{3\pi}{16}r_0^2.
}
\]

Because \(\omega=M\Omega\) and physical area is \(M^{-1}\) times normalized area, this flux is invariant under first-hitting parabolic rescaling.

## 2. Exact normalized enstrophy ledger

Let

\[
Z=\|\Omega\|_2^2,
\qquad
Q=\|\nabla\Omega\|_2^2,
\qquad
\Sigma=S/M,
\]

and let

\[
b=\frac{d}{ds}\log M,
\qquad
\frac{ds}{dt}=M.
\]

The physical enstrophy identity

\[
\frac12\frac d{dt}\|\omega\|_2^2
+\nu\|\nabla\omega\|_2^2
=
\int S:(\omega\otimes\omega)
\]

becomes exactly

\[
\boxed{
\frac12 Z_s
+\frac14 bZ
+\nu Q
=
\int\Sigma:(\Omega\otimes\Omega).
}
\]

At every dynamically normalized time \(\|\Omega\|_\infty\le1\). Using

\[
\|\Sigma\|_2^2=\frac12Z,
\]

we obtain the universal stretching ceiling

\[
\left|\int\Sigma:(\Omega\otimes\Omega)\right|
\le
\|\Omega\|_\infty\|\Sigma\|_2\|\Omega\|_2
\le
\frac{Z}{\sqrt2}.
\]

Hence

\[
\boxed{
\frac12 Z_s
+\frac14 bZ
+\nu Q
\le
\frac{Z}{\sqrt2}.
}
\]

## 3. Endpoint lower enstrophy

At any record endpoint, the same Taylor estimate gives

\[
\xi\cdot\Omega(y)
\ge
\left(1-\frac{K_2}{2}|y|^2\right)_+.
\]

Therefore

\[
\boxed{
Z\ge Z_-
:=
\frac{64\sqrt2\pi}{105}K_{2,+}^{-3/2}.
}
\]

Suppose the candidate non-turnover branch is vorticity-tight throughout the stage:

\[
\int_{B_{R_Z}}|\Omega|^2
\ge
(1-\varepsilon_Z)Z.
\]

Since \(|\Omega|\le1\),

\[
\boxed{
Z\le Z_+
:=
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
}
\]

At record-growth times \(b>0\), the current vorticity maximum equals the running maximum, so the record lower bound applies there. Thus over one stage \(M_j\to qM_j\),

\[
\int bZ\,ds
\ge
Z_-\int b\,ds
=
Z_-\log q.
\]

Integrating the normalized enstrophy inequality over the stage \(I_j\), with length \(L_j\), gives

\[
\boxed{
\nu\int_{I_j}Q\,ds
\le
\frac{Z_+}{\sqrt2}L_j
-\frac{Z_-}{4}\log q
+\frac12(Z_+-Z_-).
}
\]

This is a finite-smooth-stage upper budget for normalized palinstrophy.

## 4. Robust material-flux change forces normalized palinstrophy

Use the already established distortion-aware material-tube coarea lemma. Suppose that on an axial fraction \(\beta\in(0,1]\) of the Taylor cylinder, a material family changes its signed vorticity flux by at least a fraction \(\eta\in(0,1]\) of \(\Phi_*\):

\[
|\Delta\Phi|\ge\eta\Phi_*.
\]

Suppose also that the material deformation factor on the tube obeys

\[
M_F\le K.
\]

The physical cylinder height is \(r_0M_j^{-1/2}\). The physical stage duration satisfies

\[
\Delta t_j\le\frac{L_j}{M_j}.
\]

The coarea lemma therefore gives

\[
\int_{I_j^{phys}}\int_{tube}|\nabla\omega|^2
\ge
\frac{9\pi}{2048}
\frac{\beta\eta^2r_0^5}{\nu^2K^2L_j}
M_j^{1/2}.
\]

Since

\[
\int |\nabla\omega|^2dt
=
\int M^{1/2}Q\,ds
\le
\sqrt{qM_j}\int Q\,ds,
\]

we obtain the purely normalized finite-stage lower bound

\[
\boxed{
\int_{I_j}Q\,ds
\ge
\frac{9\pi}{2048\sqrt q}
\frac{\beta\eta^2r_0^5}{\nu^2K^2L_j}.
}
\]

## 5. Direct S-level closure certificate

Define

\[
A:=\frac{Z_+}{\sqrt2},
\]

\[
B:=\frac12(Z_+-Z_-)-\frac{Z_-}{4}\log q,
\]

and

\[
D:=
\frac{9\pi}{2048\sqrt q}
\frac{\beta\eta^2r_0^5}{\nu K^2}.
\]

The palinstrophy lower and upper bounds can coexist only if

\[
\boxed{
\frac{D}{L_j}\le AL_j+B.
}
\]

Equivalently,

\[
AL_j^2+BL_j-D\ge0.
\]

Therefore robust material-flux change requires the explicit minimum normalized stage length

\[
\boxed{
L_j\ge L_{\Phi,min}
:=
\frac{-B+\sqrt{B^2+4AD}}{2A}.
}
\]

If the smooth moving-core variance gate gives an upper stage length \(L_j\le L_{var}\) and

\[
\boxed{L_{var}<L_{\Phi,min},}
\]

then this flux-change branch is **S-closed** on the actual smooth solution.

No ancient limit, recurrent compact class, or suitable-weak extension is used.

## 6. Interpretation

The thick signed first-hitting cylinder cannot change a fixed fraction of its scale-invariant material vorticity flux arbitrarily rapidly. Rapid flux reorganization demands palinstrophy, while the exact normalized enstrophy ledger bounds how much palinstrophy can be paid on a short tight stage under the first-hitting cap.

This converts the old qualitative branch

\[
\text{viscous flux change}\to H
\]

into a literal finite-stage closure test

\[
\boxed{L_{var}<L_{\Phi,min}\Rightarrow\text{no robust flux-change stage}.}
\]

Status: **ROBUST THICK-CORE MATERIAL-FLUX CHANGE NOW HAS AN EXPLICIT SMOOTH STAGE-LENGTH FLOOR. THE BRANCH CLOSES DIRECTLY WHEN THAT FLOOR EXCEEDS THE MOVING-VARIANCE STAGE CEILING.**