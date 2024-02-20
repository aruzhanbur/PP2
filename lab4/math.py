import math

#task1
def torad(x):
    return (x * math.pi) / 180

x = int(input())
z = torad(x)
print(z)

#task2
def area(h, a, b):
    return ((a + b) * h) / 2

h, a, b = int(input()), int(input()), int(input())
z = area(h, a, b)
print(z)

#task3
def area(n, l):
    return ( n * pow(l, 2) ) / (4 * math.tan(math.pi / n))
    
n, l = int(input()), int(input())
z = area(n, l)
print(math.floor(z))

#task4
def area(b, h):
    return b * h
    
b, h = int(input()), int(input())
z = area(b, h)
print(z)