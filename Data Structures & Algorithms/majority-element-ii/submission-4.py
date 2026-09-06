class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num]+=1
            if len(dic) <= 2:
                continue
            
            newDic = defaultdict(int)
            for key, value in dic.items():
                if value > 1:
                    newDic[key] = value - 1
            dic = newDic
        
        res = []
        for key, value in dic.items():
            count = 0
            for num in nums:
                if num == key:
                    count+=1
            if count > len(nums) // 3:
                res.append(key)
        return res

