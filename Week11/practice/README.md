# 펭귄 측정 표의 머신러닝 결과 그림 2장

펭귄 연구 담당자에게 측정값으로 무엇을 예측할 수 있는지 전달하는 하나의 실습. 제공 CSV의 펭귄 342마리로 회귀선·분류 결과 산점도 2장(PNG)을 만들고, 모델 출력이 그림의 선·색 중 무엇으로 표시되는지 확인값으로 대조함.

## 제출 마감 및 push 권한 안내

**2026년 11월 11일(수) 16:50부터 push 권한이 차단된다(한국시간).** 모든 제출물은 16:50 전에 개인 저장소에 push한다. 권한 일괄 회수 작업은 **16:50에 실행**한다.

- 서술형 문제는 **다음 주 수업(2026년 11월 18일(수)) 시간에 전원이 함께** 응시한다. 마감 시점에 push된 이 실습의 코드가 문제와 채점의 기준이다.
- push 권한은 마감부터 다음 주 서술형 응시와 평가가 끝날 때까지 닫혀 있다.
- 권한이 닫혀 있는 동안 다음 주차 실습 코드는 로컬에 commit만 해 두고, 권한이 열리면 push한다.
- 서술형 시작 시각 전에 UCheck 출석 또는 지각 기록이 없으면 응시하더라도 0점이다.

문제를 처음 연 순간부터 5분 이내에 답안 제출을 완료해야 합니다. 제한시간이 지나면 문제 화면이 자동으로 사라지고 제출할 수 없습니다. 시간 내 제출하지 않으면 해당 서술형 문항은 0점 처리됩니다.

## 제공 입력과 실행 환경

- 제공 파일: `README.md`, `penguins.csv`(Seaborn 예제 데이터 penguins에서 다섯 열을 고르고 측정값이 빈 2행을 뺀 342행 × 5열)
- 한 행 = 펭귄 한 마리 = 표본 하나
- `species`: 품종 `Adelie` 151마리·`Chinstrap` 68마리·`Gentoo` 123마리, 범주형 · 분류의 타깃
- `bill_length_mm`·`bill_depth_mm`: 부리 길이(32.1–59.6mm)·부리 깊이(13.1–21.5mm), 수치형
- `flipper_length_mm`: 날개 길이(172–231mm), 수치형
- `body_mass_g`: 몸무게(2700–6300g), 수치형 · 회귀의 타깃으로만 사용

```csv
species,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g
Adelie,39.1,18.7,181.0,3750.0
Adelie,39.5,17.4,186.0,3800.0
Adelie,40.3,18.0,195.0,3250.0
```

위 3행 = 파일 앞부분(전체 342행은 `penguins.csv`).

- 특징 행렬 `X`: 부리 길이·부리 깊이·날개 길이 3열(342, 3), 분류에 사용
- 사용 도구: Python 3, pandas, NumPy, Matplotlib, Seaborn, scikit-learn
- 예시 구현 검증 환경: Python 3.12.3, scikit-learn 1.9.1, seaborn 0.13.2, matplotlib 3.10.9, pandas 3.1.0, numpy 2.5.4
- 실행 위치: Python 파일과 `penguins.csv`가 있는 폴더

| 명령 | 읽는 대상과 목적 | 바뀌는 파일·확인 결과 |
|---|---|---|
| `python --version` | Python 실행기 확인 | 파일 변경 없음, 버전 출력 |
| `python -c "import sklearn, seaborn; print(sklearn.__version__, seaborn.__version__)"` | 설치된 라이브러리 확인 | 파일 변경 없음, seaborn 0.13 이상 확인(범례 동작), 두 버전을 검증 환경과 대조 |
| `python main.py` | 현재 폴더의 `penguins.csv`를 읽어 모델 2개 학습과 그림 2장 생성 | `output/` 안 PNG 2개 생성 또는 덮어쓰기, 터미널에 교차표 1개와 확인 한 줄 출력 |

- AI로 코드 초안 작성 허용, 실제 출력과 기대값의 대조는 직접 수행
- GUI 창 없이 파일 저장(`savefig`, 이전 강의의 그림 저장)만으로 완료 가능

## 질문과 그림 규칙

담당자의 질문 두 개마다 수업의 같은 과제 유형에서 쓴 모델·설정으로 그림을 그림. 두 모델 모두 객체 생성(하이퍼파라미터) → `fit` → `predict` 순서.

| 질문 | 과제 유형 | 모델과 필수 설정 | 그림 규칙 | 출력 파일 |
|---|---|---|---|---|
| 1 날개 길이로 몸무게를 예측할 수 있는가 | 회귀 | `LinearRegression()`, X = `peng[['flipper_length_mm']]`(342, 1), y = `body_mass_g` | 실제 342마리 산점도 + 170–235mm 격자 50개의 예측값을 이은 검은 회귀선 | `output/regression.png` |
| 2 측정값 3개로 품종을 맞히는가, 어디서 틀리는가 | 분류 | `KNeighborsClassifier(n_neighbors=1)`, `train_test_split(X, y, train_size=0.5, random_state=0)` | 평가용 171마리를 `bill_length_mm`×`bill_depth_mm`에 예측 품종 색(`hue='pred'`) + 오답 검은 빈 원 | `output/classification.png` |

- 그림 2의 품종 색 순서: `hue_order=['Adelie', 'Chinstrap', 'Gentoo']` → 다시 실행해도 같은 품종 = 같은 색

## 처리 순서와 기대 출력

1. 스크립트 시작에서 `sns.set_theme(style='whitegrid', font_scale=1.2)` 적용, `output` 폴더 생성
2. `penguins.csv`를 DataFrame으로 읽고 342행 확인, 특징 행렬 `X`(342, 3)와 타깃 배열 `y`(342,) 준비
3. **질문 1 회귀선** `output/regression.png`
   - X에 열 하나짜리 DataFrame(이중 대괄호) 사용, `fit` 뒤 `coef_` = 49.69(날개 1mm 증가 → 예측 몸무게 약 49.69g 증가)
   - 격자: `np.linspace(170, 235, 50)`를 학습 때와 같은 열 이름 `flipper_length_mm`의 DataFrame으로 만들어 `predict`
   - 검산: 170mm → 약 2666g, 235mm → 약 5895g(첫·마지막 격자값의 예측)
4. **질문 2 분류 결과 산점도** `output/classification.png`
   - 먼저 342마리 전체로 학습한 뒤 같은 342마리로 정확도 계산 → 1.0(같은 데이터 평가)
   - 학습용·평가용 절반 분할 뒤 다시 학습, 평가용 171마리의 정확도 → 0.959
   - 혼동 행렬 = 실제 × 예측 교차표(`pd.crosstab(y_test, y_pred, rownames=['true'], colnames=['pred'])`) 출력
5. 두 파일 저장 후 터미널에 교차표 1개와 다음 확인 한 줄 출력

```text
pred       Adelie  Chinstrap  Gentoo
true
Adelie         72          4       0
Chinstrap       3         31       0
Gentoo          0          0      61
OK: n=342 coef=49.69 same=1.0 test=0.959 wrong=7
```

| 확인값 | 기대값 | 의미 |
|---|---:|---|
| 마리 수 `n` | 342 | 제공 표 전체 사용 |
| 기울기 `coef` | 49.69 | 날개 1mm당 예측 몸무게 증가(g), 소수 둘째 자리 |
| 같은 데이터 정확도 `same` | 1.0 | 학습한 342마리로 평가 → 외운 답의 확인, 성능 근거 아님 |
| 평가용 정확도 `test` | 0.959 | 학습에 쓰지 않은 171마리 중 164마리 정답, 소수 셋째 자리 |
| 오답 수 `wrong` | 7 | 교차표 대각선 밖 4 + 3 = Adelie ↔ Chinstrap 사이 |

| 그림 | 반드시 보이는 요소 |
|---|---|
| `regression.png` | 점 342개와 왼쪽 아래에서 오른쪽 위로 오르는 검은 직선 하나, 축 이름 `flipper_length_mm`·`body_mass_g` |
| `classification.png` | Adelie·Chinstrap·Gentoo 세 색 점과 범례 제목 `pred`, 검은 빈 원 7개(부리 길이 41–45.5mm 구간, (41.4, 18.5)·(41.5, 18.5)의 두 원은 거의 겹침), 범례 항목 `wrong` |

- 해석 범위: 이 표 342마리와 분할 한 번(`random_state=0`)의 결과, 다른 분할에서는 평가용 정확도가 달라짐
- `classification.png`의 두 축은 모델 입력 3개 중 2개(날개 길이는 그림에 없음)
- 확인 한 줄만으로 완료 판정 불가 → 두 PNG의 실제 내용과 재실행 결과 함께 확인

## 제출 파일과 평가기준

- 제출물: Python 소스 `main.py` 한 개, 생성한 `output/regression.png`·`output/classification.png`
- Python 소스: 한 개, 아래 전체 합계 기준 적용
- 개인 이해도: 다음 수업 시작 직후 교수자 감독 아래 Discord 비공개 서술형 문항 한 개로 별도 평가

| 평가기준 | 제출물의 직접 증거 |
|---|---|
| 제출한 Python 소스가 .py 파일 한 개이고, 직접 작성한 소스·설정·문서의 합계가 100줄 이내인가? | 소스 파일 개수와 빈 줄·주석을 포함한 전체 줄 수 |
| 두 질문의 모델을 지정 설정으로 학습하고 출력을 그림 규칙대로 그렸는가? | `main.py`의 `LinearRegression`·`KNeighborsClassifier(n_neighbors=1)`·`train_test_split(..., train_size=0.5, random_state=0)`, 재실행한 두 PNG의 위 표 요소 |
| 교차표와 확인값이 기대 출력과 일치하는가? | 터미널 출력의 교차표 1개와 `OK: n=342 coef=49.69 same=1.0 test=0.959 wrong=7` |

## 저장소 배치

- 위치: 학생 저장소의 `Week11/`
- 필수 파일: 안내문 `README.md`, 제공 `penguins.csv`, 작성한 `main.py`, `output/` 안 PNG 2개
- 제출 방식: 위 파일을 한 commit에 포함해 push
- 제출 완료 확인: GitHub 웹의 `Week11/output/`에서 PNG 두 장 열람, 최신 commit에 `main.py`·`penguins.csv` 포함 확인
- 검산값의 적용 범위: 제공 `penguins.csv`에 대한 값, 다른 입력에서는 교차표와 확인 한 줄이 달라짐

## 전체 작성량 기준

- 직접 작성한 Python 소스·설정·문서·제출 주소 파일을 모두 합쳐 빈 줄·주석 포함 100줄 이내
- 제외 대상: 제공 README·제공 데이터·자동 생성 파일·외부 라이선스 원문·실행 결과 이미지
- 템플릿과 생성 결과는 중복 집계하지 않고 직접 작성한 틀 원본만 집계
- Python 소스는 한 개 유지, 줄 수를 줄이기 위한 읽기 어려운 압축은 불필요

## 예시 구현의 작성량

| 집계 파일 | 실제 줄 수 |
|---|---:|
| `main.py` | 54 |
| **합계** | **54** |
