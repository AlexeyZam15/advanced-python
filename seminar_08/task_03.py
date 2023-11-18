"""
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""
import csv
import json


def json_to_csv(json_file: str, csv_file: str):
    with open(json_file, "r", encoding="utf-8") as f:
        dict_ = json.load(f)

    with open(csv_file, "w", newline='', encoding="utf-8") as f:
        csv_write = csv.DictWriter(f, fieldnames=["access level", "personal id", "name"],
                                   dialect='excel',
                                   quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        all_data = []
        for access_level, id_name in dict_["access levels"].items():
            dict_row = {"access level": access_level}
            for personal_id, name in id_name.items():
                dict_row["personal id"] = personal_id
                dict_row["name"] = name
            all_data.append(dict_row)
        csv_write.writerows(all_data)


if __name__ == '__main__':
    JSON_FILE = "task_02.json"
    CSV_FILE = "task03.csv"

    json_to_csv(JSON_FILE, CSV_FILE)
