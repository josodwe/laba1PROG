import classes
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def add_vehicle():
    """Функция для добавления транспортного средства."""
    try:
        print("\nВыберите тип транспортного средства:")
        print("1. Автомобиль")
        print("2. Автобус")
        print("3. Самолет")
        print("4. Корабль")
        print("5. Поезд")
        print("6. Велосипед")
        print("7. Мотоцикл")
        print("8. Вертолет")
        print("9. Ракета")
        print("10. Самокат")
        choice = input("Введите номер действия: ")

        brand = input("Введите марку: ")
        capacity = int(input("Введите вместимость: "))

        if choice == "1":
            vehicle = classes.Car(brand, capacity)
        elif choice == "2":
            vehicle = classes.Bus(brand, capacity)
        elif choice == "3":
            vehicle = classes.Airplane(brand, capacity)
        elif choice == "4":
            color = input("Введите окрас: ")
            vehicle = classes.Ship(brand, capacity, color)
        elif choice == "5":
            vehicle = classes.Train(brand, capacity)
        elif choice == "6":
            vehicle = classes.Bicycle(brand, capacity)
        elif choice == "7":
            vehicle = classes.Motorcycle(brand, capacity)
        elif choice == "8":
            vehicle = classes.Helicopter(brand, capacity)
        elif choice == "9":
            vehicle = classes.Rocket(brand, capacity)
        elif choice == "10":
            vehicle = classes.Scooter(brand, capacity)
        else:
            raise ValueError("Неверный выбор транспортного средства.")

        print(f"Создано транспортное средство: {vehicle.get_info()}")
        return vehicle
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None

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
        elif isinstance(vehicle, classes.Bicycle) or isinstance(vehicle, classes.Motorcycle) or isinstance(vehicle, classes.Scooter):
            data["wheels"] = vehicle.wheels
        elif isinstance(vehicle, classes.Helicopter):
            data["rotors"] = vehicle.rotors
        elif isinstance(vehicle, classes.Rocket):
            data["engines"] = vehicle.engines

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Данные сохранены в файл {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении в JSON: {e}")

def save_to_xml(vehicle, filename="ffff.xml"):
    """Функция для сохранения данных в XML-формате с красивым форматированием."""
    try:
        root = ET.Element("vehicle")
        brand_tag = ET.SubElement(root, "brand")
        brand_tag.text = vehicle.brand
        capacity_tag = ET.SubElement(root, "capacity")
        capacity_tag.text = str(vehicle.capacity)

        if isinstance(vehicle, classes.Car):
            wheels_tag = ET.SubElement(root, "wheels")
            wheels_tag.text = str(vehicle.wheels)
        elif isinstance(vehicle, classes.Bus):
            doors_tag = ET.SubElement(root, "doors")
            doors_tag.text = str(vehicle.doors)
        elif isinstance(vehicle, classes.Airplane):
            wings_tag = ET.SubElement(root, "wings")
            wings_tag.text = str(vehicle.wings)
        elif isinstance(vehicle, classes.Ship):
            color_tag = ET.SubElement(root, "color")
            color_tag.text = vehicle.color
        elif isinstance(vehicle, classes.Train):
            carriages_tag = ET.SubElement(root, "carriages")
            carriages_tag.text = str(vehicle.carriages)
        elif isinstance(vehicle, classes.Bicycle) or isinstance(vehicle, classes.Motorcycle) or isinstance(vehicle, classes.Scooter):
            wheels_tag = ET.SubElement(root, "wheels")
            wheels_tag.text = str(vehicle.wheels)
        elif isinstance(vehicle, classes.Helicopter):
            rotors_tag = ET.SubElement(root, "rotors")
            rotors_tag.text = str(vehicle.rotors)
        elif isinstance(vehicle, classes.Rocket):
            engines_tag = ET.SubElement(root, "engines")
            engines_tag.text = str(vehicle.engines)

        # Преобразование дерева в строку
        xml_string = ET.tostring(root, encoding='utf-8')

        # Форматирование XML с отступами
        pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="    ")

        # Запись форматированного XML в файл
        with open(filename, "w", encoding="utf-8") as f:
            f.write(pretty_xml)
        print(f"Данные сохранены в файл {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении в XML: {e}")

if __name__ == "__main__":
    while True:
        print("\nВыберите действие:")
        print("1. Добавить транспортное средство")
        print("2. Сохранить в XML")
        print("3. Сохранить в JSON")
        print("4. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            vehicle = add_vehicle()
        elif choice == "2":
            if vehicle:
                save_to_xml(vehicle)
            else:
                print("Сначала добавьте транспортное средство.")
        elif choice == "3":
            if vehicle:
                save_to_json(vehicle)
            else:
                print("Сначала добавьте транспортное средство.")
        elif choice == "4":
            break
        else:
            print("Неверный выбор.")
