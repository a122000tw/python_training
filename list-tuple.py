# 有序可變動列表 List
grades=[12,60,15,70,90]
grades[0]=55 # 取代 12
print(grades)
print(grades[2])
print(grades[1:4])
grades[1:4]=[] # 連續刪除
print(grades)
grades += [12,33]
print(grades)
length = len(grades)
print(length)

# 巢狀列表
data = [[3,4,5],[6,7,8]]
print(data[0][1])

# 有序不可變動列表 Tuple
data=(3,4,5)
print(data[0:2])
