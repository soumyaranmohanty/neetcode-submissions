class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        numb = set(nums)
        print(numb)
        cons = []
        dic = {}
        start =[]
        for i, ele in enumerate(numb):
            if ele-1 in numb:
                continue
            else:
                start.append(ele)

        # print(start)

        # for s in start:
        #     dic[s] = []
        #     b=s
        #     dic[s].append(s)
        #     while b+1 in nums:
        #         if b+1 not in dic[s]:
        #             dic[s].append(b+1)
        #         b=b+1

        # return len(list(sorted(dic.values()))[0])
        count=[]
        for s in start:
            temp=s
            counter=1
            while temp+1 in numb:
                counter+=1
                temp+=1
            count.append(counter)

        # print(max(count))
        return max(count)



