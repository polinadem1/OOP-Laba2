from collections import Counter, defaultdict


def process_data(data):
    #Обрабатывает данные и формирует статистику
    try:
        # Считаем дублирующиеся записи
        duplicates = Counter(tuple((key, str(value)) for key, value in row.items()) for row in data)
    except AttributeError:
        print("Ошибка: Некорректный формат строки данных.")
        return {}, {}

    buildings_by_city_and_floors = defaultdict(lambda: defaultdict(int))

    for row in data:
        city = row.get('city')
        floor = row.get('floor')

        if city and floor and floor.isdigit():
            buildings_by_city_and_floors[city][int(floor)] += 1

    return duplicates, buildings_by_city_and_floors


def display_statistics(duplicates, buildings_by_city_and_floors, processing_time):
    #Выводит статистику
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
