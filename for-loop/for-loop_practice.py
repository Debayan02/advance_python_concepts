"""for i in range(1,21,2):
    if i == 13:
        continue
    else:
        print(i)"""

"""str="helloworld"
for i in str:
    print(i)"""

#output:-[h,e,l,o,w,r]
"""str="synoppsiis"
final_str=""
prev=[]
print(type(prev))
for x,z in enumerate(str):
    if z in prev:
        continue
    else:
        prev.append(z)

for i in prev:
    final_str+=i

print(final_str)"""


#python code for finding the first occurence of non repeating character in string
"""str = "Text"
count = {}
for char in str.lower():
    cnt=1
    if char not in count:
        count[char]=cnt
    else:
        count[char]=cnt+1

print(count)

ind=0

for key,val in count.items():
    if val == 1:
        print(str.index(key))
        break"""

"""list1 = [1,2,5,8,10]
list2 = [2,4,6,7,9]
list3 = []

#print(sorted(list1+list2))
i=0
j=0

while list1 or list2:
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            #print(i,j)
            list3.append(list1[i])
            print(list3)
            list1.pop(i)
            i+=1
        else:
            #print(i,j)
            list3.append(list2[j])
            list2.pop(j)
            j+=1

print(list3)"""

