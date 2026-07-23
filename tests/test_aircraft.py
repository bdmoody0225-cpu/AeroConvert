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