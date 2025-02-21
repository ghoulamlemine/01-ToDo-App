import json
import os
FILEPATH = "todos.json"

def get_todos(filepath = FILEPATH):
    with open(filepath, "r") as file:
        """
        Read teh text file and return a to-do items 
        """
        content = json.load(file)
    return content
    
        


def write_todos(todos, filepath = FILEPATH):
    with open(filepath, "w") as file:
        """
        Wirte the todos in the text file
        """
        json.dump(todos, file)


if __name__ == "__main__":
    print("Hello")
    print(get_todos)