class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        # skip spaces
        while i < len(s) and s[i] == " ":
            i += 1
    
        # check sign
        sign = 1

        if i < len(s) and s[i] == "-":
            sign = -1
            i += 1

        elif i < len(s) and s[i] == "+":
            sign = 1
            i += 1

        # convert digits
        num = 0

        while i < len(s) and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit
            i += 1
            
        # apply sign 
        result = sign * num

        # apply 32-bit limits
        MIN = -2147483648
        MAX = 2147483647

        if result < MIN:
            return MIN

        elif result > MAX:
            return MAX

        return(result)
