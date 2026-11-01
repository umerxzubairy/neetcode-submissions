'''
Problem Statement:
Input is a string `s` and an integer `k`, we can swap any character of `s` to any other upper case english character and we can only perform it `k` times.

we need to return the length of the longest substring containing the same letters throughout the string after performing the operation k times.


Clarifying Questions:
1. Do we have to perform the k operations or we can simply return without performing the operations if the string is the same?
you do not have to perform the k operations, thats the hard limits.

2. Can `k` be greater than `s`?
Yes. Assume k can be greater than the length of s.

Dry Run:
s = "AABABBA", k = 1

4-0+1 = 5
5 - 3 = 2 > k


Examples:

Approach:
Plan:
Code:
Dry Run:
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dic = defaultdict(int)
        maxFreq = 0
        res = float('-inf')
        for r in range(len(s)):
            dic[s[r]]+=1
            maxFreq = max(maxFreq, dic[s[r]])
            while (r - l +1 - maxFreq) > k:
                dic[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res