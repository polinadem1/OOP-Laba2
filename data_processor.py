from collections import Counter, defaultdict

class DataProcessor:
    """Класс для обработки данных."""

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
