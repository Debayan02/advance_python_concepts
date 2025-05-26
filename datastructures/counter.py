"""from collections import Counter
a = [1,2,3,4,2,2,2,3,43,9,1,1,1,5,5]
print(Counter(a))

data_list = [{"name": "Nandini","age": 20}, {"name" : "Debayan","age": 34},{"name": "Koustav", "age": 25}]
print(sorted(data_list, key = lambda x: x['age'], reverse = True))

data_list2 = [2,6,7,10,3,8]
print(sorted(data_list2, key= lambda x: x, reverse = True))

data_list2 = [[4,11],[4,10],[6,7],[8,9]]
print(sorted(data_list2, key=lambda x: (x[0],x[1]), reverse = True))

data_list = [{"name": "Nandini","age": 20}, {"name" : "Debayan","age": 34},{"name": "Koustav", "age": 25}]
print(sorted(data_list, key = lambda x : x["age"], reverse=True))"""

from collections import defaultdict
ana_list = ['eat','ate','tea','silent','listen','mad','dam','aam','padu']
anagram_dict = defaultdict(list)
for words in ana_list:
    sorted_word="".join(sorted(words)) 
    #print(sorted_word, words)
    anagram_dict[sorted_word].append(words)

for k,v in anagram_dict.items():
    if len(v) > 1:
        print(v)