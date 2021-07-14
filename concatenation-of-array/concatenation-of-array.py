class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       # nums=[1,2,3,1]
        b=[]
        b=nums.copy()
        for i in range(len(nums)):
            b.append(nums[i])
        return b