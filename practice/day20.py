try:
 file = open("../eeee", 'r+')
except Exception as e:
    print("there is no file named as eeee")
    response = input('do you want to create a new file(y / n)')
    if response == 'y':
        file = open('../eeee', 'w')
    else:
        pass
else:
    file.write('sssss')
file.close()