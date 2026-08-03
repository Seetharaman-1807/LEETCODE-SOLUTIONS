class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        count = [0] * 128
        l = 0
        for r in range(len(s)):
            count[ord(s[r])] += 1
            while count[ord(s[r])] > 1:
                count[ord(s[l])] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
