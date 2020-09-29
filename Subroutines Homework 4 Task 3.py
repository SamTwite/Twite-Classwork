
def displayMenu():
    menu = "1. Add name\n""2. Display list\n""3. Quit"
    choice = -1
    while choice < 1 or choice > 3:
        choice = int(input(menu))
    #end while
    return choice
#end function

name_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',]

def display(my_name_list):
    for name in my_name_list:
        print(name)
    #next name
#end procedure

def add_name(my_name_list):
    global name_list
    for index 0 to 9 
    new_name = (int(input("Enter the name you want to add to the list"))
        name_list[index] = input
           
    





choice = displayMenu()

if choice == 1:
    add_name(name_list)
    display(name_list)
if choice == 2:
    display(name_list)
#end if
    

    
    




    
    



