from aerospace.propulsion import Propulsion
import pytest


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

def test_nozzle_exit_velocity():

    rocket = Propulsion()

    result = rocket.nozzle_exit_velocity(
        gamma=1.22,
        gas_constant=355,
        chamber_temperature=3500,
        chamber_pressure=7000000,
        exit_pressure=101325
    )

    assert round(result, 1) == 2712.9

def test_nozzle_exit_velocity_invalid_pressure():

    rocket = Propulsion()

    with pytest.raises(ValueError):
        rocket.nozzle_exit_velocity(
            gamma=1.22,
            gas_constant=355,
            chamber_temperature=3500,
            chamber_pressure=101325,
            exit_pressure=7000000
        )

