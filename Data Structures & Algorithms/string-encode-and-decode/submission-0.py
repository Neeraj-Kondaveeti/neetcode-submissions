class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s = s + str(len(st)) + "#" + st
        return s

    def decode(self, s: str) -> List[str]:

        i = 0 
        res = []

        while i < len(s):
            j = i 
            while s[j]!="#":
                j = j + 1
            
            le = int(s[i:j])
            word = s[j+1:j+1+le]
            res.append(word)
            i = j+le+1

        return res
