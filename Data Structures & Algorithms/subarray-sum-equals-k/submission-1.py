class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        prefix = res = 0
        for num in nums:
            prefix+= num
            diff = prefix - k
            res+= dic[diff]
            dic[prefix]+=1
        return res