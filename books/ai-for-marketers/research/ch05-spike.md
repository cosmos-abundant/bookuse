# ch05 과업 A 스파이크 자료카드 — 네이버·메타·구글 노코드 연결 판정

- 조사일: 2026-06-12 (researcher)
- 스파이크 판정 질문: 네이버 검색광고 API(HMAC 서명 인증)를 Make/n8n/Zapier로, VLOOKUP 수준 사용자가 따라 할 수 있게 연결할 수 있는가?
- **판정 결과: ② 플랜 B(네이버 수동 다운로드 하이브리드) 채택 권고.** 단, 문서 조사에서 발견된 "제3 경로"(구글 시트 부가기능형 전용 커넥터, 카드 06)가 실구축 검증을 통과하면 기본 경로 승격 가능. 근거는 아래 카드, 한계는 말미 "실제 구축 검증 필요 항목" 참조.
- 조사 제약 고지: naver.github.io(공식 API 문서 사이트), make.com 헬프, docs.n8n.io, support.google.com 등 다수 페이지가 자동화 접근 차단(HTTP 403)으로 직접 열람 불가했다. 해당 항목은 GitHub 저장소 원문·검색 결과 요약·커뮤니티 스레드로 교차 확인했으며, 원문 직접 확인이 안 된 부분은 카드에 명시하고 "실제 구축 검증 필요 항목"으로 분리했다.

---

## 카드 01: 네이버 검색광고 API는 요청마다 HMAC-SHA256 서명을 만들어 보내야 하는 인증 방식이다

- **주장:** 네이버 검색광고 API는 모든 요청 헤더에 X-Timestamp(밀리초 타임스탬프), X-API-KEY, X-Customer(고객 ID), X-Signature를 요구하며, X-Signature는 "타임스탬프·HTTP 메서드·URI 경로"를 조합한 문자열을 비밀키(SECRET_KEY)로 HMAC-SHA256 해시한 뒤 Base64 인코딩해 만든다. API 라이선스(액세스 라이선스·비밀키)는 네이버 검색광고 관리시스템의 도구 > API 사용 관리(API Manager)에서 발급한다.
- **출처:** ① 네이버 검색광고 API 공식 문서 저장소 README, naver/searchad-apidoc, GitHub, https://github.com/naver/searchad-apidoc (raw README 직접 확인 — 발급 절차·샘플 언어 Java/PHP/Python 확인) ② 공식 API 명세 사이트 https://naver.github.io/searchad-apidoc/ (403으로 직접 열람 불가, 서명 규칙은 검색 결과 요약 및 아래 ③으로 교차 확인) ③ "Invalid Signature 오류 관련 문의", naver/searchad-apidoc Issue #1029, https://github.com/naver/searchad-apidoc/issues/1029
- **출처 등급:** 1차(공식 저장소·공식 문서) + 보조 교차 확인
- **확인일:** 2026-06-12
- **휘발성:** [휘발성] — 인증 방식 자체는 수년간 유지됐으나 API 정책 변경 가능
- **반대 근거:** 검색했으나 미발견 — OAuth 등 더 쉬운 대체 인증을 제공한다는 자료 없음. 서명 인증이 유일한 경로.
- **인용 방식 제안:** 배경 지식으로만 (본문에서는 "요청할 때마다 일회용 도장(서명)을 직접 찍어야 하는 방식" 수준으로 풀어 쓸 것)
- **메모:** 공식 샘플 코드가 Java/PHP/Python뿐이라는 사실 자체가 "비개발자를 상정하지 않은 API"라는 본문 논거가 된다. 서명 문자열의 정확한 구성(구분자 등)은 공식 문서 원문 재확인 필요 → 검증 항목 V-2.

---

## 카드 02: Make·n8n·Zapier 어디에도 네이버 검색광고 기성(클릭만으로 연결되는) 커넥터는 없다

- **주장:** 2026년 6월 12일 기준, Zapier 앱 디렉터리·Make 앱 카탈로그(3,000+ 앱)·n8n 내장 노드 및 검증된 커뮤니티 노드 어디에도 네이버 검색광고 전용 커넥터가 존재하지 않는다. 세 도구 모두 "HTTP 요청 모듈 + 서명 직접 생성"의 범용 우회만 가능하다.
- **출처:** ① Make 앱 카탈로그, https://www.make.com/en/integrations (Naver 검색 결과 없음 — 검색 엔진 경유 확인) ② n8n 통합 문서, https://docs.n8n.io/integrations/ 및 커뮤니티 노드 검색 — 네이버 검색광고 노드 미발견, npm에도 해당 패키지 미발견(2026-06-12 검색 기준) ③ n8n Korea 커뮤니티 "네이버 광고 API 검색 자동화 문의", https://www.skool.com/n8nkorea/api — 기성 노드가 없어 HMAC-SHA256+Base64 서명을 직접 만들어야 한다는 실무 문의 ④ Zapier 앱 디렉터리에 Naver Search Ads 부재(검색 결과 기준)
- **출처 등급:** 1차(공식 카탈로그) — 단 "부재 증명"은 검색 기반이므로 완전하지 않음
- **확인일:** 2026-06-12
- **휘발성:** [휘발성] — 커넥터는 언제든 추가될 수 있음. 집필 직전·출간 직전 재확인 필수
- **반대 근거:** 검색했으나 미발견 — "네이버 검색광고를 Make/n8n/Zapier 기성 커넥터로 연결했다"는 사례 0건. 반대로 커스텀 노드를 직접 개발했다는 사례(인포그랩 블로그 등)는 존재 = 기성 경로 부재의 방증.
- **인용 방식 제안:** 수치만("2026년 6월 기준 3대 노코드 도구 모두 전용 커넥터 없음")
- **메모:** 이 카드가 판정 ②의 1차 근거. "부재"는 악마의 증명이므로 본문에서는 "확인일 기준"을 반드시 달 것.

---

## 카드 03: n8n에서는 코드 노드 없이 Crypto 노드로 HMAC 서명을 만들 수 있다 — 그러나 VLOOKUP 페르소나 눈높이를 초과한다

- **주장:** n8n 내장 Crypto 노드는 HMAC 연산(SHA256 포함, Base64 출력)을 지원하므로, 이론상 "Schedule → Set(타임스탬프·서명 문자열 조립) → Crypto(HMAC) → HTTP Request" 구성으로 코드 노드 없이 네이버 API 호출이 가능하다. 그러나 ① 서명 대상 문자열을 표현식(JavaScript expression)으로 직접 조립해야 하고 ② 밀리초 타임스탬프 생성도 표현식이며 ③ 커뮤니티에 인코딩 불일치·401 Unauthorized로 막힌 스레드가 반복 등장한다. 이는 "코드 한 줄 없이"의 문언은 충족할지 몰라도 실질은 코드 작성에 준한다.
- **출처:** ① Crypto 노드 공식 문서, n8n Docs, https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto/ (403으로 원문 직접 열람 불가, 검색 결과 요약으로 HMAC/SHA256/Base64 지원 확인) ② "HTTP Request Authentication w/HMAC-SHA256 - Stuck", n8n Community, https://community.n8n.io/t/http-request-authentication-w-hmac-sha256-stuck/167257 ③ "HMAC-SHA 256 signature issues", n8n Community, https://community.n8n.io/t/hmac-sha-256-signature-issues/33460 ④ n8n Korea 커뮤니티 문의(카드 02-③)
- **출처 등급:** 1차(공식 문서) + 3차(커뮤니티 — 난도 평가의 실증으로만 사용)
- **확인일:** 2026-06-12
- **휘발성:** [휘발성]
- **반대 근거:** 있음 — "n8n은 노코드로 HMAC 서명이 가능하다"는 주장 자체는 사실이다(공식 문서·성공 사례 존재). 즉 "불가능"이라고 쓰면 틀린다. 정확한 수위: "가능하지만, 표현식 작성과 401 디버깅을 감당해야 하며 이는 본서 페르소나의 범위를 벗어난다."
- **인용 방식 제안:** 배경 지식으로만 + 분기 박스("이미 n8n에 익숙한 독자라면" 경로)에 레시피 제공 검토
- **메모:** 복붙 가능한 완성 레시피를 책이 제공하면 페르소나도 따라 할 수는 있다 — 단 "안 될 때 스스로 못 고친다"가 결정적 결함(10장 응급처치로도 서명 오류는 못 가르친다). 실측 검증 항목 V-3.

---

## 카드 04: Make에서는 내장 sha256 함수(key 파라미터)로 HMAC을 만들 수 있다 — 역시 수식 직접 작성이 필요하다

- **주장:** Make는 내장 함수 sha256(text; [encoding]; [key])의 key 파라미터로 HMAC-SHA256을, encoding 파라미터로 Base64 출력을 지원해 HTTP 모듈 헤더 필드 안에서 서명 생성이 가능하다. 그러나 사용자가 함수식(타임스탬프·메서드·경로 문자열 조립 포함)을 한 줄 수식으로 직접 작성해야 하며, Make 커뮤니티에는 이 과정에서 막힌 질문 스레드가 다수다(Binance 등 동일 유형 서명 API 사례).
- **출처:** ① "How to generate an HMAC SHA256 signature on make", Make Community, https://community.make.com/t/how-to-generate-an-hmac-sha256-signature-on-make/17925 ② "Sha256 hmac", Make Community, https://community.make.com/t/sha256-hmac/50966 ③ "Binance HTTP Signature (hmac sha256 hash)", Make Community, https://community.make.com/t/binance-http-signature-hmac-sha256-hash/44602 ④ Make 공식 함수 문서 https://www.make.com/en/help/functions/string-functions (403으로 원문 직접 열람 불가 — 함수 시그니처는 커뮤니티 스레드 답변으로 교차 확인)
- **출처 등급:** 1차(공식 문서 — 미열람) + 3차(공식 커뮤니티 — 직원·고수 답변 포함, 난도 실증용)
- **확인일:** 2026-06-12
- **휘발성:** [휘발성]
- **반대 근거:** 있음 — 커뮤니티에 성공 보고가 존재하므로 "Make로는 불가"는 틀린 표현. 정확한 수위: "가능하지만 한 줄짜리 함수식이 사실상 코드이며, 오류 시 원인 추적이 페르소나에게 불가능하다."
- **인용 방식 제안:** 배경 지식으로만
- **메모:** sha256 함수의 정확한 파라미터 순서·인코딩 옵션은 공식 문서 원문 미확인 → 검증 항목 V-3에 포함.

---

## 카드 05: Zapier는 코드 스텝(Code by Zapier) 없이는 HMAC 서명을 만들 수 없다 — 네이버 경로 탈락

- **주장:** Zapier의 Webhooks by Zapier에는 요청별 HMAC 서명 생성 기능이 내장되어 있지 않아, 네이버 검색광고 API 호출에는 JavaScript/Python을 쓰는 Code by Zapier 스텝이 필요하다. 이는 "코드 한 줄 없이" 약속을 문언 그대로 위반하므로 본서의 네이버 연결 경로에서 제외한다.
- **출처:** ① "Secure Your Automation Webhooks with Signature Verification (Zapier, Make, n8n, IFTTT)", codehooks.io, https://codehooks.io/blog/secure-zapier-make-n8n-webhooks-signature-verification ② "Outgoing webhooks security in Zapier", Zapier Community, https://community.zapier.com/general-discussion-13/outgoing-webhooks-security-in-zapier-7736 — Code 스텝 + crypto.createHmac 사용이 표준 답변
- **출처 등급:** 2차 + 3차(공식 커뮤니티) — Zapier 공식 문서의 명시적 "불가" 선언은 미발견(부재 증명의 한계)
- **확인일:** 2026-06-12
- **휘발성:** [휘발성]
- **반대 근거:** 검색했으나 미발견 — 코드 스텝 없이 Zapier에서 요청별 HMAC을 생성한 사례 없음.
- **인용 방식 제안:** 배경 지식으로만 (도구 선택 가이드 표의 "네이버 연결" 행에 반영)
- **메모:** Zapier는 가격(카드 09)에서도 불리해, 5장 도구 선택 가이드에서 "이미 회사가 쓰고 있는 경우"로 한정될 가능성 높음.

---

## 카드 06: [제3 경로 — 챕터 방향을 바꿀 후보] 네이버 검색광고를 구글 시트에 자동 갱신해주는 전용 시트 부가기능(아임리포트)이 존재한다

- **주장:** 구글 워크스페이스 마켓플레이스에 "Naver Search Ads Data API Integration: I'm Report(아임리포트)" 부가기능이 등록되어 있다. 네이버 검색광고 데이터를 구글 스프레드시트에 연동하고 매일 아침 자동 갱신하며, 검색어·광고그룹·캠페인 성과와 200여 종의 보고서 템플릿을 제공한다고 소개된다. 사용자 입장에서는 시트 부가기능 설치 + 네이버 API 라이선스 키 입력 수준으로, HMAC 서명을 서비스가 대신 처리하는 진짜 노코드 경로다.
- **출처:** ① 구글 워크스페이스 마켓플레이스 등록 페이지, https://workspace.google.com/marketplace/app/naver_search_ads_data_api_integration_im/158359210801 (403으로 상세 페이지 직접 열람 불가 — 등재 사실·기능 설명은 검색 결과의 마켓플레이스 공식 설명문 기준) ② 아임리포트 공식 사이트, https://imreport.io/ (403 — 미열람)
- **출처 등급:** 1차(마켓플레이스 공식 등재 정보) — 단 가격·설치 수·갱신 안정성·API 키 입력 절차는 미확인
- **확인일:** 2026-06-12
- **휘발성:** [휘발성] — 소규모 서드파티 SaaS. 가격 변경·서비스 종료 리스크가 도구 3종보다 훨씬 높음
- **반대 근거:** 일부 있음 — 이 경로도 "네이버 API 라이선스 발급"(광고시스템에서 키 2종 발급)은 독자가 직접 해야 할 가능성이 높다(서비스 구조상 추정 — 미확인). 또한 서드파티 의존이라는 점에서 12장(갈아타기 프로토콜)의 "도구 존속 리스크" 최상위 사례가 된다.
- **인용 방식 제안:** 직접 인용(도구명·기능) — 단 실구축 검증(V-1) 통과 전에는 본문 기본 경로로 쓰지 말 것
- **메모:** **이 카드가 이번 스파이크의 최대 발견이다.** "Make/n8n/Zapier로 푼다"는 문제 설정 자체가 틀렸을 수 있다 — 한국 광고 채널은 한국형 전용 커넥터(시트 부가기능형)로 푸는 게 실무 표준일 가능성. 유사 서비스 추가 탐색 필요(예: SyncWith는 Google Ads/TikTok 지원, https://workspace.google.com/marketplace/app/syncwith_for_google_ads_tiktok/224327267122 — 네이버 미지원). "포터(Porter)" 등 타 한국 서비스는 검색으로 실체 확인 실패 → 미확인 목록.

---

## 카드 07: 메타 광고는 Make에 보고용 기성 커넥터가 성숙해 있다

- **주장:** Make에는 Facebook Insights 앱(광고 계정·캠페인·광고세트·광고 단위 인사이트 조회)과 Facebook Ads Campaign Management 앱이 있고, "Facebook Ads 캠페인 보고서를 이메일로 발송"하는 공식 템플릿까지 제공된다. 즉 메타 광고 성과 데이터의 주기적 시트 적재는 기성 모듈 클릭 구성으로 가능하다. n8n은 범용 Facebook Graph API 노드 경유(난도 중상), Zapier는 리드 광고·전환 전송 중심으로 성과 보고 용도는 약하다.
- **출처:** ① Facebook Insights 통합 페이지, Make, https://www.make.com/en/integrations/facebook-insights ② 공식 템플릿 "Generate and email Facebook Ads campaign reports", Make, https://www.make.com/en/templates/11863-send-facebook-ads-campaigns-report-via-email ③ Facebook Ads Campaign Management 앱 문서, Make, https://www.make.com/en/help/app/facebook-ads-cm
- **출처 등급:** 1차(공식 카탈로그·문서)
- **확인일:** 2026-06-12
- **휘발성:** [휘발성] — 메타 마케팅 API는 버전 폐기 주기가 빠름(연 2~3회). 모듈 권한·필드 변경 잦음
- **반대 근거:** 일부 있음 — Make 커뮤니티에 캠페인 데이터 추출이 기대처럼 안 된다는 질문 스레드 존재(https://community.make.com/t/extract-facebook-campaigns-data-for-data-visualization/14181). "클릭 몇 번이면 끝"으로 쓰지 말고 "기성 모듈이 있어 서명 같은 벽은 없다" 수위로.
- **인용 방식 제안:** 배경 지식으로만 + 절차는 실측 후 수록
- **메모:** 메타 연결의 실제 마찰은 서명이 아니라 메타 비즈니스 계정 권한·앱 승인 쪽일 수 있음 → 실측 검증 V-4.

---

## 카드 08: 구글 광고는 공식 구글 시트 부가기능(무료·예약 새로고침)이 있다 — 단 언어·지역 제한 가능성 미해소

- **주장:** Google Ads는 공식 Google Sheets 부가기능을 무료 제공하며, 보고서를 시트에 생성하고 "Schedule this report"로 주기적 자동 새로고침이 가능하다. 단 검색 결과 요약 기준 "영어 버전 Google Sheets에서만, 미국에서만 제공"이라는 제한 문구가 있어 한국 독자 기준 사용 가능 여부가 미확정이다. 대안으로 n8n 내장 Google Ads 노드, Make Google Ads 앱, Zapier Google Ads 통합(보고서 생성 액션 포함)이 모두 존재한다 — 구글 채널은 어느 도구든 기성 경로가 있다.
- **출처:** ① "About the add-on for Google Sheets", Google Ads Help, https://support.google.com/google-ads/answer/9000139 (403으로 원문 직접 열람 불가 — 제한 문구는 검색 요약 기준이라 원문 확인 필요) ② Google Ads 노드 문서, n8n Docs, https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googleads/ ③ "How to get started with Google Ads on Zapier", Zapier Help, https://help.zapier.com/hc/en-us/articles/8495986864781-How-to-get-started-with-Google-Ads-on-Zapier
- **출처 등급:** 1차(공식 문서 — 일부 미열람)
- **확인일:** 2026-06-12
- **휘발성:** [휘발성]
- **반대 근거:** 있음 — 위 ①의 언어/지역 제한 문구. 한국어 시트에서 작동하지 않으면 "공식 부가기능" 경로는 본문에서 빼거나 조건부로 써야 한다. 원문·실측 확인 전 단정 금지(V-5).
- **인용 방식 제안:** 배경 지식으로만, 제한 사항 해소 전까지 [확인필요] 수준
- **메모:** 구글 채널의 안전한 기본 경로는 노코드 도구의 Google Ads 커넥터(OAuth 로그인 방식 — 서명 불요) 쪽. 부가기능은 검증 후 분기 박스 후보.

---

## 카드 09: 노코드 도구 3종 가격 (2026년 6월 검색 기준 — 공식 페이지 원문 미확인)

- **주장:** 2026년 검색 시점 기준 — Zapier: 무료 100 tasks/월(2스텝 제한), Professional $29.99/월(750 tasks). Make: Core $9/월(10,000 operations). n8n: 셀프호스트 커뮤니티 에디션 무료(실행 무제한), 클라우드 Starter €24/월, Pro €60/월. 과금 단위가 다르다: Zapier는 스텝(task)당, Make는 모듈 작동(operation)당, n8n은 워크플로 실행(execution)당 — 같은 워크플로라도 비용이 수 배 차이날 수 있다.
- **출처:** ① "Zapier Pricing 2026", No Code MBA, https://www.nocode.mba/articles/zapier-pricing-2026 ② "n8n Pricing 2026", connectsafely.ai, https://connectsafely.ai/articles/n8n-cloud-pricing-guide ③ "n8n vs Zapier Pricing & Comparison 2026", Cipher Projects, https://cipherprojects.com/blog/posts/n8n-vs-zapier-automation-tool-comparison/ ④ 공식 가격 페이지(zapier.com/pricing, make.com/en/pricing, n8n.io/pricing)는 403으로 원문 확인 실패
- **출처 등급:** 2차(전문 매체/블로그) — **원 출처(공식 가격 페이지) 역추적 미완. 본문 수록 전 공식 페이지 대조 필수**
- **확인일:** 2026-06-12
- **휘발성:** [휘발성] — 가격은 가장 빨리 낡는 정보. 책에는 "2026년 6월 기준" 박스 + 절대액보다 과금 단위 차이(원리)를 중심으로
- **반대 근거:** 2차 출처 간 수치 불일치 가능성 상존(Make 무료 플랜 한도 등 미확인 항목 있음).
- **인용 방식 제안:** 수치만 + 시점 명시. 과금 단위 차이는 직접 설명 가능(구조적 사실)
- **메모:** 페르소나 비용 시나리오(주 1회 실행, 모듈 10개 내외)에서는 셋 다 무료~최저 플랜으로 충분할 것으로 추정 — 추정이므로 본문에는 실측 후.

---

## 카드 10: [플랜 B 근거] 네이버 광고시스템에는 엑셀형 맞춤 보고서(다차원 보고서)와 대용량 다운로드 보고서(TSV)가 있다

- **주장:** 네이버 검색광고 관리시스템의 보고서 메뉴는 '다차원 보고서'와 '대용량 다운로드 보고서'로 구성된다. 다차원 보고서는 기본(캠페인·광고그룹·키워드·소재별)·전환·시간·지역·매체 차원의 맞춤 보고서를 엑셀 피벗테이블 형식으로 만들고 저장(템플릿 재사용)할 수 있다. 대용량 다운로드 보고서는 계정 단위·특정일 단위 TSV 파일로, 별도 가공 도구를 가진 고급 사용자용이다. 플랜 B의 수동 단계는 "저장해둔 다차원 보고서 열기 → 기간 지정 → 다운로드"로 설계 가능하다.
- **출처:** ① "네이버광고 보고서 활용법!", 마케팅 인사이드(검색광고 대행 공식 매거진), https://inside.ampm.co.kr/insight/624 ② "대용량보고서 신규 추가 공지 (StatReport)", 네이버 검색광고 API 공식 공지, 2021-03-09, http://naver.github.io/searchad-apidoc/notice/2021/03/09/notice1/ — API 측 대용량 보고서도 TSV 제공임을 확인
- **출처 등급:** ①은 2차, ②는 1차(공식 공지)
- **확인일:** 2026-06-12
- **휘발성:** [휘발성] — 광고시스템 UI 메뉴 구성은 개편 잦음. 책에는 클릭 경로보다 "보고서 메뉴에서 저장해둔 보고서를 다운로드한다" 수준으로 UI 의존 최소화
- **반대 근거:** 검색했으나 미발견 — 보고서 다운로드 기능 폐지·축소 소식 없음.
- **인용 방식 제안:** 배경 지식으로만, 정확한 클릭 경로·파일 형식(xlsx/csv 구분)·열 구조는 실측(V-6) 후 수록
- **메모:** 플랜 B 핵심 설계: 다운로드 파일을 구글 드라이브 지정 폴더에 넣으면(또는 시트의 '네이버 원본' 탭에 붙여넣으면) 이후 정규화·합산은 노코드 도구가 자동 처리. "수동 5분" 계상은 실측으로 검증(과업 D와 연동).

---

## 카드 11: [시트 허브 근거] 광고 데이터 커넥터 생태계는 목적지로 '구글 시트'에 수렴해 있다

- **주장:** 이번 조사에서 확인된 광고 데이터 자동 적재 경로들 — Google Ads 공식 부가기능(카드 08), 네이버용 아임리포트(카드 06), SyncWith 등 서드파티 커넥터, Make/n8n의 공식 보고서 템플릿(카드 07의 Make 템플릿, n8n의 "Google Ads → Google Sheets" 템플릿 다수) — 은 모두 구글 스프레드시트를 기본 목적지로 제공한다. 비개발자가 검수·수정·공유할 수 있는 유일한 공용 데이터 허브가 시트이기 때문에, 5장의 "DB가 아니라 시트" 선택은 생태계 표준과 일치한다.
- **출처:** ① 카드 06·07·08의 각 공식 페이지 ② n8n 공식 워크플로 템플릿 "Automated Google Ads campaign reporting to Google Sheets", https://n8n.io/workflows/7387-automated-google-ads-campaign-reporting-to-google-sheets-with-airtable/ 외 다수
- **출처 등급:** 1차(각 공식 카탈로그의 존재 사실) — 단 "수렴해 있다"는 본 조사의 관찰·해석
- **확인일:** 2026-06-12
- **휘발성:** 태그 없음(구조적 경향) — 단 개별 도구명은 [휘발성]
- **반대 근거:** 있음 — 데이터 규모가 커지면 시트는 행 수·동시 편집 한계에 부딪히며, 전문 영역에서는 Looker Studio+DB·BI 도구가 표준이라는 반론 가능(Supermetrics 등은 DWH 연결을 상위 플랜으로 판매). 본문 수위: "주간 보고 규모(수백~수천 행)에서는 시트가 최적, 그 이상이면 다른 책이 필요하다"로 한계 명시.
- **인용 방식 제안:** 배경 지식으로만(논거의 보강 증거)
- **메모:** 이 카드는 사실 카드라기보다 논거 카드. 작가는 "모든 커넥터가 시트를 지원한다" 같은 전칭 명제로 쓰지 말 것.

---

## 카드 12: [난도 실증] 서명 인증은 개발자들도 반복적으로 틀리는 지점이다

- **주장:** 네이버 검색광고 API 공식 저장소에는 "Invalid Signature" 오류 문의 이슈가 다년간 반복 등록되어 있고, n8n·Make 커뮤니티에도 HMAC 서명 401 오류로 막힌 스레드가 다수다. 즉 서명 생성은 코드를 읽는 사용자조차 빈번히 실패하는 단계이며, "안 되면 어떻게 한다"를 책이 가르칠 수 없는(오류 메시지가 원인을 알려주지 않는) 유형의 실패다.
- **출처:** ① naver/searchad-apidoc Issue #1029 (Invalid Signature 문의), https://github.com/naver/searchad-apidoc/issues/1029 ② n8n Community 스레드 2건(카드 03-②③) ③ Make Community 스레드 3건(카드 04-①②③)
- **출처 등급:** 3차(커뮤니티) — 단 "이런 실패 보고가 다수 존재한다"는 사실 자체의 증거로는 1차적 성격
- **확인일:** 2026-06-12
- **휘발성:** 태그 없음(현상의 구조적 성격)
- **반대 근거:** 검색했으나 미발견 — "서명 인증이 쉽다"는 비개발자 후기 0건.
- **인용 방식 제안:** 배경 지식으로만 (판정 ②를 본문에서 정당화할 때 "개발자 커뮤니티에서도 가장 자주 막히는 지점" 정도로)
- **메모:** 판정 ②의 질적 근거. ①(순수 노코드)을 기각한 이유는 "기술적 불가"가 아니라 "실패 시 자력 복구 불가"임을 본문에 정직하게 쓸 것.

---

## 미확인 목록

카드로 만들지 못한 주장. 본문에 쓰려면 [확인필요] 표시 필수.

- **아임리포트의 가격(무료 여부)·설치 수·자동 갱신 안정성·메타/구글/카카오 확장 지원 여부** — imreport.io 및 마켓플레이스 상세 페이지 403으로 미열람. → 검증 항목 V-1
- **Google Ads 공식 시트 부가기능의 언어·지역 제한 정확한 현황(한국 계정·한국어 시트 작동 여부)** — 공식 헬프 원문 403, 2차 요약만 확보. → V-5
- **Make 무료 플랜의 월 오퍼레이션 한도** — 검색 결과에 신뢰할 수치 없음. 공식 페이지 403.
- **네이버 다차원 보고서 다운로드 파일의 정확한 형식(xlsx/csv)과 열 구조, 클릭 경로, 소요 시간 "약 5분"의 실측치** — 광고주 계정 로그인 필요. → V-6
- **네이버 API 서명 문자열의 정확한 구성(구분자 "." 여부 등)과 Stats(통계) 엔드포인트의 요청·응답 명세** — 공식 문서 사이트 403. → V-2
- **"포터(Porter)" 등 아임리포트 외 한국형 광고 데이터 커넥터 서비스의 실체** — 검색으로 확인 실패. 유사 서비스 지형 추가 탐색 필요.
- **메타 광고 연결의 실제 마찰 지점(비즈니스 계정 권한·앱 검수 요구 수준)** — 문서만으로 판정 불가. → V-4

## 실제 구축 검증 필요 항목 (발행인 실세계 과업 — 에이전트는 광고 계정·실 구축 불가)

| # | 검증 항목 | 판정에 미치는 영향 |
|---|---|---|
| V-1 | **아임리포트 실설치**: 설치→네이버 API 키 발급·입력→자동 갱신 확인, 가격·무료 한도 확인, 소요 시간 실측 | **통과 시 네이버 경로가 "진짜 노코드"로 승격 → 판정 ②의 플랜 B가 분기 박스로 강등되고 제3 경로가 기본이 될 수 있음** |
| V-2 | 네이버 API 라이선스 발급 절차 실측(도구>API 사용 관리) + 공식 문서의 서명 규칙·Stats 엔드포인트 원문 확인 | 카드 01 보강. 아임리포트 경로에서도 키 발급은 독자 몫 |
| V-3 | Make·n8n "복붙 레시피" 재현성 실측: 본서가 완성 시나리오/워크플로 JSON을 제공할 때 페르소나가 값 3개(키·시크릿·고객ID)만 바꿔 작동시킬 수 있는가 | 통과하면 "고급 분기 박스"로 수록 가능. 실패 패턴 수집은 10장 재료 |
| V-4 | 메타(Make Facebook Insights)·구글(커넥터 또는 공식 부가기능) 연결 소요 시간·마찰 실측 | "메타·구글은 성숙" 전제의 실증. 과업 D(베타 리더)와 연동 |
| V-5 | Google Ads 공식 시트 부가기능의 한국 환경 작동 여부 | 카드 08 확정 |
| V-6 | 네이버 보고서 수동 다운로드 경로·형식·소요 실측 | 플랜 B 본문 절차 + "수동 5분" 계상 근거 |
