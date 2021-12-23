a = [1, 2, 3]
b = [4, 5, 6]
c = zip(a, b)
print(c)
d = list(zip(a, b))
print(d)

for i, j in zip(a, b):
    print(i/2, j*2)

def fun1 (x, y):
    return x + y
print(fun1(1, 2))

fun2 = lambda x, y: x + y
print(fun2(2, 3))

print(map(fun1 , [1], [2]))
print(list(map(fun1, [1], [2])))
print(list(map(fun1, [1,2], [2,3])))