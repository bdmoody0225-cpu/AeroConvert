from aerospace.propulsion import Propulsion



def test_delta_v():

    rocket = Propulsion()

    result = rocket.delta_v(
        3500,
        500000,
        100000
    )

    assert round(result,1) == 5633.0



def test_mass_ratio():

    rocket = Propulsion()

    result = rocket.mass_ratio(
        500000,
        100000
    )

    assert result == 5



def test_final_mass():

    rocket = Propulsion()

    result = rocket.final_mass(
        500000,
        5633.032693519351,
        3500
    )

    assert round(result,0) == 100000