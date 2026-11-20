class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr = best = nums[0]
        for x in nums[1:]: # start from 1
            curr = max(x,curr+x) #the number and the sum
            best = max(curr,best)
        return best
        