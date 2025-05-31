import json
import os

TASKS_FILE='tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open('tasks.json', 'r') as file:
            return json.load(file)
        
    return []
    
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)