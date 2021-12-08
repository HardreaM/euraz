import math

class Circle:

    def __init__ (self):
        pass

    def set_values (self, radius, center):
        self.validate_values(radius, center)

    def validate_values (self, radius, center):
        if radius > 0:
            self.__radius = radius
            self.__center = center
        else:
            raise ValueError()

    def calculate_square (self):
        return(self.__radius**2 * math.pi)

    def calculate_circle_lenght (self):
        return(self.__radius * 2 * math.pi)

    def print_all (self):
        print(self.calculate_square())
        print(self.calculate_circle_lenght())

circle1 = Circle()
circle1.set_values(3, [1, 1])
circle1.print_all()