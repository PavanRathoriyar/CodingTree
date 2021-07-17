class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        b=[[raw[i] for raw in matrix] for i in range(len(matrix[0]))]
        
        return b