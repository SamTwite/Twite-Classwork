# nCr Calc

def calc(n):
    if n == 0 :
        return 1
    else:
        return n * calc(n - 1)
    #endif
#end function


# Enter n
a = 1022
# Enter r
b = 500


# N- R
c = a-b
d = calc(c)* calc(b)

print("The Co-efficient for the certain value is value is:")
print(calc(a)/d)


print("Click enter to see all co-effiecents")
input()

for r in range(a+1):
    print(calc(a)/(calc(r)*calc(a-r)))
    r = r +1
#End
