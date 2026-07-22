class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        
        for row_index in range(numRows - 1):
            previous_row = triangle[-1]
            current_row = [1]
            for j in range(len(previous_row) - 1):
                current_row.append(previous_row[j] + previous_row[j + 1])
            current_row.append(1)
            
            triangle.append(current_row)
            
        return triangle
