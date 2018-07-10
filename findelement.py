# find_element takes two inputs
# lst and v. lst is a list of 
# any type and v is a value of any
# type. find_element will go through
# lst and find the index at which 
# v exists. If v isn't in lst, -1
# will be returned.

def find_element(lst,v):
    counter = 0
    for i in lst:
        pos = i.find(v)
        if pos == -1:
            if counter == len(lst) -1:
                return -1
            else:
                counter = counter + 1
        elif pos > -1:
            return counter
            

# another way to do this in one line

def find_element(lst, val):
    print lst.index(val)
