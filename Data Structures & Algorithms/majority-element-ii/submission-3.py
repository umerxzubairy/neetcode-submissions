class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # cnt1 = cnt2 = nums1 = nums2 = 0
        # for num in nums:
        #     if num == nums1:
        #         cnt1+=1
        #     elif num == nums2:
        #         cnt2+=1
        #     elif cnt1 == 0:
        #         cnt1 = 1
        #         nums1 = num
        #     elif cnt2 == 0:
        #         cnt2 = 1
        #         nums2 = num
        #     else:
        #         cnt1-=1
        #         cnt2-=1
        # cnt1 = cnt2 = 0
        # for num in nums:
        #     if num == nums1:
        #         cnt1+=1
        #     elif num == nums2:
        #         cnt2+=1
        # res = []
        # print(cnt1, cnt2, nums1, nums2)
        # if cnt1 > len(nums) // 3:
        #     res.append(nums1)
        # if cnt2 > len(nums) // 3:
        #     res.append(nums2)
        # return res

        dic = defaultdict(int)
        for num in nums:
            dic[num]+=1
            if len(dic) <= 2:
                continue
            newDic = defaultdict(int)
            for key, value in dic.items():
                if value > 1:
                    newDic[key] = value -1
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