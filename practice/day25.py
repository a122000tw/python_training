import re
from typing import Pattern
# matching string
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(pattern1 in string)
print(pattern2 in string)

# regular expression
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(re.search(pattern1, string))
print(re.search(pattern2, string))

# multiple patterns ("run" or "ran")
ptn = r"r[au]n"
print(re.search(ptn, string))

# continue
print(re.search(r'r[A-Z]n', string))
print(re.search(r'r[a-z 0-9]n', string))

# \d : decimal digit
print(re.search(r'r\dn', "run r4n"))
# \D : any non-decimal digit
print(re.search(r'r\Dn', "run r4n"))

