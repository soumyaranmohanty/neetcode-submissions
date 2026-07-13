class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        pl=[]
        max_length=0
        for i in range(0, len(s)):
            unistr=""
            
            #print("ith index : ", i)
            for j in range(i, len(s)):
                #print("jth index : ", j)
                #unistr+=s[j]
                unistr+=s[j]
                #print(unistr)
                if unistr==unistr[::-1]:
                    if len(unistr)>max_length:
                        pl.append(unistr)
                        max_length=len(unistr)
                

                

        

        return list(sorted(pl, key=len))[-1]
                    


        