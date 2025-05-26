"""test_list = [{'gfg': 4, 'is': '', 'best': []},{'I': {}, 'like': 5, 'gfg':2}]
final= []
dict1 = {}
for ele in test_list:
    for k,v in ele.items():
        if v:
            dict1[k]=v
final.append(dict1)
print(final)"""

#count frequency of elements

"""from collections import defaultdict
input_list = ['apple','banana','apple','orange','apple','orange']
my_dict = defaultdict(int)
cnt = 1
for x in input_list:
    if x in my_dict:
        cnt=my_dict.get(x)
        cnt+=1
        my_dict[x]=cnt
    else:
        cnt = 1
        my_dict[x]=cnt

print(my_dict)"""


#merge two dictionaries into one

"""dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {}
for k,v in dict1.items():
    dict3[k] = v
for k1,v1 in dict2.items():
    dict3[k1] = v1
print(dict3)"""

#check if key exists

"""person = {'name': 'Alice','age': 30,'city':'New York'}
p = {}
for k in person.keys():
    if k == 'name1':
        p[k]=person.get(k)

print(p)"""

"""sample_dict = {'a': 10,'b':20,'c':30}
sum = 0
for v in sample_dict.values():
    sum+=v
print(sum)"""


"""list1 = ['a','b','c']
list2 = [1,2,3]
list3 = []
for x in zip(list1,list2):
    list3.append(x)

final_dict = {}
for x in list3:
    final_dict[x[0]]=x[1]

print(final_dict)"""

student = {
    'name': 'John',
    'grades': {'math':88,'science':92}
}

print(student["grades"]["math"])