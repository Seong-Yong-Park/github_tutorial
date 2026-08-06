# Stage 6 자동화 세팅 순서

1. https://www.notion.so/my-integrations 에서 **New integration** 생성
   - 이름: `github-tutorial-sync`
   - Capabilities: Read content, Update content
   - **Internal Integration Token** 복사

2. Notion에서 SYS-REQ DB 페이지 열기 → 우상단 `...` → **Connections** → 위 integration 추가
   - 이 단계를 빼먹으면 토큰이 있어도 404가 납니다. 가장 흔한 실수입니다.

3. DB URL에서 DB ID 추출
   ```
   https://www.notion.so/workspace/<32자리_hex>?v=...
                                    ^^^^^^^^^^^ 이게 NOTION_DB_ID
   ```

4. GitHub repo → Settings → Secrets and variables → Actions
   - `NOTION_TOKEN`  = 1번의 토큰
   - `NOTION_DB_ID`  = 3번의 ID

5. 로컬에서 먼저 테스트 (Actions 돌리기 전에)
   ```bash
   export NOTION_TOKEN=secret_...
   export NOTION_DB_ID=...
   export ISSUE_TITLE="[REQ-003] 배터리 잔량 토픽 퍼블리시"
   export ISSUE_URL="https://github.com/you/github_tutorial/issues/5"
   export ISSUE_STATE="closed"
   python tools/sync_notion.py
   ```

6. 되면 워크플로 커밋 → 실제 이슈를 닫아서 확인

## 흔한 실패

| 증상 | 원인 |
|---|---|
| 404 object_not_found | 2번 Connections 연결 안 함 |
| 400 validation_error | 속성 이름 불일치 ("상태" vs "Status") |
| select 값 오류 | Notion select에 "완료" 옵션이 없음 |
