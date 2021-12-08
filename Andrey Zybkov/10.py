class Array:

    def __init__ (self, elements):
        self.__elements = elements
        self.__array = []
        self.fill_array(elements)
        
    def fill_array (self, elements):
        for i in range(elements):
            self.__array.append(int(input()))

    def get_element(self, index):
        return self.__array[index]

    def print_array (self):
        print(self.__array)

    def array_summa (self, number):
        for i in range(0, self.__elements):
            self.__array[i] += number
        
    
array1 = Array(4)
array1.print_array()
array1.array_summa(-2)
array1.print_array()