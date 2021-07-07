class Solution:
    def reverse(self, x: int) -> int:
        
         
        a=0
        c=x
        if c<=0:
            x=-x
        
        while(x!=0):
            r=x%10
            a=a*10+r
            x=x//10
        if a>2147483647 or a<=(-2147483648):
            return 0
        if c<=0:
             return -a
        return a
            
       