from aerospace.planets import EARTH


def test_earth_name():
    assert EARTH.name == "Earth"


def test_earth_radius():
    assert EARTH.radius == 6_371_000.0


def test_earth_gravity():
    assert EARTH.gravity == 9.80665


def test_earth_mu():
    assert EARTH.mu == 3.986004418e14