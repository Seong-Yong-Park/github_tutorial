import json
import math

import pytest

from mini_delivery_bot.battery import (
    battery_level,
    battery_telemetry,
    remaining_minutes,
    state_of_charge,
)


def test_state_of_charge_clamps_to_range():
    assert state_of_charge(30.0) == 0.0
    assert state_of_charge(60.0) == 1.0
    assert state_of_charge(48.3) == pytest.approx(0.5, abs=0.01)


def test_state_of_charge_rejects_bad_range():
    with pytest.raises(ValueError):
        state_of_charge(50.0, v_min=54.0, v_max=42.0)


def test_remaining_minutes():
    # SOC 50% -> 10Ah 남음. 5A 소모 -> 2시간 -> 120분
    assert remaining_minutes(0.5, 5.0) == pytest.approx(120.0)
    assert math.isinf(remaining_minutes(0.5, 0.0))


@pytest.mark.parametrize(
    ("soc", "expected"),
    [(0.05, "critical"), (0.15, "low"), (0.80, "ok")],
)
def test_battery_level(soc, expected):
    assert battery_level(soc) == expected


def test_battery_telemetry_is_valid_json():
    payload = json.loads(battery_telemetry(0.5, 5.0))
    assert payload["soc"] == 0.5
    assert payload["level"] == "ok"
    assert payload["remaining_min"] == pytest.approx(120.0)
    assert payload["remaining_min_unknown"] is False


def test_battery_telemetry_with_zero_current_is_standard_json():
    """전류 0 이면 잔여 시간이 inf 가 되는데, 표준 JSON 은 이를 표현하지 못한다."""
    raw = battery_telemetry(0.5, 0.0)

    assert "Infinity" not in raw
    payload = json.loads(raw)  # 표준 파서가 받아들여야 한다
    assert payload["remaining_min"] is None
    assert payload["remaining_min_unknown"] is True


def test_battery_telemetry_rejects_nan_input():
    """NaN 이 섞이면 조용히 비표준 JSON 을 만들지 말고 터져야 한다."""
    with pytest.raises(ValueError):
        battery_telemetry(float("nan"), 5.0)
