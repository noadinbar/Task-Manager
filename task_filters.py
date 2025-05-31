from datetime import datetime, date
from utils import print_colored_task

def find_filter(tasks, condition):
    found = False
    for task in tasks:
        task_date = convert_date(task['due_date'])
        if task_date and condition(task_date):
            print_colored_task(task)
            found = True

    if not found:
        print("No tasks match the selected filter.")


def filter_tasks(tasks, filter_type):
    today = date.today()
    
    match filter_type:
        case "today":
            find_filter(tasks, lambda d: d == today)

        case "overdue":
            find_filter(tasks, lambda d: d < today)

        case "upcoming":
            find_filter(tasks, lambda d: d >= today)

        case "on":
            target = convert_date(input("Enter a date (DD-MM-YYYY): "))
            if target:
                find_filter(tasks, lambda d: d == target)

        case _:
            print("Unknown filter type. You can only choose between: today / upcoming / overdue / on")

def convert_date(date):
    try:
        return datetime.strptime(date, "%d-%m-%Y").date()
    except ValueError:
        print(f"Invalid date format: {date}. Please use DD-MM-YYYY.")
        return None