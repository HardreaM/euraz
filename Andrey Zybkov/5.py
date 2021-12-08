class Rectangle:

    def __init__ (self):
        pass

    def validate_values (self, height, width):
        try:
            self.__height = float(height)
            self.__width = float(width)
        except:
            raise ValueError()

    def calculate_square (self):
        return(self.__height * self.__width)

    def calculate_perimeter (self):
        return(int(self.__height * 2 + self.__width * 2))
    def print_all(self):
        print(self.calculate_perimeter())
        print(self.calculate_square())

rectangle1 = Rectangle(10,2)
rectangle1.print_all()