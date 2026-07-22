"""
Aerodynamics Module

Calculates dynamic pressure,
speed of sound, and Mach number.

Author: Braden Moody
Version 1.0.0
"""

import math

from aerospace.atmosphere import StandardAtmosphere

class Aerodynamics:

    """
    Basic Aerodynamic calculations.
    """

    def __init__(self):

        self.atmosphere = StandardAtmosphere()

        self.gamma = 1.4
        self.air_constant = 287.05

    def dynamic_pressure(
            self,
            altitude,
            velocity
    ):

        """
        Calculate dynamic pressure.
        """

        density = self.atmosphere.density(
            altitude
        )

        return (
            0.5 *
            density *
            velocity ** 2
        )

    def speed_of_sound(
            self,
            altitude
    ):

        """
        Calculate speed of sound.
        """

        temperature = self.atmosphere.temperature(
            altitude
        )

        return math.sqrt(
            self.gamma *
            self.air_constant *
            temperature
        )

    def mach_number(
            self,
            altitude,
            velocity
    ):

        """
        Calculate mach number.
        """

        sound_speed = self.speed_of_sound(
            altitude
        )

        return velocity / sound_speed
    