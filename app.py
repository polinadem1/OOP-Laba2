import time
from file_parser import FileParser
from data_processor import DataProcessor
from statistics_display import StatisticsDisplay

class App:
    """Основной класс приложения."""

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

            if not file_path.endswith(('.csv', '.xml')):
                print("Неподдерживаемый формат файла. Поддерживаются только CSV и XML.")
                continue

            start_time = time.time()

            if file_path.endswith('.csv'):
                data = self.parser.parse_csv(file_path)
            else:
                data = self.parser.parse_xml(file_path)

            if not data:
                print("Файл пустой или содержит ошибки :(")
                continue

            duplicates = self.processor.process_duplicates(data)
            buildings_by_city_and_floors = self.processor.process_buildings(data)
            processing_time = time.time() - start_time

            self.display.display_statistics(duplicates, buildings_by_city_and_floors, processing_time)
