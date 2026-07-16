class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0  
        c = 0  
        
        for num in nums:
            if num == 1:
                c += 1        
                m = max(m, c) 
            else:
                c = 0         
                
        return m
