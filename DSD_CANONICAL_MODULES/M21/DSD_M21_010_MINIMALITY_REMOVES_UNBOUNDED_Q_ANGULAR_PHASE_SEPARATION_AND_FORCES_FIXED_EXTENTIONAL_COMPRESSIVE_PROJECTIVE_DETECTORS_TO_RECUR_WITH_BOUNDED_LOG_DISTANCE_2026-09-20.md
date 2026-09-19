# M21-010 — Minimality removes unbounded q-angular phase separation: fixed extensional and compressive-projective detectors recur syndetically and therefore co-occur within bounded log-radius distance

Date: 2026-09-20  
Canonical ID: **M21-010**  
Status: **PHASE-LOCALIZATION REDUCTION / ROBUST EXTENSIONAL AND COMPRESSIVE-PROJECTIVE POPULATIONS WITH STRICT MARGINS DEFINE NONEMPTY OPEN LOCAL DETECTOR SETS AFTER A FINITE q-ANGULAR PARTITION / MINIMALITY MAKES EACH FIXED DETECTOR SYNDETIC ON EVERY HARD-HULL ORBIT / TWO SYNDETIC RETURN SETS CANNOT REMAIN ARBITRARILY FAR APART, SO THE TWO POPULATIONS RECUR WITH A UNIFORM BOUNDED LOG-RADIUS SEPARATION / q-ANGULAR PHASE LOCALIZATION THEREFORE REDUCES TO A BOUNDED-CELL TRANSITION, LOW-VORTICITY OR PROJECTIVE-ALIGNMENT SEPARATOR, OR LOCAL DERIVATIVE COST / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M21-008

At the enstrophy-production depth \(z_\omega\), the strong anti-correlation branch contains two robust populations.

An extensional population:

\[
A_+
=
\{\Gamma\ge\gamma_+\},
\]

with positive enstrophy probability

\[
\pi(A_+)\ge p_+>0.
\]

A compressive-projective population:

\[
A_-
=
\{\Gamma\le-\gamma_-,
\quad
K\ge k_-\},
\]

with

\[
\pi(A_-)\ge p_->0.
\]

All thresholds are fixed on the selected compact hard component.

## 2. Convert enstrophy mass to ordinary local mass

At \(z_\omega\),

\[
d\pi
=
\frac{E}{W}d\mu,
\]

with

\[
E=|G|^2.
\]

On the compact corridor,

\[
E\le E_{\max}<\infty.
\]

Also the M5-587 witness has

\[
W(z_\omega)>0.
\]

On the selected quantitative branch, compactness gives a component-dependent positive lower bound

\[
W(z_\omega)\ge W_*>0.
\]

Therefore

\[
\mu(A_\pm)
\ge
\frac{W_*}{E_{\max}}p_\pm
>0.
\]

Thus both populations occupy positive ordinary q-angular measure, not merely positive weighted measure.

## 3. Finite q-angular detector partition

Partition one unit q-cell and the sphere into finitely many fixed normalized detector boxes

\[
\mathcal C_1,\ldots,\mathcal C_N.
\]

Because \(A_+\) has positive q-angular measure, at least one detector box satisfies

\[
\int_{\mathcal C_{i_+}}
1_{A_+}\,d\mu
>0.
\]

Likewise there exists a fixed box \(\mathcal C_{i_-}\) with

\[
\int_{\mathcal C_{i_-}}
1_{A_-}\,d\mu
>0.
\]

Choose strict thresholds slightly below these positive values.

## 4. Open detector events on the finite-depth hull

At fixed \(z=z_\omega\), define the local detector observable

\[
\Phi_+(T)
=
\int_{\mathcal C_{i_+}}
\chi_+(\Gamma,E)\,d\mu,
\]

where \(\chi_+\) is a smooth cutoff supported inside the strict extensional margin

\[
\Gamma>\gamma_+/2
\]

and positive on

\[
\Gamma\ge\gamma_+.
\]

Likewise define

\[
\Phi_-(T)
=
\int_{\mathcal C_{i_-}}
\chi_-(\Gamma,K,E)\,d\mu,
\]

supported inside

\[
\Gamma<-\gamma_-/2,
\qquad
K>k_-/2.
\]

Smooth compact-hull dependence makes \(\Phi_\pm\) continuous.

Hence for suitable fixed thresholds \(\eta_\pm>0\),

\[
\boxed{
U_+
=
\{\Phi_+>\eta_+\},
}
\]

and

\[
\boxed{
U_-
=
\{\Phi_->\eta_-\}
}
\]

are nonempty open subsets of the finite-depth hard hull.

## 5. Fixed-depth q-flow inherits minimality

The wedge scaling action translates q while fixing z.

Therefore the same minimal q-translation hull structure used in M19-417 acts on the finite-depth profile at fixed \(z=z_\omega\).

For every nonempty open set in a compact minimal flow, return times are syndetic.

Hence there exist finite constants

\[
L_+<\infty,
\qquad
L_-<\infty
\]

such that along every hard-hull orbit:

- every q-interval of length \(L_+\) contains a return to \(U_+\);
- every q-interval of length \(L_-\) contains a return to \(U_-\).

Thus both fixed detector types recur with bounded q-gaps.

## 6. Two syndetic populations have bounded mutual separation

Take any extensional detector return at q-position \(q_+\).

Because \(U_-\) returns syndetically, the interval

\[
[q_+,q_++L_-]
\]

contains a compressive-projective detector return.

Therefore there exists \(q_-\) such that

\[
\boxed{
0\le q_--q_+\le L_-.
}
\]

Similarly, starting from a compressive return gives a nearby extensional return within \(L_+\).

Thus one can select infinitely many paired events with

\[
\boxed{
|q_+-q_-|
\le
L_{\rm pair}
:=
\max(L_+,L_-).
}
\]

Unbounded q-separation is impossible.

## 7. Angular separation is automatically bounded

The two selected angular detector patches are fixed subsets of \(S^2\).

Their geodesic separation is at most

\[
\pi.
\]

Therefore every paired event is contained in a q-angular cylinder of uniformly bounded diameter

\[
\boxed{
D_{\rm pair}
\le
L_{\rm pair}+C_{S^2}.
}
\]

Thus the phase-localization branch cannot send the two populations to arbitrarily remote angular or log-radial positions.

## 8. Construct a bounded connecting cell

For each paired event choose a normalized connected cylinder

\[
\mathcal C_{\rm pair}
\]

containing both local detector boxes.

Its q-length is bounded by

\[
L_{\rm pair}+O(1),
\]

and its angular diameter is bounded by the sphere diameter.

Therefore the family of such connecting cells has a uniform Poincare constant

\[
\boxed{
C_{P,\rm pair}<\infty.
}
\]

Both robust populations occupy fixed positive submeasure inside this bounded cell.

## 9. Return to the M21-008 interface fork

Inside \(\mathcal C_{\rm pair}\), the extensional and compressive populations have opposite strict \(\Gamma\) margins.

Therefore exactly the M21-008 local alternatives apply.

If vorticity and projective support remain nondegenerate through the connecting cell, Poincare forces

\[
\boxed{
\int_{\mathcal C_{\rm pair}}
|\nabla_{q,S}\Gamma|^2
\ge
g_*>0.
}
\]

Otherwise the connection uses:

\[
\boxed{
P_{E\text{-bottleneck}}
}
\]

or

\[
\boxed{
P_{K\text{-separator}}.
}
\]

M21-009 then reduces the robust \(K\)-separator to gradient/analytic or microinterface/turnover branches.

## 10. Phase-localization branch is no longer independent

The M21-008 branch

\[
P_{\rm phase-localization}
\]

was the possibility that the two positive populations remain separated in q/angular position.

M21-010 shows that on the compact minimal hull they cannot remain separated by an unbounded normalized distance.

Therefore

\[
\boxed{
P_{\rm phase-localization}
\Longrightarrow
P_{\Gamma\text{-grad}}
\lor
P_{E\text{-bottleneck}}
\lor
P_{K\text{-separator}}
}
\]

after bounded-pair localization.

There is no separate infinite-separation escape.

## 11. Recurrent packet count

Because both detector return sets are syndetic, paired extensional/compressive events can be selected with positive lower density in q.

Specifically, after choosing disjoint windows of fixed width,

\[
\boxed{
N_{\rm pair}(Q)
\gtrsim
c_{\rm pair}Q
}
\]

up to q-length Q.

Equivalently across physical scale ratio \(R=e^Q\),

\[
\boxed{
N_{\rm pair}(R)
\gtrsim
c_{\rm pair}\log R.
}
\]

Thus the bounded-cell transition/bottleneck geometry itself recurs at critical logarithmic multiplicity.

## 12. Criticality firewall

Logarithmic multiplicity is still far below the power multiplicities needed to defeat the known palinstrophy/raw-H2 ancestry weights by unsigned accumulation alone.

Therefore

\[
\boxed{
\text{syndetic paired transition geometry}
\not\Rightarrow
\text{ancestry contradiction}.
}
\]

The gain is structural localization, not multiplicity power.

## 13. Updated anti-correlation frontier

Combining M21-008--010,

\[
\boxed{
C_{\Gamma K}^{-}
\Longrightarrow
P_{\rm pal/strain-grad}
\lor
P_{E\text{-bottleneck}}
\lor
P_{K\text{-microinterface}}
\lor
P_{\rm analytic-cancel}
\lor
P_{K\text{-turnover}}.
}
\]

The broad q-angular phase-localization escape has been removed.

## 14. Strategic consequence

The strong anti-correlation branch is now forced into local recurrent geometry of bounded normalized size.

This is important because all remaining escape mechanisms can be tested against:

- finite-thickness Poincare cost;
- nodal/low-amplitude bottleneck cost;
- projective-alignment dynamics;
- temporal occupancy;
- and first-generation derivative ancestry.

The problem is no longer whether the two populations can avoid each other spatially.

It is whether their bounded-separation transition geometry can be too thin or too temporally sparse to charge the finite derivative budgets.

## 15. Next target

M21-011 should quantify **time/depth occupancy** of the bounded-pair transition geometry.

A single syndetic q-snapshot remains ancestry-summable.

The next useful gain would be a lower bound on normalized z-width or physical-time residence of one of:

- \(\Gamma\)-gradient transition;
- low-vorticity bottleneck;
- K-alignment microinterface/turnover.

If bounded derivative ceilings force fixed z-thickness, the recurrent bounded-pair geometry may thicken from \(O(\log R)\) snapshots into a stronger spacetime occupancy ledger.

\[
\boxed{\text{M21-010 COMPLETE; MINIMALITY REMOVES UNBOUNDED q-ANGULAR PHASE SEPARATION AND FORCES THE TWO ROBUST POPULATIONS TO RECUR WITHIN A UNIFORM BOUNDED LOG-RADIUS DISTANCE.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
