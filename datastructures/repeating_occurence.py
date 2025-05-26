"""str = "misissipie"
char_dict = {}

occurence=0
for s in str:
    if s in char_dict:
        occurence=char_dict.get(s) + 1
        char_dict[s]=occurence
    else:
        occurence=1
        char_dict[s] = occurence

for k,v in char_dict.items():
    if v > 1:
        print(k)"""

def repeating_char(str):
    char_dict = {}
    occurence=0
    for s in str:
        if s in char_dict:
            occurence=char_dict.get(s) + 1
            char_dict[s]=occurence
        else:
            occurence=1
            char_dict[s] = occurence

    return char_dict

#print(repeating_char("misissipie"))

final_dict = {}
for k,v in repeating_char("misissipie").items():
    if v > 1:
        final_dict[k]=v


#print(final_dict)

"""str1 = "listen"
str2 = "silent"
from collections import Counter
print(Counter(str1) == Counter(str2))

from collections import defaultdict
words = ['eat','ate','tea','silent','listen']
anagram_dict = defaultdict(list)
for word in words:
    sorted_word = "".join(sorted(word))
    anagram_dict[sorted_word].append(word)

for x in anagram_dict.values():
    print(x)

from collections import defaultdict
def anagram_test(words):
    anagram_dict = defaultdict(list)
    for word in words:
        sorted_word = "".join(sorted(word))
        anagram_dict[sorted_word].append(word)
    return anagram_dict

words = ['eat','ate','tea','silent','listen']
print(anagram_test(words).values())"""


"""s = "{[()]}"
st = []
for c in s:
    if c in '{[(':
        st.append(c)
    elif c in '})]':
        if not st or (c == ')' and st[-1] != '(') or (c == '}' and st[-1] != '{') or (c == ']' and st[-1] != '['):
            print('False')
            break
            st.pop()
        else:
            print('True')



s = "{[()]}"
st = []
for c in s:
    if c in '{[(':
        st.append(c)
    elif c in ')]}':
        if  (c == ')' and st[-1] != '(') or (c == '}' and st[-1] != '{') or (c == ']' and st[-1] != '['):
            print('False')
            break
        else:
            print('True')"""


str = "missisipie"
final_dict = {}
cnt = 1
for s in str:
    if s in final_dict:
        cnt +=1
        final_dict.update({s:cnt})
    else:
        cnt = 1
        final_dict.update({s:cnt})

for k,v in final_dict.items():
    if v > 1:
        print("{k} has duplicate {v} no of values")
    else:
        print("{k} doesn't have duplicate")