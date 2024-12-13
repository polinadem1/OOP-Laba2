import os
import time
from parsers import parse_csv, parse_xml
from statistics import process_data, display_statistics


def main():
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
            data = parse_csv(file_path)
        elif file_path.endswith('.xml'):
            data = parse_xml(file_path)
        else:
            print("Неподдерживаемый формат файла. Поддерживаются только CSV и XML.")
            continue

        if not data:
            print("Файл пустой или содержит ошибки :(")
            continue

        duplicates, buildings_by_city_and_floors = process_data(data)
        processing_time = time.time() - start_time

        display_statistics(duplicates, buildings_by_city_and_floors, processing_time)


if __name__ == "__main__":
    main()
