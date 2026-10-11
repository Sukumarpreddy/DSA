class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0 
        dup = x
        while x>0:
            lst = x%10
            rev = rev * 10 + lst
            x=x//10
        if rev == dup:
            return True
        else:
            return False
        


        