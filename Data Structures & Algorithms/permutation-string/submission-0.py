class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        def checkContains(count1, count2):
            for key, value in count1.items():
                if key not in count2:
                    return False
                if value != count2[key]:
                    return False
            return True
        c1 = Counter(s1)
        c2 = defaultdict(int)
        l = 0
        for r in range(len(s1)):
            c2[s2[r]]+=1
        
        if (checkContains(c1, c2)):
            return True
        for r in range(r+1, len(s2)):
            c2[s2[r]]+=1
            c2[s2[l]]-=1
            if (checkContains(c1, c2)):
                return True
            l+=1
        return False