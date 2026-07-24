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