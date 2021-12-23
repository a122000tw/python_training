# print(23.12)
# print(395.3)
# print(100.4617)
# print(564.329)

n1 = float(input("請輸入四個浮點數: \n"))
n2 = float(input())
n3 = float(input())
n4 = float(input())

print('|{0:>7.2f}{1:>7.2f}|'.format(n1, n2))
print('|{0:>7.2f}{1:>7.2f}|'.format(n3, n4))
print('|{0:<7.2f}{1:<7.2f}|'.format(n1, n2))
print('|{0:<7.2f}{1:<7.2f}|'.format(n3, n4))
