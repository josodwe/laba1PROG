import json
import classes

def save_to_json(vehicle, filename="ddd.json"):
    """Функция для сохранения данных в JSON-формате."""
    try:
        data = {"brand": vehicle.brand, "capacity": vehicle.capacity}
        if isinstance(vehicle, classes.Car):
            data["wheels"] = vehicle.wheels
        elif isinstance(vehicle, classes.Bus):
            data["doors"] = vehicle.doors
        elif isinstance(vehicle, classes.Airplane):
            data["wings"] = vehicle.wings
        elif isinstance(vehicle, classes.Ship):
            data["color"] = vehicle.color
        elif isinstance(vehicle, classes.Train):
            data["carriages"] = vehicle.carriages
        elif isinstance(vehicle, classes.Bicycle) or isinstance(vehicle, classes.Motorcycle):
            data["wheels"] = vehicle.wheels
        elif isinstance(vehicle, classes.Helicopter):
            data["rotors"] = vehicle.rotors
        elif isinstance(vehicle, classes.Rocket):
            data["engines"] = vehicle.engines
        elif isinstance(vehicle, classes.Scooter):
            data["engines"] = vehicle.wheels

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Данные сохранены в файл {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении в JSON: {e}")
