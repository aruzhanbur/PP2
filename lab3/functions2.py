#task1
def higher(y):
    if y > 5.5:
        return True
    return False

x = input()
y = int((input()))
if higher(y):
    print("Yes")
else:
    print("No")

#task2
def higher(m):
    r = [x for x in m if float(x.get('imbd', 0)) > 5.5]
    return r

ml = [
    {'first': 'name1', 'imbd': '5.4'},
    {'second': 'name2', 'imbd': '8.0'},
    {'third': 'name2', 'imbd': '5.7'},
    {'fourth': 'name4', 'imbd': '4.2'}
]

z = higher(ml)
print(z)

#task3
def higher(m):
    r = [x for x in m if x.get('category', 0) == 'soap opera']
    return r

ml = [
    {'first': 'name1', 'imbd': '5.4', 'category': 'soap opera'},
    {'second': 'name2', 'imbd': '8.0', 'category': 'thriller'},
    {'third': 'name2', 'imbd': '5.7', 'category': 'soap opera'},
    {'fourth': 'name4', 'imbd': '4.2', 'category': 'horror'}
]

z = higher(ml)
print(z)

#task4
def calcavg(m):
    if not m:
        return 0
    x = [float(z.get('imbd', 0)) for z in m]
    avg = sum(x)/len(x)
    return avg
    
ml = [
    {'first': 'name1', 'imbd': '5.4', 'category': 'soap opera'},
    {'second': 'name2', 'imbd': '8.0', 'category': 'thriller'},
    {'third': 'name2', 'imbd': '5.7', 'category': 'soap opera'},
    {'fourth': 'name4', 'imbd': '4.2', 'category': 'horror'}
]

z = calcavg(ml)
print(z)

#task5
def higher(m):
    r = [x for x in m if x.get('category', '') == 'soap opera']
    return r

def calcavg(m):
    if not m:
        return 0
    x = [float(z.get('imbd', 0)) for z in m]
    avg = sum(x) / len(x)
    return avg

ml = [
    {'first': 'name1', 'imbd': '5.4', 'category': 'soap opera'},
    {'second': 'name2', 'imbd': '8.0', 'category': 'thriller'},
    {'third': 'name2', 'imbd': '5.7', 'category': 'soap opera'},
    {'fourth': 'name4', 'imbd': '4.2', 'category': 'horror'},
    {'fifth': 'name5', 'imbd': '7.2', 'category': 'soap opera'}
]

z = higher(ml)
avgz = calcavg(z)
print(avgz)