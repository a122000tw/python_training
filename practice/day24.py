char_list = ['a', 'b', 'c', 'c', 'd', 'd']
sentence = 'Welcome Back to This Tutorial'

# print(set(char_list))
# print(type(set(char_list)))
# print(set(sentence))

unique_char = set(char_list)
unique_char.add('x')
# unique_char.clear()
# unique_char.remove('x')

set1 = unique_char
set2 = {'a', 'e', 'i'}
print(set1.difference(set2))
print(set1.intersection(set2))

# print(unique_char)