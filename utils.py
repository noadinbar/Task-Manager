from colorama import init, Fore, Style

init()

def print_colored_task(task, index=None):
    status="✅" if task["done"] else "❌" 
    color=Fore.LIGHTGREEN_EX if task["done"] else Fore.LIGHTRED_EX
    prefix= f"{index}. " if index is not None else ""
    print(f"{prefix}[{status}] {color}{task['description']}{Style.RESET_ALL}  {Fore.CYAN}(📆 Due: {task['due_date']}){Style.RESET_ALL}")


def print_to_file(task, index, file):
    status="✅" if task["done"] else "❌"
    file.write(f"{index}. [{status}] {task['description']} (📆 Due: {task['due_date']})\n")

def is_valid_index(tasks, index):
    return index>=0 and index<len(tasks)
