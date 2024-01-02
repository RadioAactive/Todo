
def open_file(listfile = "Todo project/list_save"):
     """ Scans the selected file and make the contants as a list"""
     with open(listfile , "r") as list_local:
          todo_local = list_local.readlines()
     return todo_local

def write_file( specify_varible , listfile = "Todo project/list_save"):
     """ Overwrites a file when a todo list is updated"""
     with open(listfile , "w") as list_local:
             list_local.writelines(specify_varible)

def help():
      print("""1.Show\n
2.Add\n
3.Edit\n
4.Remove""")
      help_index = int(input("What do you want help with? "))
      if help_index == 1:
           return print("Shows the list by typing 'show' in the terminal")
      elif help_index == 2:
           return print("Adds contants written in terminal by typing 'add [your task]")
      elif help_index == 3:
           return print("Edits your task by typing 'edit [your task number]")
      elif help_index == 4:
          return print("Removes your task by typing 'remove [your task number]' or remove everything by typing 'remove all")
        