# M17-319 — Persistent line-weight covariance: ancestral memory or transverse-strain payer

Date: 2026-09-08
Status: conditional reduction, not a global-regularity closure
Parent: M17-318

## 1. Purpose

M17-318 leaves a persistent covariance between a bounded coefficient `h` and the weighted vortex-line quantity `L_rho`.  This note asks what positive structural statement can be extracted without silently identifying a pre-existing line-weight contrast with newly generated strain.

The audit distinction is essential:

- a line-weight contrast may already be present at the ancestral time;
- only the *newly created* portion may be charged to the present strain budget.

Accordingly, the surviving branch is split into ancestral memory and a present transverse-strain payer.

## 2. Exact two-line ratio identity

For a tracked weighted line,

\[
\frac{d}{d\theta}\log L_\rho
=\kappa-\frac12+2\bar\sigma_\rho.
\]

For two simultaneously trackable line labels `lambda, mu`, define

\[
q(\theta):=\log\frac{L_{\rho,\lambda}(\theta)}{L_{\rho,\mu}(\theta)}.
\]

The common similarity contraction cancels exactly:

\[
\boxed{
q'(\theta)
=(\kappa_\lambda-\kappa_\mu)
+2(\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu}).
}
\]

Hence on `I=[theta_0,theta_1]`,

\[
\boxed{
q(\theta_1)-q(\theta_0)
=\int_I(\kappa_\lambda-\kappa_\mu)\,d\theta
+2\int_I(\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu})\,d\theta.
}
\]

This identity requires an actual common genealogy on `I`.  Failure of the labels to persist is an explicit genealogy/replacement exit.

## 3. Covariance forces terminal line-weight oscillation

Assume on the relevant population

\[
|\operatorname{Cov}_\delta(h,L_\rho)|\ge c_{\rm cov}>0,
\qquad
|h-\bar h_\delta|\le H_*.
\]

Then

\[
\begin{aligned}
c_{\rm cov}
&\le \mathbb E_\delta
\left(|h-\bar h_\delta|\,|L_\rho-\bar L_\rho|\right)\\
&\le H_*\,\mathbb E_\delta|L_\rho-\bar L_\rho|,
\end{aligned}
\]

so

\[
\boxed{
\operatorname*{ess\,osc}_\delta L_\rho
\ge \frac{c_{\rm cov}}{H_*}.
}
\]

If additionally

\[
0<L_\rho\le L^*,
\]

then two representatives can be selected, after absorbing the essential-supremum selection loss into a factor `1/2`, with

\[
|L_{\rho,\lambda}-L_{\rho,\mu}|
\ge \frac{c_{\rm cov}}{2H_*}.
\]

By the mean-value bound for `log` on `(0,L^*]`,

\[
|\log L_{\rho,\lambda}-\log L_{\rho,\mu}|
\ge
\frac{|L_{\rho,\lambda}-L_{\rho,\mu}|}{L^*}.
\]

Therefore at a terminal time `Theta`,

\[
\boxed{
|q(\Theta)|\ge c_L,
\qquad
c_L:=\frac{c_{\rm cov}}{2H_*L^*}>0.
}
\]

No lower bound on `L_rho` was used here; a lower bound is needed only when converting line-averaged strain into raw weighted strain energy.

## 4. Finite-window creation of the contrast

Let `I=[theta_0,Theta]`.  Suppose

\[
|q(\theta_0)|\le d_{\rm anc}<c_L
\]

and the curvature corridor obeys

\[
|\kappa_\lambda|,|\kappa_\mu|\le\delta.
\]

Then

\[
\left|
\int_I(\kappa_\lambda-\kappa_\mu)\,d\theta
\right|
\le 2\delta|I|.
\]

Using the ratio identity and the terminal contrast,

\[
2\left|
\int_I
(\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu})\,d\theta
\right|
\ge
c_L-d_{\rm anc}-2\delta|I|.
\]

Define

\[
s_*:=\frac12\bigl(c_L-d_{\rm anc}-2\delta|I|\bigr).
\]

Whenever `s_*>0`,

\[
\left|
\int_I
(\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu})\,d\theta
\right|\ge s_*.
\]

Cauchy-Schwarz gives

\[
\int_I
|\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu}|^2\,d\theta
\ge \frac{s_*^2}{|I|}.
\]

Since `|a-b|^2 <= 2(|a|^2+|b|^2)`,

\[
\boxed{
\int_I
\left(|\bar\sigma_{\rho,\lambda}|^2
+|\bar\sigma_{\rho,\mu}|^2\right)d\theta
\ge \frac{s_*^2}{2|I|}.
}
\]

In particular, one of the two lines pays at least `s_*^2/(4|I|)`.

## 5. From line-averaged strain to weighted strain

For a tracked line `gamma`,

\[
\bar\sigma_\rho
=
\frac{\int_\gamma\rho\sigma\,ds}{L_\rho},
\qquad
L_\rho=\int_\gamma\rho\,ds.
\]

Weighted Cauchy-Schwarz yields

\[
|\bar\sigma_\rho|^2
\le
\frac{\int_\gamma\rho\sigma^2\,ds}{L_\rho}.
\]

If the captured lines satisfy

\[
L_{\rho,\alpha}\ge L_*>0
\]

throughout `I`, then

\[
\int_I\sum_{\alpha\in\{\lambda,\mu\}}
\int_{\gamma_\alpha}\rho\sigma_\alpha^2\,ds\,d\theta
\ge
L_*\int_I
\sum_{\alpha\in\{\lambda,\mu\}}
|\bar\sigma_{\rho,\alpha}|^2d\theta.
\]

Consequently,

\[
\boxed{
\int_I\sum_\alpha
\int_{\gamma_\alpha}\rho\sigma_\alpha^2\,ds\,d\theta
\ge \frac{L_*s_*^2}{2|I|}.
}
\]

The weaker one-line conclusion is `L_*s_*^2/(4|I|)`.  The two-line bound above is retained because it follows directly from the summed inequality.

## 6. Transverse-strain conversion

Let `Sigma` be the symmetric strain tensor, `xi` the line direction, and

\[
\sigma=\xi\cdot\Sigma\xi,
\qquad
P_\perp=I-\xi\otimes\xi.
\]

Incompressibility gives `tr Sigma=0`.  Therefore the two-dimensional transverse block

\[
A=P_\perp\Sigma P_\perp
\]

has

\[
\operatorname{tr}A=-\sigma.
\]

For a two-dimensional symmetric block,

\[
|\operatorname{tr}A|^2\le2|A|_F^2,
\]

hence

\[
\boxed{
|P_\perp\Sigma P_\perp|_F^2\ge\frac12\sigma^2.
}
\]

Combining with the previous section,

\[
\boxed{
\int_I\sum_\alpha
\int_{\gamma_\alpha}
\rho|P_{\perp,\alpha}\Sigma P_{\perp,\alpha}|_F^2
\,ds\,d\theta
\ge
\frac{L_*s_*^2}{4|I|}.
}
\]

This is a normalized/local payer.  It is not yet a physical nonsummability theorem.

## 7. Corrected branch split

The terminal covariance cannot be charged to present strain until ancestral contrast is excluded.  The audited branch is therefore

\[
\boxed{
\begin{aligned}
H_{\rm persistent\ covariance}
\Longrightarrow{}&
H_{\rm ancestral\ line\text{-}weight\ memory}\\
&\lor H_{\rm transverse\ strain\ payer}\\
&\lor G_{\rm amplitude/line\ weight}\\
&\lor G_{\rm genealogy/replacement}\\
&\lor G_{\kappa\text{-}corridor/nodal}\\
&\lor G_{h\text{-}coefficient}.
\end{aligned}
}
\]

## 8. DSD audit

- **R21 / R33:** a fixed normalized payer is not a divergent physical dissipation budget.
- **R27 / R38:** the same-line genealogy is a required coverage statement; replacement is not silently ignored.
- **R34:** the lower line-weight hypothesis `L_* > 0` is an amplitude/weight bridge, not a geometric consequence.
- **R25 / R37:** nothing here upgrades one selected line/scale to all finer scales.
- **No ancestral-cost substitution:** already-existing `q(theta_0)` is not charged again to current strain.

## 9. Result

M17-319 closes only the *local logical ambiguity* in M17-318: persistent line-weight covariance either comes from an inherited contrast or, on a finite interval where sufficient contrast is newly created and the geometric/amplitude hypotheses persist, produces a quantitative transverse-strain payment.

The inherited branch remains open and is the target of M17-320.
