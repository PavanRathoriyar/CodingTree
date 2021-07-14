class Solution:
    def interpret(self, command: str) -> str:
        a=""
        i=0
        while(i<len(command)):
            if command[i]=='G':
                a+="G"
                i+=1
            elif i+1<len(command)  and command[i+1]=='a':
                a+="al"
                i=i+4
            else:
                a+="o"
                i+=2
        return a
                
        