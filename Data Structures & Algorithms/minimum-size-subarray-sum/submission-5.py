class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = prefix = 0
        res= float('inf')
        for r in range(len(nums)):
            prefix+= nums[r]
            while l <= r and prefix >= target:
                prefix-= nums[l]
                res = min(res, r-l+1)
                l+=1

        if res == float('inf'):
            return 0
        return res