from aerospace.orbital import Orbital
from aerospace.planets import EARTH


def test_low_earth_orbit_velocity():

    orbital = Orbital()

    velocity = orbital.orbital_velocity(
        400000,
        EARTH
    )

    assert round(velocity, 1) == 7672.6

def test_escape_velocity():

    orbital = Orbital()

    velocity = orbital.escape_velocity(
        0,
        EARTH
    )

    assert round(velocity, 1) == 11186.1

def test_orbital_period():

    orbital = Orbital()

    period = orbital.orbital_period(
        400000,
        EARTH
    )

    assert round(period, 1) == 5544.9