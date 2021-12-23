a = [1, 2, 3, 4, 5, 6, 7, 2]

a.append(0)
a.insert(1, 10)
a.remove(2) #第一次出現的數值
# print(a[-1]) #list最後一位
print(a[1:6])
print(a.index(0))
print(a.count(4))
a.sort()
print(a)

