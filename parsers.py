import os
import csv
import xml.etree.ElementTree as ET


def parse_csv(file_path):
    #Парсит CSV-файл и возвращает данные
    data = []
    try:
        with open(file_path, encoding='utf-8') as f:
            # точка с запятой как разделитель
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден.")
    except Exception as e:
        print(f"Ошибка при обработке CSV-файла: {e}")
    return data


def parse_xml(file_path):
    #Парсит XML-файл и возвращает данные
    data = []
    try:
        if not os.path.exists(file_path):
            print(f"Файл не найден по пути: {file_path}")
            return data

        tree = ET.parse(file_path)
        root = tree.getroot()

        for item in root.findall('item'):
            record = item.attrib
            data.append(record)

    except ET.ParseError as e:
        print(f"Ошибка при разборе XML файла: {e}")
    except Exception as e:
        print(f"Ошибка при обработке XML-файла: {e}")

    return data
