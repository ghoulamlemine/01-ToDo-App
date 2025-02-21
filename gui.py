import json
import FreeSimpleGUI as sg
import functions
import time
import os


if not os.path.exists("todos.json"):
    with open("todos.json", "w") as file:
        json.dump([], file)

sg.theme("Black")
clock = sg.Text(time.strftime("%b %d, %Y %H:%M:%S"), key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add", size= 8)
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True,size=[44, 10])
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")

windows = sg.Window("My TO-DO App", layout=[
                                            [clock],
                                            [label],
                                            [input_box, add_button],
                                            [list_box, edit_button, complete_button],
                                            [exit_button]

                                        ],
                                        font=('Helvetica', 12))


while True:
    event, values = windows.read(timeout=200)
    print(event, values)

    if event == sg.WIN_CLOSED:
        pass
    else:
        windows["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    
    match event:
        case 'Add':
            todo = values['todo']
            todos = functions.get_todos()
            todos.append(todo)
            functions.write_todos(todos)
            windows['todos'].update(values=todos)
        case 'Edit':
            todos = functions.get_todos()
            try:
                todo_to_edit = values['todos'][0]
            except IndexError:
                sg.popup("Please select an item first.", font("helvetica", 20))
                continue
            index = todos.index(todo_to_edit)
            todos[index] = values['todo']
            functions.write_todos(todos)
            windows['todos'].update(values=todos)
        
        case 'todos':
            try:
                windows['todo'].update(value=values["todos"][0])
            except IndexError:
                pass
        
        case "Complete":
            todos = functions.get_todos()
            try:
                todo_to_removed = values["todos"][0]
            except IndexError:
                sg.popup("Pleas select an item first.", font=("hevetica", 20))
                continue

            todos.remove(todo_to_removed)
            functions.write_todos(todos)
            windows["todos"].update(values=todos)
            windows["todo"].update(value="")
        
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

windows.close()