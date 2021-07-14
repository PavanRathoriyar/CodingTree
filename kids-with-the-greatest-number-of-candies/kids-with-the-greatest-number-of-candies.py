class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        m=max(candies)
        for i in candies:
            if i+extraCandies>=m:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        