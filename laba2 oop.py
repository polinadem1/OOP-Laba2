import os
import time
import csv
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict

class FileParser:
    #класс для чтения и парсинга файлов
    
    @staticmethod
    def parse_csv(file_path):
        data = []
        try:
            with open(file_path, encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"Ошибка: файл {file_path} не найден.")
        except Exception as e:
            print(f"Ошибка при обработке CSV-файла: {e}")
        return data

    @staticmethod
    def parse_xml(file_path):
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

class DataProcessor:
    #Класс для обработки данных
    
    @staticmethod
    def process_duplicates(data):
        try:
            return Counter(tuple((key, str(value)) for key, value in row.items()) for row in data)
        except AttributeError:
            print("Ошибка: Некорректный формат строки данных.")
            return {}

    @staticmethod
    def process_buildings(data):
        buildings_by_city_and_floors = defaultdict(lambda: defaultdict(int))

        for row in data:
            city = row.get('city')
            floor = row.get('floor')

            if city and floor and floor.isdigit():
                buildings_by_city_and_floors[city][int(floor)] += 1

        return buildings_by_city_and_floors

class StatisticsDisplay:
    #Класс для отображения статистики

    @staticmethod
    def display_statistics(duplicates, buildings_by_city_and_floors, processing_time):
        print("\nСводная статистика:")

        print("\nДублирующиеся записи:")
        has_duplicates = False
        for record, count in duplicates.items():
            if count > 1:
                print(f"Запись: {dict(record)}, Повторений: {count}")
                has_duplicates = True

        if not has_duplicates:
            print("Дублирующихся записей нет.")

        print("\nКоличество зданий по этажам в каждом городе:")
        for city, floors in buildings_by_city_and_floors.items():
            print(f"\nГород: {city}")
            for floor, count in sorted(floors.items()):
                print(f"{floor} этаж(а/ей): {count} зданий")

        print(f"\nВремя обработки файла: {processing_time:.2f} секунд")

class App:
    #Основной класс приложения

    def __init__(self):
        self.parser = FileParser()
        self.processor = DataProcessor()
        self.display = StatisticsDisplay()

    def run(self):
        print("Добро пожаловать в приложение для обработки справочников :)")

        while True:
            file_path = input("Введите путь до файла-справочника (или 'exit' для выхода из программы): ").strip()

            if file_path.lower() == 'exit':
                print("Завершение работы приложения. Пока-пока :)")
                break

            if not os.path.exists(file_path):
                print("Файл не найден :()")
                continue

            start_time = time.time()

            if file_path.endswith('.csv'):
                data = self.parser.parse_csv(file_path)
            elif file_path.endswith('.xml'):
                data = self.parser.parse_xml(file_path)
            else:
                print("Неподдерживаемый формат файла. Поддерживаются только CSV и XML.")
                continue

            if not data:
                print("Файл пустой или содержит ошибки :(")
                continue

            duplicates = self.processor.process_duplicates(data)
            buildings_by_city_and_floors = self.processor.process_buildings(data)
            processing_time = time.time() - start_time

            self.display.display_statistics(duplicates, buildings_by_city_and_floors, processing_time)

if __name__ == "__main__":
    app = App()
    app.run()
