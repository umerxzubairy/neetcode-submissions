class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix = strs[0]
        # for i in range(1, len(strs)):
        #     j = 0
        #     while j < min(len(prefix), len(strs[i])):
        #         if strs[i][j] != prefix[j]:
        #             break
        #         j+=1
        #     prefix = prefix[:j]
        # return prefix
        i = 0
        for ch in strs[0]:
            for word in strs:
                if i == len(word) or word[i] != ch:
                    return word[:i]
            i+=1
        return strs[0]