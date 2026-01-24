class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        max_count=0
        lst=['a','e','i','o','u']
        for i in range(0,k):
            if s[i] in lst:
                count+=1
        max_count=count
        for i in range(k,len(s)):
            if s[i-k] in lst:
                count-=1
            if s[i] in lst:
                count+=1
            max_count=max(max_count,count)
        
        return max_count