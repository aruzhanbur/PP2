#task1
ingr = int(input())
def conv(ingr):
    return 28.3495231 * ingr
y = conv(ingr)
print(y)

#task2

def conv(temp):
    return (5 / 9) * (temp - 32)
y = conv(temp)
temp = int(input())
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
