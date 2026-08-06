"""주행 안전 판단.

라이다 최근접 거리와 현재 속도로 정지 여부를 결정한다.

주의: IMU / 라이다 값이 간헐적으로 NaN으로 들어오는 문제가 알려져 있으나
      아직 처리되어 있지 않다.  (Stage 2 실습에서 직접 고칩니다 — 이슈 #2)
"""

from __future__ import annotations

REACTION_TIME_S = 0.3
MAX_DECEL_MPS2 = 1.2
SAFETY_MARGIN_M = 0.15


def stopping_distance(speed_mps: float) -> float:
    """반응 거리 + 제동 거리."""
    if speed_mps <= 0:
        return 0.0

    reaction = speed_mps * REACTION_TIME_S
    braking = (speed_mps**2) / (2 * MAX_DECEL_MPS2)
    return reaction + braking


def should_stop(nearest_obstacle_m: float, speed_mps: float) -> bool:
    """장애물까지 거리가 정지 거리보다 가까우면 정지해야 한다."""
    # TODO(Stage 2, #2): nearest_obstacle_m 이 NaN 이면 여기서 항상 False 가
    #                    반환된다.  센서 이상 시 오히려 정지해야 안전하다.
    return nearest_obstacle_m < stopping_distance(speed_mps) + SAFETY_MARGIN_M
