class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        ml = 0 
        freq={}

        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char,0)+1
            while freq[char]>1:
                leftchar=s[left]
                freq[leftchar]= freq[leftchar]-1
                left = left+1
            ml = max(ml, right-left+1)
        return ml