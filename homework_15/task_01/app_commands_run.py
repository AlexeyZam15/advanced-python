from homework_15.task_01.aux_modules.run_command import run_command

if __name__ == '__main__':
    py_file = "rectangles_app.py"
    file_name = py_file.split('.')[0]
    with open(f"logs/{file_name}.log", "w"):
        pass
    run_command(f"python {py_file} -h")
    run_command(f"python {py_file} -cr 10 10 r1")
    run_command(f"python {py_file} -sw 5 r1")
    run_command(f"python {py_file} -sw -5 r1")
    run_command(f"python {py_file} -sh 5 r1")
    run_command(f"python {py_file} -sh -5 r1")
    run_command(f"python {py_file} -cr 10 10 r2")
    run_command(f"python {py_file} -sum r1 r2 r3")
    run_command(f"python {py_file} -sub r1 r2 r4")
    run_command(f"python {py_file} -p r4")
    run_command(f"python {py_file} -a r4")
