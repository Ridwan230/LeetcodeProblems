class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[1]*len(nums)
        p=1
        s=1
        for i in range(len(nums)):
            answer[i]*=p
            p*=nums[i]
        for i in range(-1,-len(nums)-1,-1):
            answer[i]*=s
            s*=nums[i]
        return answer