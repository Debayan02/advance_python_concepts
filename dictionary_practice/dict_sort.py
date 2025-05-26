"""d = {2:56, 100:2, 3:333}
d1 = {}
print(sorted(d.values()))

#Handling mising keys in dictionary

ele = {'a': 5, 'c': 7, 'e': 10}
for i in ele:
    print("----This is I----------")
    print(i)
    if 'q' in i:
        print(ele["q"])
    else:
        print("Key not found")

#Remove elements with empty value fro the list of dictionary

test_list = [{'gfg': 4, 'is': '', 'best': []},{'I': {}, 'like': 5, 'gfg':0}]
final_dict= {}
final= []
for ele in test_list:
    for k,v in ele.items():
        if v:
            final_dict[k]=v
            final.append(final_dict)
            final_dict={}
print(final)



list = [{'name': "Nandini", 'age': 10},
        {'name': "Manjeet", 'age': 20},
        {'name': "Nikhil", 'age': 19}]

final_list = []
final_dict = {}
list.sort(key = lambda x: x["age"])
print(list)


alist = ['apple','guava','chiku','pomegranet']
alist.sort(key = lambda x: x[-1])
print(alist)
alist.sort(key=len)
print(alist)"""



"""d = {'ravi': 10, 'abhinav': 18, 'sanjeev': 15}
d2 = {}
ages = []
for k,v in d.items():
    ages.append(v)


for item in d.items():
    print(item[1])
sorted_by_values = dict(sorted(d.items(),key=lambda item : item[1]))
print(sorted_by_values)


sorted_by_keys = dict(sorted(d.items(), key=lambda item: item[0]))
print(sorted_by_keys)


test_dict = {"Gfg":5, "is": 7, "Best": 2}
print(dict(sorted(test_dict.items(),key=lambda item:item[1])))"""


blist = [1,8,10,4,3]
blist.sort(key=lambda x:x,reverse=True)
#print(blist)

d = {'ravi': 10, 'abhinav': 18, 'sanjeev': 15}
new_dict = dict(sorted(d.items(),key=lambda item : item[1],reverse=True))
#print(new_dict)


data = {'banana':3,'apple':4,'peer':1,'orange':2}

data2 = dict(sorted(data.items(), key=lambda item:item[1], reverse=True))
#print(data2)


data3 = [1,5,3,9,10,4]
print(sorted(data3,key=lambda x:x,reverse=True))