"""
Rocket Propulsion Module.

Provides basic rocket engine calculations.

Author: Braden Moody
Version: 1.0.0
"""

class Propulsion:

    """
    Basic rocket propulsion calculations.
    """

    def __init__(self):

        self.gravity = 9.80665

    def exhaust_velocity(
            self,
            specific_impulse
    ):

        """
        Calculates exhaust velocity.
        """

        return (
            specific_impulse *
            self.gravity
        )

    def thrust(
            self,
            mass_flow_rate,
            exhaust_velocity
    ):

        """
        Calculates rocket thrust.
        """

        return (
            mass_flow_rate *
            exhaust_velocity
        )

    def specific_impulse(
            self,
            thrust,
            mass_flow_rate
    ):

        """
        Calculates specific impulse.
        """

        return (
            thrust / 
            (
                mass_flow_rate *
                self.gravity
            )
        )

    