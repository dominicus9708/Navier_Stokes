# Navier–Stokes verification

3차원 비압축성 Navier–Stokes 존재성·정칙성 문제를 구조적으로 분석하기 위한 작업 저장소입니다.

이 저장소의 기본 공간은 **경계가 없는 전체 3차원 공간**

\[
\Omega=\mathbb R^3
\]

입니다. 유체가 수영장·상자·용기 같은 유한한 물체 안에 담겨 있다고 보지 않습니다. 대신 원점 `O`를 관측 중심으로 고정하고, 임의의 반지름 `r>0`에 대한 구면

\[
S_r=\{x\in\mathbb R^3:|x|=r\}
\]

들을 이용해 전체 공간을 **무한한 천구형 관점**에서 분석합니다. 여기서 구면은 물리적 벽이 아니라 관측·집계용 껍질이며, `r`에는 상한이 없습니다.

따라서 이 설정은 유계 구 `B_R(0)`의 내부 문제도, 육면체 주기 상자도 아닙니다. 주력 트랙은 Clay의 `\mathbb R^3` 전역 문제와 직접 맞닿도록 둡니다.

## 기본 PDE

\[
\partial_t u+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad
\nabla\cdot u=0,
\qquad
\nu>0,
\qquad
f\equiv0.
\]

물리적 벽이 없으므로 no-slip 경계조건은 사용하지 않습니다. 대신 초기장과 필요한 공간 미분은 무한원점에서 충분히 빠르게 감소하도록 둡니다.

## 중심과 초기 운동

원점은 공간의 물리적 중심이나 용기의 중심이 아니라 **분석을 위한 기준점**입니다.

기하학적 기준 실험에서는 중심 주변에 지지되는 매끄러운 발산-없는 초기장을 사용합니다. 재현성 코드의 첫 해석 benchmark는 정확한 상징 계산을 위해 Schwartz 함수

\[
\psi(x)=e^{-|x|^2}
\]

를 사용하고,

\[
u_0^{(a)}=\nabla\times\nabla\times\bigl(\psi e_a\bigr),
\qquad a\in\{x,y,z\}
\]

로 둡니다. 이 역시 `C^∞`, 발산-없음, 무한원점 급감 조건을 만족합니다. 중심 benchmark는 발견·검증용이며 최종 증명 대상을 제한하지 않습니다.

## 관측량

1. Cartesian 성분: `u_x, u_y, u_z`.
2. 반경·접선 분해: `u_r=u·e_r`, `u_t=u-u_r e_r`.
3. 임의의 `r>0`에서 구면 평균 운동에너지

\[
E(r,t)=\frac{1}{4\pi r^2}\int_{|x|=r}\frac12|u(x,t)|^2\,dS.
\]

4. 와도 `ω=∇×u`와 구면 평균 enstrophy.
5. 압력 변동의 구면 평균 및 각방향 편차.
6. 모든 `r>0`에서 순 방사 플럭스

\[
\Phi(r,t)=\int_{|x|=r}u\cdot n\,dS=0
\]

인지 확인합니다.

## '3차원 물결'의 의미

이 프로젝트의 비압축성 트랙에서 말하는 물결은 음향파가 아니라 중심부 초기 운동에 따른 속도·압력·와도·에너지의 **구면 껍질별 방사형 재배열/응답**입니다.

구면 `S_r`는 실제 경계가 아니므로 운동은 어느 유한한 반지름에서도 반사되거나 멈춘다고 가정하지 않습니다. `r→∞`까지 같은 공간이 이어지는 것으로 취급합니다.

실제 유한 전파속도의 압력파를 조사할 경우 `compressible/` 별도 트랙으로 분리하며, 그것을 Clay 문제의 직접 증명 단계와 혼합하지 않습니다.

## DSD four-paper bridge

첫 DSD 적용 설계는

`notes/2026-08-12-dsd-four-paper-first-pass.md`

에 기록합니다. 네 층은 다음 순서로 적용합니다.

1. Formation Axiom System,
2. axis-property layer,
3. Channel-Indexed Static Aggregation,
4. Structural Reorganization Dynamics.

DSD 층은 우선 보조 표현·증명감사 층입니다. 원래 Navier–Stokes PDE를 변경하지 않으며, 새 응용 대응은 `BRIDGE DEFINITION` 또는 `CONJECTURE / TARGET`로 분리합니다.

## Critical regularity bridge

첫 shell 집계만으로는 정칙성 증명과 직접 연결되지 않으므로,

`notes/2026-08-12-critical-regularity-bridge.md`

에서 표준 임계 정칙성 조건과 연결했습니다. 현재 핵심 목표는

\[
T_3(t)=\int_{\mathbb R^3}|u|^3dx
\]

를 DSD 정적 채널로 두고, 동역학에서는 압력 상관항과 와류 신장 양·음 채널을 분리해 추적하는 것입니다.

속도구배

\[
G=\nabla u
\]

를 세 실현축의 `3 x 3` property/coupling block으로 읽고,

\[
S=\frac12(G+G^T),
\qquad
\sigma=\omega^TS\omega
\]

를 와류 신장 채널로 둡니다. 현재 benchmark에서 signed stretching의 전역 합은 0이지만 positive/negative stretching은 각각 nonzero이므로, 단일 합계로의 조기 집계는 금지합니다.

## Reproducibility

Windows PowerShell/CMD 기준:

```powershell
python -m pip install -r requirements.txt
python src\dsd_bridge_baseline.py --output-dir results
python src\critical_channel_baseline.py --output-dir results
python -m unittest discover -s tests -v
```

현재 기준선은 첫 bridge `12/12`, critical-channel bridge `10/10` 검사를 수행합니다. GitHub Actions에서도 같은 검사를 실행합니다.

자세한 범위와 명령은 `REPRODUCIBILITY.md`, 정리·추측·미해결 항목 분리는 `PROOF_MAP.md`를 따릅니다.

## 디렉터리

- `notes/`: 정의, 보조정리 후보, 실패 경로, 문헌 대조
- `src/`: Python 등 재현성 계산
- `tests/`: 회귀검사
- `results/`: 수치·상징 검증 결과
- `wolfram/`: 독립적인 상징 검증 및 교차검증

기본 공간 설정은 `notes/2026-08-12-unbounded-spherical-view-baseline.md`에 기록합니다.
