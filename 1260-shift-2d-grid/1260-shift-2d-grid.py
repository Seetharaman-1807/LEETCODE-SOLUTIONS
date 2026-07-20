class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        k %= total_elements
        
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                new_1d_idx = (i * n + j + k) % total_elements
                new_r = new_1d_idx // n
                new_c = new_1d_idx % n
                result[new_r][new_c] = grid[i][j]
                
        return result
