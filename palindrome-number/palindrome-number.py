class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        z=str(x)
        for i in range(len(z)//2):
            if z[i]!=z[len(z)-i-1]:
                return False
        return True
            
        