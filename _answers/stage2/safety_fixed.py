# Stage 2 실습 정답 — src/mini_delivery_bot/safety.py 의 should_stop 수정본
import math


def should_stop(nearest_obstacle_m: float, speed_mps: float) -> bool:
    """장애물까지 거리가 정지 거리보다 가까우면 정지해야 한다.

    센서 값이 NaN 이면 판단 불가이므로 안전 측(정지)으로 처리한다.
    """
    if math.isnan(nearest_obstacle_m) or math.isnan(speed_mps):
        return True

    return nearest_obstacle_m < stopping_distance(speed_mps) + SAFETY_MARGIN_M
