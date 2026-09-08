from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Frequency count and then heap sort based on count
        # 2. Bucket sort and then iterate back
        buckets = [[] for _ in range(len(nums)+1)]
        counter = Counter(nums)
        res = []
        for key, value in counter.items():
            buckets[value].append(key)
        
        for i in range(len(buckets)-1, -1, -1):
            for key in buckets[i]:
                res.append(key)
                if len(res) == k:
                    return res
        return res