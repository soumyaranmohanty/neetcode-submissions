class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #check string length match
        if len(s)==len(t):
            elsd = {}
            eltd = {}

            for els in s :
                if els not in elsd:
                    elsd[els]=1
                if els in elsd:
                    elsd[els]+=1

            for elt in t:
                if elt not in eltd:
                    eltd[elt]=1
                if elt in eltd:
                    eltd[elt]+=1
            # print(elsd)
            # print(eltd)
            # print(len(elsd))
            #check the count of each character:
            if len(elsd)==len(eltd):
                for c in elsd:
                    if c in eltd:
                        if elsd[c]!=eltd[c]:
                            
                            return False
                    else:
                        return False
            else:
                return False
            return True
        else:
            return False


        