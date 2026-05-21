# ArchiTinder · Frontend Design Decisions

> 이 문서는 `DESIGN.md`(기존 디자인 시스템 가이드)를 기반으로,
> ArchiTinder 프론트엔드에서 **확정해야 하는 의사결정 항목**을 정리한 작업용 체크리스트입니다.
> 결정이 끝나면 각 항목 옆에 ✅를 표시하고, 최종 결과를 `design.md`로 옮깁니다.

---

## 후보가 좁혀진 항목

| 항목 | 후보 |
|---|---|
| **Color Theme** | GitHub Light · Ayu Light · GitHub Dark · SynthWave '84 |
| **Font** | IBM Plex Sans KR · Noto Serif KR |

> 위 후보들은 본 작업의 시작점입니다. 한 가지를 디폴트로 픽스할지, 사용자가 전환 가능하게 둘지도 함께 결정해야 합니다.

---

## 1. Core Philosophy (DESIGN.md §0)

- [x] **Aesthetics tone** → **Mode별 톤 분리** ✅
  - Light 테마: Clear · Editorial · Content-first (이미지 가리지 않는 절제된 배경 + sharp typography)
  - Dark 테마: Cinematic · Atmospheric · Dramatic (깊은 배경 + 풍부한 contrast + glow/neon)
  - 두 모드 공통 분모: "premium, refined, confident"
  - DESIGN.md의 "cinematic dark only" 원안 폐기 — Light가 default이므로 Light 톤도 정식 정의
- [x] **Vibe 키워드 유지 여부** → **3개 모두 채택, gesture-friendly는 일부만** ✅
  - **Glassmorphic ✅** — 헤더/입력바 등에 backdrop blur 적용
  - **Fluid ✅** — 카드/버튼 hover 시 부드러운 lift + 트랜지션
  - **Gesture-friendly ✅ (부분)** — Discovery 카드의 swipe 힌트만 유지, **액션 버튼 강조 링은 제외**
  - 5001 디폴트가 3개 모두 ON 상태
- [x] **Implementation 규칙** → **CSS variables + Inline 하이브리드 공식화** ✅
  - CSS variables 담당: 테마화 가능한 값 (color, font, spacing, motion, radius 토큰)
  - Inline 담당: one-off 레이아웃, 동적 계산값, 강조 그라데이션
  - 금지: Tailwind, Bootstrap, MUI, Chakra, styled-components, emotion 등 외부 UI/CSS-in-JS 라이브러리
  - 허용: 순수 CSS 파일 (tokens.css §10.2) + CSS Modules
  - 이유: 토큰 수정으로 전체 일관 변경 + 런타임 오버헤드 0 + 번들 사이즈 최소

## 2. Color Palette (DESIGN.md §1)

- [x] **디폴트 테마 1개 결정** → **GitHub Light** ✅
  - 배경 #FFFFFF · 강조색 #0969DA / #8250DF / #953800
  - 라이트 모드를 기본으로 하되, 사용자가 자유롭게 전환 가능하도록 함
- [x] **테마 전환 UX** → **엔드 유저에게 노출, 배경색 + 강조색 칩 형태** ✅
  - [x] **노출 위치** → **Profile 탭 → Settings 섹션 → Appearance** ✅
    - 헤더/사이드바 메인 UI를 어지럽히지 않음 (테마는 자주 바꾸는 설정 아님)
    - 모바일/데스크탑 동일 위치
  - [x] **영속성** → **사용자 계정 (크로스 디바이스)** ✅
    - 로그인 사용자: 서버 측 user preference로 저장 → 다른 기기에서도 동일 테마 자동 적용
    - 비로그인 사용자: 세션 동안만 적용 (다음 방문 시 디폴트로 복귀)
    - `prefers-color-scheme` 자동 전환은 §7에서 별도로 "대응 안 함" 확정
- [x] **Accent 운영 정책** → **테마화 (CSS 변수)** ✅
  - 각 테마마다 accent-1/2/3 세 단계 보유
  - 사용자가 테마 전환 시 accent도 함께 변경 (브랜드 일관성보다 사용자 자유도 우선)
  - DESIGN.md의 인라인 하드코딩 규칙은 폐기, CSS 변수로 통일
  - 결정 필요: (a) 테마에 따라 accent 변경 (현재 데모 방식) / (b) accent는 핑크 고정, 배경/표면만 테마화 / (c) 두 가지 분리 (`theme-color`와 `brand-accent`)
- [x] **Destructive/Skip 색상** → **테마화 (라이트/다크별 알맞은 빨강 톤)** ✅
  - GitHub Light: `#D73A49` / Ayu Light: `#E5524B` / GitHub Dark: `#F85149` / SynthWave: `#FF6188`
- [x] **Border 투명도 톤** → **현재 설정 유지 (라이트 0.08 / 다크 0.07)** ✅
- [x] **Text 위계 색상** → **4단계 유지** ✅
  - text (제목) / text-2 (강조 본문) / text-muted (보조) / text-dim (비활성·메타)

## 3. Typography (DESIGN.md §3.3, §3.8)

- [x] **본문 폰트** → **IBM Plex Sans KR** (디폴트) ✅
  - Noto Serif KR과 토글 가능 (엔드 유저용 Font 버튼)
  - 토글 버튼의 라벨 "Font"는 *전환될* 폰트로 렌더링되어 미리보기 역할
- [x] **이중 폰트 운영 여부** → **단일 폰트만 (페어링 금지)** ✅
  - 헤딩/본문/캡션 모두 동일 family 사용 — 위계는 size + weight + 자간·여백으로만
  - Font 토글(§6)은 전체 시스템 동시 전환 — 부분 전환 없음
  - Editorial pairing (Serif heading + Sans body) 의도적 배제 → 멘탈 모델 단순화 + 사용자 토글 일관성
- [x] **Font-weight 상한 700 유지** ✅ (DESIGN.md §3.8 그대로)
- [x] **Type Scale 확정** → **환경별 분리 (Desktop / Mobile 각 4단계)** ✅
  - Desktop: H1 48 / H2 30 / Body 18 / Caption 14
  - Mobile: H1 32 / H2 24 / Body 16 / Caption 13
  - Weight는 환경 공통: H1 700 / H2 600 / Body 400 / Caption 500
- [x] **Line-clamp 정책** → **카드 타이틀에만 적용 (DESIGN.md §3.3 그대로)** ✅
  - 다른 컴포넌트는 자연스러운 줄바꿈 허용

## 4. Layout & Spacing (DESIGN.md §2)

- [x] **반응형 전략** → **Mobile-first + 데스크탑 전용 재레이아웃** ✅
  - 모바일: 하단 nav bar, 페이지 좌우 16px padding
  - 데스크탑: 220px 좌측 사이드바 nav, 컨텐츠 max-width 1200px
  - 브레이크포인트: TBD (768px 또는 1024px 권장)
- [x] **TabBar 높이** → **조건부** ✅
  - 아이콘 + 키워드: **64px** (현재 디폴트)
  - 아이콘만: **56px**
  - 개발 시 라벨 제거 결정하면 56으로 변경
- [x] **iOS Safe Area** → **하단 TabBar/CTA가 있는 곳에만 적용** ✅
  - `env(safe-area-inset-bottom)`을 모든 컨테이너에 일괄 적용하지 않고, 하단 고정 요소에만 사용
- [x] **Border Radius 스케일** → **4단계 토큰화** ✅
  - `--radius-sm: 8` / `--radius-md: 12` / `--radius-lg: 20` / `--radius-xl: 24` / `--radius-pill: 999`
- [x] **터치 타겟** → **디바이스별 분리** ✅
  - 모바일: **44px** (Apple HIG)
  - 데스크탑: **32px+** (마우스 정밀도 활용)

## 5. Component Library (DESIGN.md §3)

### 5.1 Buttons (§3.1)
- [x] **Primary CTA 그라데이션** → **테마 accent 그라데이션** (`linear-gradient(135deg, var(--accent-1), var(--accent-2))`) ✅
  - 테마 전환 시 그라데이션도 함께 변경
  - 적용 위치: Persona "View persona report", Discovery ♥(Save), AI Search chat send ↑
- [x] **버튼 variants** ✅
  - **Secondary** → Surface 채움 + border (Discovery ✕ 패턴)
    `bg: var(--surface) · border: 1px solid var(--border) · color: var(--text)`
  - **Ghost** → Transparent + border (Persona Share 패턴)
    `bg: transparent · border: 1px solid var(--border) · color: var(--text)`
  - **Destructive** → Transparent + destructive border + destructive text
    `bg: transparent · border: 1px solid var(--destructive) · color: var(--destructive)`

### 5.2 Inputs (§3.2)
- [x] **Glassmorphic 효과** → **유지** (Vibe 결정의 일부) ✅
  - `backdrop-filter: blur(12px)` + `background: color-mix(in srgb, var(--surface) 72%, transparent)`
- [x] **Focus state** → **3단계 (default → focus → click moment)** ✅
  - Default: `1px solid var(--border)` (회색)
  - Focused (`:focus-within`): `1px solid var(--accent-1)` — 색만 변경, glow 없음
  - Click moment (`:has(.chat-input:active)`): + `box-shadow: 0 0 0 4px color-mix(var(--accent-1) 28%, transparent)` glow가 클릭 순간 즉시 표시 → 0.4s 동안 페이드 아웃 (Primary CTA와 동일 타이밍)

### 5.3 Card System (§3.5) — DESIGN.md에서 가장 큰 섹션
- [x] **카드 변형 채택** → **3.5.2 + 3.5.4 + 3.5.5 변형 조합** ✅
  - **Front face** = project main image + text hierarchy pattern
    - title + architects(sub-italic) + divider + **3-col info grid (YEAR + LOCATION + PROGRAM)**
    - (DESIGN.md §3.5.2의 2-col → 3-col로 확장)
  - **Back face** = 3D rotateY로 뒤집은 후 sub-image 가로 스크롤 갤러리
    - scroll-snap, 좌우 chevron 화살표, 하단 "View Gallery · N photos" 액션
  - **제외**: 3.5.1 단순 오버레이 (front가 이를 포함), 3.5.3 코너 칩 (사용처 없음)
- [x] **Hover 효과 정책** → **효과 없음** ✅
  - Discovery는 스와이프 중심 UX → hover는 자연스러운 인터랙션이 아님
  - 카드 액션은 클릭(flip) · 스와이프 · Like/Skip 버튼으로만 수행
  - DESIGN.md의 `translateY(-4px) + 핑크 보더` 패턴은 폐기
- [x] **Card aspect ratio** → **4:5 portrait** ✅
  - Tinder 가로 비율과 유사, 텍스트 계층(title/architects/info grid)에 충분한 세로 여유
  - 모바일: 화면 채움(flex:1) / 데스크탑: 명시적 `aspect-ratio: 4 / 5`
- [x] **Border 규칙** → **Border 없음 (radius + shadow만)** ✅
  - `radius-lg` + `box-shadow: 0 12px 32px rgba(0,0,0,0.3)`로 카드 경계 표현
  - 배경 이미지/그라데이션과 충돌 회피
- [x] **텍스트 가독성 처리** → **하단 검정 그래디언트 fade (front/back 동일)** ✅
  - Front: `.discovery-face.front::before` linear-gradient(180deg, transparent 30%, rgba(0,0,0,0.82))
  - Back: `.back-action` linear-gradient(to top, rgba(0,0,0,0.96) → transparent)
  - "View Gallery · N photos"도 텍스트이므로 button pill bg 제거, 그래디언트 위 직접 표기
  - 8개 대안 비교(A1~A3 text-shadow/stroke, B1 glassmorphic, B2 solid scrim, B3 gradient, C1 chips, C2 poster, D1 blend-mode) 후 그래디언트가 가장 적절 — 사진을 가리지 않으며 가독성 확실

### 5.4 Profile Action Row (§3.6)
- [ ] **Instagram 패턴 채택 여부** — Follow / Following 토글
- [ ] **Message 버튼** — 보조 액션으로 같이 둘지

### 5.5 Stats Row (§3.7)
- [ ] **Compact 스타일 (18px 숫자, 1px 디바이더) 채택**

### 5.6 Folder Card (Boards canonical)
- [x] **구조** → **상단 슬랜트 탭 (accent-1) + 바디 (surface-2)** ✅
  - 탭 SVG path로 우측 슬랜트 모서리, 탭 라벨 우측 28% 패딩으로 슬랜트 회피
  - 긴 제목은 JS 이진 탐색으로 prefix + `⋯` (U+22EF midline), 짧은 제목은 전체 표시
  - 토큰/세부 사양은 design.md §8.7
- [x] **Hover 효과** → **lift `translateY(-3px)` + 1px accent-1 outline, no shadow/glow** ✅
  - outline은 4방향 stacked `drop-shadow(1px 0 0 var(--accent-1))` 등으로 구현 (탭 슬랜트 모서리까지 따라감 — CSS `outline`은 사각형이라 불가)
  - 디폴트/호버 모두 underneath drop-shadow 없음 (평면 디자인)
  - `box-shadow` 미사용

## 6. Interaction Patterns (DESIGN.md §4)

- [x] **Desktop 키보드 조작 + 입력 방식 통합** ✅
  - Skip: `ArrowLeft` OR 마우스 좌 드래그 OR ✕ 버튼
  - Like: `ArrowRight` OR 마우스 우 드래그 OR ♥ 버튼
  - Flip: `Enter` OR 사진 클릭
  - 드래그 임계값: 카드 폭 25% 초과 시 swipe 확정, 미달은 spring back
  - Discovery 화면 활성 시에만 단축키 리스너 바인딩
- [x] **Hover 색 변경 방식** → **CSS `:hover` 의사 클래스만** ✅
  - 인라인 `onMouseEnter/Leave` + React state 패턴은 폐기
  - 이유: 성능(rerender 회피) + 단순성 + SSR 친화적
- [x] **Skeleton Loader 정책** → **§8.8 Loading State에서 결정됨** ✅ (이 항목은 §7과 중복)
- [x] **모션 토큰** → **Duration 4 + Easing 2 토큰화** ✅
  - Duration: `motion-fast 180ms` (hover/focus/chip) · `motion-normal 220ms` (transforms/lifts) · `motion-slow 400ms` (glow fade) · `motion-flip 500ms` (3D 카드 flip)
  - Easing: `motion-ease cubic-bezier(0.4, 0, 0.2, 1)` (Material standard) · `motion-ease-out cubic-bezier(0, 0, 0.2, 1)` (decelerate)
  - Click moment의 `0s`는 토큰화하지 않음 — "즉시"는 timing이 아닌 intent
  - 전 transition에서 var(--motion-*) 사용. 인라인 ms/cubic-bezier 하드코딩 금지 (design.md §3.5)

## 7. 신규 결정 (DESIGN.md에 없지만 필요)

- [x] **로딩 상태 디자인** → **Skeleton + Spinner 조합** ✅
  - 카드/리스트 골격 = Skeleton (radius + 회색 블록), 버튼/짧은 액션 = Inline spinner
  - Shimmer 애니메이션은 채택하지 않음 (성능 부담, Vibe 키워드와 무관)
- [x] **에러 상태 디자인** → **3-tier 패턴** ✅
  - Empty 컴포넌트 (데이터 없음) / Inline Error (컴포넌트 실패) / Toast (액션 실패)
  - Catastrophic full-screen 에러 안 만듦 — 항상 컴포넌트 단위 격리
- [x] **모달/시트 디자인** → **환경별 자동 선택** ✅
  - 모바일: Bottom Sheet (swipe-up, gesture-friendly Vibe와 일치)
  - 데스크탑: Centered Modal
- [x] **Toast 알림** → **bottom-center · 3s · glassmorphic** ✅
  - 모바일 nav 위로 띄움 (`calc(--tabbar-height + 16px)` 오프셋)
  - Glassmorphic 스타일 (Vibe ✅과 일치)
  - 타입별 border-color로 info/success/warning/error 구분
- [x] **다국어 폰트 백업 스택** → **Web → OS Korean → system-ui** ✅
  - Sans: IBM Plex Sans KR → Noto Sans KR → Apple SD Gothic Neo → Malgun Gothic → 맑은 고딕 → system-ui
  - Serif: Noto Serif KR → 본명조 → Nanum Myeongjo → 나눔명조 → AppleMyungjo → Batang → 바탕 → Georgia
  - 한글 이름 병기 (영문 매치 안 될 때를 위한 backup)
  - catalog.py의 IBM_PLEX/NOTO_SERIF 상수 및 design.md §2.1 `font-stack` / `font-stack-serif` 토큰에 반영
- [x] **다크/라이트 자동 전환** → **대응 안 함** ✅
  - 시스템 설정 무시, 사용자가 명시적으로 선택한 테마만 적용
  - 단순하고 예측 가능한 동작 우선

## 8. 코드 구조 / 작업 방식

- [x] **DESIGN.md vs design.md** → **design.md 단일 소스** ✅
  - design.md = single source of truth. DESIGN.md는 archive 처리 (역사 참조용)
  - 새 결정/변경은 design.md에만 추가, DESIGN.md 편집 금지
- [x] **디자인 토큰 위치** → **tokens.css 전용 파일 분리** ✅
  - :root의 CSS variables를 tokens.css에 모음
  - 컴포넌트 스타일과 분리 (관심사 분리)
- [x] **테마/폰트 추가 절차** → **catalog 수정 + design.md 업데이트 + PR 디자인 검토** ✅
  - 1) catalog.py / tokens.ts 수정 → 2) design.md 표·yaml 동기화 → 3) PR + 미리보기 → 4) reviewer 승인 후 머지
  - 자유 추가 금지 — 일관성/품질 관리
- [x] **컴포넌트 격리 정책** → **2+ 페이지 사용 시 추출 (디자인 시스템 입도는 무조건)** ✅
  - 추출 기준: 2+ 페이지 사용 / 50줄 초과 / 디자인 시스템 입도
  - inline 유지: 단일 페이지 짧은 코드 / 1회성 / 페이지 컴포지션

---

## 결정 순서 제안

1. **§1 디폴트 테마** + **§3 본문 폰트** (가장 먼저 픽스 — 다른 결정의 토대)
2. **§1 Accent 운영 정책** (인라인 vs CSS 변수 — 코드 작업 방향 결정)
3. **§4 반응형 전략** (이후 컴포넌트 설계의 기준)
4. **§5 카드 시스템** (앱의 시각적 정체성을 좌우)
5. **§6 인터랙션 패턴**
6. **§7 신규 항목 + §8 운영**

---

## 참고 도구

- Theme/Font 비교: http://127.0.0.1:5000/ (Flask 익스플로러)
- 실제 앱 적용 데모: http://localhost:5173/ (archithon-app, 우측 하단 🎨 버튼)
