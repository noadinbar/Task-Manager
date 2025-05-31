def add_task(tasks, function):
    mission_description=input("Enter the mission: ")
    new_mission={
    "description":mission_description,
    "done": False
    }
    tasks.append(new_mission)
    function(tasks)

def complete_task(tasks, function):
    index=int(input("Enter the number of mission you want to mark as completed: "))
    index-=1 #to get the real index in the list
    if index>=0 and index<len(tasks):
        tasks[index]['done']=True
        function(tasks)
        print("Task marked as completed successfully")
    else:
        print("Invalid mission number")

def delete_task(tasks, function):
    index=int(input("Enter the number of mission you want to delete"))
    index-=1 #to get the real index in the list
    if index>=0 and index<len(tasks):
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
        status="✅" if t["done"] else "❌" 
        print(f"{i}. [{status}] {t['description']}")

def search_task(tasks):
    exprssion=input("Enter which word you would like to search: ")
    for t in tasks:
        if exprssion.lower() in t['description']:
            status="✅" if t["done"] else "❌"
            print(f"[{status}] {t['description']}")

def sort_tasks(tasks):
    sorted_tasks=sorted(tasks, key=lambda t:t["done"])
    for i,t in enumerate(sorted_tasks, start=1):
        status="✅" if t["done"] else "❌" 
        print(f"{i}. [{status}] {t['description']}")

def exp_to_txt(tasks):
    with open('tasks.txt', 'w', encoding='utf-8') as file:
        for i,t in enumerate(tasks, start=1):
            status="✅" if t["done"] else "❌"
            file.write(f"{i}. [{status}] {t['description']}\n")

def exit_prog():
    print("Thank you for using ☺️")

def invalid():
     print("This command is not supported, please try again")

