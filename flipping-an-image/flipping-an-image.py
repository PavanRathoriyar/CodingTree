class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        l=len(image)
        a=list()
        b=list()
        for i in range(l):
                for j in range(l):
                        b.append(int(not(image[i][l-j-1])))
                a.append(b)
                b=[]
        return a
        
        