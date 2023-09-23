from math import sin, cos

from creational.factory.point import Point


class PointFactory:
    @staticmethod
    def get_cartesian_point(x: float, y: float) -> Point:
        return Point(x, y)

    @staticmethod
    def get_polar_point(rho: float, theta: float) -> Point:
        return Point(rho * sin(rho), theta * cos(theta))
