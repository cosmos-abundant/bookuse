# ch04 팩트체크 보고서 — 「사람이 마지막에 본다 — 검증 체계 설계」

- 감수자: fact-checker / 작성일: 2026-06-13 / 기준 시점: 2026-06-13
- 대상 원고: `books/ai-for-marketers/manuscript/ch04.md` (구조편집·교정 통과본)
- 대조 자료: `research/ch04-verification.md` (카드 01~11 + 재활용 4건), `research/ch02-selection.md`(Air Canada=카드05, Bard=카드07, automation bias=카드10), `research/ch01-foundations.md`(카드09)
- 장르: AI 활용법 — 버전·시점 명시 의무, 절차 재현성, [휘발성] 항목 재확인 적용

---

## 요약 판정

- **검증 항목: 27건**
- **오류: 1건** (원화 환산 — 교정자 회부 건)
- **불확실: 0건**
- **해소된 [확인필요]: 0건** (원고에 `[확인필요]` 표시 없음 — 작가가 미확인 4건을 전부 본문에서 배제함)
- **게이트 판정: 불통과** (오류 1건). 아래 [E-1] 정정 후 재확인 시 통과 가능.

미확인 목록 4건(국내 사례 / 과잉일반화 5배 / 검수시간 통계 / 원문 직접인용 문구)의 본문 유입 여부를 전수 점검한 결과, **유입 0건**. 작가의 출처 규율은 적절하다. 유일한 문제는 사실 주장이 아니라 환율 환산 산수다.

---

## [E-1] 오류 — 원화 환산 (교정자 회부 건 / line 5)

**원문:** "약 4억 4,000만 원 규모(A$440,000)의 보고서를 납품했다."

**문제:** A$440,000을 약 4억 4,000만 원으로 환산한 것은 **약 1 AUD = 1,000원**이라는 어림셈에 기반한 것으로 보인다. 그러나 2026-06 기준 실제 환율은 **1 AUD ≈ 1,080원**(2026-06-08 기준 1,079.79원)이다.
- 정확 환산: A$440,000 × 1,080 ≈ **4억 7,500만 원** (4억 7,000만~4억 8,000만 원대).
- 본문 "4억 4,000만 원"은 실제보다 약 3,500만 원(약 7%) 낮다. 환율 어림셈을 1:1000으로 쓴 흔한 오차다.

**근거:** AUD/KRW 2026년 환율 이력 (exchange-rates.org), 2026-06-08 기준 1 AUD = 1,079.79 KRW.

**정정안 (택1):**
1. **(권장)** 수치를 갱신: "약 4억 7,000만 원 규모(A$440,000, 2026년 6월 환율 기준)". 환율 변동성을 감안해 환산 시점을 병기.
2. 원화 환산을 빼고 원통화만: "A$440,000(약 29만 미국 달러) 규모". 카드 02도 "약 29만 달러"를 병기하고 있어 정합. 환율 휘발성 자체를 회피하는 안전책.
3. 어림 표현으로 완화: "약 4억 원대(A$440,000)" — 다만 4.4억으로 못박은 현재보다 모호하므로 1안 또는 2안을 우선 권장.

> 메모: AI 활용법 장르 규칙상 환율 같은 휘발성 수치는 시점 병기가 원칙. 1안 채택 시 "2026년 6월 환율 기준" 문구를 반드시 동반할 것.

---

## 확인 항목 (출처 명시)

### 실명 사례

**[C-1] Mata v. Avianca — 가짜 판례 6건 (line 27)** 확인.
2023년 뉴욕남부연방지방법원(S.D.N.Y.), ChatGPT 작성 서면에 실재하지 않는 판례 6건 인용. 카드 01 + 독립 교차(Seyfarth, ACC, Wikipedia, LegalClarity). **교차 충분.**

**[C-2] Mata 제재금 5,000달러 (line 27)** 확인.
2023-06-22 Castel 판사가 변호사 2인(LoDuca, Schwartz)과 로펌 Levidow에 5,000달러 제재금 부과. 카드 01 + 독립 교차(Seyfarth, LegalClarity, letsaskclaire). **교차 충분** — 카드가 우려한 1차 판결문 403 차단은 복수 2차로 해소됨. 금액·건수·날짜·판사명 일치.

**[C-3] Mata 제재 사유 한정 (line 27)** 확인.
"제재 사유는 AI 사용이 아니라 가짜임을 의심할 정황이 있었는데도 끝까지 진위를 호도한 행위"라는 본문 한정은 카드 01 반대근거 ①과 정확히 일치하며, 독립 출처(LegalClarity: "cascading failure to admit a mistake", 가벼운 쪽 제재)와도 부합. 카드의 수위 권고를 본문이 충실히 반영. 양호.

**[C-4] Deloitte 호주 — DEWR, A$440,000 (line 5)** 확인 (환산만 [E-1]).
2025년 Deloitte 호주가 고용·노동관계부(DEWR)에 납품, A$440,000. 카드 02 + 독립 교차(Accounting Times, Yahoo/AP, Fortune, Business Standard). **교차 충분.** 발주 부처·금액 일치.

**[C-5] Deloitte — 237쪽 (line 5)** 확인.
카드 02 "237쪽 분량" + 보도 교차 일치.

**[C-6] Deloitte — 가짜 학술 인용·존재하지 않는 전문가·날조 판례 인용 (line 5)** 확인.
시드니대 Chris Rudge 박사 적발. 가짜 학술 인용, 존재하지 않는 전문가, 연방판결문에 귀속된 날조 인용(판사명 오기 포함), 가공 판례 — 본문 서술과 독립 출처(Accounting Times, Business Standard) 일치. **교차 충분.**

**[C-7] Deloitte — 생성형 AI 사용 인정 + 수정본 재제출 + 대금 일부 환불 (line 5)** 확인.
Azure OpenAI GPT-4o 사용 인정, 수정본 제출, 최종 분납분 환불. 본문은 카드 02 수위 권고대로 "**대금 일부를 환불**"로 정확 금액 단정을 회피 — 양호. 독립 출처(Yahoo/AP "partially refund", "final instalment") 일치. **교차 충분.**

**[C-8] Deloitte — 핵심 결론·분석은 유지 (line 5)** 확인.
"보고서의 핵심 결론과 분석 자체는 유지됐다"는 본문은 정부 측 입장("the 'substance' of the report had been maintained ... no changes to its recommendations", Yahoo/AP)과 일치. 카드 02 반대근거 ①을 정확히 반영. 양호.

**[C-9] Air Canada 챗봇 (line 59)** 확인 (재활용).
ch02 카드 05(Moffatt v. Air Canada) 재활용. 본문은 "가짜 할인 규정의 책임이 항공사에 남은" 각도로 사용 — 카드 02/ch02 재활용 지침의 "AI 출력=조직의 책임" 프레이밍과 정합. 양호.

> 참고: Chevy $1 사례(카드 03)는 본문에 미사용. 카드 03 메모의 "곁가지, 깊이 다루지 말 것" 지침을 작가가 따른 결과로 판단. 문제 없음.

### 연구·수치

**[C-10] Stanford 법률 AI 환각 — 출처 기반 전용 도구도 무시 못 할 비율 환각 (line 61)** 확인.
Stanford RegLab/HAI, 2024년 202개 질의 평가. Lexis+ AI 17% 이상, Westlaw 34% 이상. 공급사 "환각 없음" 광고. 본문은 **구체 숫자(17/34%)를 본문에 적지 않고** "무시할 수 없는 비율"로 서술 — 카드 04가 권고한 "숫자 단정 회피·정의 논쟁 명시" 수위를 정확히 채택. line 61에 "2024년" 평가 시점, "법률 도메인이라 마케팅에 일반화 불가", "환각 정의 논쟁" 단서까지 모두 병기. **카드 한정 완벽 준수.** 독립 교차(LawSites, RegLab, eDiscoveryLLC) 일치. **교차 충분.**

**[C-11] Apple GSM-Symbolic — 최대 65%, 2024년 모델 (line 47)** 확인.
Apple, 2024-10. 무관한(그럴듯한) 절을 한 줄 추가 시 최첨단 모델 전반 정확도 최대 65% 하락(GSM-NoOp/added-clause 결과). 본문은 "**최대 65%**(상한값)", "**2024년 모델 기준**", "'LLM은 추론 못 한다'는 강한 결론에 반박 많음"을 모두 병기 — 카드 09 한정 완벽 준수. 독립 교차(MarkTechPost, Apple ML Research, arXiv/ICLR2025) 일치. **교차 충분.**
> 참고: "머릿속 계산 vs 외부 도구" 단서(line 49)도 카드 09 반대근거 ②와 정합. 양호.

**[C-12] OpenAI "Why LMs Hallucinate" 요지 (line 29)** 확인.
OpenAI, 2025년(정확히는 2025-09-05) 발표. "모른다 인정보다 그럴듯하게 찍는 것을 더 보상" → 시험 최적화로 자신 있게 지어냄. 본문 요지가 원논문 핵심 주장과 일치. 본문은 "2025년에 낸 연구"로만 표기(월 미명시) — 안전. "모델 제조사 본인 것이라 자사 책임을 학습 관행으로 돌리는 측면" 단서(line 29)는 카드 07 반대근거 ①을 반영. 독립 교차(arXiv:2509.04664, OpenAI, Medium 해설) 일치. **교차 충분.**

**[C-13] 유창성→과의존 메커니즘 (line 29, 31, 75)** 확인.
"유창하고 자신 있고 표면적으로 그럴듯한 출력이 검증을 단념시켜 과의존을 부른다" — 카드 07 교차 서베이(arXiv:2510.06265) 문구와 정합. "유창함은 진위와 무관하다"(line 31)는 카드 07 반대근거 ②의 정확 명제를 그대로 채택. 양호.

**[C-14] GPT-5 사실오류 감소 — 줄었으나 사라지지 않음 (line 73, 75)** 확인.
GPT-5 시스템 카드(2025-08-13). 추론 모드 GPT-5가 사실성 벤치마크(LongFact/FActScore)에서 직전 모델 대비 약 6배 적은 환각, 웹검색 시 사실오류 확률 대폭 감소. 본문 line 73은 숫자 없이 "사실 오류가 크게 줄었다"로 서술하고 "제조사 자체 발표·이해상충·측정 시점" 단서 병기. line 75는 "**5~6배 줄어도 0이 아닌 한**", "잔여 환각률 보고", "책임은 사람에게"로 카드 10 한정("줄었다≠없어졌다", 상대비교, 이해상충)을 완벽 준수. 독립 교차(implicator.ai, PMC12701941) 일치. **교차 충분.**
> [휘발성 점검] 카드 10은 "휘발성 강함 — 후속 모델 가능"을 경고. 검색 중 GPT-5.2 시스템 카드, GPT-5.4(2026) 자료 확인됨 = 더 신형 모델 존재. 그러나 본문은 GPT-5를 "2025년 8월" 시점 사례로 명시적으로 못박아 인용하므로(역사적 사실로 고정) 갱신 의무 없음. line 73 "측정 시점도 못 박아야 하지만"이라는 자기방어 문장이 휘발성을 정면 처리. 양호 — 다만 작가가 최신성을 강화하려면 "2025년 8월 GPT-5 기준"임을 한 번 더 못박는 선택지 있음(필수 아님).

### automation bias / 거버넌스

**[C-15] automation bias — Skitka·Mosier 원연구, 1990년대 정립 (line 33)** 확인.
Skitka, Mosier, Burdick (1999, IJHCS). 본문 "1990년대에 정립" 정확. 누락 오류(omission)·실행 오류(commission) 2분법(line 33)이 카드 08 정의와 일치. **교차 충분**(ScienceDirect, Wikipedia, CSET).

**[C-16] automation bias 해독제 — 교차검증 자료 근접·책임 명확화 (line 37, 51, 110)** 확인.
"교차검증할 자료가 손닿는 곳에 있을 때 오류 최소", "책임을 명확히 진 사람에게서 편향 감소" — 카드 08 반대근거 ②(처방 근거 전환)와 정확히 일치. 양호.

**[C-17] EU AI Act 14조 — 자동화 편향 인지 의무 (line 33)** 확인 (재활용).
ch02 카드 10 재활용. "14조는 고위험 AI 감독자가 자동화 편향을 인지하고 있어야 한다고 법문에 적었다" — 카드 06/ch02 카드 10과 정합. 본문은 "고위험 AI"에 한정해 마케터 직접규제로 오인되지 않게 처리(카드 06 반대근거 반영). 양호.

**[C-18] NIST AI RMF — 위험기반 차등 감독, 자발적 권고 (line 15)** 확인.
NIST AI RMF, 사람 감독을 핵심 기대사항으로 두되 위험 높을수록 사람 최종 승인·낮으면 주기 검토. 본문은 "표준 기구가 권하는 **모범관행이지 마케터에게 강제되는 규제는 아니다**"(line 15)로 카드 05 반대근거(자발적 프레임워크)를 정확히 명시. 카드 05 + 독립 해설 정합. **교차 충분.**

**[C-19] Anthropic human-in-the-loop / 체크포인트 권고** — 본문 직접 인용 없음. ch01 카드 09는 배경 토대로만 기능, 본문에 사실 주장으로 등장하지 않음. 검증 대상 외.

### 반대 근거 / 균형

**[C-20] AI 검수가 사람보다 나은 영역 — 방사선 좌우혼동 등 전사 오류 탐지 (line 19)** 확인.
"의료 영상 판독에서 미세조정된 모델이 좌우 혼동 같은 특정 전사 오류 탐지를 향상" — 카드 11(Radiology 게재, MedicalXpress) 정합. 본문은 한 문장으로 절제 사용. 양호.
> 주의: 카드 11의 "과잉일반화 5배" 수치는 미확인 목록 항목인데, **본문에 미유입 확인**(line 19는 방사선 사례만 사용). 작가가 미확인 수치를 배제함. 양호.

**[C-21] 자기 출력 자기 검수 금지 (line 21)** 확인.
"같은 모델은 같은 환각을 다시 통과시킨다 → 다른 도구 교차/원본 대조" — 카드 11 메모 단서와 정합. 사실 주장이라기보다 원리 설명이나, 카드 04(전용 도구도 환각)·카드 07(같은 학습편향)과 논리적으로 부합. 양호.

### 절차·고유명사

**[C-22] 기관·인명 표기** 확인.
- "미국 국립표준기술연구소(NIST)" — 정확.
- "AI 위험관리 프레임워크(AI RMF)" — 정확.
- "스키트카(Skitka)와 모지어(Mosier)" — 원어 철자 정확(Skitka, Mosier). 한글 음역 "스키트카/모지어" 무난.
- "미국 뉴욕남부연방지방법원" (line 27) — S.D.N.Y. 정확.
- "고용·노동관계부" (line 5) — DEWR(Department of Employment and Workplace Relations) 정확.
- "OpenAI", "Deloitte", "Air Canada" — 정확.

**[C-23] 절차 설명 — AI 검수 분업/원본 옆창 대조 (line 19, 51)** 확인.
"기계적 점검은 AI 1차 / 고위험은 사람"·"원본 시트를 같은 화면 옆에 띄운다"는 재현 가능한 실무 절차이며 특정 UI·버전에 의존하지 않음. AI 활용법 재현성 기준 충족. 양호.

**[C-24] 미확인 목록 — 국내 사례** 본문 유입 0건. 해외 사례(Mata/Deloitte/Air Canada)로만 충당. 양호.

**[C-25] 미확인 목록 — 과잉일반화 5배** 본문 유입 0건 ([C-20] 참조). 양호.

**[C-26] 미확인 목록 — 검수 평균시간 통계** 본문 유입 0건.
"40분"은 통계가 아니라 페르소나(김지유)·1장 약속의 서사 장치로만 사용(line 19, 112). 정량 통계로 제시되지 않음 — 카드 미확인 목록 지침("페르소나/실측으로만 서술") 준수. 양호.

**[C-27] 미확인 목록 — 원문 직접인용 문구** 본문에 원문 직접 인용 따옴표 사용 없음. 모든 연구는 요지 서술(간접)로 처리되어 글자단위 대조 대상이 없음. 따옴표 인용은 가상 인물(팀장·김지유) 대사뿐. 양호.

---

## [휘발성] 항목 재확인 결과 (2026-06-13)

| 항목 | 카드 휘발성 | 재확인 | 판정 |
|---|---|---|---|
| 원화 환산(AUD/KRW) | (교정 회부) | 1 AUD≈1,080원 | **오류 [E-1]** |
| Stanford 17/34% | 휘발성(2024 도구) | 본문 숫자 미기재·시점 병기 | 확인 |
| Apple 65% | 휘발성(2024 모델) | "상한값·2024 기준" 병기 | 확인 |
| GPT-5 감소 | 휘발성 강함 | 본문이 2025-08 시점 고정 | 확인 |
| NIST RMF | 휘발성 약함 | 본체 안정, "자발적" 명시 | 확인 |
| EU AI Act 14조 | 휘발성(2026-08 적용) | 본문 영향 없음 | 확인 |

---

## 결론

원고는 자료카드의 한정(수위 조절)을 거의 모범적으로 반영했고, 미확인 4건을 전부 배제했으며, 휘발성 수치 5건에 시점·단서를 병기했다. 사실 주장 차원의 오류·불확실은 0건이다.

**유일한 결함은 환율 환산 산수 1건([E-1])**으로, 사실(A$440,000)은 맞으나 원화 어림셈이 7% 어긋났다. AI 활용법 장르의 휘발성 처리 기준상으로도 정정이 필요하다.

- **게이트: 불통과 (오류 1건).**
- [E-1] 정정안 1안("약 4억 7,000만 원, 2026년 6월 환율 기준") 또는 2안(원화 환산 제거, "약 29만 달러" 병기) 적용 후 재확인하면 **오류 0 + [확인필요] 0** 달성으로 통과 가능.

---

### 출처 (이번 재확인에 사용한 독립 출처)

- [Mata v. Avianca $5,000 제재 — LegalClarity](https://legalclarity.org/what-happened-in-the-mata-v-avianca-case/)
- [Mata 제재 — Seyfarth Shaw](https://www.seyfarth.com/news-insights/update-on-the-chatgpt-case-counsel-who-submitted-fake-cases-are-sanctioned.html)
- [Deloitte 호주 환불 — Accounting Times](https://www.accountingtimes.com.au/technology/deloitte-to-refund-government-after-using-ai-in-440k-report)
- [Deloitte 부분 환불·substance 유지 — Yahoo/AP](https://www.yahoo.com/news/articles/deloitte-partially-refund-australian-government-070855665.html)
- [Stanford 법률 AI 17%/34% — LawSites](https://www.lawnext.com/2024/05/stanford-will-augment-its-study-finding-that-ai-legal-research-tools-hallucinate-in-17-of-queries-as-some-raise-questions-about-the-results.html)
- [Apple GSM-Symbolic 65% — MarkTechPost](https://www.marktechpost.com/2024/10/13/apple-researchers-introduce-gsm-symbolic-a-novel-machine-learning-benchmark-with-multiple-variants-designed-to-provide-deeper-insights-into-the-mathematical-reasoning-abilities-of-llms/)
- [GPT-5 시스템 카드 사실성 — implicator.ai](https://www.implicator.ai/gpt-5-cuts-claim-errors-to-9-6-with-browsing-system-card-shows/)
- [Why Language Models Hallucinate — arXiv:2509.04664](https://arxiv.org/abs/2509.04664)
- [AUD/KRW 2026 환율 이력 — exchange-rates.org](https://www.exchange-rates.org/exchange-rate-history/aud-krw-2026)
