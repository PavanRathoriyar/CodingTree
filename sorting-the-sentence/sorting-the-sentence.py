class Solution:
    def sortSentence(self, s: str) -> str:
        r=''
        b=dict()
        a=""
        for j in s:
            if j==" ":
                continue
            if j.isalpha():
                a=a+j
            else:
                b[int(j)]=a
                a=''
        for i in sorted(b):
            r=r+" "+str(b[i])
        r=r.strip()
        return r
            
            
            
            
        