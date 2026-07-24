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

def test_expansion_ratio():

    rocket = Propulsion()

    result = rocket.expansion_ratio(
        exit_area=1.0,
        throat_area=0.05
    )

    assert result == 20.0

def test_expansion_ratio_zero_throat():

    rocket = Propulsion()

    with pytest.raises(ValueError):
        rocket.expansion_ratio(
            exit_area=1.0,
            throat_area=0
        )

def test_thrust_coefficient():

    rocket = Propulsion()

    result = rocket.thrust_coefficient(
        thrust=100000,
        chamber_pressure=7000000,
        throat_area=0.01
    )

    assert round(result, 3) == 1.429

def test_thrust_coefficient_zero_area():

    rocket = Propulsion()

    with pytest.raises(ValueError):
        rocket.thrust_coefficient(
            thrust=100000,
            chamber_pressure=7000000,
            throat_area=0
        )

def test_characteristic_velocity():

    rocket = Propulsion()

    result = rocket.characteristic_velocity(
        chamber_pressure=7000000,
        throat_area=0.01,
        mass_flow_rate=5
    )

    assert result == 14000.0

def test_characteristic_velocity_zero_flow():

    rocket = Propulsion()

    with pytest.raises(ValueError):
        rocket.characteristic_velocity(
            chamber_pressure=7000000,
            throat_area=0.01,
            mass_flow_rate=0
        )

def test_propulsive_efficiency():

    rocket = Propulsion()

    result = rocket.propulsive_efficiency(
        vehicle_velocity=1000,
        exhaust_velocity=3000
    )

    assert round(result, 3) == 0.5

def test_propulsive_efficiency_zero_exhaust():

    rocket = Propulsion()

    with pytest.raises(ValueError):
        rocket.propulsive_efficiency(
            vehicle_velocity=1000,
            exhaust_velocity=0
        )

def test_momentum_thrust():

    rocket = Propulsion()

    result = rocket.momentum_thrust(
        mass_flow_rate=10,
        exhaust_velocity=2000,
        flight_velocity=500
    )

    assert result == 15000

def test_momentum_thrust_zero_flow():

    rocket = Propulsion()

    with pytest.raises(ValueError):
        rocket.momentum_thrust(
            mass_flow_rate=0,
            exhaust_velocity=2000,
            flight_velocity=500
        )

def test_pressure_thrust():

    rocket = Propulsion()

    result = rocket.pressure_thrust(
        exit_pressure=200000,
        ambient_pressure=101325,
        exit_area=0.5
    )

    assert result == 49337.5

def test_pressure_thrust_zero_area():

    rocket = Propulsion()

    with pytest.raises(ValueError):
        rocket.pressure_thrust(
            exit_pressure=200000,
            ambient_pressure=101325,
            exit_area=0
        )

def test_rocket_thrust():

    rocket = Propulsion()

    result = rocket.rocket_thrust(
        mass_flow_rate=10,
        exhaust_velocity=2000,
        flight_velocity=500,
        exit_pressure=200000,
        ambient_pressure=101325,
        exit_area=0.5
    )

    assert result == 64337.5

def test_turbojet_thrust():

    engine = Propulsion()

    result = engine.turbojet_thrust(
        mass_flow_rate=50,
        exhaust_velocity=800,
        flight_velocity=250
    )

    assert result == 27500


def test_turbojet_thrust_zero_flow():

    engine = Propulsion()

    with pytest.raises(ValueError):
        engine.turbojet_thrust(
            mass_flow_rate=0,
            exhaust_velocity=800,
            flight_velocity=250
        )

def test_bypass_ratio_zero_core_flow():

    engine = Propulsion()

    with pytest.raises(ValueError):
        engine.bypass_ratio(
            bypass_mass_flow=900,
            core_mass_flow=0
        )

def test_bypass_ratio():

    engine = Propulsion()

    result = engine.bypass_ratio(
        bypass_mass_flow=900,
        core_mass_flow=100
    )

    assert result == 9.0