class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        iter=0
        write=0
        while iter<len(nums):
            if nums[iter]!=0:
                nums[write], nums[iter]=nums[iter], nums[write]
                write+=1
            iter+=1
