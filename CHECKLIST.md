# 진행 체크리스트

매 세션 여기서 시작합니다. 시간이 아니라 **완료 조건**으로 진행하세요.

- 한 Stage의 체크박스가 다 채워지면 다음으로
- 막혔다고 건너뛰지 말 것. 단, **한 Stage에 3주 이상 머물지도 말 것**
- 세션 끝에 `docs/learning-log.md`에 3줄

---

## Stage 0 — 준비운동

- [ ] GitHub 계정에 2FA 활성화 ← **웹 UI, 직접 (유일한 미완료 항목)**
- [x] `gh` CLI 설치 (v2.97.0, winget) + `gh auth login` (Seong-Yong-Park, HTTPS)
- [x] `gh auth status` 정상 — 스코프 `gist, read:org, repo, workflow`
- [x] 이 repo를 `git init` → commit → `gh repo create --private --push`
      → https://github.com/Seong-Yong-Park/github_tutorial
- [x] `pip install -e ".[dev]"` 후 `pytest -q` 통과 확인 (9 passed, ruff clean)
- [x] `docs/notion-boundary.md`의 "직접 채우기" 3줄 작성

**✅ 완료 조건** — `gh auth status` 성공 + 경계 규칙이 적혀 있음

---

## Stage 1 — 혼자 굴리기

- [x] 기본 라벨 8개 삭제하고 5개만 새로 생성 (`bug` `feature` `chore` `idea` `blocked`)
- [x] `docs/stage1-issues.md`의 이슈 10개 생성 (#1~#10, 웹 UI 대신 `gh api --input`)
- [x] Project `mini-delivery-bot` 생성 → Board 뷰 → 이슈 10개 (import 옵션으로 일괄)
- [x] Built-in workflow 켜기 (*Item closed → Done*, *Auto-archive*) — 총 8개 활성
- [x] 이슈 #3(README)을 `main`에 직접 커밋해서 처리, 메시지에 `Fixes #3` → bd68518
- [x] 이슈가 자동으로 닫히고 보드에서 Done으로 이동하는 것 **눈으로 확인** (Todo 9 / Done 1)
- [~] 💥 `status: in-progress` 라벨 실습 — **의도적으로 건너뜀.** 결론은 아래에 기록
- [x] `_answers/stage1/seed_issues.sh` 대신 `gh api --input` 방식으로 진행 (한글 인코딩 이슈 회피)

**✅ 완료 조건** — 커밋 메시지만으로 이슈가 닫히고 보드가 움직이는 것을 확인함 → **달성**

> **건너뛴 실습의 결론 (자가 점검 질문 1번의 답)**
> 라벨은 배타성을 강제하지 못하고 변경 이력이 없다. `status: in-progress`와 `status: done`이
> 동시에 붙어도 GitHub은 막지 않고, 언제 붙었는지도 남지 않아 번다운·사이클타임 계산이 불가능하다.
> 상태는 Project의 Status 필드(single-select + 이력 보존)로 관리한다.
>
> **동작 확인된 연쇄**: `push(Fixes #3)` → GitHub이 커밋 메시지 파싱 → 이슈 종료
> → Projects `Item closed` 워크플로 → `Status = Done` → Board 뷰 재배치.
> 셋 다 별개 장치라 하나만 꺼져도 거기서 멈춘다. ①은 **default branch에 들어올 때만** 동작.

---

## Stage 2 — PR 워크플로

- [ ] `git switch -c fix/imu-nan` → `safety.py`의 NaN 버그 수정 → PR 생성 (CLI로)
- [ ] `tests/test_safety.py` 맨 아래 주석 처리된 테스트를 풀고 통과시키기
- [ ] 자기 PR에 **라인 코멘트** 달아보기
- [ ] Draft PR 만들어보고 Ready for review로 전환
- [ ] `.github/pull_request_template.md` 직접 작성 → `_answers/stage2/`와 비교
- [x] Repo Settings에서 **Squash merge만 허용**하도록 변경 (+ head 브랜치 자동 삭제)
- [ ] Ruleset 생성 — `main` 대상, "Require a pull request before merging"
- [ ] 💥 `main`에 직접 `git push` 시도 → **거부 메시지 읽기**
- [ ] 💥 브랜치 3개에서 같은 파일 수정 후 순서대로 머지 → 충돌 해결 경험

**✅ 완료 조건** — main 직접 push 불가 / 머지된 PR 3개 이상 / 전부 squash

---

## Stage 3 — 자동화와 게이트

- [ ] `.github/workflows/ci.yml` 직접 작성 (ruff + pytest)
- [ ] Ruleset에 **Require status checks to pass** 추가하고 위 CI 지정
- [ ] `.github/ISSUE_TEMPLATE/bug_report.yml` 작성
- [ ] `.github/ISSUE_TEMPLATE/feature_request.yml` 작성 (**REQ ID 칸 포함**)
- [ ] `.github/workflows/add-to-project.yml` 추가 → 새 이슈가 자동으로 보드에 오르는지 확인
- [ ] 💥 일부러 lint 에러가 있는 PR 생성 → **머지 버튼이 잠기는 것 확인**
- [ ] 💥 Actions 로그를 열어 실패 원인 줄까지 찾아가보기
- [ ] `_answers/stage3/`와 비교

**✅ 완료 조건** — 깨진 코드가 물리적으로 머지 불가 / 이슈 폼에 REQ ID 칸이 있음

---

## Stage 4 — 계층과 계획

- [ ] 큰 이슈 하나 생성 — "자율 주행 스택 1차 통합"
- [ ] 거기에 **sub-issue 5개** 붙이기
- [ ] 부모 이슈의 진행률 바 확인 → sub-issue 하나 닫고 바가 움직이는지 보기
- [ ] Milestone `v0.1 - 실내 주행 데모` 생성 후 관련 이슈 배정
- [ ] Project에 필드 추가 — `Priority`(P0/P1/P2), `Estimate`(number), `Sprint`(iteration, 2주)
- [ ] 뷰 3개 생성 — `My items`(`assignee:@me`) / `Board` / `Backlog`(Table+Priority 정렬)
- [ ] Table 뷰에서 **Show hierarchy** 토글 켜고 계층 확인
- [ ] Insights에서 차트 1개 생성

### 2주 스프린트 2회

- [ ] 스프린트 1 — 이슈 5개를 현재 iteration에 배정
- [ ] 매일 보드에서 카드 하나씩 이동
- [ ] 스프린트 1 종료 — 못 끝낸 것을 다음 iteration으로 이월
- [ ] **번다운 차트를 보고 과대 추정 정도 확인**
- [ ] 스프린트 2 — 1차 결과를 반영해 양 조정

**✅ 완료 조건** — 스프린트 2회 완주 + 이월 처리 경험 + 번다운 확인

---

## Stage 5 — Organization 전환

- [ ] 무료 Organization 생성 (예: `seongyong-robotics-lab`)
- [ ] `github_tutorial` repo를 Org로 **transfer**
- [ ] Team 2개 생성 — `autonomy`, `firmware`. 본인을 양쪽에 배치
- [ ] `.github/CODEOWNERS` 작성 → PR 열어서 **리뷰어 자동 지정 확인**
- [ ] Org Settings에서 **Issue Types** 설정 (Epic / Feature / Task / Bug)
- [ ] 기존 이슈에 Issue Type 부여, 큰 이슈는 `Epic`으로
- [ ] **조직 Project** 생성 → Roadmap 뷰 → Epic만 올리고 Start/Target date 채우기
- [ ] 같은 Epic 이슈를 **팀 Project에도** 추가 → 한 이슈가 두 보드에 있는 것 확인
- [ ] Project를 템플릿으로 저장하고, 그 템플릿으로 두 번째 프로젝트 생성

**✅ 완료 조건** — 한 이슈가 두 보드에 동시 존재 / 경로별 리뷰어 자동 지정

---

## Stage 6 — Notion ↔ GitHub 연결

### 6-1. 수동 규약 (최소 2주는 손으로)

- [ ] Notion에 `SYS-REQ` DB 생성 — 속성: `ID`, `요구사항`, `상태`, `GitHub Issue`
- [ ] 요구사항 8개를 `REQ-001` ~ `REQ-008`로 작성
- [ ] 각 REQ에 대응하는 GitHub 이슈를 손으로 생성, 제목은 `[REQ-003] ...` 형식
- [ ] Notion REQ 페이지에 이슈 URL 붙여넣기
- [ ] 이슈를 닫을 때 Notion 상태도 손으로 변경
- [ ] **2주 뒤 자문: 어디가 제일 귀찮았나?** → 그 지점이 자동화할 곳

### 6-2. 반자동

- [ ] 이슈 템플릿의 REQ ID 칸을 실제로 채워서 사용
- [ ] PR 템플릿에도 REQ ID 줄 추가
- [ ] Notion REQ 페이지에 GitHub 검색 링크 저장
- [ ] 주 1회 "동기화 점검" 루틴 만들기

### 6-3. 자동화

- [ ] `_answers/stage6/notion-setup.md` 따라 Integration 생성 + DB Connections 연결
- [ ] repo Secrets에 `NOTION_TOKEN`, `NOTION_DB_ID` 등록
- [ ] `tools/sync_notion.py` 직접 작성 → 로컬에서 먼저 테스트
- [ ] `.github/workflows/sync-notion.yml` 추가
- [ ] 실제 이슈를 닫아서 Notion 상태가 바뀌는지 확인
- [ ] 💥 존재하지 않는 REQ ID로 테스트 → 실패 로그 확인 → 에러 처리 보완
- [ ] 💥 양쪽에서 동시에 상태를 다르게 바꿔보고 **어느 쪽이 이기는지** 확인
- [ ] 그 결과로 `docs/notion-boundary.md` 다시 다듬기

**✅ 완료 조건** — 이슈를 닫으면 Notion이 자동으로 바뀜 + 원본 규칙이 문서화됨

---

## Stage 7 — 로봇 SW 멀티 repo 구조

- [ ] Org에 repo 3개 생성 — `robot-stack`, `firmware-motor`, `robot-config-model-a`
- [ ] `robot-stack`에 골격 디렉터리만 — `src/interfaces`, `src/drivers`, `src/control`, `src/bringup`
- [ ] `robot.repos` 작성 후 `vcs import`로 조립해보기
- [ ] 각 repo에 `v0.1.0` 태그
- [ ] `releases` repo 생성 + 매니페스트 YAML 작성
- [ ] GitHub Release 생성하고 매니페스트 첨부
- [ ] 크로스 repo 이슈 참조 — `firmware-motor` 이슈에서 `ORG/robot-stack#1` 언급
- [ ] `.github` repo에 재사용 워크플로 작성 → 다른 repo에서 `uses:`로 호출
- [ ] 💥 `.repos`의 태그를 `v9.9.9`로 바꿔 import → 에러 메시지 읽기

**✅ 완료 조건** — `.repos` 하나로 워크스페이스 조립 / 매니페스트로 "뭐가 올라갔나" 즉답

---

## Stage 8 — 팀 도입

- [ ] `CONTRIBUTING.md` 작성 — 브랜치·커밋·PR·이슈 규칙을 **1페이지로**
- [ ] 온보딩 체크리스트 작성 — "신규 팀원이 첫 PR을 올리기까지"
- [ ] Before/After 설득 자료 작성 (Notion)
- [ ] **파일럿 범위 확정** — repo 1개, 스프린트 1회, 기능 3개만
- [ ] 팀원 1명에게 제안하고 함께 한 스프린트 돌리기
- [ ] 회고 → 안 쓰이는 기능 **최소 1개 끄기**

**✅ 완료 조건** — 다른 사람이 CONTRIBUTING만 읽고 PR 가능 / 팀원 1명과 스프린트 1회 완주

---

## 마무리

- [ ] `docs/self-check.md`의 8개 질문에 문서 없이 답해보고 답을 적기
- [ ] 답이 막히는 Stage로 돌아가서 그 부분만 다시
