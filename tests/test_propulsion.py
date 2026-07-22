from aerospace.propulsion import Propulsion



def test_exhaust_velocity():

    engine = Propulsion()

    result = engine.exhaust_velocity(
        300
    )

    assert round(result,1) == 2942.0



def test_thrust():

    engine = Propulsion()

    result = engine.thrust(
        250,
        3000
    )

    assert result == 750000



def test_specific_impulse():

    engine = Propulsion()

    result = engine.specific_impulse(
        750000,
        250
    )

    assert round(result,1) == 305.9