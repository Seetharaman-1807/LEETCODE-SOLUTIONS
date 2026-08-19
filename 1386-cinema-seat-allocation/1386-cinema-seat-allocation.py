from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_masks = defaultdict(int)
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                row_masks[row] |= (1 << (col - 2))
        
        LEFT_MASK = 15
        RIGHT_MASK = 240
        MID_MASK = 60
        
        total_families = (n - len(row_masks)) * 2
        
        for mask in row_masks.values():
            left_free = (mask & LEFT_MASK) == 0
            right_free = (mask & RIGHT_MASK) == 0
            
            if left_free and right_free:
                total_families += 2
            elif left_free or right_free or (mask & MID_MASK) == 0:
                total_families += 1
                
        return total_families
