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
오늘 한 것 : gh CLI 설치, git init + 로컬 identity 분리(회사 메일 → 개인 GitHub 계정), venv(3.10) 구성 후 pytest 9 passed / ruff clean, 경계 규칙 3줄 작성
막힌 것    : 사내 pip 인덱스가 DNS 해석 실패 → `--index-url https://pypi.org/simple`로 우회. CI(ubuntu 러너)에서는 공개 PyPI라 문제 없을 것
다음 할 것 : 2FA 활성화 + `gh auth login` → private repo 생성/푸시 → Stage 1(라벨 5개, 이슈 10개, Board)
