# Writing without references - Apr 18, 2022

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss=''
        i=0  

        for c in range(len(s)):
            if s[c] not in ss: # Determine if a character is a duplicate
                ss=ss+s[c]
                if c==len(s)-1 and len(ss) > i: # Determine if it is the last character and if the length of the substring is the longest 
                    i=len(ss)
            elif len(ss) > i: # Determines if the length of the substring is the longest when the character is repeated
                i=len(ss)
                nc=s.rfind(s[c],0,c) # Find the last occurrence of duplicate characters
                ss=s[nc+1:c+1] # Let the substring be the content between the previous duplicate character and the duplicate character
            else:
                nc=s.rfind(s[c],0,c)
                ss=s[nc+1:c+1]
        return i
