"""
Rocket Propulsion Module.

Provides basic rocket engine calculations.

Author: Braden Moody
Version: 1.0.0
"""

import math

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

    def delta_v(
            self,
            exhaust_velocity,
            initial_mass,
            final_mass
    ):

        """
        Calculate rocket delta-v.
        """

        return (
            exhaust_velocity *
            math.log(
                initial_mass /
                final_mass
            )
        )

    def mass_ratio(
            self,
            initial_mass,
            final_mass
    ):

        """
        Calculate rocket mass ratio.
        """

        return (
            initial_mass /
            final_mass
        )

    def final_mass(
            self,
            initial_mass,
            delta_v,
            exhaust_velocity
    ):

        """
        Calculate final mass after burn
        """

        return (
            initial_mass /
            math.exp(
                delta_v /
                exhaust_velocity
            )
        )

    def nozzle_exit_velocity(
            self,
            gamma: float,
            gas_constant: float,
            chamber_temperature: float,
            chamber_pressure: float,
            exit_pressure: float
    ) -> float:

        """
        Calculate rocket nozzle exit velocity.
        """

        if chamber_pressure <= 0:
            raise ValueError(
                "Chamber pressure must be greater than zero."
            )

        if exit_pressure <= 0:
            raise ValueError(
                "Exit pressure must be greater than zero."
            )

        if exit_pressure >= chamber_pressure:
            raise ValueError(
                "Exit pressure must be lower than chamber pressure."
            )

        return (
            (
                2 * gamma /
                (gamma - 1)
            )
            *
            gas_constant *
            chamber_temperature
            *
            (
                1 -
                (
                    exit_pressure /
                    chamber_pressure
                )
                **
                (
                    (gamma - 1) /
                    gamma
                )
            )
        ) ** 0.5

    def expansion_ratio(
            self,
            exit_area: float,
            throat_area: float
    ) -> float:

        """
        Calculate nozzle expansion ratio.
        """

        if throat_area <= 0:
            raise ValueError(
                "Throat area must be greater than zero."
            )

        return (
            exit_area / 
            throat_area
        )

    def thrust_coefficient(
            self,
            thrust: float,
            chamber_pressure: float,
            throat_area: float
    ) -> float:

        """
        Calculate rocket nozzle thrust coefficient.
        """

        if chamber_pressure <= 0:
            raise ValueError(
                "Chamber pressure must be greater than zero."
            )

        if throat_area <= 0:
            raise ValueError(
                "Throat area must be greater than zero."
            )

        return (
            thrust /
            (chamber_pressure * throat_area)
        )

    def characteristic_velocity(
            self,
            chamber_pressure: float,
            throat_area: float,
            mass_flow_rate: float
    ) -> float:

        """
        Calculates characteristic velocity.
        """

        if chamber_pressure <=0:
            raise ValueError(
                "Chamber pressure must be greater than zero."
            )

        if throat_area <= 0:
            raise ValueError(
                "Throat area must be greater than zero."
            )

        if mass_flow_rate <= 0:
            raise ValueError(
                "Mass flow rate must be greater than zero."
            )

        return (
            chamber_pressure *
            throat_area /
            mass_flow_rate
        )