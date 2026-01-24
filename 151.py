class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        d=deque()
        lst.reverse()
        return " ".join(lst)
        