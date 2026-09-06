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
        for i  in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return word[:i]
        return strs[0]