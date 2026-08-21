class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base case: valid combination found
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Rule 1: Can we add an open parenthesis?
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # Rule 2: Can we add a close parenthesis?
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        return result
