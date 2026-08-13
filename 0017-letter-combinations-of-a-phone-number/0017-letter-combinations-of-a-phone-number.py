class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
            
        digit_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index: int, path: list[str]):
            # Base case: completed a full combination
            if index == len(digits):
                res.append("".join(path))
                return
                
            # Explore all possible letters for the current digit
            current_digit = digits[index]
            for letter in digit_map[current_digit]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop() # Backtrack step
                
        backtrack(0, [])
        return res
