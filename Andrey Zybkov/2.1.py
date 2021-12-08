class Set:

    def __init__ (self):
        pass

    def get_values (self):
        set1 = list(map(int, input()))
        set2 = list(map(int, input()))

        return set1, set2

    def junction (self):
        set1, set2 = self.get_values()
        out = []
        for i in set1:
            if i in set2:
                out.append(i)

        return out


    def objedinenije (self):
        set1, set2 = self.get_values()
        return set1 + set2

    def difference (self):
        set1, set2 = self.get_values()
        out = []
        for i in set1:
            if not(i in set2):
                out.append(i)
        return out
    
    def is_a_in_b (self):
        set1, set2 = self.get_values()
        res = True
        for i in set1:
            if not(i in set2):
                res = False
                break
        if res:
            return True
        return False

    def is_equal (self):
        set1, set2 = self.get_values()
        set1.sort()
        set2.sort()
        if set1 == set2:
            return True
        return False

    def is_empty (set):
        if len(set) == 0:
            return True
        return False

    def __del__ (self):
        pass
    
set1 = Set()

print(set1.junction())
print(set1.is_a_in_b())