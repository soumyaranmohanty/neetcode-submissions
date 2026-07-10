class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        le = {}
        for word in strs:
            s="".join(sorted(word))
            if s not in le:
                le[s]=[]
            
            le[s].append(word)

        ls=[]
        for a in le:
            ls.append(le[a])

        return ls






