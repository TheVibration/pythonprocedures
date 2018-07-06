#first_letter_count takes two inputs, 
#a list of strings and a letter, and the
#value returned will be the number of 
#times letter is the first letter in 
#the list of words in lst.

def first_letter_count(lst, letter):
    counter = 0
    for i in lst:
        ln = 0
        while ln <= len(i)-1:
            if i[ln] == letter:
                counter = counter + 1
                ln = ln + 1
            else:
                ln = ln + 1
    return counter

