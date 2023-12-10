from run_command import run_command

if __name__ == '__main__':
    run_command("python task_argparse_06.py -h",
                "python task_argparse_06.py -x -y -z 42 -z 73 -i -f -s")
