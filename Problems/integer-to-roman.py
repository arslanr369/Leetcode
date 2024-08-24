class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        roman_numeral = ""
        
        for value, symbol in value_symbols:
            while num >= value:
                roman_numeral += symbol
                num -= value
                
        return roman_numeral

# Explanation:
# Value-Symbol Pairs: We store the Roman numeral symbols and their corresponding integer values in descending order.
# Iterate and Convert: For each value-symbol pair, check if the current integer (num) is greater than or equal to the value. If it is, subtract the value from the integer and append the symbol to the result string. Continue this until the integer is fully converted.
Return: The final Roman numeral string is returned.