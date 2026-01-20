class Solution:
    def reverseVowels(self, s: str) -> str:
        d=deque()
        slist=list(s)
        for i in range(len(slist)):
            if slist[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                d.append(slist[i])
                slist[i]=''
        for i in range(len(slist)):
            if slist[i]=='' and d:
                slist[i]=d.pop()
        return "".join(slist)
            