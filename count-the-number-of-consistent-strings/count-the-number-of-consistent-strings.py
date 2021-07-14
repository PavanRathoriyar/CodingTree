class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for i in words:
            tag=1
            for j in i:
                if j not in allowed:
                    tag=0
                    break
                    
            if tag==1:
                c+=1
        return c
               
                
            
            

                                