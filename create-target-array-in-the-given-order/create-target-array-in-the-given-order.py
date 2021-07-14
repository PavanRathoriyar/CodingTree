class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[None]*len(nums)
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target[0:len(nums)]