import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create the to-do list
todos = []

# Define functions

def add_todo():
    # Ask for a new to-do item
    new_todo = tk.simpledialog.askstring("New To-Do", "Enter a new to-do item:")
    
    # Add it to the list
    if new_todo:
        todos.append(new_todo)
        update_list()

def complete_todo():
    # Mark the selected to-do as complete
    todo_index = todo_list.curselection()[0]
    todos[todo_index] = "[X] " + todos[todo_index]
    update_list()

def delete_todo():
    # Delete the selected to-do
    todo_index = todo_list.curselection()[0]
    todos.pop(todo_index)
    update_list()

def update_list():
    # Clear the list
    todo_list.delete(0, tk.END)
    
    # Add back each item
    for todo in todos:
        todo_list.insert(tk.END, todo)

# Create GUI components
todo_list = tk.Listbox(window)
todo_list.pack()

add_button = tk.Button(window, text="Add new to-do", command=add_todo)
add_button.pack()

complete_button = tk.Button(window, text="Complete to-do", command=complete_todo)  
complete_button.pack()

delete_button = tk.Button(window, text="Delete to-do", command=delete_todo)
delete_button.pack()

# Start the main loop
window.mainloop()
