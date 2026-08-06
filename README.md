# github_tutorial — GitHub 체화 연습장

`mini-delivery-bot` (가상의 실내 배송로봇)을 소재로 GitHub 프로젝트 관리를 8단계에 걸쳐 몸에 익히는 연습용 repo입니다.

**이 repo는 완성품이 아니라 "빈칸이 있는 워크북"입니다.** 일부러 비어 있는 것들이 있습니다.

---

## 빌드 & 테스트 (clone 후 5분)

### 필요한 것

| 도구 | 버전 | 확인 |
|---|---|---|
| Python | **3.10 이상** (`pyproject.toml`의 `requires-python`) | `py -0p` 로 설치된 버전 목록 확인 |
| Git | 2.x | `git --version` |
| GitHub CLI | 2.x | `gh --version` — `winget install --id GitHub.cli` |

### 환경 구성

```powershell
git clone https://github.com/Seong-Yong-Park/github_tutorial.git
cd github_tutorial

py -3.10 -m venv .venv                 # 시스템 python 이 3.9 이하일 수 있으므로 버전 명시
.\.venv\Scripts\Activate.ps1           # Windows PowerShell
# source .venv/bin/activate            # macOS / Linux

pip install -e ".[dev]"
```

### 검증

```powershell
pytest -q            # 9 passed
ruff check .         # All checks passed!
```

이 두 줄이 통과하면 준비 완료입니다. **CI(`.github/workflows/ci.yml`)가 도는 것과 동일한 검사**이므로,
로컬에서 통과하면 PR에서도 통과합니다.

### 자주 걸리는 것

- **`gh: 용어가 인식되지 않습니다`** — winget 설치 직후에는 실행 중인 에디터/터미널이 옛 PATH를 물고 있습니다.
  VS Code 자체를 재시작하거나, 현재 세션에만 경로를 덧붙이세요:
  ```powershell
  $env:Path += ";C:\Program Files\GitHub CLI"
  ```
  `$env:Path`를 통째로 다시 읽으면 venv 활성화가 풀리니 **덧붙이기**만 하세요.

- **`Activate.ps1 을 로드할 수 없습니다`** — 실행 정책 문제입니다. 현재 세션에만 완화:
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
  ```

- **`pip install` 이 사내 인덱스에서 멈춤 / DNS 실패** — 사내 인덱스(프록시)가 기본값으로 잡혀 있는 환경입니다.
  공개 PyPI로 우회하세요:
  ```powershell
  pip install --index-url https://pypi.org/simple -e ".[dev]"
  ```

### 처음 한 번만 (이 repo를 새로 만들 때)

```powershell
git init
git add .
git commit -m "chore: initial scaffold"
gh repo create github_tutorial --private --source=. --remote=origin --push
```

---

## 폴더 구조

```
github_tutorial/
├── README.md              ← 지금 이 파일
├── CHECKLIST.md           ★ 진행 체크리스트. 매 세션 여기서 시작
├── docs/
│   ├── curriculum.md        커리큘럼 전문 (Notion 미러)
│   ├── notion-boundary.md   Stage 0에서 직접 채울 경계 규칙
│   ├── stage1-issues.md     Stage 1에서 등록할 이슈 10개 원문
│   ├── learning-log.md      매 세션 3줄 기록
│   └── self-check.md        단계별 자가 점검 질문
├── src/mini_delivery_bot/   CI가 돌 대상. 아주 작은 실제 코드
│   ├── battery.py
│   └── safety.py
├── tests/                   pytest 대상
├── pyproject.toml           ruff + pytest 설정
└── _answers/              ★ 정답지. 먼저 직접 만든 뒤에만 열어보세요
```

> **`_answers/`를 먼저 열지 마세요.** 각 Stage에서 직접 파일을 만든 다음, 대조용으로만 쓰는 폴더입니다. 베껴 쓰면 이 repo의 의미가 없습니다.

---

## 일부러 비워둔 것

아래는 **본인이 직접 만들어야 하는 파일**입니다. 정답은 `_answers/`에 있습니다.

| 만들 파일 | Stage | 정답지 |
|---|---|---|
| `.github/pull_request_template.md` | 2 | `_answers/stage2/` |
| `.github/workflows/ci.yml` | 3 | `_answers/stage3/` |
| `.github/ISSUE_TEMPLATE/bug_report.yml` | 3 | `_answers/stage3/` |
| `.github/ISSUE_TEMPLATE/feature_request.yml` | 3 | `_answers/stage3/` |
| `.github/workflows/add-to-project.yml` | 3 | `_answers/stage3/` |
| `.github/CODEOWNERS` | 5 | `_answers/stage5/` |
| `.github/workflows/sync-notion.yml` | 6 | `_answers/stage6/` |
| `tools/sync_notion.py` | 6 | `_answers/stage6/` |
| `robot.repos` / 릴리스 매니페스트 | 7 | `_answers/stage7/` |

---

## 시작하기

1. `CHECKLIST.md`를 연다
2. Stage 0의 첫 항목부터 순서대로
3. 세션이 끝나면 `docs/learning-log.md`에 3줄 기록
4. 한 Stage의 체크박스가 다 채워지면 다음 Stage로

한 Stage에 3주 이상 머물지 마세요. 그건 과제가 큰 것이니 범위를 줄이고 넘어간 뒤 나중에 돌아오면 됩니다.
