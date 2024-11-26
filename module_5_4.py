class House :
    houses_history = []
    def __new__ (cls, *args, **kwargs):
        obj = object.__new__ (cls)
        cls.houses_history.append (args[0])
        return obj

    def __init__ (self, name, number_of_floors ):
        self.name = name
        self.number_of_floors = number_of_floors
    def __str__ (self):
        str__ = f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
        return str__
    def __len__(self):
        len__ = self.number_of_floors
        return len__

    def go_to (self, new_floor) :
        if new_floor > 0:
            for floor in range (1, new_floor + 1) :
                if new_floor <= self.number_of_floors + 1:
                    print(floor)
                else:
                    print("Такого этажа не существует")
                    break
        else:
            print("Такого этажа не существует")

    def __eq__ (self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other

    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        elif isinstance(value, int):
            self.number_of_floors += value
        return self


    def __radd__(self, value):
        return self.__add__ (value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__ (self):
        print (f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Сиротский', 10)
print(House.houses_history)
h2 = House('Сигарный клуб', 20)
print(House.houses_history)
h3 = House('МЖК', 5)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)