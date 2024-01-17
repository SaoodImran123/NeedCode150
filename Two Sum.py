class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for ele in range(0,len(nums)):
            midTarget = target-nums[ele]
            if midTarget in nums:
                val2 = nums.index(midTarget)
                if val2 != ele:
                    return [ele, val2]
        
        
