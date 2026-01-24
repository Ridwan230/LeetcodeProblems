class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s=0
        for i in t:
            if len(s)>pointer_s and i == s[pointer_s]:
                pointer_s+=1
        return pointer_s==len(s)