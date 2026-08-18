class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for word in strs:
            msg = str(msg)+str(len(word))+"#"+str(word)
        print(msg)
        return msg

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length_word_tab = []
            while s[i] != "#":
                length_word_tab.append(s[i])
                i += 1
            length_word = int("".join(length_word_tab))
            word = s[i+1 : i+1+length_word]
            res.append(word)
            i += length_word+1
        return res
            
