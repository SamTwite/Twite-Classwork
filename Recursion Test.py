def calc(n):
    if n == 0 :
        return 1
    else:
        return n * calc(n - 1)
    #endif
#end function
print("Enter the number you want to find the factorial for:")
var = input()
var = int(var)
print(calc(var))

