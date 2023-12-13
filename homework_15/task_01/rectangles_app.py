import argparse

import json

from model.rectangle import Rectangle
from aux_modules.exceptions import *
from aux_modules.logger import log_all

import os


class RectanglesApp:
    _rectangles_dict = {}

    def __init__(self, rectangle_cls: type, json_file=None):
        self.rectangle_cls = rectangle_cls
        if json_file is None:
            self._json_file = os.path.dirname(os.path.abspath(__file__)) + "/" + __file__.split("\\")[-1].split(".")[
                0] + ".json"
        else:
            if self.check_path(json_file) is not True:
                self._json_file = os.path.dirname(os.path.abspath(__file__)) + "/" + \
                                  __file__.split("\\")[-1].split(".")[0] + ".json"
            else:
                self._json_file = json_file
        if os.path.exists(self._json_file):
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
        try:
            rectangle = Rectangle(width, height, name)
            self._rectangles_dict[name] = rectangle
            self.save_to_json()
        except MyBaseException as mbe:
            print(mbe)
            raise mbe
        return rectangle

    @log_all
    def set_width(self, name, value):
        try:
            self.check_rectangle(name)
            self._rectangles_dict[name].width = value
            self.save_to_json()
        except MyBaseException as mbe:
            print(mbe)
            raise mbe
        return self._rectangles_dict[name]

    @log_all
    def set_height(self, name, value):
        try:
            self.check_rectangle(name)
            self._rectangles_dict[name].height = value
            self.save_to_json()
        except MyBaseException as mbe:
            print(mbe)
            raise mbe
        return self._rectangles_dict[name]

    def check_rectangle(self, name):
        if name not in self._rectangles_dict:
            try:
                raise ValueError
            except ValueError:
                raise NonExistentInstanceException(f"Прямоугольника с именем {name} не существует")
        return True

    @log_all
    def sum(self, r1_name, r2_name, new_name):
        try:
            self.check_rectangle(r1_name)
            self.check_rectangle(r2_name)
            res = self._rectangles_dict[r1_name] + self._rectangles_dict[r2_name]
        except MyBaseException as mbe:
            print(mbe)
            raise mbe
        return self.create_rectangle(res.width, res.height, new_name)

    @log_all
    def sub(self, r1_name, r2_name, new_name):
        try:
            self.check_rectangle(r1_name)
            self.check_rectangle(r2_name)
            res = self._rectangles_dict[r1_name] - self._rectangles_dict[r2_name]
        except MyBaseException as mbe:
            print(mbe)
            raise mbe
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
        try:
            self.check_rectangle(name)
        except MyBaseException as mbe:
            print(mbe)
            raise mbe
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
    app = RectanglesApp(Rectangle, os.path.dirname(os.path.abspath(__file__)) + "/json/rectangles_app.json")
    parser = argparse.ArgumentParser(description="Создание прямоугольников и выполнение операций с ними")
    parser.add_argument('-cr', '--create_rectangles', metavar=('width', 'height', 'name'),
                        help='создание прямоугольников с указанными шириной, высотой, и именем',
                        type=str, action="append", nargs=3)
    parser.add_argument('-sw', '--set_width', metavar=('width', 'name'),
                        help='изменение ширины прямоугольника с указанным именем',
                        type=str, action="append", nargs=2)
    parser.add_argument('-sh', '--set_height', metavar=('height', 'name'),
                        help='изменение высоты прямоугольника с указанным именем',
                        type=str, action="append", nargs=2)
    parser.add_argument('-sum', metavar=('r1_name', 'r2_name', 'new_r_name'),
                        help='сложение прямоугольников с указанными именами и создание нового',
                        type=str, action="append", nargs=3)
    parser.add_argument('-sub', metavar=('r1_name', 'r2_name', 'new_r_name'),
                        help='вычитание прямоугольников с указанными именами и создание нового',
                        type=str, action="append", nargs=3)
    parser.add_argument('-p', "--perimeter", metavar='r_name',
                        help='получение периметра прямоугольника с указанным именем',
                        type=str, action="append")
    parser.add_argument('-a', "--area", metavar='r_name',
                        help='получение площади прямоугольника с указанным именем',
                        type=str, action="append")
    parser.add_argument('-sr', "--show_rectangle", metavar='r_name',
                        help='получение строкового представления прямоугольника с указанным именем',
                        type=str, action="append")
    parser.add_argument('-sar', "--show_all_rectangles",
                        help='получение строкового представления всех прямоугольников', action="store_true")

    args = parser.parse_args()

    if args.create_rectangles:
        for r in args.create_rectangles:
            if app.create_rectangle(r[0], r[1], r[2]):
                print(f"Прямоугольник {r[2]} создан с шириной {r[0]} и высотой {r[1]}")

    if args.set_width:
        for r in args.set_width:
            if app.set_width(r[1], r[0]):
                print(f"Ширина прямоугольника {r[1]} изменена на {r[0]}")

    if args.set_height:
        for r in args.set_height:
            if app.set_height(r[1], r[0]):
                print(f"Высота прямоугольника {r[1]} изменена на {r[0]}")

    if args.sum:
        for r in args.sum:
            res = app.sum(r[0], r[1], r[2])
            if res:
                print(f"Прямоугольник {r[2]} создан из суммы прямоугольников {r[0]} и {r[1]}")
                print(f"Полученный прямоугольник - {res}")

    if args.sub:
        for r in args.sub:
            res = app.sub(r[0], r[1], r[2])
            if res:
                print(f"Прямоугольник {r[2]} создан из разности прямоугольников {r[0]} и {r[1]}")
                print(f"Полученный прямоугольник - {res}")

    if args.perimeter:
        for r in args.perimeter:
            rectangle = app.get_rectangle(r)
            if rectangle:
                print(f"Периметр прямоугольника {r} равен {rectangle.perimeter()}")

    if args.area:
        for r in args.area:
            rectangle = app.get_rectangle(r)
            if rectangle:
                print(f"Площадь прямоугольника {r} равна {rectangle.area()}")

    if args.show_rectangle:
        for r in args.show_rectangle:
            rectangle = app.get_rectangle(r)
            if rectangle:
                print(app.get_rectangle(r))

    if args.show_all_rectangles:
        rectangles = app.get_rectangles()
        if rectangles:
            print("Все прямоугольники:")
            for r in app.get_rectangles():
                print(r)
        else:
            print("Нет созданных прямоугольников")
