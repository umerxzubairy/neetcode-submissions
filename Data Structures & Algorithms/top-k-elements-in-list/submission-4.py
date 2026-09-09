class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        counter = Counter(nums)
        for key, value in counter.items():
            buckets[value].append(key)
        
        res = []
        for i in range(len(buckets)-1, 0, -1):
            if len(buckets[i]) == 0:
                continue
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res