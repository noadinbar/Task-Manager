from tasks_storage import load_tasks, save_tasks
from task_logic import *

def main():
    tasks=load_tasks()

    while True:
        command=input("Please enter your command: ")

        match command:
            case "add":
                add_task(tasks, save_tasks)

            case "complete":
                complete_task(tasks, save_tasks)

            case "delete":
                delete_task(tasks, save_tasks)

            case "clear":
                cleared= clear_tasks(tasks, save_tasks)

            case "list":
                print_tasks(tasks)

            case "search":
                search_task(tasks)

            case "sort":
                sort_tasks(tasks)

            case "export":
                exp_to_txt(tasks)

            case "filter":
                filter_by_type(tasks)

            case "exit":
                exit_prog()
                break
            case _:
               invalid()



if __name__== "__main__":
    main()

