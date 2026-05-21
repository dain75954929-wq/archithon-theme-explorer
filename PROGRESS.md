# ArchiTinder Design System — Progress Log

> 이 문서는 `design.md`(단일 진실 소스) + `DECISIONS.md`(작업 체크리스트)를 통해
> 진행한 디자인 시스템 결정 작업의 진행 기록입니다.
> 현재 design.md §9 결정 테이블에 **38개 결정**이 ✅ 처리되어 있으며,
> Persona 화면 2개 항목(§5.4 / §5.5)만 남아 있습니다.

---

## 진행 방식

1. **DECISIONS.md = 작업 체크리스트** — 미결정 항목을 `[ ]`로 추적
2. 한 번에 1~4개 항목 선택 → **AskUserQuestion**으로 사용자 협의
3. 확정된 결정은 **design.md에 명문화** (yaml 토큰 + 본문 설명)
4. 필요 시 **`templates/design_preview.html` (5001)**에 시각 구현 추가
5. **§9 결정 테이블** + **DECISIONS.md 항목** ✅ 동기화

---

## 해소된 결정 (38)

### §1 Color / Brand
- Default Theme: **GitHub Light**
- Theme Switching: 엔드 유저 노출 (배경+강조 칩)
- Accent 정책: 테마화 (CSS 변수)
- Destructive: 테마별 빨강 토큰
- Border 투명도: 라이트 0.08 / 다크 0.07 유지
- Text 위계: 4단계 (text / text-2 / text-muted / text-dim)
- **Aesthetics Tone**: Mode별 분리 — Light = Clear·Editorial·Content-first / Dark = Cinematic·Atmospheric·Dramatic. 공통 분모는 "premium, refined, confident"
- **Implementation**: CSS variables + Inline 하이브리드 (외부 UI/CSS-in-JS 라이브러리 금지)
- Vibe Keywords: Glassmorphic · Fluid · Gesture-friendly (3개 모두 채택, gesture는 swipe hint만)

### §2 Typography
- Body Font: **IBM Plex Sans KR** (default)
- Font Switching: 엔드 유저 토글 — "Font" 라벨이 전환될 폰트로 렌더링
- Font-weight 상한: **700** (800/900 금지)
- Type Scale: 환경별 분리 — Desktop H1 48 / H2 30 / Body 18, Mobile H1 32 / H2 24 / Body 16
- 단일 폰트 정책: 헤딩/본문 동일 family, 이중 폰트 페어링 금지
- **한글 폰트 fallback**: Web → OS Korean → system-ui (Sans/Serif 각각 명시적 체인)

### §3 Layout & Motion
- Border Radius: 4단계 토큰 (sm 8 / md 12 / lg 20 / xl 24 + pill 999)
- Touch Target: 모바일 44px / 데스크탑 32px+
- TabBar Height: 64 (라벨 있음) / 56 (아이콘만)
- iOS Safe Area: 하단 fixed 요소(TabBar/CTA)에만
- Responsive: Mobile-first + 데스크탑 220px 좌측 사이드바, max-width 1200
- **Motion Tokens**: Duration 4단계 (fast 180ms / normal 220ms / slow 400ms / flip 500ms) + Easing 2개 (standard / ease-out). 인라인 ms·cubic-bezier 하드코딩 금지

### §5 Theme Switcher 노출 / 영속성
- **노출 위치**: Profile → Settings → Appearance
- **영속성**: 사용자 계정 (크로스 디바이스). 비로그인은 세션 한정, 다음 방문 시 디폴트로 복귀

### §6 Interaction
- **Discovery Interaction**: 키보드 ←/→ + 마우스 드래그 → swipe(Skip/Like), Enter + 사진 클릭 → flip. 드래그 임계 25%, focus ring 명시
- **Hover 구현**: CSS `:hover` 의사 클래스만 (인라인 onMouseEnter/Leave 폐기)

### §8 Components
- **Primary CTA**: accent 그라데이션 + click moment glow shadow
- **Secondary**: surface + border
- **Ghost**: transparent + border
- **Destructive**: transparent + destructive border/text
- **Input (Glassmorphic)**: 3-state focus (default → focus → click moment glow)
- **Project Card** (§8.6, Discovery canonical)
  - Geometry: aspect 4:5 portrait
  - Border: 없음 (radius + shadow만)
  - Hover: 효과 없음 (스와이프 UX)
  - **텍스트 가독성**: 하단 검정 그래디언트 fade (front/back 동일, 버튼 pill 제거)
  - **Interaction**: 위 §6 참조
- **Folder Card** (§8.7, Boards canonical)
  - 탭(accent-1) + 바디(surface-2), SVG path 슬랜트 모서리
  - Title: 짧으면 전체 / 길면 JS 이진탐색 prefix + ⋯ (U+22EF midline)
  - Hover: lift + 1px accent outline (4방향 stacked drop-shadow, slant까지 따라감)
  - 콘텐츠 순서: overview → summary → 구분선(1px solid) → 이미지 3개 → N projects + 날짜
- **Loading** (§8.8): Skeleton (카드/리스트) + Spinner (버튼). Shimmer 없음
- **Error/Empty** (§8.9): 3-tier — Empty 컴포넌트 / Inline Error / Toast. Catastrophic full-screen 금지
- **Modal/Sheet** (§8.10): 환경별 자동 — 모바일 Bottom Sheet, 데스크탑 Centered Modal
- **Toast** (§8.11): bottom-center · 3s · glassmorphic · 타입별 border-color

### §10 코드 구조 운영
- **MD 파일 정책**: design.md = single source of truth. DESIGN.md는 archive
- **디자인 토큰 위치**: `tokens.css` 전용 파일 분리 (CSS variables만)
- **테마/폰트 추가 절차**: catalog 수정 + design.md 업데이트 + PR 디자인 검토 (자유 추가 금지)
- **컴포넌트 격리**: 2+ 페이지 사용 시 추출. 단일 페이지 50줄 초과도 추출. 디자인 시스템 입도(Button/Input/Card 등)는 무조건 컴포넌트

---

## Preview (5001) 구현 사항

설계 결정을 시각 검증하기 위해 추가/변경한 기능:

| 영역 | 구현 |
|---|---|
| **Boards · Folder Card** | SVG path 탭 + 본체, 6개 카드 (alt 팔레트), 18장 Unsplash 건축 사진 썸네일 |
| **Folder Title 잘림** | JS 이진탐색 + ⋯ midline ellipsis, 환경/화면 전환 시 재측정 |
| **Folder Hover** | translateY(-3px) + 4방향 drop-shadow outline (탭 슬랜트까지 따라감) |
| **Folder 콘텐츠 재배열** | overview → summary → divider → 이미지 → meta로 재구성, count/date 위계 통일 |
| **Discovery · Project Card** | Front 사진 + Back gallery 4장 모두 Unsplash 실제 건축 사진 |
| **Discovery 텍스트 가독성** | 8가지 변형(A1~D1) trial UI로 비교 → 검정 그래디언트 fade로 확정 후 trial 제거 |
| **Discovery Interaction** | Pointer drag (25% 임계 + spring back / fly off), 키보드 ←/→ + Enter, ✕/♥ 버튼 모두 swipe |
| **Motion Tokens 적용** | 11곳의 하드코딩 transition → `var(--motion-*)` wiring |

---

## 변경된 파일

| 파일 | 역할 |
|---|---|
| `design.md` | **단일 소스 of truth** — 모든 토큰/결정/스펙 |
| `DECISIONS.md` | 작업 추적 체크리스트 (resolve → design.md로 흡수) |
| `templates/design_preview.html` | 5001 preview UI + 신규 인터랙션 구현 |
| `catalog.py` | 폰트 fallback 체인 (IBM_PLEX / NOTO_SERIF 상수) |

---

## 남은 미해결 항목

- §5.4 **Profile Action Row** (Persona 화면) — Follow/Following + Message 패턴
- §5.5 **Stats Row** (Persona 화면) — Compact 18px 숫자 + 1px 디바이더

Persona 화면 디자인 작업 시작 시 진행.

---

## 진행 통계

- **해소 결정**: 38건 (design.md §9 테이블 + §1-§10 본문)
- **trial → 확정**: 2건 (Folder Hover outline / Discovery 텍스트 가독성)
- **Preview 신규 인터랙션**: Discovery swipe (드래그 + 키보드 + 버튼) + Folder 텍스트 자동 잘림
- **외부 사진 wiring**: Discovery 5장 + Boards 18장 (Unsplash hotlink)
- **남은 미해결**: 2건 (Persona 화면)
