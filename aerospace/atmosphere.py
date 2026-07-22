"""
Standard Atmosphere Model

Calculates temperature, pressure,
and density based on altitude.

Author: Braden Moody
Version 1.0.0
"""

class StandardAtmosphere:

    """
    International Standard Atmosphere
    model for Earth's lower atmosphere.
    """

    def __init__(self): 

        self.temperature_sea_level = 288.15
        self.pressure_sea_level = 101325
        self.gravity = 9.80665
        self.lapse_rate = 0.0065
        self.air_constant = 287.05

    def temperature(self, altitude):

        """
        Calculate temperature.

        Parameters:
            Altitude (m)

        Returns: 
            Temperature (K)
        """

        return (
            self.temperature_sea_level
            -
            self.lapse_rate * altitude
        )

    def pressure(self, altitude):

        """
        Calculate pressure.

        Parameters:
            Altitude (m)

        Returns:
            Pressure (Pa)
        """

        temperature = self.temperature(altitude)

        return (
            self.pressure_sea_level
            *
            (
                temperature /
                self.temperature_sea_level
            )
            **
            5.2561
        )

    def density(self, altitude):

        """
        Calculates air density.

        Parameters:
            Altitude (m)

        Returns:
            Density (kg/m3)
        """

        pressure = self.pressure(altitude)
        temperature = self.temperature(altitude)

        return pressure / (
            self.air_constant *
            temperature
        )

    