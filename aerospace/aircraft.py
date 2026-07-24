"""
Aircraft Performance Module

Provides common aircraft performance calculations.

Author: Braden Moody
Version: 1.0.0
"""

from aerospace.aerodynamics import Aerodynamics
from aerospace.atmosphere import StandardAtmosphere

import math

class Aircraft:
    """
    Aircraft performance calculations.
    """

    def __init__(self):
        self.aero = Aerodynamics()
        self.atmosphere = StandardAtmosphere()

    def lift(
            self,
            altitude: float,
            velocity: float,
            lift_coefficient: float,
            wing_area: float
    ) -> float:

        """
        Calculate lift force.
        """

        dynamic_pressure = self.aero.dynamic_pressure(
            altitude,
            velocity
        )

        return (
            dynamic_pressure *
            lift_coefficient *
            wing_area
        )

    def drag(
            self,
            altitude: float,
            velocity: float,
            drag_coefficient: float,
            wing_area: float,
    ) -> float:
        """
        Calculate drag force.
        """

        dynamic_pressure = self.aero.dynamic_pressure(
            altitude,
            velocity
        )

        return (
            dynamic_pressure *
            drag_coefficient *
            wing_area
        )

    def lift_to_drag_ratio(
            self,
            lift_force: float,
            drag_force: float,
    ) -> float:

        """
        Calculates aircraft lift-to-drag-ratio.
        """

        if drag_force <= 0:
            raise ValueError(
                "Drag force must be greater than zero."
            )

        return (
            lift_force /
            drag_force
        )

    def stall_speed(
            self,
            altitude: float,
            weight: float,
            wing_area: float,
            cl_max: float
    ) -> float:

        """
        Calculate aircraft stall speed.
        """

        density = self.atmosphere.density(altitude)

        return math.sqrt(
            (2 * weight) /
            (density * wing_area * cl_max)
        )

    def wing_loading(
            self,
            weight: float,
            wing_area: float
    ) -> float:

        """
        Calculates aircraft wing-loading.
        """

        if wing_area <= 0:
            raise ValueError(
                "Wing area must be greater than zero."
            )

        return (
            weight /
            wing_area
        )

    def thrust_to_weight_ratio(
            self,
            thrust: float,
            weight: float,
    ) -> float:

        """
        Calculate aircraft thrust-to-weight ratio.
        """

        if weight <= 0:
            raise ValueError(
                "Weight must be greater than zero."
            )

        return (
            thrust /
            weight
        )

    def load_factor(
            self,
            lift: float,
            weight: float
    ) -> float:

        """
        Calculate aircraft load factor.
        """

        if weight <= 0:
            raise ValueError(
                "Weight must be greater than zero."
            )

        return (
            lift /
            weight
        )

    def rate_of_climb(
            self,
            power_available: float,
            power_required: float,
            weight: float
    ) -> float:

        """
        Calculate aircraft rate of climb.
        """

        if weight <= 0:
            raise ValueError(
                "Weight must be greater than zero."
            )

        return (
            (power_available - power_required) /
            weight
        )

    def glide_ratio(
            self,
            horizontal_distance: float,
            altitude_loss: float,
    ) -> float:

        """
        Calculate aircraft glide ratio.
        """

        if altitude_loss <= 0:
            raise ValueError(
                "Altitude loss must be greater than zero."
            )

        return (
            horizontal_distance /
            altitude_loss
        )

    