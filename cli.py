import time
import functions
import os
import json

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

if not os.path.exists(functions.FILEPATH):
    with open(functions.FILEPATH, "w") as file:
        json.dump([], file)

while True:
    user_action = input("Enter: add [todo], show, edit [number], complete [number] or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)
    
    elif user_action == "show":
        todos = functions.get_todos()
        if todos:
            for index, todo in enumerate(todos):
                print(f"{index +1 } - {todo}")
        else:
            print("No todos found!")
    
    elif user_action.startswith("edit"):
        todos = functions.get_todos()
        todo_to_edit = user_action[5:].strip()

        try:
            index = int(todo_to_edit) - 1
        except ValueError:
            print("Sorry it's seems you didn't enter a number.")
            continue

        if index + 1 <= len(todos):
            todos[index] = input("Enter a new todo: ")
            functions.write_todos(todos)
            print(f"todo was modified successfully!")
        else:
            print("Sorry this index out of range.")
    
    elif user_action.startswith("complete"):
        todos = functions.get_todos()
        todo_to_complete = user_action[9:].strip()
        try:
            index = int(todo_to_complete) - 1
        except ValueError:
            print("Sorry, it's seems you didn't enter a number.")
            continue

        if index + 1 <= len(todos):
            removed_todo = todos.pop(index)
            functions.write_todos(todos)
            print(f"{removed_todo} was removed successfully")
        else:
            print("Sorry, this index is out of range")
    
    elif user_action == 'exit':
        break

    else:
        print("Command not valid.")

print("By By!")

    