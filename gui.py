import functions 
import PySimpleGUI as pg
import time

FILEPATH_TIME = "Todo project/Contents/time.txt"

time_global = time.strftime("%m %b %d, %y")

label = pg.Text("Enter a todo")
input_module = pg.InputText(tooltip="Enter TODO" , key="todo") 

#LIST BOX
upd_compiled = []
if functions.open_file() != []:
    functions.time_repeat(upd_compiled)

list_box = pg.Listbox(upd_compiled , key="list", size=[40,5] , enable_events=True)
add_button = pg.Button("Add")
edit_button = pg.Button("Edit")
remove_button = pg.Button("Remove")

window = pg.Window("Todo" , layout=[[label],[input_module , add_button] ,
                                     [list_box] , [remove_button , edit_button]])
while True:
    #LIST BOX
    compiled = []
    if functions.open_file() != []:
        functions.time_repeat(compiled)
    events , values   = window.read() # type: ignore
    print(events , values)
    match events:
        case "Add":
            if values['todo'] + '\n' in functions.open_file():
                w = pg.Window("Error" , layout=[[pg.Text("You are already doing this task!")]])
                w.read()
                continue
            #time
            time_store = functions.open_file(listfile= FILEPATH_TIME)
            time_store.append(time_global + "\n")
            functions.write_file(time_store , listfile= FILEPATH_TIME)
            
            todo = functions.open_file()
            todo.append(values["todo"] + "\n")
            functions.write_file(todo)
            total_p = []
            functions.time_repeat(total_p)
        
            window["list"].update(values = total_p) # type: ignore
        case "Edit":
            # INDEX OF TIME AND LIST_SAVE
            index = compiled.index(f"{values["list"][0]}")
            # LIST UPDATE
            local_list = functions.open_file()
            local_list[index] = values["todo"] + '\n' 
            functions.write_file(local_list)
            # TIME UPDATE
            local_time = functions.open_file(r"Todo project\Contents\time.txt")
            local_time[index] = time_global + '\n'
            functions.write_file(local_time , r"Todo project\Contents\time.txt")
            # OVERALL SAVE
            edited_list = []
            functions.time_repeat(edited_list)
            window["list"].update(values = edited_list) # type: ignore

        case "Remove":
            
            index = compiled.index(f"{values["list"][0]}")

            todo = functions.open_file()
            time_ = functions.open_file(listfile=FILEPATH_TIME)

            todo.pop(index)
            time_.pop(index)

            functions.write_file(todo)
            functions.write_file(time_ , listfile=FILEPATH_TIME)

            edited_list = []
            functions.time_repeat(edited_list)
            window["list"].update(values = edited_list) # type: ignore

            print(compiled)
            print(values["list"][0])

            continue

        case pg.WIN_CLOSED:
            break
window.close()

