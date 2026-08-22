class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        digit_sum = 0
        digit_product = 1

        while temp > 0:
            temp, digit = divmod(temp, 10)
            digit_sum += digit
            digit_product *= digit
            
        return n % (digit_sum + digit_product) == 0
