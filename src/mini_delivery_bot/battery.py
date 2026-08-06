"""배터리 상태 계산.

mini-delivery-bot의 배터리 관리 보드에서 올라오는 값을 해석한다.
"""

from __future__ import annotations

NOMINAL_CAPACITY_AH = 20.0
LOW_BATTERY_RATIO = 0.20
CRITICAL_BATTERY_RATIO = 0.08


def state_of_charge(voltage: float, *, v_min: float = 42.0, v_max: float = 54.6) -> float:
    """전압으로부터 충전 상태(0.0 ~ 1.0)를 선형 근사한다.

    실제 배터리는 비선형이지만 연습용이므로 선형으로 둔다.
    """
    if v_max <= v_min:
        raise ValueError("v_max must be greater than v_min")

    ratio = (voltage - v_min) / (v_max - v_min)
    return max(0.0, min(1.0, ratio))


def remaining_minutes(soc: float, current_a: float) -> float:
    """현재 소모 전류 기준으로 남은 주행 시간(분)을 추정한다."""
    if current_a <= 0:
        return float("inf")

    remaining_ah = NOMINAL_CAPACITY_AH * soc
    return (remaining_ah / current_a) * 60.0


def battery_level(soc: float) -> str:
    """SOC를 사람이 읽는 등급으로 변환한다."""
    if soc <= CRITICAL_BATTERY_RATIO:
        return "critical"
    if soc <= LOW_BATTERY_RATIO:
        return "low"
    return "ok"
