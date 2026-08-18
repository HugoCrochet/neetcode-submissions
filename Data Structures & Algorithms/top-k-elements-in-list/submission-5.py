class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d: 
                d[num]+=1
            else: d[num] = 1
        result = sorted(d,key=lambda a: d[a], reverse=True)
        return result[:k]       