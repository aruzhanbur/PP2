import re

#task1
p = re.compile("^a[b]*")
m = p.search("abbbb")
print(m.group())

#task2
p = re.compile("\w*[a]{1}[b]{2,3}")
m = p.search("zzzzabbbbbbb")
print(m.group())

#task3
p = re.compile("[a-z]*[_][a-z]*")
m = p.search("aboba_aboba")
print(m.group())

#task4
p = re.compile("[A-Z]{1}[a-z]*")
m = p.search("Banananaaaaaa")
print(m.group())

#task5
p = re.compile("\w[a]{1}\w*b$")
m = p.search("Banananaaaaaab")
print(m.group())

#task6
x = "Hello. My name is Aruzhan."
y = re.sub('[ ,.]', ':', x)
print(y)

#task7
def snamle(x):
   x = re.sub(r'_([a-zA-Z])', lambda match: match.group(1).upper(), x)
   return x

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
