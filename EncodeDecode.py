class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0

        while i < len(s):

            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1
            
            length = int(length)
            res.append(s[i + 1 : i + 1 + length])
            i = i + 1 + length           


        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))