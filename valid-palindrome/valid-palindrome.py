class Solution:
    def isPalindrome(self, s: str) -> bool:
        v=[val for val in s if val.isalnum()]
        z="".join(v)
        z=z.lower()
        l=len(z)
        for i in range(l//2):
            if z[i]!=z[l-i-1]:
                return  False
        return True
        