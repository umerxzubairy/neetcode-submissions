class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def findSum(arr, l ,r, target, res):
            while l < r:
                s = arr[l] + arr[r]
                if s > target:
                    r-=1
                elif s < target:
                    l+=1
                else:
                    res.append([-target, arr[l], arr[r]])
                    l+=1
                    r-=1
                    while arr[l] == arr[l - 1] and l < r:
                        l += 1

        res = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            findSum(nums, i+1, len(nums) -1 , -nums[i], res)
        return res
            
