# 無限 參數資料
def avg(*ns):
    sum = 0
    for n in ns:
        sum = sum + n
    print(sum/len(ns))

avg(1,2,3,4)
avg(5,3,6,8,9)
avg(-1,-6,5,8,-3)        
