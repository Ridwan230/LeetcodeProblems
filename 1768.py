class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge=''
        for i in range(min(len(word1),len(word2))):
            merge=merge+word1[i]+word2[i]
        if len(word1)>len(word2):
            merge=merge+word1[len(word2):]
        if len(word2)>len(word1):
            merge=merge+word2[len(word1):]
        return merge
        