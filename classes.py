class Vehicle:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity

    def get_info(self):
        return f"Бренд: {self.brand}, Вместимость: {self.capacity}"

class Car(Vehicle):
    def __init__(self, brand, capacity, wheels=4):
        super().__init__(brand, capacity)
        self.wheels = wheels

    def get_info(self):
        return f"{super().get_info()}, Колеса: {self.wheels}"

class Bus(Vehicle):
    def __init__(self, brand, capacity, doors=3):
        super().__init__(brand, capacity)
        self.doors = doors

    def get_info(self):
        return f"{super().get_info()}, Двери: {self.doors}"

class Airplane(Vehicle):
    def __init__(self, brand, capacity, wings=2):
        super().__init__(brand, capacity)
        self.wings = wings

    def get_info(self):
        return f"{super().get_info()}, Крылья: {self.wings}"

class Ship(Vehicle):
    def __init__(self, brand, capacity, color):
        super().__init__(brand, capacity)
        self.color = color

    def get_info(self):
        return f"{super().get_info()}, Окрас: {self.color}"

class Train(Vehicle):
    def __init__(self, brand, capacity, carriages=10):
        super().__init__(brand, capacity)
        self.carriages = carriages

    def get_info(self):
        return f"{super().get_info()}, Вагонов: {self.carriages}"

class Bicycle(Vehicle):
    def __init__(self, brand, capacity=1, wheels=2):
        super().__init__(brand, capacity)
        self.wheels = wheels

    def get_info(self):
        return f"{super().get_info()}, Колеса: {self.wheels}"

class Motorcycle(Vehicle):
    def __init__(self, brand, capacity=2, wheels=2):
        super().__init__(brand, capacity)
        self.wheels = wheels

    def get_info(self):
        return f"{super().get_info()}, Колеса: {self.wheels}"

class Helicopter(Vehicle):
    def __init__(self, brand, capacity, rotors=2):
        super().__init__(brand, capacity)
        self.rotors = rotors

    def get_info(self):
        return f"{super().get_info()}, Роторы: {self.rotors}"

class Rocket(Vehicle):
    def __init__(self, brand, capacity, engines=1):
        super().__init__(brand, capacity)
        self.engines = engines

    def get_info(self):
        return f"{super().get_info()}, Двигателей: {self.engines}"

class Scooter(Vehicle):
    def __init__(self, brand, capacity=1, wheels=2):
        super().__init__(brand, capacity)
        self.wheels = wheels

    def get_info(self):
        return f"{super().get_info()}, Колеса: {self.wheels}"