import os
import shutil

ONE_MORE_DIR = 'one_more_dir'

if os.path.exists(ONE_MORE_DIR):
    shutil.rmtree(ONE_MORE_DIR)

shutil.copytree('dir', ONE_MORE_DIR)
