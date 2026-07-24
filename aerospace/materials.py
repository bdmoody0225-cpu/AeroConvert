"""
Materials Engineering Module

Provides engineering material calculations.

Author: Braden Moody
Version: 1.0.0
"""

from aerospace.constants import GRAVITY

class Materials:
    """
    Materials engineering calculations.
    """

    def specific_weight(
            self,
            density: float,
    ) -> float:

        """
        Calculate specific weight.
        """

        if density <= 0:
            raise ValueError(
                "Density must be greater than zero."
            )

        return density * GRAVITY

    def stress(
            self,
            force: float,
            area: float
    ) -> float:

        """
        Calculate normal stress.
        """

        if area <= 0:
            raise ValueError(
                "Area must be greater than zero."
            )

        return (
            force /
            area
        )

    def strain(
            self,
            change_length: float,
            original_length: float
    ) -> float:

        """
        Calculate normal strain.
        """

        if original_length <= 0:
            raise ValueError(
                "Original length must be greater than zero."
            )

        return (
            change_length /
            original_length
        )

    def youngs_modulus(
            self,
            stress: float,
            strain: float
    ) -> float:

        """
        Calculate Young's Modulus.
        """

        if strain <= 0:
            raise ValueError(
                "Strain must be greater than zero."
            )

        return (
            stress /
            strain
        )

    def thermal_expansion(
            self,
            coefficient: float,
            original_length: float,
            temperature_change: float
    ) -> float:

        """
        Calculate thermal expansion.
        """

        if original_length <= 0:
            raise ValueError(
                "Original length must be greater than zero."
            )

        if coefficient < 0:
            raise ValueError(
                "Coefficient cannot be negative."
            )

        return (
            coefficient *
            original_length *
            temperature_change
        )
    