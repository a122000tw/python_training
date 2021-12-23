# def say(msg):
#     print(msg)
# say("Hello function")
# say("Hello Python")

# def add(n1, n2, n3):
#     result = n1 + n2 + n3
#     return result
# print(add(1,2,3))

# 函式可用來做程式的包裝: 同樣的邏輯可以重利用
def calc(max):
    sum = 0
    for x in range(1, max+1):
        sum += x
    print(sum)

calc(10)
calc(20)        

