---
name: illustrate
description: 챕터 삽화·도판 제작. 다이어그램(mermaid/SVG), 표, 이미지 생성 브리프를 만든다. 사용법 - /illustrate <slug> <chNN 또는 all>
---

삽화 단계를 오케스트레이션한다. 입력: $ARGUMENTS.

## 절차

1. **게이트 확인.** 대상 챕터가 퇴고 완료인지 STATUS.md로 확인. 미완료면 중단 (퇴고 중 원고가 바뀌면 도판이 어긋난다).
2. `illustrator` 에이전트 호출 (여러 챕터면 병렬). 프롬프트에 명시: 원고 경로, 자료카드 경로(차트 수치 검증용), 기존 `art/style.md`(있으면 — 스타일 통일), 저장 경로 규칙 `books/<slug>/art/chNN-figNN.*`.
3. 결과 검수 (편집장): 모든 도판에 삽입 위치·캡션·대체 텍스트가 있는지, 본문 수치와 일치하는지. illustrator가 수치 불일치를 보고하면 → 원고 오류인지 확인 후 `fact-checker` 또는 `writer`에게 회부.
4. 원고에 도판 참조를 삽입한다: 해당 위치에 `![캡션](../art/chNN-figNN.svg)` 또는 mermaid 블록 직접 삽입.
5. STATUS.md 삽화 칸 갱신.
6. **보고:** 도판 목록(종류·위치), 외부 이미지 생성이 필요한 브리프 목록(사용자가 직접 생성 AI에 넣을 것).
