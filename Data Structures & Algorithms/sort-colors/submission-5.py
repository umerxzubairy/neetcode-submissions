class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = m = 0
        r = len(nums) - 1

        while m <= r:
            if nums[m] == 0:
                temp = nums[m]
                nums[m] = nums[l]
                nums[l] = temp
                l+=1
                m+=1
            elif nums[m] == 1:
                m+=1
            else:
                temp = nums[r]
                nums[r] = nums[m]
                nums[m] = temp
                r-=1
            