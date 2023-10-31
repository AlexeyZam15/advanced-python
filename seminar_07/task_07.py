"""
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
from os import replace, path, mkdir, chdir, listdir


def sort_files(folder: str = ""):
    video = ['mp4', 'avi']
    images = ['png', 'jpeg']
    text = ['txt', 'md']
    audio = ['mp3', 'wav']

    # ссылки на переменные в словаре
    file_types = {'video': video, 'images': images, 'text': text, 'audio': audio}

    if folder:
        chdir(folder)

    for type_ in file_types:
        if not path.exists(type_):
            mkdir(type_)

    files = listdir()
    for folder, extensions in file_types.items():
        for file_type in extensions:
            files_list = list(filter(lambda x: file_type in x, files))
            for file in files_list:
                replace(file, f"{folder}/{file}")


if __name__ == '__main__':
    video = ['mp4', 'avi']
    images = ['png', 'jpeg']
    text = ['txt', 'md']
    audio = ['mp3', 'wav']
    exception = ['clv', 'json']

    # ссылки на переменные в словаре
    file_types = {'video': video, 'images': images, 'text': text, 'audio': audio, 'exception': exception}

    from task_06 import create_random_file

    FOLDER = "task_07"

    for type_var in file_types.values():
        for extension in type_var:
            create_random_file(extension, number_files=1, folder=FOLDER)

    sort_files(FOLDER)
