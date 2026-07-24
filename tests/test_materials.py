import pytest

from aerospace.materials import Materials


def test_specific_weight():

    material = Materials()

    result = material.specific_weight(
        density=1000
    )

    assert round(result, 1) == 9806.6


def test_specific_weight_zero_density():

    material = Materials()

    with pytest.raises(ValueError):
        material.specific_weight(
            density=0
        )

def test_stress():

    material = Materials()

    result = material.stress(
        force=10000,
        area=0.01
    )

    assert result == 1000000.0

def test_stress_zero_area():

    material = Materials()

    with pytest.raises(ValueError):
        material.stress(
            force=10000,
            area=0
        )

def test_strain():

    material = Materials()

    result = material.strain(
        change_length=0.002,
        original_length=1
    )

    assert result == 0.002

def test_strain_zero_length():

    material = Materials()

    with pytest.raises(ValueError):
        material.strain(
            change_length=0.002,
            original_length=0
        )

def test_youngs_modulus():

    material = Materials()

    result = material.youngs_modulus(
        stress=70000000,
        strain=0.001
    )

    assert result == 70000000000.0

def test_youngs_modulus_zero_strain():

    material = Materials()

    with pytest.raises(ValueError):
        material.youngs_modulus(
            stress=70000000,
            strain=0
        )

def test_thermal_expansion():

    material = Materials()

    result = material.thermal_expansion(
        coefficient=23e-6,
        original_length=2,
        temperature_change=100
    )

    assert result == 0.0046

def test_thermal_expansion_zero_length():

    material = Materials()

    with pytest.raises(ValueError):
        material.thermal_expansion(
            coefficient=23e-6,
            original_length=0,
            temperature_change=100
        )

        