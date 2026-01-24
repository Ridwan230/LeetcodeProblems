class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        run_avg=0
        max_avg=0

        for i in range(0,k):
            run_avg+=nums[i]
        run_avg/=k
        max_avg=run_avg

        for i in range(k,len(nums)):
            run_avg=run_avg - nums[i-k]/k + nums[i]/k
            max_avg=max(max_avg,run_avg)

        return max_avg