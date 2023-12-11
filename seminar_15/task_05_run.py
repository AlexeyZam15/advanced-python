from run_command import run_command

if __name__ == '__main__':
    with open("logs/task_05.log", "w"):
        pass
    run_command("python task_05.py -h")
    enquiries = ["1-й четверг ноября", "3-я среда мая", "5-й вторник мая", "7-я суббота июля",
                 "9-е воскресенье августа", "dfgdfg fgdfg dfg fdg", "1 fgdfg dfg fdg", "1 gfhfgh ноября",
                 "24-ый четверг ноября", "1 monday november"]
    for enquiry in enquiries:
        enquiry_split = enquiry.split()
        run_command(f"python task_05.py -n {enquiry_split[0]} -wd {enquiry_split[1]} -m {enquiry_split[2]}")
    run_command(f"python task_05.py")
    run_command(f"python task_05.py -n 2")
    run_command(f"python task_05.py -n 2 -wd 6")
    run_command(f"python task_05.py -n 2 -wd 6 -m 11")
