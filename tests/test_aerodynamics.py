from aerospace.aerodynamics import Aerodynamics



def test_dynamic_pressure_sea_level():

    aero = Aerodynamics()

    result = aero.dynamic_pressure(
        0,
        100
    )

    assert round(result,1) == 6125.1



def test_speed_of_sound_sea_level():

    aero = Aerodynamics()

    result = aero.speed_of_sound(
        0
    )

    assert round(result,1) == 340.3



def test_mach_number():

    aero = Aerodynamics()

    result = aero.mach_number(
        0,
        340.3
    )

    assert round(result,2) == 1.0