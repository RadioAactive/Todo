from functions import open_file , write_file
import time

time_global = time.strftime("%m %b %d, %y")

while True:
    print("======MAIN MENU======") 
    user_Action = input("Type Show , Add , Edit , Remove\n")
    user_Action = user_Action.lower().strip()
    
    if user_Action.startswith("add"):
        
        add = user_Action[4:]
        add = add + "\n"
                
        todo = open_file()

        todo.append(add)
                
        write_file(todo)

        #time storage

        time_contants = open_file("Todo project/time.txt")
        
        time_contants.append(time_global + "\n")

        write_file(time_contants , "Todo project/time.txt")

    elif user_Action.startswith("edit"):
        try:    
            user_Action =  int(user_Action[5:])
            user_Action =  user_Action - 1

            todo = open_file()

            if todo == []:
                print("There is nothing in the list to edit")

            edit = input("What do you want to replace it with? ")
            
            todo[user_Action] = edit  + '\n'
        
            write_file(todo)

        except ValueError:
                print("Invalid command, try using an integer.")
                continue
        except IndexError:
             print("There is no item in that number, try again!")
             continue
        
    elif user_Action.startswith("remove"):
        try:
            if user_Action == "remove all":
                write_file("")
                write_file("" , "Todo project/time.txt")
                print("Contents have been deleted")
        
            else:
                user_Action =  int(user_Action[7:]) - 1

                todo = open_file()
                
                new_todo = todo[user_Action].strip("\n")
                print(f"'{new_todo}' have been removed")
                todo.pop(user_Action)
                
                write_file(todo)
        
        except ValueError:
                print("Invalid command, try using an integer.")
                continue
        except IndexError:
            print("There is no item in that number, try again!")
            continue
        
    match user_Action:
       
        case "show" | "1":
            print("======YOUR LIST======")
            
            todo = open_file()

            if todo == []:
                print("There is nothing in the list")
            else:
                time_contants = open_file("Todo project/time.txt")
                time_contants = [remove.strip("\n") for remove in time_contants]

                new_item = [item.strip("\n") for item in todo]

                for i , lists in enumerate(new_item):
                    row = f"{i + 1}.{lists.capitalize()}"
                    if time_global == time_contants[i]:
                        print(row ,f"-- added Today")

                    elif time_global[0:2] == time_contants[i][0:2] and time_global[11:13] == time_contants[i][11:13]:
                        if int(time_global[7:9]) == int(time_contants[i][7:9]) + 1:
                            print(row ,f"-- added yesterday")

                    else:
                        print(row ,f"-- added on {time_contants[i]}")
                    
        case "exit" | "4":
            print("Exitting...")
            break
        case "help":
            help()
        case _:
            print("If you need help then type help in terminal")