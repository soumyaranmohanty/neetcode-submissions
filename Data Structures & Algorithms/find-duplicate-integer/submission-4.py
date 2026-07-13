class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        sinlist = []
        #duplicate = []

        for a in nums:
            if a not in sinlist:
                sinlist.append(a)
            elif a in sinlist:
                return a

        

        