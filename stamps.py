# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)


def stamps(num):
    
    holder = num
    counter5 = 0
    counter2 = 0
    counter1 = 0
    if num == 0:
        return counter5, counter2, counter1
    while holder > 0:
        if holder >= 5:
            holder = holder - 5
            counter5 = counter5 + 1
        else:
            if holder >= 2:
                holder = holder - 2
                counter2 = counter2 + 1
            else:
                holder = holder - 1
                counter1 = counter1 + 1
                
    return counter5, counter2, counter1
    
#print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
#print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
#print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
#print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps
