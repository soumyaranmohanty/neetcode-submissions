class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm={}
        if len(s)==0:
            return 0
        
        for i in range(0, len(s)):
            unichs = ""
            
            max_length=0
            count=0
            print("ith index : ", i)
            for j in range(i, len(s)):
                
                if s[j] not in unichs:
                    unichs+=s[j]
                    count+=1

                else:
                    
                    break
            max_length = count
            hm[unichs] = max_length
            #print("max length in ith index and j is ",max_length,  i, j)
            #print(hm)
        # print(list(sorted(hm.values())))
        # print(list(sorted(hm.values()))[-1])
        return list(sorted(hm.values()))[-1]




