class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
         a=list()
         for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==target-nums[j]:
                    a.append(i)
                    a.append(j)
                    return a
            