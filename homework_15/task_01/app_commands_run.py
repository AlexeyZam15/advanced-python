from homework_15.task_01.aux_modules.run_command import run_command

if __name__ == '__main__':
    py_file = "rectangles_app.py"
    file_name = py_file.split('.')[0]
    with open(f"logs/{file_name}.log", "w"):
        pass
    run_command(f"python {py_file} -h")
    run_command(f"python {py_file} -r 10 10 r1")
    run_command(f"python {py_file} -sw 5 r1")
    run_command(f"python {py_file} -sw -5 r1")
