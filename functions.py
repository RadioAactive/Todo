
def open_file(listfile = "Todo project/Contents/list_save"):
     """ Scans the selected file and make the contants as a list"""
     with open(listfile , "r") as list_local:
          todo_local = list_local.readlines()
     return todo_local

def write_file( specify_varible , listfile = "Todo project/Contents/list_save"):
     """ Overwrites a file when a todo list is updated"""
     with open(listfile , "w") as list_local:
             list_local.writelines(specify_varible)

def app_help():
      print("""1.Show
2.Add
3.Edit
4.Remove""")
      while True:
          help_index = int(input("What do you want help with? "))
          match help_index:
               case 1 | "show":
                    print("Shows the list by typing 'show' in the terminal")
               case 2 | "add":
                    print("Adds contants written in terminal by typing 'add [your task]")
               case 3 | "edit":
                    print("Edits your task by typing 'edit [your task number]")
               case 4 | "remove":
                    print("Removes your task by typing 'remove [your task number]' or remove everything by typing 'remove all")
          
          ask = input("Need help with something else y/n")
          if ask == "y":
               continue
          elif ask == "n":
               break
          else:
               print("not a valid response")
               break
               
        