from aerospace.aircraft import Aircraft


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