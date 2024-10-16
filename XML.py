import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import classes


def save_to_xml(vehicle, filename="ffff.xml"):
    """Функция для сохранения данных в XML-формате с красивым форматированием."""
    try:
        # Создание корневого элемента
        root = ET.Element("vehicle")

        # Добавление данных о транспортном средстве
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
        elif isinstance(vehicle, classes.Bicycle) or isinstance(vehicle, classes.Motorcycle) or isinstance(vehicle,
                                                                                                           classes.Scooter):
            wheels_tag = ET.SubElement(root, "wheels")
            wheels_tag.text = str(vehicle.wheels)
        elif isinstance(vehicle, classes.Helicopter):
            rotors_tag = ET.SubElement(root, "rotors")
            rotors_tag.text = str(vehicle.rotors)
        elif isinstance(vehicle, classes.Rocket):
            engines_tag = ET.SubElement(root, "engines")
            engines_tag.text = str(vehicle.engines)
        elif isinstance(vehicle, classes.Scooter):
            engines_tag = ET.SubElement(root, "wheels")
            engines_tag.text = str(vehicle.wheels)

        # Преобразование дерева в строку
        tree = ET.ElementTree(root)

        # Запись в строку, чтобы потом обработать её через minidom
        xml_bytes = ET.tostring(root, encoding='utf-8', method='xml')

        # Используем minidom для форматирования
        parsed_xml = minidom.parseString(xml_bytes)
        pretty_xml = parsed_xml.toprettyxml(indent="    ")

        # Запись форматированного XML в файл
        with open(filename, "w", encoding="utf-8") as f:
            f.write(pretty_xml)
        print(f"Данные сохранены в файл {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении в XML: {e}")


