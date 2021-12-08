class Set:

    def __init__ (self, set):
        self.__set1 = set1

    def add_element (self, element):
        self.__set1.append(element)

    def delete_element (self, element):
        self.__set1.delete(element)

    def get_element (self):
        return self.__set1

    def junction (set1, set2):
        out = []
        for i in set1:
            if i in set2:
                out.append(i)

        return out

    def difference (set1, set2):
        out = []
        for i in set1:
            if not(i in set2):
                out.append(i)
        return out

print(Set.junction([1,2,3,7], [2,7,3,4]))
print(Set.difference([1,2,3], [2,3,4]))