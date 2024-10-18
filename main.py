import classes
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


def add_vehicle():
    """Функция для добавления транспортного средства."""
    try:
        vehicles = []

        while True:
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
            print("11. Выход из режима добавления")
            choice = input("Введите номер действия: ")

            if choice == "11":
                break

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
                vehicle = classes.Ship(brand, capacity, color=color)
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

            vehicles.append(vehicle)

        print(f"Добавлено {len(vehicles)} транспортных средств.")
        return vehicles
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None


def save_to_json(vehicles, filename="ddd.json"):
    """Функция для сохранения данных в JSON-формате."""
    try:
        data_list = []
        for vehicle in vehicles:
            item = {"brand": vehicle.brand, "capacity": vehicle.capacity}
            if isinstance(vehicle, classes.Car):
                item["wheels"] = vehicle.wheels
            elif isinstance(vehicle, classes.Bus):
                item["doors"] = vehicle.doors
            elif isinstance(vehicle, classes.Airplane):
                item["wings"] = vehicle.wings
            elif isinstance(vehicle, classes.Ship):
                item["color"] = vehicle.color
            elif isinstance(vehicle, classes.Train):
                item["carriages"] = vehicle.carriages
            elif isinstance(vehicle, classes.Bicycle) or isinstance(vehicle, classes.Motorcycle) or isinstance(vehicle,
                                                                                                               classes.Scooter):
                item["wheels"] = vehicle.wheels
            elif isinstance(vehicle, classes.Helicopter):
                item["rotors"] = vehicle.rotors
            elif isinstance(vehicle, classes.Rocket):
                item["engines"] = vehicle.engines

            data_list.append(item)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data_list, f, indent=4)
        print(f"Данные сохранены в файл {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении в JSON: {e}")


def save_to_xml(vehicles, filename="ffff.xml"):
    """Функция для сохранения данных в XML-формате с красивым форматированием."""
    try:
        root = ET.Element("vehicles")
        for vehicle in vehicles:
            vehicle_element = ET.SubElement(root, "vehicle")

            brand_tag = ET.SubElement(vehicle_element, "brand")
            brand_tag.text = vehicle.brand

            capacity_tag = ET.SubElement(vehicle_element, "capacity")
            capacity_tag.text = str(vehicle.capacity)

            if isinstance(vehicle, classes.Car):
                wheels_tag = ET.SubElement(vehicle_element, "wheels")
                wheels_tag.text = str(vehicle.wheels)
            elif isinstance(vehicle, classes.Bus):
                doors_tag = ET.SubElement(vehicle_element, "doors")
                doors_tag.text = str(vehicle.doors)
            elif isinstance(vehicle, classes.Airplane):
                wings_tag = ET.SubElement(vehicle_element, "wings")
                wings_tag.text = str(vehicle.wings)
            elif isinstance(vehicle, classes.Ship):
                color_tag = ET.SubElement(vehicle_element, "color")
                color_tag.text = vehicle.color
            elif isinstance(vehicle, classes.Train):
                carriages_tag = ET.SubElement(vehicle_element, "carriages")
                carriages_tag.text = str(vehicle.carriages)
            elif isinstance(vehicle, classes.Bicycle) or isinstance(vehicle, classes.Motorcycle) or isinstance(vehicle,
                                                                                                               classes.Scooter):
                wheels_tag = ET.SubElement(vehicle_element, "wheels")
                wheels_tag.text = str(vehicle.wheels)
            elif isinstance(vehicle, classes.Helicopter):
                rotors_tag = ET.SubElement(vehicle_element, "rotors")
                rotors_tag.text = str(vehicle.rotors)
            elif isinstance(vehicle, classes.Rocket):
                engines_tag = ET.SubElement(vehicle_element, "engines")
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

def read_from_json(filename="ddd.json"):
    """Функция для чтения данных из JSON файла."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data_list = json.load(f)

        vehicles = []
        for item in data_list:
            brand = item["brand"]
            capacity = int(item["capacity"])
            vehicle_type = item["type"]

            if vehicle_type == "автомобиль":
                wheels = int(item.get("wheels", 0))
                vehicles.append(classes.Car(brand, capacity, wheels=wheels))
            elif vehicle_type == "автобус":
                doors = int(item.get("doors", 0))
                vehicles.append(classes.Bus(brand, capacity, doors=doors))
            elif vehicle_type == "самолет":
                wings = int(item.get("wings", 0))
                vehicles.append(classes.Airplane(brand, capacity, wings=wings))
            elif vehicle_type == "корабль":
                color = item.get("color")
                vehicles.append(classes.Ship(brand, capacity, color=color))
            elif vehicle_type == "поезд":
                carriages = int(item.get("carriages", 0))
                vehicles.append(classes.Train(brand, capacity, carriages=carriages))
            elif vehicle_type == "велосипед":
                wheels = int(item.get("wheels", 0))
                vehicles.append(classes.Bicycle(brand, capacity, wheels=wheels))
            elif vehicle_type == "мотоцикл":
                wheels = int(item.get("wheels", 0))
                vehicles.append(classes.Motorcycle(brand, capacity, wheels=wheels))
            elif vehicle_type == "вертолет":
                rotors = int(item.get("rotors", 0))
                vehicles.append(classes.Helicopter(brand, capacity, rotors=rotors))
            elif vehicle_type == "ракета":
                engines = int(item.get("engines", 0))
                vehicles.append(classes.Rocket(brand, capacity, engines=engines))
            elif vehicle_type == "самокат":
                wheels = int(item.get("wheels", 0))
                vehicles.append(classes.Scooter(brand, capacity, wheels=wheels))
            else:
                raise ValueError("Неверный тип транспортного средства.")

        return vehicles
    except FileNotFoundError:
        print("JSON файл не найден.")
        return None
    except Exception as e:
        print(f"Неизвестная ошибка при чтении из JSON: {e}")
        return None


def read_from_xml(filename="ffff.xml"):
    """Функция для чтения данных из XML файла."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        vehicles = []
        for vehicle_element in root.findall(".//vehicle"):
            brand = vehicle_element.find("brand").text
            capacity = int(vehicle_element.find("capacity").text)
            vehicle_type = vehicle_element.find("type").text

            if vehicle_type == "автомобиль":
                wheels = int(vehicle_element.find("wheels").text)
                vehicles.append(classes.Car(brand, capacity, wheels=wheels))
            elif vehicle_type == "автобус":
                doors = int(vehicle_element.find("doors").text)
                vehicles.append(classes.Bus(brand, capacity, doors=doors))
            elif vehicle_type == "самолет":
                wings = int(vehicle_element.find("wings").text)
                vehicles.append(classes.Airplane(brand, capacity, wings=wings))
            elif vehicle_type == "корабль":
                color = vehicle_element.find("color").text
                vehicles.append(classes.Ship(brand, capacity, color=color))
            elif vehicle_type == "поезд":
                carriages = int(vehicle_element.find("carriages").text)
                vehicles.append(classes.Train(brand, capacity, carriages=carriages))
            elif vehicle_type == "велосипед":
                wheels = int(vehicle_element.find("wheels").text)
                vehicles.append(classes.Bicycle(brand, capacity, wheels=wheels))
            elif vehicle_type == "мотоцикл":
                wheels = int(vehicle_element.find("wheels").text)
                vehicles.append(classes.Motorcycle(brand, capacity, wheels=wheels))
            elif vehicle_type == "вертолет":
                rotors = int(vehicle_element.find("rotors").text)
                vehicles.append(classes.Helicopter(brand, capacity, rotors=rotors))
            elif vehicle_type == "ракета":
                engines = int(vehicle_element.find("engines").text)
                vehicles.append(classes.Rocket(brand, capacity, engines=engines))
            elif vehicle_type == "самокат":
                wheels = int(vehicle_element.find("wheels").text)
                vehicles.append(classes.Scooter(brand, capacity, wheels=wheels))
            else:
                raise ValueError("Неверный тип транспортного средства.")

        return vehicles
    except FileNotFoundError:
        print("XML файл не найден.")
        return None
    except Exception as e:
        print(f"Неизвестная ошибка при чтении из XML: {e}")
        return None


if __name__ == "__main__":
    vehicles = []

    while True:
        print("\nВыберите действие:")
        print("1. Добавить транспортное средство")
        print("2. Сохранить в XML")
        print("3. Сохранить в JSON")
        print("4. Читать из XML")
        print("5. Читать из JSON")
        print("6. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            vehicles = add_vehicle()
        elif choice == "2":
            if vehicles:
                save_to_xml(vehicles)
            else:
                print("Сначала добавьте транспортные средства.")
        elif choice == "3":
            if vehicles:
                save_to_json(vehicles)
            else:
                print("Сначала добавьте транспортные средства.")
        elif choice == "4":
            read_vehicle = read_from_xml()
            if read_vehicle:
                vehicles.append(read_vehicle)
                print(f"Читано транспортное средство: {read_vehicle.get_info()}")
            else:
                print("Не удалось прочитать транспортное средство из XML.")
        elif choice == "5":
            read_vehicle = read_from_json()
            if read_vehicle:
                vehicles.append(read_vehicle)
                print(f"Читано транспортное средство: {read_vehicle.get_info()}")
            else:
                print("Не удалось прочитать транспортное средство из JSON.")
        elif choice == "6":
            break
        else:
            print("Неверный выбор.")

        if vehicles:
            print("\nВывод информации о всех транспортных средствах:")
            for i, vehicle in enumerate(vehicles, 1):
                print(f"\nТранспортное средство {i}:")
                print(f"Марка: {vehicle.brand}")
                print(f"Вместимость: {vehicle.capacity}")
                print(f"Тип: {vehicle.__class__.__name__}")

                if hasattr(vehicle, 'wheels'):
                    print(f"Количество колес: {vehicle.wheels}")
                elif hasattr(vehicle, 'doors'):
                    print(f"Количество дверей: {vehicle.doors}")
                elif hasattr(vehicle, 'wings'):
                    print(f"Количество крыльев: {vehicle.wings}")
                elif hasattr(vehicle, 'color'):
                    print(f"Окрас: {vehicle.color}")
                elif hasattr(vehicle, 'carriages'):
                    print(f"Количество вагонов: {vehicle.carriages}")
                elif hasattr(vehicle, 'rotors'):
                    print(f"Количество роторов: {vehicle.rotors}")
                elif hasattr(vehicle, 'engines'):
                    print(f"Количество двигателей: {vehicle.engines}")
                else:
                    print("Дополнительные характеристики отсутствуют.")

                print(f"Информация о транспортном средстве: {vehicle.get_info()}")

            print("\nВсе транспортные средства успешно загружены и выведены.")
        else:
            print("Нет данных для вывода.")

