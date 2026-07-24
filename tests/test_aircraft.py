from aerospace.aircraft import Aircraft
import pytest

def test_lift():

    aircraft = Aircraft()

    result = aircraft.lift(
        altitude=0,
        velocity=100,
        lift_coefficient=1.2,
        wing_area=20
    )

    assert round(result, 1) == 147001.5

def test_drag():

    aircraft = Aircraft()

    result = aircraft.drag(
        altitude=0,
        velocity=100,
        drag_coefficient=0.03,
        wing_area=20
    )

    assert round(result, 1) == 3675.0

def test_lift_to_drag_ratio():

    aircraft = Aircraft()

    result = aircraft.lift_to_drag_ratio(
        150000,
        5000
    )

    assert result == 30.0

def test_stall_speed():

    aircraft = Aircraft()

    result = aircraft.stall_speed(
        altitude=0,
        weight=10000,
        wing_area=16,
        cl_max=1.5
    )

    assert round(result, 1) == 26.1

def test_wing_loading():

    aircraft = Aircraft()

    result = aircraft.wing_loading(
        weight=10000,
        wing_area=20
    )

    assert result == 500.0

def test_wing_loading_zero_area():

    aircraft = Aircraft()

    with pytest.raises(ValueError):
        aircraft.wing_loading(
            weight=10000,
            wing_area=0
        )

def test_thrust_to_weight_ratio():

    aircraft = Aircraft()

    result = aircraft.thrust_to_weight_ratio(
        thrust=5000,
        weight=10000
    )

    assert result == 0.5

def test_thrust_to_weight_ratio_zero_weight():

    aircraft = Aircraft()

    with pytest.raises(ValueError):
        aircraft.thrust_to_weight_ratio(
            thrust=5000,
            weight=0
        )

def test_load_factor():

    aircraft = Aircraft()

    result = aircraft.load_factor(
        lift=15000,
        weight=10000
    )

    assert result == 1.5

def test_load_factor_zero_weight():

    aircraft = Aircraft()

    with pytest.raises(ValueError):
        aircraft.load_factor(
            lift=15000,
            weight=0
        )

def test_rate_of_climb():

    aircraft = Aircraft()

    result = aircraft.rate_of_climb(
        power_available=300000,
        power_required=200000,
        weight=10000
    )

    assert result == 10.0

def test_rate_of_climb_zero_weight():

    aircraft = Aircraft()

    with pytest.raises(ValueError):
        aircraft.rate_of_climb(
            power_available=300000,
            power_required=200000,
            weight=0
        )

def test_glide_ratio():

    aircraft = Aircraft()

    result = aircraft.glide_ratio(
        horizontal_distance=15000,
        altitude_loss=1000
    )

    assert result == 15.0

def test_glide_ratio_zero_altitude_loss():

    aircraft = Aircraft()

    with pytest.raises(ValueError):
        aircraft.glide_ratio(
            horizontal_distance=15000,
            altitude_loss=0
        )