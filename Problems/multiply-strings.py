class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result array with zeros
        result = [0] * (len(num1) + len(num2))
        
        # Reverse both strings for easier right-to-left multiplication
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        # Perform multiplication
        for i in range(len(num1)):
            for j in range(len(num2)):
                # Multiply the digits
                product = int(num1[i]) * int(num2[j])
                
                # Add to the corresponding position in the result array
                result[i + j] += product
                
                # Handle carry
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        return ''.join(map(str, result[::-1]))

solution = Solution()
print(solution.multiply("123", "456"))  
print(solution.multiply("2", "3"))     
