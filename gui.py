import PySimpleGUI as pg

label = pg.Text("Enter a todo")
input_module = pg.InputText(tooltip="Enter TODO")
add_button = pg.Button("Add")

window = pg.Window("Todo" , layout=[[label],[input_module , add_button] ])
window.read()
window.close()

