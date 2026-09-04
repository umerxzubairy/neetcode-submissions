class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        curr = res = 0
        for num in nums:
            curr+=num
            diff = curr - k
            res += dic[diff]
            dic[curr]+=1
        return res