# break continue

a = True
while a:
    b = input('type something')
    if b == '1':
        continue # 忽略剩下程式 重新回圈
    else:
        pass
    print('still in while')

print("Stop")
