class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l , r):
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                r-=1
                l+=1
        k %= len(nums)
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)