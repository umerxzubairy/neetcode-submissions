class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        h = len(nums) - 1
        mid = 0
        while mid <= h:
            if nums[mid] == 0:
                temp = nums[l]
                nums[l] = nums[mid]
                nums[mid] = temp
                l+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                temp = nums[h]
                nums[h] = nums[mid]
                nums[mid] = temp
                h-=1