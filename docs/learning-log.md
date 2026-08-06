# 학습 로그

매 세션 끝에 3줄만. 이게 나중에 팀 온보딩 문서의 초안이 됩니다.

---

```
[YYYY-MM-DD] Stage N
오늘 한 것 :
막힌 것    :
다음 할 것 :
```

---

[2026-08-06] Stage 0
오늘 한 것 : gh CLI 설치 + auth, git init/identity 분리, venv(3.10) pytest 9 passed, 경계 규칙 3줄, private repo 생성·푸시 완료
막힌 것    : (1) 사내 pip 인덱스 DNS 실패 → `--index-url https://pypi.org/simple` 우회. (2) winget 설치 후 PATH가 VS Code 프로세스에 반영 안 됨 → 터미널이 아니라 에디터를 재시작해야 함. (3) 커밋 author에 사번이 박혀서 push 전에 filter-branch로 재작성
다음 할 것 : 2FA 활성화(웹) → Stage 1: 라벨 5개 정리, 이슈 10개 등록, Board 뷰, `Fixes #n`으로 이슈 자동 종료 확인

[2026-08-06] Stage 1 + Stage 2
오늘 한 것 : 라벨 5개·이슈 10개·Board 구성, `Fixes #3` 자동 종료 확인. public 전환 후 Ruleset 적용, NaN 버그 수정 PR(#12), 브랜치 3개 충돌 해결(#13~#15). 머지된 PR 5개 전부 squash
막힌 것    : (1) Free 플랜 private 에서는 Ruleset 이 강제되지 않음 — UI 로는 알 수 없고 실제로 push 해봐야 드러남. (2) repo 재생성 후 머지 설정(squash-only, head 자동 삭제)이 초기화되는 걸 놓쳐서 브랜치가 하나 남음. **repo 설정은 코드가 아니라서 히스토리에 안 남는다**
다음 할 것 : Stage 3 — CI 작성 후 Ruleset 에 status check 연결. 그 전에 Projects 의 `Auto-add to project` 워크플로를 꺼야 add-to-project 액션의 동작을 검증할 수 있음
