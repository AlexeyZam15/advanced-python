from array import array


def try_exec(*commands):
    for command in commands:
        try:
            exec(command)
        except Exception as e:
            print(f'Command: {command}')
            print(f'Error: {e}')
            print()
            continue
        print(f'Command: {command}')
        print()
        continue


long_array = array('l', [-6000, 800, 100500])
# OverflowError: Python int too large to convert to C long
# TypeError: 'float' object cannot be interpreted as an integer
try_exec("long_array.append(2 ** 32)", "long_array.append(3.14)")
