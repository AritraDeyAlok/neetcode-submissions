class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix)
        columns = len(matrix[0])

        top = 0
        bottom = rows - 1 

        left = 0
        right = columns - 1

        spiral_order = []

        while top <= bottom and left <= right:
            
            # 1. Traverse upper boundary row (left --> right)
            for i in range(left, right + 1):
                spiral_order.append(matrix[top][i])

            top += 1

            # 2. Traverse right boundary column (top --> bottom)
            for j in range(top, bottom + 1):
                spiral_order.append(matrix[j][right])

            right -= 1 

            if top <= bottom:
                # 3. Traverse bottom boundary row (right --> left)
                for k in range(right, left - 1, -1):
                    spiral_order.append(matrix[bottom][k])

                bottom -= 1

            if left <= right:
                # 4. Traverse left bondary column (bottom --> top)
                for l in range(bottom, top - 1, -1):
                    spiral_order.append(matrix[l][left])

                left += 1
            
        return spiral_order