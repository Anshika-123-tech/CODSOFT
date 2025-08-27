import tkinter as tk
from tkinter import messagebox

# ---------------------------
# TASK STORAGE
# ---------------------------
tasks = []

# ---------------------------
# CLI FUNCTIONS
# ---------------------------
def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Switch to GUI mode")
    print("6. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✔ Done" if task['done'] else "❌ Not Done"
            print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")

def mark_done():
    view_tasks()
    try:
        choice = int(input("Enter task number to mark as done: "))
        tasks[choice-1]["done"] = True
        print("Task marked as done!")
    except:
        print("Invalid input!")

def delete_task():
    view_tasks()
    try:
        choice = int(input("Enter task number to delete: "))
        removed = tasks.pop(choice-1)
        print(f"Deleted task: {removed['title']}")
    except:
        print("Invalid input!")

# ---------------------------
# GUI FUNCTIONS
# ---------------------------
def refresh_listbox():
    """Update the listbox to always show tasks"""
    listbox.delete(0, tk.END)
    if not tasks:
        listbox.insert(tk.END, "No tasks yet. Add one!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔" if task['done'] else "❌"
            listbox.insert(tk.END, f"{i}. {task['title']} - {status}")

def gui_add_task():
    title = entry.get()
    if title:
        tasks.append({"title": title, "done": False})
        entry.delete(0, tk.END)
        refresh_listbox()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def gui_mark_done():
    try:
        index = listbox.curselection()[0]
        if tasks:  # avoid error if list is empty
            tasks[index]["done"] = True
            refresh_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task first!")

def gui_delete_task():
    try:
        index = listbox.curselection()[0]
        if tasks:
            tasks.pop(index)
            refresh_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task first!")

def launch_gui():
    global entry, listbox
    window = tk.Tk()
    window.title("To-Do List")

    # Entry field
    entry = tk.Entry(window, width=40)
    entry.pack(pady=5)

    # Buttons
    tk.Button(window, text="Add Task", command=gui_add_task).pack(pady=2)
    tk.Button(window, text="Mark Done", command=gui_mark_done).pack(pady=2)
    tk.Button(window, text="Delete Task", command=gui_delete_task).pack(pady=2)

    # Listbox
    listbox = tk.Listbox(window, width=50)
    listbox.pack(pady=5)

    # Show initial tasks
    refresh_listbox()

    window.mainloop()

# ---------------------------
# MAIN PROGRAM
# ---------------------------
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Switching to GUI mode...")
            launch_gui()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()


