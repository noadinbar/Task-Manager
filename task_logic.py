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

def add_task(tasks, function):
    mission_description=input("Enter the mission: ")
    due_date=input("Please enter a due date in the format- DD-MM-YYYY: ")
    new_mission={
    "description":mission_description,
    "due_date": due_date,
    "done": False
    }
    tasks.append(new_mission)
    function(tasks)

def complete_task(tasks, function):
    index=int(input("Enter the number of mission you want to mark as completed: "))
    index-=1 #to get the real index in the list
    if is_valid_index(tasks, index):
        tasks[index]['done']=True
        function(tasks)
        print("Task marked as completed successfully")
    else:
        print("Invalid mission number")

def delete_task(tasks, function):
    index=int(input("Enter the number of mission you want to delete"))
    index-=1 #to get the real index in the list
    if is_valid_index(tasks, index):
        del tasks[index]
        function(tasks)
        print("Task deleted successfully")
    else:
        print("Invalid mission number")

def clear_tasks(tasks, function):
    answer=input("Are you sure you want to clear all the missions? \n Press y to continue or n to abort: ")
    if answer.lower()=='y':
        tasks.clear()
        function(tasks)
        return True
    else: 
        print("Clear cancelled.")
        return False

def print_tasks(tasks):
    for i,t in enumerate(tasks, start=1):
        print_colored_task(t, i)
        

def search_task(tasks):
    exprssion=input("Enter which word you would like to search: ")
    for t in tasks:
        if exprssion.lower() in t['description']:
            print_colored_task(t)

def sort_tasks(tasks):
    sorted_tasks=sorted(tasks, key=lambda t:t["done"])
    for i,t in enumerate(sorted_tasks, start=1):
        print_colored_task(t, i)
       
def exp_to_txt(tasks):
    with open('tasks.txt', 'w', encoding='utf-8') as file:
        for i,t in enumerate(tasks, start=1):
            print_to_file(t, i, file)
            

def exit_prog():
    print("Thank you for using ☺️")

def invalid():
     print("This command is not supported, please try again")
