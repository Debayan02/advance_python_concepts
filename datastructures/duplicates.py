#Dictionary is a collection of {key:value} pairs which is ordered and changeable.No duplicates.

"""capitals = {"USA" : "Washington",
            "Russia" : "Moscow",
            "India" : "New Delhi",
            "Bangladesh" : "Dhaka",
            "Pakistan" : "Islamabad"}

for cap in capitals:
    print(cap)

print("-------------Keys-----------------")
print(capitals.keys())
for key in capitals.keys():
    print(key,type(key))

capitals.update({"India" : "Bangalore"})
capitals.pop("Pakistan")
print(capitals)
capitals.popitem()
print(capitals)"""

#Find the key which is having maximum unique numbers in the values

"""def max_unique():
    test_dict = {"Gfg": [5, 7, 5, 4, 5],
             "is": [6, 7, 4, 3, 3],
             "Best": [9, 9, 6, 5, 5]}

    max_key = None
    max_val = 0
    for sub in test_dict:
        print(sub)
        if len(set(test_dict[sub])) > max_val:
            max_val=len(set(test_dict[sub]))
            max_key=sub
    return max_key

res=max_unique()
print(f"{res} has the maximum no of unique keys")"""


#Find all duplicate characters in a string:

"""s = "GeeksForGeeks"

s_dict = {}
cnt = 0
for char in s:
    if char in s_dict:
        cnt+=1
        s_dict.update({char:cnt})
    else:
        cnt=1
        s_dict.update({char:cnt})
print(s_dict)
for keys,values in s_dict.items():
    if values > 1:
        print(f"{keys} has {values} no of duplicate characters")
    else:
        print(f"{keys} doesn't have duplicate and contain {values} no of character")


result = lambda a : a*a
print(result(5))"""





"""test_dict = {"Gfg": [5, 7, 5, 4, 5,0,1],
             "is": [6, 7, 4, 3, 3,88,91,1000],
             "Best": [9, 9, 6, 5, 5]}


max_key = None
max_val = 0
for key,value in test_dict.items():
    if len(set(value)) > max_val:
        max_val = len(set(value))
        max_key = key
print("Max value :",max_val)
print("Max Key :", max_key)"""


test_dict = {"Gfg": [5, 7, 5, 4, 5],
             "is": [6, 7, 4, 3, 3],
             "Best": [9, 9, 6, 5, 5]}

max_length = 0
final_dict = {}
for key,value in test_dict.items():
    if len(set(value)) > max_length:
        max_length = len(set(value))
        max_key = key
final_dict[max_key] = max_length

print(final_dict)