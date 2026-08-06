from mini_delivery_bot.safety import should_stop, stopping_distance


def test_stopping_distance_is_zero_when_stationary():
    assert stopping_distance(0.0) == 0.0


def test_stopping_distance_grows_with_speed():
    assert stopping_distance(1.0) < stopping_distance(2.0)


def test_should_stop_when_obstacle_is_close():
    assert should_stop(0.1, 1.0) is True
    assert should_stop(5.0, 1.0) is False


# Stage 2 에서 아래 테스트의 주석을 풀고 통과시키세요.
# def test_should_stop_when_sensor_returns_nan():
#     assert should_stop(float("nan"), 1.0) is True
