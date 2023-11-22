import csv
from functools import wraps
from random import randint
from typing import Callable, Iterator
import json


def generate_csv_file(file_name: str, rows: int, min_number: int = 1, max_number: int = 10):
    with open(file_name, "w", encoding="utf-8", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=["a", "b", "c"], quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        data = []
        for _ in range(rows):
            row = {"a": randint(min_number, max_number), "b": randint(min_number, max_number),
                   "c": randint(min_number, max_number)}
            data.append(row)
        csv_writer.writerows(data)


def save_to_json(func: Callable):
    @wraps(func)
    def wrapper(*args):
        with open(args[0], "r", encoding="utf-8", newline="") as csv_file:
            csv_list_of_dicts: Iterator[dict] = csv.DictReader(csv_file, fieldnames=["a", "b", "c"])
            next(csv_list_of_dicts)
            json_data = []
            for row in csv_list_of_dicts:
                a, b, c = int(row["a"]), int(row["b"]), int(row["c"])
                json_dict = {"a": a, "b": b, "c": c, "roots": func(a, b, c)}
                json_data.append(json_dict)
            with open("results.json", "w", encoding="utf-8") as json_file:
                json.dump(json_data, json_file, ensure_ascii=False, indent=4)

    return wrapper


@save_to_json
def find_roots(a: int, b: int, c: int):
    if a == 0:
        return None
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
