def run_command(*commands):
    import subprocess
    for command in commands:
        print("_" * 60, "\n", command)
        subprocess.run(command, shell=True)


if __name__ == '__main__':
    run_command("python -m doctest task_doctest_04.py",
                "python -m doctest task_doctest_04.py -v",
                "python -m doctest .\prime.md",
                "python -m doctest .\prime.md -v")
