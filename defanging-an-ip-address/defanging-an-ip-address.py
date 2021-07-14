class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        j=''
        for i in address:
            if i !='.':
                j+=i
            else:
                j+='[.]'
        return j

        
       
        