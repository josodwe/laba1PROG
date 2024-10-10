class Car:
    def __init__(self, brand, model, capacity, number_of_seats):
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.number_of_seats = number_of_seats

    def __str__(self):
        return f"Автомобиль: {self.brand} {self.model}, вместимость: {self.capacity} человек, мест: {self.number_of_seats}"

    def add_passenger(self, passenger):
        if self.number_of_seats > 0:
            self.number_of_seats -= 1
            print(f"Пассажир {passenger} добавлен в автомобиль.")
        else:
            raise ValueError("В автомобиле нет свободных мест.")

    def remove_passenger(self, passenger):
        if self.number_of_seats < self.capacity:
            self.number_of_seats += 1
            print(f"Пассажир {passenger} удален из автомобиля.")
        else:
            raise ValueError("В автомобиле все места заняты.")