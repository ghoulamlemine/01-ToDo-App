import streamlit as st
import functions
import time
todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''


st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("This is app is to increase your productivity.")

for index, todo in enumerate(todos):
    print("il")
    checkbox = st.checkbox(todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()

st.text_input(label="entered_todo", label_visibility="hidden", placeholder="Add new todo..",on_change=add_todo, key="new_todo")
