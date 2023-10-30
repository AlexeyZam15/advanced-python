import os
from pathlib import Path

open('one_more_dir/one.txt', mode="a")
open('one_more_dir/one_more.txt', mode="a")

# удаление файлов
os.remove('one_more_dir/one.txt')
Path('one_more_dir/one_more.txt').unlink()
