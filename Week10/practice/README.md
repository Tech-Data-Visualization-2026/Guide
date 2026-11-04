# 배달 시간 분포 그림 두 장의 구간·정규화 설정

배달 매장 운영 담당자에게 배달 시간의 분포와 날씨별 분포 모양을 전달하는 하나의 실습. 제공 CSV의 주문 90건으로 Seaborn 분포 그림 두 장(PNG)을 만들고, 구간 경계·그룹 정규화 기준을 코드로 지정하고 출력값으로 확인함.

## 제출 마감 및 push 권한 안내

**2026년 11월 4일(수) 16:40부터 push 권한이 차단된다(한국시간).** 모든 제출물은 16:40 전에 개인 저장소에 push한다. 권한 일괄 회수 작업은 **16:41에 실행**한다.

- 서술형 문제는 **다음 주 수업(2026년 11월 11일(수)) 시간에 전원이 함께** 응시한다. 마감 시점에 push된 이 실습의 코드가 문제와 채점의 기준이다.
- push 권한은 마감부터 다음 주 서술형 응시와 평가가 끝날 때까지 닫혀 있다.
- 권한이 닫혀 있는 동안 다음 주차 실습 코드는 로컬에 commit만 해 두고, 권한이 열리면 push한다.
- 서술형 시작 시각 전에 UCheck 출석 또는 지각 기록이 없으면 응시하더라도 0점이다.

문제를 처음 연 순간부터 5분 이내에 답안 제출을 완료해야 합니다. 제한시간이 지나면 문제 화면이 자동으로 사라지고 제출할 수 없습니다. 시간 내 제출하지 않으면 해당 서술형 문항은 0점 처리됩니다.

## 제공 입력과 실행 환경

- 제공 파일: `README.md`, `delivery.csv`(수업용 가상 자료, 90행 × 3열)
- 한 행 = 배달 주문 1건
- `distance_km`: 매장에서 배달지까지의 거리(km, 0.6~5.9), 수치형 · 이 실습의 그림에서는 미사용
- `minutes`: 주문 접수부터 도착까지의 배달 시간(분, 정수 11~58), 수치형
- `weather`: 배달 시점 날씨 `Clear`(맑음) 66건·`Rain`(비) 24건, 범주형 · CSV에 처음 나타난 순서 = Clear → Rain

```csv
distance_km,minutes,weather
1.0,58,Clear
3.1,27,Clear
2.0,26,Rain
0.6,13,Rain
1.6,23,Clear
```

위 5행 = 파일 앞부분(전체 90행은 `delivery.csv`). 0번 행 = 58분 걸린 지연 주문(배달 시간 최댓값).

- 사용 도구: Python 3, pandas, NumPy, Matplotlib, Seaborn
- 예시 구현 검증 환경: Python 3.12.3, seaborn 0.13.2, matplotlib 3.10.9, pandas 3.1.0, numpy 2.5.4
- seaborn 0.11.2(numpy 1.24.0·matplotlib 3.5.2 조합)에서는 `histplot` 실행 오류 확인 → seaborn 0.13 이상 사용
- 실행 위치: Python 파일과 `delivery.csv`가 있는 폴더

| 명령 | 읽는 대상과 목적 | 바뀌는 파일·확인 결과 |
|---|---|---|
| `python --version` | Python 실행기 확인 | 파일 변경 없음, 버전 출력 |
| `python -c "import seaborn, matplotlib, pandas; print(seaborn.__version__, matplotlib.__version__, pandas.__version__)"` | 설치된 라이브러리 확인 | 파일 변경 없음, seaborn 0.13 이상 확인 |
| `python main.py` | 현재 폴더의 `delivery.csv`를 읽어 그림 두 장 생성 | `output/dist.png`, `output/weather_kde.png` 생성 또는 덮어쓰기, 터미널에 확인 한 줄 출력 |

- AI로 코드 초안 작성 허용, 실제 출력과 기대값의 대조는 직접 수행
- GUI 창 없이 파일 저장(`savefig`, 이전 강의의 그림 저장)만으로 완료 가능

## 질문과 그림 규칙

담당자의 질문 두 개마다 지정한 Seaborn 함수와 인자로 그림을 그림. 각 인자는 수업에서 같은 질문 유형에 사용한 설정.

| 질문 | 변수와 유형 | 함수와 필수 인자 | 출력 파일 |
|---|---|---|---|
| 질문 1 배달 시간은 보통 몇 분이고 얼마나 퍼져 있는가 | `minutes` 1개, 수치형 | `histplot`, `bins`에 0분 시작·폭 5분 경계 배열 | `output/dist.png` |
| 질문 2 비 오는 날 배달 시간 분포의 모양이 다른가 | `weather` 범주형별 `minutes` | `kdeplot`, `hue='weather'`, `common_norm=False` | `output/weather_kde.png` |

## 처리 순서와 기대 출력

1. 스크립트 시작에서 `sns.set_theme(style='whitegrid', font_scale=1.2)` 적용, `output` 폴더 생성
2. `delivery.csv`를 DataFrame으로 읽고 90행 × 3열 확인
3. 구간 경계 `np.arange(0, 65, 5)`: 끝값 65 제외 → 0~60분 경계 13개, 폭 5분 구간 12개, 배달 시간 최댓값 58분 포함
   - `binwidth=5` 지정 시(Seaborn 0.13.2): 최솟값 11분~최댓값 58분을 9등분한 폭 5.22분 구간 → 경계 배열로 폭 고정
4. **질문 1 분포 그림** `output/dist.png`
   - `fig, ax = plt.subplots(figsize=(8, 5))` 후 `histplot(..., bins=경계 배열, ax=ax)`
   - 막대 높이 목록 = `ax.patches`의 `get_height()` → 막대 12개, 높이 합 90, 최댓값 23
   - `fig.savefig('output/dist.png', dpi=100)` → 800×500픽셀
5. **질문 2 날씨별 모양 그림** `output/weather_kde.png`
   - 4번과 같은 크기의 새 Axes에 `kdeplot(data=..., x='minutes', hue='weather', common_norm=False, ax=ax)`
   - 곡선마다 면적 = 높이 합 × 격자 간격(`ax.lines`의 `get_xdata()`·`get_ydata()`), `np.sort(np.round(..., 2))` → `[1. 1.]`
   - `fig.savefig('output/weather_kde.png', dpi=100)` → 800×500픽셀
6. 두 파일 저장 후 터미널에 다음 한 줄 출력

```text
OK: n=90 bars=12 sum=90 max=23 areas=[1. 1.]
```

| 확인값 | 기대값 | 의미 |
|---|---:|---|
| 주문 수 `n` | 90 | 결측·누락 없이 전체 행 사용 |
| 막대 수 `bars` | 12 | 0~60분, 폭 5분 구간 |
| 막대 높이 합 `sum` | 90 | 경계 밖으로 빠진 주문 0건 |
| 가장 높은 막대 `max` | 23 | 20~25분 구간 23건 |
| 곡선 면적 `areas` | [1. 1.] | `common_norm=False` → 날씨마다 면적 1 |

구간별 건수 = 0~5분부터 차례로 `0, 0, 6, 10, 23, 19, 17, 10, 3, 1, 0, 1`, 55~60분 막대 1건 = 0번 행의 58분 지연 주문.

| 그림 | 반드시 보이는 요소 |
|---|---|
| `dist.png` | 0~60분의 폭 5분 막대 12개, 20~25분 막대가 가장 높음, 축 이름 `minutes`·`Count` |
| `weather_kde.png` | Clear·Rain 두 곡선과 범례 제목 `weather`, Rain 곡선의 봉우리(약 30.8분)가 Clear(약 23.6분)보다 오른쪽 |

- 기본값 `common_norm=True` 대조: 면적 0.27(Rain) = 24 ÷ 90, 0.73(Clear) = 66 ÷ 90 → 곡선 높이 차이가 건수 차이를 반영하므로 질문 2에는 `False` 사용
- 해석 범위: 이 표 90건의 분포 모양 비교, 비가 배달 시간을 늘린 원인 판정 아님
- 관측 범위(11~58분) 밖으로 늘어난 KDE 곡선 꼬리: 관측이 아닌 추정값
- 확인 한 줄만으로 완료 판정 불가 → 두 PNG의 실제 내용과 재실행 결과 함께 확인

## 제출 파일과 평가기준

- 제출물: Python 소스 `main.py` 한 개, 생성한 `output/dist.png`·`output/weather_kde.png`
- Python 소스: 빈 줄·주석 포함 100줄 이내
- 개인 이해도: 다음 수업 시작 직후 교수자 감독 아래 Discord 비공개 서술형 문항 한 개로 별도 평가

| 평가기준 | 제출물의 직접 증거 |
|---|---|
| 제출한 Python 소스가 .py 파일 한 개이고 100줄 이내인가? | 소스 파일 개수와 빈 줄·주석을 포함한 전체 줄 수 |
| 두 질문의 그림을 지정 함수·인자로 그렸는가? | `main.py`의 `histplot(bins=np.arange(0, 65, 5))`·`kdeplot(hue='weather', common_norm=False)`, 재실행한 두 PNG의 위 표 요소 |
| 확인값과 그림 크기가 기대 출력과 일치하는가? | 터미널 출력 `OK: n=90 bars=12 sum=90 max=23 areas=[1. 1.]`, `dist.png`·`weather_kde.png` 800×500픽셀 |

## 저장소 배치

- 위치: 학생 저장소의 `Week10/`
- 필수 파일: 안내문 `README.md`, 제공 `delivery.csv`, 작성한 `main.py`, `output/dist.png`, `output/weather_kde.png`
- 제출 방식: 위 파일을 한 commit에 포함해 push
- 제출 완료 확인: GitHub 웹의 `Week10/output/`에서 PNG 두 장 열람, 최신 commit에 `main.py`·`delivery.csv` 포함 확인
- 검산값의 적용 범위: 제공 `delivery.csv`에 대한 값, 다른 입력에서는 확인 한 줄이 달라짐
