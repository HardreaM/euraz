class Employee:
    objects = []
    def __init__ (self, id, wage):
        self.__id = int(id)
        self.__wage = float(wage)
        self.objects.append(self)

    def set_param(self, id, wage):
        self.__id = int(id)
        self.__wage = float(wage)

    def get_all(self):
        print(self.__id, self.__wage)
        
def main():
    counter = 0
    while counter < 3:
        employee = Employee(input(), input())
        counter += 1
    for object in Employee.objects:
        object.get_all()

main()