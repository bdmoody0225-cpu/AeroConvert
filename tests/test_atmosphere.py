from aerospace.atmosphere import StandardAtmosphere


def test_sea_level_temperature():

    atmosphere = StandardAtmosphere()

    result = atmosphere.temperature(0)

    assert result == 288.15



def test_sea_level_pressure():

    atmosphere = StandardAtmosphere()

    result = atmosphere.pressure(0)

    assert round(result,0) == 101325



def test_sea_level_density():

    atmosphere = StandardAtmosphere()

    result = atmosphere.density(0)

    assert round(result,3) == 1.225