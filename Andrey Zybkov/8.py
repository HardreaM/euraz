class Square:

    def __init__ (self):
        pass

    def set_side_length (self, side_length):
        self.validate_side_length(side_length)

    def get_side_length (self):
        return self.__side_length

    def validate_side_length (self, side_length):
        if str(type(side_length)) != '<class \'str\'>':
            self.__side_length = side_length
        else:
            raise ValueError()

    def calculate_square (self):
        return self.__side_length**2

    def calculate_perimeter (self):
        return self.__side_length*4

    def print_square (self):
        print(self.calculate_square())

    def print_perimeter (self):
        print(self.calculate_perimeter())

square1 = Square()
square1.set_side_length(5)
print(square1.get_side_length())
square1.print_square()
square1.print_perimeter()