class Solution:
    def trap(self, height: List[int]) -> int:
        l = res = 0
        r = len(height) - 1
        lMax = height[l]
        rMax = height[r]
        while l < r:
            if lMax < rMax:
                l+=1
                lMax = max(height[l], lMax)
                res += max(min(lMax, rMax) - height[l], 0)
            else:
                r-=1
                rMax = max(height[r], rMax)
                res += max(min(lMax, rMax) - height[r], 0)
            
            
        return res