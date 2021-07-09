class Solution:
    def isValid(self, s: str) -> bool:
        a=['(','[','{']
        r=[]
        if s[0] not in a:
            return False
     
        for i in s:
            if i in a:
                r.append(i)
            
            elif len(r)>=1:
                    
                    k=r.pop()
                    
                    if k=='(':
                        if i!=')':
                            return False
                    if k=='[':
                        if i!=']':
                            return False
                    if k=='{':
                        if i!='}':
                            return False
            else:
                return False
        if len(r)>=1:
            return False
                
        return True
                    
        
