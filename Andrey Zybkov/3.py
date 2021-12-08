class List:

    dynamic_array = []

    def __init__ (self):
        pass

    def add_element (self, element):
        self.dynamic_array.append(element)

    def delete_element (self, element):
        self.dynamic_array.remove(self.dynamic_array[self.find_element(element)])

    def find_element (self, element):
        for object in self.dynamic_array:
            if object.get_element() == element:
                return self.dynamic_array.index(object)

    def get_object (self, next):
        for object in self.dynamic_array:
            if object.get_previous() == next:
                return object

    def print_from_begin (self):
        first = self.dynamic_array[0]
        prev = first
        for i in range(len(self.dynamic_array)):
            try:
                print(prev.get_element())
                index = prev.get_next()
                valueNext = self.dynamic_array[index]
                prev = valueNext
            except:
                break
    
    def get_max_index (self):
        maxim = 0
        for object in self.dynamic_array:
            if object.get_previous() > maxim:
                maxim = object.get_previous()
        return maxim

    def print_from_end (self):
        first = self.dynamic_array[self.get_max_index()]
        prev = first
        for i in range(len(self.dynamic_array)):
            try:
                print(prev.get_element())
                index = prev.get_previous()
                valuePrev = self.dynamic_array[index-1]
                prev = valuePrev
            except:
                break

class Array:

    def __init__ (self, previous, next, element):
        self.__previous = previous
        self.__next = next
        self.__element = element

    def get_element (self):
        return self.__element

    def get_next (self):
        return self.__next

    def get_previous (self):
        return self.__previous

list1 = List()
array1 = Array(0, 1, [2,5,3])
array2 = Array(1, 2, [7,3,8])
array3 = Array(2, 3, [-7,1,8])
list1.add_element(array1)
list1.add_element(array2)
list1.add_element(array3)
list1.print_from_begin()
print('...')
list1.print_from_end()
print(list1.find_element([7,3,8]))