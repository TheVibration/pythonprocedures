# a procedure that takes in a list
# of integers and outputs the greatest
# number in the list

def greatest(list_of_numbers):
    holder = 0
    for i in list_of_numbers:
        if i > holder:
            holder = i
    return holder
