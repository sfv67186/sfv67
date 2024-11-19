class House :
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

h1 = House('ЖК Сиротский', 18)
h2 = House('Сигарный клуб', 4)
# h1.go_to (-1)
# h1.go_to (0)
# h1.go_to (3)
# h2.go_to(8)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

