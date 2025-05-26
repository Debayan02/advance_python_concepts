#### Code for re.findall ####
"""import re
pattern = "aba"
s2 = "cabacabad"
cnt = 0
print(len(re.findall(pattern,s2)))"""



##### Code for re.search() #####
import re
pattern = '[",","."]'
string = 'The,House numbeR is 1234.'
str_list = []
for s in string.split(" "):
    if re.search(pattern, s):
        print("Match is found")
        str_list.append(s)
    else:
        print("No match found")

print(str_list)

"""### print the no of occurences of a substring ####

str = "GeeksforGeeksforGeeksforGeeks"
substr = "GeeksforGeeks"
start = 0
count = 0
while start < len(str):
    pos = str.find(substr, start)
    if pos != -1:
        start = pos + 1
        count += 1
    else:
        break


#print(count)

#### Count the no of vowels in a sentence ####
import re
str = "My name is Debayan and I am a hero"
pattern = '["a","e","i","o","u","I"]'
cnt = 0

#print(re.findall(pattern, str))"""

### Count the occurence of a substring ###
"""str = "GeeksforGeeksforGeeksforGeeks"
substr = "GeeksForGeeks"
count = 0
start = 0
while start < len(str):
    pos = str.find(substr, start)
    if pos != -1:
        start =pos + 1
        count +=1
    else:
        break

print(count)

### Possible substring count in a string ####
from collections import Counter
inp_str = "geksefokesgergeeks"
arg_str = "geeks"
temp1=Counter(inp_str)
temp2=Counter(arg_str)
for char in temp2:
    res = temp1[char] // temp2[char]
print(res)"""