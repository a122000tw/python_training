 # a = 14
 # b = 1144 
 # a < b
 # 偶數總和

a = int(input("請輸入兩個正整數(a、b, 且a<b): \n"))
b = int(input())
if a > b:
    print("錯誤, a < b")
else:
    sum = 0
    for x in range(a, b+1):
        if x % 2 == 0:
            sum = sum + x
    print(sum)        
