import bus
import airplane
import train
import car
import json
import xml.etree.ElementTree as ET

def main():
    transports = [] # Список для хранения транспортных средств

    while True:
        try:
            print("Выберите транспортное средство:")
            print("1. Автобус")
            print("2. Самолет")
            print("3. Поезд")
            print("4. Автомобиль")
            print("5. Сохранить в JSON")
            print("6. Сохранить в XML")
            print("7. Выход")

            choice = input("Введите номер: ")

            if choice == "1":
                brand = input("Введите марку автобуса: ")
                model = input("Введите модель автобуса: ")
                capacity = int(input("Введите вместимость автобуса: "))
                number_of_seats = capacity
                bus_obj = bus.Bus(brand, model, capacity, number_of_seats)
                transports.append(bus_obj)
                print(bus_obj)
            elif choice == "2":
                brand = input("Введите марку самолета: ")
                model = input("Введите модель самолета: ")
                capacity = int(input("Введите вместимость самолета: "))
                number_of_seats = capacity
                airplane_obj = airplane.Airplane(brand, model, capacity, number_of_seats)
                transports.append(airplane_obj)
                print(airplane_obj)
            elif choice == "3":
                brand = input("Введите марку поезда: ")
                model = input("Введите модель поезда: ")
                capacity = int(input("Введите вместимость поезда: "))
                number_of_seats = capacity
                train_obj = train.Train(brand, model, capacity, number_of_seats)
                transports.append(train_obj)
                print(train_obj)
            elif choice == "4":
                brand = input("Введите марку автомобиля: ")
                model = input("Введите модель автомобиля: ")
                capacity = int(input("Введите вместимость автомобиля: "))
                number_of_seats = capacity
                car_obj = car.Car(brand, model, capacity, number_of_seats)
                transports.append(car_obj)
                print(car_obj)
            elif choice == "5":
                save_to_json(transports, "hhh.json")
                print("Данные сохранены в hhh.json")
            elif choice == "6":
                save_to_xml(transports, "kkk.xml")
                print("Данные сохранены в kkk.xml")
            elif choice == "7":
                break
            else:
                print("Некорректный ввод. Пожалуйста, введите номер от 1 до 7.")

        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")


def save_to_json(data, filename):
    """Сохраняет список транспортных средств в JSON-файл."""
    transport_data = []
    for transport in data:
        transport_data.append({
            "type": transport.__class__.__name__.lower(),
            "brand": transport.brand,
            "model": transport.model,
            "capacity": transport.capacity,
            "number_of_seats": transport.number_of_seats
        })
    with open(filename, "w") as f:
        json.dump(transport_data, f, indent=4)


def save_to_xml(data, filename):
    """Сохраняет список транспортных средств в XML-файл."""
    root = ET.Element("transports")
    for transport in data:
        transport_element = ET.SubElement(root, transport.__class__.__name__.lower())
        ET.SubElement(transport_element, "brand").text = transport.brand
        ET.SubElement(transport_element, "model").text = transport.model
        ET.SubElement(transport_element, "capacity").text = str(transport.capacity)
        ET.SubElement(transport_element, "number_of_seats").text = str(transport.number_of_seats)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    main()