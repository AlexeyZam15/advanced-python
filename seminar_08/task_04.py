"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""
import csv
import json


def read_csv(csv_file: str):
    """Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader."""
    with open(csv_file, "r", encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        lines = [line for line in csv_reader]

    lines[0].append("hash")
    for line in lines[1:]:
        """Дополните id до 10 цифр незначащими нулями."""
        line[1] = line[1].zfill(10)
        """В именах первую букву сделайте прописной."""
        line[2] = line[2].title()
        """Добавьте поле хеш на основе имени и идентификатора."""
        line.append(str(hash(line[2] + line[1])))
    return lines


def list_to_json(i_list: list, json_file: str):
    """Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции."""
    with open(json_file, "w", encoding="utf-8") as f:
        json_dict_fields = i_list[0]
        json_data = []
        for line, v_list in enumerate(i_list[1:]):
            json_dict = {}
            for v_list_field_index, field in enumerate(json_dict_fields):
                json_dict[field] = v_list[v_list_field_index]
            json_data.append(json_dict)
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def csv_to_json(csv_file: str, json_file: str):
    list_to_json(read_csv(csv_file), json_file)


if __name__ == '__main__':
    CSV_FILE = "task03.csv"
    JSON_FILE = "task_04.json"
    # csv_list = read_csv(CSV_FILE)
    # list_to_json(csv_list, JSON_FILE)
    csv_to_json(CSV_FILE, JSON_FILE)
