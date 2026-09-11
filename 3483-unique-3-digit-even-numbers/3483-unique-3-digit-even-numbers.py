from collections import Counter

class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        # Count the frequency of each digit available in the input array
        available_counts = Counter(digits)
        unique_count = 0
        
        # Iterate through all valid 3-digit even numbers
        for num in range(100, 1000, 2):
            # Extract the hundreds, tens, and units digits
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            # Count how many of each digit are needed for this specific number
            needed_counts = Counter([d1, d2, d3])
            
            # Check if our available digits can satisfy the needed counts
            if all(available_counts[d] >= needed_counts[d] for d in needed_counts):
                unique_count += 1
                
        return unique_count