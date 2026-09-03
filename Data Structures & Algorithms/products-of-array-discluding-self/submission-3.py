class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(len(nums)-1):
            pre.append(pre[-1]*nums[i])
        post = [1]
        for i in range(len(nums)-1, 0, -1):
            post.append( post[-1] * nums[i])
        
        for i in range(len(nums)):
            nums[i] = pre[i] * post[len(nums)-i-1]
        return nums
