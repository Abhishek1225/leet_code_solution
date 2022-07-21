(Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit 
integer range [-231, 231 - 1], then return 0.Input: x = 123
Output: 321)




class Solution:
    def reverse(self, x):
        sign_multi = 1
        if x<0:
            sign_multi = -1
            x = x*sign_multi
        temp = x
        rev = 0
        while x!=0:
            rev = rev*10 + x%10
            if rev *sign_multi< -1*2**31 or rev*sign_multi>2**31:
                return 0
            x = x//10
        return rev *sign_multi
        
        
