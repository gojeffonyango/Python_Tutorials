from random import randint
import sympy
from sympy.abc import b,c,d,B,C,r,x

B=10
C=20
r=123

# Equation: x^3+b*x^2+c*x+d=x^3+(B−r)x^2+(C−B*r)x−C*r
equation = sympy.Eq(x**3+b*x**2+c*x+d,x**3+(B−r)*x**2+(C−B*r)*x−C*r)

print(sympy.solve(equation,"b"))
print(sympy.solve(equation,"c"))
print(sympy.solve(equation,"d"))
