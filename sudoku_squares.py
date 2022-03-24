correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

# Define a function check_sudoku() here:

def check_sudoku(square):
    # Verify that the square is not empty
    if len(square) == 0:
        return False
    # Verify that the square is properly formed
    for line in square:
        if len(square) != len(line):
            return False
    digits = set(list(range(1,len(square)+1)))

    def check_columns(square, d):
        columns = []
        for i in range(len(square)):
            column = []
            for line in square:
                column.append(line[i])
            if set(column) != d:
                return False
        return True

    def check_rows(square, d):
        for line in square:
            if set(line) != d:
                return False
        return True

    return check_rows(square, digits) and check_columns(square, digits)


print(check_sudoku(incorrect))
#>>> False

print(check_sudoku(correct))
#>>> True

print(check_sudoku(incorrect2))
#>>> False

print(check_sudoku(incorrect3))
#>>> False

print(check_sudoku(incorrect4))
#>>> False

print(check_sudoku(incorrect5))
#>>> False


