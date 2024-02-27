import re

with open("row.txt", "r") as file:
    lines = file.readlines()

#task1
p = re.compile("^a[b]*")
print("Output for task1: ")
for line in lines:
    for word in line.split():
        if p.match(word):
            print(word)
print()


#task2
p2 = re.compile("a[b]{2,3}")
print("Output for task2: ")
for line in lines:
    for word in line.split():
        if p2.match(word):
            print(word)
print()

#task3
p3 = re.compile("[a-z]*[_][a-z]*")
print("Output for task3: ")
for line in lines:
    for word in line.split():
        if p3.match(word):
            print(word)
print()

#task4
p4 = re.compile("[A-Z][a-z]+")
print("Output for task4: ")
for line in lines:
    for word in line.split():
        if p4.match(word):
            print(word)
print()

#task5
p5 = re.compile("\w[a]\w*b$")
print("Output for task5: ")
for line in lines:
    for word in line.split():
        if p5.match(word):
            print(word)
print()

#task6
new = []
print("Output for task6: ")
for line in lines:
    dodo = re.sub(r'[ ,.]', ':', line)
    new.append(dodo)

r = ''.join(new)
print(r)

#task7
def snamle(x):
   x = re.sub(r'_([a-zA-Z])', lambda match: match.group(1).upper(), x)
   return x
print("Output for task7: ")
y = "Doner_sperchikom"
result = snamle(y)
print(result)

#task8
def spl(input_str):
    return re.findall('[A-Z][^A-Z]*', input_str)

x = "SplitThisStringAtUppercaseLetters"
result = spl(x)
print(result)

#task10
x = 'CamelCaseName'
x = re.sub(r'(?<!^)(?=[A-Z])', '_', x).lower()
print(x)
