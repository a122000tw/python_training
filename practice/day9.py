class Calc:
    name = "Good calculator"
    price = 18
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
print(Calc().minus(10,11))
    