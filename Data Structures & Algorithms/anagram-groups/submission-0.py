class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        if strs == [""] : return [[""]]
        dico = {}
        i = 0
        for word in strs:
            sorted_word = ''.join(sorted(word))
            print(word)
            print(sorted_word)
            if sorted_word not in dico:
                dico[sorted_word] = i
                res.append([word])
                i += 1
            else :
                res[dico[sorted_word]].append(word)
        return res






        