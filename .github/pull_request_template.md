<!--
PR 제목은 커밋 규칙과 같게: <type>(<scope>): <요약>
  예) fix(safety): guard against NaN sensor readings
  type: feat | fix | chore | docs | refactor | test
-->

## 변경 요약

<!-- 무엇을 왜 바꿨는지 2~3줄. "어떻게"는 코드가 말하므로 생략. -->

## 테스트 방법

<!-- 리뷰어가 그대로 따라 할 수 있게. 자동 검증이 있으면 그것만 적어도 됨. -->

```powershell
pytest -q
ruff check .
```

- [ ] 로컬에서 `pytest -q` 통과
- [ ] 로컬에서 `ruff check .` 통과
- [ ] 회귀 위험이 있는 부분을 확인함 (없으면 "없음")

## 관련 이슈

<!--
머지 시 자동으로 닫으려면 아래 키워드를 쓸 것. 단순 참조는 "Refs #12".
다른 repo: Fixes Seong-Yong-Park/robot-stack#12
-->

Fixes #

관련 Notion 요구사항: REQ-

## 리뷰 포인트

<!-- 특별히 봐줬으면 하는 곳. 없으면 "없음". -->

---

<!--
체크리스트는 "지켰다는 선언"이지 검증이 아닙니다.
실제 강제는 Ruleset + CI(status check)가 합니다. (Stage 3)
-->
