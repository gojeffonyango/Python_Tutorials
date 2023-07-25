#calculator for quadratic equations
import math
#ax**2+bx+c=0

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

d = b**2-4*a*c

if d<0:
    print("Sorry theres no solution for your input, try again please")
elif d == 0:
    x = (-b)/(2*a)
    print("This equation has no solution,please give a new input" , x)
else:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print("This equation has two solutions:" ,x1, "or" ,x2)
