# Navier–Stokes verification

3차원 비압축성 Navier–Stokes 존재성·정칙성 문제를 DSD 네 층과 함께 구조적으로 분석하는 작업 저장소입니다.

## 기본 공간

기본 영역은 경계 없는 전체 3차원 공간

\[
\Omega=\mathbb R^3
\]

입니다. 유체를 수영장·상자·탱크·유한 구형 용기에 담긴 것으로 해석하지 않습니다.

원점 또는 임의의 분석 중심 `x_0`에서

\[
S_r(x_0)=\{x\in\mathbb R^3:|x-x_0|=r\}
\]

를 관측·집계용 구면으로 사용합니다. 이 구면은 물리적 벽이 아니며 `r`에 상한이 없습니다.

## 기본 PDE

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad
\nabla\cdot u=0,
\qquad
\nu>0,
\qquad
f\equiv0.
\]

DSD 적용은 이 방정식을 바꾸지 않습니다. 특히 표준 비압축성 트랙에 임의의 유한 전파속도나 추가 힘을 삽입하지 않습니다.

## DSD four-paper bridge

다음 네 층을 순서대로 사용합니다.

1. **Formation Axiom System** — 채널 존재·적용가능성·undefined/defined-zero·합성 충돌 구분.
2. **축 속성공리계** — 공간 실현축 랭크 3을 유지하고 좌표·방향·행렬 크기를 공간차원과 혼동하지 않음.
3. **Channel-Indexed Static Aggregation** — 고정시간의 속도·압력·와도·축별/구면별 항을 집계하되 조기 스칼라화로 인한 정보손실을 검사.
4. **Structural Reorganization Dynamics** — 고정시간 집계의 시간 lineage와 advection/pressure/viscous 재구성 채널을 연결.

첫 설계는 `notes/2026-08-12-dsd-four-paper-first-pass.md`에 기록되어 있습니다.

## 현재 확인된 구조

### 1. Analytic benchmark

재현성 기준장은 Schwartz 함수

\[
\psi(x)=e^{-|x|^2}
\]

에 대해

\[
u_0^{(a)}=\nabla\times\nabla\times(\psi e_a),
\qquad a\in\{x,y,z\}
\]

로 둡니다. 이는 매끄럽고 발산이 0이며 무한원점에서 급감합니다.

### 2. Shell-information separation

기준장에서는

- `r=sqrt(2)`에서 총 구면 에너지는 각방향으로 등방적이지만 축별 에너지는 서로 다름;
- `r=sqrt(5/2)`에서 shell enstrophy는 0이지만 velocity energy는 0이 아님;
- `u`와 `-u`는 여러 이차 집계량이 같아도 signed state는 다름;
- signed vortex-stretching 합은 0이어도 positive/negative stretching은 각각 nonzero임.

따라서 하나의 스칼라 합계만으로 상태를 동일시하지 않습니다.

### 3. Translation and nonlinear coupling

번역된 seed의 특수 구면은 그 seed의 새 중심에서 복원되며, 옛 원점 하나만 보는 분석은 translation complete하지 않습니다.

또한 두 divergence-free seed의 합도 divergence-free이지만

\[
Q(u)=\sum_{i,j}\partial_i u_j\partial_j u_i
\]

에는 nonzero cross term이 생깁니다. DSD 동역학에서는 이를 off-diagonal interaction channel로 보존합니다.

### 4. Critical regularity bridge

전역 critical channel로

\[
T_3(t)=\int_{\mathbb R^3}|u|^3dx
\]

를 추적합니다. Smooth decaying solution의 형식적 balance는

\[
\frac{dT_3}{dt}+3\nu D_3=3\Pi_3
\]

형태이며, 핵심 미해결 항은 pressure correlation `Pi3`입니다.

대칭 단일 seed에서는 `Pi3=0`이 symmetry로 소거되지만, 비대칭 superposition에서는 deterministic spectral audit에서 positive/negative `Pi3`가 모두 나타났습니다. 따라서 global `L3` monotone-decay shortcut은 **FAILED-ROUTE CANDIDATE**로 관리합니다.

관련 노트: `notes/2026-08-12-critical-l3-pressure-rate.md`.

### 5. Local/parabolic bridge

모든 중심의 shell data는 coarea로 ball integral을 복원합니다.

\[
\int_{B_R(x_0)}f\,dx
=
\int_0^R\int_{S_r(x_0)}f\,dS\,dr.
\]

따라서 천구형 관점을 물리적 경계 없이 local ball / parabolic-cylinder regularity quantities와 연결할 수 있습니다.

관련 노트: `notes/2026-08-12-local-parabolic-regularity-bridge.md`.

## Reproducibility

Windows PowerShell/CMD:

```powershell
python -m pip install -r requirements.txt
python src\dsd_bridge_baseline.py --output-dir results
python src\critical_channel_baseline.py --output-dir results
python src\translation_coupling_baseline.py --output-dir results
python src\critical_l3_rate_baseline.py --output-dir results
python src\coarea_local_bridge.py --output-dir results
python -m unittest discover -s tests -v
```

GitHub Actions에서도 같은 파이프라인을 실행합니다.

## 증명 상태 원칙

수치·상징 benchmark가 통과해도 global smoothness로 승격하지 않습니다. 현재 가장 중요한 열린 단계는 다음과 같습니다.

- arbitrary admissible initial data로의 일반화;
- translation-complete all-center control;
- pressure correlation `Pi3`의 non-circular critical estimate;
- positive vortex-stretching의 비상쇄 제어;
- local scale channels가 알려진 regularity gate를 모든 잠재적 blow-up point에서 강제한다는 증명;
- 최종 global a-priori bound.

세부 상태는 `PROOF_MAP.md`, 실행 범위는 `REPRODUCIBILITY.md`를 기준으로 합니다.
