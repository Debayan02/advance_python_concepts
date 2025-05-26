"""#The below code is for filter
nums = [1,2,3,4,5,6,7,8]
evens = set(filter(lambda x : x%2 == 0,nums))
print(evens)

#The below code is for map
multi = list(map(lambda x : x*2, evens))
print(multi)

#The below code is for reduce
from functools import reduce
sum = reduce(lambda a,b : a+b,nums)
print(sum)

str = "Hello world!"
output = "World hello!"
from functools import reduce
words = list(map(lambda x:x.__reversed__,str))
print(words)
#sentence = reduce(lambda x,y: x+y,words)
#sentence2 = reduce(lambda x,y:y+x,sentence)
#print(sentence2)"""


#The below code is for filter
"""nums = [1,2,3,4,5,6,7,8]
evens = set(filter(lambda x : x%2 == 0,nums))
print(evens)"""

"""def find_even(nums):
    return nums % 2 == 0
#print(find_even([1,2,3,4,5,6,7,8]))
nums = [1,2,3,4,5,6,7,8]
even = list(filter(find_even,nums))
print(even)"""


"""str = "abbvcfdcknlwgfeq"
def do_upper(s):
    return s.upper()
alist = [s for s in str]
print(alist)
final_list = list(map(do_upper,alist))
print(final_list)"""

"""from collections import defaultdict
words = ['apple','banana','orange','cherry']
final_list = defaultdict(int)
for word in words:
    final_list[word]=len(word)
print(final_list)"""

"""words = ['apple','banana','orange','cherry']
def len_word(word):
    return len(word)

final_list = list(map(len_word,words))
print(final_list)


nos = [1,2,3,4,5,6,7]

def sq_nos(nos):
    return nos**2

final_list = list(map(sq_nos,nos))
print(final_list)"""

"""a = [1,4,5]
b = [2,4,6,9]
final_list = []
if len(b) < len(a):
    for i,v in enumerate(b):
        final_list.append((a[i]+b[i]))
else:
    for i,v in enumerate(a):
        final_list.append((a[i]+b[i]))

print(final_list)"""

"""words = ['cat','dog','sheep','horse']
final_list = []
for word in words:
    for index,char in enumerate(word):
        if index == 0:
            final_list.append(char)

print(final_list)"""

"""def first_char(word):
    for index,char in enumerate(word):
        if index == 0:
            return char
        
words = ['cat','dog','sheep','horse']
final_list = list(map(first_char,words))
print(final_list)"""


#Higher order Function
"""def square(x):
    return x*x

def cube(x):
    return x * x * x

def my_map(func,args):
    result = []
    for i in args:
        result.append(func(i))
    return result

cubes = my_map(cube,[1,2,3,4,5])
print(cubes)"""


#Hgher order function where a function is returned

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}<{0}>'.format(tag,msg))

    return wrap_text

print_h1 = html_tag("H1")
print_h1("First Headline")
print_h1("Second headline")