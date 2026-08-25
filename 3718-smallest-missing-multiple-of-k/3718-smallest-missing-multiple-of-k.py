class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        # Convert array to a set for O(1) lookups
        num_set = set(nums)
        
        # Start checking from the smallest positive multiple of k
        multiple = k
        
        # Keep incrementing by k until the multiple is not in the set
        while multiple in num_set:
            multiple += k
            
        return multiple
