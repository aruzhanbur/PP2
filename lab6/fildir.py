import os
import sys
from pathlib import Path
import string
import shutil

#task1
x1 = "/Users/aruzhanb/Documents/PP2"
y1 = os.listdir(x1)
print(y1)

#task2
x2 = os.access("paw.txt", os.F_OK)
print("Exists the path:", x2)

y2 = os.access("paw.txt", os.R_OK)
print("Access to read the file:", y2)

z2 = os.access("paw.txt", os.W_OK)
print("Access to write the file:", z2)

w2 = os.access("paw.txt", os.X_OK)
print("Check if path can be executed:", w2)

#task3
x3 = os.access("paw.txt", os.F_OK)
print("Exists the path:", x3)
z3 = os.path.dirname("paw.txt") 
print(z3)

#task4
with open("paw.txt", "r") as fp:
    x4 = len(fp.readlines())
    print('Total Number of lines:', x4)

#task5
names = ["Aruzhan", "Bekzhan", "Baklazhan", "Zhanbek"]
with open("paw.txt", "w") as fr:
    fr.write("\n".join(names))

#task6
for x in string.ascii_uppercase:
    name = x + ".txt"
    f = open(name, "x")
    f.close()

#task7
shutil.copy('paw.txt', 'A.txt')

#task8
def delfel(x):
    if os.path.isfile(x) and os.access(x, os.F_OK):
        os.remove(x)
        print("Good")
    else:
        print("File does not exist or no access to the file.")

x = "Z.txt"  
delfel(x)
