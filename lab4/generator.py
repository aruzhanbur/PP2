#task1
def gen(n):
    x = 1
    while x ** 2 < n:
        yield x ** 2
        x += 1

n = int(input())
for z in gen(n):
    print(z)

#task2
def gen(n):
    for x in range(0, n):
        if x % 2 == 0:
            yield x

n = int(input())
z = gen(n)
print(*z, sep = ",")

#task3
def divis(n):
    for x in range(0, n):
        if x % 3 == 0 and x % 4 == 0:
            yield x


n = int(input())
for z in divis(n):
    print(z)

#task4
def squares(a, b):
    for i in range(a, b):
        yield i ** 2

a, b = int(input()), int(input())
for x in squares(a, b):
    print(x)

#task5
def gen(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for z in gen(n):
    print(z)