# Python Task Manager

A simple and lightweight command-line task manager written in Python.  
Supports adding, listing, completing, deleting, searching, sorting, and exporting tasks to txt file – all stored in a JSON file.

---

## Features

- Add new tasks  
- Mark tasks as completed  
- Delete individual tasks  
- Clear all tasks with confirmation  
- List tasks with status indicators (✅ / ❌)  
- Search tasks by keyword  
- Sort tasks (not completed first)  
- Export tasks to a readable `.txt` file  

---

## Requirements

- Python 3.8 or higher  

---

## ▶️ How to Run

You can run the program in 3 ways:

1. Run the run.bat file
2. Open the project in VS Code and run main.py
3. Open a terminal in the project folder and run:

```bash
python main.py
```

---

## Available Commands

| Command    | Description                          |
|------------|--------------------------------------|
| `add`      | Add a new task                       |
| `list`     | List all tasks                       |
| `complete` | Mark a task as completed             |
| `delete`   | Delete a specific task               |
| `clear`    | Clear all tasks (with confirmation)  |
| `search`   | Search for tasks by keyword          |
| `sort`     | Sort tasks (completed first)         |
| `export`   | Export tasks to `tasks.txt`          |
| `exit`     | Exit the program                     |

---

##  File Structure
.
├── main.py              # Main loop
├── task_logic.py        # Core task operations
├── tasks_storage.py     # File reading and writing (JSON)
├── tasks.json           # Task data file
├── tasks.txt            # Exported task list (generated)
└── README.md            # Project documentation

---

## Example Output

1. [❌] Buy groceries
2. [✅] Submit homework

