# ArchiTinder Design System

> 이 파일은 ArchiTinder 프론트엔드 디자인 시스템의 **단일 진실 소스(single source of truth)**입니다.
> `python design_preview.py`로 서버를 띄우면 http://127.0.0.1:5001/ 에서 이 파일이 정의하는 디자인이
> 실제 화면에 적용된 모습을 실시간으로 확인할 수 있습니다.
>
> ⚠️ 아래 `yaml` 코드 블록의 키/값은 자동으로 파싱됩니다. 들여쓰기와 따옴표를 유지하세요.

---

## 용어 (Glossary)

이 문서에서 사용하는 **디자인 시스템 용어**와 **사용자가 화면에서 보게 될 라벨** 간 매핑.
용어가 헷갈리거나 코드에서 무엇을 찾아야 할지 모를 때 이 표를 우선 참조.

| 사용자 용어 (UI 라벨) | 디자인 시스템 용어 (코드/문서) | 정의 위치 |
|---|---|---|
| **보드 (Board)** | Folder Card | §8.7 |
| **프로젝트 (Project)** | Project Card | §8.6 |

> 새 용어 매핑이 생기면 위 표에 한 줄 추가. 명세는 해당 § 섹션에서 관리.

---

## 1. Color Tokens

**디폴트 테마: GitHub Light** ✅
사용자는 테마 스위처로 자유롭게 변경 가능 (§5 참고).

### 1.1 Surface & Text
```yaml
bg:         "#FFFFFF"
surface:    "#F6F8FA"
surface-2:  "#EFF2F5"
surface-3:  "#E1E4E8"
text:       "#1F2328"
text-2:     "#24292F"
text-muted: "#656D76"
text-dim:   "#8C959F"
border:     "rgba(0,0,0,0.08)"
border-soft: "rgba(0,0,0,0.12)"
```

### 1.2 Accent (테마화 ✅)
```yaml
accent-1:   "#0969DA"
accent-2:   "#8250DF"
accent-3:   "#953800"
```

### 1.3 Destructive / Skip (테마화 ✅)
**라이트/다크별로 어울리는 빨강 톤을 별도 정의.**
현재(GitHub Light 디폴트):
```yaml
destructive: "#D73A49"
```
다른 테마 적용 시(예시, 테마 스위처가 동시 변경):
- Ayu Light → `#E5524B`
- GitHub Dark → `#F85149`
- SynthWave '84 → `#FF6188`

---

## 2. Typography

**디폴트 본문 폰트: IBM Plex Sans KR** ✅
사용자는 Font 토글 버튼으로 Noto Serif KR과 전환 가능 (§6 참고).

### 2.1 Font Family
```yaml
font-family:        "IBM Plex Sans KR"
font-stack:         '"IBM Plex Sans KR", "Noto Sans KR", "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", system-ui, -apple-system, BlinkMacSystemFont, sans-serif'
font-stack-serif:   '"Noto Serif KR", "본명조", "Nanum Myeongjo", "나눔명조", "AppleMyungjo", "Batang", "바탕", Georgia, serif'
```

**Fallback 정책 ✅** — 한글 글리프 가용성을 환경별로 보장
1. **Primary**: web 폰트 (Google Fonts에서 로드)
2. **Web fallback**: Noto Sans KR (Sans) / Nanum Myeongjo (Serif) — 더 빠르게 캐시되어 있을 가능성
3. **macOS / iOS**: Apple SD Gothic Neo (Sans) / AppleMyungjo (Serif)
4. **Windows**: Malgun Gothic / 맑은 고딕 (Sans) / Batang / 바탕 (Serif)
5. **최후**: `system-ui` / `Georgia` / `sans-serif` / `serif`

한글 이름(`맑은 고딕`, `본명조` 등)은 OS Locale에 따라 영문 이름이 매치 안 될 때를 위해 병기.

### 2.2 Type Scale — Desktop (≥ 769px)
```yaml
h1-size-desktop:      48
h2-size-desktop:      30
body-size-desktop:    18
caption-size-desktop: 14
```

### 2.3 Type Scale — Mobile (≤ 768px)
```yaml
h1-size-mobile:      32
h2-size-mobile:      24
body-size-mobile:    16
caption-size-mobile: 13
```

### 2.4 Weights (환경 공통)
```yaml
h1-weight:      700
h2-weight:      600
body-weight:    400
caption-weight: 500
```

### 2.5 Font-weight 규율
**최대 700.** 800/900 금지. (DESIGN.md §3.8 유지 ✅)
"premium, sleek, confident" 톤은 굵기가 아닌 자간·여백·팔레트로 표현.

### 2.5a 단일 폰트 정책 ✅
- **헤딩/본문/캡션 모두 동일 family 사용** (이중 폰트 운영 금지)
- 위계는 size + weight + 자간·여백으로만 표현
- Font 토글(§6)은 전체 시스템 동시 전환 — 부분 전환 없음
- Editorial Serif heading + Sans body 같은 페어링은 의도적으로 배제 → 멘탈 모델 단순화, 사용자 토글 일관성 보장

### 2.6 (Legacy aliases — 점진적 마이그레이션)
```yaml
h1-size:      48   # → h1-size-desktop
h2-size:      30   # → h2-size-desktop
body-size:    18   # → body-size-desktop
caption-size: 14   # → caption-size-desktop
```

---

## 3. Layout & Shape

### 3.1 Border Radius Scale (토큰화) ✅
```yaml
radius-sm:   8     # 작은 칩, 인풋
radius-md:   12    # 버튼, 작은 카드
radius-lg:   20    # 카드 디폴트
radius-xl:   24    # 큰 카드, 모달
radius-pill: 999   # pill 모양
```

### 3.2 Touch Target (디바이스별)
```yaml
touch-target-mobile:  44    # Apple HIG 권장
touch-target-desktop: 32    # 마우스 정밀도 활용
```

### 3.3 TabBar Height (조건부)
```yaml
tabbar-height-with-label: 64    # 아이콘 + 키워드 (현재 디폴트)
tabbar-height-icon-only:  56    # 아이콘만
tabbar-height:            64    # 현재 사용 중인 값
```
> ⚠️ 개발 시 nav 라벨을 제거하면 `tabbar-height`를 56으로 변경할 것.

### 3.4 (Legacy aliases — 점진적 마이그레이션)
```yaml
radius-card:    20   # → radius-lg
radius-button:  12   # → radius-md
```

### 3.5 Motion Tokens ✅
모든 transition은 아래 토큰만 사용. 인라인 ms/cubic-bezier 하드코딩 금지.

**Duration (4단계)**
```yaml
motion-fast:    180ms   # micro: hover, focus border, chip toggle, filter
motion-normal:  220ms   # standard: transforms, lifts (가장 자주 사용)
motion-slow:    400ms   # fade-outs: glow dispersion, color shift
motion-flip:    500ms   # heavy: Discovery 카드 3D rotateY flip
```

**Easing (2개)**
```yaml
motion-ease:     cubic-bezier(0.4, 0, 0.2, 1)   # 대부분의 transform/lift (Material standard)
motion-ease-out: cubic-bezier(0, 0, 0.2, 1)     # decelerate fade (glow 사라짐 등)
```

**Click moment 예외**
glow 등 click 순간 즉시 표시(0초)는 토큰 없이 `0s` 리터럴 유지 — "즉시"는 timing이 아닌 의도(intent).

**사용 예시**
```css
.button       { transition: transform var(--motion-normal) var(--motion-ease); }
.input        { transition: border-color var(--motion-fast),
                            box-shadow   var(--motion-slow) var(--motion-ease-out); }
.input:active { transition: box-shadow 0s; }   /* click moment — instant */
.card-flip    { transition: transform var(--motion-flip) var(--motion-ease); }
```

---

## 4. 디자인 철학

- **Aesthetics ✅ — Mode별 톤 분리**
  - **Light 테마** (GitHub Light · Ayu Light): **Clear · Editorial · Content-first**
    건축 이미지를 가리지 않는 절제된 배경, 명료한 텍스트 위계, sharp typography.
    절제된 shadow + 일관된 surface = 잡지·아카이브의 톤.
  - **Dark 테마** (GitHub Dark · SynthWave '84): **Cinematic · Atmospheric · Dramatic**
    이미지가 빛나도록 깊은 배경, 풍부한 contrast, glow/neon accent 활용.
    Deeper shadows + atmospheric gradients = 영화·갤러리 야경의 톤.
  - 두 톤 모두 "premium, refined, confident"라는 공통 분모는 유지. Mode 차이는 contrast와 분위기에서 표현.
- **Vibe ✅**: `glassmorphic` · `fluid` · `gesture-friendly (swipe hint only)` 모두 채택.
  - Glassmorphic: 헤더·입력바·gallery hint 등에 `backdrop-filter: blur(12px)` 적용
  - Fluid: 카드/버튼 hover 시 `translateY(-3px)` + 0.22s 트랜지션
  - Gesture-friendly: Discovery 카드 상단에 "← swipe ✕ · swipe ♥ →" 힌트 표시 (액션 버튼 자체는 강조 없음)
- **Implementation ✅ — CSS variables + Inline 하이브리드**
  - **CSS variables 담당**: 테마화 가능한 값 — color, font, spacing 토큰, motion 토큰, radius 등 (§3.5 motion, §1 color 참조)
  - **Inline 스타일 담당**: 고정/한차원 값 — one-off 레이아웃, 동적 계산값, 강조 그라데이션
  - **금지**: Tailwind, Bootstrap, MUI, Chakra, styled-components, emotion 등 외부 UI/CSS-in-JS 라이브러리
  - **허용**: 순수 CSS 파일 (tokens.css §10.2 참조), CSS Modules
  - 이유: 토큰 수정으로 전체 일관 변경 가능 + 런타임 오버헤드 없음 + 번들 사이즈 최소
- **Hover 구현 ✅**: 색·그림자·transform 등 시각 전환은 **CSS `:hover` 의사 클래스만** 사용. 인라인 `onMouseEnter/Leave` + React state 패턴은 폐기 — 성능/단순성 우선.
- **Theme 전환**: 사용자 명시 선택만 반영. `prefers-color-scheme` 자동 전환 대응 안 함.
- **Line-clamp**: 카드 타이틀에만 2줄 적용. 다른 텍스트는 자연 줄바꿈 허용.

---

## 5. Theme Switcher (엔드 유저용)

ArchiTinder는 **사용자가 자유롭게 색상 테마를 선택할 수 있는 기능**을 제공합니다.

### 5.1 노출 방식
- 테마 선택 버튼은 **배경색 + 강조색**으로 구성된 칩(chip) 형태
- 각 칩은 해당 테마의 배경색 + 강조색을 시각적으로 미리 보여줌
- 클릭 시 즉시 전환 (페이지 리로드 없음)

### 5.2 칩 사양 (예시)

```yaml
chip-bg-preview-size:    20    # 배경색 미리보기 원의 지름 (px)
chip-accent-preview-size: 12   # 강조색 미리보기 원의 지름 (px, 배경 위에 겹침)
chip-padding:            "6px 14px"
chip-radius:             999
```

### 5.3 후보 테마
현재 후보 (DECISIONS.md §2):
- **GitHub Light** ← 디폴트
- Ayu Light
- GitHub Dark
- SynthWave '84

### 5.4 노출 위치 ✅
- **Profile 탭 → Settings 섹션 → Appearance** 내부에 노출
- 헤더/사이드바 등 메인 UI는 어지럽히지 않음 (테마는 자주 바꾸는 설정이 아님)
- 모바일/데스크탑 동일 위치 (Profile 안의 Settings)

### 5.5 영속성 ✅
- **사용자 계정에 저장 (크로스 디바이스)**
- 로그인 사용자: 서버 측 user preference로 저장 → 다른 기기에서도 동일 테마 자동 적용
- 비로그인 사용자: 세션 동안만 적용 (다음 방문 시 디폴트 GitHub Light로 복귀)
- `prefers-color-scheme` 자동 전환 안 함 (§7에서 확정)

### 5.6 라벨/Copy
- 섹션 제목: **"Appearance"**
- 하위 항목: **"Theme"** (테마 칩 리스트), **"Font"** (§6 폰트 토글과 동일 위치)

---

## 6. Font Switcher (엔드 유저용)

ArchiTinder는 본문 폰트도 사용자가 전환할 수 있습니다.

### 6.1 토글 버튼 — "버튼 라벨 자체가 전환될 폰트의 미리보기"
- 버튼 라벨: 항상 **`Font`** 한 단어
- 버튼 라벨의 **font-family는 *현재가 아닌 다른* 폰트**로 렌더링
  → 클릭하면 어떤 폰트로 바뀔지 라벨이 직접 보여줌
- 클릭 시 두 폰트 간 토글

### 6.2 상태 머신

| 현재 본문 폰트 | 버튼 라벨 | 버튼 라벨의 font-family |
|---|---|---|
| IBM Plex Sans KR (디폴트) | `Font` | Noto Serif KR (전환될 폰트) |
| Noto Serif KR | `Font` | IBM Plex Sans KR (전환될 폰트) |

### 6.3 후보 폰트
- **IBM Plex Sans KR** ← 디폴트 (기하학적 산세리프, 테크니컬)
- Noto Serif KR (고전적 명조, 에디토리얼)

### 6.4 노출 위치 ✅
**§5.4와 동일** — Profile → Settings → Appearance 안에 Theme 칩과 같은 자리.
구체적으로는 §5.6 라벨 정의: "Font" 항목으로 Theme 바로 아래 배치.

---

## 7. Responsive Layout

ArchiTinder는 모바일 우선이지만 데스크탑에서도 자연스럽게 동작해야 합니다.

### 7.1 모바일 (≤ 768px)
- 하단 고정 nav bar (Search · Discover · Boards · Profile, 4 column grid)
- 페이지 좌우 padding 16px
- 카드 그리드: 2 column
- iOS Safe Area 대응 (`padding-bottom: env(safe-area-inset-bottom)`)

### 7.2 데스크탑 (≥ 769px)
- 좌측 220px 고정 사이드바 nav (세로 배열, 아이콘 + 라벨)
- 메인 컨텐츠 영역: 가로 스크롤 없음, max-width 1200px
- 카드 그리드: 3 column
- 페이지 좌우 padding 32px

### 7.3 브레이크포인트
```yaml
breakpoint-mobile-max: 768   # ≤ 768px → 모바일 레이아웃
breakpoint-desktop-min: 769  # ≥ 769px → 데스크탑 레이아웃
```

### 7.4 Mobile Safari UX 디테일 ✅
모바일(특히 iOS Safari)에서만 발생하는 5가지 큰 함정과 그 해결책. 모든 모바일 모듈에 일률 적용.

#### 7.4.1 입력 포커스 시 자동 줌인 방지 (iOS)
iOS Safari는 **font-size가 16px 미만인 input/textarea/select에 포커스되면 화면을 자동 확대**한다. 이후 사용자가 확대 해제를 해야 하고, 폼 작성 중에는 거의 항상 발생해서 매우 거슬리는 동작.

```yaml
input-min-font-size-mobile: 16    # 미만이면 iOS Safari가 강제 zoom-in
```

규칙:
- 모든 `<input>` `<textarea>` `<select>`는 모바일에서 **`font-size: 16` 이상** 보장
- 컴포넌트 인라인 스타일 + `index.css`의 global rule 양쪽에 적용 (둘 중 하나만 두면 깜빡임 또는 누락)
  ```css
  /* index.css 전역 */
  input, textarea, select { font-size: 16px; }
  ```
- 이 16px는 위계가 아니라 **iOS 동작 보호선** — 데스크탑에서도 같이 16px여도 무방

#### 7.4.2 키보드가 열린 다음 새 입력칸을 스크롤로 노출 (visualViewport)
"+ 항목 추가" 같은 액션이 리스트 맨 아래에 새 input을 만들고 자동 포커스 → 키보드가 뜨면서 그 input을 가린다. 단순 `requestAnimationFrame + scrollIntoView`는 키보드가 viewport를 줄이기 *전*에 실행되어 결국 가려진 상태로 멈춤.

해결: **키보드가 viewport를 줄이는 `visualViewport.resize` 이벤트를 기다린 후** `scrollIntoView({block: 'center'})`. 400ms fallback timer로 데스크탑/이벤트 없는 환경 보호.

```yaml
keyboard-reveal-fallback-ms: 400   # visualViewport resize가 안 오면 강제 scrollIntoView
keyboard-reveal-block: "center"    # 키보드 위 가운데에 입력칸 위치
```

원칙:
- 동적으로 추가된 input이 viewport 밖에 있으면 **항상 visualViewport 패턴으로 노출**
- block은 `center` (`start`/`end`는 키보드 상단/하단에 붙어버려 사용자가 컨텍스트 잃음)
- listener는 한 번 발화 후 제거 (메모리/중복 호출 방지)

#### 7.4.3 오버스크롤 영역 배경 통일 (`<meta name="theme-color">` + `background-attachment: fixed`)
iOS Safari에서 페이지를 위/아래 끝을 넘어 바운스하면, 페이지 컨테이너 뒤의 영역이 노출된다. 다크 테마에서 그 영역이 흰색으로 보이는 게 큰 문제.

해결:
1. **`<meta name="theme-color">`** 를 현재 테마의 `bg`로 동적 갱신 → iOS Safari 상단/하단 바운스 영역의 톤이 테마 배경과 일치
2. `html`에 `background: var(--color-bg); background-attachment: fixed;` → 문서 자체가 스크롤되더라도 오버스크롤 영역이 테마 색으로 채움
3. **inner overflow scroll 컨테이너를 만들지 않는다** — document가 스크롤되어야 iOS의 pull-to-refresh와 sticky header가 자연스럽게 동작

```html
<!-- index.html -->
<meta name="theme-color" content="#FFFFFF" />   <!-- 초기값; JS가 테마 적용 시 갱신 -->
```
```js
// themes.js applyTheme(id)
function setMetaThemeColor(hex) {
  let meta = document.querySelector('meta[name="theme-color"]')
  if (!meta) { meta = document.createElement('meta'); meta.setAttribute('name', 'theme-color'); document.head.appendChild(meta) }
  meta.setAttribute('content', hex)
}
```
```css
/* index.css */
html, body { background: var(--color-bg); background-attachment: fixed; min-height: 100%; }
[data-theme="github-dark"]  { color-scheme: dark; }
[data-theme="synthwave"]    { color-scheme: dark; }
```

> ⚠️ inner scroll 컨테이너(`overflow: auto` 안쪽 div)로 처리하면 pull-to-refresh가 사라지고 sticky header가 컨테이너 안쪽에 갇힌다. 반드시 document 스크롤 유지.

#### 7.4.4 모바일 네이티브 카메라/갤러리 picker
파일 선택 input에 `accept="image/*"`만 붙이면 iOS/Android 모두 **카메라·갤러리 둘 다 선택할 수 있는 네이티브 시트**를 띄운다. 별도 라이브러리/권한 요청 코드 없음 — OS가 권한 알림도 자동 처리.

```html
<input type="file" accept="image/*" style="display:none" />
<button onClick={() => fileRef.current?.click()}>사진 변경</button>
```
- 데스크탑에서는 파일 picker가 뜸 (자연 fallback)
- 선택된 이미지는 클라이언트에서 **256×256 정사각 JPEG로 리사이즈**한 뒤 저장/업로드 — localStorage/서버 둘 다 페이로드 작게 유지
- 같은 파일을 다시 고르려면 `e.target.value = ''`로 input 리셋

#### 7.4.5 모바일 단일 컬럼 셸 (mobile-only 모듈)
`archibe-profile`처럼 **모바일 전용으로 디자인되는 모듈**은 데스크탑 레이아웃을 별도로 만들지 않고 단일 셸로 처리:

```yaml
mobile-only-shell-max-width: 460   # 모바일 폼팩터 기준
mobile-only-shell-margin:    "0 auto"
mobile-only-shell-bg:        "var(--color-bg)"
```
- 셸을 `max-width: 460px; margin: 0 auto`로 두면 데스크탑 브라우저에서는 가운데 정렬된 모바일 폭으로 보임 — 별도 레이아웃 없이도 깨지지 않음
- 향후 데스크탑 전용 레이아웃이 정해지면 그때 분리

---

## 8. Components

### 8.1 Primary CTA Button ✅
주요 액션 버튼 (가입/공유/구매 같은 핵심 CTA).

```css
background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
color: #fff;
border: 0;
border-radius: calc(var(--radius-md) * 1px);
padding: 14-16px;
font-weight: 600;
min-height: 44px;
transition: transform 0.22s, background-color 0.22s, box-shadow 0.4s ease-out;
```

**Click moment (`:active`) — glow shadow** ✅
Input focus 패턴(§8.5)과 동일하게, 클릭 순간 즉시 glow가 표시되고 0.4s에 걸쳐 페이드 아웃.

```css
.primary-cta:active {
  box-shadow: 0 0 0 6px color-mix(in srgb, var(--accent-1) 28%, transparent);
  transition: transform 0.22s, box-shadow 0s;  /* glow appears instantly */
}
```

- 테마가 바뀌면 그라데이션 색도 따라 변경 (DECISIONS.md §5.1)
- 적용 위치: Persona "View persona report", Discovery ♥(Save), AI Search chat send ↑
- 기존 depth shadow가 있는 버튼(예: Discovery ♥)은 두 그림자를 스택 (`0 6px 16px rgba(0,0,0,0.25), 0 0 0 6px ...`)

### 8.2 Secondary Button ✅
보조 액션 (와닿지 않는 옵션 닫기, Skip 등).

```css
background: var(--surface);
color: var(--text);
border: 1px solid var(--border);
border-radius: calc(var(--radius-md) * 1px);
padding: 14px 16px;
font-weight: 500-600;
min-height: 44px;
```

### 8.3 Ghost Button ✅
가장 약한 강조 (Share, View more 등).

```css
background: transparent;
color: var(--text);
border: 1px solid var(--border);
border-radius: calc(var(--radius-md) * 1px);
padding: 14px 16px;
font-weight: 500;
min-height: 44px;
```

### 8.4 Destructive Button ✅
삭제 / 차단 / 취소 등 위험 액션.

```css
background: transparent;
color: var(--destructive);
border: 1px solid var(--destructive);
border-radius: calc(var(--radius-md) * 1px);
padding: 14px 16px;
font-weight: 600;
min-height: 44px;
```

> 호버 시 채움으로 전환할지(`bg: var(--destructive); color: #fff`) 는 인터랙션 결정 단계에서 정함.

### 8.5 Input (Glassmorphic, 3-state focus) ✅

```css
.input {
  background: color-mix(in srgb, var(--surface) 72%, transparent);
  border: 1px solid var(--border);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-radius: calc(var(--radius-pill) * 1px);  /* or radius-md for square inputs */
  padding: 12px 18px;
  color: var(--text);
  transition: border-color 0.18s, box-shadow 0.4s ease-out;
}

.input:focus-within {
  border-color: var(--accent-1);
}

.input:has(input:active) {  /* the brief click moment */
  box-shadow: 0 0 0 4px color-mix(in srgb, var(--accent-1) 28%, transparent);
  transition: border-color 0.18s, box-shadow 0s;  /* glow appears instantly */
}
```

**3단계 포커스 상태:**
- Default: 회색 border
- Focused (포커스 유지): accent-1 border (glow 없음, 절제됨)
- Click moment (마우스 누른 순간): accent-1 border + glow shadow → 0.4s에 걸쳐 부드럽게 페이드 아웃

### 8.6 Project Card (Discovery canonical) ✅
DESIGN.md §3.5.2 + §3.5.4 + §3.5.5의 조합. ArchiTinder의 핵심 카드.

**Front face**
```
+-------------------------------+
|  [project main image]      ↻  |  ← flip hint top-right
|                               |
|                               |
|         (gradient fade)       |
|                               |
| Title (h2, 22px, 700)         |
| Architects (13px italic, 60%) |
| ─────── divider ───────       |
| YEAR  | LOCATION | PROGRAM    |  ← 3-col info grid
| 2004  | Kanazawa | Museum     |
+-------------------------------+
```

```yaml
card-radius: 20         # var(--radius-lg)
card-shadow: "0 12px 32px rgba(0,0,0,0.3)"
card-bottom-gradient: "linear-gradient(180deg, transparent 30%, rgba(0,0,0,0.82))"
card-text-color: "#fff"
card-title: 22px / 700 / line-clamp 2
card-architects: 13px / regular / rgba(255,255,255,0.6)   # italic 제거 ✅
card-divider: "1px rgba(255,255,255,0.15)"
card-info-label: 10px / 600 / uppercase 0.06em / rgba(255,255,255,0.5)
card-info-value: 13px / 600 / #fff / single-line ellipsis
card-info-columns: 3  # YEAR + LOCATION + PROGRAM
card-info-layout: "flex / justify-content: space-between"  # 텍스트 너비대로 + 등간격 ✅
```

**Back face (3D rotateY)**
- Click anywhere on the card → `transform: rotateY(180deg)` on inner wrapper
- Back face: full-bleed horizontal-scrolling gallery of sub-images
- `scroll-snap-type: x mandatory` for clean image-per-frame snapping
- Left/Right chevron arrows (32px, dark blur) as visual affordance
- Bottom action: "View Gallery · N photos" pill with 4-stop gradient backdrop

```yaml
flip-perspective: 1200px
flip-duration: 0.5s
flip-easing: "cubic-bezier(0.4, 0, 0.2, 1)"
back-action-gradient: "linear-gradient(to top, rgba(0,0,0,0.96) 0%, rgba(0,0,0,0.65) 45%, rgba(0,0,0,0.18) 80%, transparent 100%)"
```

**Geometry ✅**
```yaml
card-aspect-ratio: "4 / 5"   # portrait, Tinder 가로 비율
                              # mobile: 화면 채움(flex:1) / desktop: 명시적 4/5
```

**Border / Hover 정책 ✅**
- **Border 없음** — `radius-lg` + `box-shadow: 0 12px 32px rgba(0,0,0,0.3)`만으로 카드 경계 표현 (배경 이미지/그라데이션과 충돌 회피)
- **Hover 효과 없음** — Discovery는 스와이프 중심 UX, hover는 자연스러운 인터랙션이 아님. 카드 액션은 클릭(flip) / 스와이프 / Like·Skip 버튼으로만 수행.

**Interaction ✅** — 환경별 input 방식 모두 동등하게 지원

| 액션 | 모바일 | 데스크탑 |
|---|---|---|
| **Skip** (← swipe) | 좌 swipe 제스처 | `ArrowLeft` 키보드 OR 마우스 좌 드래그 OR ✕ 버튼 클릭 |
| **Like** (→ swipe) | 우 swipe 제스처 | `ArrowRight` 키보드 OR 마우스 우 드래그 OR ♥ 버튼 클릭 |
| **Flip (front ↔ back)** | 카드 사진 탭 | `Enter` 키보드 OR 사진 클릭 |

원칙:
- **드래그 임계값**: 카드 폭의 25% 이상 이동 시 swipe 확정. 미달 시 원위치 spring back
- **키보드 visibility**: 활성 화면이 Discovery일 때만 단축키 리스너 바인딩 (다른 화면에서는 비활성)
- **포커스 상태**: 키보드 사용자를 위해 카드/버튼에 명시적 focus ring (`:focus-visible`)

**텍스트 가독성 처리 ✅** — Front/Back 양면에 동일한 검은 그래디언트 fade 적용
실제 프로젝트 사진(다양한 톤) 위에 흰 텍스트가 놓이므로, 하단 영역에 검정 페이드로 contrast 확보.
Glassmorphic 패널 / Solid scrim / Text-shadow / Per-element chips / mix-blend 등 8가지 대안을 비교한 끝에
**검정 그래디언트 fade가 가장 자연스럽고 사진을 가리지 않으며 가독성도 확실**하다는 결론.

Front:
```css
.discovery-face.front::before {
  content: ""; position: absolute; inset: 0;
  background: linear-gradient(180deg, transparent 30%, rgba(0,0,0,0.82));
}
```

Back (gallery 면의 "View Gallery · N photos" 액션도 동일 원칙으로 처리):
```css
.back-action {
  background: linear-gradient(to top,
    rgba(0,0,0,0.96) 0%,
    rgba(0,0,0,0.65) 45%,
    rgba(0,0,0,0.18) 80%,
    transparent 100%);
}
/* 버튼 pill 배경 없음 — "View Gallery · 6 photos"도 텍스트이므로 그래디언트 위에 직접 표기 */
.back-action button {
  background: transparent;
  border: 0;
  color: #fff;
  font-weight: 600;
}
```

핵심 원칙:
- 카드 위 모든 흰 텍스트는 **하단 검정 그래디언트 위에** 놓는다 (front title/architects/info, back action label 동일)
- 별도의 panel/scrim/chip 배경 없음 — 그래디언트가 유일한 가독성 보조 수단
- 버튼이라도 텍스트라면 pill bg 없이 그래디언트에 직접 표기

### 8.7 Folder Card (Boards canonical) ✅
"폴더" 메타포 카드. 상단 탭(라벨)이 오른쪽으로 비스듬히 좁아지는 모양.

**구조 / 콘텐츠 순서 ✅**
```
+----------------+
| Tab title (⋯)   \              ← 1. 폴더 제목 (탭 안, 긴 경우 ⋯)
+------------------+----+
|                       |
|  Overview (긴 설명)    |        ← 2. overview
|  Summary (한 줄 요약)  |        ← 3. summary
|  ─── 구분선 ───        |        ← 4. divider (1px solid --border)
|  [img] [img] [img]    |        ← 5. 프로젝트 메인 이미지 3개
|                       |
|  N projects   2026.x  |        ← 6. project count + 생성일 (양 끝 정렬)
+-----------------------+
```

```yaml
folder-tab-color:        "var(--accent-1)"
folder-tab-text-color:   "#fff"
folder-tab-height-visible: 32      # 화면에 보이는 높이 (총 48 — body 모서리 16px 가려짐)
folder-tab-offset-x:     4         # body 좌측보다 4px 안쪽에서 시작
folder-tab-radius-tl:    10        # body radius / 1.6
folder-tab-radius-tr:    7         # 슬랜트 시작점의 둥글기
folder-tab-min-width:    "calc((50% - 4px) / 0.7)"   # 슬랜트 시작점이 body 중간 정렬
folder-tab-max-width:    "calc(100% - 20px)"
folder-tab-label-padding: "0 28% 0 18px"             # 우측 28%는 슬랜트 회피 영역

folder-body-bg:          "var(--surface-2)"
folder-body-radius:      16
folder-body-padding:     18

folder-title-font-size:    13
folder-title-font-weight:  600
folder-title-ellipsis:     "⋯"     # U+22EF midline (NOT … U+2026, NOT ...)
```

**Title 잘림 처리** ✅
- 짧은 제목: 전체 표시 (잘림 없음)
- 긴 제목: JS 이진 탐색으로 탭 내부 폭에 맞는 최장 prefix를 찾아 `prefix + ⋯` 으로 렌더
- `text-overflow: clip` 사용 (브라우저 기본 `…` 진입 차단)

**Hover ✅** — **lift + 1px accent outline, shadow/glow 없음**
```css
.folder-card {
  transition: transform 0.2s ease, filter 0.18s;
  /* base: filter 없음 — 평면, drop-shadow 없음 */
}
.folder-card:hover {
  transform: translateY(-3px);
  filter:
    drop-shadow( 1px  0   0 var(--accent-1))
    drop-shadow(-1px  0   0 var(--accent-1))
    drop-shadow( 0    1px 0 var(--accent-1))
    drop-shadow( 0   -1px 0 var(--accent-1));
}
```

- 4방향 stacked `drop-shadow`로 탭의 슬랜트 모서리까지 따라가는 윤곽선 구현
  (CSS `outline`은 사각형이라 슬랜트 곡선을 따라가지 못함)
- 디폴트/호버 모두 underneath drop-shadow 없음 (평면 디자인)
- `box-shadow` 미사용

### 8.8 Loading State ✅ (Skeleton + Spinner 조합)
- **카드/리스트 골격** → **Skeleton** (radius + 회색 블록으로 실제 레이아웃 모방)
- **버튼/짧은 액션** → **Inline spinner** (버튼 라벨을 spinner로 교체, 비활성화)
- Shimmer 애니메이션 없음 (성능 부담 + Vibe ✅ 키워드와 무관)

```yaml
skeleton-bg:           "var(--surface-2)"
skeleton-radius:       "var(--radius-sm)"   # 8px
skeleton-block-height: 16                   # 텍스트 1줄, 카드는 aspect-ratio
spinner-size:          20
spinner-stroke-width:  2
spinner-duration:      "1.2s"   # 회전 1회
```

### 8.9 Error / Empty State ✅ (3-tier)
| 시나리오 | 패턴 | 위치 |
|---|---|---|
| 데이터 자체 없음 (e.g. 첫 보드, 추천 끝) | **Empty 컴포넌트** — 친근 일러스트 + 한 줄 설명 + Primary CTA | 페이지/리스트 영역 |
| 컴포넌트 로드 실패 (네트워크/서버) | **Inline Error** — 구체 메시지 + "다시 시도" 버튼 | 해당 컴포넌트 자리 |
| 액션 실패 (저장/전송 등 일시적) | **Toast** (§8.11) | bottom-center |

원칙: **catastrophic full-screen 에러는 만들지 않음** — 항상 컴포넌트 단위로 격리, 사용자가 다른 부분은 계속 사용 가능하게.

### 8.10 Modal / Bottom Sheet ✅
**환경별 자동 선택**
- 모바일 (≤768px): **Bottom Sheet** — 화면 하단에서 swipe-up. Gesture-friendly Vibe와 일치
- 데스크탑 (≥769px): **Centered Modal** — 중앙 정렬, 배경 dim

```yaml
sheet-radius-top:    "calc(var(--radius-xl) * 1px)"  # 24px, 모서리 위쪽만
sheet-handle:        "4px × 36px"                    # 상단 swipe handle bar
sheet-max-height:    "85vh"                          # 화면 85% 이하
sheet-backdrop:      "rgba(0,0,0,0.4)"
modal-max-width:     "480px"
modal-radius:        "calc(var(--radius-lg) * 1px)"  # 20px
modal-padding:       "24px"
sheet-anim-duration: "var(--motion-flip)"            # 500ms slide-up
sheet-anim-easing:   "var(--motion-ease)"
```

닫기: 모바일은 swipe-down + backdrop tap, 데스크탑은 ESC + backdrop click + 우상단 ✕ 버튼

### 8.11 Toast ✅
- **위치**: **bottom-center** (모바일 nav-bar는 가리지 않고, 데스크탑에서도 자연스러움)
- **지속 시간**: **3초** 기본 (longer-toast 옵션은 5초)
- **스타일**: **Glassmorphic** (Vibe ✅과 일치) — 헤더/입력바와 동일한 frosted-glass 패턴

```yaml
toast-position:       "bottom-center"
toast-bottom-offset:  "calc(var(--tabbar-height) + 16px)"  # 모바일: nav 위로
toast-duration:       3000   # ms
toast-duration-long:  5000   # ms (긴 메시지/중요)
toast-bg:             "color-mix(in srgb, var(--surface) 72%, transparent)"
toast-backdrop:       "blur(12px)"
toast-border:         "1px solid var(--border)"
toast-radius:         "var(--radius-pill)"
toast-padding:        "10px 16px"
toast-enter:          "var(--motion-normal) var(--motion-ease)"   # slide-up + fade-in
toast-exit:           "var(--motion-fast) var(--motion-ease-out)"  # fade-out
```

타입별 색조:
- info: default
- success: `border-color: var(--accent-2)`
- warning: `border-color: var(--accent-3)`
- error: `border-color: var(--destructive)`

### 8.12 Icon System ✅
앱 전체의 모든 line icon은 단일 시스템을 따른다. 헤더 버튼·하단 nav·인라인
icon-in-button 어디든 같은 visual weight·같은 stroke 규칙으로 렌더된다.

```yaml
# Stroke weight (모든 line icon 공통)
icon-stroke-width:      1.5       # 전체 통일
icon-style:             "outline / stroke-based only"
icon-source-convention: "Feather / Lucide"

# Size (위치별)
icon-size-header:       18        # .icon-btn / .back-btn 내부 SVG
icon-size-nav:          22        # 하단 nav 내부 SVG
icon-size-inline:       16        # ghost-btn / 인라인 SVG

# Header button frame (.icon-btn / .back-btn)
icon-btn-size:          36        # 36×36 circle tap target
icon-btn-bg:            transparent
icon-btn-bg-hover:      "var(--surface)"
icon-btn-border:        0
icon-btn-radius:        50%
```

**SVG 작성 규칙 ✅**
모든 아이콘 SVG는 동일한 attribute set으로 시작한다 — 인라인으로 `stroke-width`
지정 금지 (CSS가 단독 관리).

```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
     stroke-linecap="round" stroke-linejoin="round">
  <!-- paths only — no inline width/height/stroke-width -->
</svg>
```

- `viewBox: 0 0 24 24` — Feather/Lucide 표준
- `fill="none"` — outline 톤 유지 (filled icon 금지)
- `stroke="currentColor"` — 테마/parent color 자동 상속
- 사이즈는 CSS에서 (`.icon-btn svg { width: 18px; height: 18px; }` 등)
- stroke-width도 CSS에서 (`stroke-width: 1.5`)
- linecap·linejoin: `round` 고정 — 모서리 톤 일관

**Character glyph 금지 ✅**
`←`, `⌕`, `⤺`, `↗`, `⋯`, `+` 같은 유니코드 character는 icon-btn 안에서 절대
사용하지 않는다. 이유:
- 폰트마다 글리프 디자인이 달라 stroke weight·비율·밀도가 매번 다름
- stroke-1.5 SVG와 같은 visual weight를 절대 못 맞춤
- OS별 fallback 폰트에 따라 깨질 위험

대체 매핑 (실제 사용 중):

| 기존 글리프 | 의미 | SVG icon |
|---|---|---|
| `←` | back | arrow-left (line + polyline) |
| `⌕` | search | search (circle + handle line) |
| `⤺` | undo | rotate-counterclockwise |
| `↗` | share / external | arrow-up-right (L-shape) |
| `⋯` | more | more-horizontal (circle × 3, r=1.2) |

**Header button frame ✅**
`.icon-btn`과 `.back-btn`은 한 단일 selector로 합쳐 관리한다. 둘 다 같은 spec:
- 36×36 circle, transparent bg, no border
- hover 시에만 `var(--surface)` 배경
- 내부 SVG는 18×18, stroke 1.5
- transition: `var(--motion-fast) var(--motion-ease)` (배경 fade)

`.hdr-spacer` (제목 우측 정렬용 빈 슬롯)는 동일한 36px 폭으로 둬서 좌우 중심
잡힘 보장.

`.hdr-text-btn` (e.g. "저장")도 같은 36px height + pill radius로 헤더 줄에
세로 정렬 일치.

### 8.13 Toggle (Switch) ✅
on/off 이분 설정용 pill 스위치. 알림 설정·공개/비공개 같은 곳에 사용.
체크박스가 아니라 **즉시 적용되는 설정**을 표현 — 저장 버튼 없음.

```yaml
toggle-width:           44
toggle-height:          26
toggle-thumb-size:      20
toggle-thumb-inset:     3       # track 안쪽 패딩 (top + left/right offset)
toggle-track-radius:    999     # pill
toggle-thumb-radius:    "50%"
toggle-bg-on:           "var(--accent-1)"
toggle-bg-off:          "var(--surface-3)"
toggle-thumb-color:     "#FFFFFF"
toggle-thumb-shadow:    "0 1px 3px rgba(0,0,0,0.25)"
toggle-transition:      "var(--motion-fast) var(--motion-ease)"   # bg + thumb slide
toggle-disabled-opacity: 0.55
```

**HTML / 접근성**
- `<button type="button" role="switch" aria-checked={checked} aria-label="..." />` — 체크박스 아닌 switch
- 키보드: Tab 포커스 + Space/Enter로 토글 (브라우저 기본 button 동작)
- Disabled 시 `disabled` 속성 + `cursor: not-allowed`

**ChannelRow (라벨 + 토글 한 줄)**
```
+----------------------------+
| 푸시                  [●——] |
| 이메일                [——○] |
+----------------------------+
```
- 라벨 좌측 (`fontSize: 13`, `--color-text`)
- 토글 우측, `justify-content: space-between`
- 행 패딩 `4px 0`, 행 간격 `gap: 4`

**CategoryBlock (카드 안에 N개 ChannelRow 묶음)** — 알림 설정의 기본 단위
```
┌─────────────────────────────────────┐
│ 소셜 활동                            │  ← 라벨 (14px / 600 / --color-text)
│ 팔로우 · 좋아요 · 댓글 · 멘션         │  ← hint (12px / --color-text-muted)
│                                     │
│ 푸시                          [●——] │
│ 이메일                        [●——] │
└─────────────────────────────────────┘
```
```yaml
toggle-card-bg:         "var(--surface)"
toggle-card-border:     "1px solid var(--border)"
toggle-card-radius:     "var(--radius-lg)"
toggle-card-padding:    16
toggle-card-margin-y:   12
```

**잠금 (locked) 상태 — 필수/시스템 설정 표현** ✅
일부 설정(예: 계정 보안 알림)은 **표시는 하되 사용자가 끄지 못하게** 잠근다. 시각화 규칙:
- 카테고리 라벨 옆에 **자물쇠 아이콘** (§8.12 stroke-1.5, `width: 12`, `--color-text-dim`)
- 토글 둘 다 `disabled` (opacity 0.55, `cursor: not-allowed`)
- **저장된 값과 무관하게 항상 ON으로 렌더** — 데이터가 어떤 이유로 OFF여도 UI는 ON을 보임 (시스템이 그 알림을 강제 발송하기 때문에 그 사실을 그대로 반영)
- 카드 하단에 안내 텍스트: "이 알림은 …을 위해 항상 켜집니다."
  ```yaml
  toggle-locked-notice-size:  11
  toggle-locked-notice-color: "var(--color-text-dim)"
  toggle-locked-notice-margin-top: 10
  ```

**저장 패턴 — fire-and-forget**
토글이 바뀌면 **저장 버튼 없이 즉시** API를 호출. UI는 낙관적 업데이트(`setState`)를 먼저 적용하고, 네트워크 실패는 조용히 무시(다음 진입에서 서버 값으로 재동기화).
```js
const onChange = (next) => {
  setUser((u) => ({ ...u, notifications: next }))
  updateNotificationPrefs(next).catch(() => {})    // fire-and-forget
}
```
원칙:
- 설정 토글 = 즉시 저장, 저장 버튼 만들지 않음 ("저장" 단계가 있으면 사용자가 토글을 누르고 떠나는 멘탈 모델과 어긋남)
- 폼 입력(이름·이메일 등) = 명시적 "저장" 버튼 유지 (입력 중간값을 매 keystroke 저장하면 안 됨)

**옵트인 vs 옵트아웃 기본값 정책** ✅
한국 정보통신망법·개인정보보호법·GDPR은 **마케팅성 통신을 사전 명시 동의(옵트인)** 로 요구. 적용:
- **마케팅·프로모션 알림**: 기본 OFF (옵트인) — 사용자가 직접 켜야 발송
- **서비스 운영 알림**(계정 보안, 본인 콘텐츠 활동): 기본 ON — 서비스 사용에 필요한 것으로 간주
- **그 외 일반 알림**(소셜·추천): 기본 ON 또는 케이스별 — 가독성보다 사용자 선택권 우선

---

## 9. 결정된 사항

| 항목 | 결정 | 비고 |
|---|---|---|
| Default Theme | **GitHub Light** | (DECISIONS.md §2) ✅ |
| Theme Switching | 엔드 유저에게 노출 (배경색 + 강조색 칩) | (DECISIONS.md §2) ✅ |
| Body Font | **IBM Plex Sans KR** | (DECISIONS.md §3) ✅ |
| Font Switching | 엔드 유저에게 노출 (Font 라벨 = 전환될 폰트로 렌더링) | (DECISIONS.md §3) ✅ |
| Font-weight 상한 | **700** (800/900 금지) | (DECISIONS.md §3) ✅ |
| Type Scale | **환경별 분리 (Desktop / Mobile)** | (DECISIONS.md §3) ✅ |
| Destructive 색상 | **테마화** (테마별 알맞은 빨강) | (DECISIONS.md §2) ✅ |
| Text 위계 | **4단계 유지** | (DECISIONS.md §2) ✅ |
| iOS Safe Area | **하단 TabBar/CTA에만** | (DECISIONS.md §4) ✅ |
| Implementation | 하이브리드 (인라인 + CSS 변수) | (DECISIONS.md §1.3) |
| Accent 정책 | **테마화 (CSS 변수)** | (DECISIONS.md §2) ✅ |
| 반응형 | **Mobile-first + 데스크탑용 좌측 사이드바 재레이아웃** | (DECISIONS.md §4) ✅ |
| TabBar Height | **64px (라벨 있음) / 56px (아이콘만)** | (DECISIONS.md §4) ✅ |
| Border Radius | **4단계 토큰화 (sm/md/lg/xl)** | (DECISIONS.md §4) ✅ |
| Touch Target | **모바일 44px / 데스크탑 32px+** | (DECISIONS.md §4) ✅ |
| Vibe Keywords | **Glassmorphic ✅ · Fluid ✅ · Gesture-friendly (hint only) ✅** | (DECISIONS.md §1) ✅ |
| Folder Card Hover | **lift + 1px accent outline, no shadow/glow** | (§8.7) ✅ |
| Theme Switcher 노출 | **Profile → Settings → Appearance** | (§5.4) ✅ |
| Theme 영속성 | **사용자 계정 (크로스 디바이스), 비로그인은 세션 한정** | (§5.5) ✅ |
| Project Card Aspect | **4 / 5 portrait** | (§8.6) ✅ |
| Project Card Border | **없음 — radius + shadow만** | (§8.6) ✅ |
| Project Card Hover | **효과 없음 (스와이프 UX)** | (§8.6) ✅ |
| Project Card Text 가독성 | **하단 검정 그래디언트 fade (front/back 동일)** | (§8.6) ✅ |
| Motion Tokens | **Duration 4단계 (fast/normal/slow/flip) + Easing 2개 (standard/ease-out)** | (§3.5) ✅ |
| 이중 폰트 운영 | **단일 폰트만 — 헤딩/본문 동일 family, 토글 = 전체 전환** | (§2.5a) ✅ |
| Loading State | **Skeleton + Spinner 조합 (Shimmer 없음)** | (§8.8) ✅ |
| Error / Empty | **3-tier: Empty 컴포넌트 / Inline Error / Toast** | (§8.9) ✅ |
| Modal / Sheet | **환경별 자동: 모바일 Bottom Sheet, 데스크탑 Centered Modal** | (§8.10) ✅ |
| Toast | **bottom-center · 3s · glassmorphic** | (§8.11) ✅ |
| Discovery Interaction | **키보드 ←/→ + 드래그 → swipe, Enter + 사진 클릭 → flip** | (§8.6) ✅ |
| Hover 구현 방식 | **CSS `:hover` 의사 클래스만 (인라인 JS 금지)** | (§4) ✅ |
| 한글 폰트 fallback | **Web → OS Korean → system-ui (Sans/Serif 각각)** | (§2.1) ✅ |
| MD 파일 구조 | **design.md 단일 소스, DESIGN.md는 archive** | (§10.1) ✅ |
| 디자인 토큰 위치 | **tokens.css 전용 파일 분리** | (§10.2) ✅ |
| 테마/폰트 추가 절차 | **catalog 수정 + design.md 업데이트 + PR 디자인 검토** | (§10.3) ✅ |
| 컴포넌트 격리 정책 | **2+ 페이지 사용 시 추출 (디자인 시스템 입도는 무조건)** | (§10.4) ✅ |
| Aesthetics Tone | **Mode별 톤 분리: Light=clear/editorial, Dark=cinematic/atmospheric** | (§4) ✅ |
| Implementation 규칙 | **CSS variables + Inline 하이브리드 (외부 UI/CSS-in-JS 라이브러리 금지)** | (§4) ✅ |
| Icon 형식 | **모든 icon은 stroke-based SVG (character glyph 금지)** | (§8.12) ✅ |
| Icon Stroke Width | **1.5 — 전체 통일 (header / nav / inline 어디든)** | (§8.12) ✅ |
| Icon Size | **header 18 / nav 22 / inline-in-button 16** | (§8.12) ✅ |
| Icon SVG 규약 | **viewBox 24, fill=none, stroke=currentColor, linecap/join=round, 인라인 stroke-width 금지** | (§8.12) ✅ |
| Header Button Frame | **.icon-btn = .back-btn 단일 spec: 36×36 circle, transparent, hover만 surface bg** | (§8.12) ✅ |
| iOS 입력 줌인 방지 | **모든 input/textarea/select font-size ≥ 16px (전역 + 인라인 양쪽)** | (§7.4.1) ✅ |
| 키보드-aware 스크롤 | **`visualViewport.resize` 후 `scrollIntoView({block:'center'})`, 400ms fallback** | (§7.4.2) ✅ |
| 오버스크롤 배경 통일 | **`<meta name="theme-color">` 동적 갱신 + `html { background-attachment: fixed }`, document-level 스크롤 유지** | (§7.4.3) ✅ |
| 모바일 사진 picker | **`<input type="file" accept="image/*">` 단독 사용 (카메라/갤러리 OS 시트 자동 처리), 클라이언트 256×256 JPEG 리사이즈** | (§7.4.4) ✅ |
| Mobile-only 모듈 셸 | **`max-width: 460px; margin: 0 auto`로 단일 컬럼 (데스크탑은 가운데 정렬된 모바일 폭으로 fallback)** | (§7.4.5) ✅ |
| Toggle (Switch) Spec | **44×26 pill / thumb 20 / on=accent-1, off=surface-3 / role=switch, aria-checked** | (§8.13) ✅ |
| Toggle 저장 패턴 | **즉시 저장 (fire-and-forget), 별도 저장 버튼 없음. 폼 입력은 명시적 저장 버튼 유지** | (§8.13) ✅ |
| Toggle 잠금 상태 | **자물쇠 아이콘 + disabled + 항상 ON 강제 렌더 + 카드 하단 안내 텍스트** | (§8.13) ✅ |
| 알림 기본값 정책 | **마케팅=OFF (옵트인), 보안=ON, 일반=ON. 한국 정보통신망법·GDPR 준수** | (§8.13) ✅ |

---

## 10. 코드 구조 운영

### 10.1 MD 파일 정책 ✅
- **design.md = single source of truth.** 모든 토큰/결정/스펙은 여기 기록
- DESIGN.md (이전 디자인 시스템 가이드)는 **archive** 처리 — 역사 참조용
- 새 결정·변경은 design.md에만 추가, DESIGN.md 편집 금지
- DECISIONS.md는 결정 추적용 보조 문서 (resolve 시 design.md로 흡수)

### 10.2 디자인 토큰 위치 ✅
- **전용 `tokens.css` 파일 분리.** :root { --bg, --accent-*, --motion-*, ... } 모음
- 컴포넌트 스타일과 분리하여 토큰 관심사만 담당
- 앱의 진입 CSS (`index.css` 또는 `main.css`)에서 `@import "tokens.css"` 또는 build 시 inline
- 변경 시 캐시 무효화 잘 동작하도록 단일 파일

### 10.3 테마 / 폰트 추가 절차 ✅
새 테마·폰트는 **PR을 통해서만** 추가/제거. 단계:
1. **catalog 수정**: `catalog.py` (preview용) / `tokens.ts` (실제 앱)에 새 entry 추가
2. **design.md 업데이트**: §1.2 (테마) 또는 §2 (폰트) 표·yaml 블록·설명을 동기화
3. **PR 제출**: 새 옵션 미리보기 스크린샷 + 추가 사유 명시
4. **디자인 검토**: 1명 이상 디자인 reviewer 승인 후 머지
- 자유 추가 금지 — 일관성/품질 관리를 위해 검토 단계 필수

### 10.4 컴포넌트 격리 정책 ✅
**추출 기준 (셋 중 하나라도 해당하면 컴포넌트로 추출)**
- 2+ 페이지/화면에서 사용되는 패턴
- 단일 페이지에서만 쓰여도 50줄을 넘는 JSX 블록
- 디자인 시스템 입도 (Button / Input / Card / Toast / Modal 등) — 무조건 컴포넌트

**inline 유지가 적절한 경우**
- 단일 페이지 전용의 짧은 레이아웃 코드
- 1회성 정적 컴포지션
- 디자인 시스템보다 상위 계층의 페이지 컴포지션

> 의도: 재사용성과 가독성의 균형. 너무 일찍 추출하면 잘못된 추상, 너무 늦으면 중복 누적.

---

## 11. 진행 중 / 미결정

- [ ] **Persona 화면 컴포넌트** (DECISIONS.md §5.4 Profile Action Row + §5.5 Stats Row)
  - Persona 화면 디자인 작업 시작 시 진행
- 이 외 모든 카테고리는 §9 결정 테이블에 해소 (38건 ✅)

---

## 사용법

1. 위 `yaml` 블록의 값을 수정한다.
2. 파일을 저장한다.
3. 브라우저(http://127.0.0.1:5001/)는 1.5초마다 자동 새로고침으로 변경을 감지한다.
4. 새 토큰을 추가하려면 yaml 블록에 `key: "value"` 한 줄을 더한다.
