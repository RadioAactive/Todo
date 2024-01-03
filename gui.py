import functions
import PySimpleGUI as pg
import time

time_global = time.strftime("%m %b %d, %y")

label = pg.Text("Enter a todo")
input_module = pg.InputText(tooltip="Enter TODO" , key="todo")
add_button = pg.Button("Add")

window = pg.Window("Todo" , layout=[[label],[input_module , add_button] ])
while True:
    events , values = window.read()
    match events:
        case "Add":
            todo = functions.open_file()
            todo.append(values["todo"] + "\n")
            functions.write_file(todo)

            #time
            time_store = functions.open_file(listfile="Todo project/Contents/time.txt")
            time_store.append(time_global + "\n")
            functions.write_file(time_store , listfile="Todo project/Contents/time.txt")

        case pg.WIN_CLOSED:
            break
window.close()

