#shallow copy example
#if we change an element of old list the change will reflect in the new list as well
import copy
old_list = [[1,2],[3,4],[5,6,7]]
new_list = copy.copy(old_list)
old_list[1][1] = 10


print("old list :",old_list)
print("New list :",new_list)

old_list1 = [[1,2],[3,4],[5,6,7]]
new_list1 = copy.deepcopy(old_list1)
old_list1[1][1]=10
print("old list1 :", old_list1)
print("new list1 :", new_list1)
