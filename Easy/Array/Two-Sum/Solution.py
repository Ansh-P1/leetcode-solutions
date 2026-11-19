class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range (len(nums)):
            x = nums[i]
            if target - x in seen:
                return [seen[target-x], i]
            seen [x]=i
    
        