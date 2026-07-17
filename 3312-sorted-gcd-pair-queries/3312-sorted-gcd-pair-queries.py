import math
from typing import List
from collections import Counter
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_num = max(nums)

        counts = Counter(nums)
        
        gcd_pairs = [0] * (max_num + 1)

        for i in range(max_num, 0, -1):
            total_multiples = 0
            for j in range(i, max_num + 1, i):
                total_multiples += counts[j]
            
            base_pairs = (total_multiples * (total_multiples - 1)) // 2
            
            for j in range(2 * i, max_num + 1, i):
                base_pairs -= gcd_pairs[j]
                
            gcd_pairs[i] = base_pairs
            
        prefix_sums = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_pairs[i]
            
        ans = []
        for q in queries:
            idx = bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans
