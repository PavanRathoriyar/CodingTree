class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        x=max(nums)
        nums.remove(x)
        y=max(nums)
        nums.remove(y)
        w=min(nums)
        nums.remove(w)
        z=min(nums)
        nums.remove(z)
        return x*y-w*z