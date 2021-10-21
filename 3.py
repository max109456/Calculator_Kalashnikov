import math

print("Введите первое число")
a = float(input())
print("Введите второе число")
b = float(input())

print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)
print(b, "-", a, "=", b-a)
print(a, "*", b, "=", a*b)
print(a, "/", b, "=", a/b)
print(b, "/", a, "=", b/a)
print(a, "^", b, "=", a**b)
print(b, "^", a, "=", b**a)
print("sin", a, "sin", b, "=", math.sin(a), math.sin(b))
print("cos", a, "cos", b, "=", math.cos(a), math.cos(b))
print(a, b, "=", str(a) + str(b))
