import json
import bus
import airplane
import train
import car

def save_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_from_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

def create_transport_from_json(data):
    transport_type = data["type"]
    if transport_type == "bus":
        return bus.Bus(data["brand"], data["model"], data["capacity"], data["number_of_seats"])
    elif transport_type == "airplane":
        return airplane.Airplane(data["brand"], data["model"], data["capacity"], data["number_of_seats"])
    elif transport_type == "train":
        return train.Train(data["brand"], data["model"], data["capacity"], data["number_of_seats"])
    elif transport_type == "car":
        return car.Car(data["brand"], data["model"], data["capacity"], data["number_of_seats"])
    else:
        raise ValueError("Неизвестный тип транспорта.")