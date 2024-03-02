#task1
from functools import reduce

def umn(n):
    return reduce(lambda x, y: x * y, n)

n = input().split()
n = [int(x) for x in n]
r = umn(n)
print(r)

#task2
def counter(ss):
    u = sum(1 for x in ss if x.isupper())
    l = sum(1 for x in ss if x.islower())
    return u, l

s = input()
u, l = counter(s)
print(u)
print(l)

#task3
s = input()
if s == s[::-1]:
    print("yes")
else:
    print("no")

#task4
import math
import time 

def res(x, t):
    time.sleep(t / 1000)
    r = math.sqrt(x)
    return r

x = int(input())
t = int(input())
z = res(x, t)
print(f"Square root of {x} after {t} milliseconds is {z}")

#task5
t = input().split() 
t = tuple(bool(x) for x in t)
print(all(t)) 
