---
name: publish-prep
description: 출간 준비. 전체 통독 편집, 전체 감수, 원고 조립, 마케팅 킷 제작, 출간 체크리스트 검증. 전 챕터 퇴고 완료 후 실행. 사용법 - /publish-prep <slug>
---

출간 준비 단계를 오케스트레이션한다. 입력: $ARGUMENTS (책 slug).

## 절차

1. **게이트 확인.** STATUS.md에서 전 챕터가 퇴고 완료인지 확인. 미완료 챕터가 있으면 목록을 보여주고 중단.
2. **전체 통독 편집.** `dev-editor` 호출: 전 챕터를 통독해 챕터 간 중복·충돌·연결 끊김·용어 불일치를 점검, 보고서 `reviews/full-edit.md`. 발견 사항은 `writer`/`copy-editor`에게 회부해 해소.
3. **전체 감수.** `fact-checker` 호출: 전 원고 + 전 자료카드. 특히 [휘발성] 태그 항목 전수 재확인 (집필 후 시간이 지났다). 보고서 `reviews/full-factcheck.md`. 오류는 정정 루프 (최대 2회).
4. **front/back matter 작성.** `writer` 호출: 머리말(책의 약속, 읽는 법, 시점 일러두기), 참고 문헌(자료카드에서 생성), 찾아보기 후보 키워드.
5. **원고 조립.** 편집장이 직접: `books/<slug>/final/manuscript.md`로 머리말+목차+전 챕터+참고문헌 병합. pandoc이 설치돼 있으면 `final/manuscript.epub`과 `.docx`도 생성 시도 (실패해도 md는 유지).
6. **마케팅 킷.** `marketer` 호출: 기획안 + 완성 원고 경로 명시, `books/<slug>/marketing/`에 저장. 제목 최종 후보에 대해 `red-team-reader` 의견 1회 청취.
7. **출간 체크리스트.** `press/checklists/publish-checklist.md`를 항목별로 검증해 결과를 `books/<slug>/final/checklist-result.md`에 기록. 미충족 항목이 있으면 해소하거나 사용자 판단 요청.
8. STATUS.md에 출간 준비 완료 기록.

## 보고

- 체크리스트 통과 현황 (미충족 항목과 사유 포함)
- 최종 산출물 경로: 조립 원고, 마케팅 킷, 외부 작업 필요 목록(일러스트 생성, ISBN, 표지 디자인 등 사람이 할 일)
- 추천 제목 1순위와 마케터의 핵심 앵글
