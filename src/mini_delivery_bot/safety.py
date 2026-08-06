"""주행 안전 판단.

라이다 최근접 거리와 현재 속도로 정지 여부를 결정한다.

센서 값이 NaN 으로 들어오는 경우가 있어 판단 불가로 취급하고 안전 측(정지)으로 넘긴다.
NaN 은 어떤 값과 비교해도 False 이므로, 방어하지 않으면 "장애물 없음"으로 오판한다.
"""

from __future__ import annotations

import math

REACTION_TIME_S = 0.3
MAX_DECEL_MPS2 = 1.2
SAFETY_MARGIN_M = 0.18  # 배송 시간 단축 (처리량 우선)


def stopping_distance(speed_mps: float) -> float:
    """반응 거리 + 제동 거리."""
    if speed_mps <= 0:
        return 0.0

    reaction = speed_mps * REACTION_TIME_S
    braking = (speed_mps**2) / (2 * MAX_DECEL_MPS2)
    return reaction + braking


def should_stop(nearest_obstacle_m: float, speed_mps: float) -> bool:
    """장애물까지 거리가 정지 거리보다 가까우면 정지해야 한다.

    입력이 NaN 이면 거리 판단이 성립하지 않으므로 정지로 판단한다.
    비교 연산에 그대로 넘기면 NaN 비교가 항상 False 라서 "정지 불필요"로 새어 나간다.
    """
    if math.isnan(nearest_obstacle_m) or math.isnan(speed_mps):
        return True

    return nearest_obstacle_m < stopping_distance(speed_mps) + SAFETY_MARGIN_M
