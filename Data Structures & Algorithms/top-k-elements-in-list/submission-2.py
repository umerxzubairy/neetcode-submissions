class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buckets = [[] for _ in range(len(nums)+1)]
        counter = Counter(nums)
        for key, value in counter.items():
            buckets[value].append(key)
        for i in range(len(buckets)-1, -1, -1):
            if len(buckets[i]) == 0:
                continue
            for key in buckets[i]:
                if len(res) == k:
                    break
                res.append(key)
        return res