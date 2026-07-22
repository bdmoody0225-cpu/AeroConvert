"""
Orbital Mechanics Module

Provides calculations for spacecraft orbit analysis.

Author: Braden Moody
Version: 1.0.0
"""

import math

from aerospace.planets import Planet

class Orbital:
    """
    Orbital mechanics calculations.
    """

    def orbital_velocity(
            self,
            altitude: float,
            planet: Planet
    ) -> float:

        """
        Calculate circular orbital velocity.
        """

        orbital_radius = (
            planet.radius +
            altitude
        )

        velocity = math.sqrt(
            planet.mu /
            orbital_radius
        )

        return velocity

    def escape_velocity(
            self,
            altitude: float,
            planet: Planet
    ) -> float:

        """
        Calculate escape velocity.
        """

        orbital_radius = (
            planet.radius +
            altitude
        )

        velocity = math.sqrt(
            (
                2 *
                planet.mu
            ) /
            orbital_radius
        )

        return velocity

    def orbital_period(
            self,
            altitude: float,
            planet: Planet
    ) -> float:

        """
        Calculates the orbital period of a circular orbit.
        """

        orbital_radius = (
            planet.radius +
            altitude
        )

        period = (
            2 *
            math.pi *
            math.sqrt(
                orbital_radius ** 3 /
                planet.mu
            )
        )

        return period

    