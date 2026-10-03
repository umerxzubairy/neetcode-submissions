
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return t;
        c1 = Counter(t)
        c2 = defaultdict(int)
        for key, value in c1.items():
            c2[key] = 0
        needed = len(c1)
        have = 0
        l = 0
        res = [-1, -1]
        maxLength = float('inf')
        for r in range(len(s)):
            if s[r] in c1:
                c2[s[r]]+=1
                if c2[s[r]] == c1[s[r]]:
                    have+=1
            while l <= r and have == needed:
                length = r-l+1
                if length < maxLength:
                    maxLength = length
                    res = [l, r]
                if s[l] in c1:
                    c2[s[l]]-=1
                    if c2[s[l]] < c1[s[l]]:
                        have-=1
                l+=1
        if res[0] == -1 and res[1] == -1:
            return ""
        return s[res[0]:res[1]+1]
                    
