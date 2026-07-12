class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        first = nums[0]
        last = nums[-1]
        #if (last-first+1)!=len(nums):

        for i in range(0, len(nums)):
            if (i) not in nums:
                return i
        return len(nums)
            

        