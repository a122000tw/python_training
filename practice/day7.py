apple = 100
a = None

def fun():
    global a
    a = 10
    print(a)
    return a + 100
print(apple)
print(a)
# print(fun())
print(a)    
