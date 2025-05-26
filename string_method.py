"""def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_words("Hello world!").capitalize)


sentence = "Hello world!"
final = " ".join(sentence.split()[0])
print(final)


str1="Hello world"
str2="World"
#print(" ".join(str1.split()))
str1_new=" ".join(str1.split(" ")[::-1]).capitalize()
print(str1_new)
#str2_new = str1.split(" ")[0].lower()
#print(" ".join(str1_new.capitalize()+str2_new))


#Check if a string a apllindrome or not

word="Madam"
def pallindrome(str):
    return str[0:]==str[::-1].capitalize()

print(pallindrome(word))


def issymmetrical(str):
    mid = len(str) // 2
    if len(str) % 2 == 0:
        return str[:mid] == str[mid:]
    else:
        return str[mid+1:] == str[:mid]
    
#print(issymmetrical("MadaM"))



#Remove ith character from a string

s = "Hello World !"
#print(s.replace(" !",""))

s1="".join(list(filter(lambda c:c != ' ',s)))
#print(s1)

st = "geeks for geeks"
final = "".join(list(filter(lambda s:s != " ",st)))
#print(len(final))



str3="Hello Debayan"
print(str3[::-2])

str = "abaaba"
def check_pallindrom(s):
    return bool(s[0::] == s[::-1])

print(check_pallindrom(str))

s1 = "VISHAKSHI"
s2 = "VANSHIKA"


common_list = []
for str in s1:
    if str in s2:
        common_list.append(str)
print(len(set(common_list)))"""

"""import re
s = "geeksforgeeks is No.1 4"
print(re.findall(r'\d+', s))"""


str = "ABCDCDC"
substr = "CDB"
print(str.find(substr))

"""start = 0
cnt = 0
while start < len(str):
    pos = str.find(substr)
    if pos != -1:
        cnt +=1
        start = pos+1
    else:
        print(f"{substr}Substring is not found")

print(cnt)"""

"""pattern = "abba"
words = "cat dog dog cat"

word_list = words.split(" ")
print(word_list)

char_to_word = {}
word_to_char = {}
for char,word in zip(pattern, word_list):
    if char in char_to_word:
        if char_to_word[char] != word:
            print("False")
    else:
        char_to_word[char] = word
    
    if word in word_to_char:
        if word_to_char[word] != char:
            print("False")
        else:
            word_to_char[word] = char

print(char_to_word)"""

# First non repeating character in a string

"""from collections import OrderedDict,Counter
str = "ssaanto"
stack = []
my_dict = OrderedDict()
my_dict=Counter(str)
for k,v in my_dict.items():
    if v == 1:
        print(k)
        break"""

# Print if a string is pallindrome or not

"""def pallindrome(str):
    return str[0::] == str[::-1]

str = "madm"
print(pallindrome(str))"""

"""from collections import defaultdict
str1 = "listen"
str2 = "sient"

my_dict = defaultdict(list)
sum_str1 = 0
sum_str2 = 0
for i in str1:
    sum_str1+=ord(i)

for j in str2:
    sum_str2+=ord(j)

#print(sum_str1 == sum_str2)


alist = ['listen','silent','madam','mmdaa','abc','bc']
from collections import defaultdict
my_dict = defaultdict(list)
for word in alist:
    sorted_word="".join(sorted(word))
    my_dict[sorted_word].append(word)

final_list = []
for v in my_dict.values():
    if len(v) > 1:
        final_list.append(v)

#print(final_list)

#Capitalize the first letter of each word"""

