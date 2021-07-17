class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        a=len(mat)
        s=0
        for i in range(a):
                s+=mat[i][i]+mat[a-i-1][i]
        if a%2==1:
                return s-mat[a//2][a//2]
        else:
                return s
                