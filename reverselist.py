# In order to reverse a list, the best
# way is to find a way to start from the end of the list and
# append the element into an originally empty list.
# To do this I used the range function. First start from 
# the end of the list by doing len(lst)-1. After wards the second
# parameter of the range function is -1 because I want to go until I 
# reach the 0th indexed element of the list. Lastly, the last parameter
# of range is -1 again to let it know to go backwards by 1.

def reverse_list(lst):
    reversed = []
    for i in range(len(lst)-1, -1, -1):
        reversed.append(lst[i])
    return reversed


list1 = [1,2,3,4,5]
list2 = ['a','b','c','d']
list3 = [1, [2,3], [4,5,6], [7,8,9,10]]

print("Original: ", list1)
print("Reversed: ", reverse_list(list1))

print("\nOriginal: ", list2)
print("Reversed: ", reverse_list(list2))

print("\nOriginal: ", list3)
print("Reversed: ", reverse_list(list3))
