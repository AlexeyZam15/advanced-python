import os
from pathlib import Path

OLD_NAME = 'old_name.py'
NEW_NAME = 'new_name.py'

open(OLD_NAME, mode="w")
if os.path.exists(NEW_NAME):
    os.remove(NEW_NAME)

os.rename(OLD_NAME, NEW_NAME)

OLD_FILE = 'old_file.py'
NEW_FILE = 'new_file.py'

open(OLD_FILE, mode="w")
if os.path.exists(NEW_FILE):
    os.remove(NEW_FILE)

p = Path('old_file.py')
p.rename('new_file.py')

NEWEST_FILE = 'newest_file.py'

if os.path.exists(NEWEST_FILE):
    os.remove(NEWEST_FILE)
Path('new_file.py').rename(NEWEST_FILE)
