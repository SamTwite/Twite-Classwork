a,b,c = input("Enter the coefficients of a, b and c separated by commas: ")

d = b**2-4*a*c # discriminant

if d < 0:
    print("This equation has no real solution")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print("This equation has one solutions: ", x)
else:
    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
    print("This equation has two solutions: ", x1, " and", x2)
