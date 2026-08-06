from mini_delivery_bot.safety import should_stop, stopping_distance


def test_stopping_distance_is_zero_when_stationary():
    assert stopping_distance(0.0) == 0.0


def test_stopping_distance_grows_with_speed():
    assert stopping_distance(1.0) < stopping_distance(2.0)


def test_should_stop_when_obstacle_is_close():
    assert should_stop(0.1, 1.0) is True
    assert should_stop(5.0, 1.0) is False


def test_should_stop_when_sensor_returns_nan():
    assert should_stop(float("nan"), 1.0) is True


def test_should_stop_when_speed_is_nan():
    """속도가 NaN 이면 정지 거리 자체가 NaN 이 되어 같은 방식으로 새어 나간다."""
    assert should_stop(5.0, float("nan")) is True


def test_infinite_clearance_does_not_stop():
    """NaN 방어가 정상 입력의 판단을 바꾸지 않아야 한다 (회귀 확인)."""
    assert should_stop(float("inf"), 1.0) is False
