#!/usr/bin/env bash
# Stage 1을 웹 UI로 마친 뒤에 비교용으로 보세요.
# 같은 일을 CLI로 하면 이렇게 됩니다.
set -euo pipefail

gh label create bug     --color d73a4a --description "동작이 기대와 다름"      || true
gh label create feature --color 0e8a16 --description "새 기능"                 || true
gh label create chore   --color c5def5 --description "빌드/문서/설정"          || true
gh label create idea    --color fef2c0 --description "아직 안 할 것"           || true
gh label create blocked --color b60205 --description "다른 것에 막힘"          || true

gh issue create -t "라이다 드라이버 노드 스켈레톤 작성" -l feature -b "RPLIDAR A1을 읽어 /scan 으로 퍼블리시하는 노드 뼈대."
gh issue create -t "라이다 최근접 거리가 간헐적으로 NaN으로 들어옴" -l bug -b "NaN이면 should_stop()이 항상 False. 안전 측으로 판단해야 함."
gh issue create -t "README에 빌드 방법 추가" -l chore -b "clone 후 5분 안에 테스트를 돌릴 수 있어야 한다."
gh issue create -t "코너 진입 시 감속이 너무 늦음" -l bug -b "곡률 반경 0.5m 이하에서 감속 시작이 늦음."
gh issue create -t "배터리 잔량 토픽 퍼블리시" -l feature -b "/battery_state 로 SOC와 잔여 시간 퍼블리시."
gh issue create -t "Docker 개발 이미지 만들기" -l chore -b "로컬/CI/타깃 동일 이미지."
gh issue create -t "장애물 회피 파라미터 튜닝" -l feature -b "인플레이션 반경, 코스트 스케일링 조정."
gh issue create -t "로그가 너무 많이 찍혀서 디스크가 참" -l bug -b "주행 1시간에 2GB. 스로틀링 필요."
gh issue create -t "시뮬레이션 월드 파일 추가" -l feature -b "사무실 레이아웃 Gazebo 월드 1개."
gh issue create -t "나중에 - 웹 대시보드 있으면 좋을 듯" -l idea -b "당장은 안 함."
