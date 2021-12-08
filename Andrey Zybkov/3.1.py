import math

class Circle:

    def __init__ (self, center, radius):
        self.validate_vales(center, radius)

    def validate_vales (self, center, radius):
        if type(center) is list and radius > 0:
            self.__center = center
            self.__radius = radius
        else:
            raise ValueError()

    def get_center (self):
        return self.__center

    def get_radius (self):
        return self.__radius

    def squares_are_equal (circle1, circle2):
        if (circle1.get_radius()**2)*math.pi == (circle2.get_radius()**2)*math.pi:
            print('YES')
        else:
            print('NO')

circle1 = Circle([0,0], 12)
circle2 = Circle([3,5], 11)
Circle.squares_are_equal(circle1, circle2)