class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        result = [0] * (len(num1) + len(num2))
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i]) * int(num2[j])
                
                result[i + j] += product
                
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        return ''.join(map(str, result[::-1]))

solution = Solution()
print(solution.multiply("123", "456"))  
print(solution.multiply("2", "3"))     

# Approach:

# Basic Idea:

# When multiplying two numbers, each digit of num1 is multiplied by each digit of num2, and the results are accumulated in the correct positions in an array that will eventually represent the product.
# We handle carries while updating the array.

# Implementation Steps:

# Create an array result to store the intermediate multiplication results. The size of the result array will be len(num1) + len(num2) because multiplying two numbers can at most result in a number with this many digits.
# Iterate over each digit in num1 and num2 from right to left, simulating the process of long multiplication.
# For each digit in num1 and num2, calculate the product and add it to the appropriate position in the result array.
# Handle the carry by adding it to the next position.
Convert the result array back into a string, skipping any leading zeros.
Edge Cases:

If either num1 or num2 is "0", return "0".
Properly handle carries during the multiplication process.