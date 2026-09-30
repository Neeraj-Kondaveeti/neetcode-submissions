class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        freq = {}
        for char in s1:
            freq[char] = freq.get(char,0)+1
        
        ws = len(s1)
        left = 0 
        res = {}

        for right in range(len(s2)):
            char = s2[right]
            res[char] = res.get(char,0)+1
            if right-left+1 >ws:
                leftchar = s2[left]
                res[leftchar] = res[leftchar] - 1
                if res[leftchar]==0:
                    del res[leftchar]

                left = left+1
            if res == freq:
                return True
        return False