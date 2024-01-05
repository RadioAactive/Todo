import functions 
import PySimpleGUI as pg
import time

FILEPATH_TIME = "Todo project/Contents/time.txt"

time_global = time.strftime("%m %b %d, %y")

label = pg.Text("Enter a todo")
input_module = pg.InputText(tooltip="Enter TODO" , key="todo") 
#LIST BOX
compiled = []
if functions.open_file() != []:
    functions.time_repeat(compiled)
      
list_box = pg.Listbox(compiled , key="list", size=[40,5] , enable_events=True)
add_button = pg.Button("Add")
edit_button = pg.Button("Edit")

window = pg.Window("Todo" , layout=[[label],[input_module , add_button] ,
                                     [list_box , edit_button]])
while True:
    events , values = window.read() # type: ignore
    print(events)
    print(values)
    match events:
        case "Add":
            #time
            time_store = functions.open_file(listfile= FILEPATH_TIME)
            time_store.append(time_global + "\n")
            functions.write_file(time_store , listfile= FILEPATH_TIME)
            
            todo = functions.open_file()
            todo.append(values["todo"] + "\n")
            functions.write_file(todo)
            total_p = []
            functions.time_repeat(total_p)

            window["list"].update(values = total_p)
        case "Edit":
            todos = values["list"]
            input_todo = values["todo"]
            file_todo = functions.open_file()
            indeex = file_todo.index(todos[0])
            file_todo[indeex] = input_todo + "\n"
            print(file_todo)

            functions.write_file(file_todo)
            
            window["list"].update(values = file_todo)
         

        case pg.WIN_CLOSED:
            break
window.close()

