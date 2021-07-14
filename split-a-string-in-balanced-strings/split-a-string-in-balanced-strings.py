class Solution:
    def balancedStringSplit(self, s: str) -> int:
        d=0
        a=[]
        c=s[0]
        for i in s:
            if not a:
                c=i
            if i==c:
                a.append(0)
            else:
                a.pop()
            if not a:
                d+=1
                
        return d
                
        