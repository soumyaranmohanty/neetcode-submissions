class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix=1
        suffix=1
        ol=[1]*len(nums)
        # def product(lis):
        #     if len(lis)==1:
        #         return lis[0]
        #     return lis[0]*product(lis[1:])

        # for i, num in enumerate(nums):
        #     if i==0:
        #         prefix=1
        #         suffix=product(nums[i+1:])
        #     elif i==len(nums)-1:
        #         prefix=product(nums[0:i])
        #         suffix=1
        #     else:
        #         prefix=product(nums[0:i])
        #         suffix=product(nums[i+1:])

        #     ol.append(prefix*suffix)
        # return ol

        for i in range(len(nums)):
            #if len(nums)=5, i=0 to i=4
            ol[i]=prefix
            prefix*=nums[i]
        

        for i in range(-1, -len(nums)-1, -1):
            ol[i]*=suffix
            suffix*=nums[i]
        return ol
        