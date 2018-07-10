# a simple sudoku checker,
# check_sudoku will take in as an input
# a square list of lists that is a n x n
# sudoku puzzle. If the sudoku square is valid
# then True will be returned, else False.


#uncomment the squares to use or test in procedure
#correct = [[1,2,3],
#           [2,3,1],
#           [3,1,2]]

#incorrect = [[1,2,3,4],
#             [2,3,1,3],
#             [3,1,2,3],
#             [4,4,4,4]]

#incorrect2 = [[1,2,3,4],
#             [2,3,1,4],
#             [4,1,2,3],
#             [3,4,1,2]]

#incorrect3 = [[1,2,3,4,5],
#              [2,3,1,5,6],
#              [4,5,2,1,3],
#              [3,4,5,2,1],
#              [5,6,4,3,2]]

#incorrect4 = [['a','b','c'],
#              ['b','c','a'],
#              ['c','a','b']]

#incorrect5 = [ [1, 1.5],
#               [1.5, 1]]

def check_sudoku(lst):
    #isNum(lst)
    for i in lst:
        for j in i:
            if j == 1 or j == 2 or j == 3 or j == 4 or j == 5 or j == 6 or j == 7 or j == 8 or j == 9:
                continue
            else:
                return False
                break
    
    length = len(lst[0])
    l = length
    numCheck = length
    lst_sum = 0
    row_sum = 0
    
    #has1(lst)
    while numCheck >= 1:
        for i in lst:
            if numCheck not in i:
                return False
                break
        numCheck = numCheck - 1
            
    
    #this while loop will get what the sum of the rows and columns should be
    while length >= 1:
        lst_sum = lst_sum + length
        length = length - 1

    for i in lst:
        row_sum = 0
        for j in i:
            row_sum = row_sum + j
        if row_sum != lst_sum:
            return False
            break
    #return True after checking for columns
    
    row = 0
    col = 0
    col_sum = 0
    
    while True:
        col_sum = col_sum + lst[row][col]
        row = row + 1
        if row == l:
            if col_sum != lst_sum:
                return False
                break
            col_sum = 0
            col = col + 1
            if col == l:
                return True
                break
            row = 0

