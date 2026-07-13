class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(0, len(arr)):
            if i==len(arr)-1:
                #print(i)
                arr[i]=-1
            else:
                #print(arr[i+1:])
                arr[i] = max(arr[i+1:])
                #print(i)
            
            

        return arr
                    
                    