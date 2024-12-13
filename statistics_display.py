class StatisticsDisplay:
    """Класс для отображения статистики."""

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
