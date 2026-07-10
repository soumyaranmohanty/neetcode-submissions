class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm={}

        for num in nums:
            if num not in hm:
                hm[num]=1
            else:
                hm[num]+=1

        # first=-1
        # second=-1
      
        #l= list(sorted(hm.values()))

        #return [l[-k][0] for k in range(1,k+1)]
        # pd = {}
        # for key in hm:
        #     value=hm[key]

        #     if first<value:
        #         second=first
        #         first=value
                
        #     if second<value and first > value:
        #         second=value

        # print(first, second)
        #print(sorted(hm.items(), key=lambda x: x[1]))
        l = [list(sorted(hm.items(), key=lambda x: x[1], reverse= True))[a][0] for a in range(0,k) ]
        return l

                 
            
