class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sets=set()

        for i in range(0, len(nums)-2):

            #complim_target = 0-num

            left=i+1
            right=len(nums)-1
            # sa=set()
            while left<right:
                sum = nums[i]+nums[left]+nums[right]

                if sum==0:
                    sets.add((nums[i],nums[left],nums[right]))
                    #sets.add(list())
                    left+=1
                    right-=1

                elif sum<0:
                    left+=1

                else:
                    right-=1
        li=[]
        

        return [list(ele) for ele in sets]


        