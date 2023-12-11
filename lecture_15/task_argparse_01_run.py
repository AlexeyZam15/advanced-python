from run_command import run_command

if __name__ == '__main__':
    run_command("python task_argparse_01.py 42 3.14 73",
                "python task_argparse_01.py --help",
                "python task_argparse_01.py Hello world")
