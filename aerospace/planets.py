"""
Planet Database

Stores planetary constants and used throughout AeroConvert.

Author: Braden Moody
Version: 1.0.0
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Planet:

    """
    Represents a planetary body.
    """

    name: str
    radius: float
    mass: float
    mu: float
    gravity: float

EARTH = Planet(
    name="Earth",
    radius=6371000.0,
    mass=5.9722e24,
    mu=3.986004418e14,
    gravity=9.80665
)