# ch06 자료카드: 분석·보고서 초안·발표 슬라이드 생성 — 슬라이드 자동화 도구 · 계산 위임의 근거 · "AI는 해석, 계산은 도구"

- 담당: researcher / 작성일: 2026-06-13
- 대응 브리프: `books/ai-for-marketers/briefs/ch06.md` 자료카드 섹션 4개(AI 슬라이드/문서→슬라이드 도구 / LLM 계산 신뢰성·도구 위임 / "AI는 해석, 계산은 도구" 분업 / "4시간→40분" 통계 부재 재확인)
- 일러두기: 도구·버전·가격은 모두 [휘발성] + 확인일 2026-06-13. 집필 시점(집필 직전)에 공식 가격/기능 페이지에서 재확인할 것. AI 슬라이드 도구는 분기 단위로 플랜·가격이 바뀐다.
- 출처 접근 메모: ch04 조사와 동일하게 이번에도 arxiv.org(2211.10435, 2410.03524), proceedings.mlr.press, cs.cmu.edu PDF가 HTTP 403을 반환했다. 해당 1차 논문 건(PAL, CodeSteer)은 WebSearch 결과 요약 + 복수 출처(MLR proceedings 메타, EmergentMind, 공식 프로젝트 페이지, 기술 매체)로 교차 확정했고, 각 카드에 "집필 전 원문 PDF 재확인 필요"를 명시했다. 도구 카드의 기능·플랜은 공식 지원 문서(Microsoft Support, Google Docs Editors Help, Workspace Blog) + Gamma 공식 가격 정보로 1차 확정.

---

## 기존 카드 재사용 평가 (브리프 지시)

**ch04 카드 09 (Apple GSM-Symbolic — LLM 산술이 표면 패턴에 의존, 무관 정보 추가 시 정확도 최대 65% 하락) → ch06 재활용 가능. 본 장 핵심 처방의 "문제 진단" 절반.**

근거: ch04 카드 09는 메모와 반대 근거 항목에서 이미 6장을 두 번 가리킨다 — ① 반대 근거 ②번에 "이 연구는 모델이 머릿속(텍스트 생성)으로 계산할 때의 결과다. 코드 인터프리터/계산기 도구를 호출하면 산술 정확도는 크게 올라간다 → 6장 처방과 정합", ② 메모 실무 함의 ⓐ "계산 자체를 LLM의 텍스트 생성에 맡기지 말고 스프레드시트/코드 인터프리터로(6장 연결)". 즉 카드 09는 **"왜 AI에게 암산을 시키면 안 되는가"(문제)**의 1차 근거로 ch06에서 그대로 재활용한다. **중복 조사 불필요 — ch04 카드 09 인용.**

단 역할 분담: 카드 09는 "문제"(AI 텍스트 계산은 신뢰 못 함)까지만 받친다. ch06의 처방은 거기서 한 걸음 더 나간다 — **"그럼 계산을 어디에 맡기면 정확해지는가"(해결)**. 이 "해결" 측 1차 근거가 ch04에는 없으므로 본 파일 카드 04(PAL)·카드 05(CodeSteer)로 새로 확보했다. 본 장 논증: **AI에게 암산시키면 틀린다(카드 09) → 계산을 결정적 도구[시트 수식/코드 실행]에 떠넘기면 정확도가 오른다(카드 04·05) → 그러니 시트가 계산하고 AI는 그 숫자를 해석·서술만 한다(카드 06 처방 + 페르소나 번역).**

→ 결론: 본 파일은 ch06 고유의 **① 슬라이드 자동화 도구 실명·버전·한계(카드 01~03) ② 계산 위임이 정확도를 높인다는 1차 근거(카드 04·05) ③ "AI는 해석, 계산은 도구" 분업 권고(카드 06) ④ AI 슬라이드 품질 한계 = 반대 근거(카드 07) ⑤ "4시간→40분" 통계 부재 재확인(미확인 목록)**에 집중했다. ch04 카드 09는 인용으로 끌어온다.

---

## ① AI 슬라이드 생성 / 문서→슬라이드 자동 변환 도구 (2026년 6월)

---

## 카드 01: Microsoft 365 Copilot은 워드 문서로부터 PowerPoint 발표본 초안을 만들고, 회사 표준 템플릿/브랜드를 적용할 수 있다 [휘발성]

- **주장:** Microsoft 365 Copilot in PowerPoint는 워드(.docx) 문서를 입력으로 받아 슬라이드 초안(이미지·발표자 노트 포함)을 자동 생성한다. PowerPoint에서 새 빈 문서를 열고 리본의 Copilot → "Create presentation from file"을 선택해 워드 파일을 지정하는 노코드 경로다. 워드에서 제목/본문 스타일(Styles)로 문서를 구조화해 두면 Copilot이 슬라이드 분할을 더 잘한다. 회사 표준은 두 방식으로 반영된다 — ① 조직의 **샘플 슬라이드(기존 덱)**를 우선 참조하고 회사 템플릿의 구조·레이아웃을 보조로 사용, ② **브랜드 키트(Brand kit)** 설정 시 브랜드 보이스·톤·스타일·이미지를 적용. 단 (집필 확인일 기준) 이 "파일로부터 생성" 기능은 워드 파일만 지원하며 다른 파일 형식 지원과 Agent Mode의 파일 참조는 "곧 지원 예정"으로 표기돼 있다. 2026년 4월 Copilot의 에이전트 기능(Word·Excel·PowerPoint)이 정식 출시(GA)됐다.
- **출처:** Microsoft Support, "Create a new presentation with Copilot in PowerPoint" (https://support.microsoft.com/en-us/office/create-a-new-presentation-with-copilot-in-powerpoint-3222ee03-f5a4-4d27-8642-9c387ab4854d); Microsoft Support, "Keep your presentation on-brand with Copilot" (https://support.microsoft.com/en-us/topic/keep-your-presentation-on-brand-with-copilot-046c23d5-012e-49e0-8579-fe49302959fc); Microsoft Tech Community, "Create a PowerPoint slide from a file with Microsoft Copilot" (https://techcommunity.microsoft.com/blog/microsoft365insiderblog/create-a-powerpoint-slide-from-a-file-with-microsoft-copilot/4405839); Microsoft 365 Blog (2026-04-22), "Copilot's agentic capabilities in Word, Excel, and PowerPoint are generally available" (https://www.microsoft.com/en-us/microsoft-365/blog/2026/04/22/copilots-agentic-capabilities-in-word-excel-and-powerpoint-are-generally-available/)
- **출처 등급:** 1차(Microsoft 공식 지원 문서 + 공식 블로그). 공식 문서 직접 접근 가능, 별도 403 없음.
- **확인일:** 2026-06-13
- **휘발성:** [휘발성] 강함 — 기능 범위("워드만 지원, 나머지는 곧")·Agent Mode·브랜드 키트 동작이 빠르게 바뀐다. 라이선스(Microsoft 365 Copilot 유료 추가)도 변동. 집필 직전 위 지원 문서에서 현재 지원 파일 형식·템플릿 적용 방식 재확인 필수.
- **반대 근거:** 본 장 한계 카드 07 참조(AI 슬라이드는 일반적으로 디자인이 generic해지고 브랜드 가이드와 어긋난다 — Copilot도 예외 아님). 또한 ① Copilot은 별도 **유료 라이선스**가 필요해 "ChatGPT 유료 구독 중"인 페르소나가 회사 M365 환경에서 Copilot을 못 쓸 수 있다(회사 IT 정책 의존) — "회사가 M365 Copilot을 켜준 경우의 경로"로 조건부 서술. ② "샘플 슬라이드/템플릿 참조"는 결과 품질이 입력 덱 품질에 의존 — 좋은 표준 덱이 있어야 좋게 나온다.
- **인용 방식 제안:** 절차(노코드 경로)는 공식 문서대로 직접 인용 가능 / 단계는 본문 재현. 단 "워드만 지원" 등 제약은 확인일 명시.
- **메모:** **김지유 환경에 가장 "회사 표준 템플릿"에 가까운 경로.** 브리프 4번 "회사 표준 템플릿 위에 슬라이드가 채워지는 노코드 경로"의 1순위 후보. 단 페르소나가 회사 M365 Copilot 라이선스를 가졌는지가 분기점 — 가졌으면 Copilot, 못 가졌으면 Gamma(카드 03)/Gemini(카드 02)/수동. 보고서 명세(브리프 2번)의 출력을 워드 초안으로 받은 뒤 이 경로로 PPT화하는 흐름이 자연스럽다. **재현성 주의(ai-howto): 집필 시 실제로 워드 초안 → Copilot PPT 변환을 한 번 돌려 실제 출력·소요·한계를 본문에 수록.**

---

## 카드 02: Google Workspace의 Gemini는 Google Slides에서 "슬라이드 만들기"로 프롬프트/Workspace 데이터로부터 덱을 생성한다 [휘발성]

- **주장:** Google Workspace의 Gemini는 Google Slides에서 슬라이드를 자동 생성한다. 도구 모음/삽입 메뉴/슬라이드 메뉴의 "Help me create a slide"(슬라이드 만들기)로 접근하며, "create a five-slide deck summarizing our Q1 results" 같은 프롬프트를 주면 테마에 맞춰 불릿·시각요소가 있는 덱을 만든다. Gemini는 사용자의 Workspace 데이터(문서·시트 등)를 활용해 "온브랜드" 발표본을 만들고, 생성 후에도 프롬프트나 수동 편집으로 완전히 수정 가능하다. 디자인·서식·메시징은 Gemini가 맡고 사용자는 내용(스토리)에 집중하도록 설계됐으며, 기존 슬라이드 스타일에 맞춰 위계·여백·시각 비중을 조정한다고 안내한다. 2026년 3월 Google이 Docs·Sheets·Slides·Drive에 Gemini 기능을 확대 롤아웃했다. 이 기능은 적격 Google Workspace 또는 Google AI 플랜이 필요하다.
- **출처:** Google Docs Editors Help, "Collaborate with Gemini in Google Slides" (https://support.google.com/docs/answer/14355071); Google Workspace Blog, "Gemini update reimagines content creation for business users" (https://workspace.google.com/blog/product-announcements/reimagining-content-creation); TechCrunch (2026-03-10), "Google rolls out new Gemini capabilities to Docs, Sheets, Slides, and Drive" (https://techcrunch.com/2026/03/10/google-rolls-out-new-gemini-capabilities-to-docs-sheets-slides-and-drive/)
- **출처 등급:** 1차(Google 공식 Help/Blog) + 2차(TechCrunch 교차, 롤아웃 시점). 공식 페이지 접근 가능.
- **확인일:** 2026-06-13
- **휘발성:** [휘발성] 강함 — 기능명·메뉴 위치·필요 플랜이 변동. "Workspace Experiments" 단계 기능이 섞여 있어 가용성이 계정마다 다를 수 있음. 집필 직전 Help 문서로 현재 메뉴 경로·필요 플랜 재확인.
- **반대 근거:** 카드 07(AI 슬라이드 일반 한계) 적용. 또한 ① Google Slides는 회사가 PowerPoint 표준이면 형식 불일치(독자의 "회사 표준 템플릿"이 .pptx일 때) — Slides→PPTX 내보내기 시 레이아웃 깨짐 가능. ② Workspace/AI 플랜 라이선스 필요 — 무료 Gmail 계정에서는 제한.
- **인용 방식 제안:** 절차는 공식 Help대로 / "디자인은 Gemini, 스토리는 사람"이라는 설계 철학은 본 장 "AI는 형식, 사람은 내용·검수" 프레임과 정합해 한 줄 인용 가치.
- **메모:** **회사가 Google Workspace를 쓰는 페르소나의 경로.** Copilot(MS 환경)과 대칭. 보고서 명세 출력을 구글 문서/시트에 두고 Gemini로 슬라이드화하면 카드 01과 같은 "데이터→문서→슬라이드" 흐름. 단 김지유는 광고 데이터를 엑셀/시트로 다룬다(5장) — 회사 생산성 스택(MS냐 Google이냐)에 따라 카드 01/02 중 택일하도록 분기 박스 권장. **재현성: 집필 시 실제 1회 생성해 출력·한계 수록.**

---

## 카드 03: Gamma는 주제·개요·소스 파일로부터 약 90초 만에 덱을 생성하며, 무료 플랜 + 유료 티어에서 커스텀 테마/브랜드 적용을 제공한다 [휘발성]

- **주장:** Gamma는 주제·개요·소스 파일을 입력하면 약 90초 안에 발표 덱(또는 문서·웹페이지)을 생성하는 AI 도구다. 100개 이상 테마와 12종 이상 적응형 스마트 다이어그램(타임라인·피라미드·원형 등)을 제공하고, 자체 브랜드 테마를 가져올 수 있다. 가격(확인일 기준): 무료 플랜(1회성 AI 크레딧 약 400), Plus 월 $10(연결제 시 $8), Pro 월 $20(연 $15), Ultra 월 $100(연 $39). 팀 플랜은 좌석당 월 $20부터(최소 2석), Business는 좌석당 월 $40부터(최소 10석)로 공유 브랜드 키트·중앙 관리 포함. 커스텀 테마는 Pro·Ultra에서, 전체 브랜드 키트(로고·색·폰트 자동 적용)는 Ultra에서 제공.
- **출처:** Gamma 공식 가이드/탐색 페이지 (https://gamma.app/explore/content/guides/best-free-ai-presentation-makers-for-2026-create-slides-fast); 가격 정리(2차 교차): presentations.ai "Gamma Pricing 2026" (https://www.presentations.ai/blog/gamma-pricing), costbench.com Gamma 가격 (https://costbench.com/software/ai-presentations/gamma/)
- **출처 등급:** 1차(Gamma 공식) + 2차(가격 비교 매체 교차). **가격·플랜은 변동성이 매우 커서 집필 직전 Gamma 공식 가격 페이지(gamma.app/pricing)에서 직접 확정 필수 — 본 카드의 달러 수치는 확인일 스냅숏.**
- **확인일:** 2026-06-13
- **휘발성:** [휘발성] 매우 강함 — 가격·크레딧 정책·티어명이 분기마다 바뀐다. "월 $XX" 수치를 단정 인용하지 말고 "2026년 6월 확인 기준, 변동 가능" 단서 + 집필 시 재확인. 환율로 인한 원화 표기도 주의.
- **반대 근거:** ① 카드 07(AI 슬라이드 generic 한계) 정면 적용 — Gamma 특유의 룩이 있어 "Gamma로 만든 티"가 나며 회사 PowerPoint 표준 템플릿과 다른 별도 디자인 체계다(회사 표준 .pptx 위에 채우는 것과는 다름). ② 무료 플랜은 크레딧 소진형이라 "매주 보고서"엔 유료가 사실상 필요. ③ PPTX로 내보내도 회사 마스터 슬라이드와 정확히 일치하지 않을 수 있음(브랜드 키트로 근사할 뿐).
- **인용 방식 제안:** 기능은 직접 / 가격은 "확인일 기준, 변동" 단서 필수 + 수치만. 회사 표준 템플릿 일치도는 한계로 정직하게.
- **메모:** **회사가 M365/Google 어느 쪽도 AI를 안 켜준 페르소나의 독립 경로 + "빠르게 보기 좋은 초안"이 필요할 때.** 단 브리프 4번의 "회사 표준 템플릿 위에 채워지는"이라는 약속에는 카드 01(Copilot)이 더 정확하고, Gamma는 "별도 디자인 체계를 새로 입는" 쪽 — 이 차이를 본문에서 정직하게 구분할 것(독자가 회사 보고서 표준이 엄격하면 Gamma 결과를 다시 회사 템플릿에 옮겨야 할 수 있음). 비교축: Copilot/Gemini = 회사 표준 안에서, Gamma = 자체 디자인으로 빠르게.

---

## ② 계산을 도구에 위임하면 수치 정확도가 오른다 — 본 장 처방의 "해결" 측 1차 근거

---

## 카드 04: LLM은 추론을 맞게 해도 산술 계산 단계에서 틀린다 — 계산을 파이썬 인터프리터에 떠넘기면(PAL) GSM8K 정확도가 사고연쇄(CoT) 대비 절대 15%p 상승 (2023)

- **주장:** PAL(Program-aided Language Models) 연구는, LLM이 자연어 문제를 단계로 분해(추론)하는 데는 쓰되 **계산(해(解)를 구하는 단계)은 LLM의 텍스트 생성이 아니라 파이썬 인터프리터에 떠넘기는** 방식을 제안한다. 핵심 진단: LLM은 문제를 올바르게 분해하고도 풀이 부분에서 논리·산술 오류를 낸다("LLMs often make logical and arithmetic mistakes in the solution part even when the problem is decomposed correctly"). 계산을 결정적(deterministic) 런타임에 맡기면 정확도가 오른다 — Codex 기반 PAL은 수학 문장제 벤치마크 GSM8K에서 사고연쇄(chain-of-thought)를 쓰는 PaLM-540B를 **절대 15%p(top-1)** 능가했고, BIG-Bench Hard의 Object Counting에서 96.7% vs CoT 73.0%, Penguins in a Table에서 93.3% vs 79.2%를 기록했다.
- **출처:** Gao, L., Madaan, A., Zhou, S., Alon, U., Liu, P., Yang, Y., Callan, J., & Neubig, G. (2023). "PAL: Program-aided Language Models." ICML 2023(PMLR v202). 1차: arXiv:2211.10435 (https://arxiv.org/abs/2211.10435), PMLR (https://proceedings.mlr.press/v202/gao23f.html), CMU PDF (https://www.cs.cmu.edu/~callan/Papers/icml23-Luyu-Gao.pdf). 해설 교차: EmergentMind PAL 페이지 (https://www.emergentmind.com/papers/2211.10435)
- **출처 등급:** 1차(원 논문, ICML 동료심사). arXiv·PMLR·CMU PDF 모두 직접 접속 차단(403) — 수치(GSM8K +15%p, OC 96.7/73.0, Penguins 93.3/79.2)와 핵심 문장은 복수 출처(검색 요약 + EmergentMind 정리)로 교차 확인. **집필 전 PDF에서 정확 수치·인용 문장 확정 필요.**
- **확인일:** 2026-06-13
- **휘발성:** [휘발성] 약함 — 2022~2023년 모델(Codex/PaLM) 기준이라 절대 수치는 낡았다. 그러나 **원리("계산을 코드 실행에 떠넘기면 텍스트 산술보다 정확")는 시점 무관하게 유효**하고 후속 연구(카드 05)·도구(ChatGPT 코드 실행)가 같은 방향. 본문에는 "원리"로 인용하고 절대 수치는 "초기 연구 기준" 단서.
- **반대 근거:** ① 카드 05(CodeSteer) — 코드 실행이 항상 텍스트 추론보다 나은 건 아니다(쉬운/모호한 과제에선 텍스트가 나을 수 있고, 모델이 언제 코드를 쓸지 잘못 고르기도 한다). 따라서 "코드(계산 도구)에 맡기면 무조건 정확"으로 과장 금지. ② PAL은 LLM이 "코드를 쓰는" 방식 — 페르소나(코드 못 읽음)에겐 직접 적용 불가. 본 장 페르소나 번역은 "AI가 코드를 쓰게"가 아니라 "**계산은 시트 수식이 하고, AI는 그 숫자를 해석만**"(브리프 가드레일). 즉 PAL은 "계산은 결정적 도구에, 추론·서술은 LLM에"라는 **원리의 학술 근거**로만 쓰고, 실행 형태는 시트 수식으로 치환.
- **인용 방식 제안:** 원리 + 핵심 문장("추론이 맞아도 산술에서 틀린다") 짧은 직접 인용 / GSM8K 수치는 "초기 연구 기준" 단서 포함 수치만.
- **메모:** **본 장 핵심 처방의 "해결" 측 1차 근거 — ch04 카드 09(문제)와 짝.** 논증 완성: 카드 09 "AI 텍스트 계산은 신뢰 못 함" → 카드 04 "계산을 결정적 도구에 떠넘기면 정확도 오름" → 페르소나 처방 "증감률은 시트 수식이 계산, AI는 +23%라는 숫자의 의미만 해석·서술". **페르소나 번역 필수**: 코드/인터프리터 단어를 본문에 노출하지 말고 "AI에게 암산시키지 말고 시트가 계산하게 한다"로(브리프 스타일 유의). 김지유 버전: "전주 대비 증감률 칸은 엑셀 수식이 뽑은 값을 AI에 '읽어주고', AI는 그 값을 문장으로만 풀어 쓰게 한다."

---

## 카드 05: [균형/보강] 계산을 코드 실행에 맡길지 텍스트 추론에 맡길지는 과제·모델에 따라 다르다 — 둘 다 고려할 때 최고 성능 (2024)

- **주장:** "Steering LLMs between Code Execution and Textual Reasoning" 연구는, 수학·논리·최적화·탐색이 얽힌 과제에서 텍스트 추론에는 본질적 한계가 있어 **코드 실행이 유리**하다고 본다. 다만 코드가 항상 더 낫지는 않으며, 모델이 코드를 쓸지 텍스트로 풀지 잘못 고르는 경향이 있다(예: GPT-4o는 중간 난도 과제를 텍스트로 풀다 틀리고, GPT-3.5-turbo는 전 난도에서 코드를 더 자주 써 더 정확한 역(逆)스케일 현상). 결론적으로 **코드 결과와 텍스트 결과를 함께 고려할 때 최고 성능**이 나온다.
- **출처:** Chen, Y., Jhamtani, H., Sharma, S., Fan, C., & Wang, C. (2024). "Steering Large Language Models between Code Execution and Textual Reasoning." arXiv:2410.03524 (https://arxiv.org/abs/2410.03524); 프로젝트 페이지 CodeSteer (https://yongchao98.github.io/CodeSteer/); Microsoft Research 게재 (https://www.microsoft.com/en-us/research/publication/steering-large-language-models-between-code-execution-and-textual-reasoning/)
- **출처 등급:** 1차(arXiv + Microsoft Research). arXiv 403 — 핵심 논지는 검색 요약 + 프로젝트 페이지로 교차. **집필 전 원문 재확인 권장.**
- **확인일:** 2026-06-13
- **휘발성:** [휘발성] 약함 — 모델별(GPT-4o/3.5) 관찰은 버전 의존이나, "수치 과제엔 코드 실행이 유리, 단 자동 선택은 불완전"이라는 원리는 안정적.
- **반대 근거(이 카드 자체가 카드 04의 균형추):** "계산을 도구에 맡기면 무조건 좋다"는 단순화를 막는다. 함의: ① AI가 스스로 "언제 계산 도구를 쓸지" 판단을 못 미더워하므로 **사람이 명시적으로 "이 칸은 시트가 계산"이라고 분업을 고정**하는 게 안전(본 장 명세 설계와 정합 — 즉흥에 맡기지 말고 명세로). ② "코드와 텍스트를 함께 본다"는 본 장 "시트 계산값 + AI 해석을 사람이 대조"와 같은 방향.
- **인용 방식 제안:** 배경 지식 / 카드 04의 단서로. "도구에 맡기는 게 유리하되, 무엇을 어디에 맡길지는 사람이 명세로 고정한다"의 근거.
- **메모:** **카드 04를 "맹신"으로 읽히지 않게 하는 균형 + 명세 설계 정당화.** AI에게 "알아서 계산해"라고 두면 텍스트로 암산하다 틀릴 수 있다(GPT-4o 사례) → 그래서 본 장은 "증감 계산 = 시트 수식(고정), 해석·서술 = AI"로 **역할을 명세에 못 박는다**(3장 명세 회수). ch03 명세(입력·출력·판단·예외)에 "계산은 AI가 하지 않는다"를 예외 규칙으로 넣는 근거.

---

## ③ "AI는 해석·서술, 계산은 도구" 분업 권고

---

## 카드 06: 보고·분석 자동화의 모범 패턴은 "LLM은 의도 이해·서술, 계산·실행은 결정적 도구"의 분업이다

- **주장:** AI 분석·자동화 설계의 정착된 권고는 **LLM에게 잘하는 일(의도 이해, 문제 분해, 자연어 서술·해석)을 시키고, 못하는 일(정확한 산술·집계·결정적 실행)은 런타임/도구에 맡기는 역할 분담**이다. 단어 순서를 예측하는 것은 실제로 계산하는 것과 다르며, LLM은 단순 산술도 암기·패턴으로 맞히다가 낯설거나 복잡한 입력에서 무너진다. 그래서 값마다 LLM에 추론시키는 대신 집계·연산은 런타임(코드/스프레드시트)에서 일어나게 하고, LLM은 결과를 사람 말로 풀어 쓰게 한다. 업계(Anthropic의 도구사용·분석 도구 연구 등)는 모델에 코드 샌드박스/도구를 주면 복잡한 다단계 과제의 오류율이 낮아지고 완료율이 오른다고 보고한다.
- **출처:** TanStack Blog, "Code Mode: Let Your AI Write Programs, Not Just Call Tools" (https://tanstack.com/blog/tanstack-ai-code-mode); freeCodeCamp, "How to Make LLMs Better at Math Using AI Agents..." (https://www.freecodecamp.org/news/make-llms-better-at-math-with-ai-agents/) — 둘 다 PAL(카드 04)·도구사용 연구를 근거로 한 실무 정리. 1차 근거는 카드 04(PAL)·ch04 카드 09(GSM-Symbolic)로 연결.
- **출처 등급:** 2차(기술 블로그 — 실무 권고 정리). **권고의 1차 근거는 카드 04(PAL, ICML)·카드 05(CodeSteer)·ch04 카드 09(Apple). 본 카드는 "분업이 모범 패턴으로 통용된다"는 정황 근거이며, 단정 주장에는 1차 카드를 인용할 것.**
- **확인일:** 2026-06-13
- **휘발성:** [휘발성] 약함 — 도구/프레임워크명(Code Mode 등)은 변하나 분업 원리는 안정적.
- **반대 근거:** 검색했으나 "분업이 틀렸다"는 반대는 미발견. 단 수위 주의: ① 이 분업은 "AI는 계산을 절대 못 한다"가 아니라 "**정확성이 중요하면 계산을 결정적 도구로 검증·수행하라**"이다(추론 모델·코드 실행 켜면 산술도 개선 — ch04 카드 10 균형). ② 출처가 2차(블로그)라 본문 단정은 1차 카드로. ③ 마케터 페르소나에게 "코드/런타임/샌드박스"는 금지어 — "시트가 계산"으로 번역.
- **인용 방식 제안:** 배경 지식으로 / "단어를 예측하는 것과 계산하는 것은 다르다"는 짧은 직접 인용 가치(개념 설명용). 단정 수치·주장은 카드 04·09 인용.
- **메모:** **브리프 자료카드 3번(분업 권고)의 직답.** 본 장의 한 문장 처방 — "AI는 해석·서술, 계산은 도구" — 이 즉흥 조언이 아니라 PAL(카드 04)·CodeSteer(카드 05)·GSM-Symbolic(ch04 카드 09)로 받쳐지는 정착 패턴임을 보인다. **페르소나 번역(브리프 가드레일 핵심)**: "코드 인터프리터에 맡긴다" → "AI에게 암산시키지 말고 시트가 계산하게 한다". 독자는 코드를 쓰지 않고, 익숙한 엑셀/시트 수식이 PAL의 "결정적 런타임" 역할을 대신한다는 것이 본 장의 페르소나 적합 처방.

---

## ④ 반대 근거 — AI 슬라이드 자동생성의 품질 한계

---

## 카드 07: [반대 근거] AI 자동생성 슬라이드는 흔히 디자인이 generic·획일적이고 회사 브랜드 가이드와 어긋나, 사람의 검수·다듬기 없이는 회사 보고서 품질에 못 미친다

- **주장:** AI 슬라이드 생성 도구는 속도를 크게 줄였지만 품질을 보장하지 않는다. 대다수 AI 슬라이드 메이커는 고정 템플릿에 의존하고 공간 구성·시각적 깊이·타이포 위계 같은 고급 디자인 원칙을 "추론"하지 않아 결과가 깔끔하되 generic하게 나온다. 한 번에(one-shot) 전부 생성하는 방식이라 레이아웃을 비교·선택할 여지가 없고, 슬라이드를 독립 단위로 처리해 덱 전체의 시각적 서사가 일관되지 않는 경향이 있다. AI는 특정 브랜드 정체성이 아니라 일반적 "프로페셔널" 미감을 최적화하므로 회사 브랜드 가이드와 어긋나기 쉽고, 청중이 "AI로 뽑은 티"가 나는 획일적 템플릿을 알아보면 발표자의 신뢰도가 떨어질 수 있다. 결론: 전문가 수준 발표본에는 사람의 감독·커스터마이징이 여전히 필수다.
- **출처:** Beautiful.ai Blog, "AI Can Build Slides Fast—But Great Presentations Still Need Design Rules" (https://www.beautiful.ai/blog/ai-can-build-slides-fast--but-great-presentations-still-need-design-rules); WinningPresentations, "Why Your AI-Generated Slides Look Generic (And How to Fix It)" (https://winningpresentations.com/ai-generated-slides-look-generic/); Nuts & Bolts Speed Training, "Best AI Presentation Tools for PowerPoint: A Designer's 4-Tool Experiment & Review" (https://nutsandboltsspeedtraining.com/powerpoint-tutorials/best-ai-presentation-tools-for-powerpoint-a-designers-4-tool-experiment-review/)
- **출처 등급:** 2차/3차(디자인 전문 블로그·실사용 리뷰). **이해상충 주의: 출처 다수가 AI 슬라이드 도구나 디자인 서비스 제공사 블로그라 "사람/우리 도구가 필요하다"는 방향 편향이 있다.** 그럼에도 "generic·브랜드 불일치"라는 한계는 복수 독립 출처에서 일관 — 일반 경향으로는 신뢰. 정량 단정은 회피.
- **확인일:** 2026-06-13
- **휘발성:** [휘발성] 약함 — 도구가 개선되며 일부 완화될 수 있음(브랜드 키트 등, 카드 01~03). "현재 일반 경향"으로 서술하고 도구 개선 가능성 병기.
- **반대 근거(이 카드가 본 장 "PPT까지 자동" 약속의 반대 근거):** 균형용. 본 장 약속과 충돌하지 않게 정리 — 본 장은 "AI가 완성된 발표본을 만든다"가 아니라 "**검수·다듬기 가능한 초안**을 자동 생성한다(만들기→검수)"이다. 따라서 이 한계는 본 장 프레임("40분은 검수 시간")과 정합: 자동생성은 초안까지, 회사 표준 일치·디자인 마무리는 사람이 표적 보정. 카드 01(Copilot 회사 템플릿/브랜드 키트)·카드 02(Gemini 온브랜드)는 generic 문제를 일부 완화하는 경로로 함께 제시.
- **인용 방식 제안:** 배경 지식 + 한계의 정직한 명시(브리프 4번 "그 한계: 디자인 만족도·템플릿 제약" 직답). 정량 수치 없이 경향으로.
- **메모:** **브리프 4번이 명시 요구한 "한계(디자인 만족도·템플릿 제약)"의 근거 — 정직성 장치.** 본 장이 "버튼 한 번에 완벽한 PPT"라는 과장으로 읽히면 ai-howto 재현성·practical 정직성 위반. 처방: ① 자동생성은 "초안"으로 규정 ② 회사 표준 템플릿 적용은 Copilot/Gemini 브랜드 키트로 최대한 흡수하되 남는 보정은 사람 검수 40분에 포함 ③ "Gamma 티/AI 티"가 나는 부분은 회사 마스터로 옮기거나 핵심 슬라이드만 손보기. **재현성: 집필 시 실제 자동생성 출력의 한계(어디가 어긋났는지)를 캡처·서술해 정직하게.**

---

## ⑤ 참고: 마크다운→슬라이드 경로 (페르소나 부적합 — 분기 박스용 메모)

---

## 카드 08: [참고/한계] 마크다운→슬라이드(Marp 등) 경로는 재현성·버전관리에 강하나 CLI·코드 친화 도구라 본서 페르소나에는 부적합

- **주장:** 텍스트(마크다운)로 슬라이드를 작성해 PDF/PPTX/HTML로 변환하는 오픈소스 경로가 있다(대표: Marp — CLI 및 VS Code 확장). 단 Marp의 기본 PPTX 내보내기는 슬라이드를 "이미지 1장"으로 박아 편집 불가하다는 한계가 있다. 이를 보완한 MarpToPptx(.NET 10 기반, 2026-03 갱신)는 제목·불릿·표를 실제 편집 가능한 PowerPoint 도형으로 내보내고 mermaid/다이어그램도 렌더한다. 그러나 이들은 모두 CLI/개발 환경(VS Code, .NET) 설치·실행이 필요한 코드 친화 도구다.
- **출처:** Marp 공식 (https://marp.app/), marp-team/marp-cli (https://github.com/marp-team/marp-cli); MarpToPptx (https://github.com/jongalloway/MarpToPptx)
- **출처 등급:** 1차(공식 사이트/리포지토리).
- **확인일:** 2026-06-13
- **휘발성:** [휘발성] 약함 — 오픈소스 도구 상태는 비교적 안정적이나 버전(.NET 10 등) 의존.
- **반대 근거:** 본 카드 자체가 "이 경로는 본서에 안 맞는다"는 판정. 페르소나 김지유는 "Python이라는 단어를 보면 창을 닫는다"(기획안) — CLI·VS Code·.NET 설치는 가드레일 위반.
- **인용 방식 제안:** 사용하지 않음 또는 한 줄로만("코드를 다루는 사람을 위한 마크다운→슬라이드 경로도 있으나 본서 범위 밖"). 본문 절차로 넣지 말 것.
- **메모:** **브리프가 "마크다운→슬라이드"를 조사 대상에 넣었기에 평가는 했으나, 결론은 페르소나 부적합 = 본문 채택 불가.** 다만 "AI가 보고서를 '마크다운 텍스트'로 출력하게 한 뒤 그걸 슬라이드로 옮긴다"는 발상 자체는 유효 — 단 변환 도구는 Copilot/Gemini/Gamma(카드 01~03, 노코드)로. Marp류는 12장(도구 교체) 독자가 개발 친화로 성장했을 때의 선택지로만 한 줄 언급 가능. 본 장 기본 경로에서 제외.

---

---

## 미확인 목록

카드로 만들지 못한 주장. 작가는 이 항목을 본문에 쓸 수 없다 (쓰려면 [확인필요] 표시).

- **"보고서 작성 4시간 → 40분"(또는 분석·PPT 정리 과업의 구체적 절감 수치)의 공개 통계** — 못 찾은 이유: 존재하지 않음(ch01·ch02 미확인 목록과 동일 결론 재확인). 시장 조사들은 "AI가 마케터의 주당 약 6.1시간 / 11시간 / 13시간을 절감" 등 **AI 사용 전반의 주간 절감**을 보고하나(coschedule State of AI in Marketing 2025, Salesforce 등), ① 수치가 6~13시간으로 제각각이고 ② 2025-11 조사에선 영미권 AI 사용 직원의 68%가 주 4시간 이하 절감 ③ **"주간 광고 성과 보고서의 취합+분석+PPT 정리"라는 특정 과업의 비포/애프터를 측정한 값은 없다.** 따라서 "4시간→40분"의 유일한 근거 경로는 기획안 과업 D(베타 리더 실측, PPT 정리 시간 포함). 본 장은 이 수치를 단정하지 말고 "목표" 또는 [확인필요: 과업 D 실측]으로 표기(브리프 5번 지시). AI 전반 절감 통계는 "AI가 시간을 아껴준다"는 일반 정황으로만, 본서 특정 수치의 근거로는 사용 불가.
  - (참고 출처: coschedule.com/ai-marketing-statistics, salesforce.com/news/stories/generative-ai-statistics/, emarketer.com "Most employees using AI are saving less than half a workday per week" — 모두 본서 특정 약속의 근거로는 부적합.)
- **국내(한국) 회사·마케팅 맥락의 AI 슬라이드 도구 회사 표준 템플릿 적용 사례/제약** — 못 찾은 이유: 한국 기업 표준 .pptx 마스터에 Copilot/Gemini 브랜드 키트가 얼마나 정확히 맞는지의 공개 실측 미발견. 집필 시 작가가 실제 회사 템플릿으로 1회 변환해 본 결과(재현성)로 보완 권장 — 통계가 아닌 실측 서술로.
- **AI 슬라이드 자동생성의 "디자인 만족도"를 정량화한 독립 조사(만족도 %, 재작업률 등)** — 못 찾은 이유: 신뢰할 정량 조사 미발견. 카드 07의 한계는 **경향**으로만 서술 가능(정량 단정 불가). 작가는 "디자인이 generic해질 수 있다"까지만, "N%가 불만족" 식 수치는 쓰지 말 것.
