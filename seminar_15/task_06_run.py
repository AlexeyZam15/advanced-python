from run_command import run_command

if __name__ == '__main__':
    with open("logs/task_06.log", "w"):
        pass
    run_command("python task_06.py -h")
    run_command("python task_06.py")
    run_command("python task_06.py -p logs")