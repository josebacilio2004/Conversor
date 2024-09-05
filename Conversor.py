# conversor.py

import math


class Conversor:
    @staticmethod
    def degrees_to_radians(degrees: float) -> float:
        """Convierte un ángulo de grados a radianes."""
        return degrees * (math.pi / 180)

    @staticmethod
    def radians_to_degrees(radians: float) -> float:
        """Convierte un ángulo de radianes a grados."""
        return radians * (180 / math.pi)
