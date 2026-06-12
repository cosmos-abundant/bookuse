---
name: book-plan
description: 새 책 기획. 주제를 받아 기획자가 기획안을 만들고, 냉정한 독자의 심사를 통과시킨 뒤 책 작업 공간을 개설한다. 사용법 - /book-plan <주제 아이디어 (장르 포함하면 좋음)>
---

새 책의 기획 단계를 오케스트레이션한다. 입력: $ARGUMENTS (주제 아이디어).

## 절차

1. **사전 확인.** 주제에서 장르(실용서/문학/AI활용법)가 불분명하면 사용자에게 1회 질문(AskUserQuestion). 책 slug(영문 소문자-하이픈)를 정한다.
2. **기획.** `book-planner` 에이전트 호출. 프롬프트에 포함: 주제, 장르, 템플릿 경로 `press/templates/proposal.md`, 저장 경로 `books/<slug>/proposal.md`, "죽여보기 먼저" 절차 수행 지시.
3. **심사.** `red-team-reader` 에이전트 호출: `books/<slug>/proposal.md`를 기획안 모드로 심사, 판정문을 `books/<slug>/reviews/proposal-redteam-r1.md`에 저장.
4. **루프.** 반려 시 판정문을 첨부해 `book-planner`에게 수정시키고 재심사. 최대 2회. 2회 후에도 반려면 쟁점을 정리해 사용자에게 판단 요청.
5. **개설.** 통과 시 작업 공간 생성:
   - `books/<slug>/` 하위에 `research/ manuscript/ art/ reviews/ marketing/` 디렉터리
   - `STATUS.md` 생성 — 형식:
     ```
     # STATUS: <책 제목> (<slug>)
     - 장르: / 스타일가이드: / 기획 통과일:
     | 챕터 | 조사 | 초고 | 퇴고 | 삽화 | 비고 |
     |---|---|---|---|---|---|
     | ch01 <제목> | - | - | - | - | |
     ```
     (각 칸: `-` 미착수 / `진행` / `완료(날짜)` / `반려N회`)
6. **보고.** 사용자에게: 컨셉 한 줄, 목차 요약, 심사에서 지적되어 보강된 점, 다음 단계 안내(`/produce-chapter <slug> ch01` 또는 `/research`).
