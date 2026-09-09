class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = res = 0
        r = len(heights) - 1
        while l < r:
            res = max(res, min(heights[r], heights[l]) * (r-l))
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return res
            