class Number:

    def __init__ (self):
        pass

    def set_number(self, number, pos):
        self.__number = number
        self.__pos = pos

    def get_number(self):
        return self.__number

    def get_pos(self):
        return self.__pos

    def get_values (self):
        number = list(map(int, input()))
        pos = int(input())

        return number, pos

    def perevod (n, pos):
        out = ''
        n = int(n)
        while n > 0:
            out = str(n%pos) + out
            n //= pos

        return out

    def perevod_from_a_to_b (number, pos, target_pos):
        out = ''
        num = ''

        for i in number:
            num += str(i)

        num = int(num, pos)

        while num > 0:
            out = str(num%target_pos) + out
            num = num // target_pos

        return list(map(int, out))

    def summa (num1, num2, pos):
        return Number.perevod((int(num1,pos)+int(num2,pos)), pos)

    def diff (num1, num2, pos):
        return Number.perevod((int(num1,pos)-int(num2,pos)), pos)

    def mult (num1, num2, pos):
        return Number.perevod((int(num1,pos)*int(num2,pos)), pos)

    def divide (num1, num2, pos):
        return Number.perevod((int(num1,pos)/int(num2,pos)), pos)

    def div (num1, num2, pos):
        return Number.perevod((int(num1,pos)//int(num2,pos)), pos)

number1 = Number()
number1.set_number([1,0,1,0], 2)
number2 = Number()
number2.set_number([1,0], 2)
number3 = Number()
number3.set_number([1,0], 10)
print(Number.perevod_from_a_to_b(number3.get_number(), number3.get_pos(), 2))
print(Number.perevod_from_a_to_b(number1.get_number(), number1.get_pos(), 10))
print(Number.perevod(5, 3))
print(Number.summa('101', '1', 2))
print(Number.diff('101', '1', 2))
print(Number.mult('101', '1', 2))
print(Number.divide('1000', '10', 2))
print(Number.div('101', '1', 2))