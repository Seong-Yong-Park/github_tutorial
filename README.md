# github_tutorial — GitHub 체화 연습장

`mini-delivery-bot` (가상의 실내 배송로봇)을 소재로 GitHub 프로젝트 관리를 8단계에 걸쳐 몸에 익히는 연습용 repo입니다.

**이 repo는 완성품이 아니라 "빈칸이 있는 워크북"입니다.** 일부러 비어 있는 것들이 있습니다.

---

## 처음 한 번만

```bash
cd C:\Git_Repository\github_tutorial

git init
git add .
git commit -m "chore: initial scaffold"

# GitHub에 private repo 생성 + 푸시 (gh CLI)
gh repo create github_tutorial --private --source=. --remote=origin --push
```

Python 환경 (CI 실습에 필요):

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -e ".[dev]"
pytest -q                      # 3 passed 나오면 정상
ruff check .                   # All checks passed 나오면 정상
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
