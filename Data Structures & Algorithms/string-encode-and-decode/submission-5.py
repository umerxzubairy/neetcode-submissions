class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append('#')
            res.append(word)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        l = 0
        r = 0
        res = []
        while r < len(s):
            if s[r] == '#':
                length = int(s[l:r])
                res.append(s[r+1: r+length+1])
                l = r+length+1
                r = r+length+1
            else:
                r+=1
        return res

1#a2#ab




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))