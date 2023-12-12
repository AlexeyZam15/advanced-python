import subprocess


def run_command(*commands):
    for command in commands:
        print("_" * 60)
        print(command)
        subprocess.run(command, shell=True)
