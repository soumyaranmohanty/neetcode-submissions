class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        di = {}
        
        for ele in nums:
         if ele in di:
             print(ele)
             di[ele]+=1
             return True
         else:
             di[ele]=1
        return False

