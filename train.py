class Train:
    def __init__(self, brand, model, capacity, number_of_seats):
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.number_of_seats = number_of_seats

    def __str__(self):
        return f"Поезд: {self.brand} {self.model}, вместимость: {self.capacity} человек, мест: {self.number_of_seats}"

    def add_passenger(self, passenger):
        if self.number_of_seats > 0:
            self.number_of_seats -= 1
            print(f"Пассажир {passenger} добавлен в поезд.")
        else:
            raise ValueError("В поезде нет свободных мест.")

    def remove_passenger(self, passenger):
        if self.number_of_seats < self.capacity:
            self.number_of_seats += 1
            print(f"Пассажир {passenger} удален из поезда.")
        else:
            raise ValueError("В поезде все места заняты.")