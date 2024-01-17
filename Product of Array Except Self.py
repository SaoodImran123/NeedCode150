class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputArr = [1]*(len(nums))
        prev=1
        for x in range (1,len(nums)):
            outputArr[x] = nums[x-1] * outputArr[x-1]
        for x in range(len(nums)-2,-1,-1):
            outputArr[x] *= nums[x+1] * prev
            prev = nums[x+1] * prev
        return outputArr

            


        
