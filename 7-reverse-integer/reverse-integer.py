
class Solution:
    def reverse(self, x: int) -> int:
        rev_num = 0

        # Change 1: handle negative numbers
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:                    # Change 2: use x, not n
            lst_num = x % 10             # Change 3: use % instead of /
            rev_num = rev_num * 10 + lst_num
            x = x // 10

        # Change 4: restore the original sign
        rev_num = rev_num * sign

        # Change 5: check the 32-bit integer range
        if rev_num < -(2**31) or rev_num > 2**31 - 1:
            return 0

        return rev_num

        
        