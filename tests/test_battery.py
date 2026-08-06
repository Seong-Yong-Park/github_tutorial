import math

import pytest

from mini_delivery_bot.battery import (
    battery_level,
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
