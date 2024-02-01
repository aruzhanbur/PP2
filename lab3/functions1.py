#task1
ingr = int(input())

def conv(ingr):
    return 28.3495231 * ingr

y = conv(ingr)
print(y)

#task2
temp = int(input())

def conv(temp):
    return (5 / 9) * (temp - 32)

y = conv(temp)
print(y)

#task3
def solve(numheads, numlegs):
    r = (numlegs - 2 * numheads) / 2
    r = int(r)
    c = numheads - r
    print("Number of chicken:", c)
    print("Number of rabbit:", r)

numheads = 35
numlegs = 94
solve(numheads, numlegs)

#task4
import math

def filter_prime(k):
    for x in range(len(k)):
        a = int(k[x])
        yes = True
        if a < 2:
            yes = False
        for y in range(2, int(math.sqrt(a)) + 1):
            if a % y == 0:
                yes = False
                break
        if yes:
            print(a)
            
z = input()
k = [int(w) for w in z.split()]
filter_prime(k)

#task5
from itertools import permutations

def perm(s):
    z = set(permutations(s))
    for x in z:
        print(''.join(x))
        
y = input()
perm(y)

#task6
def rev(s):
    ss = s.split()
    rever = ' '.join(reversed(ss))
    print(rever)

s = input()
rev(s)

#task7
def has33(x):
    for i in range(len(x) - 1):
        if x[i] == 3 and x[i + 1] == 3:
            return True
    return False
            
y = input()
x = [int(z) for z in y.split()]
if has33(x):
    print('true')
else:
    print('false')

#task8
def has007(x):
    for i in range(len(x) - 1):
        if x[i] == 0 and x[i + 1] == 0 and x[i + 2]:
            return True
    return False
            
y = input()
x = [int(z) for z in y.split()]
if has007(x):
    print('true')
else:
    print('false')

#task9
def vol(r):
    z = (4 / 3) * 3.14 * r * r * r
    print(z)
    
r = int(input())
vol(r)

#task10
def un(z):
    result = []
    for x in z:
        if x not in result:
            result.append(x)
    return result

x = list(input())
result = un(x)
print(result)

#task11
def pal(s):
    if s == s[::-1]:
        return True
    return False

s = str(input())
if pal(s):
    print("palindrome")
else:
    print("not palindrome")

#task12
def histogram(y):
    for q in x:
        print("*" * q)

y = input()
x = [int(w) for w in y.split()]
histogram(y)

#task13
import random

def game():
    print("Hello! What is your name?")
    name = input()
    print("Well, {}, I am thinking of a number between 1 and 20.".format(name))
    x = random.randint(1, 20)
    count = 0 
    while True:
        print("Take a guess.")
        y = int(input())
        count += 1
        if y < x:
            print("Your guess is too low.")
        elif y > x:
            print("Your guess is too high.")
        else:
            print("Good job, {}! You guessed my number in {} guesses!".format(name, count))
            break

game()


