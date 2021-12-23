# 3 or 5 time

x = int(input("請輸入一個正整數: "))
if ((x % 5 == 0) & (x % 3 == 0)):
    print(x,"is a multiple of 3 and 5.")
elif x % 5 == 0:
    print(x,"is a multiple of 5.")
elif x % 3 == 0:
    print(x,"is a multiple of 3.")
else:
    print(x,"is not a multiple of 3 and 5.")       

