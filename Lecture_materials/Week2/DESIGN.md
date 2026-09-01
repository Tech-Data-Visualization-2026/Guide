---
name: Kami Academic · Data Visualization Week 02
canvas: 1920x1080
colors:
  parchment: "#F5F4ED"
  ivory: "#FAF9F5"
  ink: "#1B365D"
  inkLight: "#B5C8DC"
  nearBlack: "#141413"
  darkWarm: "#3D3D3A"
  olive: "#504E49"
  stone: "#6B6A64"
  sand: "#E8E6DC"
typography:
  title: "Noto Serif KR, Source Han Serif K, NanumMyeongjo, Georgia, serif"
  body: "Pretendard, Noto Sans KR, Apple SD Gothic Neo, system-ui, sans-serif"
  mono: "JetBrains Mono, D2Coding, monospace"
  titleWeight: 500
  bodySize: 28px
  minimumSize: 18px
spacing:
  slidePadX: 96px
  slidePadY: 78px
  gap: 32px
---

# Direction

Kami의 따뜻한 종이 표면과 잉크 블루 단일 강조색을 2주차 기술 강의에 적용한다. 사용자가 유지하기로 한 원문의 `##` 섹션 24개를 정확히 24장에 대응시키며, 각 장의 위계는 제목·번호·구분선·여백으로 만든다.

## Typography

- 한국어 제목은 명조 계열 500, 본문은 산세리프 28–32px을 기본으로 한다.
- 코드·명령·배열 모양은 모노스페이스로 표시하고 숫자에는 tabular nums를 적용한다.
- 이탤릭과 700 이상의 제목 굵기를 사용하지 않는다.

## Layout

- 1920×1080 고정 캔버스를 화면에 맞게 축소한다.
- 첫 장과 마지막 장은 잉크 블루, 나머지는 파치먼트 배경을 쓴다.
- 코드가 있는 장은 코드와 해석을 2열로 배치한다.
- 표와 배열은 카드보다 선·셀·간격을 이용해 구조를 드러낸다.
- 원문이 참조한 두 그림은 비율을 유지하며 캡션과 함께 사용한다.

## Interaction

- 방향키·PageUp/PageDown·Space·Home·End로 이동한다.
- Esc는 24장 개요를 열고 닫는다.
- 진행률, 현재 장 번호, localStorage 복원을 제공한다.

## Boundaries

- 두 번째 채도 높은 강조색, 그라디언트, 글래스모피즘, 장식용 아이콘을 금지한다.
- 원문에 없는 수치·인용·성능 주장을 추가하지 않는다.
- `##` 섹션을 합치거나 누락하지 않는다.

## Attribution

Visual system adapted from Open Design `kami-deck`, inspired by `tw93/kami` (MIT). Course content is derived only from `../2주차_배포용.md` and its two referenced figures.
