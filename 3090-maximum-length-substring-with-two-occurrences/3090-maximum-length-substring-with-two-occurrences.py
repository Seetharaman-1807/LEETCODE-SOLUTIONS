from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = Counter()
        max_len = 0
        i = 0
        
        for j, char in enumerate(s):
            cnt[char] += 1
            
            # Shrink the window if the frequency constraint is breached
            while cnt[char] > 2:
                cnt[s[i]] -= 1
                i += 1
                
            # Track the maximum length found so far
            max_len = max(max_len, j - i + 1)
            
        return max_len
