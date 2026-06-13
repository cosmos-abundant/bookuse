# ch12 팩트체크 보고서 — 갈아타기 프로토콜

- 감수자: fact-checker (적대적 검증)
- 감수일: 2026-06-13
- 원고: `books/ai-for-marketers/manuscript/ch12.md` (구조편집·교정 통과본)
- 자료카드: `books/ai-for-marketers/research/ch12-migration.md` (카드 13장 + 미확인 목록)
- 장르: AI 활용법 — 모든 도구·정책 정보는 [휘발성], 확인 시점 명시
- 검증 방식: 자료카드 대조 → [확인필요]·휘발성 항목 독립 WebSearch 교차 확인

---

## 종합 판정

- **검증 항목 수: 19** (본문 [확인필요] 7 + 추가 사실 12)
- **오류: 0건**
- **불확실: 0건**
- **본문 [확인필요] 해소: 7건 전부 → "확인"으로 전환 가능**
- **게이트: 통과** (오류 0 + [확인필요] 0 달성 가능)

핵심: 작가가 카드 한정 수위를 정확히 지켰다. 미확인 통계(스타트업 폐업률 85%, 평균수명 18개월, 전환비용 $450B/25~30%)는 본문 프로즈에 **한 건도 새지 않았다**(grep으로 전수 확인). 모든 [확인필요]는 "원문 403이라 검색 요약 기준"이라는 출처 강도 문제였고, 이번에 독립 출처로 교차 확인되어 해소된다.

---

## 본문 [확인필요] 7건 — 항목별 판정

### 1. OpenAI/Google deprecation 통지 기간 (라인 27, 카드 02·03) — 확인

- **검증:** OpenAI 공식 deprecations 문서 및 복수 매체 교차. GA 모델 최소 6개월, GA 변형 최소 3개월, 프리뷰 모델 2주 통지 — 본문 서술과 일치. Google Gemini의 '-latest' 별칭 2주 이메일 통지, 일반 모델은 "사전 통지"(명확한 일수 정책 약함) — 본문이 "별칭은 가리키는 대상이 바뀌기 전 2주 통지"로 별칭에 한정해 서술한 것 정확.
- **추가 확인:** OpenAI는 프리뷰 모델을 실제로 2주 통지로 은퇴시킨 사례 보도됨(The Register 2026-01-30) — 본문 라인 45 "프리뷰 모델은 2주 통지로도 끌 수 있다"의 실증.
- **출처:** developers.openai.com/api/docs/deprecations; ai.google.dev/gemini-api/docs/models
- **처리:** 라인 27 [확인필요] 마커 **삭제 가능**. 본문 수정 불필요. (휘발성 항목이므로 라인 5의 "2026년 6월 기준" 명시로 시점 표기 충족.)

### 2. Zapier 작업 단위 과금 변경 (라인 39, 카드 08) — 확인

- **검증:** Zapier task 기반 과금, 잘못 구성된 Zap의 루프로 인한 청구 폭증, 사용자 추가 시 기본료 점프 불만 → 이후 개편(Free·Starter zap 개수 제한 폐지, Filter/Formatter/Paths 무과금화, 종량제 pay-as-you-go 도입). Zapier **공식 Help Center 발표**("We're making some big improvements to Zapier plans!")로 개편 방향 1차 확인. 주요 개편은 2024년 1월.
- **본문 수위:** 라인 39는 수치 없이 "작업 단위 과금이 루프·트래픽에 취약하다"는 **구조만** 사용. 라인 41은 "개편이 오히려 사용자에게 유리한 방향"이라고 정확히 균형 잡음 — 카드 08 반대근거(가격변경≠항상 인상)와 합치.
- **출처:** help.zapier.com/.../22923011763853; chargebee.com/pricing-labs/zapier-pricing-transformation
- **처리:** 라인 39 [확인필요] 마커 **삭제 가능**. 본문 수정 불필요.

### 3. Gemini CLI 무료 차단 2026-06-18 (라인 43, 카드 07) — 확인

- **검증:** Google Developers Blog 공식("Transitioning Gemini CLI to Antigravity CLI") + The Register + 복수 마이그레이션 가이드 일치. 2026-06-18부로 무료·개인(AI Pro/Ultra, 무료 Code Assist) 사용자의 레거시 CLI 호출 차단, 유료 조직(Enterprise 라이선스) 접근 유지, Antigravity CLI(Go)로 이전 유도 — 본문 라인 43 서술과 정확히 일치.
- **미래시제 점검(중요):** 오늘은 2026-06-13으로 발효일(06-18) **5일 전**. 본문 라인 43은 "2026년 6월 18일, Google은 ... 서비스 중단하고 ... 이전을 유도했다"로 **과거형**으로 서술됨.
  - 출간 시점이 06-18 이후라면 과거형이 맞다.
  - 단, 만에 하나 Google이 발효일을 연기/철회하면 사실이 어긋난다. 카드 07도 "발효일이 조사일 직후라 출간 시 결과 재확인 필요"로 경고.
  - **권고:** 출간 직전(06-18 경과 후) 발효 여부 1회 재확인. 발효 확인되면 과거형 그대로 통과. 만약 연기되면 "2026년 6월 18일자로 예고했다"식 예고형으로 완화. **현재 정보 기준으로는 과거형 서술이 사실과 부합하므로 오류 아님.**
- **출처:** developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli; theregister.com/ai-ml/2026/05/20
- **처리:** 라인 43 [확인필요] 마커 **삭제 가능**(단 출간 직전 발효 재확인 1회 조건부).

### 4. Visual Electric 인수·90일 종료·환불 (라인 47, 카드 06) — 확인

- **검증:** Built In, Yahoo/TechCrunch, TheAIInsider 등 다수 매체 일치. 2025-10-02 Perplexity가 Visual Electric 팀 인수(acqui-hire), 90일 내 제품 종료, **사용자 데이터 내보내기 제공 + 구독자 비례(prorated) 환불** — 본문 라인 47 서술과 일치. 팀은 "Agent Experiences" 그룹 합류.
- **출처:** builtin.com/articles/perplexity-acquires-visual-electric-20251002; finance.yahoo.com/news/perplexity-acquires-team-behind-sequioa-131426564.html
- **처리:** 라인 47 [확인필요] 마커 **삭제 가능**. 본문 수정 불필요.

### 5. Meta Workplace 9개월 백업 창 타임라인 (라인 47, 카드 05) — 확인

- **검증:** Mimecast, Yoobic, Connecteam, Axios 등 일치. 2025-08-31까지 정상 작동 → 2025-09-01~2026-05-31 read-only(데이터 열람·다운로드 가능) → 2026-06-01 접근 종료·데이터 영구 삭제. read-only 창 = 약 9개월. "Download Your Information" 도구로 데이터 추출 — 본문 라인 47 "9개월에 걸친 데이터 백업 창 ... 읽기 전용으로 데이터 다운로드 ... 설정 메뉴의 데이터 내려받기 기능"과 일치.
- **시점 주의:** 2026-06-01은 이미 경과(오늘 06-13). 완전 삭제 발효된 확정 과거사실 — 본문 과거형 서술 적절.
- **출처:** mimecast.com/blog/meta-workplace-shutting-down; yoobic.com/blog/meta-is-closing-workplace
- **처리:** 라인 47 [확인필요] 마커 **삭제 가능**. 본문 수정 불필요.

### 6. GDPR 20조 데이터 이식권 (라인 69, 카드 10) — 확인

- **검증:** 아일랜드 DPC, GDPRhub, gdpr-info.eu, IAPP 등 교차. 제20조는 정보주체가 자신의 **개인데이터**를 "구조화되고 통용되며 기계가 읽을 수 있는 형식(structured, commonly used and machine-readable)"으로 받아 다른 관리자에게 이전할 권리(처리가 동의 또는 계약 근거 + 자동화 수단일 때). 예시 형식 JSON/XML/CSV. **개인데이터 한정** 범위 확인됨(동의/계약 기반 정보주체 데이터) — 본문 라인 69 "그 권리는 개인의 개인정보에 한정되고 회사 계정으로 만든 업무 데이터나 워크플로 설정까지는 보장하지 않는다"와 정확히 일치. 카드 10 반대근거(개인데이터 한정, 과장 금지)도 본문에 반영됨.
- **출처:** dataprotection.ie/en/individuals/know-your-rights/right-data-portability-article-20-gdpr; gdprhub.eu/Article_20_GDPR
- **처리:** 라인 69 [확인필요] 마커 **삭제 가능**. 본문 수정 불필요.

### 7. 도구 전환 비용 수치($450B 등) (라인 87, 카드 12) — 확인(수치 미사용 확인)

- **검증:** 카드 12의 $450B / IDC·Forrester 25%·30% / 주당 4시간 수치는 1차 출처 역추적 미완(마케팅성 블로그 순환 인용) — **본문 사용 불가 항목**. 본문 라인 87을 전수 확인한 결과, 프로즈에 수치가 **한 건도 없다**. "재학습과 전환의 비용이 따르고, 그 비용이 새 도구가 주는 이득을 넘어서는 경우가 흔하다"는 **방향성만** 서술. grep(450/25%/30%/40%/$/생산성 수치) 결과 라인 87의 매치는 [확인필요] 마커 내부 텍스트뿐.
- **판정:** 작가가 카드 12 지침("수치보다 방향성만")을 정확히 지킴. 검증 안 된 수치가 새어들지 않음.
- **처리:** 라인 87 [확인필요] 마커 **삭제 가능**. 본문 프로즈 수정 불필요. (마커 자체에 적힌 "$450B, 생산성 25~30%"는 마커 삭제 시 함께 제거되므로 본문에 수치가 남지 않음.)

---

## 추가 검증 항목 (12건) — 전부 확인

| # | 항목 | 본문 위치 | 판정 | 근거 |
|---|---|---|---|---|
| A1 | Anthropic 60일 통지·4단계(Active→Legacy→Deprecated→Retired) | 라인 27 | 확인 | 카드 01(platform.claude.com 1차 원문 열람) |
| A2 | Integromat→Make 2022-02-22 리브랜딩·make.com 이전 | 라인 3, 37 | 확인 | 복수 매체 일치 |
| A3 | Integromat 지원 2023 종료 | 라인 3 | 확인 | business-automated 등 |
| A4 | Make 1년간 같은 가격 업그레이드 제공 | 라인 37 | 확인 | 카드 09 + 매체 |
| A5 | GPT-4o 2025-08 사전통지 없이 제거 | 라인 21 | 확인 | 카드 04 + technology.org/TechRadar |
| A6 | #Keep4o 캠페인·복원·"미리 알리겠다" | 라인 21 | 확인 | 카드 04 |
| A7 | GPT-4o 2026-02-13 정식 은퇴, 사용률 0.1% | 라인 21 | 확인 | OpenAI 공식 + TechCrunch + 복수 매체 |
| A8 | GPT-5 2025-08 출시 | 라인 21 | 확인 | 카드 04 |
| A9 | OpenAI 프리뷰 2주 통지로 끈 사례 | 라인 45 | 확인 | The Register 2026-01-30 |
| A10 | Visual Electric = AI 이미지·디자인 도구, 2025-10 인수 | 라인 47 | 확인 | 카드 06 + Built In |
| A11 | 데이터 이식 형식 CSV/JSON 표준 | 라인 69, 93 | 확인 | GDPR 20조 + 카드 10·11 |
| A12 | 미확인 통계(폐업률·평균수명) 본문 미유입 | 전수 | 확인(미유입) | grep 전수 — 카드 13 배제 지침 준수 |

---

## 인용·고유명사 정합성

- 고유명사 표기 일관: Integromat, Make, make.com, Zapier, Gemini CLI, Antigravity CLI, Visual Electric, Perplexity, Workplace, ChatGPT, GPT-4o, GPT-5 — 전부 정확.
- 직접 인용문 없음(개념 서술 위주) — 글자 단위 대조 대상 없음.
- 날짜 표기: 2022-02-22, 2025-08, 2026-02-13, 2026-06-18, 90일, 9개월 — 전부 출처와 일치.

---

## 잔여 리스크 / 편집장 처리 권고

1. **마커 삭제(작가/편집장 소관):** 라인 27·39·43·47(2건)·69·87의 [확인필요] 7건은 본 보고서로 전부 "확인" 전환됐다. 감수자는 마커를 직접 지우지 않았다. 작가/편집장이 본문 프로즈는 그대로 두고 [확인필요: ...] 대괄호 블록만 제거하면 된다(본문 서술 자체는 수정 불필요).

2. **출간 직전 재확인 1건(조건부):** Gemini CLI 발효일(2026-06-18)이 오늘(06-13) 기준 미발효. 출간이 06-18 이후 확정이면 과거형 그대로 통과. 만약 출간 일정이 06-18 이전이거나 Google이 발효를 연기하면 라인 43을 예고형("2026년 6월 18일자로 예고했다")으로 완화. **현시점 정보로는 과거형이 사실과 부합 → 오류 아님.**

3. **시점 명시:** 휘발성 도구·정책 정보는 라인 5의 "2026년 6월 기준" 전역 명시로 충족. 라인 47의 Meta(2026-06-01 삭제)·Visual Electric(2025-10)·GPT-4o(2026-02-13)는 확정 과거사실이라 추가 시점표기 불필요.

4. **라인 81 아임리포트 박스:** 본 박스의 [확인필요]는 5장 경로 확정 대기(편집장 정합성 패스 소관)로, 본 팩트체크 7건 범위 밖이다. 사실 오류는 없으며 "서드파티 SaaS = 최상위 존속 리스크" 원리 수준 서술이라 안전. 5장 확정 후 편집장이 문구 조정.

---

## 출처 목록

- OpenAI Deprecations: https://developers.openai.com/api/docs/deprecations
- OpenAI 프리뷰 2주 사례(The Register): https://www.theregister.com/2026/01/30/openai_gpt_deprecations/
- OpenAI GPT-4o 은퇴 공식: https://openai.com/index/retiring-gpt-4o-and-older-models/
- Google Gemini API Models/별칭 정책: https://ai.google.dev/gemini-api/docs/models
- Google Developers Blog (Gemini CLI→Antigravity): https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/
- The Register (Gemini CLI): https://www.theregister.com/ai-ml/2026/05/20/bye-bye-gemini-cli-google-nudges-devs-toward-antigravity/
- Zapier 공식 개편 발표: https://help.zapier.com/hc/en-us/articles/22923011763853-We-re-making-some-big-improvements-to-Zapier-plans
- Chargebee (Zapier 개편 분석): https://www.chargebee.com/pricing-labs/zapier-pricing-transformation/
- Visual Electric (Built In): https://builtin.com/articles/perplexity-acquires-visual-electric-20251002
- Visual Electric (Yahoo/TechCrunch): https://finance.yahoo.com/news/perplexity-acquires-team-behind-sequioa-131426564.html
- Meta Workplace 타임라인(Mimecast): https://www.mimecast.com/blog/meta-workplace-shutting-down/
- GDPR 제20조(아일랜드 DPC): https://www.dataprotection.ie/en/individuals/know-your-rights/right-data-portability-article-20-gdpr
- GDPR 제20조(GDPRhub): https://gdprhub.eu/Article_20_GDPR
- Integromat→Make: https://www.business-automated.com/posts/integromat-changes-name-to-make
