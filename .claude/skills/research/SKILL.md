---
name: research
description: 챕터 자료조사. 리서처가 출처 있는 자료카드를 만든다. 사용법 - /research <slug> <chNN 또는 ch01-ch03 같은 범위 또는 all>
---

자료조사 단계를 오케스트레이션한다. 입력: $ARGUMENTS (책 slug + 챕터 지정).

## 절차

1. `books/<slug>/proposal.md`와 STATUS.md를 읽는다. 기획안이 없으면 중단하고 `/book-plan` 안내.
2. 대상 챕터마다 챕터 브리프가 없으면 먼저 만든다: 기획안의 해당 챕터 내용을 `press/templates/chapter-brief.md` 형식으로 구체화해 `books/<slug>/briefs/chNN.md`에 저장. (브리프 작성은 편집장의 일 — 유일하게 직접 쓰는 문서)
3. **챕터별로 `researcher` 에이전트를 병렬 호출한다** (서로 독립이므로 한 메시지에 여러 Agent 호출). 각 프롬프트에 포함: 브리프 경로, 카드 템플릿 `press/templates/research-card.md`, 저장 경로 `books/<slug>/research/chNN-<주제>.md`, 장르(AI활용법이면 [휘발성] 태그 강조).
4. 결과 취합 후 STATUS.md의 조사 칸 갱신.
5. **보고:** 챕터별 카드 수, 미확인으로 남은 주장(작가가 못 쓰는 내용), 그리고 리서처가 발견한 "챕터 방향을 바꿀 만한 사실"이 있으면 최우선으로 전달 — 필요시 기획안 수정을 제안.

문학 책이면: 고증이 필요한 요소(실존 지명·시대 등)가 기획안에 있는 경우만 수행하고, 없으면 "문학 — 자료조사 생략"으로 STATUS에 기록.
