class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        prefix = 0
        res = float('inf')
        for r in range(len(nums)):
            prefix +=nums[r]
            while prefix >= target:
                prefix-=nums[l]
                res = min(r-l+1, res)
                l+=1
        if res == float("inf"):
            return 0
        return res