import os
import shutil
from pathlib import Path

for i in range(10):
    with open(f'file_{i}.txt', 'w', encoding='utf-8') as f:
        f.write('Hello world!')

NEW_DIR = 'new_dir'

if os.path.exists(NEW_DIR):
    shutil.rmtree(NEW_DIR)

os.mkdir('new_dir')
for i in range(2, 10, 2):
    f = Path(f'file_{i}.txt')
    f.replace('new_dir' / f)

DIR_NEW = 'dir_new'

if os.path.exists(DIR_NEW):
    shutil.rmtree(DIR_NEW)

shutil.copytree('new_dir', Path.cwd() / 'dir_new')
