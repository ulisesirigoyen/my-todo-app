import streamlit as st
import functions

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    if todo:
        todos.append(todo)
        functions.write_todos(todos)
    st.session_state['new_todo'] = ""

todos = functions.get_todos()

st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')

for index, todo in enumerate(todos):
    key = f'todo-{index}'
    checkbox = st.checkbox(todo, key=key)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[key]
        st.rerun()

st.text_input(label='Enter a new todo:',
              on_change=add_todo, key='new_todo')

