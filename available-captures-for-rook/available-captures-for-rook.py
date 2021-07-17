class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        tag=1
        x=0
        y=0
        for i in range(8):
                for j in range(8):
                        
                        if board[i][j]=='R':
                                
                                x=i
                                y=j
                                tag=0
                                break
                if tag==0:
                        break
        tag=0
        if x>0:
                for i in range(x-1,-1,-1):
                        if board[i][y]=='B':
                                break
                        if board[i][y]=='p':
                                tag+=1
                                break
        if x<7:
                for i in range(x+1,8):
                        if board[i][y]=='B':
                                break
                        if board[i][y]=='p':
                                tag+=1
                                break
        if y>0:
                for j in range(y-1,-1,-1):
                        if board[x][j]=='B':
                                break
                        if board[x][j]=='p':
                                tag+=1
                                break
        if y<7:
                for j in range(y+1,8):
                        if board[x][j]=="B":
                                break
                        if board[x][j]=="p":
                                tag+=1
                                break
        return tag
                        
                
                        
                
                
                
                
                
                
                
                
                
                
                