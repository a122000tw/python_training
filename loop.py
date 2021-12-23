# break
# n = 0
# while n < 5:
#     if n == 3:
#         break
#     print(n)
#     n += 1
# print("最後的n: ", n)

# continue
# n = 0
# for x in [0,1,2,3]:
#     if x % 2 == 0:
#         continue
#     print(x)
#     n += 1
# print("最後的n: ", n)

# else
# sum = 0
# for n in range(11):
#     sum += n
# else:
#     print(sum)

# 綜合範例
# 輸入9 得到3
# 輸入11 得到(沒有整數平方根)
n = input("請輸入正整數: ")
n = int(n)
for i in range(n): # i 0 ~ n-1
    if i * i == n:    
        print("整數平方根", i)
        break # break 強制結束迴圈, 不會執行 else 區塊
else:
    print("沒有整數平方根")    

