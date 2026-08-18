from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter(nums)
        
        # Case 1: Subarray size is 1
        if k == 1:
            ans = -1
            for num, count in freq.items():
                if count == 1:
                    ans = max(ans, num)
            return ans
            
        # Case 2: Subarray size is the entire array length
        if k == n:
            return max(nums)
            
        # Case 3: 1 < k < n (Only boundary elements can appear in exactly one subarray)
        ans = -1
        if freq[nums[0]] == 1:
            ans = max(ans, nums[0])
        if freq[nums[n - 1]] == 1:
            ans = max(ans, nums[n - 1])
            
        return ans
