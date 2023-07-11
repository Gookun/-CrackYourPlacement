from typing import List
# right->bottom->left->top
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    res = []
    #right is no. of columns + 1
    left , right = 0, len(matrix[0])
    #bottom is no. of rows + 1
    top , bottom = 0, len(matrix)
    while left < right and top < bottom:
        # get every value in the top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        # get every i in the right coloumn
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break
        # get every i in bottom row
        for i in range(right, left):
            res.append(matrix[bottom - 1][i])
        bottom -= 1
        #get every i in left col
        for i in range(bottom, top):
            res.append(matrix[i][left])
        left+=1

        



'''
    L    R
  T 1 2 3
    4 5 6
    7 8 9
  B
'''
