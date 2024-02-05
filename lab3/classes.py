#task1
class strdo():
    def __init__(self):
        self.inp = ""
        
    def getstr(self):
        self.inp = input("")
        
    def prstr(self):
        print(self.inp.upper())
        
r = strdo()
r.getstr()
r.prstr()

#task2
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length ** 2

length_of_square = float(input())
x = Square(length_of_square)
y = Shape()

print("Area of Shape:", y.area())   
print("Area of Square:", x.area())  
