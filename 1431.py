class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        limit=max(candies)-extraCandies
        ans=[]
        for i in candies:
            if i>=limit:
                ans.append(True)
            else:
                ans.append(False)
        return ans