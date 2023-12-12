import argparse
import datetime
from collections import namedtuple

import json

from homework_15.task_01.model.rectangle import Rectangle
from homework_15.task_01.aux_modules.exceptions import *
from homework_15.task_01.aux_modules.logger import log_all

import os


class RectanglesApp:
    _rectangles_dict = {}

    def __init__(self, rectangle_cls: type, json_file=None):
        self.rectangle_cls = rectangle_cls
        if json_file is None:
            self._json_file = __file__.split("\\")[-1].split(".")[0] + ".json"
        else:
            if self.check_path(json_file) is not True:
                self._json_file = __file__.split("\\")[-1].split(".")[0] + ".json"
            else:
                self._json_file = json_file
        self.load_from_json()

    @property
    def json_file(self):
        return self._json_file

    @json_file.setter
    def json_file(self, value):
        if self.check_path(value) is True:
            self._json_file = value

    @log_all
    def check_path(self, path):
        path = "/".join(path.split("/")[0:-1])
        if os.path.exists(path) is False:
            try:
                raise ValueError
            except ValueError:
                raise NonExistentPathException(f"Путь {path} не существует")
        return True

    @log_all
    def create_rectangle(self, width, height, name):
        rectangle = Rectangle(width, height, name)
        self._rectangles_dict[name] = rectangle
        self.save_to_json()
        return rectangle

    @log_all
    def set_width(self, name, value):
        self.check_rectangle(name)
        self._rectangles_dict[name].width = value
        self.save_to_json()
        return self._rectangles_dict[name]

    @log_all
    def set_height(self, name, value):
        self.check_rectangle(name)
        self._rectangles_dict[name].height = value
        self.save_to_json()
        return self._rectangles_dict[name]

    @log_all
    def check_rectangle(self, name):
        if name not in self._rectangles_dict:
            try:
                raise ValueError
            except ValueError:
                raise NonExistentInstanceException(f"Прямоугольника с именем {name} не существует")
        return True

    @log_all
    def rectangles_sum(self, new_name, *r_names):
        for r_name in r_names:
            self.check_rectangle(r_name)
        res_rectangle = None
        for i in range(len(r_names) - 1):
            res_rectangle = self._rectangles_dict[r_names[i]] + self._rectangles_dict[r_names[i + 1]]
        return self.create_rectangle(res_rectangle.width, res_rectangle.height, new_name)

    @log_all
    def rectangles_sub(self, new_name, rectangle1_name, rectangle2_name):
        self.check_rectangle(rectangle1_name)
        self.check_rectangle(rectangle2_name)
        res = self._rectangles_dict[rectangle1_name] - self._rectangles_dict[rectangle2_name]
        return self.create_rectangle(res.width, res.height, new_name)

    def __repr__(self):
        return f"RectanglesApp({self.rectangle_cls.__name__})"

    @log_all
    def get_rectangles(self):
        return self._rectangles_dict.values()

    @log_all
    def get_rectangle_area(self, name):
        self.check_rectangle(name)
        return self._rectangles_dict[name]

    @log_all
    def get_rectangle(self, name):
        self.check_rectangle(name)
        return self._rectangles_dict[name]

    @log_all
    def save_to_json(self):
        json_data = {}
        for name, r in self._rectangles_dict.items():
            json_data[name] = {"width": r.width, "height": r.height}
        with open(self._json_file, "w+", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=True, indent=2)
        return self._json_file

    @log_all
    def load_from_json(self):
        try:
            with open(self._json_file, "r", encoding="utf-8") as f:
                json_data = json.load(f)
        except FileNotFoundError:
            raise JsonFileNotFoundError(f"Файл {self._json_file} не найден")
        created_rectangles = []
        for name, data in json_data.items():
            created_rectangles.append(self.create_rectangle(data["width"], data["height"], name))
        return created_rectangles


if __name__ == '__main__':
    app = RectanglesApp(Rectangle, "json/rectangles_app.json")
    # RectangleTuple = namedtuple('Rectangle', 'width height name')
    parser = argparse.ArgumentParser(description="Создание прямоугольников и выполнение операций с ними")
    parser.add_argument('-r', '--rectangles', metavar=('width', 'height', 'name'),
                        help='создание прямоугольников с указанными шириной, высотой, и именем',
                        type=str, action="append", nargs=3)
    parser.add_argument('-sw', '--set_width', metavar=('width', 'name'),
                        help='изменение ширины прямоугольника с указанным именем',
                        type=str, action="append", nargs=2)
    args = parser.parse_args()

    if args.rectangles:
        for r in args.rectangles:
            app.create_rectangle(r[0], r[1], r[2])

    if args.set_width:
        for r in args.set_width:
            app.set_width(r[1], r[0])

    # app = RectanglesApp(Rectangle, "json/rectangles_app.json")
    # app.load_from_json()
    # app.create_rectangle(10, 10, "r1")
    # app.create_rectangle(20, 20, "r2")
    # app.set_width("r1", -5)
    # app.set_height("r1", -5)
    # app.rectangles_sum("r3", "r1", "r2")
    # app.rectangles_sub("r4", "r1", "r2")
    # print(*app.get_rectangles(), sep="\n")
    # app.save_to_json()
