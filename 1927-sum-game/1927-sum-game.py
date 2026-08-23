class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        left_sum = 0
        left_q = 0
        right_sum = 0
        right_q = 0
        
        # Count sums and '?' for the left half
        for i in range(mid):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])
                
        # Count sums and '?' for the right half
        for i in range(mid, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])
        
        # Check Bob's winning condition using integer math
        # Bob wins (returns False) if the difference balances out perfectly
        if 2 * (left_sum - right_sum) == 9 * (right_q - left_q):
            return False
            
        return True
