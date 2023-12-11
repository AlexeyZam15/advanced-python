"""
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.
"""

import os
import logging
from collections import namedtuple
import argparse

logging.basicConfig(
    level=logging.NOTSET,
    format='%(message)s',
    filename='logs/task_06.log',
    encoding="utf-8"
)
logger = logging.getLogger(__name__)


def get_info(path: str):
    """
    Функция получает на вход путь до директории на ПК.
    Соберите информацию о содержимом в виде объектов namedtuple.
    Каждый объект хранит:
    ○ имя файла без расширения или название каталога,
    ○ расширение, если это файл,
    ○ флаг каталога,
    ○ название родительского каталога.
    """
    logger.info(f'Собираем информацию о содержимом директории {path}')
    Info = namedtuple('Info', 'name ext is_dir parent')
    content = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            name = os.path.basename(dir)
            is_dir = True
            parent = os.path.basename(root)
            content.append(Info(name, None, is_dir, parent))
            logger.info(f'Название: {name} - Расширение: {None} - Каталог: {is_dir} - Родительский каталог: {parent}')
        for file in files:
            name, ext = os.path.splitext(file)
            is_dir = False
            parent = os.path.basename(root)
            content.append(Info(name, ext, is_dir, parent))
            logger.info(f'Название: {name} - Расширение: {None} - Каталог: {is_dir} - Родительский каталог: {parent}')
    return content


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=get_info.__doc__)
    parser.add_argument('-p', metavar="path", help='path to directory on PC', type=str, default=".")
    args = parser.parse_args()
    content = get_info(args.p)
    print(f'Содержимое директории {args.p}:', *content, sep="\n")
