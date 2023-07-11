class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) #right is no. of columns + 1
        top, bottom = 0, len(matrix) #bottom is no. of rows + 1
        res = []
        # right-> bottom -> left ->top
        '''
            L    R
            T 1 2 3
            4 5 6
            7 8 9
            B
        '''
        while left < right and top < bottom:
            # get every value of top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # get every value of right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            # get every value in bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # get every value in left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
             
        return res      
