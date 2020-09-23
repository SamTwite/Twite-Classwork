verification = False
num = 0
times_table = 0
count = 1
num_valid = False
times_table_valid = False

num = input("Enter a number you want for the times tables, make sure the number is an integer:")
if num.isdigit():
    num_valid = True
    yes_no = input("Are you sure you want to continues with the number you just entered? [answer yes or no]")
    
    if yes_no == "yes":
        verification = True
    if yes_no== "no":
        verification = False
        num_valid = False

while not num_valid:
    num = input("Please Re-enter the number you want, make sure it is an integer:")
    if num.isdigit():
        num_valid = True
    while not verification and num_valid:
        yes_no = input("are you sure you want to procede with the number you judt entered? [answer yes or no]")
        if yes_no == "yes":
            verification = True
            num_valid = True
        if yes_no == "no":
            verification = False
            num_valid = False

times_table = input("Enter a number you want for the times tables, make sure the number is an integer:")
if times_table.isdigit():
    times_table_valid = True
    yes_no = input("Are you sure you want to continues with the number you just entered? [answer yes or no]")
    
    if yes_no == "yes":
        verification = True
    if yes_no== "no":
        verification = False
        times_table_valid = False

while not times_table_valid:
    times_table = input("Please Re-enter the number you want, make sure it is an integer:")
    if times_table.isdigit():
        times_table_valid = True
    while not verification and times_table_valid:
        yes_no = input("are you sure you want to procede with the number you judt entered? [answer yes or no]")
        if yes_no == "yes":
            verification = True
            times_table_valid = True
        if yes_no == "no": 
            verification = False
            times_table_valid = False
num = int(num)
times_table = int(times_table)
while count < times_table:
    print(num * count)
    count = count +1       
    
    
    



print("end")


    


