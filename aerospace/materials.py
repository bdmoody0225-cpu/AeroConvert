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