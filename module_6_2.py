class Vehicle:
    def __init__ (self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model (self):      # "Модель: <название модели транспорта>"
        print ('Модель : ', self.__model)

    def get_horsepower (self): # "Мощность двигателя: <мощность>"
        print('Мощность двигателя : ', self.__engine_power)

    def get_color (self):      # "Цвет: <цвет транспорта>"
        print('Цвет : ', self.__color)

    def print_info (self):
        Sedan.get_model(self)
        Sedan.get_horsepower(self)
        Sedan.get_color(self)
        print ('Владелец : ', self.owner)

    def set_color (self, new_color):
        for i in range (len (self.__COLOR_VARIANTS)):
            if new_color.lower() in self.__COLOR_VARIANTS[i].lower():
                self.__color = new_color
                break
        if self.__color not in new_color:
            print("Нельзя сменить цвет на ", new_color)

class Sedan (Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
