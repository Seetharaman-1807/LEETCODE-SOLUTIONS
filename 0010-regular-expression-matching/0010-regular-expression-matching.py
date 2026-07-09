class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            # Check the memoization cache
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base Case: end of pattern reached
            if j == len(p):
                return i == len(s)
            
            # Check if current characters match
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # If the next character is '*'
            if (j + 1) < len(p) and p[j + 1] == '*':
                # Choice 1: Ignore the '*' pattern (0 occurrences)
                # Choice 2: Use the '*' pattern (1+ occurrences, requires a valid match)
                memo[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return memo[(i, j)]
            
            # Standard single character match
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            
            memo[(i, j)] = False
            return False

        return dfs(0, 0)
