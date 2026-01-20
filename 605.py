class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        for i in range(0,len(flowerbed)):
            if flowerbed[i]==0:
                if i==0 or i>1 and flowerbed[i-1]==0:
                    if i==len(flowerbed)-1 or i<len(flowerbed)-1 and flowerbed[i+1]==0:
                        count+=1
                        flowerbed[i]=1
        return count>=n