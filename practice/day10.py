class Calc:
    name = "Good calculator"
    price = 18

    def __init__(self, name, price, hight, length, weight):
        self.name = name
        self.price = price
        self.hight = hight
        self.len = length
        self.w = weight

    def add(self, x ,y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self, x, y):
        result = x - y
        print(result)
    def times(self, x, y):    
        result = x * y
        print(result)
    def divide(self, x, y):
        result = x / y
        print(result)    

# c = Calc()
# print(c.price)
# print(Calc().minus(10,11))

c = Calc("Bad Calculator", 18, 30, 20, 10)
print(c.name, c.price, c.w)