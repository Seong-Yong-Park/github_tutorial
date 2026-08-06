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
