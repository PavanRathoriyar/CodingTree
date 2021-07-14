class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        co=0
        a=[[ 0 for i in range(n)] for j in range(m)]
        for i in indices:
                r,p=i[0],i[1]
                for k in range(n):
                        a[r][k]+=1
                for k in range(m):
                        a[k][p]+=1
        for i in a:
                for j in i:
                        if j%2==1:
                                co+=1
        return co
        
        