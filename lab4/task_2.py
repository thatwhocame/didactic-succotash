import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Чтение данных из CSV файла
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        # Преобразуем каждую строку в формат, где значения представлены как строки с 6 знаками после запятой
        data = []
        for row in reader:
            formatted_row = {key: f"{float(value):.6f}" for key, value in row.items()}
            data.append(formatted_row)

    # Запись данных в JSON файл с отступами
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Проверка работы функции
    task()

    # Печать содержимого JSON-файла для проверки результата
    with open(OUTPUT_FILENAME, mode='r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
