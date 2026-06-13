# ch12 자료카드 — 갈아타기 프로토콜 (단종·가격급변·모델 deprecation·벤더 락인)

- 조사일: 2026-06-13 (researcher)
- 대상 브리프: `books/ai-for-marketers/briefs/ch12.md`
- 연결 카드: `research/ch05-spike.md` 카드 06(아임리포트) — 본 파일 말미 "ch05 스파이크 연결 평가" 참조
- 조사 제약 고지: gdpr-info.eu, dataprotection.ie, techcrunch.com, anthropic.com, ai.google.dev, aibuilderclub.com 등 다수 페이지가 자동화 접근 차단(HTTP 403)으로 직접 열람 불가. 해당 항목은 검색 결과 요약 + 복수 매체 교차 확인으로 보강했고, 원문 직접 확인이 안 된 부분은 카드에 명시했다. Anthropic 공식 deprecation 문서(platform.claude.com)는 원문 직접 열람 성공 — 모델 단종 표·정책 문구는 1차 원문이다.
- 휘발성 주의: 이 장은 휘발성 관리가 주제다. 모델·가격·도구 상태 정보는 전부 [휘발성] + 확인일 명시. 출간 직전 재확인 필수 항목은 각 카드 메모에 표시.

---

## A. 모델 deprecation 공식 정책 (브리프 조사대상 2)

## 카드 01: Anthropic은 공개 모델 단종 시 최소 60일 전 통지하며, 4단계 수명주기(Active→Legacy→Deprecated→Retired)를 운영한다

- **주장:** Anthropic은 공개 출시된 모델에 대해 은퇴(retirement) 최소 60일 전에 통지한다("providing at least 60 days notice before model retirement for publicly released models"). 모델 수명주기는 4단계다 — **Active**(완전 지원·권장), **Legacy**(업데이트 중단, 향후 deprecated 가능), **Deprecated**(작동은 하나 비권장, 대체 모델과 은퇴일 지정), **Retired**(사용 불가, 요청 시 실패). 영향받는 고객에게는 항상 이메일과 문서로 통지한다. 은퇴일 이후 해당 모델로의 요청은 실패한다.
- **출처:** Anthropic 공식 문서 "Model deprecations", platform.claude.com, https://platform.claude.com/docs/en/about-claude/model-deprecations (원문 직접 열람 성공)
- **출처 등급:** 1차 (벤더 공식 문서)
- **확인일:** 2026-06-13
- **휘발성:** [휘발성] — 정책(60일·4단계)은 비교적 안정적이나 변경 가능. 표의 개별 모델 상태는 빠르게 낡음.
- **반대 근거:** 일부 있음 — 60일은 "API의 공개 모델" 기준이다. 파트너 플랫폼(Amazon Bedrock, Vertex AI)은 자체 은퇴 일정을 두므로 모델 상태·날짜가 다를 수 있다(공식 문서 명시). 또 OpenAI 일반 모델의 6개월보다 짧다(카드 02). 즉 "벤더마다 통지 기간이 다르다"가 정확한 본문 수위.
- **인용 방식 제안:** 직접 인용(수치 60일 + 4단계 용어). 본문에서는 "AI 회사들은 구 모델을 끌 때 미리 알려준다 — 단 그 기간이 60일~6개월로 제각각"의 근거로.
- **메모:** 이 장의 핵심 논거 중 하나. "도구는 어느 날 갑자기 사라지지 않는다, 공지 기간이 있다 → 갈아타기는 패닉이 아니라 계획된 절차"라는 안심 메시지의 1차 근거. 단 모델 picker(소비자용 ChatGPT)는 통지 없이 바뀐 전례가 있다(카드 04) — API 정책과 소비자 제품은 다르다는 점을 본문에서 구분할 것.

---

## 카드 02: OpenAI는 일반 출시(GA) 모델은 최소 6개월, 특수 변형은 3개월, 프리뷰 모델은 2주 정도의 통지 후 단종한다

- **주장:** OpenAI는 모델 은퇴 전 통지 기간을 둔다 — 일반 공개(generally available) 모델은 최소 6개월, GA 모델의 특수 변형은 최소 3개월. 프리뷰(preview) 모델은 2주 같은 짧은 통지로 은퇴될 수 있다. 모델이 deprecated로 공지되면 즉시 deprecated 상태가 되고 shutdown 날짜가 부여되며, 사용 중인 고객에게 이메일로 통지하고 deprecations 페이지에 문서화한다. "legacy"로 태그된 모델·엔드포인트는 향후 deprecation 예고 신호다.
- **출처:** ① OpenAI 공식 "Deprecations" 문서, developers.openai.com, https://developers.openai.com/api/docs/deprecations (검색 결과 요약 기준 — 원문 403으로 직접 열람 실패) ② OpenAI Help Center "Retiring GPT-4o and other ChatGPT models", https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models
- **출처 등급:** 1차(공식 문서) — 단 원문 직접 미열람, 검색 요약 기준. **본문 수록 전 공식 페이지 원문 대조 권장.**
- **확인일:** 2026-06-13
- **휘발성:** [휘발성]
- **반대 근거:** 있음 — 소비자용 ChatGPT는 이 통지 기간과 별개로 움직였다. GPT-5 출시 시 GPT-4o를 model picker에서 사전 통지 없이 제거(카드 04). 즉 "API의 6개월 정책"과 "소비자 앱의 실제 운영"은 달랐다.
- **인용 방식 제안:** 수치만 + 시점 명시. 본문에서 Anthropic 60일과 나란히 놓아 "벤더별 통지 기간 비교"로.
- **메모:** 통지 기간이 GA 6개월 / 변형 3개월 / 프리뷰 2주로 나뉜다는 점이 본문 논거로 좋다 → "프리뷰·베타 딱지가 붙은 기능에 핵심 시스템을 걸지 마라"(새 도구 평가 5문항 중 안정성 항목)의 근거.

---

## 카드 03: Google Gemini는 단종 시 사전 통지하며, '-latest' 별칭은 2주 전 이메일 통지 후 가리키는 버전을 바꾼다

- **주장:** Google은 Gemini 모델 deprecation을 Release notes에 공지하고, 가장 빠른 shutdown 예정일을 deprecations 페이지에서 추적한다. deprecations 페이지의 날짜는 "은퇴될 수 있는 가장 이른 날짜(earliest possible dates)"이며, 정확한 shutdown 날짜는 매끄러운 전환을 위해 사전 통지한다. 특히 '-latest' 모델 별칭은 가리키는 버전이 바뀌기 전 이메일로 2주 통지를 제공한다. 실제 사례: Gemini 2.0 Flash·Flash-Lite는 2026-06-01 은퇴 예정, 대체는 gemini-2.5-flash-lite 등.
- **출처:** ① Google "Gemini deprecations" 공식 문서, ai.google.dev, https://ai.google.dev/gemini-api/docs/deprecations (403으로 원문 직접 열람 실패 — 검색 결과 요약 기준) ② Google "Release notes / changelog", https://ai.google.dev/gemini-api/docs/changelog (동일)
- **출처 등급:** 1차(공식 문서) — 단 403으로 원문 직접 미열람. **본문 수록 전 원문 대조 필수.**
- **확인일:** 2026-06-13
- **휘발성:** [휘발성]
- **반대 근거:** 있음 — Google의 deprecations 날짜는 "가장 이른 날짜"라는 모호성이 있어 정확한 통지 기간을 단정하기 어렵다. '-latest' 별칭의 2주는 매우 짧다 → "편의용 별칭(latest)에 시스템을 거는 것의 위험"의 근거가 되지만, "Google은 2주만 준다"로 일반화하면 틀린다(별칭에 한정).
- **인용 방식 제안:** 수치만(별칭 2주) + 시점 명시. 일반 모델 통지 기간은 OpenAI/Anthropic처럼 명확한 숫자가 없으므로 "사전 통지" 수준으로만.
- **메모:** 3사(OpenAI/Anthropic/Google) 비교표 작성 가능 — 단 Google은 명확한 일수 정책이 약해 표에 "사전 통지(별칭은 2주)"로 기재. 표 자체가 "벤더마다 다르니 내 도구의 정책을 직접 확인하라"는 새 도구 평가 항목의 실증.

---

## 카드 04: 실제 사례 — OpenAI는 GPT-5 출시 시 GPT-4o를 사전 통지 없이 제거했다가 사용자 반발로 되살렸고, 이후 정식 은퇴시켰다 [모델이 사라지는 실명 사례]

- **주장:** 2025년 8월 OpenAI는 GPT-5 출시와 함께 ChatGPT의 model picker에서 GPT-4o를 사전 통지 없이 제거했다. 즉각적이고 큰 사용자 반발(#Keep4o 캠페인)이 일자 OpenAI는 GPT-4o를 복원하고 "앞으로 유사 변경 시 미리 알리겠다"고 밝혔다. 이후 사용률이 0.1%로 떨어지자 GPT-4o를 정식 은퇴시켰다(2026-02-13 발효). 사용자들은 GPT-4o의 "안정적 페르소나"·"예측 가능한 출력"이 후속 모델에 없다며 아쉬워했다.
- **출처:** ① "OpenAI Brings Back GPT-4o Following GPT-5 User Backlash", technology.org, 2025-08-11, https://www.technology.org/2025/08/11/openai-restores-gpt-4o-after-encountering-user-dissatisfaction-with-gpt-5/ ② TechRadar "#keep4o campaign", https://www.techradar.com/ai-platforms-assistants/chatgpt/im-grieving-openai-has-switched-off-chatgpt-4o-and-angry-users-are-backing-a-keep4o-campaign-to-restore-it ③ TechCrunch "OpenAI removes access to ... ChatGPT-4o model", 2026-02-13, https://techcrunch.com/2026/02/13/openai-removes-access-to-controversial-chatgpt-4o-model ④ OpenAI Help Center(카드 02-②)
- **출처 등급:** 2차(전문 매체 다수 교차) + 1차(OpenAI Help Center가 은퇴 사실 확인)
- **확인일:** 2026-06-13
- **휘발성:** [휘발성] — 사건은 확정 과거사실(휘발 안 됨)이나, "현재 어떤 모델이 살아있나"는 휘발.
- **반대 근거:** 해당 없음(사건 자체) — 다만 본문 함의는 양면적이다. "모델은 사라진다"의 증거이면서 동시에 "사용자가 항의하면 되돌리기도 한다 + 회사가 정책을 개선하기도 한다"의 증거. 한쪽으로만 쓰지 말 것.
- **인용 방식 제안:** 직접 인용(사례·날짜). "낡는 순서" 중 **기능/모델 변경** 단계의 대표 실명 사례.
- **메모:** 마케터에게 직접 와닿는 사례 — 보고서 명세를 특정 모델(GPT-4o)의 말투에 맞춰 튜닝해 뒀다면, 모델 교체 시 출력 톤이 바뀐다. 3장 명세·4장 검증이 이식 자산인 이유를 보여주는 회수 지점. "특정 모델 버전에 명세를 과적합시키지 마라"는 교훈으로 연결.

---

## B. 단종·가격급변·인수 변질 실명 사례 (브리프 조사대상 1 — "낡는 순서"의 실증)

## 카드 05: 실제 사례 — Meta는 Workplace(기업용 협업 도구)를 종료, 9개월 read-only 데이터 백업 창을 주고 2026-06-01 완전 삭제했다 [서비스 종료 + 데이터 이식 모범 사례]

- **주장:** Meta는 2024-05-14/15 기업용 협업 플랫폼 Workplace의 종료를 발표했다. 2025-08-31까지 정상 작동, 2025-09-01~2026-05-31 read-only(데이터 열람·다운로드만 가능), 2026-06-01 접근 종료 및 데이터 영구 삭제. 사용자는 설정의 "Download your data" 버튼으로 프로필·게시물·채팅을 2026-05-31까지 내려받을 수 있었다(관리자가 기능을 켠 경우). 즉 약 9개월의 데이터 이전 창을 제공했다.
- **출처:** ① Axios "Meta Workplace shuts down", 2024-05-14, https://www.axios.com/2024/05/14/meta-workplace-shuts-down ② Mimecast "Meta Workplace Shutting Down", https://www.mimecast.com/blog/meta-workplace-shutting-down/ ③ Connecteam / Yoobic Q&A 정리(교차 확인)
- **출처 등급:** 2차(Axios 등 매체) — Meta 공식 발표 원문(forwork.meta.com)은 미열람. 발표 사실·타임라인은 다수 매체 일치.
- **확인일:** 2026-06-13
- **휘발성:** 태그 없음(확정 과거 사실) — 단 "마케터가 쓰던 도구냐"는 약함(협업 도구). 사례로는 데이터 이전 창의 모범으로 사용.
- **반대 근거:** 해당 없음 — 오히려 "큰 회사도 도구를 접는다"의 증거. 단 마케터 직무 밀착도는 낮으니 보조 사례로.
- **인용 방식 제안:** 직접 인용(타임라인·데이터 다운로드 창). "도구가 죽을 때 잘 죽으면 9개월의 백업 창을 준다 → 그래서 평소 데이터 이식성을 확인해 둬야 그 창을 쓸 수 있다"의 근거.
- **메모:** "낡는 순서"의 마지막 단계(도구 자체의 존속)의 대형 실명 사례. 핵심 교훈: 종료 자체보다 **데이터를 빼낼 수 있느냐**가 충격의 크기를 결정한다(카드 11·12의 데이터 이식성 논거와 직결).

---

## 카드 06: 실제 사례 — AI 디자인 도구 Visual Electric은 Perplexity에 인수된 뒤 90일 후 제품을 종료했다(데이터 내보내기·환불 제공) [인수 후 제품 폐기]

- **주장:** 2025-10-02 Perplexity가 Sequoia 투자를 받은 AI 디자인 스타트업 Visual Electric(이미지 생성·무한 캔버스 편집 도구, 디자이너 대상)의 팀을 인수했다. 인수 후 제품은 90일 내 종료되며, 사용자는 데이터를 내보낼 수 있고 구독자는 비례 환불을 받는다고 공지됐다. 팀은 Perplexity에서 "Agent Experiences" 그룹을 이끈다(이른바 acqui-hire — 제품이 아니라 인력 인수).
- **출처:** ① TechCrunch "Perplexity acquires the team behind ... Visual Electric", 2025-10-02, https://techcrunch.com/2025/10/02/perplexity-acquires-the-team-behind-sequioa-backed-ai-design-startup-visual-electric/ (403으로 원문 직접 열람 실패 — 제목·요지는 검색 결과 기준) ② Built In, https://builtin.com/articles/perplexity-acquires-visual-electric-20251002 ③ IndexBox 정리(90일·데이터 내보내기·환불)
- **출처 등급:** 2차(TechCrunch 등 다수 매체 일치) — TechCrunch 원문 직접 미열람.
- **확인일:** 2026-06-13
- **휘발성:** 태그 없음(확정 과거 사실).
- **반대 근거:** 해당 없음 — "인수=서비스 개선"이 아니라 "인수=제품 폐기"일 수 있다는 직접 증거. 단 90일 내보내기 창·환불을 준 점은 "잘 죽은" 사례.
- **인용 방식 제안:** 직접 인용(도구명·90일·데이터 내보내기). "낡는 순서" 중 **인수 후 변질/폐기**의 대표 사례. 마케터가 쓰는 AI 이미지·디자인 도구라는 점에서 직무 밀착도 높음.
- **메모:** acqui-hire 패턴(잘나가는 도구도 팀째 인수되며 제품은 닫힌다)을 보여주는 최신 AI 사례. "새 도구 평가 5문항"의 '죽어도 대체재가 있는가' + '데이터를 빼낼 수 있는가' 항목 실증.

---

## 카드 07: 실제 사례 — Google은 오픈소스 Gemini CLI를 2026-06-18 종료하고 클로즈드소스 Antigravity CLI로 대체한다(무료·개인 사용자 우선 차단) [기능 폐지 + 전략 변경]

- **주장:** Google은 2026-06-18부로 Gemini CLI(및 Gemini Code Assist IDE 확장)를 무료·개인(Google AI Pro/Ultra·무료 개인 Code Assist) 사용자에게 서비스 중단하고, Go로 작성된 Antigravity CLI로 이전을 유도한다. 유료 조직(Standard/Enterprise 라이선스, 유료 API 키) 사용자는 접근이 유지된다. 매체들은 이를 "오픈소스를 클로즈드소스 AI로 교체"로 평했다.
- **출처:** ① The Register "Bye-bye, Gemini CLI; Google's gone and swapped you for a closed-source AI", 2026-05-20, https://www.theregister.com/ai-ml/2026/05/20/bye-bye-gemini-cli-google-nudges-devs-toward-antigravity/ ② Phemex / AI Builder Club / DigitalApplied 마이그레이션 정리(403으로 원문 일부 미열람 — 날짜·대상은 복수 매체 일치)
- **출처 등급:** 2차(The Register 등) — Google 공식 공지 원문 미열람. **본문 수록 전 공식 공지 대조 권장.**
- **확인일:** 2026-06-13
- **휘발성:** [휘발성] — 발효일(2026-06-18)이 조사일 직후라 출간 시점엔 "이미 일어난 일". 재확인으로 결과 반영 필요.
- **반대 근거:** 일부 있음 — Google은 대체재(Antigravity CLI)와 이전 경로를 제시했다. 즉 "기능이 사라진다"보다 "더 폐쇄적인 새 도구로 강제 이전"이 정확. 무료 사용자만 차단되고 유료는 유지 → "무료 플랜은 가장 먼저 낡는다"의 근거.
- **인용 방식 제안:** 직접 인용(도구명·날짜·무료 차단). 단 개발자 도구라 페르소나 밀착도는 낮음 → "무료 티어가 먼저 끊긴다" 논거의 보조 사례로.
- **메모:** "낡는 순서"의 **가격/플랜 단계** 실증 — 같은 종료라도 유료는 살고 무료가 먼저 끊긴다. 새 도구 평가 '가격이 내 사용량에서 지속 가능한가'에 "무료 플랜 의존 리스크" 추가 논거.

---

## 카드 08: 실제 사례 — Zapier는 task 기반 과금에서 빌링 충격·요금 점프 불만을 겪고 2024~2025 가격 구조를 개편했다 [가격 정책 급변/오버리지 쇼크]

- **주장:** Zapier는 task 기반 과금에서 사용자 불만이 누적됐다 — 월 2,000~5,000 task 구간에서 비용이 급증($130~$600+), 잘못 구성된 Zap이 밤새 루프 돌아 $400~$1,200 청구, Professional(1인 한정)→Team($69/월 기준) 단일 사용자 추가 시 기본료 3.5배 점프 등. Trustpilot 평점은 빌링 불만이 지배해 1.4/5 수준으로 보고된다. 이후 Zapier는 Free·Starter의 zap 개수 제한 폐지, Filter·Formatter 등 유틸리티 스텝 무료화, 초과 task 종량제(pay-as-you-go) 도입으로 가격 구조를 개편했다.
- **출처:** ① TrustRadius "Zapier Pricing 2026", https://www.trustradius.com/products/zapier/pricing ② eesel AI "Zapier subscription plans explained", https://www.eesel.ai/blog/zapier-subscription ③ Chargebee Pricing Labs "Zapier's Pricing Overhaul", https://www.chargebee.com/pricing-labs/zapier-pricing-transformation/
- **출처 등급:** 2차(전문 매체) — 개별 수치는 매체 추정·집계. **공식 가격 페이지(zapier.com/pricing) 원문 대조 필요**(ch05 카드 09와 동일 이슈, 403).
- **확인일:** 2026-06-13
- **휘발성:** [휘발성] — 가격은 가장 빨리 낡는 정보. 절대액보다 "과금 단위가 task당이라 루프·트래픽에 취약"이라는 구조(원리) 중심으로.
- **반대 근거:** 있음(중요) — Zapier의 개편은 사용자에게 **유리한 방향**(제한 폐지·유틸 무료화)이었다. 즉 "가격은 항상 나빠진다"는 틀린다. 가격 변경 = 인상도 인하도 구조 변경도 가능 → "내 사용량 기준으로 다시 계산하라"가 정확한 교훈.
- **인용 방식 제안:** 배경 지식으로만 + 과금 단위 원리는 직접 설명. 절대 수치는 ch05 카드 09와 함께 공식 페이지 대조 후.
- **메모:** "낡는 순서"의 **가격/플랜 단계** 핵심 사례. ch05가 추천하는 도구(Zapier/Make/n8n)가 바로 가격 변동 당사자라는 점에서 자기참조적 — 12장이 "이 책이 쓴 도구도 가격이 바뀐다"를 정직하게 인정하는 장치로 활용. 과금 단위 3종(task/operation/execution) 차이는 ch05 카드 09 참조.

---

## 카드 09: 실제 사례 — 노코드 자동화 도구 Integromat은 2022년 Make로 리브랜딩되며 인터페이스·가격 구조를 전면 개편하고 구 브랜드 지원을 종료했다 [도구 변질/리브랜딩]

- **주장:** 2022-02-22 Integromat은 Make로 리브랜딩되어 make.com 도메인으로 이전했다. 인터페이스와 가격 구조가 전면 개편됐고, 기존 고객은 1년간 같은 가격으로 Make로 업그레이드할 수 있었으나 Integromat 지원은 2023년 종료됐다. 사용자들은 새 가격 티어가 기존 설정 비용을 올릴 수 있다는 우려를 제기했다.
- **출처:** ① Make 공식 "Integromat evolves to Make", https://www.make.com/en/integromat-evolves-to-make (403으로 직접 열람 실패 — 발표 사실은 검색 결과 기준) ② Business Automated "Integromat changes name to Make", https://www.business-automated.com/posts/integromat-changes-name-to-make ③ Tripetto Help "Update Integromat automations to Make"
- **출처 등급:** 1차(Make 공식 발표 — 미열람) + 2차 교차
- **확인일:** 2026-06-13
- **휘발성:** 태그 없음(확정 과거 사실) — 단 "현재 가격"은 휘발(ch05 카드 09).
- **반대 근거:** 있음 — 이전 창(1년)·가격 동결을 제공해 비교적 매끄러운 전환이었다. "리브랜딩=재앙"은 아님. 단 UI 전면 개편으로 기존 화면 캡처·클릭 경로는 전부 무효화 → "UI는 가장 먼저 낡는다"의 직접 사례.
- **인용 방식 제안:** 직접 인용(리브랜딩·UI 개편). "낡는 순서" **UI 단계**의 대표 사례 — 도구가 살아있어도 버튼 위치·이름이 통째로 바뀐다.
- **메모:** ch05가 추천하는 Make 자신의 이력이라는 점이 강력하다. "이 책의 Make 화면 설명도 언젠가 이렇게 무효화된다 → 그래서 책은 클릭 경로가 아니라 원리를 가르친다"는 12장 메시지의 자기참조 사례. 도판 UI 의존 최소화 원칙(기획안 도판 규모)의 근거이기도.

---

## C. 벤더 락인 / 데이터 이식성 (브리프 조사대상 3)

## 카드 10: 데이터 이식성(GDPR 제20조)은 벤더 락인 방지를 목적으로, 개인이 자기 데이터를 "구조화·통용·기계판독 가능한 형식"으로 받아 다른 곳으로 옮길 권리를 보장한다

- **주장:** EU GDPR 제20조 "데이터 이식권(Right to data portability)"은 정보주체가 자신이 제공한 개인데이터를 "구조화되고, 통용되며, 기계가 읽을 수 있는 형식(structured, commonly used and machine-readable format)"으로 받아, 방해 없이 다른 관리자에게 전송할 권리를 보장한다(처리가 동의 또는 계약에 근거하고 자동화 수단으로 수행될 때). IAPP 등은 이 조항의 주된 목적 중 하나가 **벤더 락인 방지(to prevent vendor lock-in)**임을 명시한다. 통용 형식의 예: JSON, XML, CSV(PDF 스캔·독점 형식·라벨 없는 텍스트 덤프는 부적합).
- **출처:** ① GDPR 제20조 원문, gdpr-info.eu, https://gdpr-info.eu/art-20-gdpr/ (403 — 조문 텍스트는 복수 출처로 교차 확인) ② IAPP "Data portability in the EU: An obscure data subject right", https://iapp.org/news/a/data-portability-in-the-eu-an-obscure-data-subject-right (벤더 락인 방지 목적 명시) ③ 아일랜드 DPC "The right to data portability (Article 20)", https://www.dataprotection.ie/en/individuals/know-your-rights/right-data-portability-article-20-gdpr (403 — 미열람)
- **출처 등급:** 1차(법령 원문 — 직접 열람은 403, 다만 조문은 공개 법령으로 복수 출처 일치) + 2차(IAPP 권위 매체)
- **확인일:** 2026-06-13
- **휘발성:** 태그 없음(법령·확립된 개념).
- **반대 근거:** 일부 있음 — 제20조는 "정보주체(개인)의 개인데이터"에 한정된다. 회사 계정의 업무 데이터(보고서·워크플로 설정)는 이 권리의 범위 밖일 수 있다. 즉 "법이 내 워크플로 데이터를 보장한다"로 과장 금지. 본문 수위: "법적 권리는 개인데이터에 한정 → 업무 데이터는 계약·약관·내보내기 기능으로 직접 확인해야 한다."
- **인용 방식 제안:** 배경 지식으로만 + "구조화·통용·기계판독 형식"은 직접 인용 가능. 본문에서는 "데이터를 CSV/JSON 같은 표준 형식으로 빼낼 수 있는가"를 새 도구 평가 항목의 근거로.
- **메모:** 새 도구 평가 5문항 중 "데이터를 빼낼 수 있는가(락인 회피)"의 1차 권위 근거. 마케터에게는 "법적 권리"보다 "실무 체크(내보내기 버튼이 있는가, 어떤 형식인가)"로 번역해 전달.

---

## 카드 11: 벤더 락인은 데이터가 한 플랫폼에서만 접근 가능할 때 발생하며, 표준·기계판독 형식 내보내기 보장이 핵심 완화책이다

- **주장:** 데이터 이식성이 없으면 데이터는 저장된 플랫폼에서만 접근 가능해, 사일로화·벤더 락인·데이터 품질 저하로 이어진다. 데이터 이식성은 서비스에 불만인 사용자가 데이터 이력을 처음부터 재구성하지 않고도 경쟁 서비스로 옮길 수 있게 한다. 실무 권고: 락인을 피하려면 표준·기계판독 형식(JSON/XML/CSV)으로의 내보내기가 보장되는지, 직접 전송(controller-to-controller)이 기술적으로 가능한지 확인한다.
- **출처:** ① TechTarget "What is data portability?", https://www.techtarget.com/searchcloudcomputing/definition/data-portability (403 — 검색 요약 기준) ② IAPP(카드 10-②) ③ GDPR 제20조(2)·(3) 직접 전송 조항
- **출처 등급:** 2차(전문 매체) + 1차(법령 조항)
- **확인일:** 2026-06-13
- **휘발성:** 태그 없음(개념).
- **반대 근거:** 있음 — 데이터를 빼낼 수 있어도 **재구축 비용**(새 도구에 명세·연결을 다시 짜는 노동)은 남는다. "내보내기만 되면 락인이 없다"는 과장. 락인에는 데이터 락인 + 워크플로/학습곡선 락인 + 통합생태계 락인이 있다. 본문 수위: "데이터 이식성은 락인의 일부만 푼다 — 그래서 12장의 진짜 자산은 데이터가 아니라 이식 가능한 '명세'다."
- **인용 방식 제안:** 배경 지식으로만(논거 보강).
- **메모:** 이 카드가 12장의 핵심 논리축과 연결 — "도구가 죽어도 살아남는 이식 자산 = 명세(3장)·검증 체계(4장)·판단(2장)"이라는 브리프 항목 3을 떠받친다. 즉 데이터 이식성은 필요조건일 뿐, 진짜 보험은 1부 자산이라는 점을 데이터로 정당화.

---

## D. 반대 근거 — "도구를 자주 갈아타는 것이 오히려 손해" (브리프: 핵심 주장마다 반대 근거 1회)

## 카드 12: 도구를 너무 자주 바꾸면 컨텍스트 전환·재학습·마이그레이션 비용이 발생한다 — 안정성에도 값이 있다

- **주장:** 도구 전환·도구 난립(tool sprawl)에는 숨은 비용이 있다. 컨텍스트 전환은 생산 시간의 최대 40%를 소모할 수 있고(미국 경제 연 약 $450B 추정), 앱 전환 후 재집중에 주당 약 4시간이 들며, 마이그레이션 시 구현 실패·재학습·생산성 저하가 신규 도구 라이선스 비용을 압도할 수 있다. 반대로 도구 통합(consolidation)은 도구 관련 비용을 최대 30% 절감하고 생산성을 최대 25% 높인다는 업계(IDC/Forrester 인용) 보고가 있다.
- **출처:** ① "Context Switching Costs $450B/Year", waymakeros.com, https://www.waymakeros.com/learn/context-switching-costs-450b ② Syncro "The True Cost of IT Tool Sprawl", https://syncrosecure.com/blog/cost-of-it-tool-sprawl/ ③ The Digital Project Manager "Hidden Cost of Tool Sprawl", https://thedigitalprojectmanager.com/partner-spotlight/accelo/tool-sprawl-costs/
- **출처 등급:** 2차/3차(콘텐츠 마케팅성 블로그 다수) — 인용된 원 출처($450B, IDC/Forrester 25%/30%)는 **역추적 미완**. 본문 수록 시 수치보다 "방향성(전환에는 비용이 있다)"만 사용 권장.
- **확인일:** 2026-06-13
- **휘발성:** 태그 없음(현상의 구조적 성격).
- **반대 근거(이 카드 자체가 반대 근거):** 12장 주장("도구는 낡으니 갈아탈 준비를 하라")의 균형추. 즉 이 장은 "항상 최신 도구로 갈아타라"가 아니라 "**필요할 때만, 명세를 들고, 계획적으로** 갈아타라"여야 한다. 무분별한 도구 쇼핑은 자동화의 적.
- **인용 방식 제안:** 배경 지식으로만(수치 단정 금지). "갈아타기는 비용이 있다 → 새 도구 평가 5문항을 통과할 때만 움직여라"의 근거.
- **메모:** **챕터 톤을 교정하는 카드.** 브리프의 "새 도구 평가 5문항"·"갈아타기 실전 절차"가 "갈아타기를 부추기는 장"으로 오독되지 않게 하는 균형추. 작가는 이 장의 기본값을 "지금 도구를 계속 쓴다"로 두고, 5문항에 걸릴 때만 이동하도록 설계해야 한다.

---

## E. 휘발성·시장 변동 데이터 (브리프 조사대상 4 — "있으면")

## 카드 13: [수위 주의] AI 스타트업의 높은 폐업률이 보고되나, 자주 인용되는 수치들은 1차 출처 역추적이 안 됐다

- **주장(인용된 수치들, 신뢰도 낮음):** 여러 집계글이 "AI 스타트업 중간 수명 약 18개월", "AI 스타트업의 85%가 3년 내 폐업", "SaaS는 5년 내 약 70% 실패" 등을 제시한다. 단 이 수치들은 블로그·집계 매체에서 출처가 순환 인용되며 1차 데이터(연구·통계기관)로 역추적되지 않는다.
- **출처:** ① Tech Startups "Top AI Startups That Shut Down in 2025", https://techstartups.com/2025/12/09/top-ai-startups-that-shut-down-in-2025-what-founders-can-learn/ ② IdeaProof "319+ AI Startups That Failed", https://ideaproof.io/failures/ai-startups ③ 각종 SaaS 실패율 집계 블로그
- **출처 등급:** 3차(블로그·집계) — **1차 출처 없음. 원칙상 본문 사용 불가.**
- **확인일:** 2026-06-13
- **휘발성:** [휘발성]
- **반대 근거:** 해당 — 이 수치들 자체가 검증되지 않았다는 것이 반대 근거.
- **인용 방식 제안:** **본문에 수치로 쓰지 말 것.** "AI 도구 시장은 변동이 크다"는 정성적 주장은 카드 04~09의 실명 사례들로 충분히 뒷받침되므로, 검증 안 된 통계 대신 실명 사례를 쓰라.
- **메모:** 작가가 "85%가 망한다" 같은 통계의 유혹에 빠지지 않도록 일부러 카드로 남긴다 = 사실상 미확인 경고. 시장 변동성은 "수치"가 아니라 "사례의 누적"으로 보일 것.

---

## 미확인 목록 (본문에 쓰려면 [확인필요] 표시 필수)

- **OpenAI deprecations 공식 문서 원문(통지 기간 6개월/3개월/2주)** — developers.openai.com 403으로 원문 직접 미열람, 검색 요약 기준. 출간 전 원문 대조 필요(카드 02).
- **Google Gemini deprecations 문서 원문(일반 모델 통지 기간·shutdown 날짜)** — ai.google.dev 403. '-latest 2주' 외 일반 모델의 명확한 일수 정책 미확인(카드 03).
- **3사(OpenAI/Anthropic/Google) 통지 기간 비교표의 Google 칸 정확한 숫자** — Google은 명확한 일수 정책이 약함. 표에 "사전 통지(별칭 2주)"로만 기재 가능.
- **AI 스타트업 폐업률·평균 수명 통계의 1차 출처** — 전부 블로그 순환 인용, 역추적 실패(카드 13). 본문 수치 사용 불가.
- **tool churn/컨텍스트 전환 비용 수치($450B, IDC/Forrester 25%/30%)의 1차 출처** — 마케팅성 블로그 인용, 역추적 미완. 방향성만 사용(카드 12).
- **Meta Workplace 종료 공식 발표 원문(forwork.meta.com)** — 미열람. 타임라인은 매체 일치(카드 05).
- **TechCrunch Visual Electric 기사 원문** — 403으로 직접 미열람. 90일·데이터 내보내기·환불은 복수 매체 일치(카드 06).
- **Google Gemini CLI 종료 Google 공식 공지 원문** — 미열람, The Register 등 매체 기준. 발효일 2026-06-18(조사일 직후)이라 출간 시 결과 재확인 필요(카드 07).
- **Anthropic 모델 보존 약속(deprecation-commitments) 페이지 원문** — anthropic.com 403. 핵심(가중치 장기 보존, Opus 3 은퇴 후에도 접근 유지)은 platform.claude.com 공식 문서로 교차 확인됨(카드 01 메모) — 다만 약속 전문 인용 시 원문 대조 권장.

---

## ch05 스파이크 연결 평가 (브리프 조사대상 — 아임리포트 → 12장 최상위 리스크)

**연결 가능. 권장.** `research/ch05-spike.md` 카드 06(아임리포트) + 카드 06 반대근거·메모가 이미 "서드파티 의존이라는 점에서 12장(갈아타기 프로토콜)의 '도구 존속 리스크' 최상위 사례가 된다"고 명시했다. 12장에서 다음과 같이 회수할 수 있다:

1. **위험도 위계의 정점 사례로.** 12장 "낡는 순서"에서 도구 존속 리스크는 소규모 서드파티 SaaS가 가장 높다. 아임리포트(소규모 한국 SaaS, ch05 카드 06·81행 "[휘발성] 가격 변경·서비스 종료 리스크가 도구 3종보다 훨씬 높음")는 본문 도구 중 존속 리스크 최상위 = 새 도구 평가 5문항 "죽어도 대체재가 있는가"의 살아있는 적용 대상.
2. **이식 자산 논리의 시연 대상으로.** 만약 아임리포트가 죽으면? 5장 플랜 B(네이버 수동 다운로드, ch05 카드 10)가 곧바로 대체 경로가 된다 — 시트 허브(ch05 카드 11)와 합산·정규화 로직(명세)은 그대로 살아남고 "네이버→시트 연결"만 갈아끼우면 된다. 이것이 12장 "명세는 그대로, 연결만 새로"의 완벽한 실증 사례.
3. **단, 카드 06이 V-1(실설치 검증) 미통과 상태**임에 유의. 아임리포트가 5장 본문 기본 경로로 채택될지 미정(스파이크 판정은 플랜 B 권고). 12장 집필 시 "5장에서 어떤 경로가 기본이 됐든, 서드파티 커넥터를 쓴다면 그것이 가장 먼저 죽을 후보"라는 **도구 비종속적 원리**로 쓰면 5장 확정 전에도 안전하다(브리프 1행 "원리 수준으로만 참조" 지침과 합치).

**권고:** 12장은 아임리포트를 "실명 박스" 한 칸으로 넣되, 본문 논리는 "서드파티 SaaS = 최상위 존속 리스크"라는 원리로 전개. 5장 본문 경로가 스파이크 후 확정되면 편집장 정합성 패스에서 박스 문구를 맞춘다.
