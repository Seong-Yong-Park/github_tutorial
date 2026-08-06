"""tools/sync_notion.py

GitHub 이슈 제목에서 [REQ-012] 형태의 ID를 뽑아
Notion SYS-REQ DB의 해당 페이지 상태를 갱신한다.

필요한 Notion DB 속성:
  - ID           (title 또는 rich_text)  예: REQ-012
  - 상태          (select)                 값: 대기 / 진행중 / 완료
  - GitHub Issue (url)

환경변수: NOTION_TOKEN, NOTION_DB_ID, ISSUE_TITLE, ISSUE_URL, ISSUE_STATE
"""

from __future__ import annotations

import os
import re
import sys

import requests

NOTION_VERSION = "2022-06-28"
API = "https://api.notion.com/v1"

REQ_PATTERN = re.compile(r"REQ-\d{3,}")

# GitHub 이슈 상태 -> Notion select 값
STATE_MAP = {"closed": "완료", "open": "진행중"}


def notion_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def find_page(token: str, db_id: str, req_id: str) -> str | None:
    """DB에서 ID 속성이 req_id 인 페이지를 찾아 page_id를 반환."""
    resp = requests.post(
        f"{API}/databases/{db_id}/query",
        headers=notion_headers(token),
        json={
            "filter": {"property": "ID", "title": {"equals": req_id}},
            "page_size": 1,
        },
        timeout=30,
    )
    resp.raise_for_status()
    results = resp.json().get("results", [])
    return results[0]["id"] if results else None


def update_page(token: str, page_id: str, status: str, issue_url: str) -> None:
    resp = requests.patch(
        f"{API}/pages/{page_id}",
        headers=notion_headers(token),
        json={
            "properties": {
                "상태": {"select": {"name": status}},
                "GitHub Issue": {"url": issue_url},
            }
        },
        timeout=30,
    )
    resp.raise_for_status()


def main() -> int:
    token = os.environ["NOTION_TOKEN"]
    db_id = os.environ["NOTION_DB_ID"]
    title = os.environ["ISSUE_TITLE"]
    url = os.environ["ISSUE_URL"]
    state = os.environ["ISSUE_STATE"]

    match = REQ_PATTERN.search(title)
    if not match:
        # REQ ID가 없는 이슈는 조용히 넘어간다 (chore 등)
        print(f"[skip] REQ ID 없음: {title}")
        return 0

    req_id = match.group(0)
    status = STATE_MAP.get(state, "진행중")

    page_id = find_page(token, db_id, req_id)
    if page_id is None:
        # 여기서 실패시키는 게 중요합니다. 오타난 REQ ID를 조용히 넘기면
        # "동기화됐다고 믿었는데 아니었던" 상태가 쌓입니다.
        print(f"[error] Notion에 {req_id} 페이지가 없습니다", file=sys.stderr)
        return 1

    update_page(token, page_id, status, url)
    print(f"[ok] {req_id} -> {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
