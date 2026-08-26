# Navier–Stokes verification

3차원 비압축성 Navier–Stokes 존재성·정칙성 문제를 표준 수학과 DSD(Dimensional-Structural Describability) 논리 감사를 함께 사용하여 분석하는 작업 저장소입니다.

## Problem setting

기본 문제는 경계 없는 전체 공간

\[
\Omega=\mathbb R^3
\]

에서의 비강제 incompressible Navier–Stokes입니다.

\[
\partial_tu+(u\cdot\nabla)u
=-\nabla p+\nu\Delta u,
\qquad
\nabla\cdot u=0,
\qquad
\nu>0,
\qquad
f=0.
\]

관측 구면·cutoff·Leray 좌표의 shell은 분석 도구이며 물리적 용기나 벽이 아닙니다.
DSD는 PDE를 수정하지 않고, 상태·경계·채널·극한·원인/표현을 구분하는 감사 틀로만 사용합니다.

---

## Current status — 2026-08-26

\[
\boxed{\text{GLOBAL REGULARITY OF 3D NAVIER--STOKES REMAINS UNPROVED.}}
\]

현재 증명 시도는 많은 내부 가지를 하나의 large weak-critical endpoint로 압축했습니다.

가장 짧은 현행 사슬은

\[
\boxed{
\begin{array}{c}
\text{candidate blow-up}\
\Downarrow\quad\text{(upstream branch completeness still requires final audit)}\\
\text{retained recurrent W1 corridor}\
\Downarrow\\
\mathscr R_3>0\ \Longleftrightarrow\ \text{positive critical }K\text{ boundary defect}\
\Downarrow\\
\text{large high-amplitude weak-critical tail}\
\Downarrow\\
\textbf{OPEN: critical tail tightness / equivalent pump absorption}\
\Downarrow\\
\text{proved high-tail absorption lemma}\
\Downarrow\\
H^1\text{ control and continuation.}
\end{array}
}
\]

정확한 proof ledger는 [`PROOF_MAP.md`](PROOF_MAP.md)를 기준으로 합니다.

---

## Exact critical boundary coordinate

일반 W1 endpoint에서는 pointwise weak-`L3` distribution coefficient를 자동으로 가정하지 않습니다.
Tauberian 가정 없이 사용할 최종 경계좌표는

\[
\mathcal E_\lambda(U)
=
\frac12\int (|U|^2-\lambda^2)_+dY,
\]

\[
\boxed{
K(U;\lambda)
=
\lambda\mathcal E_\lambda(U).
}
\]

W1 invariant endpoint에서는

\[
\boxed{
\lim_{\lambda\downarrow0}
\langle K(U;\lambda)\rangle_\mu
=
\frac{\mathscr R_3}{3}>0.
}
\]

물리 변수에서는

\[
K_L^{phys}(t)
=
\frac L2\int(|u|^2-L^2)_+dx
\]

와 정확히 연결됩니다.

---

## Completed regularity lemma

저장소에서는 다음 보조정리를 완료했습니다.

어떤 유한 `L>0`와 terminal interval `(t0,T*)`에서

\[
\sup_{t_0<t<T_*}
\|u(t)\mathbf1_{|u(t)|>L}\|_{L^{3,\infty}}
<\varepsilon_\nu
\]

이면 nonlinear high-amplitude part를 viscosity에 흡수할 수 있고

\[
\sup_{t_0<t<T_*}\|\nabla u(t)\|_2<\infty,
\]

따라서 `T*`를 넘어 continuation이 가능합니다.

Reference:

`DSD_W1_CRITICAL_HIGH_AMPLITUDE_TAIL_ABSORPTION_LEMMA_2026-08-26.md`

---

## Single live endpoint issue

남은 주된 implication은

\[
\boxed{
\text{finite-energy Navier--Stokes + retained W1/prelimit structure}
\stackrel{?}{\Longrightarrow}
\text{uniform critical high-amplitude tail tightness}.
}
\]

예를 들어 다음이면 충분합니다.

\[
\boxed{
\lim_{L\to\infty}
\sup_{t_0<t<T_*}
K_L^{phys}(t)=0.
}
\]

이 문제는 GitHub **Issue #2**
`Final endpoint: prove critical K-tail tightness or equivalent pump absorption`
에서 단일 open endpoint로 관리합니다.

---

## DSD audit rules retained

현재 계산에서 다음 구분을 유지합니다.

- interior formation vs boundary storage;
- similarity-coordinate current vs material transport;
- defined zero vs undefined/inapplicable;
- physical source vs coordinate/boundary term;
- actual reformation vs derivative capacity;
- fixed Leray scale vs fixed physical scale;
- pointwise distribution limit vs Abel/Cesaro residue;
- gauge-dependent pressure value vs gauge-invariant pressure gradient/difference/work.

이 구분으로 여러 false closure를 제거했습니다.

---

## Routes that must not be reopened without new hypotheses

다음 shortcut은 감사에서 폐기되었습니다.

- weak-`L3` upper bound가 cubic logarithmic concentration과 모순이라는 주장;
- similarity-radial flux를 material turnover로 해석;
- periodic omega-limit tail을 원래 physical parent의 fixed annulus에 자동 상속;
- `R3/6`을 새 physical power source로 해석;
- 큰 `H2` capacity를 실제 reformation action으로 동일시;
- Mellin/Abel residue를 자동으로 `lim lambda^3 N(lambda)`와 동일시;
- pointwise pressure sign을 gauge-independent quantity로 사용;
- normalized recurrent event가 무한히 반복되면 finite physical energy와 자동 모순이라는 주장.

전체 목록과 이유는 `PROOF_MAP.md` 및 final audit를 참조합니다.

---

## Repository navigation

현재 읽을 순서는 다음과 같습니다.

1. `README.md` — 저장소 범위와 현재 상태.
2. `PROOF_MAP.md` — 최신 live proof ledger.
3. `DSD_NAVIER_STOKES_FINAL_CLOSURE_AUDIT_2026-08-26.md` — 최종 구조 감사.
4. `DSD_W1_CRITICAL_HIGH_AMPLITUDE_TAIL_ABSORPTION_LEMMA_2026-08-26.md` — 완료된 continuation lemma.
5. `DSD_W1_INTERIOR_BOUNDARY_DECOUPLING_AND_UNIFORM_NO_DEFECT_TARGET_2026-08-26.md` — exact `K` boundary target.
6. `DSD_W1_WEAK_L3_DISTRIBUTION_DEFECT_EQUIVALENCE_2026-08-26.md` — Tauberian correction 포함 distribution audit.
7. GitHub Issue #2 — 마지막 open endpoint.

날짜별 다른 문서는 위 사슬을 만들기 위한 증명·감사·폐기 기록입니다.

---

## Reproducibility

Windows PowerShell/CMD:

```powershell
python -m pip install -r requirements.txt
python src\dsd_bridge_baseline.py --output-dir results
python src\moving_material_region_baseline.py --output-dir results
python src\moving_control_energy_budget.py --output-dir results
python src\material_pullback_bridge.py --output-dir results
python src\critical_channel_baseline.py --output-dir results
python src\translation_coupling_baseline.py --output-dir results
python src\critical_l3_rate_baseline.py --output-dir results
python src\coarea_local_bridge.py --output-dir results
python -m unittest discover -s tests -v
```

GitHub Actions에서도 같은 baseline 파이프라인을 실행합니다.

---

## Definition of done

전역 정칙성을 주장하려면 최소한 다음을 모두 끝내야 합니다.

1. Issue #2의 critical endpoint bridge를 표준 수학으로 증명;
2. 그 결과로 W1 endpoint를 실제 모순으로 폐쇄;
3. arbitrary finite-time blow-up 가정에서 W1까지의 branch completeness를 처음부터 재감사;
4. 외부 정리의 정확한 hypotheses, 상수, domain, gauge, limit order를 독립적으로 재검증;
5. 그 이후에만 global regularity claim 검토.

그 전까지 이 저장소의 상태는 **structurally reduced proof attempt, not a Millennium-problem solution**입니다.