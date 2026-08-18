class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        final = []
        for word in strs: 
            word_sorted = str(sorted(word))
            if word_sorted in answer: 
                answer[word_sorted].append(word)
            else: answer[word_sorted] = [word]
        for a in answer.values():
            final.append(a)
        return final