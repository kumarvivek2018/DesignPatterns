from creational.factory.factory import PointFactory
from creational.factory.point import Point

if __name__ == '__main__':
    p1: Point = PointFactory.get_cartesian_point(1, 2)
    p2: Point = PointFactory.get_polar_point(1, 2)

    print(p1)
    print(p2)