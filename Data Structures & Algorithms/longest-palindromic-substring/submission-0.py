class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        pl=[]

        for i in range(0, len(s)):
            unistr=""
            #print("ith index : ", i)
            for j in range(i, len(s)):
                #print("jth index : ", j)
                #unistr+=s[j]
                unistr+=s[j]
                #print(unistr)
                if unistr==unistr[::-1]:
                    pl.append(unistr)
                

                

        

        return list(sorted(pl, key=len))[-1]
                    


        