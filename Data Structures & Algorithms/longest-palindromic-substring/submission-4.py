class Solution:
    def longestPalindrome(self, s: str) -> str:
        pl=[]
        max_length=0
        for i in range(0, len(s)):
            unistr=""
            for j in range(i, len(s)):
                unistr+=s[j]
                if unistr==unistr[::-1]:
                    if len(unistr)>max_length:
                        if len(pl)!=0:
                            pl.pop()
                        pl.append(unistr)
                        max_length=len(unistr)
                

                

        
        #print(pl)
        #return list(sorted(pl, key=len))[-1]
        return pl[0]
                    


        