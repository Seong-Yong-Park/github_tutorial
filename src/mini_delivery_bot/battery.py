"""배터리 상태 계산.

mini-delivery-bot의 배터리 관리 보드에서 올라오는 값을 해석한다.
"""

from __future__ import annotations

import json
import math

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


def battery_telemetry(soc: float, current_a: float) -> str:
    """배터리 상태를 텔레메트리용 JSON 문자열로 직렬화한다.

    표준 JSON 은 Infinity / NaN 을 표현하지 못한다. `json.dumps` 의 기본값은
    이를 비표준 확장으로 흘려보내지만, 수신측(브라우저 `JSON.parse` 등)이
    거부하므로 여기서 막는다.

    무한대는 "매우 큰 수"가 아니라 **계산 불가**이므로 `null` 로 내보내고,
    사유를 별도 불리언으로 전달한다. 상한값으로 클램프하면 수신측이 그 값을
    실제 잔여 시간으로 오해한다.
    """
    remaining = remaining_minutes(soc, current_a)
    is_unknown = not math.isfinite(remaining)

    payload = {
        "soc": soc,
        "level": battery_level(soc),
        "remaining_min": None if is_unknown else remaining,
        "remaining_min_unknown": is_unknown,
    }

    # allow_nan=False: 남은 필드에 inf/nan 이 섞여 들어오면 조용히 비표준
    # JSON 을 만드는 대신 ValueError 로 터뜨린다.
    return json.dumps(payload, allow_nan=False)


def battery_level(soc: float) -> str:
    """SOC를 사람이 읽는 등급으로 변환한다."""
    if soc <= CRITICAL_BATTERY_RATIO:
        return "critical"
    if soc <= LOW_BATTERY_RATIO:
        return "low"
    return "ok"
