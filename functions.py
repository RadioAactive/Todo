import time

def open_file(listfile = r"Todo project\Contents\list_save.txt"):
     """ Scans the selected file and make the contants as a list"""
     with open(listfile , "r") as list_local:
          todo_local = list_local.readlines()
     return todo_local

def write_file( specify_varible , listfile = r"Todo project\Contents\list_save.txt"):
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

def time_repeat(in_lists):
    new_item = [item.strip("\n") for item in open_file()]           
    time_global = time.strftime("%m %b %d, %y")
    time_contants = open_file(r"Todo project\Contents\time.txt")
    time_contants = [remove.strip("\n") for remove in time_contants]


    for i , lists in enumerate(new_item):
          row = f"{i + 1}. {lists.capitalize()}"
          if time_global == time_contants[i]:
               in_lists.append(f"{row} -- added Today")

          elif time_global[0:2] == time_contants[i][0:2] and int(time_global[7:9]) == int(time_contants[i][7:9]) + 1:
               if time_global[11:13] == time_contants[i][11:13]:
                    in_lists.append(f"{row} -- added Yesterday")

          else:
               in_lists.append(f"{row} -- added on {time_contants[i][3:13]}")     
               
        