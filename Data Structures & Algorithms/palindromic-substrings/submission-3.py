class Solution:
    def countSubstrings(self, s: str) -> int:

        
        count=0
        for i in range(0, len(s)):
            unistr=""
            #print("ith Loop : ", i)
            for j in range(i, len(s)):
                #print("jth Loop : ", j)
                unistr+=s[j]
                #print(unistr)
                if unistr==unistr[::-1]:
                    count+=1
                #print("Count : ", count)

        return count
        