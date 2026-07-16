class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left =0
        right = len(numbers)-1
        
        while left<right:
            su = numbers[left]+numbers[right]
            if su==target:
                return [left+1, right+1]

            if su<target:
                left+=1
            if su>target:
                right-=1

            

                    

        





