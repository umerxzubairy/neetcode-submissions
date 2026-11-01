class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        dic = defaultdict(int)
        dic[0] = 1
        res = 0
        prefix = 0
        for r in range(len(nums)):
            prefix+= nums[r]
            diff = prefix - k
            res+= dic[diff]
            dic[prefix]+=1
        return res
