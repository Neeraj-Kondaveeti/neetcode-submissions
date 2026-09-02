class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        freq = {}
        maxfreq = 0 
        maxlen = 0 
        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char,0)+1
            maxfreq = max(maxfreq,freq[char])

            ws = right-left+1
            if ws-maxfreq>k:
                leftchar = s[left]
                freq[leftchar] = freq[leftchar]-1
                left = left+1
            maxlen = max(maxlen, right-left+1)

        return maxlen