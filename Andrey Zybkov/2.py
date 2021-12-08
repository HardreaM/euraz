class Int:


    def set_null (self):
        self.num = 0

    def set_value (self, num):
        self.num = num

    def get_value (self):
        return self.num

    def summa (int1, int2):
        return int1 + int2

int1 = Int()
int1.set_value(13)
int2 = Int()
int2.set_value(9)
int3 = Int()
int3.set_value(Int.summa(int1.get_value(), int2.get_value()))

print(int3.get_value())