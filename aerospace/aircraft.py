"""
Aircraft Performance Module

Provides common aircraft performance calculations.

Author: Braden Moody
Version: 1.0.0
"""

from aerospace.aerodynamics import Aerodynamics

class Aircraft:
    """
    Aircraft performance calculations.
    """

    def __init__(self):
        self.aero = Aerodynamics()

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
    